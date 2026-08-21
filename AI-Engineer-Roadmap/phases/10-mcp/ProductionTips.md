# Production tips — Phase 10: Model Context Protocol (MCP)

## Cost

Each tool result enters the prompt — keep results small.

## Latency

Local stdio is ms. Remote is network + tool time.

## Reliability

Version tools. Health tool. Timeouts.

## Observability

Log tool, args hash, duration, user.

## Scaling

Remote servers are just services. Same as FastAPI scale.

## The boring checklist

- stderr
- least privilege
- auth if remote
- no secrets
- tests with a fake client

Production is not a later phase. It is a way of writing Tuesday's code.
