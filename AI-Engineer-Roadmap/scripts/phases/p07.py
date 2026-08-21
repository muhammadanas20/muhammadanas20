from make_phase import C, E, EX, I, Q, asg, drill, mp, phase, th

PHASE = phase(
    num="7",
    title="Vector databases",
    tagline="Pick a store on purpose: Chroma, pgvector, Qdrant, and the paid ones.",
    hours="7-10 days",
    difficulty="Medium",
    exit_ticket="The same dataset in two stores, plus a 1–2 page tradeoff memo.",
    objectives=[
        "Explain what a vector DB adds over a numpy matrix.",
        "Run Chroma locally and pgvector in Postgres.",
        "Know Qdrant, Weaviate, Milvus, Pinecone well enough to compare.",
        "Use metadata filters and payload indexes.",
        "Plan backup, tenancy, and cost.",
    ],
    prerequisites=["Phase 6. Docker from Phase 4. Postgres from Phase 2."],
    topics=["Chroma", "Qdrant", "Pinecone", "Milvus", "pgvector", "Weaviate", "filters", "HNSW"],
    nav="[Home](../../README.md) · Prev: [Phase 6](../06-embeddings-search/) · Next: [Phase 8 · RAG](../08-rag/)",
    theory=th(
        intro="""A **vector database** stores embeddings plus payload (the chunk text and metadata) and answers: *given this vector, what are the nearest neighbors, optionally filtered by metadata?*

It is not magic. It is an index (often **HNSW** or IVF) plus ops features: persistence, concurrent writes, replicas, filters.

You already did the hard part in Phase 6 (chunking, embedding). This phase is *where the vectors live*.""",
        one_liner="A vector DB is nearest-neighbor search with persistence, filters, and operations.",
        why="""Numpy files do not give you:

- Concurrent writers
- Metadata filters at scale (`tenant_id = X AND year >= 2024`)
- Replication
- Incremental upserts
- A network API your API containers can share

At 2,000 chunks, Chroma or pgvector is plenty. At 20 million, you will care about the engine.""",
        if_missing="you would either keep JSONL forever or pick Pinecone because a tutorial did.",
        analogy="""Phase 6 was a pile of GPS coordinates on a paper map.

A vector DB is a **GIS system**:

- **Index (HNSW)** = highways so you do not compare to every house
- **Payload** = the house's address and owner (chunk text, tenant)
- **Filter** = 'only houses in this zip code'
- **Collection / index name** = a map layer
- **Cloud vs self-host** = Google Maps vs printing your own atlas""",
        visual="""```mermaid
flowchart TB
  App --> API[Vector DB API]
  API --> Index[HNSW / IVF]
  API --> Payload[Chunk text + metadata]
  API --> Filter[Payload index]
```""",
        architecture="""```mermaid
flowchart LR
  FastAPI --> PG[(Postgres + pgvector)]
  FastAPI --> QD[(Qdrant)]
  FastAPI --> CH[(Chroma local)]
  PG ---|also| SQL[Users, chats]
```

A common production shape: **Postgres for truth**, vectors either in **pgvector** (one system) or **Qdrant** (specialized) with `chunk_id` as the join key.""",
        beginner="""**Collection / index:** a named bucket of vectors of a fixed dimension.

**Upsert:** insert or replace by id.

**Top-k search:** nearest neighbors.

**Metadata filter:** `where tenant_id = ...` applied with search.

**Chroma:** easy local embedded DB. Great for learning and small apps.

**pgvector:** Postgres extension. You already have Postgres. SQL + vectors together.

**Qdrant:** open source, production-friendly, excellent filters.

**Pinecone:** managed cloud. Fast to start, cost and lock-in to watch.

**Weaviate / Milvus:** capable OSS/cloud; more moving parts.

**Dimension** must match the embedding model. 768 ≠ 1536.""",
        intermediate="""**HNSW:** graph-based ANN. Parameters `M` and `ef` trade recall vs latency/memory.

**IVF:** clusters first, search some clusters. Different tradeoff.

**Payload indexes:** without them, filters may scan.

**Id strategy:** use your chunk hash or UUID, not '1,2,3' that shift when you re-chunk.

**Hybrid in-engine:** some DBs (Qdrant, Weaviate) can fuse sparse + dense.

**Consistency:** when is a write searchable? Know at-least-eventually vs sync.

**Multi-tenancy:** 
- payload filter `tenant_id` (simple, risk if you forget the filter)
- separate collections per tenant (isolation, ops cost)
- true tenant features if the engine has them""",
        advanced="""**Quantization** (scalar/product/binary) shrinks RAM at a recall cost.

**Sharding and replication.**

**Disk-based indexes** vs RAM.

**GPU indexes** (Milvus etc.) — rare for junior work.

**Schema evolution:** adding payload fields, rebuilding HNSW.

**CDC from Postgres to Qdrant** if PG is the source of truth.

**SLO:** p95 search < 50ms is a common target; measure with filters on.""",
        production="""Backups: snapshots of the vector store AND the document store. You must be able to **rebuild from documents** if the index corrupts — that is why you stored raw chunks and model id.

Cost: RAM-heavy. Don't put 10 copies of the same corpus in 10 collections 'for now'.

Never expose the vector DB to the internet. It sits on the private network like Redis.""",
        when="Shared, persistent, filtered vector search. Multiple app workers.",
        when_not="20 documents (send them). Pure SQL lookups. You have not measured that numpy is too slow.",
        code_preview='''# Chroma sketch
col.add(ids=ids, embeddings=vecs, documents=texts, metadatas=metas)
hits = col.query(query_embeddings=[q], n_results=5, where={"tenant": "acme"})
''',
        code_notes="The API is upsert + query + filter. Every vendor rhymes.",
        ex_b="Put 50 chunks in Chroma. Query. Print documents.",
        ex_m="pgvector table + IVFFlat or HNSW index. Same 50 chunks. Compare results.",
        ex_h="Qdrant in Docker with a payload index on tenant_id. Prove a forgotten filter is a data leak in a test.",
        project="Two-store comparison memo — MiniProject.md.",
        interview_preview="Why not numpy? HNSW vs exact. pgvector vs Qdrant vs Pinecone. Multi-tenant filters.",
        flash_sample="**Q:** What must match between embedder and collection?\n**A:** Dimension (and the model, conceptually).",
        mistakes_preview="No filter on tenant. Recreating collections every request. Storing vectors without the text. Using cosine in a DB configured for L2.",
        debug_preview="Empty results after filter (type mismatch string vs int). Dimension error on upsert.",
        best="Source of truth is documents. Vectors are a rebuildable index. Filter always. Metric matches embeddings. Private network.",
        industry="2025–2026: pgvector for many startups until scale hurts; Qdrant/Weaviate self-host; Pinecone/Turso-like managed when ops budget is zero.",
        perf="Warm indexes. Batch upserts. Payload indexes. Don't fetch 1000 neighbors to rerank 5 without need.",
        security="Network policy. Tenant filter tests. Auth on the DB. Don't log full payloads with PII.",
        refs="- pgvector README\n- Qdrant docs\n- Chroma docs\n- Pinecone learning center (vendor)",
        further="HNSW paper (Malkov & Yashunin). Faiss wiki.",
    ),
    examples=[
        EX(
            title="In-memory Chroma-shaped API (no extra daemon)",
            why="Learn the operations: add, query, filter.",
            code='''"""code/toy_store.py"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np

@dataclass
class Hit:
    id: str
    score: float
    text: str
    meta: dict

class ToyStore:
    def __init__(self, dim: int) -> None:
        self.dim = dim
        self.ids: list[str] = []
        self.vecs: list[np.ndarray] = []
        self.texts: list[str] = []
        self.meta: list[dict] = []

    def upsert(self, id: str, vec: np.ndarray, text: str, meta: dict | None = None) -> None:
        assert vec.shape == (self.dim,)
        if id in self.ids:
            i = self.ids.index(id)
            self.vecs[i], self.texts[i], self.meta[i] = vec, text, meta or {}
            return
        self.ids.append(id)
        self.vecs.append(vec)
        self.texts.append(text)
        self.meta.append(meta or {})

    def query(self, vec: np.ndarray, k: int = 3, where: dict | None = None) -> list[Hit]:
        hits: list[Hit] = []
        q = vec / (np.linalg.norm(vec) + 1e-12)
        for i, v in enumerate(self.vecs):
            if where and any(self.meta[i].get(k) != val for k, val in where.items()):
                continue
            s = float((v / (np.linalg.norm(v) + 1e-12)) @ q)
            hits.append(Hit(self.ids[i], s, self.texts[i], self.meta[i]))
        hits.sort(key=lambda h: -h.score)
        return hits[:k]
''',
            line_by_line="upsert by id, cosine query, metadata AND filter. This is 90% of every vendor SDK.",
            output="Hit list sorted by score.",
            dry_run="Insert N vectors. Filter some out. Sort remaining by cosine.",
            memory="O(N D) like numpy — this toy has no HNSW.",
            time="O(N D)",
            space="O(N D)",
            alternatives="Chroma, pgvector, Qdrant.",
            optimization="HNSW when N grows. Payload index for filters.",
        ),
        EX(
            title="pgvector SQL",
            why="You already operate Postgres.",
            code='''"""code/pgvector.sql -- run inside Postgres with the extension"""
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE chunks (
  id UUID PRIMARY KEY,
  doc_id UUID NOT NULL,
  tenant_id TEXT NOT NULL,
  body TEXT NOT NULL,
  embedding vector(768) NOT NULL
);

CREATE INDEX chunks_hnsw ON chunks USING hnsw (embedding vector_cosine_ops);
CREATE INDEX chunks_tenant ON chunks (tenant_id);

-- query (application binds $1 as vector, $2 as tenant)
-- SELECT id, body, 1 - (embedding <=> $1) AS score
-- FROM chunks
-- WHERE tenant_id = $2
-- ORDER BY embedding <=> $1
-- LIMIT 5;
''',
            line_by_line="`vector(768)` must match the model. `<=>` is cosine distance in pgvector. Filter on tenant_id **in the same query**.",
            output="Rows of nearest chunks.",
            dry_run="Planner uses HNSW + tenant index depending on selectivity.",
            memory="HNSW in RAM/shared buffers.",
            time="Sublinear in N with HNSW; still measure with filters.",
            space="Vectors + graph.",
            alternatives="IVFFlat (rebuild-friendly), Qdrant for heavier filter trees.",
            optimization="Partial indexes per tenant if tenants are huge and few.",
        ),
    ],
    practice=[
        drill("Chroma hello", "Add 10 docs, query, delete one, query again.", "You saw upsert/delete."),
        drill("Docker Qdrant", "compose a Qdrant, open the dashboard, create a collection.", "You can click a vector."),
        drill("Dimension mismatch", "Try to insert 384-d into 768-d. Read the error.", "You will recognize it in 50ms next time."),
    ],
    exercises={
        "beginner": [
            E("Chroma persist", "Persist to ./chroma_data, restart process, query still works.", "Not in-memory only."),
            E("Metadata filter", "Two tenants. Query with and without filter. Screenshot.", "Show the leak without filter."),
        ],
        "medium": [
            E("pgvector", "Store the Phase 6 notes index in PG. Compare top-5 to numpy.", "Overlap table."),
            E("Idempotent upsert", "Re-run ingest. Row count stays stable.", "Primary key = chunk hash."),
        ],
        "hard": [
            E("Tradeoff memo", "2 pages: Chroma vs pgvector vs Qdrant vs Pinecone for a 5M-chunk SaaS.", "Include cost, ops, filters, lock-in, backup."),
        ],
    },
    assignments=[
        asg(
            "two-store lab",
            "1 day",
            "Index the same Markdown corpus into Chroma and pgvector. Query 10 questions. Compare hits. Write TRADEOFFS.md.",
            ["code", "compose", "TRADEOFFS.md"],
            ["reproducible", "filters demo", "honest 'what I would pick'"],
        )
    ],
    quiz=[
        Q("A vector DB primarily answers", "SQL joins of money", "Nearest neighbors + filters", "Train GPTs", "Render HTML", "B", "kNN + ops."),
        Q("HNSW is", "A prompt", "An ANN index graph", "A JWT alg", "A Docker base", "B", "Approximate NN."),
        Q("pgvector lives in", "Redis", "Postgres", "The browser", "S3 only", "B", "Extension."),
        Q("Dimension mismatch", "Is silently ok", "Errors or corrupts search", "Improves recall", "Is cosine", "B", "Must match."),
        Q("Multi-tenant minimum", "Hope", "tenant_id filter (and tests)", "One shared vector for all", "Email the vendor", "B", "Filter + tests."),
        Q("Chroma is great for", "Learning and small apps", "Global 10B vector search as a first choice", "Replacing Postgres chats", "OS kernels", "A", "Right-sized."),
        Q("Vectors without stored text", "Are enough to cite", "Cannot show the user the passage", "Train better", "Are smaller so always better", "B", "Keep payload."),
        Q("Pinecone is", "OSS you must host", "A managed vector service", "A tokenizer", "A FastAPI clone", "B", "Managed."),
        Q("Metric mismatch (cosine vs L2)", "Does not matter", "Can ruin ranking", "Only affects backups", "Fixes filters", "B", "Match embedder."),
        Q("Rebuildability", "Optional", "Required — documents are source of truth", "Illegal", "Only for Redis", "B", "Index can be rebuilt."),
    ],
    flashcards=[
        C("What does a vector DB add over numpy?", "Persistence, filters, concurrency, ANN, ops."),
        C("HNSW?", "Hierarchical navigable small world — ANN graph."),
        C("pgvector operator <=> ?", "Distance (cosine distance if vector_cosine_ops)."),
        C("Collection dimension?", "Must equal embedding size."),
        C("Qdrant strength?", "Filters, OSS, production features."),
        C("When Pinecone?", "Want managed, ok with cost/lock-in."),
        C("Payload?", "Stored text + metadata beside the vector."),
        C("Why chunk hash ids?", "Stable upserts when re-ingesting."),
        C("Quantization?", "Compress vectors, trade recall for RAM."),
        C("Expose Qdrant to internet?", "No."),
    ],
    interview=[
        I("pgvector vs dedicated vector DB?", "pgvector: one system, transactions, smaller scale. Dedicated: heavier filters, scale, ANN knobs. Start with pgvector if already on PG.", "Always Pinecone. Never pgvector.", "Numbers: millions vs tens of millions, team ops skill, hybrid, cost."),
        I("How do you isolate tenants?", "Filter every query; tests that fail when filter omitted; maybe separate collections or RLS.", "We remember to filter.", "Crypto isolation, per-tenant encryption keys, query planner leaks."),
        I("What is HNSW?", "A graph ANN index. Faster than brute force, approximate. Parameters trade recall and memory.", "A neural net. A hash of the prompt.", "M, efSearch, efConstruction, memory vs IVF."),
        I("Backup story?", "Backup documents + embeddings config; vector index snapshots optional because we can rebuild. Test a restore.", "We take Docker volumes sometimes.", "RPO/RTO, rebuild time SLOs."),
        I("Why Chroma in tutorials and not in your design?", "Fast learning loop. For prod I need backups, HA, filters at scale — maybe Qdrant/pgvector.", "Chroma is fake.", "Embedded vs client-server Chroma, and when it is actually enough."),
    ],
    whiteboard=[
        "Architecture: FastAPI, Postgres, Qdrant. Where is the source of truth?",
        "Tenant filter forgotten — draw the leak and the test.",
        "Estimate RAM: 10M vectors × 768-d float32 + HNSW overhead ~1.5–2x.",
    ],
    interview_listen="tradeoffs and tenancy, not memorized vendor feature lists",
    cheatsheet={
        "remember": "Rebuildable index. Match dim + metric. Filter tenant. Don't expose. pgvector is a valid start.",
        "bash": "docker compose up qdrant postgres\n# chroma persist dir ./chroma_data",
        "python": "col.query(query_embeddings=[q], n_results=5, where={'tenant': tid})",
        "decisions": "< few million + have PG → pgvector. Need fancy filters/scale → Qdrant. No ops team → managed.",
        "numbers": "HNSW RAM often 1.5–3× raw vectors. p95 search tens of ms typical.",
        "do_not": "Internet-exposed DB. Metric mismatch. Vectors without text. Forget tenant filter.",
    },
    miniproject=mp(
        name="two-store-lab",
        time="1–2 days",
        difficulty="Medium",
        why="Hiring managers ask 'why this store?'",
        story="I can defend pgvector vs Chroma with numbers on MY corpus.",
        must=["two stores", "same 10 queries", "TRADEOFFS.md", "compose"],
        should=["Qdrant as a third optional"],
        wont=["Production HA cluster"],
        architecture="```mermaid\nflowchart LR\nCorpus --> Chroma\nCorpus --> pgvector\nQ --> Compare\n```",
        layout="stores/ chroma/ pg/ TRADEOFFS.md",
        rubric=["numbers", "tenancy paragraph", "pick one and why"],
        stretch="Cost estimate at 5M chunks.",
    ),
    resources={
        "official": ["pgvector GitHub", "Qdrant docs", "Chroma docs", "Weaviate docs", "Milvus docs", "Pinecone docs"],
        "extra": ["HNSW paper", "Faiss documentation"],
        "papers": ["Efficient and robust approximate nearest neighbor search using HNSW graphs"],
    },
    faq=[
        {"q": "Must I learn all six?", "a": "No. Hands-on two (Chroma + pgvector). Read the others enough to compare. That is the exit ticket."},
        {"q": "Redis vector search?", "a": "Exists (RediSearch). Fine as a cache of vectors, not usually your system of record."},
        {"q": "Elasticsearch/OpenSearch kNN?", "a": "Valid if the company already runs them. Not our default."},
    ],
    debugging=[
        {
            "title": "Wrong dimension",
            "symptom": "API 400 / SQL error on insert.",
            "wrong": "Collection created for another model.",
            "see": "Get collection info. Print embedding.shape.",
            "fix": "New collection + re-embed, or match the model.",
            "prevent": "Model id in collection name: `notes_bge_small_v1`.",
        },
        {
            "title": "Filter returns nothing",
            "symptom": "Unfiltered works.",
            "wrong": "where={'tenant': 1} vs '1' string.",
            "see": "Print stored payload types.",
            "fix": "Consistent types. Schema.",
            "prevent": "Pydantic on metadata.",
        },
    ],
    mistakes=[
        {"title": "New collection every process start", "body": "You re-embed the world on each deploy.", "instead": "Named persistent collection + idempotent upsert."},
        {"title": "Trusting dashboard counts", "body": "Off-by-one after failed batch.", "instead": "Application-level checksums vs document store."},
        {"title": "L2 index with cosine embeddings", "body": "Ranking looks 'almost ok' and you waste a week.", "instead": "Read the vendor metric docs. Match."},
    ],
    prod_tips={
        "cost": "RAM is the bill. Quantize or dedicated engine when numpy/PG hurts. Managed DBs charge for units — read the invoice math.",
        "latency": "Measure with filters and with cold start. HNSW efSearch is a knob.",
        "reliability": "Rebuild playbook. Snapshots. Don't be the person who can only restore chats but not search.",
        "observability": "Log collection, k, filter, latency, result ids.",
        "scaling": "Vertical then shards. Don't shard at 20k vectors.",
        "checklist": ["dim match", "metric match", "tenant tests", "backup/rebuild", "private net"],
    },
    challenge={
        "title": "Filtered recall",
        "body": "Show HNSW + highly selective filter hurting recall. Mitigate with payload index / more ef / prefilter strategy as the engine allows.",
        "constraints": ["A plot or table", "Engine named"],
        "success": "You can talk about pre vs post filtering.",
    },
    solutions=[
        {"id": "M1 overlap", "hint": "Compare id sets of top-5.", "approach": "Jaccard of result ids. Disagreements: read the chunks — maybe both are valid."},
        {"id": "H1 memo", "hint": "Table: ops, cost, filters, hybrid, lock-in, max comfortable N.", "approach": "Pick one for a fictional company with constraints."},
    ],
    code_files={
        "toy_store.py": '''"""Minimal vector store API: upsert, cosine query, metadata filter."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class Hit:
    id: str
    score: float
    text: str
    meta: dict


class ToyStore:
    def __init__(self, dim: int) -> None:
        self.dim = dim
        self.ids: list[str] = []
        self.vecs: list[np.ndarray] = []
        self.texts: list[str] = []
        self.meta: list[dict] = []

    def upsert(self, id: str, vec: np.ndarray, text: str, meta: dict | None = None) -> None:
        assert vec.shape == (self.dim,)
        if id in self.ids:
            i = self.ids.index(id)
            self.vecs[i], self.texts[i], self.meta[i] = vec, text, meta or {}
            return
        self.ids.append(id)
        self.vecs.append(vec)
        self.texts.append(text)
        self.meta.append(meta or {})

    def query(self, vec: np.ndarray, k: int = 3, where: dict | None = None) -> list[Hit]:
        hits: list[Hit] = []
        q = vec / (np.linalg.norm(vec) + 1e-12)
        for i, v in enumerate(self.vecs):
            if where and any(self.meta[i].get(key) != val for key, val in where.items()):
                continue
            s = float((v / (np.linalg.norm(v) + 1e-12)) @ q)
            hits.append(Hit(self.ids[i], s, self.texts[i], self.meta[i]))
        hits.sort(key=lambda h: -h.score)
        return hits[:k]
''',
        "pgvector.sql": """CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE chunks (
  id UUID PRIMARY KEY,
  doc_id UUID NOT NULL,
  tenant_id TEXT NOT NULL,
  body TEXT NOT NULL,
  embedding vector(768) NOT NULL
);

CREATE INDEX chunks_hnsw ON chunks USING hnsw (embedding vector_cosine_ops);
CREATE INDEX chunks_tenant ON chunks (tenant_id);
""",
    },
)
