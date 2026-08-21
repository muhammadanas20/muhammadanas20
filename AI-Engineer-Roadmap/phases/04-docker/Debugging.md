# Debugging — Phase 4: Docker

Debugging is the job. These are bugs we see every week.

## Bug 1. connection refused to postgres

**Symptom**

API boots, DB errors.

**Broken mental model**

DATABASE_URL uses localhost.

**How to see it**

Print the URL (without password). docker compose exec api ping postgres.

**Fix**

Hostname postgres. Wait for healthy.

**Prevention**

compose depends_on condition + README.
## Bug 2. Permission denied on volume

**Symptom**

Non-root user cannot write.

**Broken mental model**

Volume owned by root from an earlier run.

**How to see it**

ls -l inside container.

**Fix**

chown, or init container, or matching uid.

**Prevention**

Document uids. Don't mix root and non-root writes.


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
