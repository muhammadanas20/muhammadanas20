# LLM interview extras

**Q. Why might two identical requests differ?**  
Sampling temperature, provider-side updates, unpinned aliases, non-deterministic GPU kernels, tools racing.

**Q. What is a stop sequence?**  
A token pattern that ends generation. Less critical in chat APIs; still useful in completion-style local models.

**Q. How do you estimate tokens without the vendor tokenizer?**  
Rough 4 chars/token, then measure with the real tokenizer before you promise a CFO.

**Q. JSON mode returned extra keys.**  
Pydantic `extra='ignore'` or `'forbid'`. Prefer schema-constrained decoding.

**Q. Should the system prompt contain examples?**  
Few-shot helps format. It costs tokens. Prefer schemas when the API supports them.

Senior: discuss prompt caching, speculative decoding only at a high level, and why you still validate.
