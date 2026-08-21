"""Approximate vs real token counts. Run: python token_count.py"""
from __future__ import annotations


def approx_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def main() -> None:
    samples = [
        "hello world",
        "def cosine(a, b): return a @ b",
        "😊" * 10,
    ]
    for s in samples:
        print(f"{approx_tokens(s):4d} ~tok | {s!r}")
    print("Install tiktoken and compare with encoding.encode for your model.")


if __name__ == "__main__":
    main()
