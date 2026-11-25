#!/usr/bin/env python3
"""Discover eligible issues from descriptions and Founder comments, not target registry."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

def invoke(*args):
    done = subprocess.run(("antonina", "board", *args), capture_output=True, text=True, timeout=35)
    if done.returncode:
        raise RuntimeError("board command unavailable: " + done.stderr[-180:])
    return json.loads(done.stdout)

def explicit(text):
    normalized = re.sub(r"\s+", " ", text.lower()) if isinstance(text, str) else ""
    pats = (
        r"(?:execution|dispatch|assignment|target)\s+(?:host|target|machine|server)\s*[:=]\s*billy-dev",
        r"(?:assign(?:ed|ment)?|route(?:d)?|dispatch(?:ed)?)\s+(?:\S+\s+){0,9}(?:to|on)\s+billy-dev",
        r"(?:agent|worker)(?:\s+\S+){0,13}\s+(?:must|shall|only|exclusively)(?:\s+\S+){0,12}\s+(?:on|at)\s+billy-dev",
        r"(?:agent|worker)\s+execution(?:\s+\S+){0,14}\s+(?:on|at)\s+billy-dev",
        r"billy-dev\s+only",
        r"only\s+(?:on|at)\s+billy-dev",
    )
    return any(re.search(p, normalized.replace(chr(96), "")) for p in pats)

def get_items():
    collected = []
    seen = set()
    for page in range(1, 101):
        batch = invoke("list", "--state", "open", "--page", str(page), "--json")
        if not isinstance(batch, list):
            raise RuntimeError("unreadable board list")
        for entry in batch:
            num = entry.get("number")
            if not isinstance(num, str) or not num or num in seen:
                raise RuntimeError("invalid/duplicate board issue")
            seen.add(num)
            collected.append(entry)
        if len(batch) < 50:
            return collected
    raise RuntimeError("board pagination incomplete")

def main():
    items = []
    for row in get_items():
        issue = invoke("show", "--id", str(row["number"]), "--page", "1", "--json")
        body = issue.get("body", "")
        assigned = explicit(body) or any(
            c.get("author") == "Vitalik"
            and ("this issue" in c.get("body", "").lower()
                 or c.get("body", "").lower().startswith("execution host:"))
            and explicit(c.get("body", ""))
            for c in (issue.get("messages") or []))
        if assigned and "legislature-only" not in body.lower() and not (
            "permanent public conversation" in body.lower()
            and "town hall" in row.get("title", "").lower()):
            items.append({"number": row["number"], "title": row.get("title", "")})
    result = {"host": "billy-dev", "eligible": items, "count": len(items),
              "complete": True, "source": "board_description_and_founder_comments"}
    target = Path(os.environ.get("VICHE_STATE_ROOT", "/var/lib/lubko/wd/viche-state")) / "branches/eligible-issues.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    tmp.replace(target)
    print(json.dumps(result, sort_keys=True))

if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, KeyError, subprocess.TimeoutExpired) as e:
        print("ELIGIBILITY_DISCOVERY_UNAVAILABLE: " + str(e), file=sys.stderr)
        sys.exit(1)
