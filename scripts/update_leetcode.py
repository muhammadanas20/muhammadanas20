#!/usr/bin/env python3
"""Fetch Muhammad Anas' public LeetCode data and render lightweight local SVGs.

The checked-in JSON is also a fallback: if LeetCode is temporarily unavailable, the
last good cards remain usable and the profile never depends on a third-party image
server at page-view time.

Network strategy: the GraphQL endpoint is tried first (with retries and rotating
user agents). If it keeps failing, the public profile page is scraped instead,
because LeetCode sometimes blocks data-center IPs on /graphql/ while the HTML page
still loads. If both paths fail, the script exits non-zero so the workflow run is
visibly red instead of quietly keeping stale cards and reporting success.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "profile" / "leetcode-data.json"
USERNAME = "muhammadanas20"
ENDPOINT = "https://leetcode.com/graphql/"
PROFILE_PAGE = f"https://leetcode.com/u/{USERNAME}/"

# LeetCode's edge is inconsistent about which clients it lets through, so rotate a
# few user agents on every retry attempt.
USER_AGENTS = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "github-profile-stats/1.0",
)
# Keep retries short. LeetCode mostly either answers quickly or rejects the
# runner with a fast 403; long backoffs only turn a fast rejection into a
# minutes-long stalled job for no benefit.
RETRIES = 2
RETRY_DELAY_SECONDS = 3
REQUEST_TIMEOUT_SECONDS = 20

PROFILE_QUERY = """
query profile($username: String!) {
  allQuestionsCount { difficulty count }
  matchedUser(username: $username) {
    profile { ranking postViewCount reputation solutionCount categoryDiscussCount }
    submitStatsGlobal {
      acSubmissionNum { difficulty count submissions }
      totalSubmissionNum { difficulty count submissions }
    }
    problemsSolvedBeatsStats { difficulty percentage }
    languageProblemCount { languageName problemsSolved }
    badges { displayName creationDate }
  }
}
"""
SKILLS_QUERY = """
query skills($username: String!) {
  matchedUser(username: $username) {
    tagProblemCounts {
      advanced { tagName problemsSolved }
      intermediate { tagName problemsSolved }
      fundamental { tagName problemsSolved }
    }
    userCalendar { streak totalActiveDays submissionCalendar }
  }
}
"""
RECENT_QUERY = """
query recent($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    title titleSlug timestamp
  }
}
"""


def _request(url: str, data: bytes | None, user_agent: str) -> bytes:
    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
            "Referer": PROFILE_PAGE,
            "User-Agent": user_agent,
        },
    )
    with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
        return response.read()


def _is_transient(error: BaseException) -> bool:
    """Return True only for errors worth retrying.

    LeetCode rejecting a data-center IP comes back as HTTP 403 (or a TLS EOF
    reset). Those are NOT transient — we stop immediately instead of sleeping
    for minutes and then failing anyway.
    """
    if isinstance(error, urllib.error.HTTPError):
        # 429 too many requests could clear, but we hit it rarely via this job.
        return error.code in (429, 502, 503, 504)
    # A genuine timeout is worth retrying. TLS resets, connection resets and
    # refusals are IP-level blocks that retrying will never get past.
    reason = getattr(error, "reason", None)
    return isinstance(error, TimeoutError) or isinstance(reason, TimeoutError)


def _request_with_retries(url: str, data: bytes | None = None) -> bytes:
    """Try every user agent, with backoff, so transient/UA-based blocks recover.

    Fails fast on definitive rejections (e.g. HTTP 403 from LeetCode), so a
    blocked job doesn't stall for minutes before the workflow gives up.
    """
    attempts = USER_AGENTS * RETRIES
    last_error: Exception | None = None
    for attempt, user_agent in enumerate(attempts):
        try:
            return _request(url, data, user_agent)
        except Exception as error:  # URLError, HTTPError, TLS resets, timeouts...
            last_error = error
            if _is_transient(error) and attempt + 1 < len(attempts):
                time.sleep(RETRY_DELAY_SECONDS)
    raise RuntimeError(f"LeetCode unreachable after {len(attempts)} attempts: {last_error}")


def graphql(query: str, variables: dict) -> dict:
    body = json.dumps({"query": query, "variables": variables}).encode()
    result = json.loads(_request_with_retries(ENDPOINT, body))
    if result.get("errors"):
        raise RuntimeError(result["errors"][0].get("message", "LeetCode GraphQL error"))
    return result["data"]


def keyed(items: list[dict], value: str = "count") -> dict:
    return {item["difficulty"]: item.get(value, 0) for item in items}


def _build_from_graphql(profile_data: dict, skills_data: dict, recent_data: dict, current: dict) -> dict:
    user = profile_data.get("matchedUser")
    stats = (user or {}).get("submitStatsGlobal")
    if not user or not stats:
        raise RuntimeError("GraphQL response is missing matchedUser/submitStatsGlobal")
    accepted = keyed(stats.get("acSubmissionNum") or [], "submissions")
    submitted = keyed(stats.get("totalSubmissionNum") or [], "submissions")
    calendar = ((skills_data.get("matchedUser") or {}).get("userCalendar")) or {}
    submissions_by_day = json.loads(calendar.get("submissionCalendar") or "{}")
    badges = user.get("badges") or []
    newest_badge = max(badges, key=lambda badge: int(badge.get("creationDate") or 0), default={})

    return {
        "username": USERNAME,
        "ranking": (user.get("profile") or {}).get("ranking", current.get("ranking", 0)),
        "solved": keyed(stats.get("acSubmissionNum") or []),
        "questions": keyed(profile_data.get("allQuestionsCount") or []),
        "beats": keyed(user.get("problemsSolvedBeatsStats") or [], "percentage"),
        "acceptance": round(100 * accepted.get("All", 0) / max(submitted.get("All", 1), 1), 2),
        "submissionsYear": sum(int(value) for value in submissions_by_day.values()),
        "activeDays": calendar.get("totalActiveDays", 0),
        "maxStreak": calendar.get("streak", 0),
        "community": {
            "views": (user.get("profile") or {}).get("postViewCount", 0),
            "solutions": (user.get("profile") or {}).get("solutionCount", 0),
            "discuss": (user.get("profile") or {}).get("categoryDiscussCount", 0),
            "reputation": (user.get("profile") or {}).get("reputation", 0),
        },
        "languages": [
            {"name": item["languageName"], "solved": item["problemsSolved"]}
            for item in user.get("languageProblemCount") or []
        ],
        "skills": {
            level.title(): [
                {"name": item["tagName"], "solved": item["problemsSolved"]}
                for item in ((skills_data.get("matchedUser") or {}).get("tagProblemCounts") or {}).get(level, [])
            ]
            for level in ("advanced", "intermediate", "fundamental")
        },
        "badge": newest_badge.get("displayName") or current.get("badge", "Keep solving"),
        "recent": [
            {"title": item["title"], "slug": item["titleSlug"]}
            for item in recent_data.get("recentAcSubmissionList") or []
        ],
    }


def fetch(current: dict) -> dict:
    try:
        profile_data = graphql(PROFILE_QUERY, {"username": USERNAME})
        skills_data = graphql(SKILLS_QUERY, {"username": USERNAME})
        recent_data = graphql(RECENT_QUERY, {"username": USERNAME, "limit": 8})
        return _build_from_graphql(profile_data, skills_data, recent_data, current)
    except Exception as error:
        print(f"GraphQL fetch failed ({error}); falling back to the public profile page", file=sys.stderr)
        return parse_profile_page(current)


def _collect(node: object, wanted: set[str], found: dict[str, list]) -> None:
    """Collect every occurrence of the wanted key names from a nested JSON payload."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in wanted:
                found.setdefault(key, []).append(value)
            _collect(value, wanted, found)
    elif isinstance(node, list):
        for item in node:
            _collect(item, wanted, found)


