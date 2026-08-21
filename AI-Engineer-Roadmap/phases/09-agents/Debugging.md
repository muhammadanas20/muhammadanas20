# Debugging — Phase 9: Agents

Debugging is the job. These are bugs we see every week.

## Bug 1. Invalid tool JSON

**Symptom**

Exception in dispatcher.

**Broken mental model**

Trusting args.

**How to see it**

Raw tool_call.

**Fix**

json.loads in try; return error to model; pydantic schemas.

**Prevention**

Structured tool APIs.
## Bug 2. Loop of searches

**Symptom**

Same query 8 times.

**Broken mental model**

No step counter; model 'try again'.

**How to see it**

Trace.

**Fix**

max_steps, detect duplicate tool args, then stop.

**Prevention**

Runtime guards > prompt guards.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
