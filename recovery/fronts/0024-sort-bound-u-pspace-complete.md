# sort-bound-u-pspace-complete

## status

investigated

## origin

manual_research

## agent_id

FVuav1E9v87V0GhT4A1vK1-diarsenol

## exit_state

clearexit

## question

Is SORT-BOUND-U PSPACE-complete under polynomial-time many-one reductions, or can the antichain symmetry of S(n) rule out PSPACE-hardness while preserving PSPACE membership?

## basis

docs/research-certificates-barriers.md establishes SORT-BOUND-U in PSPACE via alternating Turing machine (APTIME=PSPACE); docs/research-hardness-boundaries.md shows GEN-SORT complexity is open and antichain is the symmetric special case with different reduction properties than arbitrary posets.

## falsifier

Exhibit either a polynomial-time many-one reduction from some PSPACE-complete problem to SORT-BOUND-U (proving PSPACE-hardness) or an unconditional proof that SORT-BOUND-U has structural properties incompatible with PSPACE-completeness for all n.

## implication

PSPACE-completeness would mean P!=PSPACE iff SORT-BOUND-U not in P (linking to a major separation), while a proof of PSPACE-membership without completeness would sharpen the gap and clarify the role of antichain structure versus arbitrary posets.

## finding_unverified

**Finding (unconditional obstruction to PSPACE-completeness):**  
`SORT-BOUND-U` is sparse ([deduction], `research-certificates-barriers.md` Claim B / `research-hardness-boundaries.md` §4) and in `PSPACE` ([deduction], Claim A via `APTIME=PSPACE`). For classes that have self-reducible complete sets and appropriate hierarchies, Mahaney’s argument generalizes: a sparse set many-one hard for `PSPACE` would imply `PSPACE ⊆ P` (by self-reducible search/census over the sparse image). The space hierarchy theorem gives `P ⊊ PSPACE` unconditionally. Therefore `SORT-BOUND-U` cannot be `PSPACE`-hard under polynomial-time many-one reductions; combined with `SORT-BOUND-U ∈ PSPACE` this means **not `PSPACE`-complete under ≤_m^p**.

**Why antichain symmetry matters (vs general posets):**  
Upward transfer fails in the blocking sense - hardness of the antichain does *not* follow from general posets (`GEN-SORT`) and the sparsity/unary structure creates this obstruction; downward embedding is easy only one way (unary). General poset hardness results (Hyafil–Rivest arbitrary tests, Laber–Nogueira approximation, Parberry networks) do not transfer to pairwise comparisons/antichain (`research-hardness-boundaries.md` §2-3). The “counting linear extensions” route is also not the obstruction (`§5`). Certificate soundness vs completeness is the point: ATM gives a sound/complete alternating test (membership) but no polynomial many-one reduction from a `PSPACE`-complete problem survives sparsity+hierarchy.

**Concrete failed/blocked approaches:**  
- Trying to encode an arbitrary `PSPACE` computation into antichain comparisons directly: the symmetric pairwise-test set + unary sparse encoding resists many-one completeness (obstructed unconditionally).  
- Using network/decision-tree NP-hardness as template: model mismatch (arbitrary tests vs pairwise, fixed family vs arbitrary).  
- Exploiting `e(P)` or entropy: not sufficient to determine `S(P)` and not the bottleneck.

**Honest limits:**  
This rules out many-one `PSPACE`-completeness; it does **not** rule out `PSPACE`-hardness under more powerful reductions (e.g. Turing), does not rule out membership in smaller classes being open, and does not yield `P!=PSPACE` from this alone (it uses `P!=PSPACE` via hierarchy the other way). No new theorem was formalized and no repo changes made. The gap remains: succinct certificates in either direction are unknown; the exact complexity class between `P` and `PSPACE` (and relation to `NP/coNP`) is still open for `SORT-BOUND-U`.

## Other metadata

```json
{
  "finished_at": 1793292480.2140238,
  "started_at": 1793292177.4511871
}
```
