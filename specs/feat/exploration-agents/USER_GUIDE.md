Exploration Agents — User Guide

What it does
- Retrieves context from AWS Bedrock Knowledge Base and augments it with graph-based next-step suggestions.

How to use
- Configure `.env` with `AWS_REGION`, `KB_ID`, and graph params.
- Build the neighbors graph once:
  - Local: `specs/feat/exploration-agents/scripts/build_graph_local.sh <docs_dir>`
  - S3: `specs/feat/exploration-agents/scripts/build_graph_s3.sh s3://bucket/prefix`
- From Python, call:
  - `from exploration_agents import retrieve_context`
  - `retrieve_context("How do I create a token?")`

Response schema
{
  "answer": "string",
  "citations": ["url"],
  "next_steps": [{"section_id":"string","rel":"string","w":0.0}],
  "tta_ms": 0
}

Limits
- Requires valid AWS credentials with access to Bedrock KB and S3.
- Graph suggestions depend on Markdown heading structure and links.

