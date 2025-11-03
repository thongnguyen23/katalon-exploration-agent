from __future__ import annotations

import collections
import io
import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import yaml  # type: ignore

from shared import load_config, get_env
from shared.config import get_env_bool
from exploration_agents.kb_retriever import kb_search
from exploration_agents.section_resolver import section_snippet_from_text


# ------------------------------
# Utilities
# ------------------------------


def _now_ms() -> int:
    return int(time.perf_counter() * 1000)


def _jaccard(a: str, b: str) -> float:
    sa = set(a.lower().split())
    sb = set(b.lower().split())
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def _seq_ratio(a: str, b: str) -> float:
    from difflib import SequenceMatcher

    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def _doc_path_from_section_id(section_id: str) -> Optional[Tuple[str, Path]]:
    # Try to map a section_id to a local markdown file under in_full/ or in/
    segs = section_id.split(".")
    for i in range(len(segs), 0, -1):
        cand_doc = ".".join(segs[:i])
        rel = cand_doc.replace(".", "/") + ".md"
        for root in ("in_full", "in"):
            p = Path(root) / rel
            if p.exists():
                return cand_doc, p
    return None


def _read_file_text(p: Path) -> Optional[str]:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        try:
            return p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return None


def _relation_priority(rel: str) -> int:
    order = {
        "NEXT_STEP": 0,
        "DEPENDS_ON": 1,
        "USES": 1,
        "TROUBLESHOOTS": 2,
        "SEE_ALSO": 3,
        "BELONGS_TO": 4,
        "MENTIONED_IN": 5,
    }
    return order.get(rel, 9)


def _default_rel_weights() -> Dict[str, float]:
    return {
        "NEXT_STEP": 0.95,
        "DEPENDS_ON": 0.90,
        "USES": 0.85,
        "BELONGS_TO": 0.90,
        "TROUBLESHOOTS": 0.80,
        "SEE_ALSO": 0.70,
        "MENTIONED_IN": 0.60,
    }


def _load_ontology_weights(path: str) -> Tuple[Dict[str, float], int, float]:
    try:
        with io.open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        ranking = (data.get("ranking") or {}).get("defaults", {})
        rel_weights = ranking.get("relation_weights", _default_rel_weights())
        fanout = int(ranking.get("fanout_cap_per_rel", 20))
        mmr_lambda = float(ranking.get("mmr_lambda", 0.3))
        return dict(rel_weights), fanout, mmr_lambda
    except Exception:
        return _default_rel_weights(), 20, 0.3


def _mmr_select(candidates: List[Tuple[str, float]], k: int, lambda_: float) -> List[str]:
    selected: List[str] = []
    pool = candidates[:]
    while pool and len(selected) < k:
        best_id = None
        best_score = -1e9
        for cid, base in pool:
            if not selected:
                score = base
            else:
                sim = max(_jaccard(cid, x) for x in selected)
                score = lambda_ * base - (1 - lambda_) * sim
            if score > best_score:
                best_score = score
                best_id = cid
        selected.append(best_id)  # type: ignore[arg-type]
        pool = [(cid, sc) for cid, sc in pool if cid != best_id]
    return selected


# ------------------------------
# Graph Index
# ------------------------------


@dataclass
class Entity:
    id: str
    type: str
    aliases: List[str]
    sources: List[str]


