"""Retrieve-only runner (no graph build, no downloads).

This module lives under `src/` so imports are resolvable for type checkers
and runtime without `sys.path` hacks.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

from shared import load_config
from exploration_agents.agent_runtime import retrieve_context


def _read_question() -> str:
    qfile = os.getenv("EA_QUESTION_FILE", "question.txt")
    try:
        return Path(qfile).read_text(encoding="utf-8").strip()
    except Exception:
        return os.getenv(
            "EA_HARDCODED_QUERY",
            "How do I generate steps with AI in Katalon?",
        )


def main() -> int:
    load_config()

    artifacts = Path("artifacts"); artifacts.mkdir(parents=True, exist_ok=True)
    logs_dir = Path("specs/feat/exploration-agents/logs"); logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = logs_dir / f"retrieve-{time.strftime('%Y%m%d-%H%M%S')}.log"

    topk = int(os.getenv("EA_TOPK", os.getenv("RETRIEVAL_TOPK", "8")))
    os.environ["RETRIEVAL_TOPK"] = str(topk)
    query = _read_question()

    resp = retrieve_context(query)

    out_json = artifacts / "last_response.json"
    out_json.write_text(json.dumps(resp, ensure_ascii=False, indent=2), encoding="utf-8")

    log_lines = [
        f"query={query}",
        f"topk={topk}",
        f"tta_ms={resp.get('tta_ms')}",
        f"citations={len(resp.get('citations', []))}",
        f"answer_preview={(resp.get('answer') or '')[:200].replace('\n',' ')}",
    ]
    log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    print(f"Retrieve-only complete.\nLog: {log_path}\nResponse: {out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

