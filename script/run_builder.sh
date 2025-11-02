#!/usr/bin/env bash
set -euo pipefail

# Simple env-only runner for the ontology builder.
# - Loads env from .env.defaults then .env
# - Uses a single shared input folder (artifacts/docs)
# - Writes outputs under artifacts/runs/<RUN_ID>/ and snapshots ontology
#
# Optional: pass RUN_ID as the first arg to label the run.

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
cd "$ROOT"

# Load env from dotenv files (no secrets echoed)
if [ -f .env.defaults ]; then set -a; . .env.defaults; set +a; fi
if [ -f .env ]; then set -a; . .env; set +a; fi

# Allow overriding RUN_ID via first arg
if [ "${1:-}" != "" ]; then
  export RUN_ID="$1"
fi

# Ensure Python can import the package
export PYTHONPATH="${PYTHONPATH:-}:src"

echo "[builder] Starting…"
python3 -m exploration_agents.builder_main
echo "[builder] Finished. See artifacts/runs/<run_id>/ for outputs and manifest.json"

