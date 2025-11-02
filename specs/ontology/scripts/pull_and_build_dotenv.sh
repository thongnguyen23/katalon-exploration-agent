#!/usr/bin/env bash
set -euo pipefail

# Load dotenv as source of truth
if [ -f .env.defaults ]; then set -a; . .env.defaults; set +a; fi
if [ -f .env ]; then set -a; . .env; set +a; fi

ARTIFACTS_DIR="${ARTIFACTS_DIR:-artifacts}"
DOCS_OUT="${DOCS_OUT:-${ARTIFACTS_DIR}/docs}"
ONTOLOGY_FILE="${ONTOLOGY_FILE:-${ARTIFACTS_DIR}/ontology.yaml}"
S3_SRC="${DOCS_S3:-${EA_S3:-}}"

if [ -z "${S3_SRC}" ]; then
  echo "Missing DOCS_S3/EA_S3 in .env/.env.defaults. Please set an S3 prefix or ARN." >&2
  exit 2
fi

mkdir -p "${DOCS_OUT}" "${ARTIFACTS_DIR}"

echo "[1/2] Syncing Markdown from S3 to ${DOCS_OUT} (dotenv-configured)" >&2
specs/feat/exploration-agents/scripts/pull_s3_md.sh "${S3_SRC}" "${DOCS_OUT}"

echo "[2/2] Building ontology graph (dotenv-configured)" >&2
specs/ontology/scripts/build_graph_local.sh "${DOCS_OUT}" --ontology "${ONTOLOGY_FILE}"

echo "Done. Artifacts in ${ARTIFACTS_DIR}/: entities.jsonl, edges.jsonl, neighbors.jsonl, build_report.json" >&2

