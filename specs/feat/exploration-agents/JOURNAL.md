2025-10-31 — Intent
- Implement exploration-agents (KB + graph) per SPEC.md.

Guardrails
- Use integration APIs (Bedrock/S3); no stubs.
- Minimal, reversible changes; keep logs concise; no secrets.

Plan
- Build `exploration_agents` package; wire env; validate locally.

2025-10-31 — Progress
- Added modules: graph_builder, kb_retriever, neighbors, agent_runtime
- Updated .env defaults (AWS + KB vars)
- Added scripts to build graph (local/S3)
- Sanity-checked graph builder and neighbors locally
