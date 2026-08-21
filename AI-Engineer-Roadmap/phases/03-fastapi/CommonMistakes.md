# Common mistakes — Phase 3: FastAPI

### 1. Business logic in the route

Cannot test without TestClient. Cannot reuse from a worker.

**Do this instead:** Service functions. Routes are glue.

### 2. Global mutable dict as DB

Fails with multiple workers.

**Do this instead:** Postgres. Even SQLite is better for a while.

### 3. Catch-all except and return 200

Clients think success.

**Do this instead:** HTTPException with the right code.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
