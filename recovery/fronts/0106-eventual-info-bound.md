# eventual-info-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

MFGgRKvDNBy6DQtPBlckxA-gallant

## exit_state

clearexit

## question

For all sufficiently large n, is S(n) equal to ⎡log2(n!)⎤ (the information-theoretic lower bound), or does there exist an infinite family with g(n)=S(n)-⌈log2(n!)⌉>=1?

## basis

AGENTS.md states structural theorems about the minimax game are in scope; gap-monotonicity-eventual showed g decreases infinitely often but not eventual vanishing/persistence. Known finite gaps (n>=12) leave the question open.

## falsifier

Exhibit an explicit infinite family of n with g(n)>=1 proved by a comparison-tree combinatorial obstruction (not just finite tables), or prove g(n)=0 for all large n via a uniform construction.

## implication

If g(n)=0 eventually, the 'decision-tree constraint' vanishes asymptotically and the complexity of exact evaluation reduces to information counting; if gaps persist infinitely often, the combinatorial constraints remain the hard part.

## finding_unverified

 are known for some $n\ge12$; equality holds for small $n$.
- The obstruction at finite $n$ is structural/global (not monotonic in $e(P)$, not a function of $e(P)$ alone), and is established by exhaustive poset search (Wells/Peczarski/Stober–Weiss), not by a short invariant. Local information-bound failures appear as early as $n=5$ but do not imply global gaps.
- Sergeev (2020) gives a constructive sorting strategy with $S(n) \le L(n) + O(n/(\log n)^{1/5})$, hence $g(n)=S(n)-L(n)=o(n)$ as $n\to\infty$. This is an asymptotic algorithmic upper bound on comparisons, not a proof of eventual equality and not a complexity classification of exact evaluation.

### Why neither falsifier is known
- **Proving $g(n)\ge1$ for all large $n$ in some infinite family**: generalizing Wells’ finite search to an infinite family is the natural obstruction. No known uniform combinatorial invariant does this. The strategy space grows (more comparisons available), and Sergeev shows the adversary can be forced into only $o(n)$ “unbalanced” splits asymptotically. Any infinite-family obstruction would need to survive that asymptotic flexibility and be checkable by a comparison-tree argument (not just finite tables).
- **Proving $g(n)=0$ for all sufficiently large $n$**: would mean a uniform construction achieving the leaf-count bound eventually. This requires a comparison tree of height exactly $L(n)$ realizing all $n!$ orderings despite (a) $n!$ not a power of two, (b) the fact that allowed splits are only those realizable by some comparison from some reachable partial order (the permutohedron/comparison constraints), and (c) the non-monotonicity/hard states observed at finite $n$. No such uniform construction is known; Sergeev gets arbitrarily close but the remaining additive gap is not shown to vanish.

### Concrete failed/obstructed approaches
- **Scalar invariants (efficiency/slack/entropy ratios)**: falsified (e.g. $n=5$ tight with small slack, $n=20$ tight vs $n=22$ not; monotonicity in $e(P)$ fails at $n=6$).
- **Lift Wells’ method directly**: finite case analysis doesn’t obviously scale; the bottleneck is global routing through the state graph, not a local scalar threshold. Reproducing beyond small $n$ is state-explosive.
- **“Information bound is enough asymptotically”**: true for comparisons count ($o(n)$), but exact equality is a much stronger exact-tree-realizability question with comparison constraints. The gap could persist as $g(n)\in\{0,1\}$ infinitely often or behave non-monotonically; the repo notes “gap-monotonicity-eventual showed g decreases infinitely often but not eventual vanishing/persistence.”

### Complexity implication (as stated)
- If $g(n)=0$ eventually: the decision-tree (combinatorial) constraint vanishes asymptotically and exact evaluation reduces closer to information counting (still need to know it’s achievable by comparisons and to compute it). 
- If gaps persist infinitely often: combinatorial constraints remain the hard part for exact $S(n)$.

**Bottom line:** The question is open. I cannot produce an explicit infinite family with $g(n)\ge1$ proved by a comparison-tree obstruction, nor a uniform construction giving $g(n)=0$ eventually. The decisive obstruction is the tension between asymptotic $o(n)$ closeness (Sergeev) and exact comparison-realizability of the leaf bound; without a new unifying invariant or a general realizability theorem, this remains unresolved. No repository changes or Lean are warranted by a proof here.

## Other metadata

```json
{
  "finished_at": 1793442141.16846,
  "started_at": 1793441858.433634
}
```
