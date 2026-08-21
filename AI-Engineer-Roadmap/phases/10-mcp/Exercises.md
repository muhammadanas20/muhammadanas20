# Exercises — Phase 10: Model Context Protocol (MCP)

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Wrap ping

MCP server with ping tool.

**Constraints:** A client can call it.

### B2. Resource

Expose README.md as a resource URI.

**Constraints:** Client reads it.

## Medium

### M1. course_search tool

Search this course Markdown.

**Constraints:** Returns top 3 snippets.

### M2. Prompt template

Expose explain_phase(n).

**Constraints:** Client can get the prompt.

## Hard

### H1. HTTP + token

Remote transport with Authorization header.

**Constraints:** Reject missing token.

### H2. Least privilege

Two tools, only one enabled by config.

**Constraints:** Test both modes.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase10/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
