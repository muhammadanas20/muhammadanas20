"""Defense-in-depth SQL guard. Still use a read-only DB role."""
from __future__ import annotations

FORBIDDEN = ("drop", "delete", "update", "insert", "alter", "truncate", "grant")


def guard_sql(sql: str, limit: int = 50) -> str:
    s = sql.strip().rstrip(";")
    low = s.lower()
    if not low.startswith("select"):
        raise ValueError("only SELECT")
    if any(w in low.split() for w in FORBIDDEN):
        raise ValueError("forbidden keyword")
    if " limit " not in f" {low} ":
        s = f"{s} LIMIT {limit}"
    return s
