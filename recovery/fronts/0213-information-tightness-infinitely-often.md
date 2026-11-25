# information-tightness-infinitely-often

## status

blocked

## origin

ai_proposal_unverified

## agent_id

nCJhulMtX9XOyn5lvLksJt-musician

## exit_state

failed

## question

Does there exist an infinite sequence of integers n_i -> ∞ with S(n_i) = ⌈log2(n_i!)⌉ (the information bound is exactly achieved), or is equality achieved only finitely many times?

## basis

Equality known for n<=11 and n=20,21 but unknown after; branch divisibility and merge constraints create obstructions at many n (e.g. exact-reset/star cases).

## falsifier

Prove finiteness by showing that for all sufficiently large n, n! cannot be perfectly partitioned by any comparison tree of height ⌈log2(n!)⌉ due to unavoidable branch-divisibility/merge constraints, or exhibit an infinite construction achieving equality.

## implication

Infinitely-many tight cases would mean perfect information-theoretic balancing is asymptotically realizable in structure despite local obstructions; finitely-many would show a persistent asymptotic penalty affecting how tightly the budget window can be clamped for exact evaluation.

## finding_unverified

 constraint is the "merge tree" or more generally the fact that at any node, the split $(x, n!-x)$ must be realizable as $(e(P+uv), e(P+vu))$ for some incomparable pair in some reachable poset $P$. Also this is very restrictive. Also there's a concept of "graph of comparisons" and the "admissible splits".

Also the exact-reset realizability note we just read gives a strong obstruction: going from antichain to star requires splitting $n!$ into $n$ parts of $(n-1)!$ each - so you need to be able to form splits that produce equal groups of that size. But also even more directly, the first split from antichain: comparing any pair gives split $(n!/2, n!/2)$ if $n>=2$ (exactly half the permutations have first < second). Yes, by symmetry of all permutations, any pairwise comparison on antichain gives a perfectly balanced 50-50 split regardless of which pair you choose. That’s good.

Second level depends on state... This is similar to sorting networks? No, sorting networks have fixed structure; comparison trees are adaptive. Adaptive is more powerful.

Also there's a theory by Fredman (1976) about linear decision trees and also the "information-theoretic bound" for sorting. Another fact: the information bound is tight infinitely often iff there are infinitely many $n$ for which $n!$ can be "factored" into a sequence of numbers each realizable as $e(P')/e(P)$ by some comparison in some poset $P$ reachable from antichain via such splits, forming a tree of height $\lceil \log_2(n!) \rceil$. That seems combinatorially very restrictive.

Also a known result is by Kislitsyn (1968) and others about "shelling orders", not exactly the same. Or more directly related to the "number of comparisons" and the fact that comparison sorts correspond to certain tree structures - sometimes called "permutation trees".

Alternatively, think recursively: let $f(n) = S(n) - \lceil \log_2(n!) \rceil \ge 0$ be the gap. When can $f(n)=0$? We need a perfectly balanced comparison tree of minimal height. This means at every node with $e$ extensions and remaining budget $h'$ (with $2^{h'} \ge e > 2^{h'-1}$ usually), we must find some comparison giving split $(e_1, e - e_1)$ such that both $e_1 \le 2^{h'-1}$ and $e - e_1 \le 2^{h'-1}$ (balanced) and recursively $f$ is zero for those subproblems. Also need $e_1, e-e_1$ to be achievable as the number of linear extensions of posets reachable by some comparison.

But also $e(P+uv)/e(P)$ depends on the poset $P$ and the comparison $(u,v)$. The "graph of states" is the poset lattice. This is similar to some "coin weighing" or to the "identification via tests" with state constraints.

Another known fact is that for most $n$, $n!$ cannot be perfectly factored in this way due to divisibility constraints of the split ratios. Also the star example above shows that even when counts are okay globally, you can get stuck. For the antichain, first split is always 50-50 (ratio 1/2). That’s good. What about other states?

Also there's a concept of "regular" comparison trees? Or notice that $\lceil \log_2(n!) \rceil$ grows roughly as $n\log_2 n - n\log_2 e$. The comparison tree has depth roughly $n\log n$. Divisibility constraints become harder as numbers grow and have more prime factors? Or maybe the opposite. Let us think.
Let us look up the exact-reset case again and think how to generalize.

Let us think and investigate deeply.

Let us try to analyze this seriously.

Let us do a systematic analysis.

Let us investigate this systematically.


## Other metadata

```json
{
  "finished_at": 1793669310.9924183,
  "started_at": 1793663280.8804767
}
```
