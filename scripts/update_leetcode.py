#!/usr/bin/env python3
"""Fetch Muhammad Anas' public LeetCode data and render lightweight local SVGs.

The checked-in JSON is also a fallback: if LeetCode is temporarily unavailable, the
last good cards remain usable and the profile never depends on a third-party image
server at page-view time.
"""
from __future__ import annotations

import argparse
import html
import json
import math
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "profile" / "leetcode-data.json"
USERNAME = "muhammadanas20"
ENDPOINT = "https://leetcode.com/graphql/"

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


def graphql(query: str, variables: dict) -> dict:
    body = json.dumps({"query": query, "variables": variables}).encode()
    request = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Referer": f"https://leetcode.com/u/{USERNAME}/",
            "User-Agent": "github-profile-stats/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.load(response)
    if result.get("errors"):
        raise RuntimeError(result["errors"][0].get("message", "LeetCode GraphQL error"))
    return result["data"]


def keyed(items: list[dict], value: str = "count") -> dict:
    return {item["difficulty"]: item.get(value, 0) for item in items}


def fetch(current: dict) -> dict:
    profile_data = graphql(PROFILE_QUERY, {"username": USERNAME})
    skills_data = graphql(SKILLS_QUERY, {"username": USERNAME})
    recent_data = graphql(RECENT_QUERY, {"username": USERNAME, "limit": 8})
    user = profile_data["matchedUser"]
    stats = user["submitStatsGlobal"]
    accepted = keyed(stats["acSubmissionNum"], "submissions")
    submitted = keyed(stats["totalSubmissionNum"], "submissions")
    calendar = skills_data["matchedUser"]["userCalendar"]
    submissions_by_day = json.loads(calendar.get("submissionCalendar") or "{}")
    badges = user.get("badges") or []
    newest_badge = max(badges, key=lambda badge: int(badge.get("creationDate") or 0), default={})

    return {
        "username": USERNAME,
        "ranking": user["profile"].get("ranking", current.get("ranking", 0)),
        "solved": keyed(stats["acSubmissionNum"]),
        "questions": keyed(profile_data["allQuestionsCount"]),
        "beats": keyed(user.get("problemsSolvedBeatsStats") or [], "percentage"),
        "acceptance": round(100 * accepted.get("All", 0) / max(submitted.get("All", 1), 1), 2),
        "submissionsYear": sum(int(value) for value in submissions_by_day.values()),
        "activeDays": calendar.get("totalActiveDays", 0),
        "maxStreak": calendar.get("streak", 0),
        "community": {
            "views": user["profile"].get("postViewCount", 0),
            "solutions": user["profile"].get("solutionCount", 0),
            "discuss": user["profile"].get("categoryDiscussCount", 0),
            "reputation": user["profile"].get("reputation", 0),
        },
        "languages": [
            {"name": item["languageName"], "solved": item["problemsSolved"]}
            for item in user.get("languageProblemCount") or []
        ],
        "skills": {
            level.title(): [
                {"name": item["tagName"], "solved": item["problemsSolved"]}
                for item in skills_data["matchedUser"]["tagProblemCounts"].get(level, [])
            ]
            for level in ("advanced", "intermediate", "fundamental")
        },
        "badge": newest_badge.get("displayName") or current.get("badge", "Keep solving"),
        "recent": [
            {"title": item["title"], "slug": item["titleSlug"]}
            for item in recent_data.get("recentAcSubmissionList") or []
        ],
    }


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def pill(x: int, y: int, width: int, text: str, color: str) -> str:
    return f'''<g transform="translate({x} {y})"><rect width="{width}" height="29" rx="14.5" fill="{color}" fill-opacity=".10" stroke="{color}" stroke-opacity=".28"/><circle cx="15" cy="14.5" r="3" fill="{color}"/><text x="26" y="19" class="pill">{esc(text)}</text></g>'''


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
    languages = "".join(
        pill(32 + i * 137, 75, 125, f"{item['name']} · {item['solved']}", language_colors[i % 4])
        for i, item in enumerate(data.get("languages", [])[:4])
    )
    sections = []
    section_colors = {"Advanced": "#fb7185", "Intermediate": "#fbbf24", "Fundamental": "#22d3a6"}
    for row, level in enumerate(("Advanced", "Intermediate", "Fundamental")):
        items = data.get("skills", {}).get(level, [])[:5]
        chips, x = [], 165
        for item in items:
            width = min(180, 38 + len(item["name"]) * 6)
            chips.append(pill(x, 124 + row * 47, width, f"{item['name']} · {item['solved']}", section_colors[level]))
            x += width + 10
            if x > 850:
                break
        sections.append(f'<text x="32" y="{143 + row * 47}" class="level" fill="{section_colors[level]}">{level.upper()}</text>' + "".join(chips))
    community = data.get("community", {})
    footer = f"{community.get('views', 0)} profile views  ·  {community.get('solutions', 0)} solutions shared  ·  {community.get('discuss', 0)} discussions  ·  {community.get('reputation', 0)} reputation"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="305" viewBox="0 0 900 305" role="img" aria-labelledby="title desc"><title id="title">LeetCode languages and skills</title><desc id="desc">Strongest topics and languages used by Muhammad Anas.</desc><style>.title{{font:700 18px 'Segoe UI',Arial,sans-serif;fill:#f8fafc}}.sub{{font:400 11px 'Segoe UI',Arial,sans-serif;fill:#94a3b8}}.pill{{font:600 11px 'Segoe UI',Arial,sans-serif;fill:#dbe4f3}}.level{{font:700 10px 'Segoe UI',Arial,sans-serif;letter-spacing:1px}}</style><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#0b1020"/><stop offset="1" stop-color="#121a31"/></linearGradient></defs><rect x=".5" y=".5" width="899" height="304" rx="18" fill="url(#bg)" stroke="#293552"/><text x="32" y="35" class="title">Languages &amp; algorithmic depth</text><text x="32" y="54" class="sub">Problems solved by language · strongest topic signals</text>{languages}<path d="M32 111h836" stroke="#293552"/>{''.join(sections)}<path d="M32 270h836" stroke="#293552"/><text x="450" y="290" text-anchor="middle" class="sub">{esc(footer)}</text></svg>'''


def write_recent(data: dict) -> None:
    lines = ["<!-- LEETCODE_RECENT_START -->", "<p align=\"center\">"]
    for index, item in enumerate(data.get("recent", [])[:6]):
        separator = " &nbsp;·&nbsp; " if index else ""
        lines.append(f'{separator}<a href="https://leetcode.com/problems/{esc(item["slug"])}/"><code>{esc(item["title"])}</code></a>')
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
    args = parser.parse_args()
    data = json.loads(DATA_PATH.read_text())
    if not args.offline:
        try:
            data = fetch(data)
            DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
            print("Fetched current public LeetCode statistics")
        except Exception as error:
            print(f"LeetCode fetch unavailable; using last good snapshot: {error}")
    (ROOT / "profile" / "leetcode-overview.svg").write_text(overview_svg(data))
    (ROOT / "profile" / "leetcode-skills.svg").write_text(skills_svg(data))
    write_recent(data)
    print("Rendered LeetCode profile assets")


if __name__ == "__main__":
    main()
