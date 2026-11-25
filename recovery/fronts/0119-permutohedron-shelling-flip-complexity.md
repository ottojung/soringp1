# permutohedron-shelling-flip-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

qZXfBEMYksRdmiMk1PHcIu-wizard

## exit_state

clearexit

## question

Is the 'shelling depth' (minimum maximum number of flips to form some shelling order consistent with an optimal comparison strategy) equal to S(n) up to lower-order factors for all n, and does computing minimal shelling depth of the permutohedron face lattice reduce to exact S(n) evaluation in a way that creates a new complexity obstruction?

## basis

Permutohedron is the state graph of permutations/comparisons; shelling orders are topological, while S(n) is the minimax/adversarial game height with fixed test set - no investigated front in the ledger directly compares shelling depth to exact comparison-strategy height for all n.

## falsifier

Construct an infinite family where every shelling order corresponding to any height-S(n) strategy has depth >= c*S(n) with c>1 asymptotically or find a canonical shelling of smaller depth not realizable by any comparison strategy, breaking equivalence for all-n.

## implication

An equivalence would relate S(n) to a well-studied topological object (permutohedron shellings) and might open geometric lower-bound tools; a clean separation would show the game constraint is stronger than pure shellability.

## finding_unverified

exploring the primary literature connections more concretely - looking up shellings of permutohedron and comparison-based sorting.

**Finding (falsification): the identity fails for all $n\ge 4$ asymptotically.**

### Model mismatch (the key point)

- **Shelling chains = weak Bruhat order chains.** A shelling order of the $n$-permutohedron (or its face/chain complex) corresponds to a maximal chain in the weak Bruhat order on $S_n$. Each step along such a chain is an *adjacent transposition* $s_i = (i\ i+1)$ (an edge-move in the permutohedron 1-skeleton). The maximum (and in fact every maximal) chain has length
  $$\ell(w_0)=\binom{n}{2}=\Theta(n^2)\,.$$
- **$S(n)$ allows arbitrary pairwise comparisons.** The sorting number $S(n)$ is the minimax height of a decision tree using *arbitrary* pairwise comparisons $(i,j)$ chosen adaptively (not restricted to adjacent transpositions). Information-theoretic bounds give $S(n)=\log_2(n!)+o(n\log n)=\Theta(n\log n)$ and optimal algorithms achieve $O(n\log n)$.

Thus if "shelling depth" means the worst-case number of moves/steps in such a shelling chain (the move-count of the shelling order), it is $\Theta(n^2)$ for every shelling order, while $S(n)=\Theta(n\log n)$; equality is false for all large $n$ and by exact values for $n\ge4$.

### On the falsifier

- **Breaking equivalence:** There is no shelling order corresponding to any height-$S(n)$ comparison strategy that achieves depth $\Theta(n\log n)$ because the move model is different (adjacent swaps only). Conversely, there is no way for a chain-restricted shelling to match arbitrary-comparison costs. The proposed equivalence is false.
- **Separation is the answer:** The game constraint (arbitrary comparisons, adaptive choice to minimize worst-case height) is strictly stronger than the topological/shelling chain constraint (adjacent moves only). This is a standard move-model separation, not a subtle invariant.
- **General poset note:** Linear-extension identification relates to $e(P)$ (e.g. 1/3–2/3) and general poset sorting is hard in some forms, but transfer to the fixed antichain family does not create the claimed equivalence here; the direction is the opposite (restriction loses the $\log n$ factor).

### Complexity implications & honest limits

- **Implication:** A naive reduction from $S(n)$ to permutohedron shelling depth fails. It does *not* obviously create a new geometric obstruction to computing $S(n)$; if anything it shows why geometric chain constraints are too weak. No obvious bridge back to $S(n)$ is apparent from this move-model separation.
- **Ambiguity:** The term "shelling depth" is sometimes used differently (e.g. intersection complexity/depth in some texts), but no standard notion produces $O(n\log n)$ for permutohedron shellings. The falsifier as stated (comparisons vs shelling moves) points decisively to the adjacent-swap/chain-length vs arbitrary-comparison model.
- **Limits:** This is a combinatorial/model separation (deduction from weak Bruhat order height vs $S(n)$), not a new complexity class separation theorem. No repository changes or new Lean theorems are warranted. The question is answered negatively by the move-model mismatch. 

**Conclusion:** No all-$n$ equivalence holds; the natural correspondence gives a clean separation (quadratic vs near-linear). The front's complexity implication is not realized by equivalence — the obstruction would need to come from elsewhere, not from equating shelling depth to $S(n)$.

## Other metadata

```json
{
  "finished_at": 1793489063.2020833,
  "started_at": 1793487081.2124524
}
```
