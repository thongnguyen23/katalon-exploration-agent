📘 Project Specification — exploration-agents

Type: AI Memory (KB + Graph)
Mode: KB-only retrieval (no FAISS, no chat memory)
Runtime: Local orchestrator agent (ADK) + AWS Bedrock KB
Source: Markdown documentation stored on S3

1. System Overview

The exploration-agents system retrieves context from Bedrock Knowledge Base (KB) and augments it with a lightweight graph memory file (neighbors.jsonl) built from the same Markdown documentation.

Main functions
1) Retrieve — query Bedrock KB for relevant passages.
2) Resolve citations — generate S3 presigned URLs for cited documents.
3) Infer Next Steps — look up relations from neighbors.jsonl based on current section.
4) Respond — return structured payload {answer, citations[], next_steps[], tta_ms}.

2. Components

Component | Responsibility
Bedrock KB | Chunk, embed, and store documentation vectors. Provides retrieval API.
Graph Builder | Parse Markdown files → extract section hierarchy and relations → output neighbors.jsonl.
Orchestrator Agent | Handle user queries, call KB, resolve citations, read graph to suggest next steps.
Configuration (.env) | Define KB_ID, S3 paths, retrieval limits, and runtime flags.

3. Data Flow

S3 Markdown (.md)
   │
   ├──> Indexed in Bedrock KB (managed)
   │
   └──> Parsed locally by Graph Builder
            ↓
        neighbors.jsonl
            ↓
User Query
   ↓
exploration-agents
   ├── Call Bedrock KB → retrieve passages
   ├── Identify section_id from metadata
   ├── Lookup neighbors.jsonl[src = section_id]
   └── Return {answer, citations, next_steps, tta_ms}

4. Core Data Structures

4.1 neighbors.jsonl

Each line represents an edge between two sections:

{"src":"truetest.auth","dst":"truetest.token.create","rel":"next","w":1.0}

- src: current section ID
- dst: related section ID
- rel: relation type (parent, next, prev, depends_on, enables, see_also)
- w: confidence weight (0–1)

4.2 KB Retrieval Result

Returned by Bedrock:

{
  "content": {"text": "..."},
  "metadata": {"x-amz-bedrock-kb-doc-id": "truetest.auth"},
  "location": {"s3Location": {"uri": "s3://docs/truetest/auth.md"}},
  "score": 0.87
}

5. Key Modules to Implement

5.1 Graph Build (ontology)
- Entry: `PYTHONPATH=src python -m exploration_agents.builder_main` (env-only)
- Input: local or S3 Markdown files (synced to artifacts/docs when SYNC_TO_LOCAL=true).
- Output per run: artifacts/runs/<run_id>/{entities.jsonl,edges.jsonl,neighbors.jsonl,build_report.json}.

5.2 kb_retriever.py
- Input: query text.
- Call bedrock-agent-runtime.retrieve() with KB_ID.
- Return top-k passages and timing info.
- Extract section_id from metadata (x-amz-bedrock-kb-doc-id).

5.3 neighbors.py
- Load neighbors.jsonl at startup into memory.
- Function:

def next_steps(section_id, min_w=0.6, limit=3) -> list[dict]:
    ...

- Filter by src == section_id and w >= min_w.
- Sort by relation priority (depends_on, enables, next, see_also).
- Return up to limit targets.

5.4 agent_runtime.py

Main orchestrator logic:

def retrieve_context(query: str):
    hits, tta = kb_search(query, top_k=8)
    best = hits[0]
    section_id = best["metadata"].get("x-amz-bedrock-kb-doc-id")
    nexts = next_steps(section_id)
    return {
        "answer": best["content"]["text"],
        "citations": [h["location"]["s3Location"]["uri"] for h in hits],
        "next_steps": nexts,
        "tta_ms": tta,
    }

6. Configuration (.env)

AWS_REGION=ap-southeast-1
KB_ID=kb-xxxxxxxxxxxxxxx
RETRIEVAL_TOPK=8
NEXTSTEP_MIN_W=0.6
GRAPH_FILE=artifacts/neighbors.jsonl

7. Execution Flow
1) Preprocess: run the env-only builder to generate neighbors.jsonl.
2) Runtime: start ADK agent → load graph → listen for queries.
3) Each query:
   - Retrieve from KB → get answer + metadata.
   - Resolve S3 links for citation.
   - Lookup graph for next steps.
   - Return structured JSON response.

8. Dependencies
- boto3 (Bedrock + S3 client)
- python-frontmatter or markdown-it (for parsing headings)
- pydantic (data models)
- uvicorn + adk (runtime agent)

9. Output Interfaces
- Tool response schema (for ADK integration):

{
  "answer": "string",
  "citations": ["url"],
  "next_steps": [{"section_id":"string","rel":"string"}],
  "tta_ms": 0
}

- Logs: per query {query, section_id, tta_ms, num_next_steps}.

10. Success Condition

Implementation is complete when:
- builder_main successfully generates neighbors.jsonl.
- retrieve_context() returns valid answer, citations, and ≥1 next_step.
- Average latency (TTA) < 600 ms per query.
