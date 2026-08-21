# Quiz — Phase 2: SQL, Postgres, and Redis

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. Redis is primarily:
    A) A relational DB
    B) An in-memory store
    C) A GPU driver
    D) An LLM
2. Chat history should live in:
    A) Only Redis
    B) Postgres (durable)
    C) Client localStorage only
    D) The model weights
3. An index typically:
    A) Slows reads, speeds writes
    B) Speeds some reads, slightly slows writes
    C) Compresses disks
    D) Trains embeddings
4. Parameterized queries prevent:
    A) GPU OOM
    B) SQL injection
    C) Hallucinations
    D) Slow disks
5. INCR in Redis is:
    A) Not atomic
    B) Atomic
    C) Transactional across keys always
    D) Slow
6. JSONB is good for:
    A) Replacing all tables
    B) Variable metadata
    C) Storing PDFs
    D) Primary keys
7. N+1 means:
    A) One plus one indexes
    B) A query per child row after a parent query
    C) Sharding
    D) Two Redis nodes
8. TTL on Redis keys:
    A) Is optional decoration
    B) Prevents unbounded memory
    C) Is illegal
    D) Replaces Postgres backups
9. A migration is:
    A) A backup
    B) Versioned schema change
    C) A Docker image
    D) An embedding
10. PDFs belong in:
    A) bytea always
    B) Object storage + URL in SQL
    C) Redis lists
    D) Git

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — RAM first.
2. **B** — Durable source of truth.
3. **B** — Tradeoff.
4. **B** — Never f-string user SQL.
5. **B** — Single-key atomic.
6. **B** — Metadata.
7. **B** — Classic ORM bug.
8. **B** — Always set for ephemeral keys.
9. **B** — Alembic etc.
10. **B** — Blob stores.

</details>
