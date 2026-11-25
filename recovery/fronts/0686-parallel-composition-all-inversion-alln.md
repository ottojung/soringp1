# parallel-composition-all-inversion-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UyQSJ4FJ9C3tHILLnem1BQ-susan

## exit_state

clearexit

## question

For all finite posets A and B, does sibling-extension-inversion all-inversion transfer across parallel (disjoint-union) composition exactly as it transfers across ordinal sums, i.e. is A || B all-inverted if and only if both A and B are all-inverted, or can disjoint-union composition create or destroy the all-inversion property that is equivalent to failure of Claim C?

## basis

Newest #301 05:54Z post reports an ordinal-sum propagation/characterization theorem for all-inversion. Independent scratch check (experiment) confirmed that rule on 320/320 small pairs, found zero all-inverted posets through n=6, and found no all-inverted A||B at total size <=6; no parallel-composition inversion theorem occurs anywhere in the 685-front ledger.

## falsifier

Exhibit finite posets A,B with allinv(A||B) differing from (allinv(A) AND allinv(B)): either a disjoint union that is all-inverted although some component is not, or two all-inverted components whose disjoint union is not all-inverted.

## implication

Together with the reported ordinal-sum propagation theorem, a parallel composition theorem would make all-inversion recognizable via Gallai modular decomposition, giving polynomial-time recognition of the Claim-C-equivalent obstruction and a stronger sound pruning invariant for exact unary S(n) evaluators.

## finding_unverified

hat no repo changes occurred.
Done. Here is the honest outcome of this front.

## Mathematical finding

**1. Exact obstruction (deduction).** The front's equivalence
`allinv(A‖B) = allinv(A) ∧ allinv(B)` is *hostage to the open Claim C* (the sibling fronts' conjecture that every poset with `m≥2` has a non-inverted optimal comparison):
- If Claim C holds, `allinv` is empty everywhere → both sides always false → the equivalence is **vacuously true**.
- Every possible falsifier exhibits an all-inverted poset (either `A‖B`, or `A` and `B`) → it **refutes Claim C**.

So the front cannot be settled without settling Claim C (verified only through n=9). Consequently the advertised complexity payoff is blocked: Gallai modular decomposition would still need the all-inversion status of each prime node, i.e. exact `m`, `e` and the optimal-pair set — the PSPACE-level minimax game plus #P-hard counting. This is a *soundness-only* general-poset observation, not a completeness/complexity theorem.

**2. Unconditional structural theorem (paper proof).** If a poset `P` has an automorphism `σ` swapping an incomparable pair `p=(x,y)`, then `σ` is an isomorphism `P+xy ≅ P+yx`, so `p` is a **forced tie, never an inversion**. Applied to `A‖B` with `A≅B`, every diagonal cross pair `(a, φ(a))` is a forced tie. Thus parallel composition has a concrete mechanism to *destroy* all-inversion that ordinal sums lack (where every optimal comparison is within-block). Verified exhaustively for all unlabeled `A` with `|A|≤3`: 20/20 diagonal pairs are forced ties (0 inversions) **and all 20 are optimal**, so `A‖A` is never all-inverted in that range. A falsifier follows *if* an all-inverted `A` with a diagonal optimal cross pair exists — none is known.

**3. Concrete cross-comparison inversion (experiment).** `W=(0,0,2,2,6,14) = {0} ‖ Q` (n=6) has an optimal cross-block pair `(0,3)` whose hard child has `e=14 < 16`. This refutes the naive analogue of the ordinal-sum theorem's property (i) for disjoint unions: parallel composition admits both optimal cross comparisons and cross-comparison inversions. `W` is not all-inverted (1 of 8 optimal pairs).

## Concrete failed approach / exact limit

I tried to lift a non-inverted optimal pair from `A` to `A‖B` to prove the create direction. Extension-count order *is* preserved (both children scale by `binom(a+b,a)·e(B)`), but minimax order need not be (ordinal sum has `m` additive; parallel composition does not). An exhaustive check of 66 within-block comparisons found 0 m-order reversals and 0 tie-breaks — so no small witness and no proof either way; and even preservation wouldn't guarantee optimality at `A‖B`. General optimality of diagonal cross pairs needs `m` at `|A|=4` unions (A001035(8) = 431,723,379 states) and is infeasible; one such run was killed by the backend failure with no side effects.

## Honest limits / S(n)

All findings are general-poset structural facts. No all-inverted poset exhibited, no Claim C progress, no new `S(n)` bound, no placement of `SORT-BOUND-U` below PSPACE, and no evaluator pruning invariant (`e` is #P-complete; finding optimal pairs *is* the minimax game). The front is **not** resolved — its only possible falsifiers refute the open Claim C.

**Effect audit:** worktree clean at `6a96398` on `billy-dev`; no Lean/repo/test/CI/ledger changes; scratch files only in `/tmp/opencode`; exactly one board #301 post landed (06:57Z), after confirming none from this front existed beforehand. Nothing duplicated.

## Other metadata

```json
{
  "finished_at": 1795330687.213607,
  "started_at": 1795328902.2828438
}
```
