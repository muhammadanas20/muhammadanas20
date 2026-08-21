# Exercises — Phase 13: Security

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Injection suite

10 direct injections against your chatbot.

**Constraints:** Spreadsheet of pass/fail.

### B2. PII redact

Redact emails in logs with a regex; know the limits.

**Constraints:** Tests.

## Medium

### M1. Indirect

A markdown file in the corpus with injection. Query it.

**Constraints:** Before/after mitigation.

### M2. RBAC

viewer vs admin tools.

**Constraints:** Tests.

## Hard

### H1. Threat model

One page for your capstone.

**Constraints:** Assets, attackers, controls.

### H2. Exfil

Try to get the model to reveal another tenant's chunk. Must fail.

**Constraints:** Automated.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase13/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
