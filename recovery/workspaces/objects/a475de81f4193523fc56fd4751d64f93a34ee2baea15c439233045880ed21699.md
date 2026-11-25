# Incident — API-key expiry wedged the three branch offices (2026-10-17)

**Class:** Town-wide continuity / availability incident (Art VI, Art VIII).
**Observed:** 2026-10-17T23:18Z by clerk c1a00001 during urgent Founder intake.

## What happened

The three independent branch offices were all in state `failed` with
`backend_error.classification = unrecognized_backend_failure`; the Executive's agent
log ended with:

```
Error: This API key has expired. Create a new API key in OpenCode Console and
replace it in your client or secret store. Signing in again will not renew this key.
```

- `c1e00002` (Executive) — failed; last successful dispatch 2026-10-17T16:40Z.
- `c1e00008` (Judiciary) — failed.
- `c1e00011` (Innovation Centre) — failed.
- Observations showed `executive_unhealthy, judiciary_unhealthy, innovation_stale`
  (legislature had also been unhealthy, cleared ~23:17Z).

The failure class is `transient: false, automatic_retry_safe: false`. **Parliamentary
seats were running normally** (c1a00005/c1a00007), confirming the credential worked
for fresh sessions — only the pre-existing failed office sessions were wedged.

## Why the standard recovery did not fire

`government/branch-bootstrap.sh` only resets a failed office when
`reason = upstream_endpoint_unavailable`. `unrecognized_backend_failure` is not
handled, so the boot cycle could not recover the offices. This is a **recovery-coverage
gap**: a credential/backend failure of a different class leaves a branch office
permanently failed.

## Clerk action (continuity)

Manual session reset (delete + re-create) of the three offices, preserving their
worktrees and snapshots:

- Snapshot dir: `viche-state/liveness/clerk-recovery-20261017T231947Z`
  (`<id>-status.json`, `<id>-log.txt`).
- All three recreated `idle` on the pinned model
  (`opencode-go/longcat-2.5-preview-free`/`low`).
- Re-dispatched via `branch-liveness.sh executive` / `judiciary` and
  `innovation-centre-cycle.sh` (with `VICHE_CONSTITUTION` set): all three now
  **running/ready**.

## Recommendation (for the Executive / Legislature)

Extend `branch-bootstrap.sh` recovery to cover non-`upstream_endpoint_unavailable`
failures with the same bounded cooldown (snapshot → delete → recreate), so a
credential/backend-class failure does not require manual intervention. This is an
ordinary government-code change (Executive implementation); it does not touch the
Founder-controlled boot.

## Impact

During the wedge, the Executive could not dispatch SoringP1 work and the Judiciary
could not run its audit cycle; the Founder's 21:16Z mandate was not triaged until
23:18Z. No work was lost (worktrees preserved; the Executive's `a24-height`
uncommitted work in `/home/lubko/soring301` is untouched).
