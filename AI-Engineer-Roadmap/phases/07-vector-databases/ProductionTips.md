# Production tips — Phase 7: Vector databases

## Cost

RAM is the bill. Quantize or dedicated engine when numpy/PG hurts. Managed DBs charge for units — read the invoice math.

## Latency

Measure with filters and with cold start. HNSW efSearch is a knob.

## Reliability

Rebuild playbook. Snapshots. Don't be the person who can only restore chats but not search.

## Observability

Log collection, k, filter, latency, result ids.

## Scaling

Vertical then shards. Don't shard at 20k vectors.

## The boring checklist

- dim match
- metric match
- tenant tests
- backup/rebuild
- private net

Production is not a later phase. It is a way of writing Tuesday's code.
