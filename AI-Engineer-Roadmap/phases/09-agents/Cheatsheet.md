# Cheatsheet — Phase 9: Agents

Print or pin. This is not a substitute for Theory.md.

## Remember

Loop + allow-list + max steps. You run tools. SQL is read-only. Graphs when state is real.

## Commands / snippets

```bash
pytest tests/test_sql_guard.py
```

```python
for i in range(MAX):
    ...
```

## Decision tree

FAQ → RAG. Multi-step tools → agent. Known flowchart → graph or even plain code.

## Numbers

max_steps 3–8. Tool timeout 5–30s. Reflection only on high stakes.

## Do not

shell in prod. Uncapped. Admin DB. Multi-agent theater.
