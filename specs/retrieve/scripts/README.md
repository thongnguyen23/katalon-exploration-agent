Retrieve (KB-first → Graph-expand, 2 Hops)

Usage
- Ensure graph artifacts exist: `artifacts/graph/entities.jsonl`, `artifacts/graph/neighbors.jsonl`.
- Configure `.env` or env vars (see `specs/retrieve/SPEC.md`).
- Run:
  - `python retrieve_main.py --query "How to create a test case in Katalon Studio?"`

Outputs
- Prints JSON to stdout and writes `artifacts/last_retrieve.json`.
- Logs under `specs/retrieve/logs/` (timestamped).
