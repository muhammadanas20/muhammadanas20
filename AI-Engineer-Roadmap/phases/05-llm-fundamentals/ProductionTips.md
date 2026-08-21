# Production tips — Phase 5: LLM fundamentals

## Cost

Log tokens. Alert on daily budget. Cache identical prompts. Smaller model for classification.

## Latency

Stream. Shrink prompts. Parallelize independent calls. TTFT SLO.

## Reliability

Timeouts, retries on 429/5xx, fallback model, fail closed on parse.

## Observability

model, prompt_version, tokens, latency, parse_ok. Phase 12 adds traces.

## Scaling

The bottleneck is usually the provider RPM. Queue. Don't hot-loop.

## The boring checklist

- temp set on purpose
- max_tokens
- validate
- timeout
- token log
- prompt version

Production is not a later phase. It is a way of writing Tuesday's code.
