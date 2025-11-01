"""Retrieve-only runner (no graph build, no downloads).

This module lives under `src/` so imports are resolvable for type checkers
and runtime without `sys.path` hacks.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
import logging

from shared import load_config
from exploration_agents.agent_runtime import retrieve_context
from exploration_agents.section_resolver import section_snippet_from_text


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

    # Route library logs to the same file for visibility
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        handlers=[logging.FileHandler(log_path, encoding="utf-8"), logging.StreamHandler()],
    )

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
    # Append base info
    with open(log_path, 'a', encoding='utf-8') as fh:
        fh.write("\n".join(log_lines) + "\n")

    # Also log readable snippets for next steps (up to 3) from local mirror
    try:
        def _local_doc_for_section(sec_id: str):
            segs = sec_id.split('.')
            for i in range(len(segs), 0, -1):
                doc_id = '.'.join(segs[:i])
                rel_path = doc_id.replace('.', '/') + '.md'
                for root in ('in_full', 'in'):
                    full = Path(root) / rel_path
                    if full.exists():
                        return doc_id, full
            return None

        nexts = resp.get('next_steps', []) or []
        lines = []
        for idx, item in enumerate(nexts[:3], 1):
            sec_id = item.get('section_id')
            got = _local_doc_for_section(sec_id)
            snippet = None
            if got:
                doc_id, full = got
                try:
                    md = full.read_text(encoding='utf-8')
                except Exception:
                    md = full.read_text(encoding='utf-8', errors='ignore')
                snippet = section_snippet_from_text(doc_id, sec_id, md, max_len=220)
            lines.append(f"next#{idx} rel={item.get('rel')} section={sec_id} snippet={(snippet or '(n/a)')}")
        if lines:
            with open(log_path, 'a', encoding='utf-8') as fh:
                fh.write("\n".join(lines) + "\n")
    except Exception:
        # best effort logging; ignore snippet failures
        pass

    print(f"Retrieve-only complete.\nLog: {log_path}\nResponse: {out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
