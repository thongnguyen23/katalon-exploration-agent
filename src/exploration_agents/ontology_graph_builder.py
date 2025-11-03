"""Ontology-Based Graph Builder (library only)

Builds an ontology-aligned knowledge graph from Markdown (local dir or S3):
- Extract typed entities (rule-based first, optional LLM fallback)
- Generate candidate relations from structure/templates
- Validate against ontology, merge, weight, cap fanout with MMR
- Emit entities.jsonl, edges.jsonl, neighbors.jsonl, build_report.json, edges.rejected.jsonl

Use `python -m exploration_agents.builder_main` as the single entrypoint for
building graphs. This module exposes only the `build_graph(...)` function.
"""

from __future__ import annotations

import argparse
import dataclasses
import io
import json
import math
import os
import re
import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Tuple

import yaml  # type: ignore

from shared import get_env, get_env_bool, load_config


# ------------------------------
# Parsing helpers
# ------------------------------

HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<title>.+?)\s*$")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\((?P<href>[^)]+)\)")


@dataclass
class Section:
    level: int
    title: str
    anchor: str
    section_id: str  # e.g., docs.path.to.file.create-test-case


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def path_to_doc_id(root: str, path: str) -> str:
    rel = os.path.relpath(path, root)
    rel = rel.replace("\\", "/")
    if rel.endswith(".md"):
        rel = rel[:-3]
    parts = [p for p in rel.split("/") if p and p != "."]
    return ".".join(parts)


def join_section_id(doc_id: str, anchor_slug: Optional[str]) -> str:
    if not anchor_slug:
        return doc_id
    dotted = anchor_slug.replace("-", ".")
    dotted = re.sub(r"\.\.+", ".", dotted)
    return f"{doc_id}.{dotted}"


def parse_markdown(doc_id: str, content: str) -> Tuple[List[Section], List[Tuple[str, str]], List[str]]:
    """Parse headings, intra-doc links, and cross-doc links.

    Returns:
        sections: ordered list of Section
        see_also_edges: list of (src_section_id, dst_section_id)
        cross_doc_hrefs: list of hrefs that look like other docs (e.g., foo/bar.md#anchor)
    """
    sections: List[Section] = []
    see_also_edges: List[Tuple[str, str]] = []
    cross_doc_hrefs: List[str] = []

    current_section: Optional[Section] = None
    for line in content.splitlines():
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group("hashes"))
            title = m.group("title").strip()
            anchor = slugify(title)
            section_id = join_section_id(doc_id, anchor)
            sec = Section(level=level, title=title, anchor=anchor, section_id=section_id)
            sections.append(sec)
            current_section = sec
            continue

        for lm in MD_LINK_RE.finditer(line):
            href = lm.group("href")
            if href.startswith("#") and current_section:
                dst_anchor = href[1:]
                dst_section_id = join_section_id(doc_id, dst_anchor)
                see_also_edges.append((current_section.section_id, dst_section_id))
            else:
                # capture likely cross-doc hrefs that end with .md
                if ".md" in href and not href.startswith("http"):
                    cross_doc_hrefs.append(href)

    return sections, see_also_edges, cross_doc_hrefs


def iter_local_markdown(root_dir: str) -> Iterator[Tuple[str, str]]:
    for path in Path(root_dir).rglob("*.md"):
        if path.is_file():
            yield str(path), path.read_text(encoding="utf-8", errors="ignore")


def iter_s3_markdown(s3_prefix: str, region: Optional[str] = None) -> Iterator[Tuple[str, str]]:
    import boto3  # type: ignore

    region = region or get_env("AWS_REGION", "us-east-1")
    s3_client = boto3.client("s3", region_name=region)
    assert s3_prefix.startswith("s3://"), "S3 prefix must start with s3://"
    _, _, rest = s3_prefix.partition("s3://")
    bucket, _, prefix = rest.partition("/")
    continuation_token = None
    while True:
        kwargs = {"Bucket": bucket, "Prefix": prefix}
        if continuation_token:
            kwargs["ContinuationToken"] = continuation_token
        resp = s3_client.list_objects_v2(**kwargs)
        for obj in resp.get("Contents", []):
            key = obj["Key"]
            if not key.endswith(".md"):
                continue
            body = s3_client.get_object(Bucket=bucket, Key=key)["Body"].read()
            try:
                text = body.decode("utf-8")
            except Exception:
                text = body.decode("utf-8", errors="ignore")
            yield f"s3://{bucket}/{key}", text
        if resp.get("IsTruncated"):
            continuation_token = resp.get("NextContinuationToken")
        else:
            break


