SPEC — Retrieve (KB-first → Graph-expand, 2 Hops)

Mode: manual CLI via retrieve_main.py (no HTTP).
Goal: Answer with KB sections, then suggest “Next Steps” using a 1–2 hop walk on the ontology graph, with transparent paths and evidence.

1) Objectives
	1.	Use the KB (section-level) as the primary source to find the most relevant context for the user’s query.
	2.	From top KB sections, infer seed entities.
	3.	Expand the graph up to 2 hops from seeds to surface guided learning paths and actionable next steps.
	4.	Return a JSON payload including an answer preview (with citations), suggestions (with badges, evidence, and path), and debug info.

2) Configuration & Artifacts

2.1 Environment (.env / .venv)

# KB Provider
SECTIONS_PROVIDER=KB
KB_ENDPOINT=<http url or sdk name>
KB_INDEX=<collection/index name>
KB_TOPK=20                    # initial top-k sections from the KB

# Graph & Ontology
GRAPH_DIR=artifacts/graph
ONTOLOGY_PATH=configs/ontology.yaml
ENTITIES_FILE=entities.jsonl
NEIGHBORS_FILE=neighbors.jsonl

# Runtime
LIMIT=5                       # max main sections; max suggestions
LANG=vi
CACHE_TTL_SEC=60
CACHE_SIZE_DOCS=512

2.2 Required files (from graph builder)
	•	entities.jsonl — {"id","type","aliases":[],"sources":["section:..."]}
	•	neighbors.jsonl — {"id":"<entity_id>","neighbors":[{"id","rel","w"}...]}

No sections.jsonl required. Sections are fetched at runtime from the KB Provider.

3) Runtime Interfaces

3.1 KB Section Provider

class SectionProviderKB:
    def __init__(self, endpoint: str, index: str, topk: int): ...
    def topk(self, query: str, k: int) -> list[dict]:
        """Return [{id, doc_id, title, text, score}] for section-level hits."""
    def by_entity(self, entity_id: str, limit: int = 1) -> list[str]:
        """Return section ids that best evidence the given entity.
           Prefer metadata filters; fallback to alias-based search."""

3.2 In-memory indices (built on start)
	•	entities_by_id: dict[id → entity]
	•	alias_index: dict[alias_lower → set(entity_id)]
	•	neighbors_idx: dict[id → list[{id, rel, w}]]

4) End-to-End Flow (KB-first, 2 hops)

flowchart TD
  A[Query] --> B[KB Search (sections)]
  B --> C[Dedupe by doc_id → K main sections]
  C --> D[Sections → Seed Entities (MENTIONED_IN/alias)]
  D --> E1[Hop-1 neighbors from seeds]
  E1 --> E2[Hop-2 neighbors from Hop-1]
  C --> F[Main Context]
  E1 --> G[Neighbor -> Evidence section]
  E2 --> G
  F --> H[Score + Diversify (MMR)]
  G --> H
  H --> I[Synthesize preview + suggestions]
  I --> J[Return JSON]

B1. KB Search (primary)
	•	hits = KB.topk(query, k=KB_TOPK) → each hit {id, doc_id, title, text, score}.
	•	Dedupe by doc_id; keep top K = LIMIT → main_sections.

B2. Sections → Seeds
	•	Prefer reverse MENTIONED_IN if available (section → [entities]).
	•	Else: for each top section, extract aliases from entities.jsonl and match in title + first 300 chars:
	•	exact/contains; or fuzzy ratio ≥ 0.86.
	•	Aggregate counts → pick top 1–3 seeds (tie-break: favor HowTo/Concept).
	•	Optional product_scope: if Product appears in a majority of seeds (>50%), use it to filter neighbors.

B3. Graph Expand — Hop-1
	•	For each seed, get neighbors_idx[seed].
	•	Prioritize by:
	1.	relation type (NEXT_STEP > DEPENDS_ON/USES > TROUBLESHOOTS > SEE_ALSO),
	2.	relation_weight from ontology,
	3.	then edge.w.
	•	Apply fanout_cap_per_rel (from ontology).
	•	Filter by product_scope if set.

