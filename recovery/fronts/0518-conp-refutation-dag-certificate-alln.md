# conp-refutation-dag-certificate-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

PLSzcYBBbAMmRTDsurPYGt-wooded

## exit_state

clearexit

## question

For all integers n >= 1 and k >= 0 with S(n) > k, does there exist a polynomial-time verifiable refutation object of size polynomial in the unary input length N = n+k+1 proving that every adaptive comparison strategy on n keys requires more than k comparisons?

## basis

docs/problem.md (open NP/coNP membership, explicit trees not certificates), docs/research-encoding-consequences.md Theorem 5.4 and open certificate table, docs/research-strategy-certificates.md Remarks 1.3/4.3; distinct from prior yes-certificate, membership-polynomial, and framed-DAG fronts.

## falsifier

Exhibit an explicit infinite family (n_i,k_i) with S(n_i)>k_i for which every sound refutation system checkable in time poly(N_i) requires certificates of superpolynomial size in N_i, or prove an unconditional superpolynomial lower bound for a natural complete refutation format.

## implication

A uniform positive answer would place SORT-BOUND-U in coNP, strengthening the known PSPACE upper bound without implying a separation; a verified lower bound would rule out an entire class of succinct no-certificates for exact unary threshold evaluation.

## finding_unverified

-root family in the hard regime) would require a structural theorem about unavoidable branching/sharing in optimal adversary play against *all* sorter strategies from the root. General-poset “game” hardness results do **not** supply this for the fixed family of antichains `{[n]}` without an encoding-preserving reduction (and such reductions are constrained/unknown here; sparsity barriers concern a different direction).
- **Soundness vs completeness:** Many candidate invariants/potentials are **sound** lower bounds on restricted forms or give one-sided certificates but are not known **complete** for all `S(n)>k` (cf. info bound, partial heuristics). A lower bound against an incomplete format would **not** satisfy the front as stated.

## Concrete failed approach (this session)
- **Attempt:** Derive either (a) a succinct universal coNP certificate schema for all `S(n)>k`, or (b) an explicit hard-regime infinite family forcing superpolynomial size in the canonical complete adversary-strategy refutation DAG (or in all poly-time verifiable sound systems) from the comparison-game minimax recurrence plus known bounds/barriers.
- **Outcome:** (a) blocked by absence of any known polynomial bound/control on complete adversary/universal branching over all sorter moves (and no usable compression theorem for the root family); (b) blocked by lack of a root-specific unavoidable-size theorem and by the fact that the fully general “every sound system” falsifier would entail an unconditional `∉ coNP`-type consequence not supported by available methods/sources. Only the tautological/easy regimes (e.g. `k < ⌈log2 n!⌉`) admit immediate short refutations.

## Exact obstruction
A decisive answer to the front requires one of:
1. **Positive (all `n`):** a **complete and sound**, polynomial-time checkable refutation system together with a proved `poly(N)` size bound for **every** NO instance `(n,k)`, `S(n)>k` (equivalently a uniform proof that `SORT-BOUND-U ∈ coNP` via explicit NO witnesses); or
2. **Negative (as falsifier):** an explicit infinite hard-regime family `(n_i,k_i)` and a rigorous superpolynomial certificate-size lower bound against **every** sound poly-time verifiable refutation system (or, at minimum, an unconditional superpolynomial lower bound for a precisely specified **natural complete** format, proved for that family).

The blocking mathematical object is a **uniform, root-anchored (antichain) completeness-and-size theorem** for NO-certificates: either a compressible complete adversary proof of minimax value `>k`, or an unavoidable superpolynomial branching/information lower bound for such proofs in the regime `⌈log2 n!⌉ <= k < S(n)`. No such theorem or counterexample was established here.

## Conclusion (labeled)
- **Status:** **open / unresolved** by this investigation. No genuinely substantive, independently checkable new theorem or counterexample was found, so no repository/Lean changes were made.
- **What is clear (deduction/literature):** uniform poly-size refutations for all NO instances ⇔ `SORT-BOUND-U ∈ coNP`; canonical minimax adversary certificates are sound and complete in principle but of unknown size; easy NO instances below the information bound have short refutations; general-poset/network hardness results and sparsity barriers do not settle this front for `S(n)`.
- **Process note:** no external side effects were taken; this is a mathematical negative/obstruction report, not a proof of membership, non-membership, or separation.

## Other metadata

```json
{
  "finished_at": 1794896858.3316944,
  "started_at": 1794896214.199139
}
```
