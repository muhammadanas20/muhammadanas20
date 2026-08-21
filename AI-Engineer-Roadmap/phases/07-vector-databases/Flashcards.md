# Flashcards — Phase 7: Vector databases

Say the answer. Then open. Do the deck two days later. That is the whole spaced-repetition system.

**Q1.** What does a vector DB add over numpy?

<details><summary>Answer</summary>

Persistence, filters, concurrency, ANN, ops.

</details>

**Q2.** HNSW?

<details><summary>Answer</summary>

Hierarchical navigable small world — ANN graph.

</details>

**Q3.** pgvector operator <=> ?

<details><summary>Answer</summary>

Distance (cosine distance if vector_cosine_ops).

</details>

**Q4.** Collection dimension?

<details><summary>Answer</summary>

Must equal embedding size.

</details>

**Q5.** Qdrant strength?

<details><summary>Answer</summary>

Filters, OSS, production features.

</details>

**Q6.** When Pinecone?

<details><summary>Answer</summary>

Want managed, ok with cost/lock-in.

</details>

**Q7.** Payload?

<details><summary>Answer</summary>

Stored text + metadata beside the vector.

</details>

**Q8.** Why chunk hash ids?

<details><summary>Answer</summary>

Stable upserts when re-ingesting.

</details>

**Q9.** Quantization?

<details><summary>Answer</summary>

Compress vectors, trade recall for RAM.

</details>

**Q10.** Expose Qdrant to internet?

<details><summary>Answer</summary>

No.

</details>
