#!/usr/bin/env python3
"""Obligation expiry (Founder directive 2026-11-16, "Act 30" in LAWS.md).

Every obligation that the town's scripts inject into an office's prompt now has
an owner who can close it alone and an expiry time. When the time passes and
nobody has renewed it with a reason, the obligation is ARCHIVED, never deleted:
the original evidence is kept, the state becomes ``expired`` and the injection
stops. An expired obligation is explicitly *unverified*; expiry is not proof
that the underlying problem is fixed (Constitution VI: no misrepresenting
progress), it only stops the obligation from taxing every future pass.

Kinds handled
  receipt  state/continuity/reconciliation-OFFICE.json  (state awaiting_reconciliation)
           owner: the office named in the receipt
  handoff  records/handoffs/H-*.txt                      (status open)
           owner: the office that holds the handoff (see its ``assigned-by``)
  mailbox  state/oversight/judiciary-mailbox/inbox/*     (unreviewed reports)
           owner: the Judiciary

Commands
  sweep [--now EPOCH]                 expire everything past its time (default)
  report                              JSON summary of live and expired obligations
  renew receipt OFFICE --reason TEXT  restart the clock for one receipt
  renew handoff ID --reason TEXT      restart the clock for one handoff
  close receipt OFFICE --evidence TXT owner closes its own receipt, no verifier needed

Environment
  VICHE_OBLIGATION_TTL_HOURS   default 72 (0 disables expiry)
  VICHE_TOWN_ROOT / VICHE_STATE_ROOT
"""
import argparse
import datetime
import json
import os
import pathlib
import re
import shutil
import sys
import tempfile
import time

TOWN = pathlib.Path(os.environ.get("VICHE_TOWN_ROOT", "/var/lib/lubko/wd/viche"))
STATE = pathlib.Path(os.environ.get("VICHE_STATE_ROOT", "/var/lib/lubko/wd/viche-state"))
LEDGER_DIR = STATE / "obligations"
CONTINUITY = STATE / "continuity"
HANDOFFS = TOWN / "records" / "handoffs"
MAILBOX = STATE / "oversight" / "judiciary-mailbox"


def ttl_seconds():
    raw = os.environ.get("VICHE_OBLIGATION_TTL_HOURS", "72")
    try:
        hours = float(raw)
    except ValueError:
        hours = 72.0
    return int(hours * 3600) if hours > 0 else 0


def iso_to_epoch(text):
    if not isinstance(text, str) or not text:
        return None
    value = text.strip()
    # Accept second-precision (canonical) and minute-precision timestamps;
    # the latter occur in durable records such as handoffs (e.g. "2026-...T16:02Z").
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%MZ"):
        try:
            return datetime.datetime.strptime(value, fmt).replace(
                tzinfo=datetime.timezone.utc).timestamp()
        except ValueError:
            continue
    return None


