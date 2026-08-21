# Cheatsheet — Phase 5: LLM fundamentals

Print or pin. This is not a substitute for Theory.md.

## Remember

Next-token ≠ truth. Temp 0 extract. Validate JSON. You run tools. Context is finite.

## Commands / snippets

```bash
ollama run llama3.2
uv pip install openai tiktoken pydantic
```

```python
Ticket.model_validate_json(raw)  # never json.loads hope
```

## Decision tree

Facts change → retrieve. Format → schema. Style at scale → fine-tune. Regex enough → no LLM.

## Numbers

~4 chars/token English. Context 8k–200k+ depending on model. Cap tool hops 3–8.

## Do not

Secrets in prompts. Unbounded loops. temp 1 for invoices. Fine-tune weekly facts.
