# LLM cheatsheet

- Next token ≠ truth
- ~4 chars / token English (measure)
- Temp **0** for JSON / classify
- Pin model versions
- `max_tokens` + timeout
- Structured output + **pydantic**
- You run tools; the model only proposes
- Cap tool hops
- Version prompts in git
- Log tokens, latency, parse_ok
- Don't put secrets in prompts
- RAG for changing facts; fine-tune for style
