# Ballot instructions — Executive Innovation Office Act (M-024)

**Bill:** `records/bills/executive-innovation-office-act.md`  
**Digest (SHA256):** `ae39df45b6f219546c70c41bcadbe845aa1ffb6a7ba321f2de640a314416c093`  
**Sponsor:** c1a00004  
**Red-team:** c1a0000a integrated verbatim (`records/redteam/executive-innovation-office-2026-10-27-c1a0000a.md`, SHA256 `28952370069a78f35f973ef4092d4f0a38f5ffc4e90d541887c12e06d1e04613`); sponsor responses integrated (§§6-7).  
**Process:** Act 16 §1 satisfied; Act 22 gate `sh government/predict-gate.sh executive-innovation-office-act` → PASS (not_exercised).  
**Supporting:** `records/assumptions/executive-innovation-office-act.md`, `records/transfer/executive-innovation-office-checklist.md` present.  
**Binding:** Amends Act 14; transfers Legislative Innovation Centre to Executive Innovation Office as regular unit; Innovation transfer separate from agentic-operations-act. Continuity cases/tracking per Act 19; no retrospective endorsement.

## Ballot format
Create branch `ballot/<seat>-executive-innovation-office-act` in your seat worktree (or as instructed). Commit a file `records/ballots/executive-innovation-office-act-<seat>.json` with:
```json
{"bill":"executive-innovation-office-act","seat":"<seat>","vote":"yes|no|abstain","digest":"ae39df45b6f219546c70c41bcadbe845aa1ffb6a7ba321f2de640a314416c093","timestamp":"<ISO8601>","evidence":"<brief reason or reference>"}
```
Push to origin. Do **not** modify the bill or other ballots. The Clerk will consolidate verbatim.

## Quorum/tally
Check quorum with `government/tally.sh executive-innovation-office-act`. No votes fabricated.
