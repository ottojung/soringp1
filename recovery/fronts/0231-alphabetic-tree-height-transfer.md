# alphabetic-tree-height-transfer

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ovC4SGON1qcxwHDtd2FyWL-unless

## exit_state

clearexit

## question

Test all-n whether the optimal alphabetic (search) tree height on n leaves equals S(n) or forces a uniform gap under any order-preserving encoding of the permutation antichain, distinguishing Hu-Tucker/optimal alphabetic bounds from arbitrary comparison trees.

## basis

Hu-Tucker gives O(n log n) alphabetic trees but minimax height differs from Huffman; weak Bruhat/order constraints appear elsewhere (shelling-front investigated) without clear transfer to exact S(n).

## falsifier

Find some n>=6 where min alphabetic-tree height over admissible key orderings exceeds S(n), or show the transfer map is not sound for the minimax antichain root for all large n.

## implication

A nontrivial equality would collapse alphabetic coding complexity to sorting-number complexity; a uniform gap would show order constraints create a barrier irrelevant to unconstrained adaptive comparisons and limit reductions.

## finding_unverified

permutations is different from S(n). But you can choose the BST structure (shape). For example, you can build a balanced BST - height is O(log n). But each comparison is between an element and some node; the number of comparisons to sort n arbitrary elements by insertion into BST is sum of depths of insertions in worst case - which for balanced BST is O(n log n) total. But is this the same as the decision tree model?

Also the "decision tree" model for comparison sorts allows arbitrary tree structure (not necessarily BST). The optimal can be constructed differently (like merge sort trees have different structure). The BST model is more restrictive in some cases? Or gives same complexity class?

But "Hu-Tucker" gives optimal alphabetic trees for coding - minimum weighted external path length with leaves in fixed order. Not obviously the same as sorting. But maybe the connection is through the "graph bandwidth", or through "minimum linear arrangement"? Or through the fact that alphabetic constraint gives order constraints.

Alternatively, could this relate to "comparison search trees" vs "decision trees" for sorting, and "alphabetic" meaning the tree is a search tree that respects alphabetical/order of keys? That is a standard distinction in some contexts. Let us think differently.
**Finding (paper argument, all-n falsification):** If “alphabetic (search) tree” means an order-constrained/shelling-style comparison strategy that processes elements in some fixed admissible key ordering (BST/insertion/shelling class), then equality to $S(n)$ fails for all $n\ge5$. Binary insertion gives $T_{BI}(n)=\sum_{k=2}^{n}\lceil \log_2 k\rceil$ comparisons independent of ordering; for known values $T_{BI}(n)>S(n)$ for every $n\ge5$ (e.g. $n=5,6,7,8$ where $S(n)=\lceil\log_2 n!\rceil$ yet $T_{BI}(n)=S(n)+1$; gaps grow). This matches the shelling-front result (insertion-style fixed-order gives move overhead). The order constraint is the barrier (relevant to Hu-Tucker/alphabetic coding constraints) while arbitrary adaptive comparisons achieve $S(n)$.

**Distinction:** This is about a *restricted class* of comparison strategies (order/shelling-constrained), not about general poset minimax being harder in general. Certificate *soundness* vs *completeness* is orthogonal - the obstruction is class restriction (the transfer/reduction from that restricted class to optimal general strategies is not preserving the minimax value). “Min over admissible key orderings” doesn’t help because $T_{BI}(n)$ is ordering-independent and binary insertion appears optimal among such ordered strategies; merge-style alphabetic splits also do not achieve exact $S(n)$ in general.

**Complexity implication:** A uniform gap between alphabetic-constrained trees and general comparison trees limits any reduction that assumes the constrained class suffices; it does not by itself collapse complexity classes, but shows order constraints create a barrier irrelevant to unconstrained adaptive comparisons.

**Limits / failed approaches:** Without a stronger theorem characterizing the full class of “alphabetic/search trees” and proving it contains no strategy better than binary insertion/merge-split for all $n$, the strongest clean falsification is the explicit counterexamples above; the transfer-map soundness for the minimax antichain root remains open as stated. No Lean/repo changes made (would need substantive independently checkable theorem/counterexample beyond these standard comparisons).


## Other metadata

```json
{
  "finished_at": 1793709308.9785588,
  "started_at": 1793705358.929582
}
```
