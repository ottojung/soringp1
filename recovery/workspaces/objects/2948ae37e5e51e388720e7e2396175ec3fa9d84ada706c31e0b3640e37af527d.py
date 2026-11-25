#!/usr/bin/env python3
"""Act 22 (Pre-Registered Prediction and Calibration Act) — ledger operations.

The Executive implements the mechanism (Acts 2/6); the Clerk exercises the
gatekeeper (§2), resolver (§3) and publisher (§5) duties. This file is the
deterministic, append-only ledger writer/reader. It records registrations,
rejections (no named evidence source), independent resolutions, and runs the
per-entry content-hash integrity check the Judiciary can run each window (§3.5,
§12). It performs no policy: it applies the recorded rules verbatim.

Ledger: records/predictions/ledger.json — an append-only list of immutable
entries. A correction is a NEW entry citing the original (§3.5); an entry is
never edited or deleted. The file is rewritten only to append.

Resolution records are immutable append-only events too. Their canonical
content hash binds outcome, resolver, evidence citation/timestamp and the
resolution timestamp, so an edit cannot silently change a score. Act 20's P1–P5
are carried as separately hashed review-checkpoint entries, not Brier-scored
registrations; their provenance, original review date and named evidence source
are retained in the same ledger.

Content hash (§3.5): sha256 over the canonical JSON of the registered
prediction's immutable content — bill id, proposition, probability, resolution
date, evidence source, author — computed at registration and committed before
the outcome-establishing evidence exists. Binding the bill id prevents a valid
entry from being reassigned to a different bill. Rejections carry a hash over
their own immutable content so the same integrity check covers them.

Usage:
  predict-ledger.py register --bill ID --proposition TEXT --probability P \
      --resolution-date DATE --evidence SOURCE --author SEAT [--cites ENTRY_ID]
  predict-ledger.py reject   --bill ID --proposition TEXT --author SEAT --reason TEXT
  predict-ledger.py resolve  --id ENTRY_ID --outcome true|false|unresolved \
      --resolver SEAT --evidence CITATION [--evidence-at EPOCH] [--reason TEXT]
  predict-ledger.py verify
  predict-ledger.py show

Exit: register/resolve 0 ok, 1 rejected/refused; verify 0 clean, 1 defect(s).
"""
import argparse
import datetime
import hashlib
import json
import os
import sys
import time
from pathlib import Path

SCHEMA = "act22-ledger-v1"
FALLBACK_RESOLVER = "c1a0000b"


def town_root() -> Path:
    return Path(os.environ.get("VICHE_TOWN_ROOT", "/var/lib/lubko/wd/viche"))


def ledger_path() -> Path:
    return Path(os.environ.get(
        "VICHE_PREDICT_LEDGER", str(town_root() / "records/predictions/ledger.json")))


def now_epoch() -> int:
    env = os.environ.get("VICHE_PREDICT_NOW")
    if env is not None:
        try:
            return int(env)
        except ValueError:
            pass
    return int(time.time())


def iso(epoch: int) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch))


def date_epoch(value: str) -> int:
    day = datetime.datetime.strptime(value, "%Y-%m-%d").replace(
        tzinfo=datetime.timezone.utc)
    return int(day.timestamp())


def load(path: Path) -> dict:
    if not path.exists():
        return {"schema": SCHEMA, "entries": [], "resolutions": []}
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise SystemExit("predict-ledger: ledger is not an object")
    data.setdefault("schema", SCHEMA)
    data.setdefault("entries", [])
    data.setdefault("resolutions", [])
    return data


