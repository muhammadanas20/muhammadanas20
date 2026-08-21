PHASE = {
    "num": "3",
    "title": "FastAPI",
    "tagline": "Models live behind an API: REST, auth, streaming, and WebSockets.",
    "hours": "7-10 days",
    "difficulty": "Medium",
    "exit_ticket": "Authenticated streaming chat endpoint with request IDs and JWT.",
    "objectives": [
        "Design REST endpoints with correct status codes and pydantic models.",
        "Use FastAPI dependency injection for DB, auth, and settings.",
        "Issue and verify JWTs; sketch OAuth2.",
        "Stream tokens with SSE; know when to use WebSockets.",
        "Add request IDs, CORS done right, and background work vs a real queue.",
    ],
    "prerequisites": ["Phases 0–2. Typed Python and a database idea."],
    "topics": ["REST", "FastAPI", "dependencies", "JWT", "OAuth2", "SSE streaming", "WebSockets"],
    "nav": "[Home](../../README.md) · Prev: [Phase 2](../02-sql-databases/) · Next: [Phase 4 · Docker](../04-docker/)",
    "theory": {
        "intro": """A notebook is not a product. A product has a **contract**: HTTP.

FastAPI is a Python framework that:

- Maps URL + method → function
- Validates bodies with pydantic
- Generates OpenAPI docs for free
- Speaks async, so streaming tokens is natural

You will wrap every later RAG and agent in this.""",
        "one_liner": "FastAPI is the front door of a Python AI service.",
        "why": """Mobile apps, web apps, and other services will not import your Python file. They will `POST /v1/chat`.

You need:

- Auth so not everyone spends your API budget
- Streaming so the UI can show tokens as they arrive
- Versioned routes so you can change prompts without breaking old clients
- Errors that are JSON, not a stack trace""",
        "if_missing": "you would demo in Streamlit forever and fail the take-home that says 'expose an API'.",
        "analogy": """A restaurant counter.

- **Route** = menu item (`POST /orders`)
- **pydantic model** = order ticket (invalid ticket never reaches the kitchen)
- **Dependency** = the maître d' who checks reservation (auth) before the kitchen
- **JWT** = a signed wristband: we don't look up your name in a filing cabinet every time, we verify the band
- **Streaming / SSE** = dishes coming out one plate at a time
- **WebSocket** = an open table conversation, not one order
- **Status codes** = 200 here's food, 401 you are not on the list, 429 too many orders, 500 kitchen fire""",
        "visual": """```mermaid
sequenceDiagram
  participant U as Client
  participant A as FastAPI
  participant Auth as JWT dep
  participant M as Model
  U->>A: POST /v1/chat (Bearer token)
  A->>Auth: verify JWT
  Auth-->>A: user_id
  A->>M: stream prompt
  loop tokens
    M-->>A: chunk
    A-->>U: SSE data: chunk
  end
```""",
        "architecture": """```mermaid
flowchart TB
  Client --> Nginx
  Nginx --> FastAPI
  FastAPI --> Deps[Dependencies: auth, db, redis]
  FastAPI --> Chat["POST /v1/chat/stream"]
  Chat --> LLM
  FastAPI --> WS["WS /v1/ws"]
```""",
        "beginner": """**HTTP method:** GET read, POST create/action, PUT replace, PATCH partial, DELETE remove. Chat is usually POST (it has a body and side effects).

**Status codes:** 2xx ok, 4xx your client messed up, 5xx we messed up.

**JSON body** in, JSON out. FastAPI parses into pydantic models.

**Path** `/v1/chats/{id}` vs **query** `?limit=20`.

**Dependency** = a function FastAPI calls before yours. `Depends(get_user)`.

**JWT** = JSON Web Token. Three base64 parts: header, payload, signature. Server signs with a secret. Client sends `Authorization: Bearer <token>`. Server verifies signature and expiry.

**SSE (Server-Sent Events)** = a long GET/POST that sends `data: ...\\n\\n` chunks. Perfect for token streams.

**WebSocket** = bidirectional persistent connection. Use for multi-user presence or when the client also sends often. For one-way token streams, SSE is simpler.""",
        "intermediate": """**OpenAPI** at `/docs` is not a toy. It is the contract. Keep models honest.

**Lifespan** (`lifespan=` in FastAPI) creates the httpx client and DB pool once.

**BackgroundTasks** are for tiny after-the-response work. They are not Celery. If you need retries, use a queue.

**CORS** is a browser rule. `allow_origins=["*"]` plus credentials is illegal and a footgun. List origins.

**Idempotency.** Clients retry POSTs. For "create chat" use client-generated ids or idempotency keys.

**Pagination.** Cursor-based for messages (`after_id`), not huge offsets.

**Error handlers.** Map `ValidationError` to 422, `PermissionError` to 403. Never leak stack traces to clients.""",
        "advanced": """**StreamingResponse** + async generator. Watch client disconnect.

**Backpressure** from slow clients.

**OAuth2** authorization code flow for "Login with Google"; JWT as the session after that. Don't invent your own crypto.

**API versioning.** `/v1` vs header. Pin prompt versions independently of API versions.

**Rate-limit middleware** using Redis from Phase 2.

**WebSocket auth:** tokens in query strings leak to logs. Prefer first-message auth or subprotocols.

**HTTP/2 and proxies** buffering SSE — `X-Accel-Buffering: no` for Nginx.""",
        "production": """Gunicorn/Uvicorn workers, health `/healthz`, readiness `/readyz` (can we see Postgres?), graceful shutdown (finish streams), request ID middleware (`X-Request-ID`), structured logs.

Never: `uvicorn --reload` in production. Never: debug=True. Never: secrets in query params.""",
        "when": "Any time another process must talk to your AI code.",
        "when_not": "A one-off script. A training job. Don't FastAPI your data migration.",
        "code_preview": '''from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.post("/v1/chat/stream")
async def chat(user=Depends(get_user)):
    return StreamingResponse(token_gen(), media_type="text/event-stream")
''',
        "code_notes": "Auth is a dependency, not an if-statement copy-pasted 12 times. StreamingResponse wraps an async generator.",
        "ex_b": "CRUD of notes with pydantic. 404 when missing.",
        "ex_m": "JWT login + protected route. Tests with TestClient.",
        "ex_h": "SSE stream of fake tokens; pytest asserts chunks; JWT required.",
        "project": "Streaming chat API stub — MiniProject.md.",
        "interview_preview": "PUT vs PATCH. Why JWT. SSE vs WebSocket. What 429 means.",
        "flash_sample": "**Q:** Where should the JWT live?\n**A:** Authorization header, not localStorage if you can use httpOnly cookies — know the tradeoff.",
        "mistakes_preview": "Returning 200 for errors. No timeouts. CORS *. Blocking I/O in async routes.",
        "debug_preview": "422 mystery (pydantic). 401 clock skew. SSE that arrives all at once (proxy buffer).",
        "best": "Small routers. Dependencies. Typed models. Request IDs. Healthchecks. Tests.",
        "industry": "FastAPI is the default Python API for AI startups in 2024–2026. Alternatives: Django Ninja, Litestar, Go/Fiber if you leave Python.",
        "perf": "Don't create httpx.Client per request. Stream. Connection pool. Avoid giant JSON logs.",
        "security": "JWT secret in env. Short expiry + refresh. HTTPS. Rate limit. Do not put PII in JWT payload you cannot rotate.",
        "refs": "- [FastAPI](https://fastapi.tiangolo.com/)\n- [JWT.io](https://jwt.io/)\n- [MDN SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)",
        "further": "OAuth 2.1 IETF drafts; Starlette internals.",
    },
    "examples": [
        {
            "title": "JWT-protected ping",
            "why": "Auth is a dependency.",
            "code": '''"""code/auth_ping.py"""
from datetime import datetime, timedelta, timezone
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

SECRET = "dev-only-change-me"
ALG = "HS256"
bearer = HTTPBearer()
app = FastAPI()

def create_token(sub: str) -> str:
    exp = datetime.now(timezone.utc) + timedelta(minutes=30)
    return jwt.encode({"sub": sub, "exp": exp}, SECRET, algorithm=ALG)

def get_user(creds: HTTPAuthorizationCredentials = Depends(bearer)) -> str:
    try:
        data = jwt.decode(creds.credentials, SECRET, algorithms=[ALG])
        return str(data["sub"])
    except JWTError as exc:
        raise HTTPException(401, "invalid token") from exc

@app.get("/v1/me")
def me(user: str = Depends(get_user)) -> dict[str, str]:
    return {"user": user}
''',
            "line_by_line": "HTTPBearer extracts the header. jwt.decode checks signature and exp. HTTPException 401 is the contract.",
            "output": "GET /v1/me without header → 403/401. With valid token → {\"user\": \"ana\"}.",
            "dry_run": "Request → security dep → decode → route.",
            "memory": "Token is a small string. Stateless: no server session store required.",
            "time": "O(1) HMAC verify",
            "space": "O(1)",
            "alternatives": "Session cookies, PASETO, opaque tokens in Redis.",
            "optimization": "Cache JWKS if using RS256/OAuth. HS256 is fine for a single service.",
        },
        {
            "title": "SSE token stream",
            "why": "This is the UX of ChatGPT-like apps.",
            "code": '''"""code/stream.py"""
import asyncio
from collections.abc import AsyncIterator
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

async def fake_tokens(prompt: str) -> AsyncIterator[bytes]:
    for word in f"You said: {prompt}".split():
        yield f"data: {word}\\n\\n".encode()
        await asyncio.sleep(0.05)
    yield b"data: [DONE]\\n\\n"

@app.post("/v1/chat/stream")
async def stream(payload: dict[str, str]) -> StreamingResponse:
    return StreamingResponse(
        fake_tokens(payload.get("prompt", "")),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
''',
            "line_by_line": "Each yield is an SSE event. [DONE] lets the client close. X-Accel-Buffering tells Nginx not to sit on the chunks.",
            "output": "data: You\\n\\ndata: said:\\n\\n ... data: [DONE]",
            "dry_run": "POST → generator starts → yield word → sleep → ... → done. Client parser splits on double newlines.",
            "memory": "O(1) besides the prompt string. We do not build the whole answer.",
            "time": "O(words) with sleeps simulating model latency",
            "space": "O(1) extra",
            "alternatives": "WebSockets; NDJSON; gRPC streaming.",
            "optimization": "Cancel upstream on disconnect. Batch tiny tokens if overhead dominates.",
        },
    ],
    "practice": [
        {"title": "OpenAPI", "body": "Build three routes. Screenshot /docs. Download the OpenAPI JSON.", "done": "A client could be generated from it."},
        {"title": "TestClient", "body": "Write two tests: 401 without token, 200 with.", "done": "pytest -q green."},
        {"title": "Request ID", "body": "Middleware that sets X-Request-ID uuid if missing and logs it.", "done": "You can grep logs by id."},
    ],
    "exercises": {
        "beginner": [
            {"title": "Notes API", "body": "CRUD notes in memory with pydantic. 404/422 correct.", "constraints": "No DB yet."},
            {"title": "Status codes", "body": "A cheat-route table: map 8 situations to codes.", "constraints": "Include 409 and 429."},
        ],
        "medium": [
            {"title": "JWT login", "body": "POST /login returns token. /me needs it.", "constraints": "Tests included. Secret from env."},
            {"title": "Pagination", "body": "GET /messages?cursor=&limit=", "constraints": "No offset pagination."},
        ],
        "hard": [
            {"title": "Disconnect", "body": "Prove that closing the client stops fake_tokens (use a flag).", "constraints": "Automated test."},
        ],
    },
    "assignments": [
        {
            "title": "Chat API stub",
            "time": "5–8 hours",
            "brief": "JWT, POST /v1/chat/stream SSE, Redis rate limit from Phase 2 (mock Redis ok), request IDs, TestClient tests.",
            "deliverables": ["app package", "tests", "openapi.json snapshot", "README"],
            "rubric": ["auth required", "stream works", "429 path", "no secrets in repo"],
        }
    ],
    "quiz": [
        {"q": "Chat creation is usually:", "choices": {"A": "GET", "B": "POST", "C": "DELETE", "D": "HEAD"}, "answer": "B", "explain": "Has body and side effects."},
        {"q": "401 means:", "choices": {"A": "Not found", "B": "Unauthenticated", "C": "Rate limited", "D": "OK"}, "answer": "B", "explain": "Who are you?"},
        {"q": "403 means:", "choices": {"A": "Authenticated but not allowed", "B": "Server crash", "C": "Redirect", "D": "Created"}, "answer": "A", "explain": "Identity known, permission denied."},
        {"q": "JWT signature proves:", "choices": {"A": "The payload was not altered and signed by someone with the secret", "B": "The user is nice", "C": "HTTPS", "D": "The DB is up"}, "answer": "A", "explain": "Integrity + authenticity of token."},
        {"q": "SSE is typically:", "choices": {"A": "Client to server only", "B": "Server to client stream", "C": "UDP", "D": "A database"}, "answer": "B", "explain": "One way stream."},
        {"q": "WebSockets are better when:", "choices": {"A": "You only send tokens down", "B": "You need frequent bidirectional messages", "C": "You hate HTTP", "D": "Always"}, "answer": "B", "explain": "Bidirectional."},
        {"q": "Depends() is:", "choices": {"A": "A type of JWT", "B": "FastAPI dependency injection", "C": "Redis", "D": "A status code"}, "answer": "B", "explain": "DI."},
        {"q": "debug=True in production:", "choices": {"A": "Is recommended", "B": "Leaks traces and is unsafe", "C": "Speeds Python", "D": "Is required for SSE"}, "answer": "B", "explain": "Never."},
        {"q": "BackgroundTasks are for:", "choices": {"A": "Multi-hour video jobs", "B": "Tiny after-response work", "C": "Training GPTs", "D": "DNS"}, "answer": "B", "explain": "Else a queue."},
        {"q": "CORS * with credentials:", "choices": {"A": "Best practice", "B": "Invalid / dangerous pattern", "C": "Required for JWT", "D": "A Postgres setting"}, "answer": "B", "explain": "List origins."},
    ],
    "flashcards": [
        {"q": "Name 2xx, 4xx, 5xx.", "a": "Success, client error, server error."},
        {"q": "What is OpenAPI here?", "a": "The auto-generated contract of your API."},
        {"q": "Bearer token lives in?", "a": "Authorization header."},
        {"q": "Why request IDs?", "a": "Tie logs, traces, and user reports together."},
        {"q": "Health vs ready?", "a": "Health: process up. Ready: dependencies reachable."},
        {"q": "SSE content type?", "a": "text/event-stream."},
        {"q": "Why not uvicorn --reload in prod?", "a": "Extra process, file watchers, not a process manager."},
        {"q": "422 in FastAPI?", "a": "Validation error from pydantic."},
        {"q": "Idempotency key?", "a": "Client token so retries do not double-create."},
        {"q": "Where to put JWT secret?", "a": "Environment / secret manager, never source."},
    ],
    "interview": [
        {
            "q": "SSE vs WebSocket for an LLM chat UI?",
            "junior": "SSE for one-way token streams: simpler, HTTP-friendly. WebSocket if both sides chatter or you need presence.",
            "mistakes": "Always WebSockets because they sound advanced.",
            "senior": "Proxy buffering, HTTP/2, mobile networks, reconnect, auth, and using WS anyway because the product already has one.",
        },
        {
            "q": "How does JWT auth work?",
            "junior": "Login issues signed token with exp and sub. Client sends it. Server verifies signature and exp. No DB hit required for the verify.",
            "mistakes": "Storing passwords in the JWT. No expiry. Using HS256 secret 'secret'.",
            "senior": "Revocation lists, rotation, RS256/JWKS, cookie vs header XSS/CSRF tradeoff, audience/issuer claims.",
        },
        {
            "q": "How do you structure a large FastAPI app?",
            "junior": "Routers per area, deps for db/auth, settings via pydantic, lifespan for pools.",
            "mistakes": "One 2,000-line main.py.",
            "senior": "Domain packages, hexagonal-ish boundaries around the model provider, feature flags.",
        },
        {
            "q": "A client retries POST /chat and duplicates messages. Fix?",
            "junior": "Idempotency key stored in Redis for 24h mapping to message id.",
            "mistakes": "Tell them not to retry.",
            "senior": "Exactly-once is a lie; at-least-once + de-dupe. Idempotency keys, unique constraints.",
        },
        {
            "q": "What do you log on each request?",
            "junior": "Request id, user id, route, status, latency. Not raw prompts if PII.",
            "mistakes": "print(request.body).",
            "senior": "Sampling, redaction, OpenTelemetry context, cost fields.",
        },
    ],
    "whiteboard": [
        "Sequence diagram of JWT login + streaming chat.",
        "Design /healthz vs /readyz for API+Postgres+Redis.",
        "Where rate limiting lives: gateway vs app vs Redis.",
    ],
    "interview_listen": "HTTP literacy plus streaming and auth, not decorator trivia",
    "cheatsheet": {
        "remember": "POST chat. JWT in header. SSE for tokens. Depends for auth. No debug in prod.",
        "bash": "uvicorn app.main:app --reload --port 8000\nhttp :8000/docs",
        "python": "return StreamingResponse(gen(), media_type='text/event-stream')",
        "decisions": "One-way stream → SSE. Bidirectional → WS. Heavy job → queue not BackgroundTasks.",
        "numbers": "JWT access 15–30 min. Workers ≈ cores. Body limits: set them.",
        "do_not": "Secrets in query. CORS *. 200 on errors. Blocking I/O in async.",
    },
    "miniproject": {
        "name": "stream-chat-api",
        "time": "1–2 days",
        "difficulty": "Medium",
        "why": "This stub becomes the shell of every later project.",
        "story": "I can log in, hit /v1/chat/stream, see tokens, and get 401 without a token.",
        "must": ["JWT", "SSE", "request id", "tests", "OpenAPI"],
        "should": ["Redis 429", "healthz"],
        "wont": ["Real model yet (fake tokens ok)", "UI"],
        "architecture": "```mermaid\nflowchart LR\nClient --> FastAPI --> JWT\nFastAPI --> Stream\n```",
        "layout": "app/main.py app/auth.py app/stream.py tests/",
        "rubric": ["pytest green", "401/200/stream", "README with curl"],
        "stretch": "Cookie session instead of JWT; write the CSRF note.",
    },
    "resources": {
        "official": ["[FastAPI](https://fastapi.tiangolo.com/)", "[Starlette](https://www.starlette.io/)", "[RFC 7519 JWT](https://datatracker.ietf.org/doc/html/rfc7519)"],
        "extra": ["TestDriven.io FastAPI series", "Nginx buffering + SSE posts"],
        "papers": ["n/a"],
    },
    "faq": [
        {"q": "Flask instead?", "a": "Fine if you already know it. This course uses FastAPI because typing + async + OpenAPI match AI services."},
        {"q": "Do I need HTTPS locally?", "a": "No. In production, yes, usually via a proxy."},
        {"q": "python-jose vs PyJWT?", "a": "Either. Be consistent. Know the algorithms you allow."},
    ],
    "debugging": [
        {
            "title": "422 Unprocessable Entity",
            "symptom": "Request 'looks fine' in the UI.",
            "wrong": "JSON types: sending string where int expected; missing field.",
            "see": "The 422 body lists loc/msg.",
            "fix": "Match the pydantic model. Print the OpenAPI schema.",
            "prevent": "Share the OpenAPI with frontend. Generate a client.",
        },
        {
            "title": "SSE arrives in one blob",
            "symptom": "UI waits then dumps the answer.",
            "wrong": "Proxy or gzip buffering.",
            "see": "curl -N, check Nginx, disable gzip on that location.",
            "fix": "X-Accel-Buffering: no; chunked transfer.",
            "prevent": "Load test through the real proxy early.",
        },
    ],
    "mistakes": [
        {"title": "Business logic in the route", "body": "Cannot test without TestClient. Cannot reuse from a worker.", "instead": "Service functions. Routes are glue."},
        {"title": "Global mutable dict as DB", "body": "Fails with multiple workers.", "instead": "Postgres. Even SQLite is better for a while."},
        {"title": "Catch-all except and return 200", "body": "Clients think success.", "instead": "HTTPException with the right code."},
    ],
    "prod_tips": {
        "cost": "Auth + rate limits are cost controls. Unauthenticated model endpoints are a credit card on the sidewalk.",
        "latency": "TTFT (time to first token) is the UX metric. Stream immediately, even a keepalive SSE comment.",
        "reliability": "Graceful shutdown: stop taking new, finish streams, then kill.",
        "observability": "Request ID in response header and logs. Later: traces.",
        "scaling": "Stateless app + Redis + PG. Horizontal scale Uvicorn workers behind a load balancer.",
        "checklist": ["auth", "rate limit", "healthz", "no debug", "timeouts", "tests"],
    },
    "challenge": {
        "title": "OAuth2 login",
        "body": "Add 'Login with GitHub' (or a fake OIDC) and issue your JWT after callback.",
        "constraints": ["No secret in frontend", "State param against CSRF"],
        "success": "A user can log in without you storing their GitHub password (you never should).",
    },
    "solutions": [
        {"id": "M1 JWT", "hint": "python-jose, HTTPBearer, exp claim.", "approach": "Login checks password hash (passlib) then encode."},
        {"id": "H1 disconnect", "hint": "request.is_disconnected in the generator loop.", "approach": "Break and cancel upstream."},
    ],
    "code_files": {
        "stream.py": '''"""Server-sent events stream of fake tokens."""
from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def fake_tokens(prompt: str) -> AsyncIterator[bytes]:
    for word in f"You said: {prompt}".split():
        yield f"data: {word}\\n\\n".encode()
        await asyncio.sleep(0.05)
    yield b"data: [DONE]\\n\\n"


@app.post("/v1/chat/stream")
async def stream(payload: dict[str, str]) -> StreamingResponse:
    return StreamingResponse(
        fake_tokens(payload.get("prompt", "")),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
''',
    },
}
