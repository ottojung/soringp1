#!/usr/bin/env python3
"""Randomized, independent audit selection. Does not trust executive task lists."""
import hashlib
from datetime import datetime
import json
import os
from pathlib import Path
import random
import secrets
import subprocess
import sys
import time


def command(*argv):
    p = subprocess.run(argv, text=True, capture_output=True, timeout=40)
    if p.returncode:
        raise RuntimeError(f"{argv[:3]} failed: {p.stderr[-250:]}")
    return p.stdout


def board(state):
    found, ids = [], set()
    for page in range(1, 101):
        data = json.loads(command("antonina", "board", "list", "--state",
                                  state, "--page", str(page), "--json"))
        if not isinstance(data, list):
            raise RuntimeError("unexpected board response")
        for issue in data:
            if issue["number"] in ids:
                raise RuntimeError("duplicate issue in board snapshot")
            ids.add(issue["number"])
            found.append(issue)
        if len(data) < 50:
            return found
    raise RuntimeError("incomplete board snapshot")


def write(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    os.replace(tmp, path)


def choose(rng, items, size, now, root, kind):
    chosen = []
    items = items[:]
    for _ in range(min(size, len(items))):
        weights = []
        for item in items:
            key = hashlib.sha256(f"{kind}:{item['id']}".encode()).hexdigest()
            previous = root / "seen" / key
            last = int(previous.read_text()) if previous.exists() else 0
            age = now - last if last else now
            try:
                created = datetime.fromisoformat(item.get("createdAt", "").replace("Z", "+00:00")).timestamp()
                issue_age = max(0, now - created)
            except (ValueError, TypeError):
                issue_age = 0
            # Persistently old issues grow harder to neglect even if somebody
            # comments on them. No project title or executive report is used.
            weights.append(1.0 + min(8.0, max(0, age) / (3 * 86400))
                           + (min(6.0, issue_age / (7 * 86400)) if kind == "ignored_work" else 0))
        threshold = rng.random() * sum(weights)
        for i, weight in enumerate(weights):
            threshold -= weight
            if threshold < 0:
                break
        chosen.append(items.pop(i))
    return chosen


def main():
    now = int(os.environ.get("VICHE_OVERSIGHT_NOW", time.time()))
    root = Path(os.environ.get("VICHE_STATE_ROOT",
                               "/var/lib/lubko/wd/viche-state")) / "oversight" / "random"
    town = os.environ.get("VICHE_TOWN_ROOT", "/var/lib/lubko/wd/viche")
    open_issues = board("open")
    closed = board("closed")
    decisions = []
    log = command("git", "-C", town, "log", "-40", "--format=%H%x09%s",
                  "--", "government/", "records/bills/")
    for line in log.splitlines():
        sha, _, title = line.partition("\t")
        if len(sha) == 40:
            decisions.append({"id": sha, "title": title})
    pools = {
        "ignored_work": [{"id": str(i["number"]), "title": i["title"], "createdAt": i.get("createdAt", "")} for i in open_issues],
        "claimed_delivery": [{"id": str(i["number"]), "title": i["title"]} for i in closed],
        "government_decision": decisions,
    }
    # The board/git universe is captured before the random seed exists.
    digest = hashlib.sha256(json.dumps(pools, sort_keys=True).encode()).hexdigest()
    seed = secrets.token_hex(32)
    rng = random.Random(int(seed, 16))
    sample = []
    for name, count in (("ignored_work", 2), ("claimed_delivery", 1),
                        ("government_decision", 1)):
        for entry in choose(rng, pools[name], count, now, root, name):
            case = {"population": name, **entry}
            case["case_id"] = hashlib.sha256(
                f"{now}:{seed}:{name}:{entry['id']}".encode()).hexdigest()[:18]
            if name != "government_decision":
                issue = json.loads(command("antonina", "board", "show", "--id",
                                           entry["id"], "--page", "1", "--json"))
                case["body"] = issue.get("body", "")[:4000]
                case["recent_comments"] = [
                    {"author": c.get("author", ""), "body": c.get("body", "")[:550]}
                    for c in issue.get("messages", [])[-3:]]
            sample.append(case)
    batch = {"at": now, "snapshot_sha256": digest, "seed_after_snapshot": seed,
             "universe": {k: len(v) for k, v in pools.items()},
             "cases": sample, "not_a_compliance_certificate": True}
    write(root / "latest.json", batch)
    for case in sample:
        write(root / "cases" / f"{case['case_id']}.json", {"at": now, **case})
        key = hashlib.sha256(f"{case['population']}:{case['id']}".encode()).hexdigest()
        seen = root / "seen" / key
        seen.parent.mkdir(parents=True, exist_ok=True)
        seen.write_text(str(now))
    print(json.dumps(batch, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Independent audit sampler failed: {error}", file=sys.stderr)
        sys.exit(1)
