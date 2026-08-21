# Exercises — Phase 3: FastAPI

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Notes API

CRUD notes in memory with pydantic. 404/422 correct.

**Constraints:** No DB yet.

### B2. Status codes

A cheat-route table: map 8 situations to codes.

**Constraints:** Include 409 and 429.

## Medium

### M1. JWT login

POST /login returns token. /me needs it.

**Constraints:** Tests included. Secret from env.

### M2. Pagination

GET /messages?cursor=&limit=

**Constraints:** No offset pagination.

## Hard

### H1. Disconnect

Prove that closing the client stops fake_tokens (use a flag).

**Constraints:** Automated test.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase3/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
