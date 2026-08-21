# Debugging — Phase 10: Model Context Protocol (MCP)

Debugging is the job. These are bugs we see every week.

## Bug 1. Client shows zero tools

**Symptom**

Server seems running.

**Broken mental model**

Handshake failed; stdout polluted; wrong command path.

**How to see it**

stderr logs; run server manually; validate JSON-RPC.

**Fix**

Clean stdout, fix initialize, check config command/args.

**Prevention**

A script client in tests.
## Bug 2. Broken JSON

**Symptom**

Parse errors in client.

**Broken mental model**

print() in a tool.

**How to see it**

Capture stdout.

**Fix**

stderr only.

**Prevention**

Lint for print.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
