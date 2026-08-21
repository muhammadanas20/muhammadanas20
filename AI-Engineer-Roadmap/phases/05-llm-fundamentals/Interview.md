# Interview — Phase 5: LLM fundamentals

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. What is a token and why do I care?

**Expected answer (junior)**

A tokenizer piece. Billing, rate limits, and context windows are in tokens. English ~4 chars/token but measure.

**Common mistakes**

1 word = 1 token always. Confusing tokens with embeddings.

**Senior-level discussion**

Tokenizer mismatch, multilingual cost, prompt caching billed differently, output vs input prices.
### Q2. When do you fine-tune vs RAG vs prompt?

**Expected answer (junior)**

Prompt first. RAG for private/changing facts. Fine-tune for style or a skill with many examples.

**Common mistakes**

Fine-tune the employee handbook.

**Senior-level discussion**

Evals, cost of training, latency, on-policy data, LoRA, catastrophic forgetting, eval regressions.
### Q3. How does function calling work end to end?

**Expected answer (junior)**

Declare schema, model returns tool call, app executes, app sends result, model answers. Allow-list.

**Common mistakes**

The model executes SQL itself. eval() on tool name.

**Senior-level discussion**

Parallel calls, idempotency, human-in-the-loop, injection via tool results, max hops.
### Q4. The model returned invalid JSON. Now what?

**Expected answer (junior)**

Validate, retry with error, lower temperature, use JSON schema mode, eventually fail closed.

**Common mistakes**

regex salvage forever; ignore the error.

**Senior-level discussion**

Constrained decoding, repair models, metrics on parse-fail rate, fallback to a bigger model.
### Q5. Why not put the entire corpus in the prompt?

**Expected answer (junior)**

Token cost, latency, context limits, lost-in-the-middle, PII sprawl.

**Common mistakes**

128k context means we are done with RAG.

**Senior-level discussion**

Needle-in-haystack benches vs real docs, cache, security, and still needing citations.


---

## Whiteboard prompts

- Draw a tool-call loop with a max-step guard.
- Estimate monthly cost: 10k chats/day, 1.5k tokens in, 400 out, pick a price.
- Compare dumping a PDF vs RAG for a 200-page policy.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for tokens, variance, tools-as-your-code, RAG vs weights.