B4. Graph Expand — Hop-2
	•	For each hop-1 target H1:
	•	Expand neighbors_idx[H1] to H2.
	•	Constraints:
	•	No 2-edge loops: H2 != seed.
	•	No repeated nodes on the path.
	•	Apply the same priority and fanout rules as hop-1.
	•	Filter by product_scope if set.

B5. Entity → Evidence Sections (runtime)
	•	For every candidate (H1/H2), map entity → section via KB.by_entity(entity_id, 1).
	•	If no evidence is found, drop the candidate.

B6. Scoring & Diversification
	•	Hop-1 score:
score1 = 0.7 * relation_weight(rel1) + 0.3 * edge_w1
	•	Hop-2 path score:

score1 = 0.7 * relation_weight(rel1) + 0.3 * edge_w1
score2 = 0.7 * relation_weight(rel2) + 0.3 * edge_w2
score_path2 = 0.6 * score1 + 0.4 * score2      # weight earlier relation higher


	•	Remove duplicates (same target), and remove suggestions whose evidence section is already in main_sections.
	•	Apply MMR (λ = 0.3) over all (hop-1 + hop-2) candidates to select ≤ LIMIT diverse suggestions.

B7. Synthesize (no LLM — preview)
	•	Answer preview: list main_sections as:
	•	title + 200–220 char snippet + citation [section:...].
	•	Suggestions: 3–5 items with:
	•	title (prefer entities.aliases[0] or normalized id),
	•	target (entity id),
	•	badge = rel1 (for hop-2, optionally expose sub_badge = rel2),
	•	evidence (section id from KB),
	•	score,
	•	path:
	•	hop-1: [{"id": seed}, {"rel": rel1}, {"id": H1}]
	•	hop-2: [{"id": seed}, {"rel": rel1}, {"id": H1}, {"rel": rel2}, {"id": H2}]

5) Scoring & Ontology Rules
	•	Relation weights come from ontology.yaml → ranking.defaults.relation_weights.
Fallback defaults:
NEXT_STEP 0.95, DEPENDS_ON 0.90, USES 0.85, BELONGS_TO 0.90, TROUBLESHOOTS 0.80, SEE_ALSO 0.70, MENTIONED_IN 0.60.
	•	Display priority for badges: NEXT_STEP > DEPENDS_ON/USES > TROUBLESHOOTS > SEE_ALSO.
	•	Respect ontology constraints, e.g., relations[].constraints.acyclic: true for NEXT_STEP.

6) Output JSON (2 hops)

{
  "query": "How to create a test case in Katalon Studio?",
  "seed_entities": ["howto:create.test.case","product:katalon.studio"],
  "main_sections": ["section:k.s.create-test-cases#intro","section:k.s.manual-mode#add-steps"],
  "suggestions": [
    {
      "title": "Run Test Suite",
      "target": "howto:run.test.suite",
      "badge": "NEXT_STEP",
      "evidence": ["section:k.s.run-test-suites#intro"],
      "score": 0.92,
      "path": [
        {"id":"howto:create.test.case"},
        {"rel":"NEXT_STEP"},
        {"id":"howto:run.test.suite"}
      ]
    },
    {
      "title": "Data-driven Testing",
      "target": "feature:data.driven",
      "badge": "USES",
      "sub_badge": "NEXT_STEP",
      "evidence": ["section:k.s.data-driven#overview"],
      "score": 0.88,
      "path": [
        {"id":"howto:create.test.case"},
        {"rel":"NEXT_STEP"},
        {"id":"howto:run.test.suite"},
        {"rel":"USES"},
        {"id":"feature:data.driven"}
      ]
    }
  ],
  "answer_preview": "Q: ...\n1) Create Test Cases [section:...] ...\n2) Manual Mode [section:...] ..."
}

7) Fallbacks & Constraints
	•	No ontology: use default weights and fanout_cap_per_rel = 20.
	•	No seeds from top sections: seed with the most common Product (if available).
	•	No evidence for a candidate: drop it.
	•	NEXT_STEP acyclic: reject paths that form cycles (especially across 2 hops).
	•	Scope filter: if a product_scope is detected, drop neighbors out of scope.

