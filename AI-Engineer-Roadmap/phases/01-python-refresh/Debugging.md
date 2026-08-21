# Debugging — Phase 1: Python refresh

Debugging is the job. These are bugs we see every week.

## Bug 1. coroutine was never awaited

**Symptom**

RuntimeWarning and nothing happens.

**Broken mental model**

Calling async def like a normal function runs it.

**How to see it**

You forgot await or asyncio.run.

**Fix**

await foo() inside async; asyncio.run(foo()) at the edge.

**Prevention**

Type checkers warn if you configure them.
## Bug 2. Tests hang

**Symptom**

pytest never ends.

**Broken mental model**

Forgot timeout; waited on a real network.

**How to see it**

Which await never returns. Add timeout= to httpx.

**Fix**

Mock network. Always set timeout.

**Prevention**

pytest-timeout plugin.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
