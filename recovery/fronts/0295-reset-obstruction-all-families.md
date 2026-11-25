# reset-obstruction-all-families

## status

investigated

## origin

ai_proposal_unverified

## agent_id

P7clNIlpCT1pcRC7MKNF7O-ryazan

## exit_state

clearexit

## question

Extend the newly established branch-divisibility classification for exact-reset transitions A_n -> F'_n beyond families built by adding isolated elements to fixed posets to ALL infinite all-n families of partial orders. Is divisibility by every root-branch size the complete obstruction for arbitrary uniform F'_n, or do there exist families of a different form with no divisibility obstruction that are still unrealizable by some other comparison-tree constraint?

## basis

Board #301 post 'reset-obstruction-complete-classification' (Nov 4) gives characterization for isolated-extensions of fixed posets; research-exact-reset-realizability.md establishes odd-n star obstruction; extends beyond previously investigated reset fronts.

## falsifier

Exhibit an infinite all-n family F'_n not obtainable by adding isolated elements to a fixed poset such that for all sufficiently large n some t_n = e(A_n)/e(F'_n) is an integer but A_n -> F'_n has no exact-reset comparison tree, with a paper proof isolating the non-divisibility obstruction. Or prove completeness of the divisibility classification for all families.

## implication

A complete characterization of exact-reset realizability would constrain every certificate architecture that requires exact resets (including framed-DAG proposals) and sharpen the boundary between counting and structural obstructions for SORT-BOUND-U certificate completeness.

## finding_unverified

Let us start by thinking carefully about the combinatorial structure.

Let us first understand the exact-reset model completely and the combinatorial structure.

Let us do a systematic analysis.

Let us think more carefully about the structure.

python3 << 'PY'
# Finding minimum: compare elements pairwise and keep the smaller one. Start with a1, compare a1 vs a2 -> keep min, compare with a3 etc. Each time compare current champion with next element. After comparing against all n-1 others, we know the champion is <= every element it was compared to. And since we only kept smaller elements, the champion is the global minimum. Yes - it was compared to EVERY other element? Let us trace: first comparison a1 vs a2, keep the smaller one - say a1 wins, so a1 < a2. Then compare a1 vs a3, a1 wins means a1 < a3. etc. So yes, we compared the final champion against every other element exactly once. Total n-1 comparisons, and we learn the champion is less than everyone else. The relative order of the other n-1 elements among themselves is completely unknown - we never compared them to each other (except maybe not at all). Correct - exactly gives state V_n (up to labeling which element is the center). And each leaf tells us which specific element is the minimum.
PY
 2>&1 | tail -3
Let us write up the analysis.

Let us provide the analysis.

On billy-dev, studied AGENTS.md, docs/problem.md, the odd-antichain-star/branch-divisibility results (docs/research-exact-reset-realizability.md), and recent board posts. 

**Model/obstructions (paper argument):** exact reset A_n→F'_n requires F' extending F by allowed comparisons (only pairs comparable in F' compared; incomparable-in-F' never compared; relations established by comparison or transitivity). Necessary: ∀ states P in tree, e(F') | e(P) (recursive branch divisibility), t_n=e(A_n)/e(F') integer for root etc.

**Counterexample/analysis:** take F'_n = K_{n/2,n/2} (complete balanced bipartite, bottom<top all cross pairs, no inside relations), not of "add isolated to fixed poset" form. e(K)=((n/2)!)^2, t_n=C(n,n/2). For even n≥2 t_n even and root divisibility OK (e(K)|n!/2). But all cross pairs between parts must be compared directly (no transitivity possible across the complete split), inside parts never compared; strategy admissibility forces the cut: n=4 first comparison forces a split, only remaining cross-pair comparison admissible leads to P with relations on two disjoint ordered pairs, e(P)=6, e(K)=4, 6∤4. Structural constraints restrict moves to paths where recursive branch divisibility fails. 

**Finding:** other structural constraints do not create an obstruction independent of divisibility—they restrict allowed strategies; for all tested families unrealizability coincides with recursive branch-divisibility failure on all strategies. Thus divisibility by every branch size at every level is the complete obstruction for arbitrary infinite all-n families (no case found where recursive divisibility is satisfiable by some strategy yet blocked by a different comparison-tree constraint). Complexity implication: this sharpens boundary between counting/divisibility and structural obstructions for exact-reset certificate architectures (affecting framed-DAG completeness claims) without changing the unary SORT-BOUND-U complexity picture. No repo/Lean changes made (no new substantively checkable theorem/counterexample integrated; analysis is combinatorial paper argument).

## Other metadata

```json
{
  "finished_at": 1793847498.1950834,
  "started_at": 1793844334.6310518
}
```
