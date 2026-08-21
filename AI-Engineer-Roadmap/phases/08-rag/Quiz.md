# Quiz — Phase 8: Retrieval-Augmented Generation (RAG)

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. RAG's first step is
    A) Fine-tune
    B) Retrieve relevant context
    C) Train a transformer from scratch
    D) Increase temperature
2. If sources lack the answer, the model should
    A) Invent
    B) Say it doesn't know
    C) Use Reddit
    D) Fine-tune live
3. RRF is
    A) A GPU
    B) A way to fuse ranked lists
    C) A tokenizer
    D) A JWT
4. A reranker typically
    A) Reads query and document together
    B) Replaces embeddings
    C) Trains GPT
    D) Is Docker
5. Faithfulness measures
    A) Speed
    B) Whether the answer is supported by context
    C) Font size
    D) Uptime
6. GraphRAG is usually
    A) The default for FAQs
    B) Heavy; for global/corpus-level questions
    C) A Redis command
    D) Free of cost
7. Hallucination with RAG often means
    A) The GPU is old
    B) Retrieval missed or chunks are bad
    C) Python 3.11
    D) CORS
8. Parent retrieval
    A) Retrieves small, generates with larger parent
    B) Deletes parents
    C) Is SQL CASCADE
    D) Is temperature
9. Eval set should be
    A) Improvised after each prompt change only
    B) Frozen first, then you may split train/holdout
    C) Secret from yourself
    D) The Wikipedia dump
10. k=50 chunks in the prompt
    A) Always better
    B) Can add noise, cost, lost-in-the-middle
    C) Is required for cosine
    D) Fixes injection

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — Retrieve.
2. **B** — Abstain.
3. **B** — Fusion.
4. **A** — Cross-encoder.
5. **B** — Support.
6. **B** — Overkill often.
7. **B** — Look at chunks.
8. **A** — Small-to-big.
9. **B** — Freeze.
10. **B** — More ≠ better.

</details>
