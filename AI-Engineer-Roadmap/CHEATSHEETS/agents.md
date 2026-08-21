# Agents cheatsheet

```
for step in range(MAX):
    if tool: run allow-listed tool
    else: return text
raise timeout
```

- FAQ → RAG, not an agent
- Allow-list + timeouts + max_steps
- SQL: read-only role + parser + LIMIT
- HITL for money / email / writes
- LangGraph when state/cycles are real
- Multi-agent only with a reason
- Trace every tool
- Policy in Python, not only in the prompt
