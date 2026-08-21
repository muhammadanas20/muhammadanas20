# Common mistakes — Phase 5: LLM fundamentals

### 1. Prompt in a Slack screenshot as the source of truth

Nobody can review or rollback.

**Do this instead:** File in git with a version field logged on each call.

### 2. temperature=1 for extraction

Random JSON, random categories.

**Do this instead:** 0 or 0.1.

### 3. Letting the model invent tool results

It will. Fluently.

**Do this instead:** If a tool fails, send the error; do not ask it to guess the order status.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
