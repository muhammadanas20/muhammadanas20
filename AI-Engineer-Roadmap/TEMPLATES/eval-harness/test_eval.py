"""Fail CI when quality drops. Replace `run` with your pipeline."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

CASES = Path(__file__).with_name("cases.jsonl")


def run(question: str) -> str:
    return "I don't know."


@pytest.mark.parametrize(
    "case",
    [json.loads(line) for line in CASES.read_text().splitlines() if line.strip()],
)
def test_case(case: dict) -> None:
    out = run(case["question"]).lower()
    if case.get("must_abstain"):
        assert "don't know" in out or "do not know" in out
        return
    for needle in case.get("must_include", []):
        assert needle.lower() in out
