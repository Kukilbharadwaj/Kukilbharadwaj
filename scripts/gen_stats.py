#!/usr/bin/env python3
"""Generate assets/stats.svg from the GitHub API.

Self-hosted replacement for github-readme-stats, whose public instance keeps
going down. Run locally (unauthenticated, 60 req/hr) or from CI with GITHUB_TOKEN.

    python scripts/gen_stats.py [username]
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER = sys.argv[1] if len(sys.argv) > 1 else "Kukilbharadwaj"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = Path(__file__).resolve().parent.parent / "assets" / "stats.svg"

LANG_COLORS = {
    "Python": "#3572A5", "Jupyter Notebook": "#DA5B0B", "JavaScript": "#F1E05A",
    "TypeScript": "#3178C6", "HTML": "#E34C26", "CSS": "#563D7C", "C": "#555555",
    "C++": "#F34B7D", "Java": "#B07219", "Shell": "#89E051", "Dockerfile": "#384D54",
    "Makefile": "#427819", "PowerShell": "#012456", "Go": "#00ADD8", "Rust": "#DEA584",
    "Ruby": "#701516", "PHP": "#4F5D95", "Vue": "#41B883", "SCSS": "#C6538C",
    "Mako": "#7E858D", "Batchfile": "#C1F12E", "Procfile": "#A0A0A0",
}
FALLBACK = ["#00E5FF", "#7C3AED", "#2ea44f", "#F5C542", "#FF7A59", "#4CC9F0"]


def api(path: str) -> object:
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "profile-stats-generator",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def contributions_last_year() -> int | None:
    """Total commit contributions — GraphQL only, needs a token."""
    if not TOKEN:
        return None
    query = """
    query($login:String!){ user(login:$login){ contributionsCollection{
        totalCommitContributions
        restrictedContributionsCount } } }"""
    body = json.dumps({"query": query, "variables": {"login": USER}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "profile-stats-generator",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            c = json.load(r)["data"]["user"]["contributionsCollection"]
        return c["totalCommitContributions"] + c["restrictedContributionsCount"]
    except (urllib.error.URLError, KeyError, TypeError):
        return None


def collect() -> dict:
    user = api(f"/users/{USER}")

    repos, page = [], 1
    while True:
        batch = api(f"/users/{USER}/repos?per_page=100&page={page}&type=owner")
        repos += batch
        if len(batch) < 100:
            break
        page += 1

    owned = [r for r in repos if not r["fork"]]
    stars = sum(r["stargazers_count"] for r in owned)
    forks = sum(r["forks_count"] for r in owned)

    # Counted by each repo's primary language, not by bytes: byte counts let a
    # couple of notebook repos swamp everything and misrepresent the profile.
    langs: dict[str, int] = {}
    for r in owned:
        if r["language"]:
            langs[r["language"]] = langs.get(r["language"], 0) + 1

    top = sorted(langs.items(), key=lambda kv: kv[1], reverse=True)[:6]
    total = sum(v for _, v in top) or 1

    return {
        "repos": user["public_repos"],
        "followers": user["followers"],
        "stars": stars,
        "forks": forks,
        "counted": total,
        "commits": contributions_last_year(),
        "langs": [(n, v / total * 100) for n, v in top],
    }


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(d: dict) -> str:
    rows = [
        ("Public repositories", f"{d['repos']}"),
        ("Total stars earned", f"{d['stars']}"),
        ("Total forks", f"{d['forks']}"),
        ("Followers", f"{d['followers']}"),
    ]
    if d["commits"] is not None:
        rows.append(("Commits (last year)", f"{d['commits']}"))

    stat_svg = []
    for i, (label, value) in enumerate(rows):
        y = 92 + i * 38
        delay = 0.35 + i * 0.12
        stat_svg.append(
            f'  <g class="fin" style="animation-delay:{delay:.2f}s">\n'
            f'    <circle cx="34" cy="{y - 5}" r="3" fill="#00E5FF" opacity="0.8"/>\n'
            f'    <text class="mono lbl" x="50" y="{y}">{esc(label)}</text>\n'
            f'    <text class="mono val" x="424" y="{y}" text-anchor="end">{value}</text>\n'
            f'  </g>'
        )

    bar, legend, x = [], [], 0.0
    for i, (name, pct) in enumerate(d["langs"]):
        color = LANG_COLORS.get(name, FALLBACK[i % len(FALLBACK)])
        w = pct / 100 * 412
        bar.append(f'    <rect x="{500 + x:.1f}" y="126" width="{w:.1f}" height="16" fill="{color}"/>')
        col, row = i % 2, i // 2
        lx, ly = 500 + col * 212, 182 + row * 30
        legend.append(
            f'  <g class="fin" style="animation-delay:{1.1 + i * 0.1:.2f}s">\n'
            f'    <circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{color}"/>\n'
            f'    <text class="mono leg" x="{lx + 18}" y="{ly}">{esc(name)}</text>\n'
            f'    <text class="mono leg" x="{lx + 196}" y="{ly}" text-anchor="end" fill="#8FA6C4">{pct:.1f}%</text>\n'
            f'  </g>'
        )
        x += w

    stamp = datetime.now(timezone.utc).strftime("%d %b %Y").upper()
    nl = "\n"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 300" width="940" height="300" role="img" aria-label="GitHub statistics for {USER}">
  <defs>
    <linearGradient id="sbg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0B0F1A"/><stop offset="100%" stop-color="#0E1626"/>
    </linearGradient>
    <linearGradient id="sedge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.65"/>
      <stop offset="100%" stop-color="#7C3AED" stop-opacity="0.65"/>
    </linearGradient>
    <clipPath id="barclip"><rect x="500" y="126" width="412" height="16" rx="8"/></clipPath>
    <clipPath id="reveal"><rect x="500" y="126" width="0" height="16">
      <animate attributeName="width" from="0" to="412" dur="1.4s" begin="0.8s" fill="freeze"
               calcMode="spline" keySplines="0.2 0.8 0.2 1" keyTimes="0;1"/>
    </rect></clipPath>
    <style>
      .mono {{ font-family: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, Consolas, monospace; }}
      .lbl {{ font-size:13.5px; fill:#8FA6C4 }}
      .val {{ font-size:17px; font-weight:700; fill:#E8EEF7 }}
      .leg {{ font-size:12.5px; fill:#C6D4E6 }}
      .hdr {{ font-size:10.5px; fill:#5A6B85; letter-spacing:2.4px }}
      @keyframes fin {{ from {{ opacity:0; transform:translateY(6px) }} to {{ opacity:1; transform:translateY(0) }} }}
      .fin {{ opacity:0; animation: fin .5s ease-out forwards }}
    </style>
  </defs>

  <rect x="1" y="1" width="938" height="298" rx="14" fill="url(#sbg)" stroke="url(#sedge)" stroke-width="1.3"/>

  <text class="mono hdr" x="28" y="34">GITHUB&#160;&#183;&#160;LIVE&#160;STATS</text>
  <text class="mono hdr" x="912" y="34" text-anchor="end">SYNCED&#160;{stamp}</text>
  <path d="M28 46 H912" stroke="#1D2A40" stroke-width="1"/>
  <path d="M470 62 V272" stroke="#1D2A40" stroke-width="1"/>

  <text class="mono hdr" x="28" y="70" fill="#00E5FF">ACTIVITY</text>
{nl.join(stat_svg)}

  <text class="mono hdr" x="500" y="70" fill="#7C3AED">TOP LANGUAGES</text>
  <rect x="500" y="126" width="412" height="16" rx="8" fill="#162034"/>
  <g clip-path="url(#barclip)"><g clip-path="url(#reveal)">
{nl.join(bar)}
  </g></g>
  <text class="mono hdr" x="500" y="112">PRIMARY LANGUAGE ACROSS {d['counted']} PUBLIC REPOSITORIES</text>
{nl.join(legend)}

  <text class="mono hdr" x="28" y="286" fill="#3E4C63">GENERATED BY scripts/gen_stats.py &#183; NO THIRD-PARTY SERVICE</text>
</svg>
'''


if __name__ == "__main__":
    data = collect()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(data), encoding="utf-8")
    print(f"wrote {OUT}")
    print(json.dumps({k: v for k, v in data.items() if k != "langs"}, indent=2))
    for n, p in data["langs"]:
        print(f"  {n:<20} {p:5.1f}%")
