#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 s3://bucket/prefix [out_jsonl]" >&2
  exit 1
fi

S3_PREFIX="$1"
OUT_PATH="${2:-}"

export PYTHONPATH=src:${PYTHONPATH:-}

python3 - <<'PY'
import os, sys
from exploration_agents.graph_builder import build_graph

prefix = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else None
path = build_graph(prefix, out)
print(path)
PY
"${S3_PREFIX}" "${OUT_PATH:-}"

