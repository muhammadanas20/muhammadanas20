# Cheatsheet — Phase 6: Embeddings and search

Print or pin. This is not a substitute for Theory.md.

## Remember

Same model. Structure-aware chunks. Metadata. Eval recall@k. Keyword still lives.

## Commands / snippets

```bash
uv pip install numpy sentence-transformers tiktoken
```

```python
scores = (index / norms) @ (q / qn)
```

## Decision tree

IDs → keyword. Paraphrase → dense. Both → hybrid (Phase 8).

## Numbers

Chunk 200–800 tokens. Overlap ~10–20%. 768-d * 4B * N RAM.

## Do not

Mix models. Slice tables. Embed secrets. Skip eval.
