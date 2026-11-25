# antonina-hF7HI5N9t7KHIUc58BsEAE-awaits

Session: ses_e18d2624dffe2ZgOc5hKfSQCEA
Workspace: /home/lubko/soring301-exec-n12-obstruction-20261116
Created: 1794879889021; updated: 1794880829708

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 112 (msg_1e735e750001DnwSzCfkRYc7IX)

No duplicate post, no exec-report, no ledger entry for my front — the previous turn appears to have died before doing anything. Let me verify there are no other side effects (temp files, checkpoints), then start the actual work.

## Output 145 (msg_1e73644eb001lcWgiB2ORnMhUM)

State assessment complete. The previous turn left **no** side effects: no `exec-report.md`, no board post with this author, no ledger entry, clean worktree (the `/tmp/opencode` files belong to other fronts — root-reachable-collision, component-reversal, an Executive office round; none are mine). So I do the full task now.

Reading the key background docs:

## Output 200 (msg_1e73870e10017JzyrwSoRsEjxN)

I now have full context on the prior survey. Before designing the attack, I need to pin down one decisive literature fact: what is actually known about lower bounds on the excess `S(n) − log₂ n!` asymptotically (this determines whether an "infinite family with root lift" would be new knowledge or already covered by asymptotic bounds).

## Output 215 (msg_1e73965c10011X5meIZQ5ZSb7p)

Web search is unavailable; the repo's own notes should record these facts:

## Output 308 (msg_1e73ba4660019UWTtfX97OkilW)

Completed.

- **exec-report.md** written at `./exec-report.md` (untracked deliverable; no other repo/Lean/PR changes; worktree otherwise clean).
- **Board post** made to Antonina issue #301 authored "SoringP1 frontier: n12-obstruction-invariant" (confirmed present, no prior duplicate).

**Result (obstruction, not a new invariant).** No invariant in the surveyed families (one-ply `L1`, two-ply/`L_k`, merge-factor/ordinal-sum, low-dimensional scalars) — nor any invariant in the local pair-split `T`-hierarchy over an info-scored child scorer — can be strictly above `C` at a balanced antichain root. The balanced free-pair path `P_t` (t disjoint ordered pairs + free elements) keeps `L_j(P_t)=C(P_t)` for all `j,t`, so `L_k(A_n)=C(n)` (verified `L_j(A_12)=29` for `j=0..8`). Merge-factor and scalars are likewise excluded at the root. `F` itself lifts (`F(A_12)=30`) but is the minimax problem itself; whether any faster-than-`F` invariant lifts an infinite family containing 12 remains open, as does `S(n)` vs `C(n)` for `n≥23`.
