# tally-np-membership-collapse

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UgSATTj6k3AaPTDtjd6XML-pieces

## exit_state

clearexit

## question

Is there an all-n polynomial-time many-one reduction from some NP-complete language to SORT-BOUND-U, or is NP membership of SORT-BOUND-U provably false under known barriers without implying P=NP?

## basis

Mahaney/Fortune and Book's theorem for tally sets; SORT-BOUND-U is sparse unary tally-like language with no known polynomial certificate.

## falsifier

Construct an explicit polynomial-time many-one reduction from SAT to SORT-BOUND-U preserving the unary/threshold encoding, or prove NP ∩ TALLY ⊆ P follows from such a reduction in a way inconsistent with Mahaney/Book theorems.

## implication

NP membership would be a major structural breakthrough; ruling it out would sharpen the boundary between certificate existence and the sparse/tally structure.

## finding_unverified

Let us look up more about complexity of S(n). Also look at the full literature more and any other docs.

**Finding (mathematical):**

- **Reduction/hardness (many-one):** `SORT-BOUND-U` is sparse (≤ O(L²) strings up to length L). By Mahaney’s theorem, if it were NP-hard under polynomial-time many-one reductions then `P=NP`. No explicit all-n poly-time many-one reduction from any NP-complete language is known. Known barriers rule out *completeness/hardness* via this route without assuming `P!=NP` is false; they do **not** construct such a reduction.
- **NP membership:** Not ruled out by Mahaney/Book/Fortune. `P=NP ⇔ NP ∩ TALLY ⊆ P` (Book), so showing `SORT-BOUND-U ∉ NP` alone would not imply `P!=NP` (other tally languages could still be). Ladner-style intermediate behavior is consistent with sparsity in principle. No known theorem provably falsifies NP membership of this specific combinadic/tally threshold language without implying a class collapse.
- **Distinctions:** (a) NP-hardness ≠ NP membership. (b) Certificate *soundness* vs *completeness* matters — an exponential tree is not a polynomial certificate; absence of a known polynomial certificate is not a proof of non-membership. (c) General-poset NP-hardness (Hyafil–Rivest, min-height/verification) does not transfer to the fixed family `S(n)` without an encoding-preserving reduction; that’s a transfer barrier, not a membership barrier.
- **Concrete obstruction:** The natural candidate certificates (optimal comparison trees, full DP tables) are exponentially large in input length for nontrivial instances; proving no polynomial certificate exists would require a lower-bound argument for this exact language, which is not provided by sparsity alone. Any attempt at a SAT→SORT-BOUND-U many-one reduction must bridge “constraint satisfaction” to “exact minimax height of comparison sorting” for all n simultaneously while preserving unary threshold encoding and producing only strings in `SORT-BOUND-U` with correct yes/no — no such bridge is obvious and we found no published reduction; generic poset results fail the “fixed family S(n)” transfer requirement.

**Conclusion:** NP membership remains open. The decisive barrier is to **hardness** (sparsity + Mahaney), not to membership. A serious falsifier must either produce an explicit reduction (and accept the P=NP consequence if combined with membership) or find a new theorem ruling out NP membership without collapse — neither is apparent from known literature. No repository changes are justified by a new theorem/counterexample at this time.


## Other metadata

```json
{
  "finished_at": 1793354386.4756894,
  "started_at": 1793354048.4366043
}
```
