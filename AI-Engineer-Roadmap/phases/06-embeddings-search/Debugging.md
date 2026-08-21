# Debugging — Phase 6: Embeddings and search

Debugging is the job. These are bugs we see every week.

## Bug 1. Random results

**Symptom**

Top hit is unrelated.

**Broken mental model**

Different models; not normalizing; embedding the filename not the body.

**How to see it**

Print model id on ingest and query. Print the chunk text not just ids.

**Fix**

Align models. Look at actual text.

**Prevention**

Store model id. Retrieval eval.
## Bug 2. Everything scores 0.99

**Symptom**

No discrimination.

**Broken mental model**

You embedded empty strings or the same boilerplate header on every chunk.

**How to see it**

Print chunk lengths and a pair of vectors.

**Fix**

Strip boilerplate. Better splits.

**Prevention**

Min chunk length. Dedupe.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
