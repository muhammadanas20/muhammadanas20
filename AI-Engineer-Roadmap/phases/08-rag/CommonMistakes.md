# Common mistakes — Phase 8: Retrieval-Augmented Generation (RAG)

### 1. Evaluating only by chatting with it

You remember the happy path.

**Do this instead:** Frozen JSONL + scores in CI.

### 2. Retrieving then ignoring 'I don't know'

The model fills gaps from pretraining.

**Do this instead:** Explicit abstain; maybe a classifier.

### 3. One pipeline for all query types

Navigational, factual, summary, chit-chat need different handling.

**Do this instead:** Route. Chit-chat should not retrieve random docs.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
