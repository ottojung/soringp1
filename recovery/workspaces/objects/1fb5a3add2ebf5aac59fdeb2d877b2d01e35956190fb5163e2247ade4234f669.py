#!/usr/bin/env python3
"""Fixed daily plenary sitting (Founder directive 2026-11-16, item 5).

Measured problem: 8 of 10 parliamentary seats had not run since Nov 8, because
a seat only sits when the Clerk summons it and the Clerk summons nobody when no
new business arrives. A quorum (six seats) could therefore never form.

Once per UTC day, at or after VICHE_PARLIAMENT_HOUR (default 17), every
non-Clerk seat that owes a ballot on an open bill is added to
records/SUMMONED.txt with a generated summons naming those bills. The
constitutional boot dispatches each seat once; this script then removes the
seats it added so they are not re-run every sitting interval. No model call is
made here.

Business comes from government/bills.py, which derives each bill's state from
the records that decide it (Act 31 §8). When no seat owes a ballot the sitting
is recorded as not convened and nobody is summoned: on 17 and 18 November nine
seats each spent a sitting proving that the listed bills were withdrawn drafts.

  daily-sitting.py run               called from government/boot.sh each cycle
  daily-sitting.py dispatched SEAT   called by sitting.sh when SEAT is dispatched
  daily-sitting.py status            print today's record

Environment
  VICHE_DAILY_SITTING=off     disable
  VICHE_PARLIAMENT_HOUR       UTC hour, default 17
  VICHE_PARLIAMENT_SEATS      all (default) or N: summon only the first N
                              non-Clerk seats (N=5 gives a six-seat quorum
                              with the Clerk)
  VICHE_DAILY_NOW             epoch override for tests
"""
import datetime
import json
import os
import pathlib
import sys
import tempfile
import time

TOWN = pathlib.Path(os.environ.get("VICHE_TOWN_ROOT", "/var/lib/lubko/wd/viche"))
STATE = pathlib.Path(os.environ.get("VICHE_STATE_ROOT", "/var/lib/lubko/wd/viche-state"))
ROOT = STATE / "parliament" / "daily"
SUMMONED = TOWN / "records" / "SUMMONED.txt"
MARKER = "<!-- daily-plenary -->"
WINDOW_SECONDS = 6 * 3600


def now():
    return int(os.environ.get("VICHE_DAILY_NOW", time.time()))


def atomic_write(path, text):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".tmp.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w") as handle:
            handle.write(text)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def seat_ids():
    path = TOWN / "government" / "seats.tsv"
    ids = []
    if path.is_file():
        for line in path.read_text().splitlines():
            if line.strip():
                ids.append(line.split("\t")[0])
    return ids


def summoned_ids():
    if not SUMMONED.is_file():
        return []
    return [line.strip() for line in SUMMONED.read_text().splitlines() if line.strip()]


def write_summoned(ids):
    SUMMONED.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(SUMMONED, "".join(i + "\n" for i in ids))


def record_path(day):
    return ROOT / (day + ".json")


