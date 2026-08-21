# Production tips — Phase 2: SQL, Postgres, and Redis

## Cost

Managed PG is cheap vs your time. Redis RAM is the cost to watch — do not cache 10MB answers blindly.

## Latency

Chat list should be indexed. Round-trips kill: batch.

## Reliability

Backups you have restored once. Migrations in CI against a throwaway DB.

## Observability

slow query log. Redis `INFO stats`. Token usage table.

## Scaling

Vertical first. Read replica for analytics. Partition messages when you actually need it.

## The boring checklist

- FKs on
- backups
- pool
- TTL
- parameterized SQL
- tenant_id plan

Production is not a later phase. It is a way of writing Tuesday's code.
