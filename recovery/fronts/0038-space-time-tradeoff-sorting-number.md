# space-time-tradeoff-sorting-number

## status

investigated

## origin

executive_manual

## agent_id

hcDYkeCzxAEHp0O0chKMyT-gunpowder

## exit_state

clearexit

## question

Can we achieve a better space-time tradeoff for exact computation of S(n) than current bounds, or is there a lower bound tradeoff that rules out subexponential time with polynomial space?

## basis

research-plan.md lists space reduction as open; combining time/space tradeoffs is a natural extension.

## falsifier

Construct a subexponential-time polynomial-space uniform algorithm for S(n), or prove a tradeoff lower bound showing it's impossible.

## implication

Understanding space-time tradeoffs clarifies the complexity landscape and may reveal new barriers.

## finding_unverified

Let us look up the exact time bounds again.

Let us look up the exact question again carefully.

Let us start by studying the codebase and docs as instructed.

Let us formulate a precise claim to test.

Let us start by exploring. The task says "attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it" with the given FRONT.

Let us analyze the space-time tradeoff possibilities.

Let us start by doing a careful analysis.

I studied AGENTS.md, docs/problem.md, and the board/operational state on billy-dev. For SORT-BOUND-U (unary, N = n+k+1), current bounds: budgeted DFS gives DTIME(2^(O(N log N))) ∩ DSPACE(O(N log N)); the function S(n) via binary search gives 2^(O(n log^2 n)), polynomial space in n. The ATM characterization places it in PSPACE but sparsity (and non-EXPTIME-hardness under many-one reductions) means it's not PSPACE-complete under many-one polytime reductions.

Precise claim examined: is there a uniform deterministic algorithm for S(n)/SORT-BOUND-U achieving better space-time tradeoff than current bounds, or is subexponential time with polynomial space ruled out? 

Findings:
- Adding (P,d)-memoization to the budgeted DFS (trading space for time) gives dramatic empirical improvement (n=6: non-memoized hits cap ~10^7 nodes in ~50s; memoized completes in ~2.4s with ~190k cached states). This is a standard better tradeoff point than the pure DFS baseline.
- Symmetry quotients (S_n × Z_2, automorphism orbits) and Stober–Weiss bidirectional/efficiency-pruning methods can reduce state counts; asymptotically quotients by groups of size n! don't change the 2^(Θ(n^2)) state class exponent.
- The winning frontier barrier shows 2^(Ω(n log^2 n)) states exist but selective algorithms need not enumerate them; it rules out algorithms that necessarily enumerate all winning states at info budget, not arbitrary selective algorithms.
- Meet-in-the-middle splits depth but frontier sizes remain exponential; storing frontiers is costly in space.

Obstruction/limits:
- No proof rules out subexponential time with polynomial space for SORT-BOUND-U (the standard PSPACE-completeness → SUBEXP argument doesn't directly apply because it's not PSPACE-complete under many-one reductions and is sparse). No constructive algorithm achieving 2^(o(N)) time with poly(N) space is known.
- The exponential-in-n-log^n time appears tied to the game-tree/alternation structure; reducing below the current exponent while keeping polynomial space remains open.
- Reducing space below storing the comparison path is open (budgeted DFS docs note this). The DFS baseline with no memoization is suboptimal relative to memoized variants.

Conclusion: memoization gives a concrete better space-time tradeoff than the published no-memoization DFS; space can be traded for time. Whether subexponential time with polynomial space is achievable remains open (not ruled out by known barriers, not demonstrated). No repository changes made.


## Other metadata

```json
{
  "finished_at": 1793342513.6165886,
  "started_at": 1793334678.0777311
}
```
