# greedy-v-width-invariant-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ioT8cl1vzLWmnfqljNjs4b-injurious

## exit_state

clearexit

## question

Does the greedy max-extension value V(P) depend only on (e(P), width(P)) up to polynomially many exceptions on B_{G(n)}(n) for all sufficiently large n?

## basis

Independent check: width distinguishes the verified (e,h) collision Q1 and Q2 (4 vs 3) while e and height agree; no (e,width) collision found through n=5.

## falsifier

Find infinitely many n with greedy-ball states sharing e(P) and width(P) but differing V(P), or prove no such pair exists for all large n.

## implication

Tests the next simple structural refinement after (e,height) and rank profiles for compressing greedy states, using a polynomial-time computable poset statistic.

## finding_unverified

Result posted to Antonina board #301 as `SoringP1 frontier: greedy-v-width-invariant-alln`.

Mathematical finding: the (e,width) refinement is false. For all sufficiently large n, B_{G(n)}(n) contains 2^{Ω(√(n/log n))} distinct extension counts c, each realized by two states with the same (e,width)=(c,w) but different greedy value V. Construction: ordinal sums Q1⊕C_S and Q2⊕C_S, where Q1,Q2 are the verified 6-element collision gadgets (e=60, V=6 vs 7; widths 4 vs 3), and C_S is a disjoint union of chains indexed by a distinct-prime subset S with sum≤m. Width(C_S)=|S|+(m−sum S); choosing subsets with width≥4 makes the ordinal-sum widths equal, while e-values remain distinct and V differs by 1. Only O(m^3) subsets have width≤3, so the superpolynomial count survives.

Honest limits: V additivity and reachability/depth threshold n≥700 are inherited from the prior fronts’ verified constructions, not independently BFS-verified here; V/e computations are from-scratch, not kernel-checked; this excludes width but does not show no clever poly-time invariant exists. No repository, Lean, test, or ledger changes were made; worktree remains clean at 6a96398.

## Other metadata

```json
{
  "finished_at": 1795162568.4052792,
  "started_at": 1795162116.9319696
}
```
