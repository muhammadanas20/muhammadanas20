# Cheatsheet — Phase 8: Retrieval-Augmented Generation (RAG)

Print or pin. This is not a substitute for Theory.md.

## Remember

Retrieve → generate → eval. Hybrid+rerank before agents. I don't know is a feature. Citations must be real.

## Commands / snippets

```bash
pytest tests/eval_rag.py -q
```

```python
hits = hybrid(q); top = rerank(q, hits)[:5]; answer = generate(q, top)
```

## Decision tree

FAQ → naive/hybrid. Messy queries → rewrite. Global themes → maybe graph. Multi-hop tools → agentic.

## Numbers

k retrieve 20, rerank to 5. Gold set 25–100. Faithfulness: track it, set a bar (e.g. 0.8) that matches YOUR judge.

## Do not

GraphRAG first. Tune on the only eval set without a holdout. Invent citations. 50 chunks in context by default.
