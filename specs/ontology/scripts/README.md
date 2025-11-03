This folder no longer provides runnable scripts.

Single entrypoint for building the graph:
- PYTHONPATH=src python -m exploration_agents.builder_main

Behavior
- Reads configuration only from environment (.venv).
- If `DOCS_S3`/`EA_S3` and `SYNC_TO_LOCAL=true`, syncs Markdown to `artifacts/docs/`.
- Writes outputs to `artifacts/runs/<run_id>/` and snapshots ontology there.
