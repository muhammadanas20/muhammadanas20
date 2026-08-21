# Debugging — Phase 2: SQL, Postgres, and Redis

Debugging is the job. These are bugs we see every week.

## Bug 1. too many clients already

**Symptom**

Postgres rejects connections.

**Broken mental model**

Open a new connection per request without pooling, forget to close.

**How to see it**

`SELECT count(*) FROM pg_stat_activity;`

**Fix**

Pool. Close. Find idle-in-transaction.

**Prevention**

SQLAlchemy pool + context managers.
## Bug 2. Rate limit never expires

**Symptom**

User blocked forever.

**Broken mental model**

INCR without EXPIRE, or EXPIRE on every hit resetting the window wrongly / not at all.

**How to see it**

`TTL key` in redis-cli.

**Fix**

Set expire when n==1. Alert on keys without TTL.

**Prevention**

A wrapper that always takes ttl.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
