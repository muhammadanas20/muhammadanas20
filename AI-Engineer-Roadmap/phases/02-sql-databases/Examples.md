# Examples — Phase 2: SQL, Postgres, and Redis

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. A chat schema that will survive Phase 8

Design it once. Embeddings can wait. The relations cannot.

```python
"""code/schema.sql"""
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

```

**What every interesting line is doing**

UUIDs avoid guessable IDs. CHECK constraint on role. Token columns for cost. Composite index matches 'latest messages in this chat'.

**Expected output**

```text
Tables created. \d messages in psql shows indexes.
```

**Dry run**

CREATE TABLE writes catalog rows. INDEX builds a B-tree on (conversation_id, created_at).

**Memory**

Empty tables are tiny. Indexes grow with rows.

**Time complexity:** DDL is O(1) here; index build later is O(n log n)  
**Space complexity:** O(n) rows + O(n) index

**Alternatives**

Bigserial PKs; separate token_usage table; partitioning messages by month at huge scale.

**Optimization**

Don't index everything. Write amplification is real.

---

### Example 2. Fixed-window rate limit in Redis

This is how you stop a buggy client from draining your OpenAI budget.

```python
"""code/rate_limit.py"""
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

```

**What every interesting line is doing**

Key includes the window id so it rotates. INCR is atomic so two requests cannot both see 19. Expire only on first increment to avoid resetting the window.

**Expected output**

```text
True until the 21st call in that minute.
```

**Dry run**

t=0 n=1 expire set → ... → t=same window n=21 return False.

**Memory**

One integer per user per window in Redis RAM.

**Time complexity:** O(1) Redis ops  
**Space complexity:** O(users per window)

**Alternatives**

Token bucket Lua script; Postgres advisory locks (slower); API gateway limits.

**Optimization**

Pipeline incr+expire when n==1. Sliding window with ZSET if fairness matters.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
