PHASE = {
    "num": "2",
    "title": "SQL, Postgres, and Redis",
    "tagline": "Chat history, users, documents, and rate limits do not belong in a JSON file.",
    "hours": "7-10 days",
    "difficulty": "Medium",
    "exit_ticket": "Migrated Postgres schema for users/docs/chats plus a Redis rate limiter.",
    "objectives": [
        "Model users, documents, conversations, and messages in SQL.",
        "Use Postgres indexes, JSONB, and EXPLAIN without fear.",
        "Run schema migrations (Alembic or similar).",
        "Use Redis for cache, rate limits, and short-lived session data.",
        "Know when SQL vs a vector DB vs object storage is the right store.",
    ],
    "prerequisites": ["Phase 0–1. You can write Python and run Docker."],
    "topics": ["SQL", "Postgres", "indexes", "JSONB", "migrations", "Redis", "caching", "rate limits"],
    "nav": "[Home](../../README.md) · Prev: [Phase 1](../01-python-refresh/) · Next: [Phase 3 · FastAPI](../03-fastapi/)",
    "theory": {
        "intro": """An AI app that forgets chats on restart is a demo.

Production systems store:

- **Who** the user is (Postgres)
- **What** they uploaded (object storage + a row pointing at it)
- **Which chunks** we embedded (Postgres + vector column or a vector DB)
- **How often** they may call the model (Redis)
- **Traces** of what we sent the model (Postgres or a tracing backend)

This phase is the data spine. Skip it and Phase 8 will rot.""",
        "one_liner": "Postgres is the source of truth; Redis is the short-term memory and traffic cop.",
        "why": """LLMs are stateless. Your product is not.

If you store chats in a list in RAM:

- Restart wipes history
- Two servers cannot share state
- You cannot audit what was said
- You cannot bill or rate-limit fairly

SQL exists because relations (user has many chats has many messages) are real. Redis exists because some data is hot and disposable (a 60-second rate-limit counter).""",
        "if_missing": "you would ship a chatbot that cannot remember yesterday and cannot stop a runaway bill.",
        "analogy": """A library.

- **Postgres** = the catalog and the ledgers. Authoritative. Durable. Queryable.
- **Indexes** = the card catalog. Extra space, much faster lookup.
- **JSONB** = a notebook taped to a catalog card for messy extra fields.
- **Redis** = the whiteboard at the front desk: "this visitor has checked out 5 things today." Wiped at close. Fast. Not the catalog.
- **Migrations** = remodeling the library without losing books.""",
        "visual": """```mermaid
flowchart LR
  API --> PG[(Postgres: users, chats, docs)]
  API --> RD[(Redis: rate limit, cache)]
  API --> S3[Object storage: raw PDFs]
  PG --> Vec[pgvector or external vector DB]
```""",
        "architecture": """```mermaid
erDiagram
  USERS ||--o{ CONVERSATIONS : owns
  CONVERSATIONS ||--o{ MESSAGES : contains
  USERS ||--o{ DOCUMENTS : uploads
  DOCUMENTS ||--o{ CHUNKS : splits
  MESSAGES {
    uuid id
    text content
    text role
    jsonb meta
  }
```""",
        "beginner": """**Table** = spreadsheet with a schema. **Row** = one record. **Primary key** = unique id, often UUID.

**Foreign key** = a pointer to another table that the database enforces.

**SQL** = the language: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`.

**Index** = extra data structure (often B-tree) that makes lookups fast and writes a bit slower.

**Postgres** = a powerful open-source relational database. Speaks SQL. Handles JSON, text search, and (with pgvector) embeddings.

**Redis** = in-memory key-value store. Data lives in RAM (and optionally on disk). Operations are microseconds. Keys can expire (`EXPIRE`).

**Migration** = a versioned script that changes schema. Never "just ALTER TABLE on prod by hand" as a habit.""",
        "intermediate": """**Normalization** = don't duplicate user emails on every message; store `user_id`. **Denormalization** = copy a field on purpose for read speed. Both are tools.

**EXPLAIN ANALYZE** shows how Postgres runs a query. `Seq Scan` on a large table is a smell if you expected a lookup.

**JSONB** + GIN indexes: good for metadata (`{"source": "wiki", "lang": "en"}`). Bad as a junk drawer for everything.

**Transactions** (`BEGIN`/`COMMIT`) group writes. Either all succeed or none. Use them when you insert a document AND its chunks.

**Redis patterns for AI:**

- `INCR` + `EXPIRE` = rate limit
- `SET key json EX 3600` = cache embedding or a whole answer
- Lists/streams = cheap queues (or use a real queue later)

**N+1 queries:** looping messages and querying the user each time. Join or prefetch.""",
        "advanced": """**Isolation levels.** Default READ COMMITTED is fine. Serializable is for money. Know that two rate-limit checks in Postgres without Redis can race.

**Connection pooling.** Postgres connections are expensive. Use PgBouncer or SQLAlchemy pool. One connection per asyncio task blindly will melt a small instance.

**Partial indexes.** `CREATE INDEX ... WHERE deleted_at IS NULL`.

**LISTEN/NOTIFY** for cheap fanout. Or Redis pub/sub.

**Cache invalidation.** Hardest problem. Prefer short TTLs and cache keys that include `doc_version`.

**pgvector** vs dedicated vector DB: if your scale is < few million vectors and you already operate Postgres, pgvector is a sane default. We compare in Phase 7.""",
        "production": """Backups, point-in-time recovery, migration expand/contract (add column, backfill, then switch), read replicas, and **never** running `DELETE FROM messages` without WHERE in prod.

For AI apps specifically:

- Store **prompt version** and **model name** on each message
- Store **token counts** for cost
- Soft-delete documents so you can rebuild indexes
- Redis is not your chat history

Multi-tenant: `tenant_id` on every table. Row Level Security if you are serious.""",
        "when": "Any state that must survive a restart, any relationship, any audit trail. Redis for counters, locks, hot caches.",
        "when_not": "Do not store 200MB PDFs as bytea. Do not store embeddings-only in Redis without a durable copy. Do not use Mongo 'because JSON' if your data is relational.",
        "code_preview": '''# Redis sliding window rate limit (fixed window shown for clarity)
# INCR user:42:llm_calls  +  EXPIRE 60
# if value > 20: reject
''',
        "code_notes": "Fixed window is simple and slightly bursty at boundaries. Sliding window is fairer. Start simple.",
        "ex_b": "Write CREATE TABLE for users and messages. Insert two rows. JOIN them.",
        "ex_m": "Add an index, prove with EXPLAIN that a query uses it. Write Alembic migration.",
        "ex_h": "Implement Redis rate limit + Postgres chat persist in one Python script with transactions.",
        "project": "Schema + limiter — MiniProject.md.",
        "interview_preview": "Index vs full scan. Why Redis for rate limits. How to migrate without downtime.",
        "flash_sample": "**Q:** Where do PDFs live?\n**A:** Object storage; Postgres stores the URL and metadata.",
        "mistakes_preview": "No index on `user_id`. Chat history in Redis only. SELECT * in a hot path. Storing API keys in a table in plaintext.",
        "debug_preview": "Idle in transaction. Connection pool exhausted. Cache serving stale policy docs.",
        "best": "Migrations in CI. Foreign keys on. UUID PKs or bigints on purpose. TTL on every Redis key. Parameterized queries only.",
        "industry": "Managed Postgres (RDS, Cloud SQL, Neon, Supabase) + ElastiCache/Redis or KeyDB. ORM: SQLAlchemy 2.0 + Alembic.",
        "perf": "Index foreign keys. Limit chat list queries. Don't load full message history if you only need the last 20. Connection pool size ≈ (CPU*2) as a starting heuristic, then measure.",
        "security": "Parameterized SQL (no f-strings). Least-privilege DB roles (the SQL agent in Phase 9 will be read-only). Encrypt disks. Redis AUTH + not exposed to the internet.",
        "refs": "- [Postgres docs](https://www.postgresql.org/docs/)\n- [Redis docs](https://redis.io/docs/)\n- [SQLAlchemy 2.0](https://docs.sqlalchemy.org/)",
        "further": "- *Designing Data-Intensive Applications* (Kleppmann) ch. 2–3\n- Use The Index, Luke",
    },
    "examples": [
        {
            "title": "A chat schema that will survive Phase 8",
            "why": "Design it once. Embeddings can wait. The relations cannot.",
            "code": '''"""code/schema.sql"""
CREATE TABLE users (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email         TEXT UNIQUE NOT NULL,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE conversations (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       UUID NOT NULL REFERENCES users(id),
  title         TEXT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE messages (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
  role          TEXT NOT NULL CHECK (role IN ('user','assistant','system')),
  content       TEXT NOT NULL,
  model         TEXT,
  prompt_version TEXT,
  input_tokens  INT,
  output_tokens INT,
  meta          JSONB NOT NULL DEFAULT '{}',
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX messages_convo_created_idx ON messages (conversation_id, created_at);
''',
            "line_by_line": "UUIDs avoid guessable IDs. CHECK constraint on role. Token columns for cost. Composite index matches 'latest messages in this chat'.",
            "output": "Tables created. \\d messages in psql shows indexes.",
            "dry_run": "CREATE TABLE writes catalog rows. INDEX builds a B-tree on (conversation_id, created_at).",
            "memory": "Empty tables are tiny. Indexes grow with rows.",
            "time": "DDL is O(1) here; index build later is O(n log n)",
            "space": "O(n) rows + O(n) index",
            "alternatives": "Bigserial PKs; separate token_usage table; partitioning messages by month at huge scale.",
            "optimization": "Don't index everything. Write amplification is real.",
        },
        {
            "title": "Fixed-window rate limit in Redis",
            "why": "This is how you stop a buggy client from draining your OpenAI budget.",
            "code": '''"""code/rate_limit.py"""
import time
import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def allow(user_id: str, limit: int = 20, window_s: int = 60) -> bool:
    key = f"rl:{user_id}:{int(time.time() // window_s)}"
    # INCR is atomic. First INCR should set expiry.
    n = r.incr(key)
    if n == 1:
        r.expire(key, window_s)
    return n <= limit
''',
            "line_by_line": "Key includes the window id so it rotates. INCR is atomic so two requests cannot both see 19. Expire only on first increment to avoid resetting the window.",
            "output": "True until the 21st call in that minute.",
            "dry_run": "t=0 n=1 expire set → ... → t=same window n=21 return False.",
            "memory": "One integer per user per window in Redis RAM.",
            "time": "O(1) Redis ops",
            "space": "O(users per window)",
            "alternatives": "Token bucket Lua script; Postgres advisory locks (slower); API gateway limits.",
            "optimization": "Pipeline incr+expire when n==1. Sliding window with ZSET if fairness matters.",
        },
    ],
    "practice": [
        {"title": "psql gym", "body": "Run 10 queries: insert, join, group by token counts, explain.", "done": "You used EXPLAIN at least twice."},
        {"title": "Redis CLI", "body": "SET, GET, INCR, EXPIRE, TTL, KEYS (then promise never to use KEYS in prod — SCAN).", "done": "You saw a key vanish after TTL."},
        {"title": "Migration", "body": "Add `messages.latency_ms` via a migration, not by editing the original CREATE in prod fantasy.", "done": "Upgrade and downgrade scripts exist."},
    ],
    "exercises": {
        "beginner": [
            {"title": "Join practice", "body": "List the last 20 messages with user email.", "constraints": "One query, no N+1."},
            {"title": "JSONB filter", "body": "Store meta.source and query all messages from source=web.", "constraints": "Use JSONB operators, not string search."},
        ],
        "medium": [
            {"title": "Alembic", "body": "Init Alembic, autogenerate from SQLAlchemy models matching schema.sql.", "constraints": "Revision files committed."},
            {"title": "Cache stampede", "body": "Cache a fake expensive embedding. Show two processes missing cache at once. Then add a lock.", "constraints": "Write a paragraph on stampede."},
        ],
        "hard": [
            {"title": "Expand/contract migration", "body": "Rename `title` to `subject` without downtime: add column, backfill, dual-write, switch, drop.", "constraints": "Document each step."},
        ],
    },
    "assignments": [
        {
            "title": "Chat persistence + limiter",
            "time": "4–6 hours",
            "brief": "Python CLI: add-user, new-convo, post-message, list-messages. Redis 10 req/min per user. Docker compose for both stores.",
            "deliverables": ["compose.yaml", "schema", "CLI", "README with EXPLAIN output"],
            "rubric": ["FK constraints", "index used", "limit enforced", "no SQL injection"],
        }
    ],
    "quiz": [
        {"q": "Redis is primarily:", "choices": {"A": "A relational DB", "B": "An in-memory store", "C": "A GPU driver", "D": "An LLM"}, "answer": "B", "explain": "RAM first."},
        {"q": "Chat history should live in:", "choices": {"A": "Only Redis", "B": "Postgres (durable)", "C": "Client localStorage only", "D": "The model weights"}, "answer": "B", "explain": "Durable source of truth."},
        {"q": "An index typically:", "choices": {"A": "Slows reads, speeds writes", "B": "Speeds some reads, slightly slows writes", "C": "Compresses disks", "D": "Trains embeddings"}, "answer": "B", "explain": "Tradeoff."},
        {"q": "Parameterized queries prevent:", "choices": {"A": "GPU OOM", "B": "SQL injection", "C": "Hallucinations", "D": "Slow disks"}, "answer": "B", "explain": "Never f-string user SQL."},
        {"q": "INCR in Redis is:", "choices": {"A": "Not atomic", "B": "Atomic", "C": "Transactional across keys always", "D": "Slow"}, "answer": "B", "explain": "Single-key atomic."},
        {"q": "JSONB is good for:", "choices": {"A": "Replacing all tables", "B": "Variable metadata", "C": "Storing PDFs", "D": "Primary keys"}, "answer": "B", "explain": "Metadata."},
        {"q": "N+1 means:", "choices": {"A": "One plus one indexes", "B": "A query per child row after a parent query", "C": "Sharding", "D": "Two Redis nodes"}, "answer": "B", "explain": "Classic ORM bug."},
        {"q": "TTL on Redis keys:", "choices": {"A": "Is optional decoration", "B": "Prevents unbounded memory", "C": "Is illegal", "D": "Replaces Postgres backups"}, "answer": "B", "explain": "Always set for ephemeral keys."},
        {"q": "A migration is:", "choices": {"A": "A backup", "B": "Versioned schema change", "C": "A Docker image", "D": "An embedding"}, "answer": "B", "explain": "Alembic etc."},
        {"q": "PDFs belong in:", "choices": {"A": "bytea always", "B": "Object storage + URL in SQL", "C": "Redis lists", "D": "Git"}, "answer": "B", "explain": "Blob stores."},
    ],
    "flashcards": [
        {"q": "Source of truth for chats?", "a": "Postgres (or similar RDBMS)."},
        {"q": "Redis use cases in AI apps?", "a": "Rate limit, cache, session, job queue, pub/sub."},
        {"q": "What does EXPLAIN tell you?", "a": "The query plan: scans, joins, estimated cost."},
        {"q": "Foreign key purpose?", "a": "The DB enforces that referenced rows exist."},
        {"q": "Why UUID PKs?", "a": "Not guessable, merge-friendly, can generate in app."},
        {"q": "Cache stampede?", "a": "Many requests miss cache together and slam the origin."},
        {"q": "Parameterized SQL?", "a": "Placeholders + bound values, never string concat."},
        {"q": "Connection pool why?", "a": "Creating PG connections is expensive."},
        {"q": "Soft delete?", "a": "Set deleted_at instead of removing the row."},
        {"q": "When pgvector?", "a": "You already run Postgres and vector scale is moderate."},
    ],
    "interview": [
        {
            "q": "Why not store chat history in Redis?",
            "junior": "Redis is ephemeral (unless you treat it as a primary, which is a different design). Restarts, eviction, and no rich queries. Postgres is durable and queryable.",
            "mistakes": "Redis persistence exists so it is 'the same' as Postgres.",
            "senior": "Redis as cache of recent messages is fine. Dual-write, TTL, and the cost of large values in RAM. AOF/RDB are not a substitute for a relational audit log.",
        },
        {
            "q": "How do you rate-limit LLM calls?",
            "junior": "Redis INCR per user per window. Reject over limit. Mention tokens as a better unit than requests.",
            "mistakes": "In-memory dict on one server. Limit only in the client.",
            "senior": "Token buckets, per-tenant budgets, distributed counters, sliding windows, coupling to billing, 429 + Retry-After.",
        },
        {
            "q": "How does an index help and hurt?",
            "junior": "Faster lookups, extra storage, slower writes.",
            "mistakes": "Index every column.",
            "senior": "Selectivity, covering indexes, write amplification, bloat, VACUUM, partial indexes.",
        },
        {
            "q": "Design storage for a RAG app.",
            "junior": "PG for metadata and chats, object storage for files, vector store for embeddings, Redis for limits.",
            "mistakes": "One Mongo collection named 'data'.",
            "senior": "Versioned documents, rebuildable indexes, tenant isolation, backup/restore story including vectors.",
        },
        {
            "q": "What is a transaction isolation anomaly you actually hit?",
            "junior": "Two requests both think they can insert a unique email.",
            "mistakes": "Pretending they never happen.",
            "senior": "Unique constraints, upsert, serializable vs app-level locks, Redis for hot counters.",
        },
    ],
    "whiteboard": [
        "ER diagram for a multi-tenant RAG app.",
        "Rate limiter: fixed vs sliding vs token bucket.",
        "Zero-downtime add-column migration.",
    ],
    "interview_listen": "whether you separate durable truth from ephemeral counters",
    "cheatsheet": {
        "remember": "PG = truth. Redis = hot & short. Index FKs. Parameterize. TTL everything ephemeral.",
        "bash": "psql $DATABASE_URL\nredis-cli ping\ndocker compose up postgres redis",
        "python": "cur.execute('SELECT * FROM users WHERE email = %s', (email,))  # never f-string",
        "decisions": "Must survive restart → Postgres. Counter/cache → Redis. Big file → object storage. Vectors → Phase 7.",
        "numbers": "Redis ops ~0.1ms local. PG simple PK lookup ~1ms. Pool size: measure. Rate limit windows 60s is a common start.",
        "do_not": "KEYS * in prod. SELECT * on wide tables in hot paths. Redis as only DB. SQL via string concat.",
    },
    "miniproject": {
        "name": "chat-ledger",
        "time": "1 day",
        "difficulty": "Medium",
        "why": "Every later project will import this schema idea.",
        "story": "I can persist chats and get 429ed when I spam.",
        "must": ["compose Postgres+Redis", "schema.sql", "CLI", "rate limit 20/min", "README with EXPLAIN"],
        "should": ["Alembic", "token columns"],
        "wont": ["UI", "embeddings yet"],
        "architecture": "```mermaid\nflowchart LR\nCLI --> PG\nCLI --> Redis\n```",
        "layout": "compose.yaml schema.sql src/ledger/",
        "rubric": ["FKs", "index used", "limit works", "gitignore .env"],
        "stretch": "Sliding window limiter in Lua.",
    },
    "resources": {
        "official": ["[Postgres tutorial](https://www.postgresql.org/docs/current/tutorial.html)", "[Redis commands](https://redis.io/commands/)", "[SQLAlchemy 2](https://docs.sqlalchemy.org/)"],
        "extra": ["Use The Index, Luke", "Postgres weekly"],
        "papers": ["Not required. Read Kleppmann if you want depth."],
    },
    "faq": [
        {"q": "SQLite enough?", "a": "For Phase 2 drills on a plane, yes. For Compose + Redis drills, use Postgres. pgvector and production features differ."},
        {"q": "ORM or raw SQL?", "a": "Learn SQL first. Then SQLAlchemy. Never only an ORM you cannot see through."},
        {"q": "Do I need Kafka?", "a": "No."},
    ],
    "debugging": [
        {
            "title": "too many clients already",
            "symptom": "Postgres rejects connections.",
            "wrong": "Open a new connection per request without pooling, forget to close.",
            "see": "`SELECT count(*) FROM pg_stat_activity;`",
            "fix": "Pool. Close. Find idle-in-transaction.",
            "prevent": "SQLAlchemy pool + context managers.",
        },
        {
            "title": "Rate limit never expires",
            "symptom": "User blocked forever.",
            "wrong": "INCR without EXPIRE, or EXPIRE on every hit resetting the window wrongly / not at all.",
            "see": "`TTL key` in redis-cli.",
            "fix": "Set expire when n==1. Alert on keys without TTL.",
            "prevent": "A wrapper that always takes ttl.",
        },
    ],
    "mistakes": [
        {"title": "Building SQL with f-strings", "body": "SQL injection. Game over.", "instead": "Bound parameters."},
        {"title": "No index on conversation_id", "body": "List-messages becomes a seq scan.", "instead": "Composite index matching the query."},
        {"title": "Cache without version", "body": "Users see yesterday's policy after a doc update.", "instead": "Key includes doc hash or version."},
    ],
    "prod_tips": {
        "cost": "Managed PG is cheap vs your time. Redis RAM is the cost to watch — do not cache 10MB answers blindly.",
        "latency": "Chat list should be indexed. Round-trips kill: batch.",
        "reliability": "Backups you have restored once. Migrations in CI against a throwaway DB.",
        "observability": "slow query log. Redis `INFO stats`. Token usage table.",
        "scaling": "Vertical first. Read replica for analytics. Partition messages when you actually need it.",
        "checklist": ["FKs on", "backups", "pool", "TTL", "parameterized SQL", "tenant_id plan"],
    },
    "challenge": {
        "title": "Multi-tenant row isolation",
        "body": "Two tenants. Prove a query without tenant_id in the WHERE cannot leak (RLS policy).",
        "constraints": ["Postgres RLS", "two roles"],
        "success": "A test that fails when RLS is disabled and passes when enabled.",
    },
    "solutions": [
        {"id": "B1 join", "hint": "JOIN users ON ... ORDER BY created_at DESC LIMIT 20", "approach": "Index (conversation_id, created_at desc)."},
        {"id": "M2 stampede", "hint": "SET lock key NX EX 10 while computing.", "approach": "Only one worker fills cache; others wait or serve stale."},
    ],
    "code_files": {
        "schema.sql": """CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  title TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
  role TEXT NOT NULL CHECK (role IN ('user','assistant','system')),
  content TEXT NOT NULL,
  model TEXT,
  prompt_version TEXT,
  input_tokens INT,
  output_tokens INT,
  meta JSONB NOT NULL DEFAULT '{}',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX messages_convo_created_idx ON messages (conversation_id, created_at);
""",
        "rate_limit.py": '''"""Fixed-window rate limiter using Redis INCR."""
from __future__ import annotations

import time

import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


def allow(user_id: str, limit: int = 20, window_s: int = 60) -> bool:
    key = f"rl:{user_id}:{int(time.time() // window_s)}"
    n = r.incr(key)
    if n == 1:
        r.expire(key, window_s)
    return n <= limit
''',
    },
}
