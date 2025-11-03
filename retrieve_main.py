from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path

from shared import load_config, get_env
from src.retrieve_kb2hops import GraphIndex, SectionProviderKB, RetrieveEngine


def _env(key: str, default: str) -> str:
    return os.getenv(key, default)


def _int_env(key: str, default: int) -> int:
    try:
        return int(os.getenv(key, str(default)))
    except Exception:
        return default


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    load_config()

    p = argparse.ArgumentParser(description="KB-first → Graph-expand (2 hops) retriever")
    p.add_argument("--query", "-q", help="User query text")
    p.add_argument("--limit", "-k", type=int, default=_int_env("LIMIT", 5), help="Max sections/suggestions")
    args = p.parse_args(argv)

    query = args.query or os.getenv("EA_HARDCODED_QUERY") or Path(os.getenv("EA_QUESTION_FILE", "question.txt")).read_text(encoding="utf-8").strip()
    limit = args.limit

    # Logging
    logs_dir = Path("specs/retrieve/logs"); logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = logs_dir / f"retrieve-{time.strftime('%Y%m%d-%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        handlers=[logging.FileHandler(log_path, encoding="utf-8"), logging.StreamHandler()],
    )

    # Config
    graph_dir = _env("GRAPH_DIR", "artifacts/graph")
    entities_file = _env("ENTITIES_FILE", "entities.jsonl")
    neighbors_file = _env("NEIGHBORS_FILE", "neighbors.jsonl")
    ontology_path = _env("ONTOLOGY_PATH", "configs/ontology.yaml")
    kb_topk = _int_env("KB_TOPK", 20)

    # Indices
    g = GraphIndex(graph_dir=graph_dir, entities_file=entities_file, neighbors_file=neighbors_file)
    g.load()

    provider = SectionProviderKB(endpoint=_env("KB_ENDPOINT", None), index=_env("KB_INDEX", None), topk=kb_topk, ttl_sec=_int_env("CACHE_TTL_SEC", 60))
    engine = RetrieveEngine(provider=provider, g=g, ontology_path=ontology_path, limit=limit)

    t0 = time.perf_counter()
    result = engine.run(query)
    tta = int((time.perf_counter() - t0) * 1000)
    result.setdefault("debug", {})["wall_ms"] = tta

    # Emit
    artifacts = Path("artifacts"); artifacts.mkdir(parents=True, exist_ok=True)
    out_path = artifacts / "last_retrieve.json"
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"\nSaved: {out_path}\nLog: {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

