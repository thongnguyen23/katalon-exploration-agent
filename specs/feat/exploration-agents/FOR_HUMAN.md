Open Items

- KB ID provided: `D2EM2KMIKG` (saved to `.env` as `KB_ID` and `KNOWLEDGE_BASE_ID`).
- Confirm AWS credentials with access to the target Bedrock Knowledge Base and S3 bucket(s) for source docs. Without these, live retrieval cannot be validated.
- Confirm expected section_id convention in Bedrock KB metadata (`x-amz-bedrock-kb-doc-id`) matches graph builder output (doc path segments joined by dots + dotted section slug).
