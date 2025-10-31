Scripts

- `build_graph_local.sh <docs_dir>` — run graph builder on a local directory of `.md` files and write `artifacts/neighbors.jsonl`.
- `build_graph_s3.sh s3://bucket/prefix` — run graph builder on an S3 prefix.

All scripts expect env loaded from `.env.defaults` + `.env`.
