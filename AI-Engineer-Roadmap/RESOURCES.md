# Resources

Canonical sources first. Blog posts second. Twitter threads never as a source of truth.

This page is meant to stay current. When a link dies, fix it in a PR.

---

## How to read this list

You do **not** need to read everything.

For each phase, do:

1. The phase `Theory.md`
2. The official docs linked in that phase's `Resources.md`
3. At most one paper or deep blog

If you are still confused, do the exercises. More tabs will not help.

---

## Official documentation (bookmark)

| Topic | Start here |
| --- | --- |
| Python typing | [typing docs](https://docs.python.org/3/library/typing.html) |
| Pydantic | [docs.pydantic.dev](https://docs.pydantic.dev/) |
| FastAPI | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) |
| SQLAlchemy | [docs.sqlalchemy.org](https://docs.sqlalchemy.org/) |
| Postgres | [postgresql.org/docs](https://www.postgresql.org/docs/) |
| Redis | [redis.io/docs](https://redis.io/docs/) |
| Docker | [docs.docker.com](https://docs.docker.com/) |
| OpenAI API | [platform.openai.com/docs](https://platform.openai.com/docs) |
| Anthropic | [docs.anthropic.com](https://docs.anthropic.com/) |
| Ollama | [docs.ollama.com](https://docs.ollama.com/) |
| Hugging Face | [huggingface.co/docs](https://huggingface.co/docs) |
| Chroma | [docs.trychroma.com](https://docs.trychroma.com/) |
| Qdrant | [qdrant.tech/documentation](https://qdrant.tech/documentation/) |
| pgvector | [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector) |
| LangGraph | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/) |
| MCP | [modelcontextprotocol.io](https://modelcontextprotocol.io/) |
| OpenTelemetry | [opentelemetry.io/docs](https://opentelemetry.io/docs/) |
| Langfuse | [langfuse.com/docs](https://langfuse.com/docs) |
| Ragas | [docs.ragas.io](https://docs.ragas.io/) |
| DeepEval | [docs.confident-ai.com](https://www.deepeval.com/docs) |

---

## Foundational papers (read the abstract, then the figures)

You do not need to reproduce the math. You need the idea and the limitation.

| Paper | Why we care |
| --- | --- |
| Attention Is All You Need (Vaswani et al., 2017) | Transformers |
| BERT (Devlin et al., 2018) | Bidirectional encoders, still shapes embedding models |
| Retrieval-Augmented Generation (Lewis et al., 2020) | The original RAG |
| Dense Passage Retrieval (Karpukhin et al., 2020) | Dual encoders for retrieval |
| Lost in the Middle (Liu et al., 2023) | Why dumping a whole PDF into context fails |
| Self-RAG (Asai et al., 2023) | When to retrieve, when to critique |
| Corrective RAG (Yan et al., 2024) | Retrieve → grade → correct |
| Toolformer (Schick et al., 2023) | Models that call tools |
| ReAct (Yao et al., 2022) | Reason + act loops |
| Generative Agents (Park et al., 2023) | Memory streams (ideas, not a production blueprint) |

Links change. Search the title + PDF. Prefer arXiv.

---

## High-signal engineering blogs

- OpenAI, Anthropic, Google DeepMind engineering / cookbook posts
- Pinecone and Qdrant learning centers (vendor, but diagrams are good — keep your skepticism)
- Anthropic: *Building effective agents*
- OpenAI: *A practical guide to building agents*
- Microsoft: ION / Azure architecture center — RAG on Azure is a useful *pattern* even if you do not use Azure
- Simon Willison's weblog — excellent on evals, local models, and MCP
- Eugene Yan, Chip Huyen (especially *Designing Machine Learning Systems* as a book), Hamel Husain on evals

---

## Free curricula that complement this one

This course is **AI engineering**. These fill adjacent gaps.

| Resource | Use for |
| --- | --- |
| [microsoft/ML-For-Beginners](https://github.com/microsoft/ML-For-Beginners) | Classic ML (scikit-learn) if your stats are rusty |
| [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | Neural nets, CV, NLP internals |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | Language and CS books |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | Extra build ideas |
| [DARKANGEL689/100-Days-Of-Docker](https://github.com/DARKANGEL689/100-Days-Of-Docker) | Extra Docker drills if Phase 4 felt thin |
| Hugging Face NLP / agents courses | Extra practice, different voice |

We teach production LLM systems. We do not replace a linear algebra course or a distributed systems course. Steal from those when you need them.

---

## Models to practice with (as of 2026)

Names will rot. The *roles* will not.

| Role | Local (Ollama / similar) | Hosted |
| --- | --- | --- |
| Cheap chat | llama3.x, qwen2.5, phi | GPT-4.1-mini, Claude haiku-class, Groq-hosted OSS |
| Strong chat | qwen2.5-32b if you have RAM | GPT-4.1 / o-series, Claude sonnet/opus-class |
| Embeddings | nomic-embed-text, bge-m3 | text-embedding-3-large, voyage, cohere |
| Rerank | bge-reranker | cohere rerank |
| Code | qwen2.5-coder | Claude / GPT class |

Always record **model + date + eval score**. "We used GPT" is not an experiment.

---

## Datasets for evals

- Your own documents + 25 handwritten questions (best)
- HotpotQA, Natural Questions (research comparisons)
- FinanceBench, LegalBench (if you work in that domain)
- A private holdout you never prompt-engineer against

---

## Books worth buying or borrowing

- *Designing Machine Learning Systems* — Chip Huyen
- *Building LLMs for Production* / similar applied LLM ops books (skim, they date fast)
- *Designing Data-Intensive Applications* — Kleppmann (the data systems spine)
- *Python 3.11+* reference you already like

---

## YouTube (optional)

Prefer talks from conferences (PyCon, QCon, AI Engineer World's Fair) over 4-hour "complete bootcamp" videos. Use video when a diagram is not enough. Come back and write code.

---

## Staying current without drowning

Once a week, 30 minutes:

1. Changelog of one tool you actually use
2. One eval or security write-up
3. Ignore the rest

If you change frameworks every Friday you will never ship the capstone.
