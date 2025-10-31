Modules and Responsibilities

- `src/exploration_agents/graph_builder.py`
  - Parse Markdown (local dir or S3 prefix)
  - Build edges: `next`, `prev`, `parent`, `see_also`
  - Output JSONL: `artifacts/neighbors.jsonl`

- `src/exploration_agents/kb_retriever.py`
  - `kb_search(query, top_k)` → (hits, tta_ms)
  - AWS `bedrock-agent-runtime.retrieve`
  - Resolve S3 presigned URLs for citations

- `src/exploration_agents/neighbors.py`
  - Load JSONL into memory map: `src -> list[edge]`
  - `next_steps(section_id, min_w, limit)`

- `src/exploration_agents/agent_runtime.py`
  - `retrieve_context(query)` → response schema
  - Logging per query

Environment
- Uses `src/shared/config.py` helpers: `load_config`, `get_env*`
- New .env keys: `AWS_REGION`, `KB_ID`, `RETRIEVAL_TOPK`, `NEXTSTEP_MIN_W`, `GRAPH_FILE`

Integrations
- Bedrock KB: `boto3.client('bedrock-agent-runtime')`
- S3 presign: `boto3.client('s3').generate_presigned_url('getObject', ...)`
