Scripts

- [deprecated] Use the single entrypoint instead:
  `PYTHONPATH=src python -m exploration_agents.builder_main`
- `pull_s3_md.sh s3://bucket/prefix [out_dir]` — copy only `*.md` from an S3 prefix into a local directory (default `in`) using AWS CLI, preserving structure.
- `run_full_flow.sh [--s3 <src>] [--out in] [--flatten] [--query "..."] [--topk N] [--log <file>]` — end-to-end: pull → build → retrieve; logs to `specs/feat/exploration-agents/logs/run-*.log` and writes `artifacts/last_response.json`.

All scripts expect env loaded from `.env.defaults` + `.env`.
