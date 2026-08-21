# Cheatsheet — Phase 2: SQL, Postgres, and Redis

Print or pin. This is not a substitute for Theory.md.

## Remember

PG = truth. Redis = hot & short. Index FKs. Parameterize. TTL everything ephemeral.

## Commands / snippets

```bash
psql $DATABASE_URL
redis-cli ping
docker compose up postgres redis
```

```python
cur.execute('SELECT * FROM users WHERE email = %s', (email,))  # never f-string
```

## Decision tree

Must survive restart → Postgres. Counter/cache → Redis. Big file → object storage. Vectors → Phase 7.

## Numbers

Redis ops ~0.1ms local. PG simple PK lookup ~1ms. Pool size: measure. Rate limit windows 60s is a common start.

## Do not

KEYS * in prod. SELECT * on wide tables in hot paths. Redis as only DB. SQL via string concat.