# ------------------------------
# Ontology & validation
# ------------------------------


@dataclass
class RelationRule:
    name: str
    from_types: Sequence[str]
    to_types: Sequence[str]
    default_weight: float
    acyclic: bool = False


@dataclass
class Ontology:
    version: str
    relation_weights: Dict[str, float]
    fanout_cap_per_rel: int
    mmr_lambda: float
    evidence_min: int
    require_sources: bool
    rules: Dict[str, RelationRule]

    @staticmethod
    def load(path: str) -> "Ontology":
        data = yaml.safe_load(open(path, "r", encoding="utf-8"))
        ranking = (data.get("ranking") or {}).get("defaults", {})
        rel_weights = ranking.get(
            "relation_weights",
            {"NEXT_STEP": 0.95, "DEPENDS_ON": 0.9, "USES": 0.85, "BELONGS_TO": 0.9, "TROUBLESHOOTS": 0.8, "SEE_ALSO": 0.7, "MENTIONED_IN": 0.6},
        )
        fanout = ranking.get("fanout_cap_per_rel", 20)
        mmr_lambda = ranking.get("mmr_lambda", 0.3)
        ev = data.get("evidence_policy", {})
        min_src = int(ev.get("min_sources_per_edge", 1))
        require_sources = bool(ev.get("require_sources_field", True))

        # Build relation rules; fall back to defaults from spec if missing
        spec_rules = {
            "BELONGS_TO": RelationRule("BELONGS_TO", ["Feature", "Concept", "HowTo", "API"], ["Product"], rel_weights.get("BELONGS_TO", 0.9)),
            "DEPENDS_ON": RelationRule("DEPENDS_ON", ["HowTo"], ["Concept", "Feature"], rel_weights.get("DEPENDS_ON", 0.9)),
            "NEXT_STEP": RelationRule("NEXT_STEP", ["HowTo"], ["HowTo"], rel_weights.get("NEXT_STEP", 0.95), acyclic=True),
            "USES": RelationRule("USES", ["HowTo", "Concept"], ["API", "Feature"], rel_weights.get("USES", 0.85)),
            "TROUBLESHOOTS": RelationRule("TROUBLESHOOTS", ["Troubleshooting"], ["HowTo", "Feature"], rel_weights.get("TROUBLESHOOTS", 0.8)),
            "SEE_ALSO": RelationRule("SEE_ALSO", ["Product", "Feature", "Concept", "HowTo", "API", "Troubleshooting"], ["Product", "Feature", "Concept", "HowTo", "API", "Troubleshooting"], rel_weights.get("SEE_ALSO", 0.7)),
            "MENTIONED_IN": RelationRule("MENTIONED_IN", ["Product", "Feature", "Concept", "HowTo", "API", "Troubleshooting"], ["Section"], rel_weights.get("MENTIONED_IN", 0.6)),
        }

        # If ontology file defines explicit rules, overlay weights/sets
        for r in (data.get("relations") or []):
            name = r.get("name") or r.get("id")
            if not name:
                continue
            spec_rules[name] = RelationRule(
                name=name,
                from_types=list(r.get("from", r.get("from_types", [])) or spec_rules.get(name, RelationRule(name, [], [], 0.5)).from_types),
                to_types=list(r.get("to", r.get("to_types", [])) or spec_rules.get(name, RelationRule(name, [], [], 0.5)).to_types),
                default_weight=float(r.get("weight", rel_weights.get(name, 0.7))),
                acyclic=bool(r.get("acyclic", spec_rules.get(name, RelationRule(name, [], [], 0.5)).acyclic)),
            )

        return Ontology(
            version=str(data.get("version", "0.0")),
            relation_weights=rel_weights,
            fanout_cap_per_rel=fanout,
            mmr_lambda=float(mmr_lambda),
            evidence_min=min_src,
            require_sources=require_sources,
            rules=spec_rules,
        )

    def allow(self, rel: str, from_type: str, to_type: str) -> bool:
        rule = self.rules.get(rel)
        if not rule:
            return False
        if from_type in rule.from_types or "any" in [t.lower() for t in rule.from_types]:
            if to_type in rule.to_types or "any" in [t.lower() for t in rule.to_types]:
                return True
        return False