def _pick(candidates: list, predicate):
    for candidate in candidates:
        try:
            if predicate(candidate):
                return candidate
        except TypeError:
            continue
    return None


def parse_profile_page(current: dict) -> dict:
    """Assemble the stats dict from the public profile page payload.

    LeetCode renders the profile server-side with a `__NEXT_DATA__` JSON blob that
    carries the same fields as the GraphQL endpoint. We scan for the well-known key
    names (which survive minor payload reshuffles) and fall back to the last good
    values for anything the payload does not expose.
    """
    raw = _request_with_retries(PROFILE_PAGE)
    match = re.search(
        r'<script[^>]*id="__NEXT_DATA__"[^>]*>(.*?)</script>',
        raw.decode("utf-8", "replace"),
        re.DOTALL,
    )
    if not match:
        raise RuntimeError("profile page has no __NEXT_DATA__ payload (page blocked or layout changed)")
    payload = json.loads(match.group(1))
    wanted = {
        "profile",
        "allQuestionsCount",
        "submitStatsGlobal",
        "problemsSolvedBeatsStats",
        "languageProblemCount",
        "tagProblemCounts",
        "userCalendar",
        "recentAcSubmissionList",
        "badges",
    }
    found: dict[str, list] = {}
    _collect(payload, wanted, found)

    stats = _pick(found.get("submitStatsGlobal", []), lambda v: isinstance(v, dict) and "acSubmissionNum" in v)
    calendar = _pick(found.get("userCalendar", []), lambda v: isinstance(v, dict) and "submissionCalendar" in v)
    if not stats or not calendar:
        raise RuntimeError("profile page payload is missing submitStatsGlobal/userCalendar")

    def looks_like_profile(v):
        return isinstance(v, dict) and sum(
            key in v for key in ("ranking", "postViewCount", "solutionCount", "reputation")
        ) >= 2

    profile = _pick(found.get("profile", []), looks_like_profile) or {}
    questions = _pick(found.get("allQuestionsCount", []), lambda v: isinstance(v, list) and len(v) >= 3)
    beats = _pick(found.get("problemsSolvedBeatsStats", []), lambda v: isinstance(v, list) and len(v) >= 3)
    languages = _pick(found.get("languageProblemCount", []), lambda v: isinstance(v, list) and v)
    tags = _pick(found.get("tagProblemCounts", []), lambda v: isinstance(v, dict) and "fundamental" in v)
    recent = _pick(
        found.get("recentAcSubmissionList", []),
        lambda v: isinstance(v, list) and any(isinstance(i, dict) and "titleSlug" in i for i in v),
    )
    badges = _pick(
        found.get("badges", []),
        lambda v: isinstance(v, list) and any(isinstance(i, dict) and "displayName" in i for i in v),
    ) or []

    accepted = keyed(stats.get("acSubmissionNum") or [], "submissions")
    submitted = keyed(stats.get("totalSubmissionNum") or [], "submissions")
    submissions_by_day = json.loads(calendar.get("submissionCalendar") or "{}")
    newest_badge = max(badges, key=lambda badge: int(badge.get("creationDate") or 0), default={})
    community = current.get("community", {})

    return {
        "username": USERNAME,
        "ranking": profile.get("ranking") or current.get("ranking", 0),
        "solved": keyed(stats.get("acSubmissionNum") or []),
        "questions": keyed(questions) if questions else current.get("questions", {}),
        "beats": (keyed(beats, "percentage") if beats else {}) or current.get("beats", {}),
        "acceptance": round(100 * accepted.get("All", 0) / max(submitted.get("All", 1), 1), 2),
        "submissionsYear": sum(int(value) for value in submissions_by_day.values()),
        "activeDays": calendar.get("totalActiveDays", 0),
        "maxStreak": calendar.get("streak", 0),
        "community": {
            "views": profile.get("postViewCount", community.get("views", 0)),
            "solutions": profile.get("solutionCount", community.get("solutions", 0)),
            "discuss": profile.get("categoryDiscussCount", community.get("discuss", 0)),
            "reputation": profile.get("reputation", community.get("reputation", 0)),
        },
        "languages": (
            [{"name": item["languageName"], "solved": item["problemsSolved"]} for item in languages]
            if languages
            else current.get("languages", [])
        ),
        "skills": (
            {
                level.title(): [
                    {"name": item["tagName"], "solved": item["problemsSolved"]}
                    for item in tags.get(level, [])
                ]
                for level in ("advanced", "intermediate", "fundamental")
            }
            if tags
            else current.get("skills", {})
        ),
        "badge": newest_badge.get("displayName") or current.get("badge", "Keep solving"),
        "recent": (
            [{"title": item["title"], "slug": item["titleSlug"]} for item in recent]
            if recent
            else current.get("recent", [])
        ),
    }


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


