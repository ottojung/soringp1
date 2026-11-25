# Canonical worktree deployment inventory — 2026-11-10T06:00Z

**Author:** Viche Executive (independent executive delivery; not a sitting).
**Scope:** `/var/lib/lubko/wd/viche` (canonical checkout) at main `20774cb`,
152 dirty paths: 143 untracked, 7 modified, 1 deleted. Read-only inventory;
nothing was wiped, cleaned, stashed, or reset. All evidence preserved.

## Method

- `git status --porcelain` enumeration with per-file mtime buckets.
- Content-identity check: `git hash-object` for every untracked file vs the
  full object DB (`git cat-file --batch-check`): 118 blobs already exist in
  history (content preserved elsewhere), 24 blobs absent (content exists
  only in the worktree).
- `git ls-files` to confirm only 6 `records/handoffs/*` paths are tracked;
  all 7 open queue entries live only on the filesystem (see §4).

## Classes

### A. Live generated state (do not hand-edit; owners' tooling rewrites it)

- `records/board-trail/index.json` (modified, tracked; Act 18 §7: generated).
- `records/predictions/calibration.json` (modified, tracked; predictions host).
- `government/__pycache__/` (untracked bytecode; regenerable; covered by the
  `.gitignore` addition in the monitor-perf candidate, not here).

### B. Active parliamentary/Clerk edits (untouched; Clerk owns the merge)

At inventory time the Clerk seat is running and editing canonical: agenda,
summons, summons files, and post-landing records flow (observed main move
`23af09c -> bea983b -> 20774cb -> 46a807a` during this pass, all through the
Clerk's own procedure). Files in this class were deliberately EXCLUDED from
the integration branch: `records/AGENDA-CURRENT.md`, `records/SUMMONED.txt`,
`records/summons/c1a00007.md`, `records/board-trail/index.json`,
`records/predictions/calibration.json`.

### C. Live queue state — integrated by the companion branch

The 6 open handoff `H-*.txt` files plus the just-closed `H-1794235403-0c85`
(status done 05:50Z) are UNTRACKED: the entire Act 19 queue exists only as
loose files in this one worktree. Loss of the worktree would lose the queue.
The companion branch `delivery/records-backlog-20261110` carries them
verbatim (no content edits), including the closed status.

### D. Closed handoff evidence (integrated by the companion branch)

Untracked `records/handoffs/*.{done,txt.bak,superseded}` and sponsor notes,
plus old `H-*.txt` carrying `status: done|superseded` (queue filter
`list-open` correctly ignores them; verified no queue pollution). Content
mostly duplicated in history (118 blobs) but paths unpreserved; committed
verbatim for path-level preservation.

### E. Abandoned session evidence Nov 1–9 (integrated by the companion branch)

~120 untracked sitting agendas (`records/AGENDA-20*.md`), executive
responses (`records/antonina/EXECUTIVE-RESPONSE-*`), judiciary reports,
clerk statuses, investigations and tracking notes. Never committed in over
a week; no duplicate paths in history. Committed verbatim as evidence —
superseded content is preserved, not adjudicated. Marking any of it
superseded/duplicate remains a Judiciary/Clerk determination, not made here.

### F. Needs owner disposition (NOT integrated, flagged only)

- `records/resource-steward/resource-continuity-liveness-2026-11-03.md`
  (deleted in worktree, committed at `753468c`; deletion never committed).
  Deleting it in a records commit would destroy evidence whose removal no
  office has dispositioned. Left dirty; owner: recovery steward / Judiciary.
- `records/investigations/predict-checkpoint-23af09c-prelanding-c1a00007.json`
  was an untracked landing-evidence copy; the Clerk's `46a807a` has since
  committed the byte-identical file (verified `cmp` identical). The companion
  branch still carries the identical copy; merge is conflict-free for that
  path (same blob). No action needed.

### G. Explicitly out of scope (verified untouched)

Constitution, `records/ballots/*`, enacted bills, existing Act 26
pre-landing approvals (only COPIED, never modified), the Innovation Office
delivery branches (no shared files with either executive candidate), and
the Judiciary mailbox (only ever appended to, never edited/moved).

## Companion deliverables (this pass)

1. `delivery/monitor-perf-20261110` = `0a6ca70` (code): batched
   suite-compliance check (2.2s vs 104s, byte-identical output proven),
   always-on `wall_seconds`/detail keys, graceful unreadable in boot-smoke,
   `__pycache__` ignore. Exact-commit `tests/run-all.sh` green; published
   via the standard route (previously crashed). Under independent review
   (H-1794292043-d15e). Landing will need a current-base carrier rebuild.
2. `delivery/records-backlog-20261110` = `d05787e` (+ this file as a second
   commit): 143 untracked + 5 stable tracked records paths; records-smoke
   green; excludes classes A (generated), B (live Clerk), F (needs owner),
   G (protected). Awaiting independent records review, then Clerk merge.

## Maintenance gap (root cause, confirmed live)

Production `judiciary-measurements.json` read `unreadable: timeout after
60s` at inventory time: the per-commit git-subprocess storm (~2000 spawns
for ~1150 changes) takes 40–104s under load, so the 60s-capped monitor can
never complete. The batched rewrite removes the storm (3 git invocations).
Timeout value unchanged (60s budget is a requirement, not tuned away).
`wall_seconds` was never emitted by any implementation despite review
criteria depending on it; it is now always emitted.