# ------------------------------
# Entities & edges
# ------------------------------


@dataclass
class Entity:
    id: str
    type: str
    aliases: List[str]
    sources: List[str]


@dataclass
class Edge:
    src: str
    dst: str
    rel: str
    count: int
    sources: List[str]
    w: float = 0.0  # filled after merge/weighting


# ------------------------------
# Detection rules (rule-based first)
# ------------------------------


CREATE_PREFIXES = ("create", "run", "configure", "debug")


def detect_primary_entity(doc_path: str, title: str) -> Optional[Tuple[str, str]]:
    """Return (entity_name, type) for the doc-level entity, if any.

    Priority: HowTo/Troubleshooting/API/Concept/Feature > Product (folder-level context only).
    """
    slug = Path(doc_path).name.lower()
    parent_parts = Path(doc_path).parts

    # Troubleshooting by filename/title
    if any(x in slug for x in ("troubleshoot", "failed", "error")) or re.search(r"\b(Failed|Error|Troubleshooting)\b", title, re.I):
        return (title.strip(), "Troubleshooting")

    # API doc (rare as primary), but detect if title starts with WebUI./WS./Mobile.
    if re.match(r"^(WebUI|WS|Mobile)\.", title):
        return (title.strip(), "API")

    # HowTo patterns
    if re.match(r"^(Create|Run|Configure|Debug)\b", title):
        return (title.strip(), "HowTo")

    # Concepts
    if re.search(r"\b(Test\s*Case|Test\s*Suite|Test\s*Object|Object\s*Repository)\b", title, re.I):
        return (re.sub(r"\s+", " ", title).strip(), "Concept")

    # Features
    if re.search(r"\b(Smart\s*Wait|Object\s*Spy)\b", title, re.I):
        return (title.strip(), "Feature")

    # Product by folder prefix (fallback only if nothing else matched)
    lowered = "/".join(p.lower() for p in parent_parts)
    if "katalon-studio" in lowered:
        return ("Katalon Studio", "Product")
    if any(x in lowered for x in ("katalon-testops", "testops", "katalon-platform")):
        return ("TestOps", "Product")
    if "katalon-truetest" in lowered:
        return ("TrueTest", "Product")

    return None


def extract_api_mentions(text: str) -> List[str]:
    # Simple tokenization for API like WebUI.click, WS.sendRequest
    return sorted(set(re.findall(r"\b(?:WebUI|WS|Mobile)\.[A-Za-z_][A-Za-z0-9_]*", text)))


def extract_concept_mentions(text: str) -> List[str]:
    hits = []
    for kw in ["Test Case", "Test Suite", "Test Object", "Object Repository"]:
        if re.search(rf"\b{re.escape(kw)}\b", text, re.I):
            hits.append(kw)
    return sorted(set(hits))


# ------------------------------
# LLM fallback (optional, via LiteLLM)
# ------------------------------


