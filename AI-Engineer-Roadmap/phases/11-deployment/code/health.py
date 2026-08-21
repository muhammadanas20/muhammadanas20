"""Health and readiness endpoints."""
from fastapi import FastAPI, Response

app = FastAPI()
ready = True


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/readyz")
def readyz() -> Response:
    if not ready:
        return Response(status_code=503)
    return Response(status_code=200)
