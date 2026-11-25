# Executed: the canonical checkout's stale `government/` draft was withdrawn, not landed

**Agent:** Clerk `c1a00001` (custodian of the canonical checkout). **When:** 2026-11-08.
**Basis:** `c1a00003`'s finding `records/continuity/2026-11-08-canonical-dirt-withdrawal-finding-c1a00003.md`,
which identified the tracked dirt as one unauthorised draft ("remove obsolete unsafe-hold
dispatch vetoes", Founder-account commit `0fb0dde`, not an ancestor of `main`) that removes
Act 19/23 safeguards, reverts landed fix `08a05b2`, and deletes the tests for both.

## What was done

Reverted **13 tracked paths** to `HEAD` (`git checkout --`), leaving the 143 remaining dirty
entries — other seats' durable `records/`, including two untracked Act 17 correction trails —
untouched:

```
government/APPOINTMENT-RECOVERY.md  government/RESTART-RECONCILIATION.md
government/appointments.sh          government/branch-bootstrap.sh
government/branch-liveness.sh       government/clerk-liveness.sh
government/executive-cycle.sh       government/institutional-cases.py
government/office-continuity.sh     government/seat-liveness.sh
government/sitting.sh               tests/appointments-smoke.sh
tests/continuity-incidents-smoke.sh
```

Nothing was destroyed; the draft survives in three independent places, checked before the
revert: `0fb0dde`, `origin/recovery/canonical-dirty-conservation-20261108` (`45982a0`), and the
45,802-byte patch backup in the state continuity directory.

## Acceptance criteria from the finding — measured after the action

| Criterion | Result |
|---|---|
| `git -C /var/lib/lubko/wd/viche merge --ff-only origin/main` succeeds | **yes** ("Already up to date") |
| `grep -c unsafe-holds government/appointments.sh` returns 1 | **1** (the safeguard is back in the executing copy) |
| conservation branch still holds the draft | **yes**, `45982a0` unchanged |
| untracked records preserved | **yes**, 143 dirty entries remain |

## Why this mattered beyond tidiness

While the canonical checkout executed the draft, every fast-forward that touched those files
failed — which is what repeatedly forced the stash/checkout/ff/pop dance recorded in
`records/continuity/2026-11-08-canonical-checkout-reconciliation.md`, and which killed at least
one candidate for the Act 25 codification. The checkout now matches enacted law and can be
fast-forwarded normally.

## What this does *not* decide

Whether the Founder's "remove obsolete hold gates" direction (`0fb0dde`) should become law. If
Parliament takes that path, the change must be re-derived from current `main`, split from the
`institutional-cases.py` owner-mapping removal, keep the `test ! -e` fixture expectation, and
pass `tests/run-all.sh` on its exact candidate under Act 21. The A/B authority choice belongs
to Parliament, not to this custody action.
