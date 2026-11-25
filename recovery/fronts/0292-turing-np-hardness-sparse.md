# turing-np-hardness-sparse

## status

investigated

## origin

ai_proposal_unverified

## agent_id

jzrRz3Tdzqi0TmzbWNiINS-parietal

## exit_state

clearexit

## question

Is the unary threshold language SORT-BOUND-U NP-hard under polynomial-time Turing reductions, or can this be ruled out without collapsing P to NP?

## basis

SORT-BOUND-U is sparse (problem.md); Mahaney rules out many-one NP-hardness unless P=NP, while Ogiwara–Watanabe give PH collapse to Δ₂P for Turing NP-hardness of sparse sets.

## falsifier

Exhibit a polynomial-time Turing reduction from some NP-complete language to SORT-BOUND-U, or prove unconditionally that no such reduction exists via the Ogiwara–Watanabe sparse-set theory.

## implication

Polynomial-time Turing NP-hardness of a sparse set in PSPACE would imply the polynomial hierarchy collapses to Δ₂P; ruling it out would clarify the boundary beyond Mahaney's many-one case.

## finding_unverified

 of the sparse set.
- **Application to SORT-BOUND-U (deduction):** From sparsity + OW: `SORT-BOUND-U` is not NP-hard under `≤_T^p` unless `PH ⊆ Δ₂P`. This is a *conditional* barrier (collapse of PH to Δ₂P), not an unconditional proof of non-hardness. It is strictly weaker in the "rule out now" sense than Mahaney: Mahaney needs only `P!=NP` to rule out many-one; OW needs `PH ⊈ Δ₂P` (a stronger separation/open collapse, above P!=NP in the sense that P!=NP does not imply PH!=Δ₂P) to rule out Turing NP-hardness. Also `SORT-BOUND-U` being in PSPACE means Turing NP-hardness would already place NP inside PSPACE (trivial) but combined with sparsity gives the PH collapse consequence.
- **Certificate/soundness vs completeness (deduction):** Exhibiting an optimal sorting tree is not an NP certificate (tree may be exponentially large). The Brightwell–Winkler `#P`-completeness of counting linear extensions is a general-poset result; there is no function reduction `S(P)=f(e(P))` in general (Prop 5.1 in hardness-boundaries) so counting linear extensions hardness does not transfer to `S(n)` without an encoding-preserving reduction from some NP-complete language *directly* to the `S(n)` minimax (uniform/unary-threshold) decision. Soundness of any candidate certificate must be distinguished from completeness of the language.
- **Exact falsifier answer:** 
  1. **Exhibit a `≤_T^p` reduction from some NP-complete language to `SORT-BOUND-U`:** No such reduction is known. The sparse+minimax structure plus general-poset non-transfer suggests a high barrier, but not an obvious combinatorial obstruction obvious from existing texts.
  2. **Prove unconditionally no such reduction exists via Ogiwara–Watanabe:** Not possible. OW is a *conditional* theorem (hardness => PH collapse), not an unconditional non-reducibility result. The theory provides the obstruction "if you can do Turing NP-hardness, you get PH⊆Δ₂P"; to rule out Turing hardness *without collapsing P to NP* you would need that the collapse target `Δ₂P` is already ruled out relative to PH (i.e. `PH ⊈ Δ₂P`), which is not known. Also one cannot get unconditional rule-out from sparsity alone for Turing reductions (contrast with many-one). 
- **Honest limits:** The frontier question is sharp. The standard sparse-set theory gives the exact boundary: many-one ruled out unless P=NP; Turing ruled out unless PH collapses to Δ₂P. There is currently no unconditional proof ruling out `≤_T^p` NP-hardness of `SORT-BOUND-U`, and no known reduction. The consequence is real (`PH ⊆ Δ₂P` is a strong collapse) but not the same as P=NP. No Lean/repo changes warranted by existing theory alone. A genuine advance would require either a reduction (unlikely given barriers+non-transfer) or a new theorem extending OW/unconditional sparsity arguments to rule out Turing hardness for this specific class without full PH collapse - none obvious from the studied literature.

**Concrete failed/obstructed angle:** Trying to port Brightwell–Winkler/#P-completeness directly fails by certificate-size/non-determinism mismatch and by the `S(P) != f(e(P))` obstruction (general-poset counting hard but the *minimax comparison cost* is not determined by extension count). Any attempted reduction must bridge from NP (existential witnesses over assignments) to the comparison-minimax/antichain structure of total orders with all-n uniformity and unary encoding - no standard bridge is apparent; sparsity blocks many-one and forces PH collapse for Turing.


## Other metadata

```json
{
  "finished_at": 1793830175.9097009,
  "started_at": 1793830017.2238364
}
```