def save(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n")
    tmp.replace(path)


def content_hash(entry: dict) -> str:
    """Canonical content hash over the immutable prediction fields (§3.5)."""
    if entry.get("kind") == "rejection":
        canon = {"kind": "rejection", "bill_id": entry.get("bill_id", ""),
                 "proposition": entry.get("proposition", ""),
                 "author": entry.get("author", ""), "reason": entry.get("reason", ""),
                 "registered_at": entry.get("registered_at")}
    elif entry.get("kind") == "review_checkpoint":
        canon = {key: entry.get(key) for key in (
            "kind", "id", "proposition", "resolution_date", "evidence_source",
            "author", "source_ref", "source_registered_on", "recorded_at")}
    else:
        canon = {"bill_id": entry.get("bill_id", ""),
                 "proposition": entry.get("proposition", ""),
                  "probability": entry.get("probability"),
                  "resolution_date": entry.get("resolution_date", ""),
                  "evidence_source": entry.get("evidence_source", ""),
                 "author": entry.get("author", ""),
                 "registered_at": entry.get("registered_at")}
    blob = json.dumps(canon, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(blob).hexdigest()


def resolution_hash(resolution: dict) -> str:
    """Hash the immutable resolution event separately from its prediction."""
    canon = {key: resolution.get(key) for key in (
        "id", "outcome", "resolver", "evidence_citation", "evidence_at",
        "resolved_at", "reason")}
    blob = json.dumps(canon, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(blob).hexdigest()


def next_id(data: dict, bill_id: str, kind: str) -> str:
    n = 1 + sum(1 for e in data["entries"]
                if e.get("bill_id") == bill_id and e.get("kind") == kind)
    return "%s-%s-%d" % (bill_id, kind, n)


def cmd_register(a) -> int:
    path = ledger_path()
    data = load(path)
    if not (a.evidence or "").strip():
        # §3.1: a prediction lacking a named evidence source is rejected and the
        # rejection recorded (anti-vagueness signal, §3.6).
        entry = {"id": next_id(data, a.bill, "rejection"), "kind": "rejection",
                 "bill_id": a.bill, "proposition": a.proposition, "author": a.author,
                 "reason": "no named evidence source", "status": "rejected",
                 "registered_at": now_epoch()}
        entry["registered_iso"] = iso(entry["registered_at"])
        entry["content_hash"] = content_hash(entry)
        data["entries"].append(entry)
        save(path, data)
        print("predict-ledger: REJECTED (no named evidence source) %s" % entry["id"])
        return 1
    try:
        p = float(a.probability)
    except (TypeError, ValueError):
        print("predict-ledger: probability must be a number in (0,1)", file=sys.stderr)
        return 2
    if not (0.0 < p < 1.0):
        print("predict-ledger: probability must be in (0,1)", file=sys.stderr)
        return 2
    try:
        due_at = date_epoch(a.resolution_date)
    except (TypeError, ValueError):
        print("predict-ledger: resolution date must be YYYY-MM-DD", file=sys.stderr)
        return 2
    registered_at = now_epoch()
    if registered_at >= due_at:
        print("predict-ledger: registration must precede its resolution date",
              file=sys.stderr)
        return 1
    entry = {"id": next_id(data, a.bill, "registration"), "kind": "registration",
             "bill_id": a.bill, "proposition": a.proposition, "probability": p,
             "resolution_date": a.resolution_date, "evidence_source": a.evidence,
             "author": a.author, "self_reference": bool(a.self_reference),
              "status": "registered", "registered_at": registered_at,
              "registered_iso": iso(registered_at)}
    if a.cites:
        entry["cites"] = a.cites
    entry["content_hash"] = content_hash(entry)
    data["entries"].append(entry)
    save(path, data)
    print("predict-ledger: registered %s (hash %s)" % (entry["id"], entry["content_hash"]))
    return 0


def cmd_resolve(a) -> int:
    path = ledger_path()
    data = load(path)
    target = next((e for e in data["entries"] if e.get("id") == a.id), None)
    if target is None:
        print("predict-ledger: no such entry: %s" % a.id, file=sys.stderr)
        return 2
    if target.get("kind") != "registration":
        print("predict-ledger: entry is not a registration: %s" % a.id, file=sys.stderr)
        return 2
    # §3.2: the author may not resolve their own prediction.
    if a.resolver == target.get("author"):
        print("predict-ledger: REFUSED — resolver %s is the author of %s "
              "(fallback resolver is %s)" % (a.resolver, a.id, FALLBACK_RESOLVER),
              file=sys.stderr)
        return 1
    if any(r.get("id") == a.id for r in data["resolutions"]):
        print("predict-ledger: already resolved: %s" % a.id, file=sys.stderr)
        return 1
    if not (a.evidence or "").strip():
        print("predict-ledger: every resolution requires an evidence citation",
              file=sys.stderr)
        return 2
    if a.outcome == "unresolved" and not (a.reason or "").strip():
        print("predict-ledger: unresolved requires a reason", file=sys.stderr)
        return 2
    try:
        due_at = date_epoch(target.get("resolution_date", ""))
    except (TypeError, ValueError):
        print("predict-ledger: invalid registered resolution date", file=sys.stderr)
        return 2
    resolved_at = now_epoch()
    if resolved_at < due_at:
        print("predict-ledger: REFUSED — prediction is not due until %s"
              % target.get("resolution_date"), file=sys.stderr)
        return 2
    evidence_at = None
    if a.outcome in ("true", "false"):
        try:
            evidence_at = int(a.evidence_at)
        except (TypeError, ValueError):
            print("predict-ledger: scored resolution requires --evidence-at EPOCH",
                  file=sys.stderr)
            return 2
        if evidence_at <= int(target.get("registered_at", 0)):
            print("predict-ledger: outcome evidence must follow registration",
                  file=sys.stderr)
            return 2
        if evidence_at > resolved_at:
            print("predict-ledger: outcome evidence timestamp is in the future",
                  file=sys.stderr)
            return 2
    res = {"id": a.id, "outcome": a.outcome, "resolver": a.resolver,
           "evidence_citation": a.evidence, "evidence_at": evidence_at,
           "resolved_at": resolved_at,
           "resolved_iso": iso(resolved_at)}
    if a.reason:
        res["reason"] = a.reason
    res["content_hash"] = resolution_hash(res)
    if res["resolved_at"] < int(target.get("registered_at", 0)):
        res["defect"] = "resolution_timestamp_precedes_registration"
    data["resolutions"].append(res)
    save(path, data)
    print("predict-ledger: resolved %s -> %s by %s" % (a.id, a.outcome, a.resolver))
    return 0


def cmd_verify(a) -> int:
    path = ledger_path()
    data = load(path)
    defects = []
    seen = set()
    for e in data["entries"]:
        eid = e.get("id")
        if eid in seen:
            defects.append({"id": eid, "defect": "duplicate_entry_id"})
        seen.add(eid)
        want = content_hash(e)
        if e.get("content_hash") != want:
            defects.append({"id": eid, "defect": "content_hash_mismatch",
                            "recorded": e.get("content_hash"), "recomputed": want})
        if e.get("kind") == "registration":
            if not str(e.get("evidence_source", "")).strip():
                defects.append({"id": eid, "defect": "missing_evidence_source"})
            try:
                if not (0.0 < float(e.get("probability")) < 1.0):
                    raise ValueError
                date_epoch(e.get("resolution_date", ""))
                int(e.get("registered_at"))
            except (TypeError, ValueError):
                defects.append({"id": eid, "defect": "invalid_registration_fields"})
    known = {e.get("id"): e for e in data["entries"] if e.get("kind") == "registration"}
    for r in data["resolutions"]:
        want = resolution_hash(r)
        if r.get("content_hash") != want:
            defects.append({"id": r.get("id"), "defect": "resolution_content_hash_mismatch",
                            "recorded": r.get("content_hash"), "recomputed": want})
        if r.get("defect"):
            defects.append({"id": r.get("id"), "defect": r["defect"]})
        target = known.get(r.get("id"))
        if target is None:
            defects.append({"id": r.get("id"), "defect": "resolution_without_registration"})
        elif r.get("resolver") == target.get("author"):
            defects.append({"id": r.get("id"), "defect": "author_self_resolved"})
        elif int(r.get("resolved_at", 0)) < int(target.get("registered_at", 0)):
            defects.append({"id": r.get("id"), "defect": "resolution_timestamp_precedes_registration"})
        else:
            if not (r.get("evidence_citation") or "").strip():
                defects.append({"id": r.get("id"), "defect": "missing_resolution_evidence"})
            if r.get("outcome") == "unresolved" and not (r.get("reason") or "").strip():
                defects.append({"id": r.get("id"), "defect": "unresolved_without_reason"})
            if r.get("outcome") in ("true", "false"):
                try:
                    evidence_at = int(r.get("evidence_at"))
                    if evidence_at <= int(target.get("registered_at", 0)):
                        defects.append({"id": r.get("id"), "defect": "outcome_evidence_not_after_registration"})
                    if evidence_at > int(r.get("resolved_at", 0)):
                        defects.append({"id": r.get("id"), "defect": "outcome_evidence_after_resolution"})
                except (TypeError, ValueError):
                    defects.append({"id": r.get("id"), "defect": "missing_outcome_evidence_timestamp"})
            try:
                if int(r.get("resolved_at", 0)) < date_epoch(target.get("resolution_date", "")):
                    defects.append({"id": r.get("id"), "defect": "resolution_before_due_date"})
            except (TypeError, ValueError):
                defects.append({"id": r.get("id"), "defect": "invalid_resolution_date"})
    resolution_ids = [r.get("id") for r in data["resolutions"]]
    for eid in set(resolution_ids):
        if resolution_ids.count(eid) > 1:
            defects.append({"id": eid, "defect": "duplicate_resolution"})
    out = {"schema": SCHEMA, "entries": len(data["entries"]),
           "resolutions": len(data["resolutions"]), "defects": defects}
    print(json.dumps(out, sort_keys=True))
    if defects:
        print("predict-ledger: INTEGRITY DEFECTS: %d" % len(defects), file=sys.stderr)
        return 1
    print("predict-ledger: integrity clean (%d entries, %d resolutions)"
          % (len(data["entries"]), len(data["resolutions"])))
    return 0


def cmd_show(a) -> int:
    print(json.dumps(load(ledger_path()), sort_keys=True, indent=2))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Act 22 prediction ledger")
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("register")
    r.add_argument("--bill", required=True)
    r.add_argument("--proposition", required=True)
    r.add_argument("--probability", required=True)
    r.add_argument("--resolution-date", required=True)
    r.add_argument("--evidence", default="")
    r.add_argument("--author", required=True)
    r.add_argument("--self-reference", action="store_true")
    r.add_argument("--cites", default="")
    r.set_defaults(fn=cmd_register)

    j = sub.add_parser("reject")
    j.add_argument("--bill", required=True)
    j.add_argument("--proposition", required=True)
    j.add_argument("--author", required=True)
    j.add_argument("--reason", required=True)
    j.set_defaults(fn=lambda a: _reject(a))

    s = sub.add_parser("resolve")
    s.add_argument("--id", required=True)
    s.add_argument("--outcome", required=True, choices=["true", "false", "unresolved"])
    s.add_argument("--resolver", required=True)
    s.add_argument("--evidence", default="")
    s.add_argument("--evidence-at", default=None,
                   help="outcome evidence timestamp (Unix epoch); required for true/false")
    s.add_argument("--reason", default="")
    s.set_defaults(fn=cmd_resolve)

    c = sub.add_parser("add-review-checkpoint")
    c.add_argument("--id", required=True)
    c.add_argument("--proposition", required=True)
    c.add_argument("--resolution-date", required=True)
    c.add_argument("--evidence", required=True)
    c.add_argument("--author", required=True)
    c.add_argument("--source-ref", required=True)
    c.add_argument("--source-registered-on", required=True)
    c.set_defaults(fn=cmd_add_review_checkpoint)

    sub.add_parser("verify").set_defaults(fn=cmd_verify)
    sub.add_parser("show").set_defaults(fn=cmd_show)

    a = ap.parse_args()
    return a.fn(a)


def _reject(a) -> int:
    path = ledger_path()
    data = load(path)
    entry = {"id": next_id(data, a.bill, "rejection"), "kind": "rejection",
             "bill_id": a.bill, "proposition": a.proposition, "author": a.author,
             "reason": a.reason, "status": "rejected",
             "registered_at": now_epoch(), "registered_iso": iso(now_epoch())}
    entry["content_hash"] = content_hash(entry)
    data["entries"].append(entry)
    save(path, data)
    print("predict-ledger: REJECTED %s (%s)" % (entry["id"], a.reason))
    return 0


def cmd_add_review_checkpoint(a) -> int:
    """Carry a pre-existing statutory checkpoint forward without rescoring it."""
    path = ledger_path()
    data = load(path)
    if any(e.get("kind") == "review_checkpoint" and e.get("id") == a.id
           for e in data["entries"]):
        print("predict-ledger: review checkpoint already present: %s" % a.id,
              file=sys.stderr)
        return 1
    try:
        date_epoch(a.resolution_date)
        datetime.datetime.strptime(a.source_registered_on, "%Y-%m-%d")
    except ValueError:
        print("predict-ledger: checkpoint dates must be YYYY-MM-DD", file=sys.stderr)
        return 2
    entry = {"id": a.id, "kind": "review_checkpoint", "instrument": "act20-review",
             "proposition": a.proposition, "resolution_date": a.resolution_date,
             "evidence_source": a.evidence, "author": a.author,
             "source_ref": a.source_ref,
             "source_registered_on": a.source_registered_on,
             "recorded_at": now_epoch(), "status": "carried_forward_not_brier_scored"}
    entry["content_hash"] = content_hash(entry)
    data["entries"].append(entry)
    save(path, data)
    print("predict-ledger: carried review checkpoint %s from %s" %
          (a.id, a.source_ref))
    return 0


if __name__ == "__main__":
    sys.exit(main())
