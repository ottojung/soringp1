# strategy-certificate-not-tree

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Mesql7TExS5V0kXEEQQPVX-brink

## exit_state

clearexit

## question

Is there a polynomial-in-n succinct certificate for S(n) <= k other than an exponentially large sorting decision tree, such as a compact recursive strategy with polynomially verifiable soundness and completeness?

## basis

Succinct-cert-complete-antichain front established NP-vs-PSPACE equivalence but left certificate existence open.

## falsifier

A proof that any sound-and-complete certificate for the antichain root must encode an exponentially large decision tree, or a concrete subexponential certificate family.

## implication

Membership of SORT-BOUND-U in NP or coNP would follow from a succinct complete certificate; ruling it out closes that route.

## finding_unverified

## Mathematical finding

**Claim attacked (all-n):** There is no polynomial-in-`n` succinct certificate for `S(n) ≤ k` whose *completeness* (every permutation is sorted within `k` comparisons by the encoded strategy) can be verified in polynomial time, other than (or compressing) an exponentially large sorting decision tree.

**Result:** The claim survives; the obstruction is the *completeness* side, not soundness.

**Reasoning.** A certificate for `SORT-BOUND-U` must witness *both* soundness (the encoded object sorts) and completeness (it sorts *all* `n!` permutations within `k`). Soundness of a compact recursive strategy (e.g. "split by a pivot, recurse") is polynomially checkable locally. Completeness is not: verifying that the strategy's decision tree has height `≤ k` on every root-to-leaf path requires, in the worst case, exhibiting/checking an exponentially large set of distinct paths (one per permutation, or equivalently a full decision tree of height `k` with up to `n!` leaves). A polynomial-time verifier cannot reconstruct or validate that the compact description's induced tree has no path longer than `k` without expanding it, because the number of distinct adaptive comparison sequences of length `≤ k` is exponential and the strategy's choices depend on outcomes. Hence a polynomially verifiable certificate would have to *contain* the exponential tree (or an equivalent exponentially large witness), defeating succinctness. This is exactly the standard obstruction: `SORT-BOUND-U ∈ NP` would require such a certificate, so this rules out the NP-membership route unless `NP = PSPACE` (which the project's own `SORT-BOUND-U ∈ PSPACE` bound makes equivalent to that separation). Soundness-only certificates (heuristics, partial strategies) are cheap and do not help completeness.

**Consequence for complexity:** Closes the "succinct complete certificate" route to `SORT-BOUND-U ∈ NP`/`coNP`. Membership in NP would require either an exponential certificate (not NP) or a new method bypassing the completeness expansion—none known. No new lower bound on `S(n)` itself follows; only the certificate-complexity frontier.

**Limits / honesty.**
- This is a *barrier argument*, not a proof that `SORT-BOUND-U ∉ NP` (that would imply `NP ≠ PSPACE`, out of scope and not achieved).
- It does not rule out *non-uniform* advice or circuits (tally ⇒ `P/poly`).
- It does not improve the exact evaluator or space bound.
- No repository/Lean changes warranted: no new theorem ripe for kernel-checking; the argument is a complexity-theoretic observation, not a formalized result.

**Next decisive obstacle:** whether there exists any subexponential (e.g. `2^{o(n log n)}`) complete certificate family, or whether completeness inherently requires full decision-tree size. This remains open. No repo changes made.

## Other metadata

```json
{
  "finished_at": 1794104878.9977272,
  "started_at": 1794104847.5102782
}
```
