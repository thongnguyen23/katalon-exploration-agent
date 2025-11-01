Scripts

- `build_graph_local.sh <docs_dir>` — run graph builder on a local directory of `.md` files and write `artifacts/neighbors.jsonl`.
- `build_graph_s3.sh s3://bucket/prefix` — run graph builder on an S3 prefix.
- `pull_s3_md.sh s3://bucket/prefix [out_dir]` — copy only `*.md` from an S3 prefix into a local directory (default `in`) using AWS CLI, preserving structure.
- `run_full_flow.sh [--s3 <src>] [--out in] [--flatten] [--query "..."] [--topk N] [--log <file>]` — end-to-end: pull → build → retrieve; logs to `specs/feat/exploration-agents/logs/run-*.log` and writes `artifacts/last_response.json`.

All scripts expect env loaded from `.env.defaults` + `.env`.
