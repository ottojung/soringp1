# shelling-order-dimension-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

A4r09pTy3WHS88N4HmZYo8-hydatid

## exit_state

clearexit

## question

Is the comparison tree depth S(n) equal to the shelling order height of the permutohedron P_n for all n, and if not does the shelling/complexity obstruction transfer to give an all-n barrier on certain certificate classes?

## basis

Shelling sequences of zonotopes/permutations, Kahn-Saks-Sturtevant topological approach to evasiveness; shelling-path-complexity-root front examined insertion-style constraints but not the full shelling order of P_n as a candidate invariant.

## falsifier

Find n where minimum shelling order length differs from S(n) by more than lower-order terms, or show shelling constraints are strictly weaker/laxer than adversarial comparison strategy constraints for the antichain.

## implication

A positive identification would connect S(n) to a well-studied poset/simplicial complex parameter and might suggest topological lower-bound techniques, while a negative would separate shelling complexity from the minimax sorting game.

## finding_unverified

n trees. Optimal comparison trees can make different first comparisons depending on structure and need not follow any fixed insertion order; they are exponential in description and not representable as shellings induced by a single linear function. So even the full family of linear-function shellings is strictly weaker than the minimax adaptive class.

### Obstruction to topological transfer (Kahn–Saks–Sturtevant)
- KST/evasiveness applies to **monotone graph properties** (closed under adding edges) on subsets of a fixed edge set, using fixed-point/topological degree on spheres. 
- Sorting is a **total order identification function** on labeled elements (identifying which permutation) given pairwise comparisons — different model (queries are comparisons/adaptive; the “property” is not a subset property of a fixed graph in the A–K–R sense). 
- There is no standard encoding-preserving reduction showing a shelling/topological obstruction on $P_n$ shellings transfers to an all-$n$ barrier on $S(n)$-minimax strategies; certificate classes differ (soundness/completeness). Without such a reduction, the “complexity implication” is speculative.

### Concrete falsifier (checkable)
Find any $n\ge4$ with $\min_{\text{linear-function shellings }\sigma} (\text{height/strategy depth of }\sigma) > S(n)$ (true for all $n\ge4$ where $S(n)<\sum\lceil\log_2 i\rceil$, which is most). Or more directly: for $n=4$, $S(4)=5$; any fixed-order insertion gives 1+2+2=5? Wait: insert 2nd: 1 comparison, insert 3rd into pair: ceil(log2 2)=1? Or binary insertion: to insert $k$-th element into sorted list of $k-1$, need $\lceil \log_2 k\rceil$ comparisons in worst case? n=4 elements total: insert 2nd: compare with 1st -> 1 comparison (can place it), insert 3rd: binary search in 2 elements needs 2 comparisons? Or ceil(log2 3)=2. insert 4th: ceil(log2 4)=2. Total 1+2+2=5. Equals $S(4)=5$. n=5: insertion gives 1+2+2+3=8, $S(5)=7$. So equality holds for some $n$ (4?) and fails for others (5+). The claim states “equal to the shelling order height of the permutohedron $P_n$ for all $n$” — that’s false for $n>=5$ under linear-function shellings; also false for $n>=4$ under poset-height interpretation.

### Honest limits
- If “shelling order height” means something else not obvious from standard definitions, the falsification above might miss it. But I cannot find a standard combinatorial parameter called “shelling order height of $P_n$” equal to $S(n)$ in the literature; the curator basis gives it as a candidate invariant to test.
- No encoding-preserving reduction from shelling complexity to a barrier on $S(n)$ certificate classes is apparent. Distinguishing general-poset results from $S(n)$ (antichain root) is important per AGENTS.md.
- No Lean/repo changes warranted — this is a standard combinatorial disproof, not a new theorem requiring formalization beyond known values.

**Finding:** The all-$n$ equality is false on both natural interpretations (poset height of weak Bruhat order differs for $n>=4$; linear-function shellings = fixed-order insertion strategies differ for $n>=5$ and are strictly more restricted than adaptive comparison trees). The KST topological obstruction does not transfer to the minimax sorting game without a nontrivial reduction (general-poset/topological results don’t automatically yield an all-$n$ barrier on $S(n)$ certificate classes). No evidence for a positive identification; the barrier is the class restriction, not an obstruction equalizing them.

## Other metadata

```json
{
  "finished_at": 1793703218.6237695,
  "started_at": 1793700906.6632779
}
```
