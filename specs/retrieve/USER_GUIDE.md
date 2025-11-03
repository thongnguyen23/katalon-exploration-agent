Retrieve (KB-first → Graph-expand, 2 Hops)

What It Does
- Retrieves top KB sections for a query.
- Infers seed entities, expands the ontology graph up to 2 hops.
- Returns an answer preview with citations and diverse suggestions with evidence and transparent paths.

How To Run
- Prepare artifacts: `artifacts/graph/entities.jsonl` and `artifacts/graph/neighbors.jsonl` (from the graph builder).
- Ensure `.env` or env vars contain required keys (see SPEC):
  - `KB_ID`/`KNOWLEDGE_BASE_ID` for Bedrock KB (or set `KB_ENDPOINT`, `KB_INDEX`).
  - `KB_TOPK`, `LIMIT`, `GRAPH_DIR`, `ONTOLOGY_PATH`, `ENTITIES_FILE`, `NEIGHBORS_FILE`.
- Run: `python retrieve_main.py --query "<your question>"`.

Outputs
- JSON printed to stdout and saved to `artifacts/last_retrieve.json`.
- Logs written to `specs/retrieve/logs/`.

Known Limits
- Requires local mirror of docs (`in_full/` or `in/`) to extract robust titles/snippets.
- Evidence mapping prefers entity→sources in `entities.jsonl`; falls back to alias KB search.
- Bedrock KB credentials must be present in environment to retrieve sections.

