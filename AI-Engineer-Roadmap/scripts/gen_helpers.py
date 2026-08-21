"""Helpers to assemble a complete PHASE dict from compact specs."""

from __future__ import annotations

from typing import Any


def quiz_tf(items: list[tuple[str, str, str]]) -> list[dict[str, Any]]:
    """items: (question, A/B/C/D answer letter, explain) with 4 choices provided as q dicts already."""
    return items  # passthrough if already structured


def q(q: str, choices: dict[str, str], answer: str, explain: str) -> dict[str, Any]:
    return {"q": q, "choices": choices, "answer": answer, "explain": explain}


def card(q: str, a: str) -> dict[str, str]:
    return {"q": q, "a": a}


def iq(q: str, junior: str, mistakes: str, senior: str) -> dict[str, str]:
    return {"q": q, "junior": junior, "mistakes": mistakes, "senior": senior}


def ex(title: str, body: str, constraints: str) -> dict[str, str]:
    return {"title": title, "body": body, "constraints": constraints}


def example(
    title: str,
    why: str,
    code: str,
    line_by_line: str,
    output: str,
    dry_run: str,
    memory: str,
    time: str,
    space: str,
    alternatives: str,
    optimization: str,
) -> dict[str, str]:
    return {
        "title": title,
        "why": why,
        "code": code,
        "line_by_line": line_by_line,
        "output": output,
        "dry_run": dry_run,
        "memory": memory,
        "time": time,
        "space": space,
        "alternatives": alternatives,
        "optimization": optimization,
    }


def make_phase(**kwargs: Any) -> dict[str, Any]:
    required = [
        "num",
        "title",
        "tagline",
        "hours",
        "difficulty",
        "exit_ticket",
        "objectives",
        "prerequisites",
        "topics",
        "nav",
        "theory",
        "examples",
        "practice",
        "exercises",
        "assignments",
        "quiz",
        "flashcards",
        "interview",
        "whiteboard",
        "interview_listen",
        "cheatsheet",
        "miniproject",
        "resources",
        "faq",
        "debugging",
        "mistakes",
        "prod_tips",
        "challenge",
        "solutions",
    ]
    missing = [k for k in required if k not in kwargs]
    if missing:
        raise ValueError(f"Phase {kwargs.get('num')} missing {missing}")
    kwargs.setdefault("code_files", {})
    kwargs.setdefault("examples_intro", "")
    return kwargs
