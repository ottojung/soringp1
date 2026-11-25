#!/usr/bin/env python3
"""Read-only Executive diagnostic for the Billy SoringP1 research frontier.

Observations are not proof that any mathematical claim was completed. The
Executive independently verifies current Antonina and board status before
launching or reassigning research. No worker caps or model selection here.
"""
import json
import os
from pathlib import Path
import time


def snapshot(path, now=None):
    now = time.time() if now is None else now
    try:
        data = json.loads(Path(path).read_text())
        if not isinstance(data, dict) or not isinstance(data.get("fronts"), list):
            raise ValueError("invalid frontier-ledger schema")
        fronts = data["fronts"]
        if not all(isinstance(x, dict) and isinstance(x.get("status"), str)
                   and isinstance(x.get("id"), str) for x in fronts):
            raise ValueError("invalid research front")
    except (OSError, ValueError, TypeError) as exc:
        return {
            "status": "unavailable",
            "reason": type(exc).__name__,
            "action": "inspect the Billy research ledger and managed agent inventory; do not infer zero work",
        }

    counts = {k: sum(f["status"] == k for f in fronts)
              for k in ("ready", "running", "launching", "investigated", "blocked")}
    curator = data.get("curator")
    if not isinstance(curator, dict):
        curator = {}
    remaining = counts["ready"] + counts["running"] + counts["launching"]
    curating = bool(curator.get("agent_id"))
    # The research ledger may retain historical exit_state values recorded
    # before Antonina renamed succeeded to clearexit. Only the ledger needs
    # historical interpretation; current Antonina statuses use clearexit.
    empty_curation = (curator.get("exit_state") in ("clearexit", "succeeded")
                      and curator.get("added") == 0)
    incomplete = [
        f["id"] for f in fronts
        if f["status"] == "blocked" and
        (not f.get("finding_unverified", "").strip()
         or f.get("finding_unverified") == "No final text; audit needed")
    ]
    if remaining:
        status = "fronts_claimed_or_ready_not_verified"
    elif curating:
        status = "curation_running_not_verified"
    elif empty_curation:
        status = "depleted_after_empty_curation"
    else:
        status = "depleted_or_unavailable_curation"
    last = curator.get("last_finished_at")
    age = (max(0, int(now - last)) if isinstance(last, (int, float)) else None)
    return {
        "status": status,
        "fronts_total": len(fronts),
        "counts": counts,
        "curator": {"state": ("running" if curating else curator.get("exit_state", "unknown")),
                    "new_fronts": curator.get("added"), "last_finished_age_seconds": age},
        "blocked_without_final_finding": incomplete[:12],
        "action": ("Verify current live agents and originating SoringP1 #301/GitHub issues; "
                   "if theorems remain open and no substantive frontier is active, "
                   "seek independently falsifiable NEW research directions from "
                   "actual mathematical obstacles and literature, or record why a "
                   "candidate is unsuitable; never manufacture busywork"),
        "caveat": "Ledger and agent completions are not verified mathematical results; no numerical worker cap.",
    }


def main():
    path = os.environ.get(
        "SORING_FRONTIER_STATE",
        str(Path.home() / ".local/state/soringp1/frontier-ledger.json"),
    )
    print(json.dumps(snapshot(path), sort_keys=True))


if __name__ == "__main__":
    main()
