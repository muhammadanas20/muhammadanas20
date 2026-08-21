# Practice — Phase 4: Docker

Guided drills. Timer on. No tutorial hopping.



### Drill 1. Build and run

Build the example image. Exec into it. cat /etc/os-release. Observe you are in Debian-slim, not your Mac.

**Done when:** You felt the isolation.

### Drill 2. Break the cache on purpose

Change a line of Python vs requirements.txt. See which rebuilds.

**Done when:** You can predict cache hits.

### Drill 3. down -v

Write data to PG, compose down, up, data still there. Then down -v, data gone.

**Done when:** You respect volumes.

## Cool-down

Explain today's idea to a rubber duck in 90 seconds using the analogy from Theory.md. If you need the file open, you are not done.
