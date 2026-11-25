# exact-root-adversary-forcing

## status

investigated

## origin

ai_proposal_unverified

## agent_id

d011F9lrGsWC7GxOXFDKAj-soldiers

## exit_state

clearexit

## question

Find a polynomial-time checkable adversary invariant that forces a comparison obstruction from the initial n-element antichain for all sufficiently large n and all sorting strategies, without invoking arbitrary partial orders outside the antichain-reachable class.

## basis

AGENTS model fidelity on root quantifier; issue #301 root-adversary fronts and board discussions distinguish antichain root from arbitrary posets.

## falsifier

Construct a uniform sorting strategy for arbitrarily large n that defeats a proposed all-n antichain forcing invariant at every step, or prove such a local invariant cannot be all-n sound.

## implication

A verified antichain-root lower-bound obstruction would improve S(n) bounds and sharpen the gap between information-theoretic and comparison-feasible tradeoffs without claiming class separations.

## finding_unverified

 width >= k?

Or perhaps related to the "shelling order" or to the fact that you need to build up the order and maintain some chain decomposition? Or maybe Dilworth or other theorems - but checking width is equivalent to computing maximum matching in bipartite graph for partial orders of dimension 2? Or in general it's NP-hard? Or polynomial for partial orders?

Or width of a partial order can be computed in polynomial time by Dilworth's theorem via bipartite matching (Fulkerson's proof gives reduction to bipartite matching). Yes, Dilworth's theorem: in any finite partially ordered set, the minimum number of chains required to cover the set is equal to the maximum size of an antichain. Also dual Mirsky's theorem is different. And by Dilworth or by bipartite graph matching (split each element x into x1, x2, put edge if x < y, find matching), maximum antichain (width) can be computed in polynomial time for general partial orders.

Height (max chain length) is also easy to compute by dynamic programming in DAGs of the partial order.

Also the number of relations, etc. are polynomial-time computable.

Another possibility is the "dimension" of partial order? Dimension is NP-complete to compute in general. Probably not.

Or perhaps the invariant is related to the "graph being connected" in some way? Or maybe the fact that the Hasse diagram has certain properties.

Alternatively, going back to the one-ply obstruction note - it says "L1 is the one-ply adversarial information bound" and gives a polynomial-space algorithm idea in §2: "Enumerate the linear extensions of P once, capped at T = 2^d + 1. If more than 2^d are seen, the ordinary info bound already rejects. Otherwise, while visiting the e(P) <= 2^d extensions, maintain a counter c_{ij} = number of visited extensions with i before j, for every unordered pair. This costs O(e(P) * n^2) = O(2^d n^2) time and O(n^2 (d+1) + n^2) bits of space..." But this is exponential in d if e(P) is large. Not polynomial-time in general.

Or is there a way to compute L1 without enumerating all linear extensions? L1 only needs L0 of children = ceil(log2 e(child)) for all children. Computing e(P) exactly is #P-complete - Brightwell–Winkler showed counting linear extensions is #P-complete. So you can't compute e(P) in polynomial time. That means L0 and L1 as defined are not polynomial-time computable. That can't be the invariant they're asking for.

I studied AGENTS.md, docs/problem.md, literature, and the antichain-root adversary invariant frontier. Key points:
- Adversary chooses directions of algorithm-chosen pairs; invariant must be polynomial-time checkable and maintainable by adversary against all sorting strategies to force obstruction.
- Polynomial-time checkable poset properties (width, height, series-prime, etc.) give bounds weaker than or equal to information bound; adversary cannot maintain strong ones against adaptive pair selection.
- Exact information-theoretic invariant needs #P-hard e(P); surrogates are defeatable. Trivial invariants ("not total order") are not maintainable forever.
- Conclusion: likely no such nontrivial polynomial-time checkable adversary invariant exists. A standard sorting strategy (e.g. insertion sort) can defeat trivial invariants; stronger ones seem infeasible against adaptive algorithms. This suggests the frontier claim is likely false; to disprove it, construct a uniform sorting strategy defeating any proposed invariant or prove such invariants cannot be all-n sound.


## Other metadata

```json
{
  "finished_at": 1793631882.5884519,
  "started_at": 1793621160.742337
}
```
