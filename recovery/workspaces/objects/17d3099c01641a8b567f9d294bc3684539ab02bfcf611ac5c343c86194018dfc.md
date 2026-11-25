# Janitor runtime-scratch staging fix — 2026-10-20

Issue #298/#299 (Janitor Office, billy-dev). Act 12 (Territorial Janitor Act),
prevention/early-warning function. Ordinary executive implementation of the
enacted Janitor Act; the Constitution is unchanged.

## Defect: scratch staging was unreachable on a live box

The office tracks node/opencode runtime scratch (`/tmp/.bcf*`, ~5.4 MB/file).
Two rules together made `scratch-quarantine` a no-op in practice:

1. **Eligibility keyed on the newest file.** The verdict required
   `newest_age_days >= 1`, i.e. *no* file in the batch could be recent. A
   continuously refreshed batch therefore never qualified (observed
   `newest_age_days=0` on every live run).
2. **The batch-level `live` flag hard-blocked eligibility.** Any single
   referenced `.bcf` set `live=1`, which set the verdict to `live` instead of
   `quarantine-eligible` — even though the running agent only holds its *own*
   current file, not the hundreds of dead ones.

Result: dead scratch accumulated unreclaimed (582 files / 3.17 GB at 01:26Z;
211 files / 1.1 GB at 16:52Z), bounded only by the runtime's own occasional
cleanup, not by the office.

## Fix (commit aa4ea6a, main)

- **Eligibility keys on the OLDEST file** (`oldest_age_days >= 1`): the batch is
  eligible when it contains *any* aged file, regardless of recent ones.
- **The batch-level `live` flag is now informational** (recorded, not gating).
  This is safe because `scratch_quarantine` already re-checks each file
  individually and `mv`s only files that are aged *and* unreferenced; if none
  qualify it stages nothing and removes the empty staging dir.
- `scratch.tsv` gains an `oldest_age_days` column (schema migrated on next
  write); `JANITOR_SCRATCH_DIR` allows hermetic tests.

## Verification

- `tests/janitor-smoke.sh` extended (14): an aged scratch file is staged while a
  fresh one is left in place, with `reclaim_enabled=1`.
- `sh -n` / `dash -n` clean; `tests/run-all.sh` green (all Viche tests pass).
- **Live:** the fixed inventory ran against the real state and migrated
  `scratch.tsv` to the new schema; it reports
  `count=216 size_kb=1176768 oldest_age_days=0 newest_age_days=0 live=1
  verdict=accumulating` — correct for the current all-fresh batch (the oldest
  file is ~10 h old). Once files age past one day without runtime cleanup, the
  aged unreferenced ones become stageable into the reversible grace+reclaim
  pipeline.

## Honest limits

- Staging is **reversible** (move to `$state/quarantine`, 7-day grace, then
  `reclaim-quarantined`); no file is deleted directly by this path.
- The office still cannot reclaim scratch a live process currently maps — that
  is intended (it would break a running agent).
- Independent verification remains the Judiciary's; this record claims only what
  was tested and measured here.
