# Debugging — Phase 12: Production AI / LLMOps

Debugging is the job. These are bugs we see every week.

## Bug 1. Eval score jumped 20%

**Symptom**

Looks like a win.

**Broken mental model**

Gold labels edited; judge model changed; leak.

**How to see it**

Diff the dataset and judge version.

**Fix**

Pin everything. Holdout.

**Prevention**

Dataset version in the report.
## Bug 2. Cache served another tenant's answer

**Symptom**

Data leak.

**Broken mental model**

Key = query only.

**How to see it**

Redis keys.

**Fix**

tenant_id in key. Flush.

**Prevention**

Test two tenants same query.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
