SPEC — Ontology-Based Graph Builder

Project: Katalon Knowledge / GraphRAG PoC
Version: v0.2 (2025-11-01)

1  Purpose

Build an ontology-driven knowledge graph from Markdown documentation (local or S3).
The graph supports retrieval-augmented reasoning (RAG) and contextual “Next Step” suggestions after answering a user query.

2  Scope

In Scope	Out of Scope
Parse Markdown structure (titles, links, headings)	Semantic understanding of full document text
Extract typed entities & typed relations defined in ontology.yaml	Storage in graph DB (JSONL output only)
Merge, weight, and validate edges	UI or visualization
Produce build report & runtime adjacency	—

3  Inputs & Configuration

Item	Description
Source	docs_dir or s3://bucket/prefix
Ontology	ontology.yaml (typed schema + annotations)
Optional maps	synonyms.json, product_map.yaml, entity_whitelist.txt
ENV vars	AWS_REGION, GRAPH_FILE (default artifacts/edges.jsonl)

4  Outputs

File	Purpose
entities.jsonl	{id,type,aliases,sources}
edges.jsonl	{src,dst,rel,w,count,sources}
neighbors.jsonl	{id,neighbors:[{id,rel,w}]}
build_report.json	summary & violations
edges.rejected.jsonl	invalid or out-of-ontology edges

5  Ontology Schema (annotated)

5.1 Header & Governance

version: 0.2
updated_at: 2025-11-01
owner: ai-platform@katalon
review_process: "Docs + AI weekly review / PR approval"
ranking:
  defaults:
    relation_weights: {NEXT_STEP:0.95, DEPENDS_ON:0.9, USES:0.85,
                       BELONGS_TO:0.9, TROUBLESHOOTS:0.8,
                       SEE_ALSO:0.7, MENTIONED_IN:0.6}
    fanout_cap_per_rel: 20
    mmr_lambda: 0.3
evidence_policy:
  min_sources_per_edge: 1
  require_sources_field: true

5.2 Entity Types (annotated subset)

Name	Description	Detect Rules	Examples
Product	Top-level products	folder prefix katalon-studio/, testops/	Katalon Studio
Feature	Product capability	filename contains smart-wait,object-spy	Smart Wait
Concept	Core test artifacts	test-case,object-repository	Test Case
HowTo	Task-oriented guide	prefix create-,run-,configure-	Create Test Case
API	Keyword / method	pattern webui. ws.	WebUI.click
Troubleshooting	Error/fix topics	filename troubleshoot,failed,error	Fix Failed Execution

5.3 Relation Types (annotated)

Name	From → To	Weight	Constraints	Description
BELONGS_TO	Feature/Concept/HowTo/API → Product	0.9	—	within product
DEPENDS_ON	HowTo → Concept/Feature	0.9	—	prerequisite
NEXT_STEP	HowTo → HowTo	0.95	acyclic	workflow order
USES	HowTo/Concept → API/Feature	0.85	—	uses API/feature
TROUBLESHOOTS	Troubleshooting → HowTo/Feature	0.8	—	fixes topic
SEE_ALSO	any → any	0.7	—	related docs
MENTIONED_IN	any entity → Section	0.6	—	evidence link

Each type includes optional fields:
x-description, x-ui_label {vi,en}, x-detect_rules, x-examples, x-ui_badge, x-evidence_min.

6  Build Pipeline (9 Steps)
  1.	Load ontology → compile validators (allowed(from,to,rel), default_weight)
  2.	Parse Markdown → extract sections (doc_id, section_id, title, links)
  3.	Detect entities
  •	rule-based first, LLM fallback (see Prompts)
  •	normalize aliases → emit entities.jsonl and MENTIONED_IN edges
  4.	Generate candidate edges via structure & template rules (BELONGS_TO, NEXT_STEP, etc.)
  5.	Validate edges against ontology (from→to allowed, direction normalized)
  6.	Merge duplicates & compute w = min(1, max(default, 1 − exp(−0.3 × count)))
  7.	Fanout cap + MMR per node (≤ 20 neighbors/rel, λ = 0.3)
  8.	Emit edges.jsonl, neighbors.jsonl
  9.	Validate report (no orphan nodes, no NEXT_STEP cycles, coverage ≥ 90%)

7  CLI Usage

specs/.../build_graph_local.sh docs/ \
  --ontology artifacts/ontology.yaml \
  --emit-entities artifacts/entities.jsonl \
  --emit-edges artifacts/edges.jsonl \
  --emit-neighbors artifacts/neighbors.jsonl \
  --enable-llm-entity true \
  --llm-provider openai --llm-model gpt-4o-mini \
  --fanout-cap 20 --mmr-lambda 0.3

8  Runtime Ranking Rules

score = 0.7*relation_weight + 0.2*recency_boost + 0.1*popularity
Priority: NEXT_STEP > DEPENDS_ON/USES > TROUBLESHOOTS > SEE_ALSO

Return 3–5 unique suggestions not already shown in the Answer.

9  Lightweight LLM Prompts

A) Entity Extraction + Typing

System

You extract entities from Katalon technical docs.
Return JSON only. Allowed types: ["Product","Feature","Concept","HowTo","API","Troubleshooting"].
Prefer entities helpful for guidance and next-step suggestions.

User

TITLE: {{title}}
LEAD_TEXT: {{first_2_sentences}}
Return ≤4 entities following:
{"entities":[{"name":"","type":"","evidence":"","aliases":[]}]}
Rules:
- WebUI.*, WS.* ⇒ API
- Create/Run/Configure/Debug ⇒ HowTo
- Test Case/Suite/Object ⇒ Concept
- Smart Wait/Object Spy ⇒ Feature
- Katalon Studio/TestOps ⇒ Product
- Failed/Error ⇒ Troubleshooting

B) Relation Suggestion (fallback)

System

Suggest relations using only title/lead text.
Return JSON only with ["BELONGS_TO","NEXT_STEP","DEPENDS_ON","USES","TROUBLESHOOTS"].

User

ENTITIES: {{json_entities}}
TITLE: {{title}}
LEAD_TEXT: {{lead}}
Output: {"relations":[{"src":"","dst":"","rel":"","evidence":""}]}
Max 3 relations.

10  Acceptance Criteria (Demo)
  •	≥ 90 % of files yield ≥ 1 entity
  •	Each HowTo → ≥ 1 edge of NEXT_STEP or DEPENDS_ON/USES
  •	No NEXT_STEP cycles; orphans < 1 %
  •	Build time < 30 s (excl. LLM)
  •	Query “Create Test Case” → suggest “Run Test Suite”, “Test Object”, “WebUI.click”, “Fix Failed Execution”

11  Risks & Mitigations

Risk	Mitigation
LLM noise	Use only for uncertain sections, enforce JSON schema, cache output
Edge explosion	Fanout cap + MMR + dedupe
Direction errors	Validate against ontology from→to map; reject invalids
Ontology drift	Version control & weekly review

Summary

This spec defines:
  1.	Ontology schema with annotations (entity + relation metadata)
  2.	9-step graph build pipeline with validation and weighting
  3.	Lightweight LLM prompts for entity typing & relation hints
  4.	Governance rules for maintainability and demo clarity

Together, it produces an explainable, ontology-aligned GraphRAG ready for the “Answer + Next Steps” leadership demo.
