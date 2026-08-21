# Quiz — Phase 3: FastAPI

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. Chat creation is usually:
    A) GET
    B) POST
    C) DELETE
    D) HEAD
2. 401 means:
    A) Not found
    B) Unauthenticated
    C) Rate limited
    D) OK
3. 403 means:
    A) Authenticated but not allowed
    B) Server crash
    C) Redirect
    D) Created
4. JWT signature proves:
    A) The payload was not altered and signed by someone with the secret
    B) The user is nice
    C) HTTPS
    D) The DB is up
5. SSE is typically:
    A) Client to server only
    B) Server to client stream
    C) UDP
    D) A database
6. WebSockets are better when:
    A) You only send tokens down
    B) You need frequent bidirectional messages
    C) You hate HTTP
    D) Always
7. Depends() is:
    A) A type of JWT
    B) FastAPI dependency injection
    C) Redis
    D) A status code
8. debug=True in production:
    A) Is recommended
    B) Leaks traces and is unsafe
    C) Speeds Python
    D) Is required for SSE
9. BackgroundTasks are for:
    A) Multi-hour video jobs
    B) Tiny after-response work
    C) Training GPTs
    D) DNS
10. CORS * with credentials:
    A) Best practice
    B) Invalid / dangerous pattern
    C) Required for JWT
    D) A Postgres setting

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — Has body and side effects.
2. **B** — Who are you?
3. **A** — Identity known, permission denied.
4. **A** — Integrity + authenticity of token.
5. **B** — One way stream.
6. **B** — Bidirectional.
7. **B** — DI.
8. **B** — Never.
9. **B** — Else a queue.
10. **B** — List origins.

</details>