def load(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return None


def release_finished(current):
    """Remove from SUMMONED.txt the seats this script added and that have sat
    (or whose six-hour window expired). Seats the Clerk summoned itself are
    never touched."""
    if not ROOT.is_dir():
        return
    for path in sorted(ROOT.glob("2*.json")):
        data = load(path)
        if not isinstance(data, dict):
            continue
        added = list(data.get("added", []))
        dispatched = set(data.get("dispatched", []))
        convened = int(data.get("convened_at", 0))
        release = [s for s in added if s in dispatched or current - convened > WINDOW_SECONDS]
        if not release:
            continue
        write_summoned([i for i in summoned_ids() if i not in set(release)])
        data["added"] = [s for s in added if s not in release]
        data["released"] = sorted(set(data.get("released", [])) | set(release))
        atomic_write(path, json.dumps(data, sort_keys=True) + "\n")


def open_bills():
    """Open bills from government/bills.py: [{id, not_voted, ...}]. A failure
    to read bill state convenes nobody rather than guessing."""
    import subprocess
    script = TOWN / "government" / "bills.py"
    if not script.is_file():
        return None
    try:
        done = subprocess.run([sys.executable, str(script), "open", "--json"],
                              capture_output=True, text=True, timeout=120,
                              env=dict(os.environ, VICHE_BILLS_NOW=str(now())))
        if done.returncode != 0:
            return None
        return json.loads(done.stdout)
    except (OSError, ValueError, subprocess.TimeoutExpired):
        return None


def convene(current):
    day = datetime.datetime.fromtimestamp(current, datetime.timezone.utc)
    try:
        hour = int(os.environ.get("VICHE_PARLIAMENT_HOUR", "17"))
    except ValueError:
        hour = 17
    if day.hour < hour:
        return
    stamp = day.strftime("%Y-%m-%d")
    if record_path(stamp).exists():
        return
    if not (STATE / "inaugurated").exists():
        return
    seats = seat_ids()
    if not seats:
        return
    clerk, others = seats[0], seats[1:]
    limit = os.environ.get("VICHE_PARLIAMENT_SEATS", "all")
    if limit.isdigit():
        others = others[: int(limit)]
    bills = open_bills()
    agenda = ROOT / "plenary-agenda.md"
    if bills is None:
        # Bill state unreadable: record it, summon nobody, try again next cycle.
        print("Viche: daily plenary postponed, bill state unreadable", file=sys.stderr)
        return
    owed = {}
    for bill in bills:
        for seat in bill.get("not_voted", []):
            owed.setdefault(seat, []).append(bill["id"])
    business = [s for s in others if owed.get(s)]
    lines = ["# Daily plenary sitting " + stamp, "",
             "Generated by government/daily-sitting.py from government/bills.py (Act 31 §8).", "",
             "## Open bills and the seats that have not yet voted on their current text"]
    lines += ["- %s (records/bills/%s.md): %s" % (b["id"], b["id"], " ".join(b.get("not_voted", [])) or "all seats have voted; the Clerk tallies")
              for b in bills] or ["- none"]
    if not business:
        lines += ["", "No seat owes a ballot, so no seat is summoned today."]
    else:
        lines += ["", "## What a summoned seat delivers",
                  "- For each bill listed against you: an independent ballot on its current text, recorded",
                  "  as records/ballots/BILL-SEAT.json plus your row in records/ballots/BILL.tsv, or a recorded",
                  "  reason to abstain or to ask for an amendment.",
                  "- Then land it: commit in your worktree and run",
                  "  `government/propose-delivery.sh --office SEAT SLUG`. The integrator does the rest (Act 31)."]
    lines.append("")
    atomic_write(agenda, "\n".join(lines))
    added = []
    if business:
        summons_dir = TOWN / "records" / "summons"
        summons_dir.mkdir(parents=True, exist_ok=True)
        existing = summoned_ids()
        for seat in business:
            file = summons_dir / (seat + ".md")
            if not file.exists() or file.stat().st_size == 0 or MARKER in file.read_text():
                atomic_write(file, "%s\n# Daily plenary sitting %s for seat %s\n\n"
                                   "Your ballot is owed on: %s.\nThe agenda is %s.\n"
                                   "This summons was generated; the Clerk may replace it with a specific assignment.\n"
                             % (MARKER, stamp, seat, ", ".join(owed[seat]), agenda))
            if seat not in existing:
                existing.append(seat)
                added.append(seat)
        write_summoned(existing)
    atomic_write(record_path(stamp), json.dumps(
        {"day": stamp, "clerk": clerk, "convened_at": current, "convened": bool(business),
         "added": added, "dispatched": [], "bills_listed": [b["id"] for b in bills],
         "owed": {s: owed[s] for s in business}}, sort_keys=True) + "\n")
    if business:
        print("Viche: daily plenary convened for %s with %d seat(s)" % (stamp, len(added)), file=sys.stderr)


def dispatched(seat):
    current = now()
    stamp = datetime.datetime.fromtimestamp(current, datetime.timezone.utc).strftime("%Y-%m-%d")
    path = record_path(stamp)
    data = load(path)
    if not isinstance(data, dict) or seat not in data.get("added", []):
        return
    data["dispatched"] = sorted(set(data.get("dispatched", [])) | {seat})
    atomic_write(path, json.dumps(data, sort_keys=True) + "\n")


def main(argv):
    command = argv[0] if argv else "run"
    if command == "run":
        if os.environ.get("VICHE_DAILY_SITTING", "on") == "off":
            return 0
        ROOT.mkdir(parents=True, exist_ok=True)
        release_finished(now())
        convene(now())
    elif command == "dispatched" and len(argv) == 2:
        dispatched(argv[1])
    elif command == "status":
        stamp = datetime.datetime.fromtimestamp(now(), datetime.timezone.utc).strftime("%Y-%m-%d")
        data = load(record_path(stamp))
        if data is not None:
            print(json.dumps(data, sort_keys=True, indent=2))
    else:
        print("usage: daily-sitting.py run|dispatched SEAT|status", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
