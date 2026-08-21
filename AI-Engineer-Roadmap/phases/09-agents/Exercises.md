# Exercises — Phase 9: Agents

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Two-tool loop

add and now, real or fake model.

**Constraints:** max_steps test.

### B2. Unknown tool

Model asks for shell. You return error JSON, do not crash.

**Constraints:** Fail closed.

## Medium

### M1. LangGraph retry

A node fails, edge retries once, then ends.

**Constraints:** State includes attempt count.

### M2. Memory

Persist last 5 facts per user in Postgres, retrieve into system prompt.

**Constraints:** Not the whole history forever.

## Hard

### H1. SQL agent

Read-only, LIMIT, traces, 10 adversarial prompts.

**Constraints:** Zero DDL success.

### H2. Supervisor two-agent

Researcher + writer with a hard turn cap.

**Constraints:** Cost log.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase9/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