def llm_entities(title: str, lead_text: str, provider: str, model: str, max_entities: int = 4) -> List[Tuple[str, str, List[str]]]:
    """Return list of (name, type, aliases) via LLM; tolerant of failures."""
    try:
        from litellm import completion  # type: ignore
    except Exception:
        return []

    sys_prompt = (
        "You extract entities from Katalon technical docs.\n"
        'Return JSON only. Allowed types: ["Product","Feature","Concept","HowTo","API","Troubleshooting"].\n'
        "Prefer entities helpful for guidance and next-step suggestions."
    )
    user_prompt = (
        f"TITLE: {title}\n"
        f"LEAD_TEXT: {lead_text}\n"
        'Return ≤4 entities following:\n{"entities":[{"name":"","type":"","evidence":"","aliases":[]}]}\n'
        "Rules:\n- WebUI.*, WS.* ⇒ API\n- Create/Run/Configure/Debug ⇒ HowTo\n- Test Case/Suite/Object ⇒ Concept\n- Smart Wait/Object Spy ⇒ Feature\n- Katalon Studio/TestOps ⇒ Product\n- Failed/Error ⇒ Troubleshooting"
    )
    try:
        resp = completion(
            model=model,
            messages=[{"role": "system", "content": sys_prompt}, {"role": "user", "content": user_prompt}],
            temperature=0.1,
            timeout=15,
            metadata={"provider": provider},
        )
        text = resp["choices"][0]["message"]["content"]
        obj = json.loads(text)
        out = []
        for e in (obj.get("entities") or [])[:max_entities]:
            name = str(e.get("name", "")).strip()
            et = str(e.get("type", "")).strip()
            aliases = [a for a in (e.get("aliases") or []) if isinstance(a, str)]
            if name and et:
                out.append((name, et, aliases))
        return out
    except Exception:
        return []


# ------------------------------
# Graph build
# ------------------------------


def now_utc_ts() -> float:
    return datetime.now(tz=timezone.utc).timestamp()


def exp_count_weight(default_w: float, count: int) -> float:
    return float(min(1.0, max(default_w, 1.0 - math.exp(-0.3 * max(0, count)))))


def runtime_score(rel_w: float, recency: float, popularity: float) -> float:
    return 0.7 * rel_w + 0.2 * recency + 0.1 * popularity


def jaccard(a: str, b: str) -> float:
    ta = set(re.split(r"[^a-z0-9]+", a.lower())) - {"", "md"}
    tb = set(re.split(r"[^a-z0-9]+", b.lower())) - {"", "md"}
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def mmr_select(candidates: List[Tuple[str, float]], k: int, lambda_: float) -> List[str]:
    """MMR over string ids only; diversity by id token overlap."""
    selected: List[str] = []
    cand = candidates[:]
    while cand and len(selected) < k:
        best_id = None
        best_score = -1e9
        for cid, base in cand:
            if not selected:
                score = base
            else:
                sim = max(jaccard(cid, s) for s in selected)
                score = lambda_ * base - (1 - lambda_) * sim
            if score > best_score:
                best_score = score
                best_id = cid
        assert best_id is not None
        selected.append(best_id)
        cand = [(cid, w) for cid, w in cand if cid != best_id]
    return selected


