2025-11-01 — Pre (intent & plan)
- Intent: Implement ontology-driven graph builder per SPEC v0.2.
- Guardrails: minimal, reversible changes; no edits to shared tools; JSONL-only outputs.
- Plan: load ontology → parse markdown → detect entities → generate + validate edges → merge/weight → fanout+MMR → emit artifacts → report.

2025-11-01 — Post (outcomes)
- Added `src/exploration_agents/ontology_graph_builder.py` (library-only; no CLI).
- Single entrypoint: `exploration_agents.builder_main` (env-only).
- Ontology moved to `configs/ontology.yaml`, snapshot per run.
- Emissions: entities.jsonl, edges.jsonl, neighbors.jsonl, build_report.json, edges.rejected.jsonl.
- Next: improve detectors; add tests and demo dataset.
