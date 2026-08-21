# Production tips — Phase 13: Security

## Cost

Attacks can burn tokens. Budgets per user. Anomaly alerts.

## Latency

Run cheap filters first; expensive policy model async if you can.

## Reliability

Fail closed on authz. Fail open on a down safety API only if blast radius is tiny — usually fail closed too.

## Observability

Log denials, injection heuristic hits, tool RBAC failures.

## Scaling

Authz checks are cheap compared to LLMs. Do them.

## The boring checklist

- threat model
- injection tests
- RBAC
- redaction
- no shell
- secret scan

Production is not a later phase. It is a way of writing Tuesday's code.
