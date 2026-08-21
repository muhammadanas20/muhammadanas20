# Debugging — Phase 8: Retrieval-Augmented Generation (RAG)

Debugging is the job. These are bugs we see every week.

## Bug 1. Fluent wrong answer with a citation

**Symptom**

Looks professional.

**Broken mental model**

The citation was not in the retrieved set, or the chunk does not say that.

**How to see it**

Log prompt. Assert citation ⊆ retrieved ids. Diff answer vs chunk.

**Fix**

Stricter prompt, citation check post-process, better chunks.

**Prevention**

Unit test: citation subset. Faithfulness metric.
## Bug 2. Good chunks, bad answer

**Symptom**

You would have answered correctly from those chunks.

**Broken mental model**

Prompt too loose, too much extra context, temperature high, lost in the middle.

**How to see it**

Ablate to 2 gold chunks.

**Fix**

Tighten prompt, lower k, put gold chunks at edges, temp 0.

**Prevention**

Prompt versions + eval.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
