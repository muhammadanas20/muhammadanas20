"""Fixed-window rate limiter using Redis INCR."""
from __future__ import annotations

import time

import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


def allow(user_id: str, limit: int = 20, window_s: int = 60) -> bool:
    key = f"rl:{user_id}:{int(time.time() // window_s)}"
    n = r.incr(key)
    if n == 1:
        r.expire(key, window_s)
    return n <= limit
