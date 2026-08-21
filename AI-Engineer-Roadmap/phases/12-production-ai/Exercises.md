# Exercises — Phase 12: Production AI / LLMOps

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. CSV logger

model, tokens, ms, cache_hit.

**Constraints:** 50 rows from a script.

### B2. Budget

Fail 429-like after N tokens.

**Constraints:** Test.

## Medium

### M1. Redis cache

TTL 60s, tenant in key.

**Constraints:** Prove cross-tenant miss.

### M2. Fallback

Primary raises, secondary returns, metric fallback=1.

**Constraints:** Test with monkeypatch.

## Hard

### H1. CI eval gate

Ragas or custom score; fail < 0.7 on 10 cases.

**Constraints:** YAML in Actions.

### H2. Shadow prompt

v2 runs in background, scores logged, v1 still served.

**Constraints:** No user-facing change.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase12/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
