# adaptive-tree-verification-hardness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

n2smvz1W0iMb5d6Ax4jc27-offended

## exit_state

clearexit

## question

For a succinctly described adaptive comparison tree (or framed DAG) that claims to sort n elements within k comparisons, is the validity+height verification problem complete for coNP or harder under the unary input encoding?

## basis

Parberry showed sorting-network verification is NP-complete (fixed networks); adaptive comparison trees are a different object and framed DAG soundness is only partially characterized.

## falsifier

Show polynomial-time verification for all valid inputs via a uniform algorithm, or prove coNP-completeness (model-preserving) distinguishing this adaptive case from Parberry's fixed-network verification.

## implication

CoNP-complete verification would create a gap between existence of a certificate and efficient checkability depending on representation, informing the NP-membership question for SORT-BOUND-U without conflating with network verification.

## finding_unverified

. If the certificate is given as a succinct DAG (polynomial size), checking is in $P$.

### Concrete failed/refuted approaches
- **"Mimic Parberry directly":** Try to reduce some NP-complete problem to "this adaptive strategy fails" - fails because the "program" is a strategy (adversarial responses are already handled by the strategy branches; failure would mean the strategy is not a valid sorter, which is a local/structural property, not "exists some input the network miscomputes" in the circuit sense). The quantifier structure is inverted by representation.
- **"Treat framed DAG as a circuit and apply Parberry":** Framed DAGs use comparisons+permutations and meet/intersection annotations (a kind of strategy with guaranteed information). This is not a fixed comparator network computing a function for all inputs without strategy structure - it's explicitly a strategy. No obvious model-preserving reduction found; attempts hit the representation distinction.
- **"Use counting (#P) as coNP-hardness":** Counting $e(P)$ is #P-complete but verification of the strategy doesn't require computing $e(P)$ values unless someone uses a particular (possibly inefficient) annotation scheme; the checker only needs to verify the meet/intersection is done correctly per the grammar rules ([research-framed-certificate-frontier.md:170-215] discusses entropy/forgetting as analytic conditions, not verification rules).

### Honest limits / obstruction
- **No proof of coNP-completeness.** I cannot construct a model-preserving reduction from a coNP-complete problem to adaptive strategy verification; the natural reductions fail due to strategy representation. This is a refutation of the analogy, not a proof that it's in $P$ by some other means.
- **Completeness is the hard/open part.** Even if verification is in $P$, we do not know if every $n$ has a polynomial-size framed/adaptive strategy certificate at height $S(n)$ (cf. [research-framed-certificate-frontier.md:220-240]). That’s exactly what affects $NP$-membership of $SORT-BOUND-U$: $SORT-BOUND-U \in NP$ iff there is a polynomial (in unary input length $m=\Theta(n\log n)$) succinct certificate for $S(n)\le k$. Verification being easy is necessary but not sufficient.
- **Model details matter.** If "succinctly described" allows adversarial encodings, or if annotations are untrusted in a weird way, need to be careful - but standard complexity assumptions say description is given and we verify it. Also need to distinguish "tree" (possibly exponential) vs "succinctly described" (DAG/compressed). The front says "succinctly described", so we’re in compressed case.
- **No Lean/repo changes.** No new theorem/counterexample of publishable/substantive form found; just a representation-level distinction clarifying the frontier.

**Bottom line:** The falsifier "prove coNP-completeness (model-preserving) distinguishing this adaptive case from Parberry's fixed-network verification" is refuted by the representation distinction. The correct complexity split is: **fixed-network correctness = coNP-complete (circuit/universal over inputs, no strategy)** vs **adaptive strategy validity = in P (strategy verification by backwards induction/meet-checking)**. Therefore coNP-complete verification is not the case here; the gap (if any) is between existence of certificates and their size (completeness), not between existence and efficient checkability. This directly informs $NP$-membership of $SORT-BOUND-U$ without conflating the models.

## Other metadata

```json
{
  "finished_at": 1793830239.967006,
  "started_at": 1793830018.1179636
}
```
