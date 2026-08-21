# Common mistakes — Phase 12: Production AI / LLMOps

### 1. Dashboard theater

20 graphs, no action.

**Do this instead:** 3 SLOs with alerts.

### 2. Semantic cache on policy docs without version

Yesterday's policy.

**Do this instead:** doc_version in key or skip cache.

### 3. Retrying 400s

Paying for a bad prompt forever.

**Do this instead:** Retry 429/5xx only.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
