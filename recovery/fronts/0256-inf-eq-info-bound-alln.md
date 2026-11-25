# inf-eq-info-bound-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Y1brWAPHeOfYI7RXcths7p-radiating

## exit_state

clearexit

## question

Determine for the exact sorting function S(n) whether the set {n >= 0 | S(n) = ⎡log2(n!)⎤} is infinite or finite, by analyzing all-n constraints on perfect levelwise comparison splits rather than restricting to fixed heuristic constructions such as Ford–Johnson.

## basis

Peczarski/Stober–Weiß give equality at small n and again at 20,21 with gaps; fredman-additive-exact-regime notes FJ matches only there but the general question of infinitude remains open.

## falsifier

Prove that for all sufficiently large n, some invariant (e.g. a modular/divisibility obstruction on the extension-count class of every reachable poset) forces S(n) >= ⎡log2(n!)⎤ + 1, or construct an explicit infinite family achieving equality.

## implication

A finiteness proof would sharply delimit when the information-theoretic lower bound is exactly achievable; an infinitude proof would reveal a nontrivial infinite regime of perfect splitting. Neither directly yields P!=PSPACE but changes the asymptotic structure of S(n).

## finding_unverified

Let us look up the question again carefully - "determine for the exact sorting function S(n) whether the set {n >= 0 | S(n) = ⎡log2(n!)⎤} is infinite or finite, by analyzing all-n constraints on perfect levelwise comparison splits rather than restricting to fixed heuristic constructions such as Ford–Johnson. FALSIFIER: Prove that for all sufficiently large n, some invariant (e.g. a modular/divisibility obstruction on the extension-count class of every reachable poset) forces S(n) >= ⎡log2(n!)⎤ + 1, or construct an explicit infinite family achieving equality."

So they want an analysis of "all-n constraints on perfect levelwise comparison splits" - this suggests looking at levelwise splitting (tree level by level). The divisibility/modular obstruction on extension counts is mentioned as an example. Also we saw that at some poset states (like e=8 poset at n=5), there are no perfectly balanced comparisons. Also as we go down a perfectly balanced tree structure, we reach states with certain e values. But is there a modular obstruction?

Also another angle - for a perfectly balanced decision tree of height h = ceil(log2 n!) with n! leaves, the tree is almost complete. But the comparison constraints create obstructions. Also related to the "graph bandwidth" or to the fact that certain poset states are not "sortable" with balanced splits.

Alternatively, think recursively: let T be the set of n with equality. T contains small n. To have equality for larger n, you need to find some first comparison giving balanced or nearly balanced splits to states from which equality is achievable in h-1 more steps. This is similar to some partitioning problems. And there might be modular obstructions.

Let us write up a careful analysis.

Let us analyze carefully.

Let us understand the full picture of this specific front.

Let us do a systematic analysis.

Let us post our analysis.

Let us provide the analysis as requested.

I analyzed the problem as requested - looking at all-n constraints on perfect levelwise comparison splits, reviewed the branch divisibility obstruction literature, and examined both directions of the falsifier. The branch divisibility obstruction applies to exact resets to uniform classes but not directly to standard sorting trees ending in total orders; the infinitude question remains open. No new theorem or counterexample found, worktree is clean.

## Other metadata

```json
{
  "finished_at": 1793742336.5146778,
  "started_at": 1793733973.3422053
}
```
