# sparse-turing-np-hardness-collapse

## status

investigated

## origin

ai_proposal_unverified

## agent_id

xW8zeqcqR3vl4eOAEBD6dH-overborne

## exit_state

clearexit

## question

Does polynomial-time Turing (Cook) reducibility of NP-complete languages to SORT-BOUND-U, despite its sparsity, force a collapse of the polynomial hierarchy beyond P=NP, and is such Turing-hardness compatible with known Mahaney obstructions?

## basis

SORT-BOUND-U is sparse (Mahaney), many-one NP-hardness => P=NP; Ogiwara–Watanabe theory covers bounded Turing reductions for sparse sets, unbounded Turing cases give PH collapses in some forms - unexplored for this exact tally language.

## falsifier

Exhibit a formal barrier showing that Ogiwara–Watanabe or related sparse Turing-hardness consequences do not apply here due to the specific structure of SORT-BOUND-U, or construct an explicit Turing reduction from some NP-complete language to SORT-BOUND-U for all relevant n.

## implication

Establishing Turing-hardness of SORT-BOUND-U for NP would have major complexity consequences distinct from many-one reductions; ruling it out would close a plausible route around Mahaney's barrier.

## finding_unverified

context.

Let us read the key docs on this topic.

Let us look up more details about Ogiwara–Watanabe and also think about structure of S(n).

**Claim under test (falsifiable):** If some NP-complete language is polynomial-time Turing (Cook) reducible to `SORT-BOUND-U` (sparse unary tally), does that force a collapse of the polynomial hierarchy beyond `P=NP`? Is such Turing-hardness compatible with known Mahaney obstructions?

**Analysis (paper argument):**

- `SORT-BOUND-U = {1^n#1^k : S(n) ≤ k}` is sparse (Lemma 3.1 in docs) and in fact `P/log` (Thm 3.7) / `P/poly` (Thm 3.3). 
- **Many-one:** Mahaney/Fortune show sparse NP/coNP-hard under ≤_m^p ⇒ `P=NP`. (barrier)
- **Bounded truth-table:** Ogiwara–Watanabe show sparse hard under bounded truth-table reductions from SAT ⇒ `P=NP`.
- **Unbounded Turing (Cook):** For any sparse (or more generally any set in `P/poly`) `S`, `NP ⊆ P^S ⊆ P/poly` (because the polynomially-many oracle answers up to needed length are encodable in polynomial advice). By Karp–Lipton, `NP ⊆ P/poly ⇒ PH ⊆ Σ_2^P`. This is the standard consequence (sometimes called “Mahaney for Turing” / follows from Karp–Lipton). Refinements exist if `S ∈ NP`, but the collapse to `Σ_2^P` is general.

**Conclusions:**
1. **Collapse beyond P=NP:** Yes. Turing-hardness of an NP-complete language to a sparse set implies `PH = Σ_2^P`. This is strictly weaker than `P=NP` in form but is a strong collapse of the hierarchy; it is a different (and in general expected) consequence than many-one hardness. So “beyond P=NP” in the sense of higher hierarchy collapse is forced.
2. **Compatibility with Mahaney:** Compatible. Mahaney blocks ≤_m^p reductions; Cook reductions are more powerful and are not blocked by Mahaney — they trigger the Karp–Lipton/PH-collapse consequence instead. The obstructions are reduction-class dependent, not contradictory.
3. **Structure-based barrier?** I see no formal barrier from the special structure of `SORT-BOUND-U` (monotonicity, threshold form, `P/log` advice) that evades `NP ⊆ P^{sparse} ⊆ P/poly ⇒ PH ⊆ Σ_2^P`. The structure is what makes it sparse/simple, not what protects against the oracle-advice collapse. The general theory applies directly.

**Failed/obstructed approach:** Trying to construct an explicit Turing reduction from some NP-complete language to `SORT-BOUND-U` seems implausible as a path — `SORT-BOUND-U` only provides threshold answers about a single function `S(n)` (the sorting number). Encoding arbitrary NP instances and extracting a yes/no via polynomially many queries to “is S(n_i) ≤ k_i?” is not obviously possible without computing S(n_i) itself; there is no known reduction in the literature and the function’s structure doesn’t suggest an obvious encoding. But this is a “no obvious reduction” / “hard to construct”, not a formal obstruction theorem. The formal obstruction to Turing-hardness is the complexity consequence (would imply PH collapse), not impossibility of construction.

**Honest limits:** The question as stated asks to “exhibit a formal barrier…” or construct reduction. I found no formal barrier specific to `SORT-BOUND-U` structure; the general sparse-set theory applies. I found no candidate explicit reduction. The key mathematical point is: Turing-hardness ⇒ PH collapses to Σ_2^P (distinct from Mahaney), and this is compatible with Mahaney (different reduction classes). No repository changes needed; this is a consequence of established theorems (Mahaney, Ogiwara–Watanabe, Karp–Lipton).

## Other metadata

```json
{
  "finished_at": 1793631226.3685648,
  "started_at": 1793631006.9124615
}
```
