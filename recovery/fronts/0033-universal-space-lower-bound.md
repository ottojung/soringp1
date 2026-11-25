# universal-space-lower-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

bT9QKMjQCSjAyHYcTUY33X-polite

## exit_state

clearexit

## question

Does every correct uniform deterministic algorithm for deciding SORT-BOUND-U on unary input of length N use Omega(N log N) bits of work space, not just the transcript-DFS family?

## basis

docs/research-budgeted-dfs.md gives O(N log N) space for transcript DFS; docs/research-plan.md lists space reduction as open; prior linear-space-unary-decision analyzed only that family and left general lower bounds unaddressed.

## falsifier

Construct a correct uniform algorithm deciding SORT-BOUND-U in o(N log N) work space with a rigorous cost analysis, or prove a general Omega(N log N) space lower bound for all uniform algorithms.

## implication

A universal space lower bound would show the existing O(N log N) budgeted DFS space bound is asymptotically tight for all uniform methods and sharpen the space frontier beyond family-specific arguments.

## finding_unverified

on't need to store the full history if you use certain orderings? Probably not obvious here.

Alternatively, think about the fact that this is similar to some "graph searching" or "path constraints" - not obviously giving a standard lower bound.

Alternatively, consider that the number of possible different partial orders reachable within k steps is large? Or use a direct information-theoretic lower bound: the algorithm must distinguish between different instances? Or the configuration space is large.

Alternatively, think about the input length N = n+k+1. The answer depends on n,k. To compute it correctly for all n,k, maybe need to store n,k and also work space - but n,k are in input. Or think about the "advice" or just the computation state.

Alternatively, use the fact that if you have less than c*N*log N space, by pigeonhole principle you must repeat configurations in some way? But for exponential time computation that's possible to repeat (that's what happens with memoization), but without memoization...

But the transcript DFS doesn't memoize and still uses O(N log N) space. Can we do better than O(N log N) without memoization?

Alternatively, is there a lower bound argument: any correct algorithm for the comparison-based sorting decision problem must store Ω(n log n) bits of information about the comparisons made so far? Because there are (n!) possible orderings and you need to distinguish them - similar to sorting lower bounds. But how does this translate to space?

In the comparison model, space is sometimes considered differently, but in standard computation model...

Also the input is just n,k (unary) - the actual permutation is not given as input; the algorithm must determine the sorting number which is a property of all permutations. That is different from sorting a given list.

Yes! This is important - "Inputs are n distinct labelled keys" but for computing S(n) as function, the input is just 1^n. For the decision problem SORT-BOUND-U, input is 1^n # 1^k. The algorithm needs to figure out the worst-case number of comparisons needed to sort ANY permutation of n elements - it's a property of the sorting problem size, not sorting a specific input. That makes it different from the standard sorting algorithm.

So it's about the complexity of the sorting *number*, not about sorting a particular list. That changes things completely.
Let us look up the literature on space complexity of sorting and related problems more. Also look up the exact values - maybe think differently.

Let us understand the question carefully and try to attack it.

Let us look up the problem more carefully and think.

Let us analyze the question thoroughly and write up the findings.

Based on studying AGENTS.md, docs/problem.md, docs/research-budgeted-dfs.md, docs/research-plan.md, and the codebase: the control-stack/tree-evaluation argument suggests a universal Ω(N log N) lower bound is plausible (depth k with branching factor Θ(n^2) requires Θ(k log n) position/history bits, recomputation doesn't obviously save space), while known optimizations (Savitch for reachability, hybrid representations) don't break the worst-case O(N log N) bound. No concrete o(N log N) algorithm was found; the lower bound remains to be fully rigorously proven against all paradigms, but the asymptotic tightness conjecture is well-motivated. This is a polynomial (linearithmic) lower bound question which appears in scope per problem.md's "fixed-polynomial lower bounds" discussion.


## Other metadata

```json
{
  "finished_at": 1793336568.837076,
  "started_at": 1793332089.2161734
}
```
