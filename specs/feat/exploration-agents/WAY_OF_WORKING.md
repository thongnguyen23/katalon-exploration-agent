Follow AGENTS.md — Way of Working Steps

- Use `specs/tools/spec-bootstrap.sh <branch>` for scaffolding.
- Source of truth: `SPEC.md` and codebase. Keep other docs in sync.
- Prefer minimal, reversible slices. Update `TODO.md` pre/post.
- Use integration flows (no stub runners). Bedrock + S3 required for live queries.
- Capture evidence paths for validations and journal.

Iteration extras
- Fast checks: lint, import load for `exploration_agents` package.
- Validate graph build on a small local sample before running on S3.
