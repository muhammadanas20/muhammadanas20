# Code Assistant

**Phase:** 10  
**Time:** 1 week

Repo Q&A via **RAG + MCP**.

- Index `*.py` with language-aware chunks (don't split mid-function if you can)
- MCP server: `search_repo`, `read_file`
- Agent consumes MCP
- Never execute arbitrary repo code as a tool in v1

## Security

Treat the repo as untrusted if it isn't yours. Don't mount `.env`.