PILL_FONT_SIZE = 11
PILL_TEXT_START = 26
PILL_TEXT_END_PADDING = 13
PILL_TEXT_GAP = 10


def estimated_text_width(text: object) -> int:
    """Return a conservative width for semibold 11px pill text.

    SVG text metrics vary slightly with the font available on the viewer. Using a
    conservative estimate keeps labels and their counts from touching or crossing
    the pill border even when Segoe UI falls back to Arial.
    """
    return math.ceil(len(str(text)) * PILL_FONT_SIZE * 0.6)


def pill_width(label: str, count: object, minimum: int = 0) -> int:
    count_label = f"· {count}"
    content_width = (
        PILL_TEXT_START
        + estimated_text_width(label)
        + PILL_TEXT_GAP
        + estimated_text_width(count_label)
        + PILL_TEXT_END_PADDING
    )
    return max(minimum, content_width)


def pill(x: int, y: int, width: int, label: str, count: object, color: str) -> str:
    """Render a pill with its count right-aligned safely inside the border."""
    return f'''<g transform="translate({x} {y})"><rect width="{width}" height="29" rx="14.5" fill="{color}" fill-opacity=".10" stroke="{color}" stroke-opacity=".28"/><circle cx="15" cy="14.5" r="3" fill="{color}"/><text x="{PILL_TEXT_START}" y="19" class="pill">{esc(label)}</text><text x="{width - PILL_TEXT_END_PADDING}" y="19" text-anchor="end" class="pill pill-count">· {esc(count)}</text></g>'''


