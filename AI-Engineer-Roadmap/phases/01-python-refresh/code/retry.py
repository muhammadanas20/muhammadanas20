"""Exponential backoff with jitter. Production primitive."""
from __future__ import annotations

import random
import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def retry(times: int = 3, base: float = 0.2) -> Callable[[Callable[..., T]], Callable[..., T]]:
    def deco(fn: Callable[..., T]) -> Callable[..., T]:
        def wrapped(*args: object, **kwargs: object) -> T:
            last: Exception | None = None
            for attempt in range(times):
                try:
                    return fn(*args, **kwargs)
                except Exception as exc:
                    last = exc
                    time.sleep(base * (2**attempt) + random.random() * 0.05)
            assert last is not None
            raise last

        return wrapped

    return deco
