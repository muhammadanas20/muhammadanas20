# Debugging — Phase 3: FastAPI

Debugging is the job. These are bugs we see every week.

## Bug 1. 422 Unprocessable Entity

**Symptom**

Request 'looks fine' in the UI.

**Broken mental model**

JSON types: sending string where int expected; missing field.

**How to see it**

The 422 body lists loc/msg.

**Fix**

Match the pydantic model. Print the OpenAPI schema.

**Prevention**

Share the OpenAPI with frontend. Generate a client.
## Bug 2. SSE arrives in one blob

**Symptom**

UI waits then dumps the answer.

**Broken mental model**

Proxy or gzip buffering.

**How to see it**

curl -N, check Nginx, disable gzip on that location.

**Fix**

X-Accel-Buffering: no; chunked transfer.

**Prevention**

Load test through the real proxy early.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
