# SQL Agent

**Phase:** 9  
**Time:** 3–5 days

Natural language → **guarded SELECT** → table.

## Threat model (write this first)

- Attacker wants DROP TABLE / data from another tenant
- Controls: read-only role, parser, LIMIT, allow-listed tables, max steps, traces

## Must

- `guard_sql` from Phase 9
- Read-only DB user in compose
- Adversarial tests (see `tests/adversarial.sql.txt`)
- Trace every tool call
- FastAPI or CLI

## Must not

- Execute model-produced SQL as a superuser
- `eval()` anything
