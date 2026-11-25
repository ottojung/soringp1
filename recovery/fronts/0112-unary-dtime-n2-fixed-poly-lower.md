# unary-dtime-n2-fixed-poly-lower

## status

investigated

## origin

ai_proposal_unverified

## agent_id

W3W27rMUBB5WLVWQcEdnsU-passport

## exit_state

clearexit

## question

Is SORT-BOUND-U in DTIME(N^2) for unary input length N=n+k+1, or is there an all-n lower bound forcing runtime >= c N^2 on infinitely many inputs?

## basis

problem.md states fixed-polynomial lower bounds like SORT-BOUND-U ∉ DTIME(N^2) have no known technique and are not blocked by P!=PSPACE equivalences.

## falsifier

Construct a uniform DTIME(N^2) decider for SORT-BOUND-U on all unary valid inputs with a correctness argument, or disprove for all c by an adversary/incompressibility argument for all large N.

## implication

A fixed-polynomial lower bound would be a first step below exponential/PSPACE without implying P!=PSPACE directly; refutation would tighten time bounds for the unary game.

## finding_unverified

e. Or related to "coin weighing" no. Or more directly related to the "minimum comparison sort" which is a standard problem - but complexity of computing S(n) itself?

Another angle - there’s work by Fredman (1976) on sorting networks, but adaptive? Or the "decision tree complexity" of the sorting function vs computing its depth. Also Yao’s principle? Maybe use adversary arguments on the algorithm.

Alternatively, look up known results about complexity of S(n). Let us search more in the repo.
Let us start by exploring more of the codebase and understanding the full picture.

Let us start by exploring the full picture more carefully.

Let us look up the exact model again - "inputs are n distinct labelled keys" - so elements have fixed identities (e.g., they are the specific items with those labels). The comparison is between keys. So the poset is on labelled elements, not unlabeled up to isomorphism. That matches the budgeted DFS using indices 0..n-1 as fixed labels.

Let us start by analyzing the problem carefully.

Let us think systematically about how to attack this.

Let us look up the full context again.

Studied AGENTS.md, docs/problem.md, docs/literature.md, docs/research-winning-frontier-barrier.md, docs/research-budgeted-dfs.md, docs/research-encoding-consequences.md, docs/research-hardness-boundaries.md, docs/research-certificates-barriers.md. 

**Claim:** Is SORT-BOUND-U ∈ DTIME(N^2) for N = n+k+1 (unary input)? Or is there an all-n lower bound forcing runtime ≥ c N^2 infinitely often?

**Structure (facts):** SORT-BOUND-U = {1^n # 1^k | S(n)≤k} is a sparse tally threshold (P/log), in PSPACE∩EXPTIME (budgeted DFS 2^(O(N log N))). f(n)=n+S(n) strictly increasing gives cutoff t_N; advice trivial but uniform computation hard. General-poset hardness/certificates don't transfer (soundness≠completeness). Circuit lower bounds blocked (trivially in P/poly); many-one EXPTIME/NP-hardness blocked by sparsity (Berman–Hartmanis/Mahaney).

**Attempt 1 (construct DTIME(N^2) decider):** Need to compute/find cutoff uniformly in time quadratic in N. Reduces to computing S(n). Best known is exponential in n log^2 n (poset DP with symmetry quotient still exponential in n^2); winning frontier gives 2^(Ω(n log^2 n)) winning states. No known formula, exact values only to n≤22, selective search not obviously polynomial. No clear polynomial algorithm path found.

**Attempt 2 (disprove by adversary/incompressibility):** Time hierarchy doesn't directly apply to this specific structured sparse language; diagonalizing against DTIME(N^2) won't obviously yield this threshold. Winning frontier shows exponential state space but doesn't force enumeration (selective search not excluded). Repo diagonal construction shows recurrences alone don't force P, but S(n) has sorting-specific structure (must realize a comparison tree for all permutations) — unclear if this helps or hinders. No clean adversary/incompressibility argument found; problem.md explicitly states no known technique for fixed-polynomial lower bounds like SORT-BOUND-U ∉ DTIME(N^2).

**Conclusion:** Neither direction provably resolved with current techniques. Obstruction to upper bound is exponential state space with no known polynomial method; obstruction to lower bound is lack of applicable techniques given sparsity/P/log/P/poly structure. Question remains open — consistent with repo's assessment that fixed-polynomial lower bounds have no known technique and aren't blocked by P!=PSPACE equivalences.


## Other metadata

```json
{
  "finished_at": 1793469618.3376484,
  "started_at": 1793464278.9717484
}
```
