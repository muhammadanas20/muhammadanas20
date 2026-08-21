# Debugging — Phase 7: Vector databases

Debugging is the job. These are bugs we see every week.

## Bug 1. Wrong dimension

**Symptom**

API 400 / SQL error on insert.

**Broken mental model**

Collection created for another model.

**How to see it**

Get collection info. Print embedding.shape.

**Fix**

New collection + re-embed, or match the model.

**Prevention**

Model id in collection name: `notes_bge_small_v1`.
## Bug 2. Filter returns nothing

**Symptom**

Unfiltered works.

**Broken mental model**

where={'tenant': 1} vs '1' string.

**How to see it**

Print stored payload types.

**Fix**

Consistent types. Schema.

**Prevention**

Pydantic on metadata.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
