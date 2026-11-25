# Janitor liveness-aware idle build-cache reclamation — 2026-10-20

Issue #298/#299 (Janitor Office, billy-dev). Act 12.3(2) (reclaim when verified
safe), 12.4 (evidence standard), 12.7 (executive gate). Ordinary executive
implementation of the enacted Janitor Act; the Constitution is unchanged.

## Why

The office's only `.lake` rule was `age >= 30 days`, which never fires on the
fast SoringP1 research cadence. The filesystem reached **94% used (level=high,
~15 GB free)** overnight and was relieved only by a **manual** executive action
(`records/JANITOR-IDLE-CACHE-RECLAIM-2026-10-20.md`), whose explicit follow-up
recommendation was a liveness-aware build-cache rule. Disk is the binding
constraint on SoringP1 research parallelism.

## What (commit 522fc08, main)

New mode `reclaim-idle-caches` and an automatic trigger in `cycle`. A `.lake`
cache is deleted **only** when all hold:

- **Not live:** no process references the cache or its worktree — checked with
  `path_in_use` (a `/proc` scan of cwd/root/open-fd/maps/mounts), *not* the
  Antonina registry (which the 2026-10-20 record showed misses raw `opencode
  run` processes).
- **Idle:** the cache mtime is at least `idle_cache_seconds` old (default 6 h).
- **No unique work:** the worktree is a git worktree with **no unpushed commits**
  and **no uncommitted changes**.

Deleting a `.lake` loses only build time, never data
(recovery: `cd <worktree> && lake update && lake exe cache get && lake build`).
Every decision is logged with its path and reason. Gated by `reclaim_enabled=1`
(Act 12.7) and `idle_cache_enabled=1`; `cycle` runs it only at high/critical
pressure (`severity >= 2`). `--dry-run` reports without deleting.

## Verification

- `tests/janitor-smoke.sh` test 15: dry-run deletes nothing; a clean, fully
  pushed worktree's idle `.lake` is reclaimed; an unpushed worktree's `.lake` is
  retained (`reason=unpushed`).
- `sh -n` / `dash -n` clean; `tests/run-all.sh` green (all Viche tests pass).
- **Live dry-run** against the real inventory: 2 idle SoringP1 caches identified
  (`/home/lubko/soring301/.lake` 8.1 GB idle ~3.4 d; `soring301-explore-hardness/.lake`
  0.1 GB idle ~16 h) = **8.6 GB** reclaimable; **all** AssemblyP1 worktrees
  correctly skipped (`reason=unpushed`). No deletion performed in the dry-run.

## Honest limits

- Reclamation is **deletion of regenerable build output**, not a reversible
  move — the Act 12.3(2) evidence gates (liveness + idle + pushed + clean) are
  the safeguard; the recovery command is recorded per action.
- The default 6 h idle threshold matches the 2026-10-20 emergency precedent; it
  is configurable. Under sustained pressure an active-but-idle worktree's cache
  may be reclaimed and later rebuilt (time cost, not data loss).
- The rule does not reclaim non-`.lake` artifacts; those remain under the
  age/quarantine pipeline.
- Independent verification remains the Judiciary's.
