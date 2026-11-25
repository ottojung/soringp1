# poset-canonicalization-state-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

9dQWOXk26MPMxWI7jb8a5z-joliet

## exit_state

clearexit

## question

Is there a polynomial-time computable canonical labeling for all posets reachable from an antichain on some height-S(n) strategy such that the number of canonical classes is polynomial in n for all n, or does every complete canonical system produce exponentially many classes on these reachable sets?

## basis

Adversary-memory-state-minimality and orbit-quotient-exponential-barrier investigated but the specific all-n question of polynomial vs exponential canonical classes for height-S(n)-reachable states remains unresolved.

## falsifier

Give a uniform polynomial canonicalizer with proof of class-count poly(n) on all height-S(n)-reachable posets for all n, or prove for some infinite family of those posets that any canonicalizer preserving minimax order-type requires exp(Theta(n log n)) classes.

## implication

Polynomial classes would suggest memoization is feasible for the game graph; exponential classes would be a structural barrier to simple DP by state canonicalization without losing optimality.

## finding_unverified

e-minimality and orbit-quotient-exponential-barrier investigated but the specific all-n question..." So perhaps related to adversary strategy/state minimization?

Also look up what "orbit-quotient" means - quotient by orbits under group action gives S_n orbits. "Exponential barrier" from orbit quotient suggests the orbit count is exponential. But in our optimal-play states, orbit quotient gave counts like n=6 gives 134 classes which is exponential in n^? 134 is about 2^(7.1), and n^2 is 36, so not exponential in n^2; but is it exponential in n? Or just growing quickly. 134 for n=6 is large but not obviously exponential in n (could be polynomial in some other sense). Also compare to total labelled posets which grow as 2^(Θ(n^2)) - orbit quotient (by S_n, size n!) gives factor n! reduction but still exponential in n log n in some way? Or A000112 is still 2^(Θ(n^2)/something) - Kleitman–Rothschild says log2 of number of posets is n^2/4 + o(n^2). Quotienting by S_n gives another factor related to n! ~ e^{n log n}, so log of A000112 is still Θ(n^2). So orbit quotient by full symmetric group doesn't kill the exponential (in n^2) growth.
Let us compute growth.

**Finding (mathematical, no proof):** The question splits on *what* equivalence is allowed.

- **Orbit quotient is exponential-in-`n²`.** Relabelling by `S_n` gives unlabelled poset classes `A000112(n) = 2^(Θ(n²))` (Kleitman–Rothschild). Our measurements confirm: all-poset quotient is 318 at `n=6`; optimal-play quotient is smaller but still 134 at `n=6`, 19 at `n=5` etc., growing quickly (not obviously polynomial in `n`). 
- **Coarser invariants fail to preserve minimax order-type.** Linear-extension count is falsified at `n=5` (two non-isomorphic posets same `e(P)` but different `F(P)`). Comparability graph is ruled out; modular decomposition up to reversal fails at `n=7`. The state genuinely needs enough structure to determine the minimax value.
- **Restricting to "optimal-play" states helps but is not obviously polynomial.** The union of all states on some height-`S(n)` strategy is much smaller than all labelled posets (e.g. `n=6`: 65k labelled → 1551 in union-of-all-optimal DAG → 134 quotient classes), but still exponential in structure; no evidence of polynomial-in-`n` growth from small `n`.

**Concrete failed approach / obstruction:** We found no candidate minimax-preserving equivalence coarser than poset isomorphism that is obviously polynomial-size for all `n`. More directly, there is no known infinite family that forces *any* congruence for the minimax operator (preserving `F` and optimal-move legality/values) to have `exp(Θ(n log n))` classes, and no known polynomial-time canonicalizer with a proof of polynomial class count. The "adversary-memory/state-minimality" and orbit-quotient barriers are suggestive but not tight to this *optimal-play* restriction.

**Honest limits:** This remains unresolved. A proof of exponential classes would need to show some infinite family is pairwise inseparable by any minimax-preserving equivalence (stronger than isomorphism in some way? Or ruling out all coarser ones). A proof of polynomial classes would need an explicit polynomial canonicalizer with a full all-`n` correctness argument. Neither exists in the current evidence. The sparsity/Mahaney barriers don't directly force exponential canonical classes - they constrain NP-hardness routes. No repository changes or Lean formalization are warranted without such a substantive, checkable result.


## Other metadata

```json
{
  "finished_at": 1793426521.0827773,
  "started_at": 1793425379.916516
}
```
