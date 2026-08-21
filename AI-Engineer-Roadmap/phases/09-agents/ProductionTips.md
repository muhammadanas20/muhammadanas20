# Production tips — Phase 9: Agents

## Cost

Each hop is a full model fee. Budget hops. Smaller model for tool choice.

## Latency

Parallel tools. Stream the final answer only.

## Reliability

Timeouts, retries on tools not on non-idempotent POSTs, fallback to human.

## Observability

Trace tool name, args (redacted), duration, result size.

## Scaling

Agents are QPS-expensive. Queue. Don't hide a batch job in an agent.

## The boring checklist

- max_steps
- allow-list
- timeouts
- least privilege
- traces
- adversarial tests

Production is not a later phase. It is a way of writing Tuesday's code.
