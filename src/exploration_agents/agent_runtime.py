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

from shared import get_env, load_config, sanitize_log_data
from .kb_retriever import kb_search
from .neighbors import next_steps


logger = logging.getLogger(__name__)


def retrieve_context(query: str) -> Dict[str, Any]:
    load_config()
    top_k = int(get_env("RETRIEVAL_TOPK", "8"))

    hits, tta_ms = kb_search(query, top_k=top_k)
    if not hits:
        raise RuntimeError("KB returned no results for the query")

    best = hits[0]
    meta = best.get("metadata", {}) or {}
    section_id = meta.get("x-amz-bedrock-kb-doc-id") or meta.get("bedrock-kb-doc-id")

    # Build citations as presigned URLs when available; fallback to s3 URI
    citations: List[str] = []
    for h in hits:
        loc = (h.get("location", {}) or {}).get("s3Location", {})
        uri = loc.get("uri")
        presigned = h.get("presigned_url")
        citations.append(presigned or uri)

    nexts = next_steps(section_id) if section_id else []

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
                "tta_ms": payload["tta_ms"],
                "num_next_steps": len(payload["next_steps"]),
            }
        ),
    )

    return payload