def overview_svg(data: dict) -> str:
    solved, totals = data["solved"], data["questions"]
    total = solved.get("All", 0)
    radius, circumference = 57, 2 * math.pi * 57
    progress = total / max(totals.get("All", 1), 1)
    colors = {"Easy": "#22d3a6", "Medium": "#fbbf24", "Hard": "#fb7185"}
    bars = []
    for index, level in enumerate(("Easy", "Medium", "Hard")):
        y = 164 + index * 48
        count, maximum = solved.get(level, 0), totals.get(level, 0)
        width = max(3, round(330 * count / max(maximum, 1)))
        beats = data.get("beats", {}).get(level)
        beats_text = f" · beats {beats:.2f}%" if isinstance(beats, (int, float)) else ""
        bars.append(f'''<g transform="translate(258 {y})"><text class="label" y="-8">{level}</text><text class="value" x="330" y="-8" text-anchor="end">{count} / {maximum}{beats_text}</text><rect width="330" height="9" rx="4.5" fill="#202a44"/><rect width="{width}" height="9" rx="4.5" fill="{colors[level]}"/></g>''')
    metrics = [
        ("GLOBAL RANK", f"#{data['ranking']:,}"),
        ("ACCEPTANCE", f"{data['acceptance']:.2f}%"),
        ("SUBMISSIONS · YEAR", f"{data['submissionsYear']:,}"),
        ("ACTIVE DAYS", f"{data['activeDays']:,}"),
        ("MAX STREAK", f"{data['maxStreak']} days"),
    ]
    metric_svg = "".join(
        f'''<g transform="translate({635 + (i % 2) * 135} {120 + (i // 2) * 72})"><text class="eyebrow">{label}</text><text class="metric" y="25">{value}</text></g>'''
        for i, (label, value) in enumerate(metrics)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="350" viewBox="0 0 900 350" role="img" aria-labelledby="title desc">
<title id="title">Muhammad Anas LeetCode overview</title><desc id="desc">{total} problems solved, rank {data['ranking']:,}, {data['acceptance']:.2f} percent acceptance.</desc>
<style>.title{{font:700 23px 'Segoe UI',Arial,sans-serif;fill:#f8fafc}}.sub{{font:400 12px 'Segoe UI',Arial,sans-serif;fill:#94a3b8}}.eyebrow{{font:600 9px 'Segoe UI',Arial,sans-serif;letter-spacing:1.2px;fill:#8290aa}}.metric{{font:700 18px 'Segoe UI',Arial,sans-serif;fill:#f1f5f9}}.label{{font:600 12px 'Segoe UI',Arial,sans-serif;fill:#cbd5e1}}.value{{font:500 11px 'Segoe UI',Arial,sans-serif;fill:#94a3b8}}.big{{font:800 34px 'Segoe UI',Arial,sans-serif;fill:#f8fafc}}.small{{font:500 11px 'Segoe UI',Arial,sans-serif;fill:#94a3b8}}</style>
<defs><linearGradient id="bg" x1="0" y1="0" x2="900" y2="350"><stop stop-color="#0b1020"/><stop offset="1" stop-color="#121a31"/></linearGradient><linearGradient id="accent"><stop stop-color="#8b5cf6"/><stop offset="1" stop-color="#22d3ee"/></linearGradient></defs>
<rect x=".5" y=".5" width="899" height="349" rx="18" fill="url(#bg)" stroke="#293552"/><circle cx="846" cy="32" r="95" fill="#8b5cf6" opacity=".055"/><circle cx="50" cy="350" r="110" fill="#22d3ee" opacity=".04"/>
<g transform="translate(32 35)"><rect width="34" height="34" rx="9" fill="#ffa116"/><path d="M22 8 12 17c-4 4-1 10 4 10h9M14 12l5-5" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/><text x="48" y="20" class="title">LeetCode · problem-solving signal</text><text x="48" y="39" class="sub">Static, repository-hosted snapshot · refreshed daily</text></g>
<g transform="translate(112 198)"><circle r="57" fill="none" stroke="#202a44" stroke-width="10"/><circle r="57" fill="none" stroke="url(#accent)" stroke-width="10" stroke-linecap="round" stroke-dasharray="{circumference:.1f}" stroke-dashoffset="{circumference * (1-progress):.1f}" transform="rotate(-90)"/><text class="big" y="2" text-anchor="middle">{total}</text><text class="small" y="21" text-anchor="middle">SOLVED</text><text class="small" y="78" text-anchor="middle">of {totals.get('All', 0):,}</text></g>
{''.join(bars)}<path d="M610 105v205" stroke="#293552"/>{metric_svg}
<g transform="translate(258 292)"><rect width="330" height="38" rx="11" fill="#ffa116" fill-opacity=".10" stroke="#ffa116" stroke-opacity=".30"/><text x="14" y="15" class="eyebrow" fill="#fbbf24">LATEST BADGE</text><text x="14" y="30" class="label">{esc(data['badge'])}</text></g></svg>'''


def skills_svg(data: dict) -> str:
    language_colors = ["#8b5cf6", "#22d3ee", "#fbbf24", "#fb7185"]
    language_chips, x = [], 32
    for index, item in enumerate(data.get("languages", [])[:4]):
        width = pill_width(item["name"], item["solved"], minimum=125)
        if x + width > 868:
            break
        language_chips.append(
            pill(x, 75, width, item["name"], item["solved"], language_colors[index % 4])
        )
        x += width + 12
    languages = "".join(language_chips)

    sections = []
    section_colors = {"Advanced": "#fb7185", "Intermediate": "#fbbf24", "Fundamental": "#22d3a6"}
    for row, level in enumerate(("Advanced", "Intermediate", "Fundamental")):
        items = data.get("skills", {}).get(level, [])[:5]
        chips, x = [], 165
        for item in items:
            width = pill_width(item["name"], item["solved"])
            if x + width > 868:
                break
            chips.append(
                pill(x, 124 + row * 47, width, item["name"], item["solved"], section_colors[level])
            )
            x += width + 10
        sections.append(f'<text x="32" y="{143 + row * 47}" class="level" fill="{section_colors[level]}">{level.upper()}</text>' + "".join(chips))
    community = data.get("community", {})
    footer = f"{community.get('views', 0)} profile views  ·  {community.get('solutions', 0)} solutions shared  ·  {community.get('discuss', 0)} discussions  ·  {community.get('reputation', 0)} reputation"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="305" viewBox="0 0 900 305" role="img" aria-labelledby="title desc"><title id="title">LeetCode languages and skills</title><desc id="desc">Strongest topics and languages used by Muhammad Anas.</desc><style>.title{{font:700 18px 'Segoe UI',Arial,sans-serif;fill:#f8fafc}}.sub{{font:400 11px 'Segoe UI',Arial,sans-serif;fill:#94a3b8}}.pill{{font:600 11px 'Segoe UI',Arial,sans-serif;fill:#dbe4f3}}.pill-count{{font-variant-numeric:tabular-nums}}.level{{font:700 10px 'Segoe UI',Arial,sans-serif;letter-spacing:1px}}</style><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0b1020"/><stop offset="1" stop-color="#121a31"/></linearGradient></defs><rect x=".5" y=".5" width="899" height="304" rx="18" fill="url(#bg)" stroke="#293552"/><text x="32" y="35" class="title">Languages &amp; algorithmic depth</text><text x="32" y="54" class="sub">Problems solved by language · strongest topic signals</text>{languages}<path d="M32 111h836" stroke="#293552"/>{''.join(sections)}<path d="M32 270h836" stroke="#293552"/><text x="450" y="290" text-anchor="middle" class="sub">{esc(footer)}</text></svg>'''


def write_recent(data: dict) -> None:
    lines = ["<!-- LEETCODE_RECENT_START -->", "<p align=\"center\">"]
    for index, item in enumerate(data.get("recent", [])[:6]):
        separator = " &nbsp;·&nbsp; " if index else ""
        lines.append(f'{separator}<a href="https://leetcode.com/problems/{esc(item["slug"])}"><code>{esc(item["title"])}</code></a>')
    lines.extend(["</p>", "<!-- LEETCODE_RECENT_END -->"])
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text()
    start, end = "<!-- LEETCODE_RECENT_START -->", "<!-- LEETCODE_RECENT_END -->"
    if start in readme and end in readme:
        before = readme.split(start, 1)[0]
        after = readme.split(end, 1)[1]
        readme_path.write_text(before + "\n".join(lines) + after)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="render from checked-in data only")
    parser.add_argument(
        "--fail-hard",
        action="store_true",
        help="exit non-zero if LeetCode cannot be reached instead of keeping the last good snapshot",
    )
    args = parser.parse_args()
    data = json.loads(DATA_PATH.read_text())
    if not args.offline:
        try:
            data = fetch(data)
        except Exception as error:
            print(f"WARNING: LeetCode refresh failed: {error}", file=sys.stderr)
            print(
                "WARNING: keeping the last good snapshot so this run stays green; "
                "the profile is never left broken by a third-party outage.",
                file=sys.stderr,
            )
            if args.fail_hard:
                raise SystemExit(1)
        else:
            DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
            print("Fetched current public LeetCode statistics")
    (ROOT / "profile" / "leetcode-overview.svg").write_text(overview_svg(data))
    (ROOT / "profile" / "leetcode-skills.svg").write_text(skills_svg(data))
    write_recent(data)
    print("Rendered LeetCode profile assets")


if __name__ == "__main__":
    main()
