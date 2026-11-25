# recursive-mass-divisibility-tight-height

## status

investigated

## origin

ai_proposal_unverified

## agent_id

N3OoWDMN5K9hnRKtdg84Cj-hectic

## exit_state

clearexit

## question

For the n-element antichain, define M(T) as the multiset of outcome masses at nodes of a framed comparison tree T; is there an all-n obstruction forcing that for every T with height = ceil(log2 n!) there is some node v and some allowed framed leaf class size e(F') with e(F') not dividing the number of extensions passing through v consistent with any sound framing below v?

## basis

Root divisibility is necessary but not sufficient; docs/research-exact-reset-realizability.md shows single-level obstruction; need all-level (recursive) falsifiable test distinguishable from heterogeneous frame freedom.

## falsifier

Exhibit an infinite sequence of odd/even n with explicit height-ceil(log2 n!) framed trees T_n having every node mass divisible by the gcd of sizes of some compatible framed class families below it (a kind of 'divisible refinement'), or give a general factorization theorem for some nontrivial class.

## implication

A universal recursive obstruction would rule out all framed certificates at information-theoretic height for infinitely many n without assuming exact resets, directly impacting the NP-certificate completeness question for SORT-BOUND-U while remaining about certificate soundness/completeness rather than class separations.

## finding_unverified

Let us first look up the full user message again carefully. The user says "On billy-dev ONLY..." and gives the full prompt with the FRONT/FALSIFIER/COMPLEXITY IMPLICATION. This reads like instructions for what to do - perhaps the task is to actually do this research? Let us look up the environment again - we are in the repo, on billy-dev context. The instructions say "You have access to a set of tools..." - we need to satisfy the user's request.

Let us think through this.

Let us start by exploring more concretely and then writing up analysis.

Let us start by exploring systematically.

Let us first understand the mathematical structure better.

Let us analyze this carefully.

Let us also think about trying to find counterexamples by attempting to construct such trees for some n. But without more concrete specification of "allowed framed leaf classes" and "framing" in this exact model, it's hard to be certain. But I should report honestly as the instructions say.

I examined AGENTS.md, docs/problem.md, and the repository state (current worktree at recursive-mass-divisibility-tight-height on billy-dev). The exact-reset note shows a single-level divisibility obstruction (A_n -> V_n impossible for odd n because root split n!/2 not divisible by e(V_n)=(n-1)!, framing doesn’t help). The front asks for a recursive/all-level divisibility obstruction for framed comparison trees of height h=ceil(log2 n!) to some allowed framed leaf class.

Key points from analysis:
- If allowed framed leaf classes include e(F')=1 (total orders), 1 divides everything so obstruction cannot hold.
- Every positive integer is realizable as some poset’s e(F') (e.g. disjoint union chain-of-1 and chain-of-m-1 gives C(m,1)=m); homogeneous fixed-F' resets are very strict, heterogeneous class families give more flexibility. Also root antichain splits are forced balanced for any comparison.
- For sorting to total orders, using e(F')=1 refinement is always divisible; no obvious obstruction. In framed certificate DAGs (with joins) there is more flexibility than trees.
- Without a precise combinatorial specification of “allowed framed leaf classes” and framing constraints in this model, the universal obstruction cannot be definitively proved or disproved from stated info. It’s a plausible generalization if allowed class set is strongly restricted (excludes trivial classes, requires homogeneous types) AND forced splits create recursive problems; conversely it appears falsifiable via heterogeneous refinement or allowing trivial classes. Any conclusive result would require independently checkable formalization of those constraints.

No repository/Lean changes made (not obviously substantive independently checkable theorem/counterexample found under current model ambiguity). Tests pass (168 tests OK).

## Other metadata

```json
{
  "finished_at": 1793698896.5361173,
  "started_at": 1793693040.0330062
}
```
