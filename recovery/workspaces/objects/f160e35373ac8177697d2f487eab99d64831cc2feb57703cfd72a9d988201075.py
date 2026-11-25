#!/usr/bin/env python3
"""Act 22 §3.3 — deterministic calibration scorer.

Reads the append-only ledger (records/predictions/ledger.json), recomputes each
entry's content hash (§3.5 integrity), and writes the derived, regenerated
records/predictions/calibration.json each cycle. It computes, per §3.3: Brier
score (per prediction and aggregate); Brier skill score against the
climatological (base-rate) predictor, reporting BOTH the always-0.5 baseline and
the base-rate baseline; log score; reliability/calibration; discrimination;
resolution coverage; and per-author and aggregate figures. Act 20 §7 P1–P5 are
reported in a separate "review_checkpoint" block (Act 22 §9) so the two
instruments do not double-count. The same-model / small-sample limitations are
reported, not hidden.

Usage: predict-scorer.py [--now EPOCH]
Exit 0 on success (defects are reported in the output, not by exit code).
"""
import argparse
import datetime
import hashlib
import json
import math
import os
import time
from pathlib import Path

SCHEMA = "act22-calibration-v1"
ACT20_CHECKPOINTS = [
    {"id": "P1", "label": "at least one instrument fails a known answer (detector test P1a)"},
    {"id": "P2", "label": "aggregate measured FP > 0 and TP < 1.0 over a non-trivial archive"},
    {"id": "P3", "label": "a material rate change is detected after an instrument change (drift)"},
    {"id": "P4", "label": "the archive grows >=1 verified case per measurement window"},
    {"id": "P5", "label": "the report->measurement interface is delivered"},
]


def town_root() -> Path:
    return Path(os.environ.get("VICHE_TOWN_ROOT", "/var/lib/lubko/wd/viche"))


