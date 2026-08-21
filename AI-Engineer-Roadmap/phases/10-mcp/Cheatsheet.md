# Cheatsheet — Phase 10: Model Context Protocol (MCP)

Print or pin. This is not a substitute for Theory.md.

## Remember

USB for tools. stderr logs. Least privilege. Auth remote. Not a model.

## Commands / snippets

```bash
python -m my_mcp_server  # stdio
# configure in client JSON
```

```python
print(msg, file=sys.stderr)
```

## Decision tree

Reusable across hosts → MCP. One caller → function.

## Numbers

Keep resource sizes prompt-small. Tool timeouts still apply.

## Do not

stdout debug. Public unauth HTTP. Whole-home filesystem. .env resources.
