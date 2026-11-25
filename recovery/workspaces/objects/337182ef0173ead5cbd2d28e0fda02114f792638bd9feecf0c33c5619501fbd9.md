# Janitor inventory accounting fix — 2026-10-20

Issue #298/#299 (Janitor Office, billy-dev). Act 12.2 territorial accounting.
Ordinary executive implementation of the enacted Janitor Act; the Constitution
is unchanged.

## Defects observed on the live office

1. **No single-writer guard.** Two `inventory` passes ran 41 s apart
   (15:24:07Z and 15:24:48Z) and interleaved appends into the shared
   `$jstate/tmp/inventory.tsv`, producing **282 rows for 186 paths**. The
   `mv`-based publish is atomic, but the shared temp file is not.
2. **Nested `.lake` double-count.** `box_visible_kb` summed *every* row.
   A `…/.lake` row is already contained in its parent worktree's `du`, so it was
   counted twice. Combined with (1), the office reported **270.9 GB
   "box-visible" on a 186.2 GB-used device**, and the clamped
   `outside_box_kb = device_used − box_visible` collapsed to **0** — making the
   headline territorial accounting meaningless.

## Fix (commit 37bb6f6, main)

- **Single-writer lock.** An `mkdir`-based lock (`$jstate/lock`, POSIX-atomic)
  guards every mutating mode (`observe|reclaim|cycle|inventory|classify|
  quarantine|reclaim-quarantined|scratch-quarantine`). Read-only `report`/`status`
  stay lock-free. A lock older than `lock_stale_seconds` (default 900 s) is
  presumed dead and reclaimed; the holder removes it via an `EXIT` trap.
- **Correct territorial sum.** `box_visible_kb` now sums distinct top-level
  paths only, excluding nested `…/.lake` rows:
  `NR>1 && $3 !~ /\/\.lake$/ && !seen[$3]++`.
- **Testability.** `JANITOR_ROOTS` / `JANITOR_FILE_ROOTS` override the inventory
  roots (defaults unchanged) so the scan can run hermetically.

## Verification

- `tests/janitor-smoke.sh` extended with (12) a lock regression — a held fresh
  lock makes a mutating run skip cleanly, a stale lock is reclaimed and logged —
  and (13) a territorial-accounting regression asserting `box_visible_kb` equals
  the sum of distinct top-level paths with a nested `.lake` present.
- `sh -n` / `dash -n` clean; `tests/run-all.sh` green (all Viche tests pass).
- **Live repair.** The corrupt live inventory would not self-heal for ~24 h
  (daily cadence), so the fixed script was run against the real state:
  inventory now **186 rows / 186 unique paths**; territorial
  `device_used 187.0 GB, box_visible 125.9 GB, outside_box 61.1 GB` — a sensible
  decomposition, replacing the impossible 270.9 GB / 0 GB.

## Honest limits

- `box_visible_kb` remains a threshold-filtered **lower** bound (rows < 100 MB
  are not counted), so `outside_box_kb` is a corresponding upper bound; this is
  documented in the script.
- The lock addresses the observed same-state race; it does not add cross-host
  locking (out of scope — one box).
- Independent verification remains the Judiciary's; this record claims only what
  was tested and measured here.