def content_hash(entry: dict) -> str:
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
    canon = {key: resolution.get(key) for key in (
        "id", "outcome", "resolver", "evidence_citation", "evidence_at",
        "resolved_at", "reason")}
    blob = json.dumps(canon, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(blob).hexdigest()


def mean(xs):
    return (sum(xs) / len(xs)) if xs else None


def due_epoch(value):
    return int(datetime.datetime.strptime(value, "%Y-%m-%d").replace(
        tzinfo=datetime.timezone.utc).timestamp())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--now", type=int, default=None)
    a = ap.parse_args()
    now = a.now if a.now is not None else int(time.time())

    root = town_root()
    pred = root / "records/predictions"
    ledger_p = Path(os.environ.get("VICHE_PREDICT_LEDGER", str(pred / "ledger.json")))
    out_p = Path(os.environ.get("VICHE_PREDICT_CALIBRATION", str(pred / "calibration.json")))
    rc_p = pred / "review-checkpoint.json"

    ledger = json.loads(ledger_p.read_text()) if ledger_p.exists() else {"entries": [], "resolutions": []}
    entries = ledger.get("entries", [])
    resolutions = ledger.get("resolutions", [])
    res_by_id = {}
    for r in resolutions:
        res_by_id.setdefault(r.get("id"), r)

    defects = []
    seen = set()
    invalid_entry_ids = set()
    for e in entries:
        if e.get("id") in seen:
            defects.append({"id": e.get("id"), "defect": "duplicate_entry_id"})
            invalid_entry_ids.add(e.get("id"))
        seen.add(e.get("id"))
        if e.get("content_hash") != content_hash(e):
            defects.append({"id": e.get("id"), "defect": "content_hash_mismatch"})
            invalid_entry_ids.add(e.get("id"))
    duplicate_resolution_ids = set()
    for eid in set(r.get("id") for r in resolutions):
        if sum(r.get("id") == eid for r in resolutions) > 1:
            defects.append({"id": eid, "defect": "duplicate_resolution"})
            duplicate_resolution_ids.add(eid)
    invalid_resolution_ids = set()
    for r in resolutions:
        want = resolution_hash(r)
        if r.get("content_hash") != want:
            defects.append({"id": r.get("id"),
                            "defect": "resolution_content_hash_mismatch",
                            "recorded": r.get("content_hash"),
                            "recomputed": want})
            invalid_resolution_ids.add(r.get("id"))

    registered = [e for e in entries if e.get("kind") == "registration" and e.get("status") == "registered"]
    rejected = [e for e in entries if e.get("kind") == "rejection"]

    scored, unresolved, due, due_unresolved = [], [], [], []
    scored_ids, unresolved_ids = set(), set()
    for e in registered:
        if (e.get("id") in invalid_entry_ids
                or e.get("id") in duplicate_resolution_ids):
            continue
        r = res_by_id.get(e.get("id"))
        rd = str(e.get("resolution_date", ""))
        try:
            is_due = due_epoch(rd) <= now
        except (TypeError, ValueError):
            defects.append({"id": e.get("id"), "defect": "invalid_resolution_date"})
            continue
        if not (e.get("evidence_source") or "").strip():
            defects.append({"id": e.get("id"), "defect": "missing_evidence_source"})
            continue
        if is_due:
            due.append(e)
        if e.get("id") in invalid_resolution_ids:
            if is_due:
                due_unresolved.append(e.get("id"))
            continue
        if r is None:
            if is_due:
                due_unresolved.append(e.get("id"))
            continue
        resolved_at = int(r.get("resolved_at", 0))
        if resolved_at < due_epoch(rd):
            defects.append({"id": e.get("id"), "defect": "resolution_before_due_date"})
            continue
        if r.get("resolver") == e.get("author"):
            defects.append({"id": e.get("id"), "defect": "author_self_resolved"})
        elif resolved_at < int(e.get("registered_at", 0)):
            defects.append({"id": e.get("id"), "defect": "resolution_timestamp_precedes_registration"})
        elif not (r.get("evidence_citation") or "").strip():
            defects.append({"id": e.get("id"), "defect": "missing_resolution_evidence"})
        elif r.get("outcome") == "unresolved":
            if not (r.get("reason") or "").strip():
                defects.append({"id": e.get("id"), "defect": "unresolved_without_reason"})
            else:
                unresolved.append(e)
                unresolved_ids.add(e.get("id"))
        elif r.get("outcome") in ("true", "false"):
            try:
                evidence_at = int(r.get("evidence_at"))
                if evidence_at <= int(e.get("registered_at", 0)):
                    raise ValueError("outcome_evidence_not_after_registration")
                if evidence_at > resolved_at:
                    raise ValueError("outcome_evidence_after_resolution")
                scored.append((e, r))
                scored_ids.add(e.get("id"))
            except (TypeError, ValueError) as err:
                reason = str(err) or "missing_outcome_evidence_timestamp"
                defects.append({"id": e.get("id"), "defect": reason})
        else:
            defects.append({"id": e.get("id"), "defect": "invalid_resolution_outcome"})

    n_scored = len(scored)
    outcomes = [1.0 if r.get("outcome") == "true" else 0.0 for _, r in scored]
    probs = [float(e.get("probability")) for e, _ in scored]

    brier = [(p - o) ** 2 for p, o in zip(probs, outcomes)]
    brier_agg = mean(brier)
    base_rate = mean(outcomes)
    brier_base = (base_rate * (1 - base_rate)) if base_rate is not None else None
    skill_base = None
    if brier_agg is not None and brier_base is not None:
        # The base-rate predictor is perfect when every observed outcome has
        # the same value (baseline Brier=0). Skill is undefined then; report
        # null rather than divide by zero or imply a finite comparison.
        if brier_base > 0:
            skill_base = 1 - brier_agg / brier_base
    brier_05 = 0.25
    skill_05 = (1 - brier_agg / brier_05) if brier_agg is not None else None

    logs = []
    for p, o in zip(probs, outcomes):
        logs.append(-(o * math.log(p) + (1 - o) * math.log(1 - p)))
    log_agg = mean(logs)

    bins = [[0.0, 0.1], [0.1, 0.2], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5],
            [0.5, 0.6], [0.6, 0.7], [0.7, 0.8], [0.8, 0.9], [0.9, 1.0]]
    reliability = []
    for lo, hi in bins:
        idx = [i for i, p in enumerate(probs) if (p >= lo and (p < hi or (hi == 1.0 and p <= hi)))]
        if not idx:
            continue
        mp = mean([probs[i] for i in idx])
        of = mean([outcomes[i] for i in idx])
        reliability.append({"bin": [lo, hi], "count": len(idx),
                            "mean_predicted": round(mp, 4), "observed_frequency": round(of, 4)})

    high = [o for p, o in zip(probs, outcomes) if p >= 0.8]
    low = [o for p, o in zip(probs, outcomes) if p <= 0.2]
    discrimination = {
        "high_conf_n": len(high), "high_conf_accuracy": (round(mean(high), 4) if high else None),
        "low_conf_n": len(low), "low_conf_accuracy": (round(1 - mean(low), 4) if low else None),
    }

    per_author = {}
    for e in registered:
        au = e.get("author", "?")
        d = per_author.setdefault(au, {"registered": 0, "scored": [], "unresolved": 0,
                                       "due_unresolved": 0})
        d["registered"] += 1
        r = res_by_id.get(e.get("id"))
        if r is None or e.get("id") in invalid_resolution_ids:
            if e.get("resolution_date", "") <= time.strftime("%Y-%m-%d", time.gmtime(now)):
                d["due_unresolved"] += 1
        elif e.get("id") in unresolved_ids:
            d["unresolved"] += 1
        elif e.get("id") in scored_ids:
            d["scored"].append((e, r))

    def score_group(group):
        gp = [float(e.get("probability")) for e, _ in group]
        go = [1.0 if r.get("outcome") == "true" else 0.0 for _, r in group]
        gb = [(p - o) ** 2 for p, o in zip(gp, go)]
        gm = mean(gb)
        gr = mean(go)
        gb_rate = gr * (1 - gr) if gr is not None else None
        gl = mean([-(o * math.log(p) + (1 - o) * math.log(1 - p))
                   for p, o in zip(gp, go)])
        high = [o for p, o in zip(gp, go) if p >= 0.8]
        low = [o for p, o in zip(gp, go) if p <= 0.2]
        rel = []
        for lo, hi in bins:
            ids = [i for i, p in enumerate(gp)
                   if p >= lo and (p < hi or (hi == 1.0 and p <= hi))]
            if ids:
                rel.append({"bin": [lo, hi], "count": len(ids),
                            "mean_predicted": round(mean([gp[i] for i in ids]), 4),
                            "observed_frequency": round(mean([go[i] for i in ids]), 4)})
        return {
            "scored": len(group),
            "brier": round(gm, 6) if gm is not None else None,
            "baselines": {
                "always_0_5": {"brier": 0.25,
                               "skill_vs_ledger": round(1 - gm / 0.25, 6) if gm is not None else None},
                "base_rate": {"p": round(gr, 6) if gr is not None else None,
                              "brier": round(gb_rate, 6) if gb_rate is not None else None,
                              "skill_vs_ledger": (round(1 - gm / gb_rate, 6)
                                                  if gm is not None and gb_rate else None)},
            },
            "log_score": round(gl, 6) if gl is not None else None,
            "reliability": rel,
            "discrimination": {
                "high_conf_n": len(high),
                "high_conf_accuracy": round(mean(high), 4) if high else None,
                "low_conf_n": len(low),
                "low_conf_accuracy": round(1 - mean(low), 4) if low else None,
            },
        }

    authors = []
    for au, d in sorted(per_author.items()):
        metrics = score_group(d["scored"])
        covered = len(d["scored"]) + d["unresolved"]
        metrics.update({"author": au, "registered": d["registered"],
                        "unresolved": d["unresolved"],
                        "due_unresolved": d["due_unresolved"],
                        "coverage": round(covered / d["registered"], 4)
                        if d["registered"] else None,
                        "observed_true_rate": round(mean([
                            1.0 if r.get("outcome") == "true" else 0.0
                            for _, r in d["scored"]]), 4)
                        if d["scored"] else None})
        authors.append(metrics)

    # Resolution coverage counts true/false and explicitly unresolved
    # resolutions; due-but-not-yet-resolved entries remain uncovered.
    coverage = (len(scored) + len(unresolved)) / len(registered) if registered else None

    # Act 20 §7 checkpoints live in the ledger as carried-forward statutory
    # records but are deliberately excluded from Brier scoring.
    checkpoint_entries = [e for e in entries
                          if e.get("kind") == "review_checkpoint"]
    for e in checkpoint_entries:
        if e.get("content_hash") != content_hash(e):
            defects.append({"id": e.get("id"),
                            "defect": "review_checkpoint_content_hash_mismatch"})
    checkpoint_by_id = {e.get("id"): e for e in checkpoint_entries}
    checkpoints = []
    if rc_p.exists():
        rc = json.loads(rc_p.read_text())
        definitions = rc.get("checkpoints", [])
    else:
        definitions = [dict(c) for c in ACT20_CHECKPOINTS]
    for definition in definitions:
        e = checkpoint_by_id.get(definition.get("id"))
        row = dict(definition)
        row["registered"] = e is not None
        row["resolution"] = "pending"
        if e is not None:
            row.update({"proposition": e.get("proposition"),
                        "resolution_date": e.get("resolution_date"),
                        "evidence_source": e.get("evidence_source"),
                        "author": e.get("author"),
                        "source_ref": e.get("source_ref"),
                        "source_registered_on": e.get("source_registered_on")})
            row["integrity"] = ("clean" if e.get("content_hash") == content_hash(e)
                                else "defect")
        checkpoints.append(row)

    payload = {
        "schema": SCHEMA, "act": 22, "generated_at": now,
        "generated_iso": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
        "generated_by": "government/predict-scorer.py",
        "counts": {
            "registered": len(registered), "rejected": len(rejected),
            "resolved_scored": n_scored, "unresolved": len(unresolved),
            "due": len(due), "due_unresolved": len(due_unresolved),
        },
        "coverage": (round(coverage, 4) if coverage is not None else None),
        "brier": {"aggregate": (round(brier_agg, 6) if brier_agg is not None else None),
                  "per_prediction": [{"id": e.get("id"), "probability": p, "outcome": o,
                                      "brier": round((p - o) ** 2, 6)}
                                     for (e, _), p, o in zip(scored, probs, outcomes)]},
        "baselines": {"always_0_5": {"brier": brier_05,
                                     "skill_vs_ledger": (round(skill_05, 6) if skill_05 is not None else None)},
                      "base_rate": {"p": (round(base_rate, 6) if base_rate is not None else None),
                                    "brier": (round(brier_base, 6) if brier_base is not None else None),
                                    "skill_vs_ledger": (round(skill_base, 6) if skill_base is not None else None)}},
        "log_score": {"aggregate": (round(log_agg, 6) if log_agg is not None else None),
                      "per_prediction": [{"id": e.get("id"), "log": round(v, 6)}
                                         for (e, _), v in zip(scored, logs)]},
        "reliability": reliability,
        "discrimination": discrimination,
        "per_author": authors,
        "review_checkpoint": {
            "instrument": "Act 20 §7",
            "note": ("carried into the Act 22 ledger (Act 22 §9); review checkpoints, "
                     "not Brier predictions — reported separately so the instruments "
                     "do not double-count"),
            "checkpoints": checkpoints,
        },
        "integrity": {"defects": defects, "clean": not defects},
        "limitations": [
            "single substrate (same model) — per-author differences are within-substrate",
            "no causal identification",
            "small samples early in the window",
            "self-fulfilling/self-defeating predictions limited but not eliminated",
            "resolver independence is procedural, not substantive",
            "descriptive of past accuracy, not a guarantee of future accuracy",
        ],
    }
    out_p.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    tmp.replace(out_p)
    print("predict-scorer: %d registered, %d scored, coverage=%s, Brier=%s, skill(base)=%s"
          % (len(registered), n_scored, payload["coverage"],
             payload["brier"]["aggregate"], payload["baselines"]["base_rate"]["skill_vs_ledger"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
