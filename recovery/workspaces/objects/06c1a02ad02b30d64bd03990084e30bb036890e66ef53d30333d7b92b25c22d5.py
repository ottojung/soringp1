#!/usr/bin/env python3
"""Where every bill stands, derived from evidence (Founder directive 2026-11-18).

Measured problem: a bill's state existed only in the prose at the top of its file,
and that prose is stale (most enacted bills still begin "DRAFT ... NOT ENACTED").
The daily plenary therefore guessed from file times and summoned nine seats two
days running to vote on three bills that were withdrawn or never sponsored.

This module reads state from the records that actually decide it, so nothing has
to be kept in sync by hand:

  enacted    government/LAWS.md cites the bill id as the enacted bill
             ("on bill ID", "bill ID", "bill `ID`" or "tally.sh ID` PASSED")
  withdrawn  the bill's title line begins "# WITHDRAWN" (its sponsor's act)
  open       ballots were solicited: records/ballots/ID-vote-instructions.md
             (or the older records/ballots/ID-UPPERCASE-VOTE.md) exists,
             the bill is neither enacted nor withdrawn, and the bill, its
             instructions or its ballots changed in the last LAPSE_DAYS (14)
  superseded a later version of the same bill exists ("ID-v2", "ID-v3", ...
             is the Town's own versioning convention) and that later version is
             enacted, open or withdrawn: ballots go to the latest version only
  lapsed     solicited, but nothing happened for LAPSE_DAYS (Act 31 §8);
             re-soliciting (recording new vote instructions) reopens it
  draft      anything else; not vote business

Activity dates come from Git history (commit time of the last change to those
files), falling back to file times only when Git is unavailable.

For an open bill, the ballots that count are the rows of records/ballots/ID.tsv
whose digest equals the bill file's current sha256 (the rule tally.sh enforces).

  bills.py list [--json]     every bill and its state (enacted, withdrawn,
                             superseded, open, lapsed or draft)
  bills.py open [--json]     open bills, with the seats that have not yet voted
  bills.py status ID         one bill as JSON
"""
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import time

TOWN = pathlib.Path(os.environ.get("VICHE_TOWN_ROOT", "/var/lib/lubko/wd/viche"))
LAPSE_DAYS = 14


def now():
    return int(os.environ.get("VICHE_BILLS_NOW", time.time()))


def last_activity(bill):
    rel = ["records/bills/%s.md" % bill, "records/ballots/%s.tsv" % bill,
           "records/ballots/%s-vote-instructions.md" % bill,
           "records/ballots/%s-VOTE.md" % bill.upper()]
    try:
        done = subprocess.run(["git", "-C", str(TOWN), "log", "-1", "--format=%ct", "--"] + rel,
                              capture_output=True, text=True, timeout=30)
        if done.returncode == 0 and done.stdout.strip().isdigit():
            return int(done.stdout.strip())
    except (OSError, subprocess.TimeoutExpired):
        pass
    times = []
    for r in rel:
        try:
            times.append(int((TOWN / r).stat().st_mtime))
        except OSError:
            pass
    return max(times) if times else 0


def _laws():
    try:
        return (TOWN / "government" / "LAWS.md").read_text()
    except OSError:
        return ""


def enacted(bill, laws):
    b = re.escape(bill)
    end = r"(?![A-Za-z0-9_-])"
    patterns = (r"\bbill[ :]+`?" + b + end,
                r"tally\.sh " + b + r"`? PASSED")
    return any(re.search(p, laws) for p in patterns)


def withdrawn(path):
    try:
        with open(path) as handle:
            for line in handle:
                if line.strip():
                    return bool(re.match(r"#\s*WITHDRAWN\b", line.strip(), re.IGNORECASE))
    except OSError:
        pass
    return False


def solicited(bill):
    ballots = TOWN / "records" / "ballots"
    return ((ballots / (bill + "-vote-instructions.md")).is_file()
            or (ballots / (bill.upper() + "-VOTE.md")).is_file())


def digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def seats():
    path = TOWN / "government" / "seats.tsv"
    try:
        return [line.split("\t")[0] for line in path.read_text().splitlines() if line.strip()]
    except OSError:
        return []


def votes(bill, current_digest):
    path = TOWN / "records" / "ballots" / (bill + ".tsv")
    voted = []
    try:
        for line in path.read_text().splitlines():
            fields = line.split("\t")
            if len(fields) == 3 and fields[2] == current_digest:
                voted.append(fields[0])
    except OSError:
        pass
    return sorted(set(voted))


def version(bill):
    """(stem, n): "x-act-v3" -> ("x-act", 3); "x-act" -> ("x-act", 1)."""
    match = re.match(r"^(.*)-v(\d+)$", bill)
    return (match.group(1), int(match.group(2))) if match else (bill, 1)


def later_versions(bill):
    stem, n = version(bill)
    folder = TOWN / "records" / "bills"
    found = []
    for path in folder.glob(stem + "*.md"):
        s, m = version(path.stem)
        if s == stem and m > n:
            found.append(path.stem)
    return found


def status(bill, laws=None):
    laws = _laws() if laws is None else laws
    path = TOWN / "records" / "bills" / (bill + ".md")
    if not path.is_file():
        return None
    if enacted(bill, laws):
        state = "enacted"
    elif withdrawn(path):
        state = "withdrawn"
    elif any(enacted(later, laws) or withdrawn(TOWN / "records" / "bills" / (later + ".md"))
             or solicited(later) for later in later_versions(bill)):
        state = "superseded"
    elif solicited(bill):
        state = "open" if now() - last_activity(bill) < LAPSE_DAYS * 86400 else "lapsed"
    else:
        state = "draft"
    out = {"id": bill, "state": state, "file": "records/bills/%s.md" % bill}
    if state == "open":
        current = digest(path)
        voted = votes(bill, current)
        out.update({"digest": current, "voted": voted,
                    "not_voted": [s for s in seats() if s not in voted]})
    return out


def all_bills():
    laws = _laws()
    folder = TOWN / "records" / "bills"
    found = []
    if folder.is_dir():
        for path in sorted(folder.glob("*.md")):
            entry = status(path.stem, laws)
            if entry is not None:
                found.append(entry)
    return found


def main(argv):
    command = argv[0] if argv else "list"
    as_json = "--json" in argv
    if command == "status" and len(argv) >= 2:
        entry = status(argv[1])
        if entry is None:
            print("no such bill: " + argv[1], file=sys.stderr)
            return 1
        print(json.dumps(entry, sort_keys=True))
        return 0
    if command not in ("list", "open"):
        print("usage: bills.py list|open [--json] | status ID", file=sys.stderr)
        return 2
    entries = all_bills()
    if command == "open":
        entries = [e for e in entries if e["state"] == "open"]
    if as_json:
        print(json.dumps(entries, sort_keys=True))
    else:
        for e in entries:
            extra = ""
            if e["state"] == "open":
                extra = "  not yet voted: " + (" ".join(e["not_voted"]) or "nobody")
            print("%-10s %s%s" % (e["state"], e["id"], extra))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
