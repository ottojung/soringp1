# fan-family-excess-boundedness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

iJLBG7V6Fcz2MKbn2Iuv2e-infecting

## exit_state

clearexit

## question

For all integers m,k >= 2 and 1 <= r <= m-1, is the information excess F(P)-ceil(log2 e(P)) of the fan poset P=(A_m (+) A_k) with r cross relations deleted from a fixed maximal element at most 3?

## basis

Newest board #301 prime-excess-unboundedness (01:56Z) derives the fan-family extension count and reports an exact scan over m,k <= 22 with maximum excess 3, while stating that this family alone does not grow; no all-(m,k,r) proof exists.

## falsifier

Exhibit m,k,r with exact F(P)-ceil(log2 e(P)) >= 4, or prove that the fan family excess is unbounded as m,k,r grow.

## implication

Since the fan family contains the single-deletion prime family, a uniform bound would imply the antichain excess E(n) is bounded by an absolute constant; a counterexample would give a simpler unbounded prime family than the iterated gluing.

## finding_unverified

Recovering — I'll verify what already happened before doing anything new.
No board post exists yet for this front — nothing duplicated. The worktree is clean and prior scratch logs show partial exact-minimax data. I'll verify the key anomaly before continuing.
The DP checks out on small cases. Now I'll run the falsifier scan: find small-`n` fan posets where the lower bound plus max possible `eta` could reach 4, then compute exact `F`.
The scan confirms the obstruction: no `d_lb≥2` below `n=17`, so exact computation can't reach a falsifier. Let me fill the exact small table and verify the structural pieces.
All structural pieces verify. Let me fill the last small gaps in the exact table.
All paths to a falsifier are blocked at precise,checkable points. Now let me find the board-posting mechanism used by prior fronts.
The draft checks out against the logs. Posting once now.
Recovery complete. No duplicate side effects; the one unfinished item (the board report) is now done.

## What actually happened (verified, not repeated)

- **Worktree:** clean at `6a96398`, no commits/edits/Lean changes — before and after.
- **Board #301:** no post from this front existed (digest confirmed zero matches); the prior turn posted nothing. I posted **exactly once** at `2026-11-10T07:43:21Z` (verified as 1 unique match). No duplicate.
- **Ledger:** still `status: running` (keeper-managed; left untouched).
- **Prior-turn artifact issue found and fixed:** the earlier scratch exact-minimax solver memoized on `tuple(sorted(succ))`, which is unsound (drops element identity) and gave wrong values (e.g. `F(2,3,1)=5`). All reported exact values use the corrected full-tuple solver, cross-checked against the referee `F_fast` implementation.

## Mathematical finding

The front's falsifier (exact excess ≥ 4, or unboundedness proof) was **not met**, and the universal bound-3 was **not proved** — the question remains **OPEN**, with the gap now precisely mapped:

- **Sandwich [paper proof]:** `S(m)+S(k) ≤ F(P) ≤ S(m)+S(k)+⌈log₂(r+1)⌉` for every fan. Upper bound via: after sorting both antichains exactly `r+1` extensions remain (only `b*`'s rank among the `r` partners is free), so binary search finishes.
- **`r=1` class:** `eta ∈ {0,1}`, both occur; excess ∈ `[E(m)+E(k)−1, E(m)+E(k)+2]`. Hence a uniform fan bound of 3 would force `E(n) ≤ 4` for all `n` — the proof direction is at least as hard as an open problem.
- **Exact data (corrected solver):** maximum exact excess **1** over all computable fans (`n≤8` plus two `n=8` cases); genuine `eta=1` at `(3,4,3)`, `(4,2,2)`; `eta=0` is the norm.
- **Exact obstruction:** a counterexample needs `d_lb=3` (first at `n=27`, exact `F` infeasible) + `eta≥1`, or `d_lb=2` (first `n=17`) + `eta≥2`, or new `S`-values beyond `n=22`. Every path is blocked at a checkable point.
- **Failed approaches recorded with flaws identified:** splice/twin lower bound (twin flips the `A`-order — refuted by optimal-tree inspection), subtree-sorting fallacy, adversary-forcing of maximal `eta` (refuted by `eta=0` data).

No process success is claimed as proof; no repo/Lean changes were warranted.

## Other metadata

```json
{
  "finished_at": 1794296655.8293908,
  "started_at": 1794289511.54995
}
```
