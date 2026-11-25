# Janitor idle-cache valve: per-HEAD unpushed check — 2026-10-20

Issue #298/#299 (Janitor Office, billy-dev). Act 12.3(2)/12.4. Corrects the
liveness-aware idle build-cache reclamation added earlier the same day
(`records/JANITOR-IDLE-CACHE-RECLAIM-AUTOMATION-2026-10-20.md`). Ordinary
executive implementation of the enacted Janitor Act.

## Defect: the valve was silently disabled

The idle-cache rule required, per cache, that its worktree be a git worktree
with **no unpushed commits**, checked with
`git log --branches --not --remotes`. Branch refs are **shared across a
repository's linked worktrees**, so a single unrelated worktree's unpushed commit
made *every* `.lake` in that repository look unpushed.

Observed 2026-10-20 18:20: the SoringP1 caches were skipped
`reason=unpushed commits=1` even though the main checkout's `HEAD` (`main`) was
clean and fully pushed — the one unpushed commit was on the separate
`research/unary-state-quotient-20261020` worktree branch. The valve therefore
could not fire on the very caches it was built to reclaim.

## Fix (commit 7ea810f, main)

- Check only the worktree's **own HEAD**: `git log --not --remotes` (defaults to
  `HEAD`, which is per-worktree), not `--branches`.
- **Conservative fallback:** if the repo has **no remote-tracking refs** at all,
  `--not --remotes` is empty and cannot confirm the work is saved, so the cache is
  treated as unpushed (skipped). Verified: in a repo with no remotes,
  `git log --not --remotes` returns 0 commits (misleading), hence the fallback.
- The other gates are unchanged: no live process (`path_in_use`), idle >=
  `idle_cache_seconds` (default 6 h), and a clean worktree (no uncommitted
  changes). `cycle` still runs it only at high/critical pressure.

## Verification

- `tests/janitor-smoke.sh` test 15 now adds an **unrelated unpushed branch** to
  the same repo and still reclaims the pushed worktree's idle `.lake`; the
  no-remote worktree is still retained (`reason=unpushed`).
- `sh -n` / `dash -n` clean; `tests/run-all.sh` green (all Viche tests pass).
- **Live dry-run** now identifies **20 verifiably idle, regenerable caches,
  ~30.2 GB** (including `/home/lubko/soring301/.lake` 8.1 GB and the stale
  AssemblyP1 caches, idle 6–28 days) — matching the Founder's #299 direction to
  "reclaim automatically when verified safe" box-wide. No deletion performed in
  the dry-run.

## Honest limits

- Reclamation deletes regenerable build output (recovery: `lake update && lake
  exe cache get && lake build`); the evidence gates are the safeguard.
- The rule now can reclaim **other projects'** (e.g. AssemblyP1) stale caches
  under pressure, per the Founder's #299 territorial directive; the 6 h idle gate
  plus the pushed/clean/liveness checks ensure only stale, saved, unreferenced
  caches are touched. This is a behaviour change from the conservative
  `--branches` check and is recorded here for transparency.
- Independent verification remains the Judiciary's.
