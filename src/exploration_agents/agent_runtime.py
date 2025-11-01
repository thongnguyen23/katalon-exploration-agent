"""Orchestrator runtime for exploration-agents.

Exposes `retrieve_context(query)` that:
- Calls Bedrock KB to retrieve passages
- Picks the best hit, extracts section_id
- Looks up graph next-steps
- Returns structured payload
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List
import os

from shared import get_env, load_config, sanitize_log_data
from .kb_retriever import kb_search
from .neighbors import next_steps
from .section_resolver import resolve_section_id, section_snippet_from_text


logger = logging.getLogger(__name__)


def retrieve_context(query: str) -> Dict[str, Any]:
    load_config()
    top_k = int(get_env("RETRIEVAL_TOPK", "8"))

    hits, tta_ms = kb_search(query, top_k=top_k)
    if not hits:
        raise RuntimeError("KB returned no results for the query")

    best = hits[0]
    meta = best.get("metadata", {}) or {}
    # Try to resolve a section inside the document using the snippet
    resolved_section_id, confidence, reason = resolve_section_id(best)
    section_id = resolved_section_id or meta.get("x-amz-bedrock-kb-doc-id") or meta.get("bedrock-kb-doc-id")

    # Build citations as presigned URLs when available; fallback to s3 URI
    citations: List[str] = []
    for h in hits:
        loc = (h.get("location", {}) or {}).get("s3Location", {})
        uri = loc.get("uri")
        presigned = h.get("presigned_url")
        citations.append(presigned or uri)

    raw_nexts = next_steps(section_id) if section_id else []
    nexts = [{"section_id": e["section_id"], "rel": e["rel"]} for e in raw_nexts]

    # Attempt to log human-friendly snippets for the first few next steps
    next_snippets: list[dict] = []
    if nexts:
        def _doc_key_from_section_id(sec_id: str) -> tuple[str, str] | None:
            # Return (doc_id, local_path) if found under in_full/ or in/
            segs = sec_id.split('.')
            for i in range(len(segs), 0, -1):
                doc_id = '.'.join(segs[:i])
                rel_path = doc_id.replace('.', '/') + '.md'
                for root in ('in_full', 'in'):
                    full = f"{root}/{rel_path}"
                    if os.path.exists(full):
                        return doc_id, full
            return None

        # Fill snippet on each next step item (limit 220 chars)
        for item in nexts:
            sec_id = item["section_id"]
            got = _doc_key_from_section_id(sec_id)
            snippet = None
            if got:
                doc_id, local_path = got
                try:
                    md_text = open(local_path, 'r', encoding='utf-8').read()
                except Exception:
                    md_text = open(local_path, 'r', encoding='utf-8', errors='ignore').read()
                snippet = section_snippet_from_text(doc_id, sec_id, md_text, max_len=220)
            item["snippet"] = snippet

        # Also prepare a compact preview list for logs (first 3 items)
        for item in nexts[:3]:
            next_snippets.append({
                "section_id": item["section_id"],
                "rel": item["rel"],
                "snippet": item.get("snippet"),
            })

    answer_text = (best.get("content", {}) or {}).get("text")
    if not answer_text:
        # Some KBs return `content` as a list of text blocks
        content = best.get("content")
        if isinstance(content, list) and content and isinstance(content[0], dict):
            answer_text = content[0].get("text")

    payload: Dict[str, Any] = {
        "answer": answer_text or "",
        "citations": [c for c in citations if c],
        "next_steps": nexts,
        "tta_ms": int(tta_ms),
    }

    logger.info(
        "query_log: %s",
        sanitize_log_data(
            {
                "query": query,
                "section_id": section_id,
                "section_resolve_conf": round(confidence, 3),
                "section_resolve_reason": reason,
                "tta_ms": payload["tta_ms"],
                "num_next_steps": len(payload["next_steps"]),
                "next_snippets": next_snippets,
            }
        ),
    )

    return payload
