from make_phase import C, E, EX, I, Q, asg, drill, mp, phase, th

PHASE = phase(
    num="6",
    title="Embeddings and search",
    tagline="Text becomes geometry. Search becomes nearest neighbors. Chunking is the hidden boss fight.",
    hours="7-10 days",
    difficulty="Medium",
    exit_ticket="Semantic search over a real folder of Markdown files you can explain line by line.",
    objectives=[
        "Explain what an embedding is (and is not).",
        "Choose cosine vs L2 vs dot product with a reason.",
        "Chunk documents without destroying headings and tables.",
        "Load files (Markdown, HTML, PDF text) into a pipeline.",
        "Build a tiny semantic search that beats grep on paraphrases.",
        "Know when keyword search still wins.",
    ],
    prerequisites=["Phase 5. You know what a token is."],
    topics=["Embeddings", "similarity", "chunking", "loaders", "semantic search", "hybrid intro"],
    nav="[Home](../../README.md) · Prev: [Phase 5](../05-llm-fundamentals/) · Next: [Phase 7 · Vector DBs](../07-vector-databases/)",
    theory=th(
        intro="""An **embedding** is a list of numbers (a vector) that represents a piece of text so that *similar meaning* sits nearby in space.

If 'reset password' and 'I forgot my login' land close together, search can find the right article even when the words differ.

This phase is retrieval **without** a fancy database. A numpy matrix is enough to learn. Phase 7 puts the same vectors into real stores.""",
        one_liner="Embeddings turn meaning into coordinates you can search.",
        why="""Keyword search fails on paraphrases. LLMs fail on facts they were not given.

Embeddings sit in the middle: cheap, fast, good enough to find the 5 paragraphs the model should read.

If your chunks are garbage, your RAG is garbage. Most 'the model is dumb' tickets are chunking tickets.""",
        if_missing="you would paste entire PDFs into the prompt or grep exact words and call it AI.",
        analogy="""A library that shelves books by *topic vibe*, not alphabet.

- Each chunk is a book with a GPS coordinate (the vector).
- A question is also given a GPS coordinate.
- Search = find the nearest books.
- **Chunking** = tearing chapters into pamphlets. Tear through a table and the pamphlet is nonsense.
- **Overlap** = repeating the last paragraph so sentences that straddled a cut still live together.
- **Keyword search** = the old card catalog. Still better for SKUs, error codes, names.""",
        visual="""```mermaid
flowchart LR
  D[Documents] --> Split[Chunk]
  Split --> Emb[Embedding model]
  Q[Query] --> EmbQ[Same embedding model]
  Emb --> M[Matrix of vectors]
  EmbQ --> NN[Nearest neighbors]
  M --> NN
  NN --> Hits[Top-k chunks]
```""",
        architecture="""```mermaid
flowchart TB
  subgraph ingest
    L[Loader] --> C[Chunker] --> E[Embed] --> S[Store]
  end
  subgraph query
    U[User] --> QE[Embed query] --> R[kNN / hybrid] --> Out[Chunks + scores]
  end
  S --> R
```""",
        beginner="""**Vector:** `[0.12, -0.44, ...]` with hundreds or thousands of dimensions.

**Embedding model:** a smaller model than a chat LLM, trained so similar text has similar vectors. Examples: `nomic-embed-text`, `bge-m3`, `text-embedding-3`.

**Similarity:**
- **Cosine** = angle between vectors (most common for text)
- **Dot product** = like cosine if vectors are normalized
- **L2 / Euclidean** = straight-line distance

**Chunk:** a slice of a document you embed as one unit. 200–800 tokens is a common band. Not a law.

**Overlap:** 10–20% repeated between neighbors.

**kNN:** k nearest neighbors — the k closest vectors to the query.

**Loader:** code that turns a file into text (and metadata like path, heading).""",
        intermediate="""**You must use the same embedding model at query time as at ingest.** Mixing models is a silent failure — scores look numeric and are meaningless.

**Metadata** (source, heading, date, tenant) is not embedded by accident. You store it beside the vector for filters.

**Recursive / structure-aware chunking:** split on headings, then paragraphs, then sentences. Better than `text[i:i+500]`.

**Tables and code:** keep them intact; they die when sliced mid-row.

**Semantic vs keyword:** error code `ECONNRESET` wants keyword. 'why did my upload fail' wants semantic. **Hybrid** (Phase 8) does both.

**ANN vs exact kNN:** exact is fine to 10k–100k vectors in RAM. Then use HNSW etc (Phase 7).""",
        advanced="""**Matryoshka embeddings:** truncate dimensions for cheaper search with a small quality hit.

**Late chunking / long-context embedders:** embed with more surrounding context.

**ColBERT / multi-vector:** one vector per token, richer matching, heavier.

**Domain drift:** an embedding model trained on web text may be weak on legal citations. Measure.

**Dimensionality:** 384 is fast; 1024–3072 often better. Not linear.

**Normalization:** cosine assumes you understand whether the vendor already L2-normalized.""",
        production="""Version the embedding model id on every row. If you change models, **re-embed the corpus**. Store `chunk_text`, `hash`, `doc_version`. Rebuild must be a button you have pressed.

Eval: a set of (query, relevant chunk ids). Metric: recall@k, MRR. Do this before you add an LLM — retrieval eval is cheaper and more honest.""",
        when="Search, clustering, dedup, RAG retrieval, recommendation of similar tickets.",
        when_not="When exact match is required (IDs, SKUs) — use SQL/keyword. When you have 3 documents — just send them. When legal needs guaranteed phrase match.",
        code_preview="""# pseudo
vecs = embed(chunks)           # (N, D)
q = embed([query])[0]          # (D,)
scores = vecs @ q              # if normalized, this is cosine
idx = scores.argmax()
""",
        code_notes="Normalized dot product = cosine. One matrix multiply is the whole search engine at small N.",
        ex_b="Embed 10 sentences. Print the nearest pair.",
        ex_m="Chunk this course's README by headings. Search 'what is a token?'.",
        ex_h="Compare 3 chunk sizes on 15 handwritten queries. Report recall@5.",
        project="Folder search CLI — MiniProject.md.",
        interview_preview="What is an embedding? Why same model? How do you chunk a PDF with tables? Cosine vs L2.",
        flash_sample="**Q:** Can I embed with model A and query with model B?\n**A:** No. The spaces are different.",
        mistakes_preview="Fixed 500-char slices through tables. Forgetting overlap. Embedding the query with a chat model. No metadata.",
        debug_preview="All scores ~0.1 and random. (Wrong model, or unnormalized mix.)",
        best="Structure-aware chunks. Same model. Metadata. Eval set of 25 queries. Version the model id.",
        industry="sentence-transformers, OpenAI embeddings, Cohere, Voyage, Nomic. Chunking libraries: unstructured, llama-index node parsers — understand them before importing.",
        perf="Batch embed. Approximate NN later. Cache query embeddings. Don't re-embed unchanged hashes.",
        security="Embeddings can leak information (inversion research). Don't embed secrets. Tenant-filter before kNN results leave the box.",
        refs="- Dense Passage Retrieval (Karpukhin 2020)\n- sentence-transformers docs\n- Lost in the Middle (why not to skip chunking and dump)",
        further="Pinecone/Qdrant learning centers (vendor-aware). Hybrid search intro in Phase 8.",
    ),
    examples=[
        EX(
            title="Cosine search in pure numpy",
            why="If you cannot do this, a vector DB is a black box.",
            code='''"""code/cosine_search.py"""
from __future__ import annotations

import numpy as np

def normalize(x: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(x, axis=1, keepdims=True) + 1e-12
    return x / n

def search(index: np.ndarray, query: np.ndarray, k: int = 3) -> tuple[np.ndarray, np.ndarray]:
    """index (N, D), query (D,) both unnormalized. Returns (indices, scores)."""
    idx_n = normalize(index)
    q_n = query / (np.linalg.norm(query) + 1e-12)
    scores = idx_n @ q_n
    k = min(k, scores.shape[0])
    top = np.argpartition(-scores, kth=k - 1)[:k]
    order = top[np.argsort(-scores[top])]
    return order, scores[order]

if __name__ == "__main__":
    rng = np.random.default_rng(0)
    index = rng.normal(size=(100, 8))
    query = index[42] + 0.01 * rng.normal(size=(8,))
    ids, sc = search(index, query, k=3)
    print(ids, sc.round(3))
''',
            line_by_line="Normalize rows to unit length. Dot product = cosine. argpartition is O(N) for top-k, faster than full sort.",
            output="[42 ...] with the first score ~1.0",
            dry_run="Build random index. Query near row 42. Cosine peak at 42.",
            memory="O(N*D) for the matrix. 10k * 768 * 4 bytes ≈ 30MB.",
            time="O(N D) brute force",
            space="O(N D)",
            alternatives="faiss, hnswlib, a vector DB.",
            optimization="ANN when N is large. Filter metadata first if selective.",
        ),
        EX(
            title="Heading-aware chunker (Markdown)",
            why="Naive windows murder documentation.",
            code='''"""code/chunk_md.py"""
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Chunk:
    heading: str
    text: str

def chunk_markdown(md: str, max_chars: int = 800) -> list[Chunk]:
    chunks: list[Chunk] = []
    heading = "root"
    buf: list[str] = []

    def flush() -> None:
        text = "\\n".join(buf).strip()
        if text:
            chunks.append(Chunk(heading=heading, text=text))
        buf.clear()

    for line in md.splitlines():
        if line.startswith("#"):
            flush()
            heading = line.lstrip("#").strip() or heading
            continue
        buf.append(line)
        if sum(len(x) for x in buf) >= max_chars:
            flush()
    flush()
    return chunks
''',
            line_by_line="Split on headings first. Only then apply a size cap. Each chunk keeps the heading as metadata for citations.",
            output="A list of Chunk(heading=..., text=...)",
            dry_run="See a # line → flush previous buffer, start new heading.",
            memory="O(document)",
            time="O(n) characters",
            space="O(n)",
            alternatives="RecursiveCharacterTextSplitter; HTML header splits; PDF by pages (worse) vs by layout (better).",
            optimization="Token-length not chars. Keep overlap of last 1–2 sentences.",
        ),
    ],
    practice=[
        drill("Nearest neighbor by hand", "Draw 5 points on paper in 2D. Query point. Rank cosine vs L2 if one vector is very long.", "You can say when L2 and cosine disagree."),
        drill("Break a table", "Chunk a Markdown table with a 40-char window. Read the chunks. Feel the pain.", "You refuse to ship that splitter."),
        drill("Grep vs semantic", "Find a paraphrase in this course that grep misses and embeddings catch.", "One screenshot or note."),
    ],
    exercises={
        "beginner": [
            E("Ten sentences", "Embed with a local model (or fake vectors) and print a similarity matrix.", "Same model for all."),
            E("Metadata", "Each chunk stores path + heading. Filter search to one file.", "Filter happens before or after kNN — document which."),
        ],
        "medium": [
            E("Token chunker", "Chunk by tiktoken counts not chars, overlap 50 tokens.", "No chunk exceeds 400 tokens."),
            E("Eval mini", "12 queries with labeled files. Report recall@3.", "Do not tune on the same 12 until you freeze them first."),
        ],
        "hard": [
            E("Hybrid preview", "Combine BM25 (or simple TF-IDF) with cosine using a weighted sum. Compare to either alone.", "Table of three systems on the 12 queries."),
        ],
    },
    assignments=[
        asg(
            "notes-search",
            "6 hours",
            "CLI: index a folder of Markdown, persist numpy + jsonl, query from CLI, show path, heading, score, snippet.",
            ["indexer", "query CLI", "5 example queries", "README"],
            ["same model documented", "chunks keep metadata", "re-index is idempotent on unchanged files"],
        )
    ],
    quiz=[
        Q("An embedding is", "A JPEG of the text", "A vector representing meaning", "A Git commit", "A JWT", "B", "Geometry of meaning."),
        Q("Query with a different embedding model", "Is faster", "Is invalid / incomparable", "Is required", "Increases recall always", "B", "Different spaces."),
        Q("Cosine similarity cares about", "Mostly direction/angle", "Only vector length", "File size", "CPU vendor", "A", "Angle."),
        Q("A good reason for overlap", "It looks professional", "Sentences spanning a cut stay together", "It reduces storage", "It trains the LLM", "B", "Boundary context."),
        Q("Error code ECONNRESET is best found with", "Only 3072-d embeddings", "Keyword / exact", "Temperature 2", "Docker", "B", "Identifiers."),
        Q("Chunking through a table is", "Fine", "Usually destructive", "Required", "A kind of embedding", "B", "Keep tables whole."),
        Q("k in kNN is", "The vector dimension", "How many neighbors to return", "The learning rate", "Token count", "B", "Top-k."),
        Q("Re-embed the corpus when", "You change the embedding model", "You change CSS", "You add a JWT", "Never", "A", "New space."),
        Q("Metadata is for", "Filters and citations", "Replacing vectors", "Training GPT", "TLS", "A", "Beside the vector."),
        Q("Brute-force cosine is", "O(N D)", "O(1)", "O(log N) always", "Impossible", "A", "Until ANN."),
    ],
    flashcards=[
        C("Same model at ingest and query?", "Yes. Always."),
        C("Typical chunk size?", "Hundreds of tokens, structure first."),
        C("Cosine vs L2?", "Cosine = angle; L2 = distance; normalize and they relate."),
        C("What is recall@k?", "Fraction of queries where a relevant chunk appears in top k."),
        C("Why metadata?", "Filter (tenant, date) and cite (path, heading)."),
        C("ANN?", "Approximate nearest neighbor — faster, slightly less exact."),
        C("When keyword wins?", "IDs, codes, names, exact phrases."),
        C("What is a loader?", "File → text + metadata."),
        C("Matryoshka?", "Embeddings you can truncate."),
        C("Hash chunks?", "Skip re-embedding unchanged text."),
    ],
    interview=[
        I("What is an embedding?", "A vector such that similar meanings are close. Produced by an embedding model, not by a chat model (usually).", "Calling ChatGPT 'the embedding'. Confusing tokens with vectors.", "MTEB, domain shift, dim vs quality, late interaction models."),
        I("How do you chunk a messy PDF?", "Extract structure if possible; split by headings/pages as fallback; keep tables; overlap; store page numbers.", "500-char slices. OCR ignored.", "Layout models, parent-child, multimodal embeddings for figures."),
        I("Cosine or L2?", "Cosine for text when we care about orientation. If the vendor says normalize + dot, do that.", "Random choice.", "Inner product indexes, metric must match the index."),
        I("How do you know retrieval works without an LLM?", "Gold queries, recall@k, MRR, looking at the actual chunks.", "Only vibe-checking the chatbot.", "nDCG, contamination, inter-annotator agreement."),
        I("Hybrid search in one minute.", "Keyword (BM25) plus dense vectors, fuse scores, often then rerank.", "Hybrid means two vector DBs.", "RRF, learned fusion, query routing."),
    ],
    whiteboard=[
        "Draw ingest vs query paths. Mark the model id.",
        "Given a 20-page PDF with 3 tables, sketch chunks.",
        "Estimate RAM for 1M chunks × 768-d float32.",
    ],
    interview_listen="chunking quality and same-model discipline, not vendor names",
    cheatsheet={
        "remember": "Same model. Structure-aware chunks. Metadata. Eval recall@k. Keyword still lives.",
        "bash": "uv pip install numpy sentence-transformers tiktoken",
        "python": "scores = (index / norms) @ (q / qn)",
        "decisions": "IDs → keyword. Paraphrase → dense. Both → hybrid (Phase 8).",
        "numbers": "Chunk 200–800 tokens. Overlap ~10–20%. 768-d * 4B * N RAM.",
        "do_not": "Mix models. Slice tables. Embed secrets. Skip eval.",
    },
    miniproject=mp(
        name="md-search",
        time="1 day",
        difficulty="Medium",
        why="You will reuse this indexer inside RAG.",
        story="I type a question about my notes and get paths + snippets.",
        must=["index folder", "persist", "query CLI", "metadata", "README with 5 queries"],
        should=["hash skip", "token chunker"],
        wont=["LLM answers yet"],
        architecture="```mermaid\nflowchart LR\nFolder --> Chunk --> Embed --> npz\nQuery --> Embed --> kNN\n```",
        layout="src/mdsearch/ index/ cli.py",
        rubric=["reproducible", "model name recorded", "no secrets"],
        stretch="Watchdog re-index on file change.",
    ),
    resources={
        "official": ["sentence-transformers", "OpenAI embeddings docs", "tiktoken"],
        "extra": ["MTEB leaderboard", "Unstructured.io docs"],
        "papers": ["DPR 2020", "Sentence-BERT 2019"],
    },
    faq=[
        {"q": "Chat model as embedder?", "a": "Some APIs offer it. Dedicated embedding models are cheaper and usually better for kNN. Don't roll your own by averaging chat hidden states unless you know why."},
        {"q": "GPU needed?", "a": "No for small corpora. CPU sentence-transformers is fine for this phase."},
        {"q": "PDF libraries?", "a": "pypdf for simple; pymupdf / unstructured / vendor OCR for real documents."},
    ],
    debugging=[
        {
            "title": "Random results",
            "symptom": "Top hit is unrelated.",
            "wrong": "Different models; not normalizing; embedding the filename not the body.",
            "see": "Print model id on ingest and query. Print the chunk text not just ids.",
            "fix": "Align models. Look at actual text.",
            "prevent": "Store model id. Retrieval eval.",
        },
        {
            "title": "Everything scores 0.99",
            "symptom": "No discrimination.",
            "wrong": "You embedded empty strings or the same boilerplate header on every chunk.",
            "see": "Print chunk lengths and a pair of vectors.",
            "fix": "Strip boilerplate. Better splits.",
            "prevent": "Min chunk length. Dedupe.",
        },
    ],
    mistakes=[
        {"title": "Character windows on code and tables", "body": "Broken rows, broken functions.", "instead": "Language-aware or header-aware splits."},
        {"title": "One chunk = one PDF", "body": "Lost in the middle later; retrieval too coarse.", "instead": "Smaller chunks, maybe parent-child in Phase 8."},
        {"title": "No gold queries", "body": "You tune prompts forever.", "instead": "25 labeled questions first."},
    ],
    prod_tips={
        "cost": "Embedding is cheap vs chat. Still cache and skip unchanged hashes. Don't re-embed the world every deploy.",
        "latency": "Brute force to ~100k is often <50ms. Then ANN. Batch queries.",
        "reliability": "Idempotent indexer. Checksums. Model id in the index header.",
        "observability": "Log query, top-k ids, scores. Later: retrieval traces.",
        "scaling": "Phase 7. Don't build a distributed ANN on day one.",
        "checklist": ["same model", "metadata", "eval@k", "hashes", "no secrets embedded"],
    },
    challenge={
        "title": "Multilingual",
        "body": "Index English + another language. Query in both. Use a multilingual embedder. Report recall.",
        "constraints": ["Same pipeline", "Document failures (names, code ids)"],
        "success": "A table, not a vibe.",
    },
    solutions=[
        {"id": "M2 eval", "hint": "Freeze 12 queries in a JSONL before changing chunk size.", "approach": "recall@k = hits / N. Don't leak test queries into prompt tuning later."},
        {"id": "H1 hybrid", "hint": "Min-max normalize scores then 0.5*bm25 + 0.5*cos or RRF.", "approach": "RRF is often more stable than weighted sums."},
    ],
    code_files={
        "cosine_search.py": '''"""Brute-force cosine search — the whole idea of a vector DB."""
from __future__ import annotations

import numpy as np


def normalize(x: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(x, axis=1, keepdims=True) + 1e-12
    return x / n


def search(index: np.ndarray, query: np.ndarray, k: int = 3) -> tuple[np.ndarray, np.ndarray]:
    idx_n = normalize(index)
    q_n = query / (np.linalg.norm(query) + 1e-12)
    scores = idx_n @ q_n
    k = min(k, scores.shape[0])
    top = np.argpartition(-scores, kth=k - 1)[:k]
    order = top[np.argsort(-scores[top])]
    return order, scores[order]


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    index = rng.normal(size=(100, 8))
    query = index[42] + 0.01 * rng.normal(size=(8,))
    ids, sc = search(index, query, k=3)
    print(list(ids), sc.round(3))
''',
        "chunk_md.py": '''"""Heading-aware Markdown chunker."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Chunk:
    heading: str
    text: str


def chunk_markdown(md: str, max_chars: int = 800) -> list[Chunk]:
    chunks: list[Chunk] = []
    heading = "root"
    buf: list[str] = []

    def flush() -> None:
        text = "\\n".join(buf).strip()
        if text:
            chunks.append(Chunk(heading=heading, text=text))
        buf.clear()

    for line in md.splitlines():
        if line.startswith("#"):
            flush()
            heading = line.lstrip("#").strip() or heading
            continue
        buf.append(line)
        if sum(len(x) for x in buf) >= max_chars:
            flush()
    flush()
    return chunks
''',
    },
)
