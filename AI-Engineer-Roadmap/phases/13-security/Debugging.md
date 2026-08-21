# Debugging — Phase 13: Security

Debugging is the job. These are bugs we see every week.

## Bug 1. System prompt leak

**Symptom**

User pastes your handbook on Twitter.

**Broken mental model**

You put a key in it. Or you cared too much about secrecy vs blast radius.

**How to see it**

What's in the prompt.

**Fix**

Remove secrets. Assume leak. Rotate if needed.

**Prevention**

Secrets never in prompts.
## Bug 2. Guardrail false positive

**Symptom**

Legit medical/legal questions blocked.

**Broken mental model**

Keyword filters.

**How to see it**

False positive set.

**Fix**

Allow-list internal intents; tune; don't block retrieval of your own policies.

**Prevention**

Eval safety and utility together.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
