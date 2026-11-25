# sparse-pspace-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

kCrCOAClNZw9RPT9R4QYxp-sailing

## exit_state

clearexit

## question

Is SORT-BOUND-U PSPACE-complete under polynomial-time many-one reductions, or does its unary-sparse form and minimax structure place it strictly below PSPACE-complete problems relative to logspace/polynomial many-one reducibility?

## basis

SORT-BOUND-U is sparse and in PSPACE (problem.md); Berman-Hartmanis and later density theorems constrain sparse complete sets for some classes but PSPACE many-one completeness of sparse languages is not obviously ruled out by Mahaney alone.

## falsifier

Construct an explicit polynomial-time many-one reduction from some known PSPACE-complete language to SORT-BOUND-U, or prove SORT-BOUND-U is not PSPACE-hard under polynomial-time many-one reductions (e.g. via a density/sparsity or structural invariant).

## implication

PSPACE-completeness would mean exact S(n) evaluation is as hard as general PSPACE; a strict lower containment would reflect the combinatorial structure of sorting/minimax and could open paths to better bounds or to understanding the PH/PSPACE boundary.

## finding_unverified

poly-time many-one reduction from a known PSPACE-complete language (e.g. TQBF) to `SORT-BOUND-U`. Obstruction: `SORT-BOUND-U` is a very special language (tally-like in form `1^n#1^k`, only values determined by the sorting number function `S(n)` which is the minimax comparison-complexity of sorting `n` distinct keys). There is no obvious encoding-faithful reduction from arbitrary quantified boolean formulas/games to "is the sorting decision tree height ≤ k for n elements?" The combinatorial object is the comparison-poset minimax (a fixed, highly structured family) not arbitrary PSPACE computations; hardness of optimization over *arbitrary* partial orders does not transfer without a reduction (AGENTS.md §Model fidelity). No standard gadget is apparent and the structure is too rigid.
- Attempted to derive a density/sparsity contradiction for PSPACE-completeness: could not reproduce Berman–Hartmanis. The key difference is class padding/hierarchy properties used for EXPTIME; PSPACE is closed under polynomial padding but the "complete set density" argument that blocks EXPTIME-completeness of sparse sets does not obviously apply to PSPACE in the same unconditional form. I found no primary source stating "sparse PSPACE-complete under poly-time m-reductions is impossible" - the known barriers are conditional (Karp–Lipton style) or apply to NP/EXPTIME. This is consistent with the board notes saying "PSPACE many-one completeness of sparse languages is not obviously ruled out by Mahaney alone".

**Honest limits / conclusion:**
- `[conjecture]` **Neither direction is ruled out by known sparsity/density theorems alone.** The unary sparsity + `P/log` nonuniform membership and Mahaney/EXPTIME barriers are strong structural constraints, but they do not unconditionally prove `SORT-BOUND-U` is *not* PSPACE-complete under polynomial-time many-one reductions. A proof of non-completeness would need either a new unconditional density theorem for PSPACE, or a structural invariant of the minimax/comparison model not present in general PSPACE computations. Conversely, a reduction would require a highly non-obvious encoding from some PSPACE-complete language into the sorting-number threshold.
- `[deduction]` **What is clear:** `SORT-BOUND-U ∉ EXPTIME-hard` under poly-time m-reductions (Berman–Hartmanis) - weaker upper side in some forms? No, it's in `PSPACE ⊆ EXPTIME`. The real question is the PSPACE level. The combinatorial structure (sorting/minimax, comparison-based, the "antichain root" / fixed family) suggests it may be strictly below PSPACE-complete problems, but without a theorem this remains a plausible conjecture, not a proof. No concrete obstruction was found that constitutes a disproof of PSPACE-completeness; the falsifier remains open given current knowledge.

**Concrete failed approach:** trying to lift EXPTIME density argument to PSPACE failed because the standard padding/time-hierarchy step used for EXPTIME doesn't directly yield a contradiction for PSPACE-completeness of a sparse set under poly-time many-one reductions - the consequence is consistent with `PSPACE ⊆ P/poly` (open). **Exact obstruction (current):** no unconditional sparsity/density theorem blocks sparse PSPACE-complete sets under poly-time m-reductions; the barrier is not Mahaney and not Berman–Hartmanis. Proving strict containment below PSPACE-complete would require a new structural lower-bound/diagonalization argument exploiting the comparison/minimax structure, not just sparsity.

## Other metadata

```json
{
  "finished_at": 1793369961.900181,
  "started_at": 1793369625.7016947
}
```
