Branch Conventions
- Spec path: `specs/retrieve/` (matches git branch `retrieve`).
- Canonical spec: `specs/retrieve/SPEC.md` (do not edit arbitrarily).

Iteration Extras
- Fast validations over integration: run CLI with a small LIMIT (≤5).
- Keep logs under `artifacts/logs` and `specs/retrieve/logs` when practical.
- Update `TODO.md` before and after each slice; reflect real next actions.
- Journal concise entries with commands, artifacts, outcomes.

Build Inputs
- Graph artifacts expected under `artifacts/graph/{entities.jsonl,neighbors.jsonl}`.
- Ontology at `configs/ontology.yaml` (fallback weights if missing).

Out of Scope
- No HTTP server or UI changes in this branch.
- No modifications to `specs/tools/` scripts without explicit approval.
