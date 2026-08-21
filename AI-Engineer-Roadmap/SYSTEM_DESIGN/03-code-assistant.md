# Design: coding assistant over a monorepo

Chunk by AST / function, not 500 chars.

Index per commit SHA. Don't serve stale index after big refactors without rebuild.

Eval: unit tests as oracle where possible.

Security: no `run_tests` as root; sandbox. Don't embed `.env`.

MCP: `read_file`, `search`, `get_symbol`.
