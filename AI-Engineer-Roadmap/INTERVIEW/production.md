# Production interview extras

**Q. SLOs for a chat API?**  
TTFT p95, error rate, cost/1k, eval faithfulness, fallback rate.

**Q. How do you pin quality when the vendor updates the model?**  
Pin snapshots if offered, shadow eval nightly, alert on score drop.

**Q. Semantic cache cross-tenant?**  
A breach. Key = tenant + versions + query.

**Q. 429s from OpenAI.**  
Backoff + jitter, queue, fallback, budget, cache.

**Q. Logs vs traces vs metrics?**  
Logs = events. Metrics = aggregates. Traces = one request's tree. You want all three at different resolutions.
