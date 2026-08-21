# Quiz — Phase 7: Vector databases

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. A vector DB primarily answers
    A) SQL joins of money
    B) Nearest neighbors + filters
    C) Train GPTs
    D) Render HTML
2. HNSW is
    A) A prompt
    B) An ANN index graph
    C) A JWT alg
    D) A Docker base
3. pgvector lives in
    A) Redis
    B) Postgres
    C) The browser
    D) S3 only
4. Dimension mismatch
    A) Is silently ok
    B) Errors or corrupts search
    C) Improves recall
    D) Is cosine
5. Multi-tenant minimum
    A) Hope
    B) tenant_id filter (and tests)
    C) One shared vector for all
    D) Email the vendor
6. Chroma is great for
    A) Learning and small apps
    B) Global 10B vector search as a first choice
    C) Replacing Postgres chats
    D) OS kernels
7. Vectors without stored text
    A) Are enough to cite
    B) Cannot show the user the passage
    C) Train better
    D) Are smaller so always better
8. Pinecone is
    A) OSS you must host
    B) A managed vector service
    C) A tokenizer
    D) A FastAPI clone
9. Metric mismatch (cosine vs L2)
    A) Does not matter
    B) Can ruin ranking
    C) Only affects backups
    D) Fixes filters
10. Rebuildability
    A) Optional
    B) Required — documents are source of truth
    C) Illegal
    D) Only for Redis

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — kNN + ops.
2. **B** — Approximate NN.
3. **B** — Extension.
4. **B** — Must match.
5. **B** — Filter + tests.
6. **A** — Right-sized.
7. **B** — Keep payload.
8. **B** — Managed.
9. **B** — Match embedder.
10. **B** — Index can be rebuilt.

</details>
