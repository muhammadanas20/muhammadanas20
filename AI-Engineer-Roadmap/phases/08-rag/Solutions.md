# Solutions — Phase 8: Retrieval-Augmented Generation (RAG)

Spoilers. Try for 25 minutes first.

We give **hints and approaches**, not copy-paste repos. If you paste a full solution into your portfolio without understanding it, the interview will hurt.

### M1 hybrid

rank_bm25 + rank_dense → rrf.

<details><summary>Approach (still not full code)</summary>

Equalize k=20 each. Measure recall@5.

</details>

### H2 CRAG

A cheap model returns {relevant: bool}. If false, rewrite once. max_retries=1.

<details><summary>Approach (still not full code)</summary>

Log extra calls. Cap cost.

</details>

Full working patterns related to this phase also live in [`code/`](./code/) and [EXAMPLES](../../EXAMPLES/).
