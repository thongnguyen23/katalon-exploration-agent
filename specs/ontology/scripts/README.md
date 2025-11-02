Ontology Graph Builder Scripts

- `build_graph_local.sh` — Run the ontology-based graph builder on a local directory or S3 prefix.
- `pull_and_build_dotenv.sh` — Use .env as the single source of truth: sync S3 (EA_S3/DOCS_S3) to `artifacts/docs/` and build the graph.

Usage
- Local docs: `specs/ontology/scripts/build_graph_local.sh docs/ --ontology artifacts/ontology.yaml` 
- S3 prefix:  `specs/ontology/scripts/build_graph_local.sh s3://my-bucket/kdocs/ --ontology artifacts/ontology.yaml`
- Dotenv end-to-end: `specs/ontology/scripts/pull_and_build_dotenv.sh`

Common options
- `--emit-entities <path>` — default `artifacts/entities.jsonl`
- `--emit-edges <path>` — default `artifacts/edges.jsonl`
- `--emit-neighbors <path>` — default `artifacts/neighbors.jsonl`
- `--synonyms <synonyms.json>` — optional alias map
- `--product-map <product_map.yaml>` — optional folder→product map
- `--entity-whitelist <file>` — optional allowlist (one id per line)
- `--enable-llm-entity true|false` — use LLM fallback for entity detection
- `--llm-provider <name>` `--llm-model <id>` — used when LLM is enabled
- `--fanout-cap <int>` `--mmr-lambda <float>` — override ranking defaults

Artifacts
- `artifacts/entities.jsonl` — `{id,type,aliases,sources}`
- `artifacts/edges.jsonl` — `{src,dst,rel,w,count,sources}`
- `artifacts/neighbors.jsonl` — `{id,neighbors:[{id,rel,w}]}`
- `artifacts/build_report.json` — summary & violations
- `artifacts/edges.rejected.jsonl` — rejected edges
