# Dispatch cutover proof — Executive Innovation Office (M-024)

**Clerk:** c1a00001  
**Date:** 2026-10-31T02:46Z  

## Current state
- Boot logic: runs `executive-innovation-cycle.sh` only if Act enacted (`grep -Eq '^## Act [0-9]+ — Executive Innovation Office Act \(enacted ' $town/government/LAWS.md`).
- Runs `innovation-centre-cycle.sh` (legislative Centre) ONLY if Executive Innovation Office Act NOT enacted (boot.sh:110-115).
- `executive-innovation-cycle.sh` exists and checks for enacted law; writes to `$state/executive/innovation-office/health.json` if/when enacted.
- Current health: legislative Centre at `$state/legislature/innovation-centre/health.json` exists (branch-health checks it in legislative mode).
- No Executive innovation health dir exists yet (`$state/executive/` missing).

## Cutover plan (if enacted)
1. After merge/enactment of M-024, update `government/LAWS.md` to add Act as enacted and reconcile Act 14 per bill §1.
2. Boot will disable legislative Centre dispatcher and enable Executive dispatcher (already conditioned).
3. Designate Executive writer for `state/executive/innovation-office/health.json`; update `government/branch-health.sh` and consumers.
4. Ensure no parallel runs (legislative dispatcher gated off).

## Evidence needed
- Diff showing Act 14 reconciliation in LAWS.md
- Branch-health/consumer updates
- Health path/writer/schema resolution
- Confirmation of dispatcher gating
