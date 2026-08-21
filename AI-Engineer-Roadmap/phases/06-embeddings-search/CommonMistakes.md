# Common mistakes — Phase 6: Embeddings and search

### 1. Character windows on code and tables

Broken rows, broken functions.

**Do this instead:** Language-aware or header-aware splits.

### 2. One chunk = one PDF

Lost in the middle later; retrieval too coarse.

**Do this instead:** Smaller chunks, maybe parent-child in Phase 8.

### 3. No gold queries

You tune prompts forever.

**Do this instead:** 25 labeled questions first.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
