# Common mistakes — Phase 7: Vector databases

### 1. New collection every process start

You re-embed the world on each deploy.

**Do this instead:** Named persistent collection + idempotent upsert.

### 2. Trusting dashboard counts

Off-by-one after failed batch.

**Do this instead:** Application-level checksums vs document store.

### 3. L2 index with cosine embeddings

Ranking looks 'almost ok' and you waste a week.

**Do this instead:** Read the vendor metric docs. Match.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
