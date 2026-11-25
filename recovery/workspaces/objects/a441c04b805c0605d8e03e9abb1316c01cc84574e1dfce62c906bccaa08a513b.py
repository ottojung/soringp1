#!/usr/bin/env python3
"""Durable cross-branch corrective cases, with evidence-based operational closure.

A case is a monitored obligation, NOT a Judiciary verdict or an authorization
to enact law. Observation and routing remain deterministic even if every model
is down. Existing independent Judiciary/Parliament/Executive powers remain.

Two closures exist.

1. Automatic (Founder directive, 2026-11-16): a case whose signal has been
   absent for VICHE_CASE_AUTOCLOSE_CLEAR consecutive observations (default 20,
   about an hour at the three-minute cycle) is closed as `auto_closed` with a
   machine-written closure record naming exactly that evidence. Cases had
   sat open for days at hundreds of clean checks waiting on a Judiciary
   sign-off that consumed model quota and verified nothing the probe had not.
   A re-fire after auto-closure opens a new case and archives the old one.
2. Manual: the Clerk records `verified_closed` after an independent Judiciary
   disposition, with a case-bound closure_evidence artifact; the mechanical
   check below only verifies that artifact is complete and attributed.

Auto-closure is an observation ("the signal stayed clear"), not a finding that
the underlying cause was repaired. The Judiciary may still review any
auto-closed case; it stays listed in the index for that purpose.
"""
import argparse
import json
import os
import pathlib
import tempfile
import time

ROOT = pathlib.Path(os.environ.get("VICHE_STATE_ROOT", "/var/lib/lubko/wd/viche-state"))
STORE = ROOT / "institutional-cases"
CLOSED_STATES = ("verified_closed", "auto_closed")


def autoclose_threshold():
    try:
        value = int(os.environ.get("VICHE_CASE_AUTOCLOSE_CLEAR", "20"))
    except ValueError:
        return 20
    return value if value > 0 else 0  # 0 disables automatic closure


def read(path):
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, ValueError):
        return {}


