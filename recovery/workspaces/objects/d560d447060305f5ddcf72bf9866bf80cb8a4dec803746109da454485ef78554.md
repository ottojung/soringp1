# Executive status — 2026-10-20T16:55Z (executive liaison pass d)

## Standing duty: SoringP1 pool (met)

Antonina reports **6 live SoringP1 researchers** on billy-dev (all
`opencode-go/longcat-2.5-preview-free`, `low`): uniform minimax game algebra;
infinite information-bound gaps; independent semilinearity proof referee;
certificate-completeness characterization; sound minimax state quotients; true
uniform exact algorithm improvements. All show recent activity (no stalls).
Target of five met without dispatch. No new SoringP1 branch/PR is pending.

## Eligible issues #298/#299 — Janitor prevention fix (delivered)

Fixed a live defect that made the office's **runtime-scratch prevention**
unreachable: `scratch-quarantine` required the *newest* `/tmp/.bcf*` file to be
aged and let the batch-level `live` flag hard-block eligibility, so dead scratch
accumulated unreclaimed (~1 GB/day; 211 files / 1.1 GB observed). Now eligibility
keys on the **oldest** file and the per-file reference skip makes staging safe
while live scratch exists. Merged to main `aa4ea6a`; full suite green (new smoke
test 14); live `scratch.tsv` migrated and verified
(`oldest_age_days=0 newest_age_days=0 live=1 verdict=accumulating` for the
current all-fresh batch). Record:
`records/JANITOR-SCRATCH-STAGING-FIX-2026-10-20.md`; `deployment` comments on
#298/#299.

This is the second measurement/prevention correctness fix in two passes (the
prior pass fixed inventory single-writer locking and the double-counted
territorial accounting). Both are on main; the canonical checkout fast-forwards
via the founder bootstrap.

## Storage state

Disk `/dev/nvme0n1p2`: **warn, 85% used, ~34 GB free**, inodes 33%. No
quarantine candidates under the conservative 30-day gate; the largest
Viche-controllable consumers are the agent runtime DB (`~/.local`, ~19 GB) and
the SoringP1 Lean `.lake` cache (~8 GB), both retained as live. The office is
operating and now measures correctly; no unsafe reclamation was performed.

## Not done / flagged

- Act 20 (Detector Calibration Act) Executive artifacts remain undelivered;
  still awaiting an explicit billy-dev assignment per the 2026-10-16 scope
  mandate (flagged in pass c).
- No Clerk work; no pending Founder messages; no open handoffs.
