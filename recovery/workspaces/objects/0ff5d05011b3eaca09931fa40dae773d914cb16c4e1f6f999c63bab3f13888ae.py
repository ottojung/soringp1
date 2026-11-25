#!/usr/bin/env python3
"""Non-mutating inventory of Viche work that exists off main.

This is a decision aid, not permission to merge or enact legislation.
Records signed by another office still need Act 21 verification and review.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone


def git(path, *args, required=True):
    proc = subprocess.run(
        ["git", "-C", str(path), *args],
        text=True, capture_output=True, check=False,
    )
    if proc.returncode and required:
        raise RuntimeError(f"git {' '.join(args)} in {path}: {proc.stderr.strip()}")
    return proc.stdout.strip() if proc.returncode == 0 else None


def classify(paths):
    files = [p for p in paths if p != "AGENTS.md"]
    if not files:
        return "policy-only"
    if any(p == "government/LAWS.md" or p.startswith("records/ballots/")
           or p.startswith("records/bills/") for p in files):
        return "legislative-review"
    if any(p.startswith(("government/", "tests/", "constitution/", "deploy/", ".github/"))
           for p in files):
        return "code-review"
    if all(p.startswith("records/") for p in files):
        return "records-review"
    return "mixed-review"


def collect(repo, seats):
    repo = Path(repo).resolve()
    seats = Path(seats).resolve()
    head = git(repo, "rev-parse", "refs/remotes/origin/main")
    entries = []
    worktrees = git(repo, "worktree", "list", "--porcelain").splitlines()
    for item in worktrees:
        if not item.startswith("worktree "):
            continue
        path = Path(item[len("worktree "):]).resolve()
        if path == seats or seats not in path.parents:
            continue
        branch = git(path, "symbolic-ref", "-q", "--short", "HEAD", required=False)
        if branch is None:
            continue
        counts = git(path, "rev-list", "--left-right", "--count",
                     "refs/remotes/origin/main...HEAD")
        behind, ahead = [int(v) for v in counts.split()]
        if ahead == 0:
            continue
        files = git(path, "diff", "--name-only", "refs/remotes/origin/main...HEAD").splitlines()
        if not files:
            continue
        category = classify(files)
        if category == "policy-only":
            continue
        dirty = git(path, "status", "--porcelain", "--untracked-files=normal").splitlines()
        remote = f"refs/remotes/origin/{branch}"
        published_sha = git(path, "rev-parse", "--verify", remote, required=False)
        unpublished = int(git(path, "rev-list", "--count", f"{remote}..HEAD")) if published_sha else ahead
        entries.append({
            "branch": branch,
            "worktree": str(path),
            "head": git(path, "rev-parse", "HEAD"),
            "ahead_main": ahead,
            "behind_main": behind,
            "files": files,
            "category": category,
            "dirty": dirty,
            "unpublished_commits": unpublished,
            "needs": (
                "parliamentary authority and ballot audit before enactment"
                if category == "legislative-review" else
                "independent review and exact-commit full suite"
                if category in ("code-review", "mixed-review") else
                "independent records review and exact-commit records smoke"
            ),
        })
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "canonical": head,
        "candidate_count": len(entries),
        "candidates": sorted(entries, key=lambda x: (bool(x["dirty"]), x["category"], -x["ahead_main"], x["branch"])),
        "caveat": "Inventory is not proof of deliverability or legislative authority; no automatic merge permission.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=os.environ.get("VICHE_TOWN_ROOT", "/var/lib/lubko/wd/viche"))
    parser.add_argument("--seats", default=os.environ.get("VICHE_SEATS_ROOT", "/var/lib/lubko/wd/viche-seats"))
    parser.add_argument("--brief", action="store_true")
    args = parser.parse_args()
    try:
        result = collect(args.repo, args.seats)
    except (OSError, RuntimeError, ValueError) as e:
        print(f"delivery-inventory: {e}", file=sys.stderr)
        return 1
    if not args.brief:
        print(json.dumps(result, indent=2))
    else:
        for item in result["candidates"]:
            status = ("dirty" if item["dirty"] else "clean")
            if item["unpublished_commits"]:
                status += f", unpublished={item['unpublished_commits']}"
            print(f"{item['category']} | {status} | ahead={item['ahead_main']} | {item['branch']}")
        print("Review, exact-commit verification and legal authority remain prerequisites.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
