#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Run the full exploration-agents flow: pull -> build -> retrieve.

Usage:
  run_full_flow.sh [--s3 <s3://bucket/prefix|arn:aws:s3:::bucket[/prefix]>] [--out <dir>] [--flatten]
                   [--query "text"] [--topk <N>] [--log <path>]

Defaults:
  --s3     arn:aws:s3:::public-mcp-test
  --out    in
  --flatten  (enabled if present)
  --query  "How do I generate steps with AI in Katalon?"
  --topk   8
  --log    specs/feat/exploration-agents/logs/run-YYYYmmdd-HHMMSS.log

Environment:
  Loads .env.defaults and .env for AWS_*, KB_ID/KNOWLEDGE_BASE_ID, GRAPH_FILE, etc.

Outputs:
  - artifacts/neighbors.jsonl (graph)
  - artifacts/last_response.json (last retrieval response)
  - Log file with a timestamp under specs/feat/exploration-agents/logs
USAGE
}

S3_SRC="arn:aws:s3:::public-mcp-test"
OUT_DIR="in"
FLATTEN=0
QUERY="How do I generate steps with AI in Katalon?"
TOPK=8
LOG_PATH=""

while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help) usage; exit 0;;
    --s3) S3_SRC="$2"; shift 2;;
    --out) OUT_DIR="$2"; shift 2;;
    --flatten) FLATTEN=1; shift 1;;
    --query) QUERY="$2"; shift 2;;
    --topk) TOPK="$2"; shift 2;;
    --log) LOG_PATH="$2"; shift 2;;
    *) echo "Unknown arg: $1" >&2; usage; exit 1;;
  esac
done

# Load env for AWS/KB
if [ -f .env.defaults ]; then set -a; . .env.defaults; set +a; fi
if [ -f .env ]; then set -a; . .env; set +a; fi

GRAPH_FILE=${GRAPH_FILE:-artifacts/neighbors.jsonl}

# Prepare logging
LOG_DIR="specs/feat/exploration-agents/logs"
mkdir -p "$LOG_DIR" artifacts
if [ -z "$LOG_PATH" ]; then
  TS=$(date +%Y%m%d-%H%M%S)
  LOG_PATH="$LOG_DIR/run-$TS.log"
fi
touch "$LOG_PATH"

echo "[run] START $(date -Iseconds)" | tee -a "$LOG_PATH"
echo "[run] S3_SRC=$S3_SRC OUT_DIR=$OUT_DIR FLATTEN=$FLATTEN TOPK=$TOPK" | tee -a "$LOG_PATH"
echo "[run] KB_ID=${KB_ID:-${KNOWLEDGE_BASE_ID:-}} AWS_REGION=${AWS_REGION:-}" | tee -a "$LOG_PATH"
echo "[run] GRAPH_FILE=$GRAPH_FILE" | tee -a "$LOG_PATH"

# 1) Pull Markdown
CMD_PULL=("$(dirname "$0")/pull_s3_md.sh" "$S3_SRC" "$OUT_DIR")
if [ "$FLATTEN" = "1" ]; then CMD_PULL+=("--flatten"); fi
echo "[run] pull: ${CMD_PULL[*]}" | tee -a "$LOG_PATH"
"${CMD_PULL[@]}" 2>&1 | tee -a "$LOG_PATH"

# 2) Build graph
export PYTHONPATH=src:${PYTHONPATH:-}
echo "[run] build_graph_local.sh $OUT_DIR" | tee -a "$LOG_PATH"
"$(dirname "$0")/build_graph_local.sh" "$OUT_DIR" 2>&1 | tee -a "$LOG_PATH"
if [ ! -f "$GRAPH_FILE" ]; then echo "[run][err] graph not found at $GRAPH_FILE" | tee -a "$LOG_PATH"; exit 2; fi
EDGE_COUNT=$(wc -l < "$GRAPH_FILE" | tr -d ' ')
echo "[run] graph edges=$EDGE_COUNT" | tee -a "$LOG_PATH"

# 3) Retrieve context
RESP_JSON="artifacts/last_response.json"
echo "[run] retrieve query=\"$QUERY\" topk=$TOPK" | tee -a "$LOG_PATH"
python - <<PY 2>&1 | tee -a "$LOG_PATH"
import json
from shared import load_config
from exploration_agents.agent_runtime import retrieve_context
load_config()
resp = retrieve_context("""$QUERY""")
print("[run] answer_preview:", (resp.get('answer') or '')[:300].replace('\n',' '))
print("[run] citations:", len(resp.get('citations', [])))
print("[run] next_steps:", resp.get('next_steps', [])[:5])
print("[run] tta_ms:", resp.get('tta_ms'))
open("$RESP_JSON","w",encoding="utf-8").write(json.dumps(resp, ensure_ascii=False, indent=2))
print("[run] wrote:", "$RESP_JSON")
PY

echo "[run] DONE $(date -Iseconds)" | tee -a "$LOG_PATH"
echo "[run] log: $LOG_PATH" | tee -a "$LOG_PATH"

