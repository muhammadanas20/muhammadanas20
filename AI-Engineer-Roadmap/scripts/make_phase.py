"""Factory for remaining phases — unique content, shared skeleton."""
from __future__ import annotations

from typing import Any


def T(**kwargs: Any) -> dict[str, Any]:
    return kwargs


def phase(
    num: str,
    title: str,
    tagline: str,
    hours: str,
    difficulty: str,
    exit_ticket: str,
    objectives: list[str],
    prerequisites: list[str],
    topics: list[str],
    nav: str,
    theory: dict[str, str],
    examples: list[dict[str, str]],
    practice: list[dict[str, str]],
    exercises: dict[str, list[dict[str, str]]],
    assignments: list[dict[str, Any]],
    quiz: list[dict[str, Any]],
    flashcards: list[dict[str, str]],
    interview: list[dict[str, str]],
    whiteboard: list[str],
    interview_listen: str,
    cheatsheet: dict[str, str],
    miniproject: dict[str, Any],
    resources: dict[str, list[str]],
    faq: list[dict[str, str]],
    debugging: list[dict[str, str]],
    mistakes: list[dict[str, str]],
    prod_tips: dict[str, Any],
    challenge: dict[str, Any],
    solutions: list[dict[str, str]],
    code_files: dict[str, str] | None = None,
    examples_intro: str = "",
) -> dict[str, Any]:
    return {
        "num": num,
        "title": title,
        "tagline": tagline,
        "hours": hours,
        "difficulty": difficulty,
        "exit_ticket": exit_ticket,
        "objectives": objectives,
        "prerequisites": prerequisites,
        "topics": topics,
        "nav": nav,
        "theory": theory,
        "examples": examples,
        "practice": practice,
        "exercises": exercises,
        "assignments": assignments,
        "quiz": quiz,
        "flashcards": flashcards,
        "interview": interview,
        "whiteboard": whiteboard,
        "interview_listen": interview_listen,
        "cheatsheet": cheatsheet,
        "miniproject": miniproject,
        "resources": resources,
        "faq": faq,
        "debugging": debugging,
        "mistakes": mistakes,
        "prod_tips": prod_tips,
        "challenge": challenge,
        "solutions": solutions,
        "code_files": code_files or {},
        "examples_intro": examples_intro,
    }


def Q(q: str, a: str, b: str, c: str, d: str, ans: str, why: str) -> dict[str, Any]:
    return {"q": q, "choices": {"A": a, "B": b, "C": c, "D": d}, "answer": ans, "explain": why}


def C(q: str, a: str) -> dict[str, str]:
    return {"q": q, "a": a}


def I(q: str, junior: str, mistakes: str, senior: str) -> dict[str, str]:
    return {"q": q, "junior": junior, "mistakes": mistakes, "senior": senior}


def E(title: str, body: str, constraints: str) -> dict[str, str]:
    return {"title": title, "body": body, "constraints": constraints}


def EX(
    title: str,
    why: str,
    code: str,
    line_by_line: str,
    output: str,
    dry_run: str,
    memory: str = "O(n) in input size.",
    time: str = "See notes.",
    space: str = "See notes.",
    alternatives: str = "See theory.",
    optimization: str = "Measure first.",
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


def drill(title: str, body: str, done: str) -> dict[str, str]:
    return {"title": title, "body": body, "done": done}


def asg(title: str, time: str, brief: str, deliverables: list[str], rubric: list[str]) -> dict[str, Any]:
    return {"title": title, "time": time, "brief": brief, "deliverables": deliverables, "rubric": rubric}


def mp(**kwargs: Any) -> dict[str, Any]:
    return kwargs


def th(
    intro: str,
    one_liner: str,
    why: str,
    if_missing: str,
    analogy: str,
    visual: str,
    architecture: str,
    beginner: str,
    intermediate: str,
    advanced: str,
    production: str,
    when: str,
    when_not: str,
    code_preview: str,
    code_notes: str,
    ex_b: str,
    ex_m: str,
    ex_h: str,
    project: str,
    interview_preview: str,
    flash_sample: str,
    mistakes_preview: str,
    debug_preview: str,
    best: str,
    industry: str,
    perf: str,
    security: str,
    refs: str,
    further: str,
) -> dict[str, str]:
    return locals()
