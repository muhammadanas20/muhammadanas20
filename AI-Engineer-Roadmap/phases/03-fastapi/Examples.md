# Examples — Phase 3: FastAPI

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. JWT-protected ping

Auth is a dependency.

```python
"""code/auth_ping.py"""
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

```

**What every interesting line is doing**

HTTPBearer extracts the header. jwt.decode checks signature and exp. HTTPException 401 is the contract.

**Expected output**

```text
GET /v1/me without header → 403/401. With valid token → {"user": "ana"}.
```

**Dry run**

Request → security dep → decode → route.

**Memory**

Token is a small string. Stateless: no server session store required.

**Time complexity:** O(1) HMAC verify  
**Space complexity:** O(1)

**Alternatives**

Session cookies, PASETO, opaque tokens in Redis.

**Optimization**

Cache JWKS if using RS256/OAuth. HS256 is fine for a single service.

---

### Example 2. SSE token stream

This is the UX of ChatGPT-like apps.

```python
"""code/stream.py"""
import asyncio
from collections.abc import AsyncIterator
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

async def fake_tokens(prompt: str) -> AsyncIterator[bytes]:
    for word in f"You said: {prompt}".split():
        yield f"data: {word}\n\n".encode()
        await asyncio.sleep(0.05)
    yield b"data: [DONE]\n\n"

@app.post("/v1/chat/stream")
async def stream(payload: dict[str, str]) -> StreamingResponse:
    return StreamingResponse(
        fake_tokens(payload.get("prompt", "")),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )

```

**What every interesting line is doing**

Each yield is an SSE event. [DONE] lets the client close. X-Accel-Buffering tells Nginx not to sit on the chunks.

**Expected output**

```text
data: You\n\ndata: said:\n\n ... data: [DONE]
```

**Dry run**

POST → generator starts → yield word → sleep → ... → done. Client parser splits on double newlines.

**Memory**

O(1) besides the prompt string. We do not build the whole answer.

**Time complexity:** O(words) with sleeps simulating model latency  
**Space complexity:** O(1) extra

**Alternatives**

WebSockets; NDJSON; gRPC streaming.

**Optimization**

Cancel upstream on disconnect. Batch tiny tokens if overhead dominates.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
