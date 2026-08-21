"""curl-like SSE reader for /v1/chat/stream."""
from __future__ import annotations

import sys
import urllib.request


def main(url: str) -> None:
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req, timeout=30) as resp:
        for raw in resp:
            line = raw.decode()
            if line.startswith("data:"):
                print(line[5:].strip(), flush=True)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000/v1/chat/stream")
