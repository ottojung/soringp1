# Current random-audit sample (4 cases) — Clerk triage, 2026-11-08

Source: `/var/lib/lubko/wd/viche-state/oversight/random/latest.json`
(`sampled 268`, `reported 264`, `unreported 4`, `cases_unreported_overdue 0`).
The four are **newly sampled**, not overdue. Recorded here so the agenda carries
them rather than letting a fresh sample look like a defect.

| Case | Issue | Subject | Clerk note |
|---|---|---|---|
| `f996b4c6e4ec1460d8` | 279 | Volodyslav Journal 3: multiple independent adversarial reviews before merge | External repo; `Execution-Host: billy-dev`; four independent lenses required. No local clone — delivery state unverifiable here. |
| `286321f712a55e9a24` | `lWMIGRLB53TS70RCs2gpI8-suppose` | Viche: adjudicate Act 17 double-correction limit before Judiciary PR #32 | **Legislature matter** (Act 17 per-case/per-cycle limit), already open. |
| `95392423a74b262de2` | 142 | Kawun: rejecting-message settle leaves reply port unanswered | External project; needs its owner and an independent check. |
| `cdb96b7f46a111ceae` | `08a05b2…` | `government/appointments.sh`: do not fail identity resolution on transient agent status | **Evidence below**: the merge is in HEAD; the runtime file is a stale older revision. |

## Case `cdb96b7f46a111ceae` — Clerk evidence (not a closure)

```
git show HEAD:government/appointments.sh | grep -c 'live=unknown'   -> 1
grep -c 'live=unknown' government/appointments.sh                    -> 0
git hash-object government/appointments.sh   -> c3ef7f4e…
08a05b2^:government/appointments.sh          -> a54f63d2…
08a05b2:government/appointments.sh           -> c6b85f5f…   (== HEAD)
```
The worktree blob `c3ef7f4e…` corresponds to an **older committed revision**
(found in history at `45982a0`). So the "merged but not deployed" gap is a
**stale/dirty worktree copy**, not a missing merge and not a novel work-in-progress
edit. Reconciling it is Executive/Recovery Steward work under Act 19; it must be
done without discarding other uncommitted work.

This is evidence for the Auditor, **not** a disposition: the Clerk is not the
independent verifier of a file it is reporting on.
