# Debugging — Phase 11: Deployment

Debugging is the job. These are bugs we see every week.

## Bug 1. 502 Bad Gateway

**Symptom**

Platform URL fails.

**Broken mental model**

App listens on 127.0.0.1 or wrong PORT.

**How to see it**

Logs. PORT env. docker run locally with same env.

**Fix**

0.0.0.0 and the platform's PORT.

**Prevention**

Smoke test in CI against the container.
## Bug 2. Works then dies after 30s

**Symptom**

SSE/chat cut off.

**Broken mental model**

Proxy idle timeout.

**How to see it**

Platform timeout settings. Nginx proxy_read_timeout.

**Fix**

Raise timeouts; heartbeats.

**Prevention**

Load test the real URL, not localhost.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
