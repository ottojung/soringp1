# orbit-quotient-exponential-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

CDgVkK09dgqGSWvsVwbsQY-regretted

## exit_state

clearexit

## question

For all sufficiently large n, is there an infinite family of partial orders reachable on some optimal sorting strategies from an n-antichain such that every automorphism-orbit quotient (under any canonical labeling scheme used by a uniform algorithm) still requires >= 2^(c n log n) distinct classes for some fixed c>0?

## basis

Prior automorphism-orbit-time-barrier investigation noted symmetry helps intuition but no all-n barrier proved; permutohedron/orbit structure and budgeted DFS state explosion remain unresolved.

## falsifier

Construct a uniform canonical labeling that maps every such family to < 2^(epsilon n log n) orbit classes for all sufficiently large n and all epsilon>0, preserving the exact minimax height information needed for S(n).

## implication

A global all-n obstruction would rule out naive symmetry quotienting as the source of a polynomial-time uniform evaluator for S(n) without changing the comparison model; a positive construction would give a concrete path to improved uniform bounds.

## finding_unverified

1} below and t_0 < ... < t_{m-1} above, and b_i below t_j iff i>=j. Yes, it's the comparability graph of the crown graph's order? Or it's a Ferrers diagram shape.

Also is there any reason this couldn't appear? Starting from empty, you can add relations one by one to build up any poset. So topologically it's reachable. Is there some optimal strategy that goes through it?

Maybe if we construct such a strategy. Or perhaps it's known that all "indecomposable" posets of certain types appear. But this is vague. Let us look up more about the state graph structure.
Let us study the full picture more.

Let us start by exploring the codebase more and understanding the full picture.

Let us look up the exact terminology from the codebase.

Let us understand this question deeply. The staircase posets have trivial Aut(P) - so no symmetry within the poset. If they appear on optimal strategies and form a large family with trivial automorphism groups and all pairwise non-isomorphic in some strong sense, then quotienting by automorphism orbits gives no help. Also are there exponentially many such states?

Also the information-theoretic bound is n log n. The number of states is related. Let us look up the question again more carefully.

Let us read more about the information budget / admissibility.

Worktree is clean — the interrupted turn caused no external side effects (only in-shell computations; no board posts, no commits). The heavy n=8 labelled-state run was the wrong tool anyway (labelled space is ~4×10⁸). I'll continue with the decisive computation using the quotient DP.
**Finding: no all-\(n\) theorem or counterexample was established.** The strongest concrete result is a formulation obstruction: counting poset isomorphism classes is not the same as proving a lower bound for every exact minimax quotient.

The existing board record reports a useful distinction. If “preserving exact minimax height” means only that equivalent states have the same \(F(P)\), grouping states by \(F(P)\) gives at most \(S(n)+1=O(n\log n)\) classes. That refutes any lower bound based on value preservation alone, but it is not a useful evaluator: computing the grouping requires knowing \(F\) already. A quotient usable by the minimax DP must also preserve the paired successor structure. The board’s finite bisimulation experiment reaches only \(n\le6\) and establishes no asymptotic bound.

The earlier counts \(1,2,5,12,19,134,802\) through \(n=7\) count isomorphism classes reached by repeatedly taking *locally minimax moves*. They do not settle the prompt’s broader “some optimal sorting strategy” wording, which can include slack subtrees. Nor do these finite counts establish either a \(2^{\Omega(n\log n)}\) lower bound or a \(2^{o(n\log n)}\) upper bound. The staircase construction is not a witness: at \(n=4,6\) it is not reached by locally minimax moves, and its shortest transcript plus \(F(P)\) exceeds \(S(n)\).

General-poset facts about asymmetric posets or many reachable states do not establish root-optimal reachability. Likewise, a sound verifier or a value-preserving class map does not establish completeness or a uniform exact evaluator.

**Exact unresolved obstacle:** characterize the states reachable on *some* height-\(S(n)\) strategy, including possible slack paths, and bound the number of classes in the coarsest quotient that preserves the two-outcome minimax transitions. The interrupted work made no board post or repository change; the worktree remains clean.

## Other metadata

```json
{
  "finished_at": 1793417517.07201,
  "started_at": 1793411287.0259624
}
```