class GraphIndex:
    def __init__(self, graph_dir: str, entities_file: str, neighbors_file: str):
        self.graph_dir = graph_dir
        self.entities_file = Path(graph_dir) / entities_file
        self.neighbors_file = Path(graph_dir) / neighbors_file

        self.entities_by_id: Dict[str, Entity] = {}
        self.alias_index: Dict[str, set[str]] = collections.defaultdict(set)
        self.neighbors_idx: Dict[str, List[Dict[str, Any]]] = {}
        # reverse MENTIONED_IN: section_id -> [entity_id]
        self.mentioned_in_rev: Dict[str, List[str]] = collections.defaultdict(list)

    def load(self) -> None:
        # entities
        if self.entities_file.exists():
            with io.open(self.entities_file, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    obj = json.loads(line)
                    e = Entity(
                        id=obj["id"],
                        type=obj.get("type", ""),
                        aliases=[a for a in obj.get("aliases", []) if isinstance(a, str)],
                        sources=[s for s in obj.get("sources", []) if isinstance(s, str)],
                    )
                    self.entities_by_id[e.id] = e
                    for al in set([e.id] + e.aliases):
                        self.alias_index[al.lower()].add(e.id)

        # neighbors
        if self.neighbors_file.exists():
            with io.open(self.neighbors_file, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    obj = json.loads(line)
                    nid = obj["id"]
                    neigh = obj.get("neighbors", []) or []
                    norm = []
                    for n in neigh:
                        nid2 = n.get("id")
                        rel = n.get("rel")
                        w = float(n.get("w", 0.0))
                        if nid2 and rel:
                            norm.append({"id": nid2, "rel": rel, "w": w})
                            # Build reverse MENTIONED_IN index
                            if rel == "MENTIONED_IN":
                                self.mentioned_in_rev[nid2].append(nid)
                    self.neighbors_idx[nid] = norm

    def product_of(self, entity_id: str) -> Optional[str]:
        # Direct product
        ent = self.entities_by_id.get(entity_id)
        if ent and ent.type == "Product":
            return ent.id
        # Graph BELONGS_TO
        for n in self.neighbors_idx.get(entity_id, []):
            if n.get("rel") == "BELONGS_TO":
                return n.get("id")
        # Infer from doc_id prefix
        root = (entity_id.split(".")[0] if "." in entity_id else entity_id).lower()
        if root.startswith("katalon-studio"):
            return "Katalon Studio"
        if any(x in entity_id.lower() for x in ("katalon-platform", "testops")):
            return "TestOps"
        if root.startswith("katalon-truetest"):
            return "TrueTest"
        if root.startswith("katalon-testcloud"):
            return "TestCloud"
        return None

    def in_scope(self, entity_id: str, product_scope: Optional[str]) -> bool:
        if not product_scope:
            return True
        p = self.product_of(entity_id)
        return (p == product_scope) or (entity_id == product_scope)


# ------------------------------
# KB Section Provider with TTL cache
# ------------------------------


class TTLCache:
    def __init__(self, ttl_sec: int):
        self.ttl_ms = int(ttl_sec * 1000)
        self.store: Dict[str, Tuple[int, Any]] = {}

    def get(self, key: str) -> Optional[Any]:
        ent = self.store.get(key)
        if not ent:
            return None
        ts, val = ent
        if _now_ms() - ts > self.ttl_ms:
            self.store.pop(key, None)
            return None
        return val

    def set(self, key: str, val: Any) -> None:
        self.store[key] = (_now_ms(), val)


class SectionProviderKB:
    def __init__(self, endpoint: str | None, index: str | None, topk: int, ttl_sec: int = 60):
        self.endpoint = endpoint or "bedrock"
        self.index = index or os.getenv("KB_ID") or os.getenv("KNOWLEDGE_BASE_ID") or ""
        self.default_topk = topk
        self.cache_topk = TTLCache(ttl_sec)
        self.cache_by_entity = TTLCache(max(300, ttl_sec * 5))

    def topk(self, query: str, k: Optional[int] = None) -> Tuple[List[Dict[str, Any]], int]:
        key = f"q::{query.strip().lower()}::{k or self.default_topk}"
        cached = self.cache_topk.get(key)
        if cached is not None:
            return cached

        # Local/demo mode: search local markdown sections instead of Bedrock KB
        if (self.endpoint or "").lower() == "local":
            hits, elapsed = self._local_topk(query, k or self.default_topk)
            out = (hits, elapsed)
            self.cache_topk.set(key, out)
            return out

        timeout_ms = int(os.getenv("KB_TIMEOUT_MS", "1100"))
        t0 = _now_ms()
        try:
            hits, tta_ms = kb_search(query, top_k=k or self.default_topk)
        except Exception:
            last = self.cache_topk.get(key)
            if last is not None:
                return last
            raise
        elapsed = _now_ms() - t0
        if elapsed > timeout_ms:
            # Return from cache if available
            last = self.cache_topk.get(key)
            if last is not None:
                return last

        norm_hits: List[Dict[str, Any]] = []
        for h in hits:
            # Normalize to {id, doc_id, title, text, score}
            # We infer doc_id by looking up local file for the resolved section.
            text = ""
            content = h.get("content")
            if isinstance(content, dict):
                text = content.get("text") or ""
            elif isinstance(content, list) and content and isinstance(content[0], dict):
                text = content[0].get("text") or ""

            # Resolve section_id by fetching local/s3 content through existing logic
            from exploration_agents.section_resolver import resolve_section_id

            try:
                sec_id, _conf, _reason = resolve_section_id(h)
            except Exception:
                continue
            if not sec_id:
                continue
            # derive doc_id by scanning local paths
            doc = _doc_path_from_section_id(sec_id)
            doc_id = doc[0] if doc else None
            title = None
            if doc:
                md = _read_file_text(doc[1])
                if md:
                    # extract a snippet and best-effort title (first heading matching section)
                    snippet = section_snippet_from_text(doc[0], sec_id, md, max_len=220)
                    text = snippet or text
                    # best-effort title = last token of section_id after doc prefix, prettified
                    anchor = sec_id[len(doc[0]) + 1 :] if sec_id.startswith(doc[0] + ".") else sec_id
                    title = anchor.replace(".", " ").strip().title()

            norm_hits.append(
                {
                    "id": sec_id,
                    "doc_id": doc_id or sec_id,
                    "title": title or "",
                    "text": text or "",
                    "score": float(h.get("score", h.get("relevanceScore", 0.0)) or 0.0),
                }
            )

        out = (norm_hits, elapsed)
        self.cache_topk.set(key, out)
        return out

    def _local_topk(self, query: str, k: int) -> Tuple[List[Dict[str, Any]], int]:
        # Lightweight local search over markdown files for demo/offline usage
        from exploration_agents.section_resolver import _parse_sections

        roots: List[str] = []
        env_dir = os.getenv("LOCAL_DOCS_DIR")
        if env_dir:
            roots.append(env_dir)
        for d in ("in_full", "in", "specs/ontology/demo_docs"):
            if d not in roots:
                roots.append(d)

        t0 = _now_ms()
        hits: List[Dict[str, Any]] = []
        q = (query or "").strip()
        for root in roots:
            if not os.path.isdir(root):
                continue
            for dirpath, _, filenames in os.walk(root):
                for fn in filenames:
                    if not fn.endswith(".md"):
                        continue
                    full = os.path.join(dirpath, fn)
                    rel = os.path.relpath(full, root).replace("\\", "/")
                    doc_id = ".".join([p for p in rel[:-3].split("/") if p])
                    md = _read_file_text(Path(full)) or ""
                    if not md:
                        continue
                    for sid, body in _parse_sections(doc_id, md):
                        text = (body or "").strip()
                        score = 0.0
                        hay = (doc_id + " " + text).lower()
                        if q and q.lower() in hay:
                            score += 0.5
                        score += 0.5 * _seq_ratio(q, hay[:500])
                        if score <= 0.1:
                            continue
                        tail = sid[len(doc_id) + 1 :] if sid.startswith(doc_id + ".") else sid
                        title = tail.replace(".", " ").strip().title()
                        hits.append({
                            "id": sid,
                            "doc_id": doc_id,
                            "title": title,
                            "text": text[:220],
                            "score": score,
                        })
        hits.sort(key=lambda h: float(h.get("score", 0.0)), reverse=True)
        return hits[:k], _now_ms() - t0

    def by_entity(self, entity_id: str, index: GraphIndex, limit: int = 1, query_context: Optional[str] = None) -> List[str]:
        key = f"e::{entity_id}::{limit}"
        cached = self.cache_by_entity.get(key)
        if cached is not None:
            return cached

        # Try KB search first (more likely to return a precise section), then fall back to sources
        e = index.entities_by_id.get(entity_id)
        out: List[str] = []
        phrases: List[str] = []
        if e:
            phrases = [e.id] + [a for a in e.aliases if isinstance(a, str)]
        else:
            phrases = [entity_id]
        # Include a context-augmented phrase if provided
        if query_context:
            q = query_context.strip()
            for p in phrases[:2]:
                phrases.append(f"{p} {q}")
        # KB search attempt
        for ph in phrases:
            hits, _ = self.topk(ph, k=5)
            for h in hits[:2]:
                sid = h.get("id")
                if sid and sid not in out:
                    out.append(sid)
                if len(out) >= limit:
                    break
            if len(out) >= limit:
                break
        # Fallback to sources from entities.jsonl
        if len(out) < limit and e and e.sources:
            for doc_id in e.sources:
                from exploration_agents.neighbors import first_section_for_doc
                sid = first_section_for_doc(doc_id) or doc_id
                if sid not in out:
                    out.append(sid)
                if len(out) >= limit:
                    break

        self.cache_by_entity.set(key, out)
        return out


# ------------------------------
# Engine
# ------------------------------


class RetrieveEngine:
    def __init__(self, provider: SectionProviderKB, g: GraphIndex, ontology_path: str, limit: int = 5):
        self.provider = provider
        self.g = g
        self.limit = limit
        self.rel_w, self.fanout_cap, self.mmr_lambda = _load_ontology_weights(ontology_path)
        self.strict_scope = get_env_bool("STRICT_PRODUCT_SCOPE", False)

    def _rel_weight(self, rel: str) -> float:
        return float(self.rel_w.get(rel, _default_rel_weights().get(rel, 0.7)))

    def _majority_product(self, entities: List[str]) -> Optional[str]:
        if not entities:
            return None
        prod = [e for e in entities if (self.g.entities_by_id.get(e) or Entity(e, "", [], [])).type == "Product"]
        if not prod:
            return None
        # majority threshold > 50%
        cnt = collections.Counter(prod)
        top_prod, top_n = cnt.most_common(1)[0]
        return top_prod if top_n > len(entities) / 2 else None

    def _alias_guess(self, text: str) -> List[str]:
        found: set[str] = set()
        t = (text or "").lower()
        for al, ids in self.g.alias_index.items():
            if al in t or _seq_ratio(al, t) >= 0.86:
                found.update(ids)
        return list(found)

    def _dedupe_by_doc(self, sec_ids: List[str]) -> List[str]:
        seen_doc: set[str] = set()
        out: List[str] = []
        for sid in sec_ids:
            got = _doc_path_from_section_id(sid)
            doc_id = got[0] if got else sid
            if doc_id in seen_doc:
                continue
            seen_doc.add(doc_id)
            out.append(sid)
            if len(out) >= self.limit:
                break
        return out

    def _render_preview(self, query: str, main_sections: List[str], hits_map: Dict[str, Dict[str, Any]]) -> str:
        lines = [f"Q: {query}"]
        for i, sid in enumerate(main_sections, 1):
            h = hits_map.get(sid, {})
            title = h.get("title") or sid.split(".")[-1].replace("-", " ").title()
            text = (h.get("text") or "").strip()
            if len(text) > 220:
                text = text[:219] + "…"
            lines.append(f"{i}) {title} [section:{sid}] {text}")
        return "\n".join(lines)

    def run(self, query: str) -> Dict[str, Any]:
        # KB search
        hits, tta_ms = self.provider.topk(query, k=self.limit * 4)
        hits_map = {h["id"]: h for h in hits}

        # Dedupe by doc
        main_sections = self._dedupe_by_doc([h["id"] for h in hits])

        # Seeds via reverse MENTIONED_IN else alias (include query aliases to avoid product-only seeds)
        seed_counts: Dict[str, int] = collections.Counter()
        for sid in main_sections:
            for eid in self.g.mentioned_in_rev.get(sid, []):
                seed_counts[eid] += 1
            if not self.g.mentioned_in_rev.get(sid):
                text = (hits_map.get(sid, {}).get("title", "") + " " + hits_map.get(sid, {}).get("text", "")[:300])
                for eid in self._alias_guess(text):
                    seed_counts[eid] += 1
        # Also mine aliases directly from the user query
        for eid in self._alias_guess(query):
            seed_counts[eid] += 1
        # Prefer non-Product seeds when available
        type_bias = {"HowTo": 3, "Concept": 2, "Feature": 2, "API": 1.5, "Product": 1}
        def _score_seed(eid: str) -> float:
            et = (self.g.entities_by_id.get(eid) or Entity(eid, "", [], [])).type
            return seed_counts[eid] * type_bias.get(et, 1)
        seeds = sorted(seed_counts.keys(), key=_score_seed, reverse=True)[:3]
        # Ensure at least one non-Product if available
        if seeds and all((self.g.entities_by_id.get(s) or Entity(s, "", [], [])).type == "Product" for s in seeds):
            non_prod = [s for s in seed_counts.keys() if (self.g.entities_by_id.get(s) or Entity(s, "", [], [])).type != "Product"]
            if non_prod:
                seeds = [non_prod[0]] + seeds[:2]
        if not seeds:
            # fallback: choose a common Product if any
            products = [e.id for e in self.g.entities_by_id.values() if e.type == "Product"]
            if products:
                seeds = products[:1]

        # Product scope selection
        product_scope: Optional[str] = None
        if self.strict_scope:
            # If any Product seed exists, lock to it; else infer from main sections
            prod_seeds = [s for s in seeds if (self.g.entities_by_id.get(s) or Entity(s, "", [], [])).type == "Product"]
            if prod_seeds:
                # pick the most frequent by seed_counts, then first
                prod_seeds.sort(key=lambda s: seed_counts.get(s, 0), reverse=True)
                product_scope = prod_seeds[0]
            else:
                # infer from main sections' products (majority)
                prods = [self.g.product_of(sid) for sid in main_sections]
                prods = [p for p in prods if p]
                if prods:
                    from collections import Counter
                    product_scope = Counter(prods).most_common(1)[0][0]
        else:
            product_scope = self._majority_product(seeds)

        # Hop-1
        h1_list: List[Dict[str, Any]] = []
        for s in seeds:
            for n1 in self.g.neighbors_idx.get(s, []):
                if product_scope and not self.g.in_scope(n1["id"], product_scope):
                    continue
                ev = self.provider.by_entity(n1["id"], index=self.g, limit=1, query_context=query)
                if not ev:
                    continue
                score1 = 0.7 * self._rel_weight(n1["rel"]) + 0.3 * float(n1.get("w", 0.0))
                h1_list.append(
                    {"seed": s, "id": n1["id"], "rel1": n1["rel"], "ev": ev, "score1": score1}
                )

        # Hop-2
        paths2: List[Dict[str, Any]] = []
        for h1 in h1_list:
            for n2 in self.g.neighbors_idx.get(h1["id"], []):
                if n2["id"] == h1["seed"]:
                    continue  # avoid 2-edge loop
                if product_scope and not self.g.in_scope(n2["id"], product_scope):
                    continue
                ev2 = self.provider.by_entity(n2["id"], index=self.g, limit=1, query_context=query)
                if not ev2:
                    continue
                score2 = 0.7 * self._rel_weight(n2["rel"]) + 0.3 * float(n2.get("w", 0.0))
                path_score = 0.6 * h1["score1"] + 0.4 * score2
                paths2.append(
                    {
                        "seed": h1["seed"],
                        "mid": h1["id"],
                        "id": n2["id"],
                        "rel1": h1["rel1"],
                        "rel2": n2["rel"],
                        "ev": ev2,
                        "score": path_score,
                    }
                )

        # Unify candidates; drop overlaps with main sections
        def _c_key(x: Dict[str, Any]) -> str:
            return x["target"]

        cands: List[Dict[str, Any]] = []
        for p in paths2:
            cands.append(
                {
                    "target": p["id"],
                    "title": (self.g.entities_by_id.get(p["id"]) or Entity(p["id"], "", [], [])).aliases[:1] or [p["id"]],
                    "badge": p["rel1"],
                    "sub_badge": p.get("rel2"),
                    "evidence": p["ev"],
                    "score": float(p["score"]),
                    "path": [
                        {"id": p["seed"]},
                        {"rel": p["rel1"]},
                        {"id": p["mid"]},
                        {"rel": p["rel2"]},
                        {"id": p["id"]},
                    ],
                }
            )
        for h1 in h1_list:
            cands.append(
                {
                    "target": h1["id"],
                    "title": (self.g.entities_by_id.get(h1["id"]) or Entity(h1["id"], "", [], [])).aliases[:1] or [h1["id"]],
                    "badge": h1["rel1"],
                    "evidence": h1["ev"],
                    "score": float(h1["score1"]),
                    "path": [{"id": h1["seed"]}, {"rel": h1["rel1"]}, {"id": h1["id"]}],
                }
            )

        # Drop suggestions whose evidence overlaps with main sections
        main_set = set(main_sections)
        cands = [c for c in cands if not (set(c.get("evidence", [])) & main_set)]
        # Enforce strict scope at candidate stage as well
        if product_scope:
            cands = [c for c in cands if self.g.in_scope(c["target"], product_scope)]

        # Deduplicate by target keep highest score
        best: Dict[str, Dict[str, Any]] = {}
        for c in cands:
            t = c["target"]
            prev = best.get(t)
            if (not prev) or (c["score"] > prev["score"]):
                best[t] = c
        cands = list(best.values())

        # MMR selection across all candidates by target id
        mmr_base = sorted([(c["target"], c["score"]) for c in cands], key=lambda x: -x[1])
        sel_ids = _mmr_select(mmr_base, self.limit, self.mmr_lambda)
        sel = [next(c for c in cands if c["target"] == sid) for sid in sel_ids]

        # Render preview
        preview = self._render_preview(query, main_sections, hits_map)

        # Final payload
        return {
            "query": query,
            "seed_entities": seeds,
            "main_sections": main_sections,
            "suggestions": [
                {
                    "title": (c.get("title") or [c["target"]])[0],
                    "target": c["target"],
                    "badge": c["badge"],
                    **({"sub_badge": c["sub_badge"]} if c.get("sub_badge") else {}),
                    "evidence": c.get("evidence", []),
                    "score": round(float(c["score"]), 4),
                    "path": c["path"],
                }
                for c in sel
            ],
            "answer_preview": preview,
            "debug": {"tta_ms": int(tta_ms), "limit": self.limit},
        }
