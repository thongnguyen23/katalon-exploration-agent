Entry Points
- `retrieve_main.py` — CLI runner. Reads `.env`, loads indices, calls SectionProviderKB, returns JSON.

Key Modules
- `src/exploration_agents/kb_retriever.py` — wraps Bedrock KB `retrieve`; reused by SectionProviderKB.
- `src/exploration_agents/section_resolver.py` — resolves section IDs and extracts snippets.
- `src/exploration_agents/ontology_graph_builder.py` — defines ontology defaults used for relation weights.
- New `src/retrieve_kb2hops.py` — retrieval logic (seeds, expansion, scoring, MMR) [to be added in this branch].

Config
- Env keys:
  - `SECTIONS_PROVIDER=KB`
  - `KB_TOPK=20`, `LIMIT=5`, `LANG=vi`
  - `GRAPH_DIR=artifacts/graph`, `ONTOLOGY_PATH=configs/ontology.yaml`
  - `ENTITIES_FILE=entities.jsonl`, `NEIGHBORS_FILE=neighbors.jsonl`
  - `CACHE_TTL_SEC=60`, `CACHE_SIZE_DOCS=512`

Artifacts
- `artifacts/graph/entities.jsonl` — {id,type,aliases[],sources[]}
- `artifacts/graph/neighbors.jsonl` — {id, neighbors:[{id,rel,w}]}

Validation Notes
- Prefer reverse MENTIONED_IN for seeds; alias fuzz ≥ 0.86 fallback.
- 2-hop expansion with acyclic NEXT_STEP; scope filter by majority Product.
- MMR(λ=0.3) across hop-1 + hop-2; drop overlap with main sections.
