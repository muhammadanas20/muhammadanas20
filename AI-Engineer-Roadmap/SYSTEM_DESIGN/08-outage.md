# Design: vendor outage

Timeouts, retries on 429/5xx, fallback model, degrade to retrieval snippets without generation, status page, queue.

Don't block the thread. Don't retry 400s.

Run a game day: flip a fake flag `PRIMARY_DOWN=1`.
