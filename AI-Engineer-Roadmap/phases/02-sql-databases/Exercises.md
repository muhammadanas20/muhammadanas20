# Exercises — Phase 2: SQL, Postgres, and Redis

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Join practice

List the last 20 messages with user email.

**Constraints:** One query, no N+1.

### B2. JSONB filter

Store meta.source and query all messages from source=web.

**Constraints:** Use JSONB operators, not string search.

## Medium

### M1. Alembic

Init Alembic, autogenerate from SQLAlchemy models matching schema.sql.

**Constraints:** Revision files committed.

### M2. Cache stampede

Cache a fake expensive embedding. Show two processes missing cache at once. Then add a lock.

**Constraints:** Write a paragraph on stampede.

## Hard

### H1. Expand/contract migration

Rename `title` to `subject` without downtime: add column, backfill, dual-write, switch, drop.

**Constraints:** Document each step.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase2/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
