# Design: text-to-SQL analyst

Prefer a **semantic layer** (approved metrics) over free SQL.

If free SQL: read-only, parser, LIMIT, column ACLs, dry-run EXPLAIN, audit.

Eval: Spider-like gold queries on a snapshot warehouse.

Never: model as superuser.
