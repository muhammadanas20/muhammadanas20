from make_phase import C, E, EX, I, Q, asg, drill, mp, phase, th

PHASE = phase(
    num="8",
    title="Retrieval-Augmented Generation (RAG)",
    tagline="Ground the model in your data. Then measure whether you actually did.",
    hours="14-21 days",
    difficulty="Hard",
    exit_ticket="A RAG service with a frozen eval set and scores, not vibes.",
    objectives=[
        "Implement naive RAG end to end.",
        "Add hybrid search and a reranker.",
        "Use parent-document / small-to-big retrieval.",
        "Explain agentic RAG, GraphRAG, Self-RAG, Corrective RAG — and when they are overkill.",
        "Evaluate with faithfulness, relevancy, and recall.",
    ],
    prerequisites=["Phases 5–7. FastAPI optional but recommended."],
    topics=[
        "Naive RAG",
        "Hybrid search",
        "Reranking",
        "Parent retrieval",
        "Agentic RAG",
        "GraphRAG",
        "Self-RAG",
        "Corrective RAG",
        "Evaluation",
    ],
    nav="[Home](../../README.md) · Prev: [Phase 7](../07-vector-databases/) · Next: [Phase 9 · Agents](../09-agents/)",
    theory=th(
        intro="""**Retrieval-Augmented Generation** means:

1. Find relevant pieces of *your* data
2. Put them in the prompt
3. Ask the model to answer **using those pieces**
4. Prefer answers that can be cited
5. **Measure** whether the answer is supported

Without step 5 you have a demo.

RAG is the default architecture for 'chat with our docs' because facts change and do not belong in weights.""",
        one_liner="Retrieve first, generate second, evaluate always.",
        why="""Fine-tuning cannot keep up with a wiki that changes daily.

A 200k context window is not a retrieval strategy (cost, latency, lost-in-the-middle, security).

Companies hire people who can make RAG **less wrong**, not people who can import LangChain.""",
        if_missing="you would ship a chatbot that invents refund policies with a smile.",
        analogy="""Open-book exam.

- **Naive RAG** = grab 5 nearest pages, write the essay.
- **Hybrid** = also use the index at the back of the book (keywords).
- **Rerank** = a TA skims 50 pages and keeps the best 5.
- **Parent retrieval** = find a paragraph, hand the student the whole section.
- **Agentic RAG** = the student may search twice if the first pages were weak.
- **GraphRAG** = a mind map of who relates to whom, not just pages.
- **Self-RAG** = the student asks 'do I even need the book?' and 'did I cite it honestly?'
- **Corrective RAG** = a grader says 'these pages are off, search again.'
- **Evaluation** = a marking rubric, not 'looks good to me.'""",
        visual="""```mermaid
flowchart LR
  U[Question] --> RW[Optional rewrite]
  RW --> H[Hybrid retrieve]
  H --> RR[Rerank]
  RR --> P[Build prompt + citations]
  P --> LLM
  LLM --> A[Answer + sources]
  A --> EV[Eval: faithful? relevant?]
```""",
        architecture="""```mermaid
flowchart TB
  subgraph ingest
    Docs --> Chunk --> Embed --> VDB[(Vector DB)]
    Chunk --> BM[BM25 index]
  end
  subgraph serve
    Q[Query] --> Retriever
    VDB --> Retriever
    BM --> Retriever
    Retriever --> Rerank --> Prompt --> LLM --> Out
  end
  Out --> Traces
  Out --> Evals
```""",
        beginner="""**Naive RAG:** embed query → top-k chunks → stuff into prompt → generate.

**Prompt pattern:**

```
You are a helpful assistant.
Use ONLY the sources.
If the sources do not contain the answer, say you don't know.
Cite source ids.

Sources:
[1] ...
[2] ...

Question: ...
```

**Citation:** return chunk ids / URLs. The UI shows them. Hallucinated citations are a bug.

**k:** 3–10 starting point. Too small = miss. Too large = noise + cost.

**This already beats dumping PDFs** for most wikis.""",
        intermediate="""**Hybrid search:** BM25 (keyword) + dense. Fuse with **RRF** (reciprocal rank fusion) which is simple and strong.

**Reranker:** a cross-encoder that reads (query, chunk) together and scores relevance. Slow per pair, great on 20–50 candidates.

**Query rewrite:** the raw user message may be 'that too' — rewrite using chat history into a standalone search query.

**Parent / small-to-big:** retrieve small chunks (precise), expand to parent section (context for the LLM).

**Metadata filters:** tenant, language, product version — applied *before* the model sees data.

**Faithfulness:** is the answer supported by retrieved text?
**Answer relevancy:** does it address the question?
**Context precision/recall:** did we retrieve the right stuff?

Tools: Ragas, DeepEval, a spreadsheet of 40 questions.""",
        advanced="""**Agentic RAG:** the model may call `search` multiple times, or `read_parent`. It is an agent with a retrieve tool. Higher latency and cost. Useful when one hop fails.

**GraphRAG:** extract entities/relations, retrieve a subgraph. Helps 'themes across a corpus' and global questions. Heavy pipelines. Overkill for FAQs.

**Self-RAG:** special tokens / a policy for retrieve-on-demand and critique. Paper: Asai et al. 2023. You can approximate with a cheap classifier: 'needs retrieval?'

**Corrective RAG (CRAG):** grade retrieved docs; if poor, web search or retry. Yan et al. 2024.

**HyDE:** generate a hypothetical answer, embed that, search. Helps some corpora, hurts others. Measure.

**Routing:** classify query to a collection (policies vs engineering vs HR).""",
        production="""Ship naive + hybrid + rerank + evals first. Do not start with GraphRAG.

Production RAG is:

- Versioned ingest
- Frozen eval set (never prompt-engineered against until after freeze)
- Online eval / user thumbs
- Tracing of retrieved ids
- Cost per question
- Fallback: 'I don't know' is a feature
- Freshness: re-index on doc change
- Security: injection in documents (Phase 13)

A staff engineer asks: *what is faithfulness on the holdout set?* If you cannot answer, you are not in production.""",
        when="Private or changing knowledge. Citations required. Corpus bigger than a prompt.",
        when_not="Three static paragraphs (just prompt). Tasks with no corpus (pure generation). When a SQL query is the actual answer (maybe an agent, Phase 9). Real-time unknown web facts without a search tool.",
        code_preview='''def answer(q: str) -> str:
    hits = retrieve(q, k=20)
    top = rerank(q, hits)[:5]
    return generate(q, top)
''',
        code_notes="Three functions. You should be able to unit-test retrieve without generate.",
        ex_b="Naive RAG over this course's Markdown. 10 questions.",
        ex_m="Hybrid + rerank. Compare faithfulness vs naive.",
        ex_h="Implement CRAG-style grading with a small model. Show a case it saves and a case it wastes money.",
        project="PDF Chat — PROJECTS/01-pdf-chat and MiniProject.md.",
        interview_preview="Draw naive RAG. Why hybrid? How to eval? When GraphRAG? Hallucination despite RAG?",
        flash_sample="**Q:** RAG still hallucinated. First suspect?\n**A:** Retrieval miss or bad chunk, not 'the temperature of the soul'.",
        mistakes_preview="No eval. k=50 into the prompt. No 'I don't know'. Citing documents not actually retrieved. GraphRAG on day one.",
        debug_preview="Answer sounds right, citation is wrong. Query rewrite destroyed meaning. Reranker scored boilerplate headers high.",
        best="Hybrid + rerank + parent expansion + eval harness + I don't know. Simple graph.",
        industry="Every serious team has a gold set. Many use Ragas/DeepEval/Promptfoo. LangSmith/Langfuse for traces.",
        perf="Cache embeddings and frequent queries (careful with freshness). Stream the answer. Retrieve in parallel (BM25 + dense).",
        security="Treat retrieved text as untrusted. Prompt injection via wiki pages. Tenant filters. Redact PII in traces.",
        refs="- Lewis et al. 2020 RAG\n- Self-RAG 2023\n- CRAG 2024\n- Ragas docs\n- Anthropic / OpenAI RAG cookbooks",
        further="Microsoft GraphRAG blog (know the cost). HyDE paper. 'Building RAG with evaluation first' posts by Hamel / Eugene Yan.",
    ),
    examples=[
        EX(
            title="Naive RAG in one file (fake retrieve + generate)",
            why="See the data flow without 12 libraries.",
            code='''"""code/naive_rag.py"""
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Hit:
    id: str
    text: str
    score: float

CORPUS = [
    Hit("h1", "A token is a piece of text the model bills and counts.", 0),
    Hit("h2", "Docker images are immutable snapshots.", 0),
    Hit("h3", "Redis is great for rate limits, not chat history.", 0),
]

def retrieve(q: str, k: int = 2) -> list[Hit]:
    ql = q.lower().split()
    scored: list[Hit] = []
    for h in CORPUS:
        score = sum(w in h.text.lower() for w in ql)
        scored.append(Hit(h.id, h.text, float(score)))
    scored.sort(key=lambda x: -x.score)
    return scored[:k]

def prompt(q: str, hits: list[Hit]) -> str:
    src = "\\n".join(f"[{h.id}] {h.text}" for h in hits)
    return (
        "Use ONLY the sources. If missing, say you don't know.\\n"
        f"Sources:\\n{src}\\n\\nQuestion: {q}\\nAnswer:"
    )

def generate_fake(p: str) -> str:
    if "h1" in p and "token" in p.lower():
        return "A token is a billed text piece [h1]."
    return "I don't know."

if __name__ == "__main__":
    q = "What is a token?"
    hits = retrieve(q)
    print(generate_fake(prompt(q, hits)))
''',
            line_by_line="retrieve is testable. prompt is a pure function. generate is replaceable with a real model. Fake keyword retrieve stands in for vectors.",
            output="A token is a billed text piece [h1].",
            dry_run="Query → score corpus by word overlap → top 2 → prompt → fake generate sees h1.",
            memory="O(corpus)",
            time="O(|corpus| * |query|)",
            space="O(k)",
            alternatives="Replace retrieve with cosine / hybrid.",
            optimization="This is the skeleton. Don't add GraphRAG here.",
        ),
        EX(
            title="RRF fusion of two ranked lists",
            why="Hybrid search without learned weights.",
            code='''"""code/rrf.py"""
from __future__ import annotations

from collections import defaultdict

def rrf(*ranked_id_lists: list[str], k: int = 60) -> list[str]:
    """Reciprocal Rank Fusion. k=60 is the common constant, not top-k."""
    scores: dict[str, float] = defaultdict(float)
    for lst in ranked_id_lists:
        for rank, doc_id in enumerate(lst, start=1):
            scores[doc_id] += 1.0 / (k + rank)
    return [d for d, _ in sorted(scores.items(), key=lambda x: -x[1])]

if __name__ == "__main__":
    dense = ["a", "b", "c"]
    bm25 = ["c", "a", "z"]
    print(rrf(dense, bm25))
''',
            line_by_line="Each list contributes 1/(k+rank). Docs that rank well in both win. No score calibration needed.",
            output="['a', 'c', 'b', 'z'] or similar — a and c boosted.",
            dry_run="a: 1/61 + 1/62; c: 1/63 + 1/61 — compute and sort.",
            memory="O(n) unique ids",
            time="O(n log n) sort",
            space="O(n)",
            alternatives="Weighted sum of min-max normalized scores; learned fusion.",
            optimization="RRF is the default until eval says otherwise.",
        ),
    ],
    practice=[
        drill("Don't know", "Ask your naive RAG a question off-corpus. It must refuse.", "Refusal is tested."),
        drill("Citation integrity", "Force the model to cite. Check every citation exists in retrieved ids.", "A script, not your eyes only."),
        drill("Gold set", "Write 15 questions with expected chunk ids before you tune anything.", "File committed."),
    ],
    exercises={
        "beginner": [
            E("Naive over notes", "Index NOTES or this phase folder. 8 questions.", "Print retrieved chunks before the answer."),
            E("I don't know", "Add 4 adversarial questions. All must refuse.", "No extra facts from world knowledge."),
        ],
        "medium": [
            E("Hybrid + RRF", "BM25 + dense. Table vs dense-only recall@5.", "Same gold set."),
            E("Rerank", "Take k=20, rerank to 5 (cross-encoder or a cheap LLM score). Latency vs quality.", "Record p95."),
        ],
        "hard": [
            E("Parent retrieval", "Small child chunks for search, parent section for the prompt.", "Diagram + eval."),
            E("Mini CRAG", "Grade context; if bad, retry with rewrite. Cost multiplier reported.", "Must not infinite loop."),
        ],
    },
    assignments=[
        asg(
            "pdf-chat-v1",
            "1–2 weeks (this is the phase)",
            "See PROJECTS/01-pdf-chat. FastAPI, one vector store, hybrid or rerank, 25-question eval, Docker.",
            ["running app", "eval table", "README architecture"],
            ["faithfulness number", "I don't know works", "citations valid", "compose up"],
        )
    ],
    quiz=[
        Q("RAG's first step is", "Fine-tune", "Retrieve relevant context", "Train a transformer from scratch", "Increase temperature", "B", "Retrieve."),
        Q("If sources lack the answer, the model should", "Invent", "Say it doesn't know", "Use Reddit", "Fine-tune live", "B", "Abstain."),
        Q("RRF is", "A GPU", "A way to fuse ranked lists", "A tokenizer", "A JWT", "B", "Fusion."),
        Q("A reranker typically", "Reads query and document together", "Replaces embeddings", "Trains GPT", "Is Docker", "A", "Cross-encoder."),
        Q("Faithfulness measures", "Speed", "Whether the answer is supported by context", "Font size", "Uptime", "B", "Support."),
        Q("GraphRAG is usually", "The default for FAQs", "Heavy; for global/corpus-level questions", "A Redis command", "Free of cost", "B", "Overkill often."),
        Q("Hallucination with RAG often means", "The GPU is old", "Retrieval missed or chunks are bad", "Python 3.11", "CORS", "B", "Look at chunks."),
        Q("Parent retrieval", "Retrieves small, generates with larger parent", "Deletes parents", "Is SQL CASCADE", "Is temperature", "A", "Small-to-big."),
        Q("Eval set should be", "Improvised after each prompt change only", "Frozen first, then you may split train/holdout", "Secret from yourself", "The Wikipedia dump", "B", "Freeze."),
        Q("k=50 chunks in the prompt", "Always better", "Can add noise, cost, lost-in-the-middle", "Is required for cosine", "Fixes injection", "B", "More ≠ better."),
    ],
    flashcards=[
        C("Naive RAG?", "Retrieve top-k, stuff prompt, generate."),
        C("Hybrid?", "Keyword + dense, fused."),
        C("Rerank?", "Rescore candidates with a stronger model."),
        C("Faithfulness?", "Answer supported by retrieved text."),
        C("CRAG?", "Grade retrieval, correct if poor."),
        C("Self-RAG?", "Retrieve/critique on demand."),
        C("GraphRAG?", "Retrieve via a knowledge graph."),
        C("Why citations?", "User trust + you can debug."),
        C("Query rewrite?", "Standalone search query from chatty history."),
        C("When not RAG?", "No corpus, or three paragraphs, or SQL is the answer."),
    ],
    interview=[
        I("Draw RAG on the board.", "Ingest: load-chunk-embed-store. Query: rewrite-retrieve-filter-rerank-prompt-generate-cite. Eval loop.", "Starting with LangChain classes.", "Where you'd put cache, tenancy, tracing."),
        I("RAG still hallucinated. Debug.", "Print retrieved chunks. Check they actually support the answer. If yes, prompt/grounding issue. If no, retrieval/chunking. Check filters, query rewrite, k.", "Buy a bigger model immediately.", "Faithfulness metrics, injection, stale index."),
        I("Hybrid vs dense-only?", "Keywords catch ids/codes; dense catches paraphrases. Fuse with RRF. Measure.", "Hybrid is always better so skip eval.", "When BM25 dominates (legal clauses) vs semantic FAQs."),
        I("How do you evaluate RAG?", "Gold questions, retrieval recall@k, faithfulness, relevancy, human spot checks, later online thumbs. Freeze the set.", "We ask the LLM if it did a good job (only).", "LLM-as-judge bias, DeepEval/Ragas pitfalls, inter-annotator."),
        I("When is an agent better than RAG?", "When you need tools, multi-step, or multiple sources with decisions. Not for 'search these docs and answer'.", "Agents always; RAG is dead.", "Cost/latency, failure modes, mixing agentic RAG."),
    ],
    whiteboard=[
        "Full RAG architecture for a 10k-doc help center, 500 QPS peak, 2s p95.",
        "Compare naive vs hybrid+rerank vs GraphRAG for 'What is our refund policy?' vs 'Themes in 10k tickets'.",
        "Design an eval harness with CI gate.",
    ],
    interview_listen="whether you debug retrieval before blaming the LLM, and whether you have numbers",
    cheatsheet={
        "remember": "Retrieve → generate → eval. Hybrid+rerank before agents. I don't know is a feature. Citations must be real.",
        "bash": "pytest tests/eval_rag.py -q",
        "python": "hits = hybrid(q); top = rerank(q, hits)[:5]; answer = generate(q, top)",
        "decisions": "FAQ → naive/hybrid. Messy queries → rewrite. Global themes → maybe graph. Multi-hop tools → agentic.",
        "numbers": "k retrieve 20, rerank to 5. Gold set 25–100. Faithfulness: track it, set a bar (e.g. 0.8) that matches YOUR judge.",
        "do_not": "GraphRAG first. Tune on the only eval set without a holdout. Invent citations. 50 chunks in context by default.",
    },
    miniproject=mp(
        name="pdf-chat",
        time="3–7 days",
        difficulty="Hard",
        why="The portfolio default. Do it properly.",
        story="I upload a PDF, ask questions, see citations, and you can read my eval table.",
        must=["ingest PDF", "query API", "citations", "25-q eval", "Docker", "I don't know"],
        should=["hybrid or rerank", "FastAPI stream"],
        wont=["GraphRAG unless extra time"],
        architecture="```mermaid\nflowchart LR\nPDF --> Chunk --> VDB\nQ --> Retrieve --> LLM --> Cite\n```",
        layout="See ../../PROJECTS/01-pdf-chat/",
        rubric=["eval numbers", "compose up", "README diagram", "limitations section"],
        stretch="Parent retrieval + streaming + traces.",
    ),
    resources={
        "official": ["Ragas", "DeepEval", "Qdrant hybrid docs", "LlamaIndex / LangChain RAG tutorials — read, then simplify"],
        "extra": ["Hamel Husain on evals", "Anthropic contextual retrieval"],
        "papers": ["Lewis RAG 2020", "Self-RAG 2023", "CRAG 2024", "Lost in the Middle 2023"],
    },
    faq=[
        {"q": "LangChain or raw?", "a": "Raw first (this phase's code/). Then a framework if the graph grows. Interviews expect you to explain without the framework."},
        {"q": "How big a gold set?", "a": "25 is a start. 50–100 is better. Quality of labels > thousands of noisy ones."},
        {"q": "Can I use the LLM to generate eval questions?", "a": "As a draft. Humans must edit. Models reuse phrasing from the corpus and overfit retrieval."},
    ],
    debugging=[
        {
            "title": "Fluent wrong answer with a citation",
            "symptom": "Looks professional.",
            "wrong": "The citation was not in the retrieved set, or the chunk does not say that.",
            "see": "Log prompt. Assert citation ⊆ retrieved ids. Diff answer vs chunk.",
            "fix": "Stricter prompt, citation check post-process, better chunks.",
            "prevent": "Unit test: citation subset. Faithfulness metric.",
        },
        {
            "title": "Good chunks, bad answer",
            "symptom": "You would have answered correctly from those chunks.",
            "wrong": "Prompt too loose, too much extra context, temperature high, lost in the middle.",
            "see": "Ablate to 2 gold chunks.",
            "fix": "Tighten prompt, lower k, put gold chunks at edges, temp 0.",
            "prevent": "Prompt versions + eval.",
        },
    ],
    mistakes=[
        {"title": "Evaluating only by chatting with it", "body": "You remember the happy path.", "instead": "Frozen JSONL + scores in CI."},
        {"title": "Retrieving then ignoring 'I don't know'", "body": "The model fills gaps from pretraining.", "instead": "Explicit abstain; maybe a classifier."},
        {"title": "One pipeline for all query types", "body": "Navigational, factual, summary, chit-chat need different handling.", "instead": "Route. Chit-chat should not retrieve random docs."},
    ],
    prod_tips={
        "cost": "Rerankers and agentic loops multiply spend. Cache retrieval for identical questions. Smaller generate model if grounded.",
        "latency": "Parallel BM25+dense. Stream tokens. Don't GraphRAG on the hot path.",
        "reliability": "Index freshness. Rebuild. Version. Empty retrieval → abstain, not improv.",
        "observability": "Trace retrieved ids, scores, prompt version, faithfulness sample.",
        "scaling": "The retrieve path scales with the vector DB. The generate path scales with the provider. Separate SLOs.",
        "checklist": ["gold set", "abstain", "citations checked", "tenant filter", "hybrid or evidence it is unnecessary", "CI eval"],
    },
    challenge={
        "title": "Beat your naive baseline by 15% faithfulness without a bigger generator",
        "body": "Only retrieval/prompt/rerank changes. Report the ablation table.",
        "constraints": ["Same generate model", "Same gold set holdout"],
        "success": "A table people believe.",
    },
    solutions=[
        {"id": "M1 hybrid", "hint": "rank_bm25 + rank_dense → rrf.", "approach": "Equalize k=20 each. Measure recall@5."},
        {"id": "H2 CRAG", "hint": "A cheap model returns {relevant: bool}. If false, rewrite once. max_retries=1.", "approach": "Log extra calls. Cap cost."},
    ],
    code_files={
        "naive_rag.py": '''"""Naive RAG skeleton — retrieve, prompt, generate."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Hit:
    id: str
    text: str
    score: float


CORPUS = [
    Hit("h1", "A token is a piece of text the model bills and counts.", 0),
    Hit("h2", "Docker images are immutable snapshots.", 0),
    Hit("h3", "Redis is great for rate limits, not chat history.", 0),
]


def retrieve(q: str, k: int = 2) -> list[Hit]:
    words = q.lower().split()
    scored = [
        Hit(h.id, h.text, float(sum(w in h.text.lower() for w in words))) for h in CORPUS
    ]
    scored.sort(key=lambda x: -x.score)
    return scored[:k]


def prompt(q: str, hits: list[Hit]) -> str:
    src = "\\n".join(f"[{h.id}] {h.text}" for h in hits)
    return (
        "Use ONLY the sources. If missing, say you don't know.\\n"
        f"Sources:\\n{src}\\n\\nQuestion: {q}\\nAnswer:"
    )


def generate_fake(p: str) -> str:
    if "h1" in p and "token" in p.lower():
        return "A token is a billed text piece [h1]."
    return "I don't know."


if __name__ == "__main__":
    question = "What is a token?"
    hits = retrieve(question)
    print(generate_fake(prompt(question, hits)))
''',
        "rrf.py": '''"""Reciprocal Rank Fusion for hybrid search."""
from __future__ import annotations

from collections import defaultdict


def rrf(*ranked_id_lists: list[str], k: int = 60) -> list[str]:
    scores: dict[str, float] = defaultdict(float)
    for lst in ranked_id_lists:
        for rank, doc_id in enumerate(lst, start=1):
            scores[doc_id] += 1.0 / (k + rank)
    return [d for d, _ in sorted(scores.items(), key=lambda x: -x[1])]


if __name__ == "__main__":
    print(rrf(["a", "b", "c"], ["c", "a", "z"]))
''',
    },
)
