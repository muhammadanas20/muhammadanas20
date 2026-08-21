# Solutions — Phase 6: Embeddings and search

Spoilers. Try for 25 minutes first.

We give **hints and approaches**, not copy-paste repos. If you paste a full solution into your portfolio without understanding it, the interview will hurt.

### M2 eval

Freeze 12 queries in a JSONL before changing chunk size.

<details><summary>Approach (still not full code)</summary>

recall@k = hits / N. Don't leak test queries into prompt tuning later.

</details>

### H1 hybrid

Min-max normalize scores then 0.5*bm25 + 0.5*cos or RRF.

<details><summary>Approach (still not full code)</summary>

RRF is often more stable than weighted sums.

</details>

Full working patterns related to this phase also live in [`code/`](./code/) and [EXAMPLES](../../EXAMPLES/).
