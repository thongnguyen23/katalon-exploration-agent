"""Section Resolver

Given a Bedrock KB retrieval hit, determine the most likely section_id
in our graph by aligning the returned text snippet against the source
Markdown document.

Heuristics (in order):
- Exact substring match of the snippet within a section's body (confidence=0.95)
- Token overlap score across sections; pick max (confidence in [0.6,0.9])
- Fallback: map doc_id -> first H1 section (confidence=0.3)
"""

from __future__ import annotations

import html
import io
import re
import urllib.request
from typing import Dict, List, Optional, Tuple


HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<title>.+?)\s*$")
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def join_section_id(doc_id: str, anchor_slug: Optional[str]) -> str:
    if not anchor_slug:
        return doc_id
    dotted = anchor_slug.replace("-", ".")
    dotted = re.sub(r"\.\.+", ".", dotted)
    return f"{doc_id}.{dotted}"


def _normalize_text(t: str) -> str:
    t = html.unescape(t)
    t = TAG_RE.sub(" ", t)
    t = t.replace("\u00A0", " ")
    t = WS_RE.sub(" ", t).strip()
    return t


def _fetch_text(uri: str) -> Optional[str]:
    try:
        with urllib.request.urlopen(uri, timeout=8) as resp:
            raw = resp.read()
            try:
                return raw.decode("utf-8")
            except Exception:
                return raw.decode("utf-8", errors="ignore")
    except Exception:
        return None


def _parse_sections(doc_id: str, md: str) -> List[Tuple[str, str]]:
    """Return list of (section_id, section_text) preserving order.

    Section text accumulates lines until the next heading of same/higher level.
    """
    sections: List[Tuple[str, List[str]]] = []
    current: Optional[Tuple[str, List[str]]] = None
    current_level = None

    # Ensure there is at least a doc-root section if no H1 present
    def start_section(level: int, title: str):
        nonlocal current, current_level
        anchor = slugify(title) if title else None
        sid = join_section_id(doc_id, anchor or "")
        current = (sid, [])
        current_level = level
        sections.append(current)

    for line in md.splitlines():
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group("hashes"))
            title = m.group("title").strip()
            start_section(level, title)
        else:
            if current is None:
                start_section(1, doc_id.split(".")[-1])
            current[1].append(line)

    out: List[Tuple[str, str]] = []
    for sid, lines in sections:
        out.append((sid, "\n".join(lines)))
    return out


def _token_overlap(a: str, b: str) -> float:
    a_set = {t for t in re.findall(r"[a-z0-9]+", a.lower()) if len(t) > 2}
    b_set = {t for t in re.findall(r"[a-z0-9]+", b.lower()) if len(t) > 2}
    if not a_set or not b_set:
        return 0.0
    inter = len(a_set & b_set)
    denom = min(len(a_set), len(b_set))
    return inter / denom if denom else 0.0


def _doc_id_from_uri(uri: str) -> Optional[str]:
    try:
        # accept http(s) or s3 URIs; extract path and drop extension
        m = re.match(r"^(?:https?://[^/]+|s3://[^/]+)/(?P<path>[^?]+)", uri)
        if not m:
            return None
        path = m.group("path")
        if path.endswith(".md"):
            path = path[:-3]
        parts = [p for p in path.split("/") if p]
        return ".".join(parts)
    except Exception:
        return None


def resolve_section_id(hit: Dict) -> Tuple[Optional[str], float, str]:
    """Return (section_id, confidence, reason). Safe for missing fields.

    Expects hit structure like Bedrock retrieve results with optional
    `presigned_url` and metadata `x-amz-bedrock-kb-doc-id`.
    """
    meta = hit.get("metadata", {}) or {}
    doc_id = meta.get("x-amz-bedrock-kb-doc-id") or meta.get("bedrock-kb-doc-id")

    snippet = hit.get("content", {})
    if isinstance(snippet, dict):
        snippet = snippet.get("text")
    elif isinstance(snippet, list) and snippet and isinstance(snippet[0], dict):
        snippet = snippet[0].get("text")
    if not isinstance(snippet, str):
        snippet = ""

    # Prefer presigned; else fall back to uri if http(s); ignore s3:// here
    uri = hit.get("presigned_url")
    if not uri:
        uri = ((hit.get("location", {}) or {}).get("s3Location", {}) or {}).get("uri")
        if uri and uri.startswith("s3://"):
            uri = None  # cannot fetch directly

    # If doc_id is missing, try to derive it from the URI path
    if not doc_id:
        uri_for_doc = hit.get("presigned_url") or (((hit.get("location", {}) or {}).get("s3Location", {}) or {}).get("uri"))
        doc_id = _doc_id_from_uri(uri_for_doc) if uri_for_doc else None
        if not doc_id:
            return None, 0.0, "no_doc_id"

    md_text: Optional[str] = _fetch_text(uri) if uri else None
    if not md_text:
        # Fallback to first H1 mapping when we cannot fetch
        return join_section_id(doc_id, doc_id.split(".")[-1]), 0.3, "fallback_first_h1"

    sections = _parse_sections(doc_id, md_text)
    norm_snippet = _normalize_text(snippet)

    # Exact substring within any section's body
    best_sid = None
    best_score = 0.0
    best_reason = ""
    for sid, body in sections:
        norm_body = _normalize_text(body)
        if norm_snippet and norm_snippet in norm_body:
            return sid, 0.95, "exact_substring"
        # Token overlap heuristic
        score = _token_overlap(norm_snippet, norm_body)
        if score > best_score:
            best_score, best_sid = score, sid
            best_reason = "token_overlap"

    if best_sid and best_score >= 0.5:
        return best_sid, min(0.9, 0.6 + 0.4 * best_score), best_reason

    # Last resort: first section encountered (typically H1)
    return sections[0][0], 0.3, "fallback_first_h1"
