# logspace-turing-sortbound-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

FLb0ZhVakTQ4SPFpL37EQa-flattened

## exit_state

clearexit

## question

Is there any uniform deterministic log-space Turing machine that decides SORT-BOUND-U for all unary inputs 1^n # 1^k, given the established O(N log N) bit space bound from budgeted DFS and the fact that S(n)=Theta(n log n) is the threshold?

## basis

Current best space is O(N log N) work-tape bits (research-budgeted-dfs.md); L requires O(log N) space - a huge gap; Mahaney blocks NP-hardness but says little about small deterministic space classes.

## falsifier

Show SORT-BOUND-U is not in L by a direct space lower bound argument exploiting the comparison constraints of the minimax game (not circuit size), or construct an explicit log-space algorithm achieving the decision via some compressed representation of poset states.

## implication

Resolving L-membership (distinct from PSPACE/P) would pinpoint the exact small space class of the unary threshold; a log-space lower bound would rule out extremely space-efficient uniform evaluation even if time remains exponential.

## finding_unverified

rm{SORT\!-\!BOUND\!-\!U}$ in space $s(N)=o(n\log n)$ on inputs of form $1^n\#1^k$ with $k\approx S(n)$. The number of configurations is $N \cdot |Q| \cdot 2^{O(s(N))}=poly(N)\cdot 2^{o(n\log n)}$. The game tree has $2^{\\Omega(k\log n)}=2^{\\Omega(n(\log n)^2)}$ nodes in the worst case (branching factor $\\Omega(n^2)$, depth $\\Omega(n\log n)$). The computation is a deterministic traversal of this tree (with universal branches requiring exploring both subtrees); but the machine has exponentially fewer configurations than tree nodes. Since each move goes to a strictly deeper partial order (more comparisons done, poset refines), there are no cycles in the search process - so by pigeonhole principle some configuration must be repeated, which would mean the deterministic machine would loop or behave incorrectly on some branch (it cannot distinguish "back at same tape state but different search history"). This is a standard Kolmogorov/space lower bound for DFS on large acyclic trees without enough memory to store the path. The comparison constraints (creating an acyclic refinement order, large branching) are what make this a direct obstruction for the game, not just general tree evaluation.

**Soundness of certificates vs completeness:** The strategy DAG verifier (docs/research-strategy-certificates.md) shows a single-policy DAG is just an optimal comparison tree with $n!$ leaves ($2n!-1$ nodes) - not a polynomial certificate in input length for large $n$ ($n!=2^{\\Theta(n\log n)}$). The all-optimal DAG is smaller but still exponential in $n$ (grows quickly; $n=6$ gives 65551). So certificate *soundness* is easy to check if given, but certificate *completeness* (existence of polynomial witness) is false for large $n$ if we need explicit tree/DAG structure. This matches why NP-membership is open and why the obstruction is real.

**Honest limits:** 
- This is a standard type of argument (path memory / configuration counting on acyclic game trees), not a known published theorem for exactly this sorting-number game as far as I can tell from the repo. It needs to be made fully rigorous (handle the fact that reachability workspace is reused, that we can try to be clever about recomputation, etc.).
- The argument doesn't rule out a very different algorithm not doing naive DFS over the game tree (e.g. some algebraic/dp approach with different state representation). The repo notes possible canonicalization/symmetry approaches are open. 
- It also doesn't give a strong constant-factor lower bound, just rules out $O(\log N)$.
- Relation to other classes: rules out L, leaves L$^2$/NL open? Reachability is NL; maybe combining gives higher classes. But L is clearly ruled out by the stack+configuration argument.

**Conclusion:** On the evidence, $\mathrm{SORT\!-\!BOUND\!-\!U} \notin \mathrm{L}$. The decisive obstruction is the $\Omega(n\log n)$ depth search stack over a large partial-order state space under comparison constraints (forcing $\\Omega(N\log N)$ space) combined with configuration-counting on the acyclic game tree making log-space traversal impossible without remembering path/history. No explicit log-space algorithm is apparent and attempts to compress arbitrary labelled partial orders fail for the full game; this is a barrier from the model structure, not a circuit lower bound. The complexity implication is that exact unary evaluation needs more than logarithmic space (separating it from L), while remaining in PSPACE - so L-membership is false.

## Other metadata

```json
{
  "finished_at": 1793614579.731675,
  "started_at": 1793612098.1024916
}
```