def build_graph(
    source: str,
    ontology_path: str,
    emit_entities: str,
    emit_edges: str,
    emit_neighbors: str,
    synonyms_json: Optional[str] = None,
    product_map_yaml: Optional[str] = None,
    entity_whitelist: Optional[str] = None,
    enable_llm_entity: bool = False,
    llm_provider: Optional[str] = None,
    llm_model: Optional[str] = None,
    fanout_cap: Optional[int] = None,
    mmr_lambda: Optional[float] = None,
) -> Dict[str, object]:
    # Config must come from environment; do not load .env here.
    t0 = time.time()

    ontology = Ontology.load(ontology_path)
    if fanout_cap is None:
        fanout_cap = ontology.fanout_cap_per_rel
    if mmr_lambda is None:
        mmr_lambda = ontology.mmr_lambda

    synonyms: Dict[str, List[str]] = {}
    if synonyms_json and Path(synonyms_json).exists():
        synonyms = json.loads(Path(synonyms_json).read_text(encoding="utf-8"))

    product_map: Dict[str, str] = {}
    if product_map_yaml and Path(product_map_yaml).exists():
        product_map = yaml.safe_load(Path(product_map_yaml).read_text(encoding="utf-8")) or {}

    whitelist: Optional[set[str]] = None
    if entity_whitelist and Path(entity_whitelist).exists():
        whitelist = set(
            s.strip() for s in Path(entity_whitelist).read_text(encoding="utf-8").splitlines() if s.strip() and not s.strip().startswith("#")
        )

    os.makedirs(os.path.dirname(emit_entities) or ".", exist_ok=True)
    os.makedirs(os.path.dirname(emit_edges) or ".", exist_ok=True)
    os.makedirs(os.path.dirname(emit_neighbors) or ".", exist_ok=True)

    # Pass 1: iterate docs, detect entities/mentions, collect structural edges
    entities: Dict[str, Entity] = {}
    primary_for_doc: Dict[str, str] = {}  # doc_id -> entity_id
    entity_types: Dict[str, str] = {}
    mention_edges: List[Edge] = []
    see_also_edges: List[Edge] = []
    next_candidates_per_dir: Dict[str, List[Tuple[str, str]]] = defaultdict(list)  # dir -> [(doc_id, title)]
    file_mtime: Dict[str, float] = {}

    if source.startswith("s3://"):
        iterator = iter_s3_markdown(source)
        doc_root = source
        is_s3 = True
    else:
        iterator = iter_local_markdown(source)
        doc_root = source
        is_s3 = False

    for path, text in iterator:
        if is_s3:
            # derive doc_id relative to provided prefix
            _, _, rest = doc_root.partition("s3://")
            bucket_root, _, prefix_root = rest.partition("/")
            rel_doc_path = path.split(f"s3://{bucket_root}/", 1)[-1]
            if rel_doc_path.startswith(prefix_root):
                rel_doc_path = rel_doc_path[len(prefix_root) :].lstrip("/")
            doc_id = ".".join([p for p in rel_doc_path.replace("\\", "/").split("/") if p]).removesuffix(".md")
        else:
            doc_id = path_to_doc_id(doc_root, path)

        # mtime for recency
        try:
            mtime = Path(path).stat().st_mtime
        except Exception:
            mtime = now_utc_ts()
        file_mtime[doc_id] = mtime

        sections, see_intra, cross_hrefs = parse_markdown(doc_id, text)
        title = sections[0].title if sections else Path(path).stem.replace("-", " ")

        # Collect for NEXT_STEP heuristics (by directory)
        parent_dir = str(Path(doc_id).parent)
        next_candidates_per_dir[parent_dir].append((doc_id, title))

        # Primary entity detection
        pe = detect_primary_entity(path, title) or (None if not enable_llm_entity else None)
        if pe is None and enable_llm_entity:
            lead = "\n".join(text.splitlines()[:4])
            llm_out = llm_entities(title, lead, llm_provider or "openai", llm_model or "gpt-4o-mini")
            if llm_out:
                name, ety, aliases = llm_out[0]
                pe = (name, ety)
        if pe is not None:
            name, etype = pe
            ent_id = name
            if whitelist and ent_id not in whitelist:
                pass
            else:
                ent = entities.get(ent_id)
                aliases = list(set([ent_id] + synonyms.get(ent_id, [])))
                if ent is None:
                    ent = Entity(id=ent_id, type=etype, aliases=aliases, sources=[doc_id])
                    entities[ent_id] = ent
                    entity_types[ent_id] = etype
                else:
                    # merge sources
                    if doc_id not in ent.sources:
                        ent.sources.append(doc_id)
                primary_for_doc[doc_id] = ent_id

        # API + Concept mentions → entities + MENTIONED_IN
        for api in extract_api_mentions(text):
            if whitelist and api not in whitelist:
                continue
            if api not in entities:
                entities[api] = Entity(id=api, type="API", aliases=[api] + synonyms.get(api, []), sources=[doc_id])
                entity_types[api] = "API"
            else:
                if doc_id not in entities[api].sources:
                    entities[api].sources.append(doc_id)
            # link to doc root section as evidence
            mention_edges.append(Edge(src=api, dst=doc_id, rel="MENTIONED_IN", count=1, sources=[f"doc:{doc_id}"]))

        for concept in extract_concept_mentions(text):
            if whitelist and concept not in whitelist:
                continue
            if concept not in entities:
                entities[concept] = Entity(id=concept, type="Concept", aliases=[concept] + synonyms.get(concept, []), sources=[doc_id])
                entity_types[concept] = "Concept"
            else:
                if doc_id not in entities[concept].sources:
                    entities[concept].sources.append(doc_id)
            mention_edges.append(Edge(src=concept, dst=doc_id, rel="MENTIONED_IN", count=1, sources=[f"doc:{doc_id}"]))

        # SEE_ALSO (intra)
        for src, dst in see_intra:
            see_also_edges.append(Edge(src=src, dst=dst, rel="SEE_ALSO", count=1, sources=[f"doc:{doc_id}"]))

        # SEE_ALSO (cross-doc)
        for href in cross_hrefs:
            # tolerate ./relative.md or ../path/file.md#anchor
            clean = href.split("#")[0]
            clean = clean.lstrip("./")
            clean = clean[:-3] if clean.endswith(".md") else clean
            # map to doc ids (join '.' separator)
            target_id = ".".join([p for p in clean.replace("\\", "/").split("/") if p])
            if target_id:
                see_also_edges.append(Edge(src=doc_id, dst=target_id, rel="SEE_ALSO", count=1, sources=[f"link:{href}"]))

    total_files = len(primary_for_doc) if primary_for_doc else sum(1 for _ in Path(source).rglob("*.md")) if not source.startswith("s3://") else len(file_mtime)

    # Pass 2: candidate relations
    edge_bag: Dict[Tuple[str, str, str], Edge] = {}
    rejected: List[Edge] = []

    def add_edge(src: str, dst: str, rel: str, src_evidence: str) -> None:
        key = (src, dst, rel)
        e = edge_bag.get(key)
        if e is None:
            edge_bag[key] = Edge(src=src, dst=dst, rel=rel, count=1, sources=[src_evidence])
        else:
            e.count += 1
            if src_evidence not in e.sources:
                e.sources.append(src_evidence)

    # BELONGS_TO: primary entities to products (by path or product_map)
    for doc_id, ent_id in primary_for_doc.items():
        etype = entity_types.get(ent_id, "")
        # find product from doc path mapping hints
        prod: Optional[str] = None
        # product_map can map prefixes to product names
        for pref, prod_name in product_map.items():
            if doc_id.replace(".", "/").startswith(pref.strip("/")):
                prod = prod_name
                break
        # fallback by folder heuristics
        if not prod:
            if "katalon-studio" in doc_id:
                prod = "Katalon Studio"
            elif any(x in doc_id for x in ("testops", "katalon-platform")):
                prod = "TestOps"
        if prod and etype in ("Feature", "Concept", "HowTo", "API"):
            # ensure product entity exists
            if prod not in entities:
                entities[prod] = Entity(id=prod, type="Product", aliases=[prod] + synonyms.get(prod, []), sources=[doc_id])
                entity_types[prod] = "Product"
            add_edge(ent_id, prod, "BELONGS_TO", f"doc:{doc_id}")

    # USES: from primary (HowTo/Concept) to API mentions in same doc
    for doc_id, ent_id in primary_for_doc.items():
        etype = entity_types.get(ent_id, "")
        if etype not in ("HowTo", "Concept"):
            continue
        # gather API entities that cite this doc as source
        for api_id, e in entities.items():
            if e.type == "API" and doc_id in e.sources:
                add_edge(ent_id, api_id, "USES", f"doc:{doc_id}")

    # DEPENDS_ON: HowTo depends on Concept mentioned in same doc
    for doc_id, ent_id in primary_for_doc.items():
        etype = entity_types.get(ent_id, "")
        if etype != "HowTo":
            continue
        for cid, e in entities.items():
            if e.type == "Concept" and doc_id in e.sources:
                add_edge(ent_id, cid, "DEPENDS_ON", f"doc:{doc_id}")

    # TROUBLESHOOTS: Troubleshooting pages reference primary HowTo/Feature in same folder
    dir_to_primary: Dict[str, List[str]] = defaultdict(list)
    for doc_id, ent_id in primary_for_doc.items():
        dir_to_primary[str(Path(doc_id).parent)].append(ent_id)
    for doc_id, ent_id in primary_for_doc.items():
        if entity_types.get(ent_id) != "Troubleshooting":
            continue
        for target in dir_to_primary.get(str(Path(doc_id).parent), []):
            if entity_types.get(target) in ("HowTo", "Feature"):
                add_edge(ent_id, target, "TROUBLESHOOTS", f"doc:{doc_id}")

    # NEXT_STEP: from Create -> Run/Configure/Debug for similar titles within directory
    for directory, items in next_candidates_per_dir.items():
        # items: [(doc_id, title)]
        creates = [(d, t) for d, t in items if re.match(r"^Create\b", t)]
        runs = [(d, t) for d, t in items if re.match(r"^(Run|Configure|Debug)\b", t)]
        for d1, t1 in creates:
            for d2, t2 in runs:
                # if share a main object (e.g., Test Case/Test Suite), connect
                if jaccard(t1, t2) >= 0.2:
                    src_ent = primary_for_doc.get(d1)
                    dst_ent = primary_for_doc.get(d2)
                    if src_ent and dst_ent and entity_types.get(src_ent) == "HowTo" and entity_types.get(dst_ent) == "HowTo":
                        add_edge(src_ent, dst_ent, "NEXT_STEP", f"dir:{directory}")

    # Include gathered SEE_ALSO and MENTIONED_IN edges
    for e in see_also_edges + mention_edges:
        key = (e.src, e.dst, e.rel)
        cur = edge_bag.get(key)
        if cur is None:
            edge_bag[key] = e
        else:
            cur.count += e.count
            for s in e.sources:
                if s not in cur.sources:
                    cur.sources.append(s)

    # Validation: enforce from→to types per ontology; normalize direction if needed
    def entity_type(ent_id: str) -> str:
        if ent_id in entity_types:
            return entity_types[ent_id]
        # section ids are treated as "Section"
        if re.search(r"\.[a-z0-9]+(\.|$)", ent_id) or "/" in ent_id or ent_id.count(".") >= 1 and ent_id not in entities:
            return "Section"
        # default to Concept for unknown (conservative)
        return "Concept"

    validated: Dict[Tuple[str, str, str], Edge] = {}
    for (src, dst, rel), e in list(edge_bag.items()):
        ft, tt = entity_type(src), entity_type(dst)
        if ontology.allow(rel, ft, tt):
            validated[(src, dst, rel)] = e
        else:
            rejected.append(e)

    # Merge duplicates already done; Weighting
    for e in validated.values():
        default_w = ontology.rules.get(e.rel, RelationRule(e.rel, [], [], 0.7)).default_weight
        e.w = exp_count_weight(default_w, e.count)

    # NEXT_STEP cycle detection (simple DFS); drop edges if cycles found
    if ontology.rules["NEXT_STEP"].acyclic:
        adj: Dict[str, List[str]] = defaultdict(list)
        for (s, d, r), e in validated.items():
            if r == "NEXT_STEP":
                adj[s].append(d)

        temp, perm = set(), set()
        cycle_edges: List[Tuple[str, str]] = []

        def dfs(u: str, stack: List[str]) -> None:
            if u in perm:
                return
            if u in temp:
                # cycle: stack ... u -> u
                if stack:
                    cycle_edges.append((stack[-1], u))
                return
            temp.add(u)
            for v in adj.get(u, []):
                dfs(v, stack + [u])
            temp.remove(u)
            perm.add(u)

        for node in list(adj.keys()):
            dfs(node, [])
        # remove edges that close cycles
        for s, d in cycle_edges:
            e = validated.pop((s, d, "NEXT_STEP"), None)
            if e:
                rejected.append(e)

    # Fanout cap + neighbors.jsonl with runtime scoring
    neighbors_records: List[dict] = []
    edges_by_src_rel: Dict[Tuple[str, str], List[Edge]] = defaultdict(list)
    for (s, d, r), e in validated.items():
        edges_by_src_rel[(s, r)].append(e)

    # recency/popularity per edge
    def recency_for_edge(e: Edge) -> float:
        # Use most recent doc mtime from sources with prefix doc:
        mts = []
        for s in e.sources:
            if s.startswith("doc:"):
                doc = s.split(":", 1)[1]
                mts.append(file_mtime.get(doc, now_utc_ts()))
        if not mts:
            return 0.0
        newest = max(mts)
        days = max(0.0, (now_utc_ts() - newest) / 86400.0)
        return float(math.exp(-days / 365.0))  # ~1.0 within a year

    def popularity_for_edge(e: Edge) -> float:
        return min(1.0, math.log(1.0 + float(e.count), 10.0))

    # Per (src,rel) cap + MMR, then group for neighbors
    neighbors_map: Dict[str, List[Tuple[str, str, float]]] = defaultdict(list)
    for (src, rel), lst in edges_by_src_rel.items():
        # base candidate score = edge weight; will turn into runtime_score
        cand = [(e.dst, e.w) for e in lst]
        # sort by w desc for stable MMR
        cand.sort(key=lambda x: -x[1])
        sel_ids = mmr_select(cand, min(fanout_cap, len(cand)), float(mmr_lambda))
        # compute runtime score
        for dst in sel_ids:
            e = next(x for x in lst if x.dst == dst)
            rel_w = ontology.relation_weights.get(rel, e.w)
            rec = recency_for_edge(e)
            pop = popularity_for_edge(e)
            score = runtime_score(rel_w, rec, pop)
            neighbors_map[src].append((dst, rel, float(score)))

    for src, neigh in neighbors_map.items():
        # sort by score desc, stable by rel priority
        priority = {"NEXT_STEP": 0, "DEPENDS_ON": 1, "USES": 1, "TROUBLESHOOTS": 2, "SEE_ALSO": 3, "BELONGS_TO": 4}
        neigh.sort(key=lambda t: (priority.get(t[1], 9), -t[2], t[0]))
        neighbors_records.append({"id": src, "neighbors": [{"id": d, "rel": r, "w": round(w, 4)} for d, r, w in neigh]})

    # Orphans
    all_nodes = set()
    has_edge = set()
    for (s, d, r) in validated.keys():
        all_nodes.add(s)
        all_nodes.add(d)
        has_edge.add(s)
        has_edge.add(d)
    orphans = [n for n in all_nodes if n not in has_edge]
    orphans_pct = (len(orphans) / max(1, len(all_nodes))) * 100.0

    # Coverage: files with ≥ 1 entity
    files_with_entity = set()
    for e in entities.values():
        files_with_entity.update(e.sources)
    coverage = (len(files_with_entity) / max(1, (len(file_mtime) or total_files))) * 100.0

    # Emit
    with io.open(emit_entities, "w", encoding="utf-8") as f:
        for e in entities.values():
            f.write(json.dumps(dataclasses.asdict(e), ensure_ascii=False) + "\n")
    with io.open(emit_edges, "w", encoding="utf-8") as f:
        for (s, d, r), e in validated.items():
            f.write(
                json.dumps({"src": s, "dst": d, "rel": r, "w": round(e.w, 4), "count": e.count, "sources": e.sources}, ensure_ascii=False)
                + "\n"
            )
    if rejected:
        rej_path = os.path.join(os.path.dirname(emit_edges), "edges.rejected.jsonl")
        with io.open(rej_path, "w", encoding="utf-8") as f:
            for e in rejected:
                f.write(
                    json.dumps({"src": e.src, "dst": e.dst, "rel": e.rel, "count": e.count, "sources": e.sources}, ensure_ascii=False)
                    + "\n"
                )
    with io.open(emit_neighbors, "w", encoding="utf-8") as f:
        for rec in neighbors_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    t1 = time.time()
    report = {
        "version": "0.2",
        "ontology_version": ontology.version,
        "inputs": {"source": source, "ontology": ontology_path},
        "counts": {
            "entities": len(entities),
            "edges": len(validated),
            "rejected": len(rejected),
            "files": len(file_mtime) or total_files,
        },
        "coverage_pct": round(coverage, 2),
        "orphans_pct": round(orphans_pct, 2),
        "params": {"fanout_cap": fanout_cap, "mmr_lambda": mmr_lambda},
        "violations": {
            "coverage_below_90": coverage < 90.0,
            "orphans_over_1pct": orphans_pct >= 1.0,
        },
        "timing_sec": round(t1 - t0, 3),
    }
    report_path = os.path.join(os.path.dirname(emit_edges) or ".", "build_report.json")
    with io.open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    return report


# CLI removed; use exploration_agents.builder_main as the single entrypoint.
