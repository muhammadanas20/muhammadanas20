# Interview — Phase 3: FastAPI

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. SSE vs WebSocket for an LLM chat UI?

**Expected answer (junior)**

SSE for one-way token streams: simpler, HTTP-friendly. WebSocket if both sides chatter or you need presence.

**Common mistakes**

Always WebSockets because they sound advanced.

**Senior-level discussion**

Proxy buffering, HTTP/2, mobile networks, reconnect, auth, and using WS anyway because the product already has one.
### Q2. How does JWT auth work?

**Expected answer (junior)**

Login issues signed token with exp and sub. Client sends it. Server verifies signature and exp. No DB hit required for the verify.

**Common mistakes**

Storing passwords in the JWT. No expiry. Using HS256 secret 'secret'.

**Senior-level discussion**

Revocation lists, rotation, RS256/JWKS, cookie vs header XSS/CSRF tradeoff, audience/issuer claims.
### Q3. How do you structure a large FastAPI app?

**Expected answer (junior)**

Routers per area, deps for db/auth, settings via pydantic, lifespan for pools.

**Common mistakes**

One 2,000-line main.py.

**Senior-level discussion**

Domain packages, hexagonal-ish boundaries around the model provider, feature flags.
### Q4. A client retries POST /chat and duplicates messages. Fix?

**Expected answer (junior)**

Idempotency key stored in Redis for 24h mapping to message id.

**Common mistakes**

Tell them not to retry.

**Senior-level discussion**

Exactly-once is a lie; at-least-once + de-dupe. Idempotency keys, unique constraints.
### Q5. What do you log on each request?

**Expected answer (junior)**

Request id, user id, route, status, latency. Not raw prompts if PII.

**Common mistakes**

print(request.body).

**Senior-level discussion**

Sampling, redaction, OpenTelemetry context, cost fields.


---

## Whiteboard prompts

- Sequence diagram of JWT login + streaming chat.
- Design /healthz vs /readyz for API+Postgres+Redis.
- Where rate limiting lives: gateway vs app vs Redis.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for HTTP literacy plus streaming and auth, not decorator trivia.
