# Design: multi-tenant RAG SaaS

API keys hashed. Quota in Redis. `tenant_id` on PG rows, vectors, cache keys, logs.

Tests: same query, two tenants, zero overlap.

Noisy neighbor: per-tenant QPS and token budgets.

Onboarding: upload docs, isolate collection or payload filter + tests.

Billing stub: usage records from token logs.
