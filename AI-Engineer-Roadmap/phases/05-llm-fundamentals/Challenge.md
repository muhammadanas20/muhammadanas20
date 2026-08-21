# Challenge — Phase 5: LLM fundamentals

This is optional. It is also how you get interesting interview stories.

## Provider adapter

One interface `complete(messages, tools, schema)` with OpenAI and Ollama backends. Tests fake both.

**Constraints**

- No if openai in business logic
- Feature flag env

**Success looks like**

Switching providers is an env var.
