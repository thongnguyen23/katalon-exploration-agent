2025-11-03 — Intent & Guardrails (pre)

Intent
- Implement KB-first → Graph-expand (2 hops) retrieval per SPEC.
- Provide a manual CLI `retrieve_main.py` (no HTTP) that returns JSON with answer preview and graph-based suggestions.

Guardrails
- Minimal, precise changes; reuse existing Bedrock KB wrapper and graph artifacts.
- No edits to tested build scripts under `specs/tools/`.
- Prefer integration over stubs; surface contract violations early.

 Immediate Plan
  - Add SectionProviderKB and in-memory indices (entities, aliases, neighbors).
  - Implement seeds from sections (reverse MENTIONED_IN, then alias fuzz ≥ 0.86).
  - Expand 1–2 hops with ontology weights, scope filter, MMR selection.
  - Synthesize preview + suggestions JSON; log timings; add caching.

2025-11-03 — Implementation (post)

Commands
- Created branch: `git switch -c retrieve`
- Scaffold: `specs/tools/spec-bootstrap.sh retrieve`
- Added spec: `SPEC_RETRIEVE_KB_FIRST_2HOPS.md` and `specs/retrieve/SPEC.md`
- Implemented: `src/retrieve_kb2hops.py`, `retrieve_main.py`

Artifacts
- Indices loaded from `artifacts/graph/{entities.jsonl,neighbors.jsonl}` (expected present).
- Output JSON at `artifacts/last_retrieve.json`; logs under `specs/retrieve/logs/`.

Next
- Validate end-to-end with real KB credentials and local doc mirror.
- Tune title/snippet extraction when only s3/http is available.
