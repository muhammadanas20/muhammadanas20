# Interview — Phase 2: SQL, Postgres, and Redis

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. Why not store chat history in Redis?

**Expected answer (junior)**

Redis is ephemeral (unless you treat it as a primary, which is a different design). Restarts, eviction, and no rich queries. Postgres is durable and queryable.

**Common mistakes**

Redis persistence exists so it is 'the same' as Postgres.

**Senior-level discussion**

Redis as cache of recent messages is fine. Dual-write, TTL, and the cost of large values in RAM. AOF/RDB are not a substitute for a relational audit log.
### Q2. How do you rate-limit LLM calls?

**Expected answer (junior)**

Redis INCR per user per window. Reject over limit. Mention tokens as a better unit than requests.

**Common mistakes**

In-memory dict on one server. Limit only in the client.

**Senior-level discussion**

Token buckets, per-tenant budgets, distributed counters, sliding windows, coupling to billing, 429 + Retry-After.
### Q3. How does an index help and hurt?

**Expected answer (junior)**

Faster lookups, extra storage, slower writes.

**Common mistakes**

Index every column.

**Senior-level discussion**

Selectivity, covering indexes, write amplification, bloat, VACUUM, partial indexes.
### Q4. Design storage for a RAG app.

**Expected answer (junior)**

PG for metadata and chats, object storage for files, vector store for embeddings, Redis for limits.

**Common mistakes**

One Mongo collection named 'data'.

**Senior-level discussion**

Versioned documents, rebuildable indexes, tenant isolation, backup/restore story including vectors.
### Q5. What is a transaction isolation anomaly you actually hit?

**Expected answer (junior)**

Two requests both think they can insert a unique email.

**Common mistakes**

Pretending they never happen.

**Senior-level discussion**

Unique constraints, upsert, serializable vs app-level locks, Redis for hot counters.


---

## Whiteboard prompts

- ER diagram for a multi-tenant RAG app.
- Rate limiter: fixed vs sliding vs token bucket.
- Zero-downtime add-column migration.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for whether you separate durable truth from ephemeral counters.
