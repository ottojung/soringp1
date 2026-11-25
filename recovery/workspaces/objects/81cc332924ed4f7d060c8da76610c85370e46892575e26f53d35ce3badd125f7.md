# K1 Disposition — Kawun #181 locked-surface re-pin

**Date:** 2026-10-17T16:03Z
**Seat:** c1a00002 (Executive liaison)
**Status:** BLOCKED — Founder authorization required

## Finding Summary

`ottojung/skrynia-apps` `origin/main` `87cda273` re-pinned `package.json` sha256
in `policy/locked-policy.json` (`78fcf230…` → `2d59cd93…`) without an authorizing
intent change. `package.json` is a Founder-locked surface. The issue's constraint
forbade re-pinning locked policy.

## Disposition

**The Town holds; it may not self-authorize a locked-policy change.**

This finding is consolidated with the pending Founder decision M-013 (Kawun
locked-policy change authorization). The Founder must either:
- **Authorize** the `package.json` locked-surface re-pin (with an explicit intent
  change recorded), or
- **Decline** it, in which case the re-pin must be reverted and the check-gate
  fix delivered without a locked-policy change.

No corrective action has been taken on the Kawun repo. The locked-surface
change remains in place pending Founder decision.

## checkGate.test.ts

`source/kawunapp/tests/policy/checkGate.test.ts` (the non-vacuity guard required
by the issue, present on `release/along-long-namespace` @ `4f8f9675`) is **absent
from `origin/main`**. This is a separate defect from the locked-surface re-pin.
The guard should be delivered to `main` as part of the corrective action, but
only after the locked-surface disposition is resolved.

## Evidence

- `records/OVERSIGHT-FINDING-2026-10-17-kawun-181-locked-policy.md`
- Kawun `AGENTS.md`: "Changing locked policy requires an explicit direct
  user-authorized intent change"
- No intent record exists; 0 `Vitalik` comments on #181

## Required Founder Action

One-line authorization (or decline) for the `package.json` locked-surface
re-pin, consolidated with M-013.
