# framed-certificate-tightening

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ffxVYer9HHgAn4sU0TZ9pD-stones

## exit_state

clearexit

## question

Prove or disprove that there exists an all-n family of framed comparison histories with polynomially many classes forming a locally-checkable exact certificate for SORT-BOUND-U, identifying the exact obstruction from the odd-star/reset divisibility results.

## basis

Framed certificate frontiers, research-exact-reset-realizability.md, and #301 discussion of certificate soundness versus completeness.

## falsifier

Extend the odd-ratio/reset obstruction to all mixed boundary families for all large n, or give an explicit all-n constructive certificate with a completeness proof.

## implication

Resolving this would settle whether the framed-certificate route can yield an NP certificate for the unary threshold, directly addressing the core NP-membership question in model-fidelity terms.

## finding_unverified

t each node, every input order consistent with the comparison history so far is in the set represented by R (all extensions of R that are still feasible). And intersection means R only gets stronger (more relations) when branches merge. So merging/joins are forgetful - you can only add constraints, you lose the ability to distinguish branches that had different possibilities except through what remains common.

Also "framed comparison histories with polynomially many classes" - perhaps equivalence classes of comparison histories under some congruence that preserves the state up to framing, and polynomially many classes means the quotient DAG is small. This is similar to the quotient certificate idea in strategy certificates.

But can we do this for all n with exact height S(n)? The odd-star/reset obstruction was about exact resets (exact classes). Maybe even with forgetful joins, you get similar divisibility/incompatibility obstructions?

Or another way: to achieve exact height S(n) with polynomial compression, you need to be able to merge states in a way that preserves optimality. The branch divisibility obstructions constrain what merges are possible.

Alternatively, looking up the "mixed boundary families" - perhaps families of boundary posets that mix different structures (like in some insertion schemes), and the obstruction extends to all such families, showing you can't form a uniform polynomial family of classes for all n.

Let us look up more about the root-reachable-certified-quotient front again: it wants "a candidate exact root-reachable equivalence of optimal comparison histories stronger than relabelled-poset isomorphism, with an explicitly checkable two-outcome congruence and a polynomial bound on distinct classes for all n". So quotienting comparison histories (paths in the decision tree) up to some equivalence. Polynomially many classes would mean the quotient is polynomial size.

The odd-star exact reset was impossible due to divisibility - but if you allow forgetful behavior, maybe different issues arise. Or perhaps the obstruction generalizes.

Let us analyze this carefully. The key phrase: "all-n family of framed comparison histories with polynomially many classes forming a locally-checkable exact certificate for SORT-BOUND-U". "Exact certificate" - in the framed certificate grammar (checker), the certificate gives height <= k and is sound. To get exact height = S(n), we need the certificate to achieve exactly the optimal height. Also "exact" might be used to distinguish from forgetful/approximate. 

Let us write the report.

I've studied AGENTS.md, docs/problem.md, the board #301 context, the framed-certificate frontier, the exact-reset realizability note, the strategy-DAG/quotient materials, and the checker. The odd-star exact-reset obstruction is a partitioning/divisibility obstruction (needs e(F') | e(P) at every state under balanced splits) — forgetful framed certificates use intersection at joins (merges, making guaranteed posets weaker and e(Q) larger), so they do not require exact partitioning into fixed-size classes; leaves only need to be total orders. I found no precise definition of "mixed boundary families" in the repo to attack as specified, no explicit generalization, and the quotient needs a canonical summary not yet specified. No theorem/counterexample established; the precise obstruction from those divisibility results to forgetful framed certificates remains unidentified. No repo/Lean changes made.

## Other metadata

```json
{
  "finished_at": 1793623031.1414504,
  "started_at": 1793621161.0378747
}
```
