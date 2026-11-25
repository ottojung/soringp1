# linear-extensions-count-pruning-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

sk5Giban051UkT4l4TNucs-deem

## exit_state

clearexit

## question

For the winning-frontier family of layered posets (union of chains plus between-level edges) appearing at depths near S(n), is there an all-n obstruction showing that any exact uniform evaluator for S(n) that uses the information bound ceil(log2 e(P)) for pruning must compute e(P) exactly on exponentially many of these states and that exact linear-extension counting on this class is not uniform-polytime per state, forcing exponential total time regardless of other pruning?

## basis

Brightwell–Winkler counting linear extensions is #P-complete; winning frontier gives exponentially many non-isomorphic states at fixed depth; obstacle is class restriction plus uniform cost, not existence of hard arbitrary posets.

## falsifier

Exhibit a uniform polynomial-time algorithm to compute e(P) exactly for all posets in that layered winning-frontier family for large n, or show a sound pruning scheme avoiding exact e(P) that achieves subexponential total evaluation time on an all-n adversarial instance from the family.

## implication

A verified all-n barrier would link #P-hardness of counting to the concrete complexity of evaluating S(n) via pruning, without requiring circuit lower bounds and while distinguishing general-poset counting from this structured class.

## finding_unverified

ial in $s$ for growing $s$; there is no known uniform polynomial-time algorithm for all $P$ in this unbounded-width layered family, and the state graph is exponentially large in $n^{1/2}$.

### Obstruction to pruning-based exact evaluation of $S(n)$
The repo’s winning-frontier theorem shows there are $\ge 2^{(1/4-o(1))n(\log n)^2}$ pairwise non-isomorphic reachable winning states at fixed depth (exponentially many in $n(\log n)^2$) with the same information/pruning budget. Any exact uniform evaluator for $S(n)$ that relies heavily on the information bound $L_0(P)=\lceil\log_2 e(P)\rceil$ (and stronger one-ply variants using $e(P)$ on children, see `research-one-ply-obstruction.md`) must, on many of these states, know $e(P)$ (or the exact split counts) to prune correctly/safely. If computing $e(P)$ exactly for states in this family is not uniform-polynomial-time per state when width is growing, then doing it on exponentially many states forces total exponential time regardless of other pruning heuristics. The obstruction is **class restriction + uniform cost + exponentially many states**, not just existence of arbitrary hard posets.

### Falsifier status
- **Falsify by algorithm:** exhibit a uniform polynomial-time algorithm to compute $e(P)$ exactly for all posets in this layered winning-frontier family for large $n$. Given $(L+1)^s = \exp(\Theta(\sqrt{n}\log n))$ states and no obvious algebraic collapse for arbitrary between-level bipartite graphs, this appears implausible; I found no such algorithm in the repo and no standard result suggesting it.
- **Falsify by pruning:** show a sound pruning scheme avoiding exact $e(P)$ that achieves subexponential total evaluation time on an all-$n$ adversarial instance from the family. The information bound is not tight and one-ply helps on some cases, but with exponentially many states and no known succinct certificate/strong compression that preserves $F$ (cf. `research-state-compression.md` showing $e(P)$ alone is insufficient and other invariants fail), this is also not obvious. No such scheme is demonstrated here.

### Complexity implication
A verified all-$n$ barrier linking #P-hardness/expensive counting on this structured class to the concrete complexity of evaluating $S(n)$ via pruning is plausible in principle and matches the repo’s framing, but it is **not established as a theorem here**. The key is: this is a restricted class (layered, union of chains) where bounded-width DP fails (width grows) and the counting is expensive/uniform-hard in effect, distinguishing it from “arbitrary posets” while still creating an exponential frontier obstruction. What’s missing is a rigorous encoding-preserving reduction from a known #P-complete problem to exact $e(P)$ counting on this *exact* diagonal-forced layered family for all large $n$ (or a proof that profile-DP is optimal/uniformly hard), plus an argument that no sound pruning avoids exact counts on an adversarial all-$n$ instance.

**Conclusion:** The obstruction argument is coherent and matches the repo’s evidence (frontier size + profile-DP exponential in width + pruning dependence on $e(P)$). However, I did not derive a new rigorous all-$n$ barrier theorem or a concrete counterexample/algorithm here — only a structural analysis. No Lean/repo changes made (per policy). The decisive obstacle remains: formalizing the reduction for the diagonal-forced layered class and showing pruning cannot avoid exact counting on an all-$n$ adversarial family.

## Other metadata

```json
{
  "finished_at": 1793778479.771806,
  "started_at": 1793776249.2261758
}
```