def atomic(path, item):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".case-", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as handle:
            json.dump(item, handle, sort_keys=True, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def collect():
    incident = read(ROOT / "branches/incident.json")
    signals = set(incident.get("signals", []))
    # A stale health file must NEVER be treated as current proof of operation.
    town = pathlib.Path(os.environ.get("VICHE_TOWN_ROOT", "/var/lib/lubko/wd/viche"))
    laws = (town / "government/LAWS.md").read_text() if (town / "government/LAWS.md").exists() else ""
    import re
    executive = bool(re.search(r"^## Act \d+ — Executive Innovation Office Act \((re-)?enacted ", laws, re.M))
    innovation_path = ("executive/innovation-office/health.json" if executive
                       else "legislature/innovation-centre/health.json")
    innovation = read(ROOT / innovation_path)
    now = int(os.environ.get("VICHE_CASE_NOW", time.time()))
    if innovation and now - innovation.get("observed_at", 0) > 1800:
        signals.add("innovation_stale")
    # A failed office may be masked by a stale or missing branch-health probe;
    # its terminal continuity record remains an independently observable case.
    for office in ("executive", "judiciary", "innovation-centre", "c1a00001"):
        receipt = read(ROOT / ("continuity/reconciliation-" + office + ".json"))
        if receipt.get("state") in ("preparing", "awaiting_reconciliation"):
            verified = read(ROOT / ("continuity/verified-" + office + ".json"))
            valid = (receipt.get("state") == "awaiting_reconciliation"
                and verified.get("previous_agent") == receipt.get("previous_agent")
                and verified.get("successor_agent") == receipt.get("successor_agent")
                and verified.get("verified_by") == "judiciary"
                and verified.get("verification_scope") == "external_effect_reconciled"
                and isinstance(verified.get("evidence_ref"), str)
                and bool(verified["evidence_ref"].strip()))
            if not valid:
                signals.add("continuity_unverified_" + office)
    return now, signals


def owner(signal):
    # The law already authorizes operational continuity under Acts 2/5.
    if signal == "judiciary_mailbox_pending":
        return "judiciary"
    # Changing the offices or statutes requires actual parliamentary action.
    if signal.startswith("innovation_") or signal.startswith("continuity_"):
        return "executive"
    if signal.endswith("_unhealthy") or signal.endswith("_missing") or signal.endswith("_stale"):
        return "executive"
    return "legislature"


def archive_superseded(path, case, now, reason):
    """Keep the old case independently visible when its signal re-fires.

    Use a separate case-bound JSON file rather than a sidecar ledger that the
    existing index cannot see. Never silently overwrite an earlier archive.
    The ordinary index already counts any artifact-less historical closure.
    """
    case_id = case.get("id")
    if not isinstance(case_id, str) or not case_id:
        raise ValueError(f"Cannot archive case without original ID: {path}")
    archived = path.with_name("archive-" + case_id.replace(":", "-") + ".json")
    if archived.exists():
        # A crash after the archive is durable but before the live-case swap
        # must not erase history OR permanently block safe resumption.
        previous = read(archived)
        if previous.get("archive_reason") == reason and all(
            previous.get(key) == value for key, value in case.items()
        ):
            return
        raise FileExistsError(f"Conflicting case archive: {archived}")
    entry = dict(case)
    entry["archived_at"] = now
    entry["archive_reason"] = reason
    atomic(archived, entry)


def reconcile():
    now, signals = collect()
    STORE.mkdir(parents=True, exist_ok=True)
    # Archived cases remain indexed but are not probed as fresh signal names.
    existing = [p for p in sorted(STORE.glob("*.json"))
                if not p.name.startswith("archive-")]
    names = set(signals) | {p.stem for p in existing}
    for signal in sorted(names):
        if (signal.startswith("archive-")
                or not signal.replace("_", "").replace("-", "").isalnum()):
            continue
        path = STORE / (signal + ".json")
        case = read(path)
        # Addendum/evidence files live beside case objects; preserve them but
        # never treat a list-shaped record as a case.
        if not isinstance(case, dict):
            case = {}
        # Refresh the owner on every reconcile. A case created under an older
        # routing map must not keep surfacing to the wrong office after the
        # mapping changes.
        if case:
            case["owner"] = owner(signal)
        if signal in signals:
            if not case or case.get("state") in CLOSED_STATES:
                if case and case.get("state") in CLOSED_STATES:
                    # Archive first: the re-fired instance replaces the live
                    # object, and the prior history must survive the swap.
                    archive_superseded(path, case, now, "re-fire after close")
                case = {
                    "id": f"{signal}:{now}", "signal": signal,
                    "first_seen": now, "state": "open",
                    "clear_observations": 0,
                    "judiciary": "independent_fact_finding_required",
                    "legislature": "consider_evidence_and_legislation_if_needed",
                    "executive": "investigate_and_repair_within_existing_authority",
                    "owner": owner(signal),
                    "closure_rule": CLOSURE_RULE,
                }
            case["last_seen"] = now
            case["observations"] = case.get("observations", 0) + 1
            case["clear_observations"] = 0
        elif case.get("state") == "open":
            # Signal absence is observational data, NEVER a recovery verdict.
            # Keep the obligation visible for an Executive investigation and
            # an independent evidence-based Judiciary disposition. Authorized
            # agents, not this collector, must determine whether it is closed.
            case["clear_observations"] = case.get("clear_observations", 0) + 1
            case["last_clear_observed_at"] = now
            case["closure_rule"] = CLOSURE_RULE
            threshold = autoclose_threshold()
            if threshold and case["clear_observations"] >= threshold:
                case["state"] = "auto_closed"
                case["closed_at"] = now
                case["closure_evidence"] = {
                    "disposition": "auto_clear",
                    "recorded_by": "institutional-cases.py",
                    "basis": "signal absent for %d consecutive observations "
                             "(threshold %d), last seen %s" % (
                                 case["clear_observations"], threshold, case.get("last_seen")),
                    "scope": "observation that the signal stayed clear; not a finding "
                             "that the cause was repaired; Judiciary may still review",
                    "authority": "Founder directive 2026-11-16",
                }
        elif not case:
            continue
        atomic(path, case)
    records = [x for x in (read(p) for p in sorted(STORE.glob("*.json")))
               if isinstance(x, dict) and x.get("id")]
    active = [x for x in records if x.get("state") == "open"]
    # A closed label without a case-bound closure artifact is not resolution.
    # Historical cases closed by the removed absent-signal path stay visible
    # to monitoring and to the responsible office until an authorized
    # reconciliation supplies the evidence. This does not reopen or rewrite
    # any case object, and it does not change open-case dispatch.
    unresolved = [x for x in records if closure_unsubstantiated(x)]
    auto = [x for x in records if x.get("state") == "auto_closed"]
    atomic(STORE / "index.json", {
        "observed_at": now,
        "active": [x["id"] for x in active],
        "count": len(active),
        "unresolved_without_closure_evidence": [
            {"id": x.get("id"), "signal": x.get("signal"), "state": x.get("state"),
             "reason": "verified_closed without a case-bound closure artifact"}
            for x in unresolved],
        "unresolved_without_closure_evidence_count": len(unresolved),
        "auto_closed": [{"id": x.get("id"), "closed_at": x.get("closed_at")} for x in auto],
        "auto_closed_count": len(auto),
        "total_obligations": len(active) + len(unresolved),
        "caveat": "operational health, not proof of delivery; a closed label "
                  "without a case-bound closure artifact is listed as unresolved",
    })
    return active


CLOSURE_RULE = ("closes automatically after %s consecutive clear observations, or "
                "earlier by Clerk record of an independent Judiciary disposition"
                % os.environ.get("VICHE_CASE_AUTOCLOSE_CLEAR", "20"))


def nonempty_text(value):
    return isinstance(value, str) and bool(value.strip())


def closure_unsubstantiated(case):
    """True for a closed case whose closure is not backed by a complete artifact.

    Historical closures from the absent-signal path carry no closure_evidence.
    Closure is a recorded manual decision by the Clerk after an independent
    Judiciary disposition; this is a mechanical completeness check, not proof
    of the disposition's truth. An incomplete or self-declared artifact is not
    resolution.
    """
    if case.get("state") != "verified_closed":
        return False
    evidence = case.get("closure_evidence")
    if not isinstance(evidence, dict) or not evidence:
        return True
    if evidence.get("closure_eligible") is not True:
        return True
    if evidence.get("verified_by") != "judiciary":
        return True
    if evidence.get("recorded_by") != "clerk":
        return True
    if evidence.get("disposition") not in ("confirmed_resolved", "superseded", "withdrawn"):
        return True
    return not all(nonempty_text(evidence.get(key))
                   for key in ("verifier", "evidence_ref"))


def report():
    return [x for x in (read(p) for p in sorted(STORE.glob("*.json")))
            if isinstance(x, dict) and x.get("id") and x.get("state") == "open"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=("reconcile", "report"))
    args = parser.parse_args()
    cases = reconcile() if args.operation == "reconcile" else report()
    print(json.dumps({
        "open_cases": cases,
        "rule": "Judiciary independently investigates; Parliament decides legal changes; "
                "Executive repairs within existing authority and implements ratified changes. "
                "Never close for agent activity, a comment, or a PR. A case whose "
                "signal stays clear for the configured number of observations closes "
                "automatically (Founder directive 2026-11-16).",
    }, separators=(",", ":")))
