Open Items

- Provide `KB_ID` and confirm AWS credentials with access to the target Bedrock Knowledge Base and S3 bucket(s) for source docs. Without these, live retrieval cannot be validated.
- Confirm expected section_id convention in Bedrock KB metadata (`x-amz-bedrock-kb-doc-id`) matches graph builder output (doc path segments joined by dots + dotted section slug).
