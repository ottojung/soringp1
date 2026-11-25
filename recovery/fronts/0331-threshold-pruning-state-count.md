# threshold-pruning-state-count

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QyelzB1hSqLANjdzFLzrUa-stories

## exit_state

clearexit

## question

In the budgeted exact minimax DFS for SORT-BOUND-U, does replacing the e<=7 Hanamura-Iwata base by the exact extension-threshold base e(P) <= T(b) imply accept reduce the worst-case number of expanded reachable states below the established 2^{O(n log^2 n)} frontier for all n?

## basis

docs/research-budget-pruning.md extension cutoff and e<=7 base; board #301 supported T(6)=33, T(7)=54 and T(8)=88; the winning-frontier barrier gives 2^{Omega(n log^2 n)} nonisomorphic winning states at the relevant depth.

## falsifier

An infinite all-n family of reachable states with e(P) > T(b) that every correct threshold-pruned evaluator must expand, or a proof that the pruned state count remains 2^{Omega(n log^2 n)} at the antichain root.

## implication

A yes answer would improve the exact unary time bound toward 2^{O(n log n)}; a no-go would show the Fibonacci threshold is structural only and sharpens the boundary of the current evaluator even though the pruning rule is sound.

## finding_unverified

,
- the exact threshold acceptance `e(P)≤T(b) ⇒ True`,
- total-state termination,

expands at least

\[
2^{S(n)-O(d(n))}=2^{\Omega(n\log n)}
\]

reachable states. Thus the threshold base cannot collapse the optimal search below the `n log n` scale, let alone to polynomial or `2^{O(n)}`.

**Proof sketch.**

1. All-`b` upper bound, no Fibonacci conjecture: the staircase `W_{b+2}` has `e=F_{b+3}` and `F=b+1`, so

   \[
   T(b)\le F_{b+3}-1<2^{b-1}\qquad(b\ge 7).
   \]

2. Write the slack of a winning state as `s=b-log₂ e(P)`. Both children of a winning comparison have `e≤2^{b-1}`.
   - If both children exceed `T(b-1)`, neither is accepted: the search branches.
   - If one child is accepted, then `e(P)≤2^{b-1}+T(b-1)`, forcing `s≥1-o(1)`; the heavy child then has slack reduced by `1-o(1)`.
   
   Hence along any root-to-leaf path there are at most `d(n)+O(1)` “unary” steps where one child is accepted.

3. The root has `e=n!`, slack `d(n)=o(n)`. On the heavy path, `e≥n!/2^t=2^{b-d}`, so while `b≫d` the state itself is not accepted. Therefore the successful search skeleton has at least `S(n)-O(d(n))` binary branching levels.

4. A binary tree with at most `d` unary nodes on any path still has at least `2^{S-O(d)}` nodes. Since `S(n)=Θ(n log n)` and `d=o(n)`, this is `2^{Ω(n log n)}`.

**Concrete ceiling witness.** For `P_m` = ordinal sum of `m` two-antichains, `e(P_m)=2^m` and `F(P_m)=m`. By the all-`b` upper bound, `e(P_m)>T(m)`, and the threshold base rejects every state until constant budget. Direct exact-threshold runs for `m≤8` gave `2^{m-1}-1` expanded calls (e.g. `m=8`: `127`). This shows the threshold rule does not even collapse information-ceiling states.

## Failed approach and exact obstruction

The natural attempt was to transfer the winning-frontier barrier to the threshold-pruned DFS. That transfer fails:

- The winning-frontier states are **winning** and may have `e(P)>T(b)`. Indeed `A_n` itself and the ordinal-sum ladders are winning with `e>T(b)`.
- Therefore `e(P)>T(b)` cannot be interpreted as “losing” or “forced to expand.” Soundness of the threshold rule is not completeness.
- The winning-frontier theorem counts reachable winning states, not states that every selective evaluator must examine; it was explicitly not a time lower bound.

To obtain the missing `2^{Ω(n log² n)}` bound, one would need an all-`n` family of **budget-feasible losing children** with

\[
e(P)\le 2^{b-1}\quad\text{but}\quad F(P)>b-1,
\]

so that the information cutoff does not prune them and the threshold accept cannot resolve them. That is exactly an all-`n` local non-tightness/gap family. The known `n=12` gap is finite evidence, not such a family.

## Honest limits

- The proved lower bound is `2^{Ω(n log n)}`, not `2^{Ω(n log² n)}`. It rules out reduction to `2^{O(n)}` or polynomial time by this pruning route, but it leaves open whether the threshold base can improve `2^{O(n log² n)}` all the way to `2^{O(n log n)}`.
- Exact `T(b)` is known only for `b≤8` (`4,7,12,20,33,54,88`); the all-`r` identity `T(r)=F_{r+3}-1` remains open. The argument above deliberately uses only the proved upper bound `T(b)≤F_{b+3}-1`.
- The lower bound is for the threshold-only evaluator family. Other structural rules—ordinal-sum additivity, memoization, orbit quotients—can bypass it, so it is not a general lower bound on all algorithms.
- This is a paper proof relying on the published Sergeev asymptotic; it is not Lean-checked and was not integrated into the repository.

## Other metadata

```json
{
  "finished_at": 1794096985.4478557,
  "started_at": 1794095931.76037
}
```
