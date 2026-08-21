# Debugging — Phase 5: LLM fundamentals

Debugging is the job. These are bugs we see every week.

## Bug 1. content is None

**Symptom**

You print message.content and it's empty.

**Broken mental model**

Assuming every turn is text. It may be a tool_call.

**How to see it**

Log the raw response object.

**Fix**

Branch on tool vs text.

**Prevention**

Typed response handling.
## Bug 2. JSON cut in half

**Symptom**

ValidationError unexpected end.

**Broken mental model**

max_tokens too small or output too chatty before JSON.

**How to see it**

finish_reason=length.

**Fix**

Raise max_tokens, instruct 'JSON only', use schema mode.

**Prevention**

Monitor finish_reason.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
