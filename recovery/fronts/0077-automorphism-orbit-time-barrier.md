# automorphism-orbit-time-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UMJnwjx8pGrwn81yCYi7I2-growths

## exit_state

clearexit

## question

For posets in the sorting-minimax state graph, does the existence of families with trivial automorphism group but quadratic incomparable-pair counts (the staircase/height-two family) force the minimax DFS to visit Omega(2^(c n log n)) distinct states in the worst case for some uniform strategy class, or can cross-state canonicalization + admissible pruning achieve 2^(o(n log n)) uniform time?

## basis

The staircase poset P_m has Aut trivial yet Theta(n^2) incomparable pairs (time-exponent note); quotienting by Aut gives no reduction, but this is a limitation of local pruning not yet shown to force global exponential state explosion for the full minimax algorithm.

## falsifier

Prove a state-count lower bound for any correct uniform minimax evaluator exploiting trivial-aut orbit families, or give a constructive uniform method using cross-state compression/canonical labeling that beats the known 2^(O(n log^2 n)) numeric-n bound on those families.

## implication

This would distinguish within-state orbit pruning (provably insufficient) from global state compression: a global obstruction would bound uniform evaluators even without strong automorphism symmetry, while a positive construction would improve the known upper bound for computing S(n).

## finding_unverified

hich model. Also adversary can force choices, but showing unavoidable for *all* uniform evaluators is hard without fixing representation.
- *Concrete failure:* Quadratic branching is already the worst case for incomparable pairs; trivial Aut means no local orbit collapse, but to force exponential *distinct* poset-states you need that you can't reach same poset via different orders or can't canonicalize - but posets are the state objects and different orders give different transcripts but same poset is reachable; memoization would collapse them. A "uniform minimax evaluator" that does no cross-state memoization/canonicalization would visit path nodes (possibly many) but calling them "distinct states" conflates paths and poset states. Also quotienting is sound for any evaluator that can canonicalize. No obvious invariant (like the linear-extension counterexample shows leaf count fails) gives a forced distinct-poset lower bound on staircase specifically.

**Falsifier attempt 2 (upper bound / constructive beating):** Give constructive uniform method with cross-state compression/canonical labeling beating `2^{O(n log^2 n})` on staircase families.
- *Known:* Quotient DP already does this in practice (extends to n=9) but canonicalization is expensive; asymptotically class count still `2^{Θ(n^2)}`. The budgeted DFS (§13) says "quotient's raw state count is still 2^{Θ(n^2)}", so better bound needs structure not just canonicalization. Staircase is a height-two family but doesn't obviously have special decomposition exploited by known methods; series/parallel decompositions exist but minimax of disjoint unions isn't additive (`docs/research-state-compression.md` §Next). No published method beats `n log^2 n` exponent.
- *Concrete failure:* No obvious decomposition makes staircase "easy"; it's just asymmetric height-two. Cross-state canonical labeling is necessary but not obviously sufficient to drop exponent below `n log^2 n` given `2^{Θ(n^2)}` class space and no known decomposition theorem.

**Exact obstruction:** The gap is between "within-state orbit pruning provably insufficient" (established) and "global state explosion forced for all uniform minimax evaluators" (not established). The trivial-Aut + quadratic-pair property is necessary but not sufficient to force a worse asymptotic than the general `2^{O(n log^2 n)}` bound because (1) branching factor is already quadratic generally, (2) cross-state canonicalization/quotienting is sound and collapses by `2^{Θ(n log n)}` while keeping exponent class same, (3) no all-n invariant forces distinct poset-state visits on staircase beyond what general posets already require - and the budgeted (no-memo) DFS already achieves `2^{O(n log^2 n)}` by path counting. To force larger than known bound you'd need to rule out all cross-state compression for this family; to beat known bound you'd need structure staircase doesn't obviously provide. Neither direction is established by current literature.

**Bridge to S(n):** The question directly addresses the exponent of uniform exact evaluation of `S(n)`. A global obstruction would mean trivial-symmetry families still force exponential state explosion despite quotienting - contradicting "canonicalization helps" intuition; a positive construction would improve the known upper bound. But neither is proved. This remains an open obstacle (consistent with §13 of budgeted DFS).

**No repo/Lean changes.** Reported limits honestly; no new theorem/counterexample established.

## Other metadata

```json
{
  "finished_at": 1793391245.1269374,
  "started_at": 1793390334.9262326
}
```
