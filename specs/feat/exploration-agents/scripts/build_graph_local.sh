#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <docs_dir> [out_jsonl]" >&2
  exit 1
fi

DOCS_DIR="$1"
OUT_PATH="${2:-}"

export PYTHONPATH=src:${PYTHONPATH:-}

# Pass arguments to Python via argv after '-'
python3 - "${DOCS_DIR}" "${OUT_PATH:-}" <<'PY'
import os, sys
from exploration_agents.graph_builder import build_graph

docs = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else None
path = build_graph(docs, out)
print(path)
PY
 
