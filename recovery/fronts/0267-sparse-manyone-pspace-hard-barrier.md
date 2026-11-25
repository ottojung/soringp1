# sparse-manyone-pspace-hard-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

VKHmWZDMIl2vJ31UMSHCa5-residents

## exit_state

clearexit

## question

For SORT-BOUND-U (sparse unary threshold), is there an unconditional all-n barrier to many-one polynomial-time PSPACE-hardness stronger or different from EXPTIME-nonhardness, and would such hardness imply a specific collapse distinct from Mahaney's NP case?

## basis

SORT-BOUND-U in PSPACE and sparse; EXPTIME-many-one nonhardness is known but PSPACE-many-one hardness barrier not explicitly settled as theorem in repo docs.

## falsifier

Exhibit a many-one polynomial-time reduction from some PSPACE-complete language to SORT-BOUND-U preserving the sparse/unary structure with an explicit all-n correctness argument, or derive an unconditional theorem showing PSPACE-hardness is possible despite sparsity.

## implication

Clarifying PSPACE-hardness status would fix where SORT-BOUND-U sits relative to PH/PSPACE without relying on P!=PSPACE equivalences and would delimit alternation/certificate routes.

## finding_unverified

I'll give a precise answer based on the docs.

**Finding ([deduction]):** Unconditional barrier exists by density/preimage, same class as EXPTIME — not an open gap.

- **Sparsity + preimage:** `SORT-BOUND-U` is sparse ([deduction] Lemma 4.1 in `docs/research-hardness-boundaries.md`): `O(L^2)` strings of length ≤ L, realized as an initial interval by monotonicity (Theorem 4.3). A polynomial-time many-one reduction `f` from language `A` to a sparse language `L` maps each string of length `n` to some string of length `≤ p(n)`, so `|A ∩ Σ^n| ≤ \sum_{m ≤ p(n)} |L ∩ Σ^m| ≤ q(n)` polynomial in `n`. Thus `A` must be sparse.
- **PSPACE-complete sets are not sparse:** QBF (and standard PSPACE-complete languages) are not sparse. Therefore no sparse language can be many-one polynomial-time hard for PSPACE (contradiction). This is the same density argument as Berman–Hartmanis for EXPTIME and is unconditional for many-one reductions; it does not require self-reducibility.
- **Repo state:** `SORT-BOUND-U ∈ PSPACE`. The repo explicitly states `SORT-BOUND-U` is unconditionally not EXPTIME-hard under p-time many-one reductions (Corollary 4.2b). The PSPACE many-one case follows by identical logic but is not numbered as a separate theorem in the docs — that matches "PSPACE-many-one hardness barrier not explicitly settled as theorem in repo docs" as a paperwork point, not a logical gap.

**Complexity implication:** A p-time many-one reduction from a PSPACE-complete language to `SORT-BOUND-U` is impossible unconditionally (would make the PSPACE-complete language sparse). If such a reduction were somehow possible (it’s not), it would imply `PSPACE ⊆ P/poly` (sparse ⊆ P/poly) and hence `PSPACE = Σ_2^P` by the Karp–Lipton/Meyer collapse (distinct from Mahaney’s `P=NP`; both are PH collapses but to different levels/premises). The barrier is stronger in kind than “not obvious” — it’s a density obstruction for many-one reductions at PSPACE level as well.

**Falsifier attempt / obstruction:** No explicit p-time many-one reduction preserving sparse/unary structure is possible for all-n correctness because it would violate density (preimage of sparse). The natural attempt is to encode QBF/alternating computations into comparison orders; the obstruction is not a missing gadget but that the target language has only polynomially many yes-instances per length while the source has exponentially many — a cardinality/density obstruction that no encoding can fix for many-one reductions. Turing reductions are not ruled out by this argument (and remain open in principle, though sparsity gives other consequences).

**Limits:** This is a many-one obstruction. It does not rule out polynomial-time Turing reductions to a sparse set (that’s the harder Mahaney/Yap territory) and does not yield a separation like `P!=PSPACE`. Also `SORT-BOUND-U ∈ P/log` is nonuniform but consistent with sparsity. No repo change warranted; the obstruction is standard and follows directly from stated facts.

## Other metadata

```json
{
  "finished_at": 1793773649.4608345,
  "started_at": 1793773366.0835948
}
```
