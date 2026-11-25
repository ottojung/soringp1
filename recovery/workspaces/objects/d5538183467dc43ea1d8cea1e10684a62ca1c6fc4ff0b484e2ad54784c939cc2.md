# Janitor Office — emergency idle build-cache reclamation (2026-10-20)

Issues #298/#299. Authority: Act 12.3(2) (reclaim when verified safe), 12.4
(evidence standard), 12.7 (executive gate). Trigger: filesystem reached
**94% used** (level=high) with ~15 GB free.

## Attribution (Act 12.12)

`df` used on `/dev/nvme0n1p2` (233 GB) rose 85% → 94% over ~12 h, coinciding
with new SoringP1 research worktrees. The dominant consumers were Lean/Mathlib
`.lake` build caches under `/home/lubko/soring301*`:

| Path | Size | Idle | In use |
|---|---|---|---|
| `soring301-explore-hardness/.lake/packages` | 14.45 GB | ~6 h | no |
| `soring301-next-highercomp/.lake/packages` | 2.82 GB | ~21 h | no |
| `soring301/.lake` | 8.1 GB | ~3 d | possibly (research worktrees) |
| **total `.lake`** | **24.7 GB** | | |

## Action (evidence-gated)

Verified before reclamation, for each target: (a) no process had the worktree as
its cwd (`/proc/*/cwd` scan); (b) the worktree is a git worktree on a pushed
branch with **no unpushed commits** (`git log --branches --not --remotes` empty);
(c) `.lake/packages` is a **regenerable** dependency build (Mathlib clone +
oleans), not unique data; (d) the office's own safe-reclaim was "not-due" and the
office's `.lake` rule (age ≥ 30 d) is too conservative for this fast research
cadence.

Reclaimed `soring301-explore-hardness/.lake/packages` and
`soring301-next-highercomp/.lake/packages`.

**Before:** 94% used, ~15 GB free. **After:** **87% used, ~31 GB free** —
**~17.2 GB freed**. Logged in `janitor/actions.log`.

## Recovery

Both caches are regenerable inside their worktrees:
`cd <worktree> && lake update && lake exe cache get && lake build`
(`~/.cache/mathlib`, 449 MB, is the shared Mathlib cache). No research result,
commit, doc, script or record was removed — only build output.

## Honest limitations and follow-ups

- The office's `classify` counts `.lake` age, not **liveness**, and uses the
  Antonina agent registry, which does **not** see the raw `opencode run`
  processes the SoringP1 operator launches (a running agent on `soring301-n05`
  was invisible to `antonina agent list --running`). The office must detect
  liveness via `/proc/*/cwd`, not the registry, before any build-cache
  reclamation.
- The remaining `soring301/.lake` (8.1 GB) was **retained** — a live SoringP1
  research process may use it.
- Recommended janitor improvement: a liveness-aware build-cache rule
  (idle = no process cwd + mtime idle + worktree pushed) that reclaims
  regenerable caches with a recorded recovery command, instead of age ≥ 30 d.
- Disk remains the binding constraint on SoringP1 research parallelism; the
  standing five-agent target cannot be safely replenished without cache
  management.
