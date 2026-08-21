# Challenge — Phase 2: SQL, Postgres, and Redis

This is optional. It is also how you get interesting interview stories.

## Multi-tenant row isolation

Two tenants. Prove a query without tenant_id in the WHERE cannot leak (RLS policy).

**Constraints**

- Postgres RLS
- two roles

**Success looks like**

A test that fails when RLS is disabled and passes when enabled.
