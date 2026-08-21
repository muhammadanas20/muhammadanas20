# Flashcards — Phase 6: Embeddings and search

Say the answer. Then open. Do the deck two days later. That is the whole spaced-repetition system.

**Q1.** Same model at ingest and query?

<details><summary>Answer</summary>

Yes. Always.

</details>

**Q2.** Typical chunk size?

<details><summary>Answer</summary>

Hundreds of tokens, structure first.

</details>

**Q3.** Cosine vs L2?

<details><summary>Answer</summary>

Cosine = angle; L2 = distance; normalize and they relate.

</details>

**Q4.** What is recall@k?

<details><summary>Answer</summary>

Fraction of queries where a relevant chunk appears in top k.

</details>

**Q5.** Why metadata?

<details><summary>Answer</summary>

Filter (tenant, date) and cite (path, heading).

</details>

**Q6.** ANN?

<details><summary>Answer</summary>

Approximate nearest neighbor — faster, slightly less exact.

</details>

**Q7.** When keyword wins?

<details><summary>Answer</summary>

IDs, codes, names, exact phrases.

</details>

**Q8.** What is a loader?

<details><summary>Answer</summary>

File → text + metadata.

</details>

**Q9.** Matryoshka?

<details><summary>Answer</summary>

Embeddings you can truncate.

</details>

**Q10.** Hash chunks?

<details><summary>Answer</summary>

Skip re-embedding unchanged text.

</details>
