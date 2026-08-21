# Debugging — Phase 14: Capstone

Debugging is the job. These are bugs we see every week.

## Bug 1. Infinite polish

**Symptom**

Never deployed.

**Broken mental model**

The demo needs one more framework.

**How to see it**

MUST list.

**Fix**

Freeze. Ship.

**Prevention**

Calendar the freeze on day 1.
## Bug 2. Demo fail on Wi-Fi

**Symptom**

Vendor timeout.

**Broken mental model**

No backup video, no local fallback.

**How to see it**

Chaos exercise.

**Fix**

Video + local compose.

**Prevention**

Rehearse offline path.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
