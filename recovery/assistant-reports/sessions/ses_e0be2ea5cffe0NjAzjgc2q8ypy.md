# antonina-FBg9he1rIQQA4N4O8FxLDW-chartered

Session: ses_e0be2ea5cffe0NjAzjgc2q8ypy
Workspace: /home/lubko/soring-fronts/equivariant-optimal-play-class-count-alln
Created: 1795096909488; updated: 1795098931337

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 488 (msg_1f43b5c1a0011381bDnDMZjwO8)

Reported once to #301 (author `SoringP1 frontier: equivariant-optimal-play-class-count-alln`, 14:34:31Z); board scan confirms no duplicate. Worktree clean at `6a96398`; no repo/Lean/test/workflow changes.

Summary of the finding:
- **(iii) refuted (deduction):** a deterministic S_n-equivariant optimal play exists for every n — an Aut-orbit of any optimal comparison is optimal and lifts well-defined under isomorphism, with no loss in minimax value.
- **Exact small-n enumeration:** minimal equivariant optimal class counts for n=1..7 are `1,2,4,6,11,14,19`; n≤5 matches the prior absolute minima, so equivariance costs nothing there, and n=6,7 are new. Counts track `S(n)+O(n)`, supporting but not proving polynomiality.
- **Label c (precise obstruction):** neither the all-n polynomial construction nor a superpolynomial lower bound was obtained; union non-additivity and GI-type canonicalization remain obstacles. No new consequence for SORT-BOUND-U beyond the existing PSPACE/budgeted-DFS bounds.

## Output 498 (msg_1f43b7826001zPKuYuzWiBFSPn)

Recovered state: the front is complete and no further action is needed.

- **#301 post:** `SoringP1 frontier: equivariant-optimal-play-class-count-alln` was posted once (2026-11-19T14:34:31.123Z); board scan shows no duplicate. No repost made.
- **Worktree:** `/home/lubko/soring-fronts/equivariant-optimal-play-class-count-alln` clean at `6a96398` (`git status --porcelain` empty). No repo/Lean/test/workflow changes.
- **Scratch/side effects:** experiments ran only under `/tmp/opencode/q2`; an `n=8` search process was stopped (no result).

**Result (reported):** (iii) refuted — a deterministic S_n-equivariant optimal play exists for all n with no minimax-value penalty. Exact minimal equivariant class counts n=1..7: `1,2,4,6,11,14,19` (near `S(n)+O(n)`; n≤5 matches prior absolute minima). Outcome **c** (precise obstruction): neither an all-n polynomial construction nor a superpolynomial lower bound proved; union non-additivity and GI-type canonicalization remain. No new consequence for `S(n)`/`SORT-BOUND-U` (still PSPACE via budgeted DFS). No unfinished work.
