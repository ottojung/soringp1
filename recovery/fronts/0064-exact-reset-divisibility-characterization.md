# exact-reset-divisibility-characterization

## status

investigated

## origin

ai_proposal_unverified

## agent_id

8CyCfvUTMaQMNJAcYv1qOb-brass

## exit_state

clearexit

## question

For pairs of boundary posets (F,F') reachable in an exact-reset certificate system, characterize exactly when e(F') divides e(F) is realizable by some comparison stage (with branch-isomorphism constraints), and does that arithmetic condition fail for some all-n family while e-ratios remain integer powers-of-two-friendly?

## basis

Exact-reset tree realizability result (A_n->V_n counterexample for odd n) shows arithmetic divisibility is necessary but not sufficient; branch-divisibility-generalization was investigated without a complete characterization.

## falsifier

Find an all-n family with integer e(F)/e(F') powers of two in ratio but unbranchable by any pairwise stage, or prove the divisibility+branch-isomorphism conditions are equivalent to a simple arithmetic invariant for all comparison modules.

## implication

A complete realizability characterization would turn ceiling/rounding from vague obstruction into a checkable grammar constraint and clarify whether exact-reset certificate architectures are fundamentally limited or merely under-specified.

## finding_unverified

r of two). Every comparison: either comparing incomparable element y with some chain element gives split m/(2^k) where m is position of y (unbalanced unless m = 2^(k-1) which gives balanced count but branches non-isomorphic), or comparing chain elements gives split determined by where y sits but chain elements remain comparable - also gives unbalanced splits in general? Let us check. Comparing two chain elements when y is placed somewhere - the relative order of chain elements is fixed by chain relations, so comparing chain elements gives unbalanced or trivial splits. Yes, only y vs some chain element gives non-trivial splits, and only the middle one gives balanced count but wrong branch structure.

So this is an all-n family (parametrized by k, n = 2^k elements total) where e(F)/e(F') can be a power of two in principle, but there is no comparison stage with branch-isomorphism constraints realizable - either no balanced split exists, or balanced splits exist but lead to non-isomorphic branches. So the arithmetic condition (ratio power of two / balanced splits possible) is not sufficient; branch-isomorphism is an extra constraint that fails here. That matches the falsifier.

The characterization is: for exact reset with branch-isomorphism, every node must make a comparison that is "automorphism-preserving" in the right sense giving balanced split to isomorphic states, which is extremely restrictive. The simple arithmetic invariant (ratio being power of two / all branch sizes powers of two etc.) is necessary but not sufficient because of the poset structure constraints on which comparisons are allowed and whether they preserve isomorphism classes.
Now I need to report this finding. The instruction says "Report honest limits. ... On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." Also says "Do not create Lean or repository changes without a genuinely substantive, independently checkable new theorem or counterexample."

This is a concrete counterexample family. The family F^(k) = (chain of 2^k - 1) union {one element incomparable to all} has e(F^(k)) = 2^k. For any comparison stage to a single F' with e(F') = e(F^(k)) / 2^m (ratio power of two), branch-isomorphism requires every node to split into isomorphic branches of equal size. The only comparison giving equal split is comparing the incomparable element with the middle chain element, but this gives non-isomorphic branches. All other comparisons give unbalanced splits. Hence impossible for any m>=1. This is a general all-n family (parametrized by k, total size n=2^k). This disproves the idea that divisibility+power-of-two ratio is sufficient; the obstruction is the automorphism/isomorphism constraint on branch structure. Let us verify this carefully.
The counterexample is the family F_k = C_{2^k - 1} ∪ {y incomparable} (a chain of length 2^k - 1 plus one isolated element), with e(F_k)=2^k. The ratio to any F' is a power of two in principle, but branch-isomorphism is impossible: only y vs the middle chain element gives balanced split (|branch|=2^{k-1}) but branches are non-isomorphic (in one branch y becomes above the whole chain by transitivity, in the other y remains incomparable to many below middle); all other comparisons give unbalanced splits. This is an all-n family (n=2^k elements) where integer power-of-two ratio holds but no comparison stage is realizable under branch-isomorphism constraints.


## Other metadata

```json
{
  "finished_at": 1793376265.3127422,
  "started_at": 1793373798.9381154
}
```
