2025-11-01 — Pre (intent & plan)
- Intent: Implement ontology-driven graph builder per SPEC v0.2.
- Guardrails: minimal, reversible changes; no edits to shared tools; JSONL-only outputs.
- Plan: load ontology → parse markdown → detect entities → generate + validate edges → merge/weight → fanout+MMR → emit artifacts → report.

2025-11-01 — Post (outcomes)
- Added `src/exploration_agents/ontology_graph_builder.py` with CLI.
- Script: `specs/ontology/scripts/build_graph_local.sh` (local or S3).
- Default config: `artifacts/ontology.yaml`.
- Emissions: entities.jsonl, edges.jsonl, neighbors.jsonl, build_report.json, edges.rejected.jsonl.
- Next: improve detectors; add tests and demo dataset.
