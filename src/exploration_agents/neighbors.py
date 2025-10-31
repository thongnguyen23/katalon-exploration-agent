"""Neighbors Graph Loader and Next-Step Suggestion."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Dict, List

from shared import get_env, load_config

logger = logging.getLogger(__name__)


REL_PRIORITIES = {
    "depends_on": 0,
    "enables": 1,
    "next": 2,
    "see_also": 3,
    "prev": 4,
    "parent": 5,
}


@dataclass
class Edge:
    src: str
    dst: str
    rel: str
    w: float


_GRAPH: Dict[str, List[Edge]] = {}
_GRAPH_PATH: str | None = None


def _load_graph_once() -> None:
    global _GRAPH, _GRAPH_PATH
    if _GRAPH:
        return
    load_config()
    if _GRAPH_PATH is None:
        _GRAPH_PATH = get_env("GRAPH_FILE", "artifacts/neighbors.jsonl")
    try:
        with open(_GRAPH_PATH, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                obj = json.loads(line)
                edge = Edge(
                    src=obj["src"], dst=obj["dst"], rel=obj.get("rel", "see_also"), w=float(obj.get("w", 1.0))
                )
                _GRAPH.setdefault(edge.src, []).append(edge)
        logger.info("Loaded neighbors graph: %s (nodes=%d)", _GRAPH_PATH, len(_GRAPH))
    except FileNotFoundError:
        logger.warning("Neighbors graph not found at %s; next_steps() will return empty.", _GRAPH_PATH)


def next_steps(section_id: str, min_w: float | None = None, limit: int = 3) -> List[dict]:
    """Suggest next steps based on neighbors graph.

    Returns a list of {section_id, rel, w} objects.
    """
    _load_graph_once()
    min_w = min_w if min_w is not None else float(get_env("NEXTSTEP_MIN_W", "0.6"))

    candidates = [e for e in _GRAPH.get(section_id, []) if e.w >= min_w]
    candidates.sort(key=lambda e: (REL_PRIORITIES.get(e.rel, 99), -e.w, e.dst))
    out = [{"section_id": e.dst, "rel": e.rel, "w": e.w} for e in candidates[:limit]]
    return out


def load_graph(path: str | None = None) -> int:
    """Explicitly (re)load the graph, useful for tests or CLI usage."""
    global _GRAPH, _GRAPH_PATH
    _GRAPH = {}
    if path:
        _GRAPH_PATH = path
    else:
        _GRAPH_PATH = None  # force _load_graph_once to read from env
    _load_graph_once()
    return sum(len(v) for v in _GRAPH.values())