def epoch_to_iso(epoch):
    return datetime.datetime.fromtimestamp(int(epoch), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def atomic_write(path, text, mode=None):
    path = pathlib.Path(path)
    fd, name = tempfile.mkstemp(prefix=".tmp.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w") as handle:
            handle.write(text)
        if mode is not None:
            os.chmod(name, mode)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def ledger(entry):
    LEDGER_DIR.mkdir(parents=True, exist_ok=True)
    with open(LEDGER_DIR / "ledger.jsonl", "a") as handle:
        handle.write(json.dumps(entry, sort_keys=True) + "\n")


# --- receipts ---------------------------------------------------------------

def receipt_clock(receipt):
    """Epoch from which the receipt's time-to-live is counted."""
    start = iso_to_epoch(receipt.get("at"))
    renewed = iso_to_epoch(receipt.get("renewed_at"))
    candidates = [value for value in (start, renewed) if value is not None]
    return max(candidates) if candidates else None


def receipts():
    for path in sorted(CONTINUITY.glob("reconciliation-*.json")):
        try:
            data = json.loads(path.read_text())
        except (OSError, ValueError):
            continue
        if isinstance(data, dict):
            yield path, data


def expire_receipts(now, ttl):
    expired = []
    for path, data in receipts():
        if data.get("state") != "awaiting_reconciliation":
            continue
        clock = receipt_clock(data)
        if clock is None or ttl <= 0 or now - clock < ttl:
            continue
        archive = CONTINUITY / "archive"
        archive.mkdir(parents=True, exist_ok=True)
        stamp = re.sub(r"[^0-9A-Za-z]", "", str(data.get("at", "unknown")))
        copy = archive / (path.stem + "-" + stamp + ".original.json")
        if not copy.exists():
            shutil.copy2(path, copy)
        updated = dict(data)
        updated.update({
            "state": "expired",
            "expired_at": epoch_to_iso(now),
            "expired_unverified": True,
            "expiry_reason": "ttl_elapsed_without_renewal",
            "expiry_ttl_hours": ttl / 3600,
            "original_preserved": str(copy.relative_to(STATE)),
        })
        atomic_write(path, json.dumps(updated, separators=(",", ":")) + "\n", 0o600)
        age = (now - clock) / 3600
        ledger({"at": epoch_to_iso(now), "kind": "receipt", "id": data.get("office", path.stem),
                "age_hours": round(age, 1), "action": "expired"})
        expired.append(data.get("office", path.stem))
    return expired


# --- handoffs ---------------------------------------------------------------

def handoff_fields(path):
    fields = {}
    try:
        for line in path.read_text().splitlines():
            match = re.match(r"^([a-z-]+):\s*(.*)$", line)
            if match:
                fields[match.group(1)] = match.group(2)
    except OSError:
        pass
    return fields


def expire_handoffs(now, ttl):
    expired = []
    if not HANDOFFS.is_dir():
        return expired
    for path in sorted(HANDOFFS.glob("H-*.txt")):
        fields = handoff_fields(path)
        if fields.get("status") != "open":
            continue
        created = iso_to_epoch(fields.get("created"))
        renewed = iso_to_epoch(fields.get("renewed"))
        clock = max([v for v in (created, renewed) if v is not None], default=None)
        if clock is None or ttl <= 0 or now - clock < ttl:
            continue
        text = path.read_text()
        text = re.sub(r"(?m)^status: open$", "status: expired", text, count=1)
        if not text.endswith("\n"):
            text += "\n"
        text += "closed: %s\nnote: expired unverified after %dh without renewal (Act 30); evidence preserved\n" % (
            epoch_to_iso(now), ttl // 3600)
        atomic_write(path, text)
        ledger({"at": epoch_to_iso(now), "kind": "handoff", "id": fields.get("id", path.stem),
                "age_hours": round((now - clock) / 3600, 1), "action": "expired"})
        expired.append(fields.get("id", path.stem))
    return expired


# --- Judiciary mailbox -------------------------------------------------------

def mailbox_item_epoch(path):
    match = re.match(r"^(\d{8})T(\d{4})(\d{2})?Z", path.name)
    if match:
        date, hhmm, ss = match.group(1), match.group(2), match.group(3) or "00"
        try:
            return datetime.datetime.strptime(date + hhmm + ss, "%Y%m%d%H%M%S").replace(
                tzinfo=datetime.timezone.utc).timestamp()
        except ValueError:
            pass
    try:
        return path.stat().st_mtime
    except OSError:
        return None


def expire_mailbox(now, ttl):
    expired = []
    inbox = MAILBOX / "inbox"
    if not inbox.is_dir() or ttl <= 0:
        return expired
    target = MAILBOX / "expired"
    for path in sorted(inbox.iterdir()):
        if not path.is_file() or path.name.startswith("."):
            continue
        stamp = mailbox_item_epoch(path)
        if stamp is None or now - stamp < ttl:
            continue
        target.mkdir(parents=True, exist_ok=True)
        destination = target / path.name
        if destination.exists():
            destination = target / (path.name + "." + str(int(now)))
        os.replace(path, destination)
        ledger({"at": epoch_to_iso(now), "kind": "mailbox", "id": path.name,
                "age_hours": round((now - stamp) / 3600, 1), "action": "expired"})
        expired.append(path.name)
    return expired


# --- commands ---------------------------------------------------------------

def sweep(now):
    ttl = ttl_seconds()
    result = {"at": epoch_to_iso(now), "ttl_hours": ttl / 3600,
              "receipts": expire_receipts(now, ttl),
              "handoffs": expire_handoffs(now, ttl),
              "mailbox": expire_mailbox(now, ttl)}
    LEDGER_DIR.mkdir(parents=True, exist_ok=True)
    atomic_write(LEDGER_DIR / "latest.json", json.dumps(result, sort_keys=True) + "\n")
    return result


def report(now):
    ttl = ttl_seconds()
    live = {"receipts": [], "handoffs": [], "mailbox": 0}
    for _, data in receipts():
        if data.get("state") == "awaiting_reconciliation":
            clock = receipt_clock(data)
            live["receipts"].append({
                "office": data.get("office"),
                "expires_at": epoch_to_iso(clock + ttl) if clock and ttl else None})
    if HANDOFFS.is_dir():
        for path in sorted(HANDOFFS.glob("H-*.txt")):
            fields = handoff_fields(path)
            if fields.get("status") == "open":
                created = iso_to_epoch(fields.get("created"))
                renewed = iso_to_epoch(fields.get("renewed"))
                clock = max([v for v in (created, renewed) if v is not None], default=None)
                live["handoffs"].append({
                    "id": fields.get("id"),
                    "expires_at": epoch_to_iso(clock + ttl) if clock and ttl else None})
    inbox = MAILBOX / "inbox"
    if inbox.is_dir():
        live["mailbox"] = sum(1 for p in inbox.iterdir() if p.is_file() and not p.name.startswith("."))
    totals = {"receipt": 0, "handoff": 0, "mailbox": 0}
    ledger_path = LEDGER_DIR / "ledger.jsonl"
    if ledger_path.is_file():
        for line in ledger_path.read_text().splitlines():
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            if entry.get("action") == "expired" and entry.get("kind") in totals:
                totals[entry["kind"]] += 1
    return {"at": epoch_to_iso(now), "ttl_hours": ttl / 3600, "live": live, "expired_total": totals}


def renew(kind, ident, reason, now):
    if not reason or not reason.strip():
        raise SystemExit("renewal requires a reason")
    if kind == "receipt":
        path = CONTINUITY / ("reconciliation-" + ident + ".json")
        data = json.loads(path.read_text())
        if data.get("state") != "awaiting_reconciliation":
            raise SystemExit("receipt %s is %s, not awaiting_reconciliation" % (ident, data.get("state")))
        data["renewed_at"] = epoch_to_iso(now)
        data["renewals"] = int(data.get("renewals", 0)) + 1
        data["renewal_reason"] = reason.strip()
        atomic_write(path, json.dumps(data, separators=(",", ":")) + "\n", 0o600)
    elif kind == "handoff":
        path = HANDOFFS / (ident + ".txt")
        fields = handoff_fields(path)
        if fields.get("status") != "open":
            raise SystemExit("handoff %s is %s, not open" % (ident, fields.get("status")))
        text = path.read_text()
        if not text.endswith("\n"):
            text += "\n"
        text += "renewed: %s\nrenewal-reason: %s\n" % (epoch_to_iso(now), " ".join(reason.split()))
        atomic_write(path, text)
    else:
        raise SystemExit("unknown kind " + kind)
    ledger({"at": epoch_to_iso(now), "kind": kind, "id": ident, "action": "renewed", "reason": reason.strip()})


def close_receipt(office, evidence, now):
    if not evidence or not evidence.strip():
        raise SystemExit("closing a receipt requires evidence text")
    path = CONTINUITY / ("reconciliation-" + office + ".json")
    data = json.loads(path.read_text())
    if data.get("state") != "awaiting_reconciliation":
        raise SystemExit("receipt %s is %s" % (office, data.get("state")))
    data.update({"state": "closed_by_owner", "closed_at": epoch_to_iso(now),
                 "closed_by": office, "closure_evidence": evidence.strip(),
                 "independently_verified": False})
    atomic_write(path, json.dumps(data, separators=(",", ":")) + "\n", 0o600)
    ledger({"at": epoch_to_iso(now), "kind": "receipt", "id": office, "action": "closed_by_owner",
            "evidence": evidence.strip()})


def close_handoff(ident, evidence, now):
    if not evidence or not evidence.strip():
        raise SystemExit("closing a handoff requires evidence text")
    path = HANDOFFS / (ident + ".txt")
    if not path.is_file():
        raise SystemExit("no such handoff: %s" % ident)
    fields = handoff_fields(path)
    if fields.get("status") != "open":
        raise SystemExit("handoff %s is %s, not open" % (ident, fields.get("status")))
    text = path.read_text()
    if not text.endswith("\\n"):
        text += "\\n"
    text = re.sub(r"(?m)^status: open$", "status: closed_by_owner", text, count=1)
    text += "closed: %s\n" % epoch_to_iso(now)
    text += "closed-by: owner\n"
    text += "closure-evidence: %s\n" % " ".join(evidence.split())
    text += "independently-verified: false\n"
    atomic_write(path, text)
    ledger({"at": epoch_to_iso(now), "kind": "handoff", "id": ident, "action": "closed_by_owner",
            "evidence": evidence.strip()})


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--now", type=int, default=None)
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("sweep")
    sub.add_parser("report")
    renew_p = sub.add_parser("renew")
    renew_p.add_argument("kind", choices=["receipt", "handoff"])
    renew_p.add_argument("ident")
    renew_p.add_argument("--reason", required=True)
    close_p = sub.add_parser("close")
    close_p.add_argument("kind", choices=["receipt", "handoff"])
    close_p.add_argument("ident")
    close_p.add_argument("--evidence", required=True)
    args = parser.parse_args(argv)
    now = args.now if args.now is not None else int(os.environ.get("VICHE_OBLIGATION_NOW", time.time()))
    command = args.command or "sweep"
    if command == "sweep":
        print(json.dumps(sweep(now), sort_keys=True))
    elif command == "report":
        print(json.dumps(report(now), sort_keys=True, indent=2))
    elif command == "renew":
        renew(args.kind, args.ident, args.reason, now)
    elif command == "close":
        if args.kind == "receipt":
            close_receipt(args.ident, args.evidence, now)
        elif args.kind == "handoff":
            close_handoff(args.ident, args.evidence, now)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
