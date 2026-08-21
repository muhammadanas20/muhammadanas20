# Common mistakes — Phase 2: SQL, Postgres, and Redis

### 1. Building SQL with f-strings

SQL injection. Game over.

**Do this instead:** Bound parameters.

### 2. No index on conversation_id

List-messages becomes a seq scan.

**Do this instead:** Composite index matching the query.

### 3. Cache without version

Users see yesterday's policy after a doc update.

**Do this instead:** Key includes doc hash or version.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
