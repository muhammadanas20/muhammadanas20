# FAQ — Phase 12: Production AI / LLMOps

### Langfuse or LangSmith?

Either. Open source / self-host bias → Langfuse. Already in LangChain ecosystem → LangSmith. Learn traces, not logos.

### Must I OpenTelemetry?

It's the portable layer. Fine to start with a vendor SDK.

### Eval cost?

Run small in CI (10–30 cases). Nightly full set. Don't judge 10k traces with GPT-4 every commit.

Didn't see your question? Open an issue. Beginner questions are first-class.
