# Challenge — Phase 1: Python refresh

This is optional. It is also how you get interesting interview stories.

## 100 concurrent fake streams

Simulate 100 clients consuming an async token generator. Prove memory stays flat vs the list-building version.

**Constraints**

- Measure RSS
- No external model

**Success looks like**

A table: N clients × pattern × peak RAM.