8) Caching & Timeouts
	•	Cache KB.topk(query) by normalized query (TTL = CACHE_TTL_SEC).
	•	Cache KB.by_entity(eid) (TTL 5–10 minutes).
	•	Set KB call timeout ~800–1200 ms; fallback to last-good cache entry on timeout.

9) Acceptance (Demo)
	•	answer_preview contains ≥ 2 valid citations from KB.
	•	Suggestions include ≥ 1 hop-1 (prefer NEXT_STEP) and ≥ 1 hop-2 (when graph permits).
	•	No duplicate targets; do not reuse evidence already used in the answer.
	•	P95 end-to-end latency < 1.8s with caching.
	•	No NEXT_STEP cycles.

10) Pseudocode (integration sketch)

# KB search
hits = kb.topk(query, k=KB_TOPK)                  # [{id, doc_id, title, text, score}]
main_sections = dedupe_by_doc([h["id"] for h in hits])[:LIMIT]
hits_map = {h["id"]: h for h in hits}

# sections → seeds
seed_counts = Counter()
for h in hits[:LIMIT]:
    text = (h.get("title","") + " " + h.get("text","")[:300]).lower()
    for eid in alias_guess_from_text(text, alias_index):   # or reverse MENTIONED_IN if you have it
        seed_counts[eid] += 1
seeds = [eid for eid,_ in seed_counts.most_common(3)] or fallback_product(entities_by_id)
scope = majority_product(seeds, entities_by_id)  # optional

# hop-1
h1_list = []
for s in seeds:
    for n1 in neighbors_idx.get(s, []):
        if scope and not in_scope(n1["id"], scope): continue
        ev1 = kb.by_entity(n1["id"], limit=1)
        if not ev1: continue
        score1 = 0.7*rel_weight(n1["rel"]) + 0.3*float(n1.get("w",0))
        h1_list.append({"seed":s,"id":n1["id"],"rel1":n1["rel"],"ev":ev1,"score1":score1})

# hop-2
paths2 = []
for h1 in h1_list:
    for n2 in neighbors_idx.get(h1["id"], []):
        if n2["id"] == h1["seed"]: continue           # avoid 2-edge loop
        if scope and not in_scope(n2["id"], scope): continue
        ev2 = kb.by_entity(n2["id"], limit=1)
        if not ev2: continue
        score2 = 0.7*rel_weight(n2["rel"]) + 0.3*float(n2.get("w",0))
        path_score = 0.6*h1["score1"] + 0.4*score2
        paths2.append({
          "seed":h1["seed"],"mid":h1["id"],"id":n2["id"],
          "rel1":h1["rel1"],"rel2":n2["rel"],"ev":ev2,"score":path_score
        })

# unify candidates (hop-1 + hop-2), drop overlaps with main, apply MMR
cands = [
  {"target":p["id"],"badge":p["rel1"],"sub_badge":p.get("rel2"),
   "evidence":p["ev"],"score":p["score"],
   "path":[{"id":p["seed"]},{"rel":p["rel1"]},{"id":p["mid"]},{"rel":p["rel2"]},{"id":p["id"]}]}
  for p in paths2
] + [
  {"target":h1["id"],"badge":h1["rel1"],"evidence":h1["ev"],"score":h1["score1"],
   "path":[{"id":h1["seed"]},{"rel":h1["rel1"]},{"id":h1["id"]}]}
  for h1 in h1_list
]
cands = drop_overlap_with_main(cands, main_sections)
suggestions = mmr_select(sorted(cands, key=lambda x: x["score"], reverse=True), k=LIMIT, lambda_=0.3)

# answer preview (no LLM)
answer_preview = render_preview(query, main_sections, hits_map)

return {
  "query": query,
  "seed_entities": seeds,
  "main_sections": main_sections,
  "suggestions": suggestions,
  "answer_preview": answer_preview
}

If you want this tailored to your current code layout (files, module names), say the word and I’ll align identifiers and folder structure accordingly.

