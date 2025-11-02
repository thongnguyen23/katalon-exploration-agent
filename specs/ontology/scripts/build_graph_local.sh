#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <docs_dir|s3://bucket/prefix> [options]" >&2
  echo "Example: $0 docs/ --ontology artifacts/ontology.yaml --emit-entities artifacts/entities.jsonl --emit-edges artifacts/edges.jsonl --emit-neighbors artifacts/neighbors.jsonl" >&2
  exit 1
fi

SRC="$1"; shift || true

PYTHONPATH="${PYTHONPATH:-}:src" python3 -m exploration_agents.ontology_graph_builder "$SRC" \
  --ontology artifacts/ontology.yaml \
  --emit-entities artifacts/entities.jsonl \
  --emit-edges artifacts/edges.jsonl \
  --emit-neighbors artifacts/neighbors.jsonl \
  "$@"

echo "Graph build artifacts written under artifacts/"
