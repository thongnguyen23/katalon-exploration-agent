Technical Notes — Ontology Graph Builder

Modules
- `src/exploration_agents/ontology_graph_builder.py` — library (no CLI)
  - Ontology loading/validation (`Ontology`, `RelationRule`)
  - Markdown parsing (`parse_markdown` headings + links)
  - Entity detection (rule-based; optional LLM via LiteLLM)
  - Edge generation (BELONGS_TO, NEXT_STEP, DEPENDS_ON, USES, TROUBLESHOOTS, SEE_ALSO, MENTIONED_IN)
  - Merge + weighting (exp count formula)
  - Fanout cap + MMR (string-level Jaccard diversity)
  - Emissions: `entities.jsonl`, `edges.jsonl`, `neighbors.jsonl`, `build_report.json`, `edges.rejected.jsonl`

Entry Point (single)
- `PYTHONPATH=src python -m exploration_agents.builder_main`

Configs & Maps
- `configs/ontology.yaml` — ranking defaults + relation rules.
- Optional: `synonyms.json`, `product_map.yaml`, `entity_whitelist.txt`.

Validation Tips
- Acyclic NEXT_STEP enforced; cycles removed into `edges.rejected.jsonl`.
- Coverage target: ≥90% files with ≥1 entity.
- Orphans target: <1%.

Outputs
- `artifacts/entities.jsonl` — one JSON per line
- `artifacts/edges.jsonl` — merged edges with weights
- `artifacts/neighbors.jsonl` — adjacency records for runtime
- `artifacts/build_report.json` — build summary and violations
