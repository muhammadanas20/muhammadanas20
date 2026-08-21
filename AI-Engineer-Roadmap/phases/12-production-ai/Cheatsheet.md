# Cheatsheet — Phase 12: Production AI / LLMOps

Print or pin. This is not a substitute for Theory.md.

## Remember

Trace. Eval in CI. Pin models. Tenant in cache keys. Fallback. Budget.

## Commands / snippets

```bash
pytest tests/eval -q
# langfuse / promptfoo CLIs as you choose
```

```python
try: primary()
except TimeoutError: fallback()
```

## Decision tree

Exact cache first. Semantic cache later. Router if cost hurts.

## Numbers

Sample 1% online. TTFT SLO ~1–2s chat. Set a real $ daily cap.

## Do not

PII traces. Cross-tenant cache. Unpinned aliases. 500-only alerts.
