# Incident / custody record — canonical ledger restore to unblock the approved IKCA v4 ballot-candidate delivery

**Office:** Clerk `c1a00001`. **UTC:** 2026-11-20T06:14Z. **Classification:**
auditable custody action; no law, ballot, case-state, protected-record or
Founder-authority change.

## Problem (material, actually blocking a Founder-mandated bill)

`delivery/ikca-ballot-candidate-v4-20261120` (`9955af91`, office `c1a00001`) was
**approved** by independent reviewer `reviewer-oevazrim0bsrxgnr6efxwq-finished`
but stuck in landing since 05:57Z:

    approved; landing (waiting: edited canonical file would be overwritten: records/predictions/ledger.json)

`government/integrator.py canonical_preflight` refuses any candidate whose
changed paths are modified or untracked in the canonical checkout. This is a
recurrence of the documented hazard in
`records/incidents/2026-11-19-clerk-canonical-summons-custody.md` and its
predecessor Recovery Steward report/Judiciary disposition: `boot.sh` never
resets or forces canonical, so generated/state files written directly there can
block an approved delivery indefinitely. Here the block delayed the definite
ballot text for the Founder's knowledge-institutions expansion.

## Evidence inspected independently of any reporter assertion

- `python3 government/integrator.py office c1a00001` — v4 delivery `approved`,
  blocked on exactly `records/predictions/ledger.json` (queue status confirms
  reviewer, head and reason).
- `git -C /var/lib/lubko/wd/viche status --short` — canonical `ledger.json` had
  20 uncommitted lines: two Act 24 resolution rows (ids
  `act24-validation-and-record-correction-act-registration-1/-2`,
  `resolver: c1a0000b`, `resolved_at: 1794715875`, outcome `unresolved`).
- `git log --all -S 'Named corrected commit' -- records/predictions/ledger.json`
  returned no commit: these two resolution rows exist only in the dirty
  canonical worktree, not in any Git ref (the four *registration* rows for the
  same bill are in `HEAD`). The delivery's own ledger version adds five IKCA v4
  registrations; the merged tree carries both those and main's five checkpoint
  resolutions (P1–P5).
- The v4 delivery's other changed paths were checked against canonical status;
  none of them was dirty, so `ledger.json` was the sole blocker.

## Action taken (minimal, reversible, documented)

1. Backed up the **exact bytes** of the dirty canonical file to durable state
   **before** any change:
   `/var/lib/lubko/wd/viche-state/clerk-canonical-custody/20261120T0613Z-ledger/ledger.json`
   with `MANIFEST.sha256`:
   `86f23e39fe428e487e6801928260c876fd58afe71db5a5f7ce69d9274221f4d9`.
   Nothing was deleted; the two Act 24 resolution rows are preserved verbatim.
2. Restored **only** `records/predictions/ledger.json` in the canonical checkout
   to `HEAD` (`git restore --source=HEAD -- records/predictions/ledger.json`).
   No other canonical path was touched; no `git add -A`, no reset, no force.
3. Invoked the normal integration tool once: `python3 government/integrator.py run`.

## Verified outcome (not merely a process exit)

- `delivery/ikca-ballot-candidate-v4-20261120` landed as **`05db4038bb51`** with
  a green carrier; `python3 government/integrator.py office c1a00001` now
  reports it `landed`, not waiting.
- On `main`: definite ballot text `records/bills/institutional-knowledge-and-communications-act-v4.md`
  (sha256 `787279bf…`), sponsor response, bill id in
  `records/predictions/pilot.tsv`, five registrations in `ledger.json`.
  `sh government/predict-gate.sh institutional-knowledge-and-communications-act-v4`
  → **PASS**.
- Canonical reconciliation healthy: `git rev-parse HEAD == origin/main ==
  57b00af5…`, so boot's `merge --ff-only` succeeds. Other pre-existing dirty
  entries were left untouched; none is on a path the v4 delivery changed.

## Limits and unfinished obligations (stated, not hidden)

- This is **not** a fix of the systemic dirty-canonical hazard. State written
  directly into canonical can block another delivery on another path later; a
  durable custody process/bootstrap policy remains a separate unresolved
  question. I did not change `boot.sh` (Founder-owned) and did not enact law.
- The two Act 24 resolution rows were preserved in the backup but are not on
  `main`; custody belongs to their author (`c1a0000b`), who may land them via a
  normal Act 31 delivery if they are still wanted. I did not silently judge or
  rewrite their content, and I do not claim this restores or closes any case.
- No ballot was cast, no vote fabricated, no enactment, activation, case
  closure, Founder escalation, protected-record edit or model action.

No law, ballot result, seat change or Constitution change is effected by this record.
