# depth-balance-threshold-sharp-20261119exec

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ccHlWkNhlDjZafRHEL7NwA-squatter

## exit_state

clearexit

## question

Determine the sharp threshold constant c* = sup{c : for every finite poset P, e(P) > c*2^m(P) implies DEPTH-BALANCE B(P)}. Is the verified sufficient condition e > (5/8)2^m optimal, i.e. is there a family with e/2^m approaching 5/8 from below that violates B? Can the criterion be strengthened to cover the reachable-from-antichain optimal-play regime where e/2^m can be as small as 2^{-o(n)}? Give a rigorous argument, not just enumeration.

## basis

The verified 2026-11-19 depth-balance-induction-recovery report proved the unconditional (5/8)2^m sufficient condition but never optimised the constant; the 11:25Z Executive correction fixed a wording slip in that report. No ledger front mentions this threshold constant.

## falsifier

Exhibit a family of posets with e/2^m approaching a constant above any claimed c* from below that violates DEPTH-BALANCE, or prove no such family exists and identify the exact extremal constant.

## implication

Sharpening the threshold narrows exactly where a depth-balance counterexample can live (currently the window F_{m+2} <= e <= (5/8)2^m) and a strengthened reachable-state criterion supports a balanced-optimal normal form for exact evaluation of S(n).

## finding_unverified

Done. One comment posted to #301 (11:52:59Z) under the exact author `SoringP1 frontier: depth-balance-threshold-sharp-20261119exec`; final duplicate scan confirms exactly 1 post by that author and a clean worktree. No repository/Lean/test/workflow/ledger changes.

## What I found (deliverable **c** — barrier)

**Definitions / corrected characterization.** With the 11:25Z Executive correction, `B(P)` fails iff every optimal comparison (hard child depth exactly `m−1`) has easy child depth `≤ m−3`; pairs leaving a child at depth `m` are non-optimal and irrelevant. `c* = sup{c : e > c·2^m ⇒ B for all finite P}`.

**Baseline [deduction].** The 11:08Z theorem stands: `e > (5/8)·2^m ⇒ B`, so `c* ≥ 5/8`.

**BARRIER [deduction + independently checked experiment].** The inequality behind that theorem is an *equality* for infinitely many posets with an optimal `(m−1, m−3)` move whose two children are individually tight:
- Base witness `P5` = successor bitmasks `(0,5,1,5,1,17)`, `m=5`, `e=20=5·2²`, optimal moves `{1,4}`,`{3,4}` with child depths `(4,2)` and child counts `(16,4)=(2⁴,2²)`. Verified by two independent from-scratch engines.
- Infinite family `P_m = P5 ⊕ (A₂)^{⊕(m−5)}`: `e=5·2^{m−3}`, ratio exactly **5/8**, tight `(m−1,m−3)` children (checked m=5..8); uses the ordinal-sum lemma `m(Q⊕R)=m(Q)+m(R)`.
- Consequence: any method using only (i) the information bound on one optimal move's children and (ii) easy-child depth `≤ m−3` is capped at 5/8. A strict improvement must use the global "all optimal moves unbalanced" condition.

**Reachable-regime limitation [deduction].** The hypothesis `e>c·2^m` depends only on `(e,m)` and is silent when `e/2^m ≤ c`; since the optimal-play root ratio is `2^{-(S(n)−log2 n!)}` with `o(n)` excess (Sergeev), no constant threshold can certify depth-balance in the small-ratio regime — a structural criterion is needed.

## Honest limits
- `c*` is **not** computed. Existence of any B-failing poset is itself open (none through n=10; any counterexample n≥11, series-prime, Fibonacci-nonminimal). If B is universal, `c*=+∞` (degenerate); otherwise `c* ∈ [5/8,1]`.
- The n≤6 census (4920 ratio-5/8 extremal posets with a tight unbalanced move, all satisfying B) is consistent with 5/8 not being attained by a B-failing poset, but is not a proof. The question of a B-failing family approaching 5/8 from below stays open — the §3 family has ratio 5/8 but satisfies B.
- No claim about `S(n)`, `SORT-BOUND-U`, or any complexity separation.
Confirmed: the single #301 comment by `SoringP1 frontier: depth-balance-threshold-sharp-20261119exec` (posted 11:52:59Z) is the only external side effect, and the worktree is clean. No further action needed — the deliverable (barrier result) is complete.

## Other metadata

```json
{
  "finished_at": 1795089322.9778137,
  "started_at": 1795088068.9510741
}
```
