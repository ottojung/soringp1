# Disjoint-union (parallel) module reversal of the exact minimax value `F`

**Status:** research note (2026-10-18). A **restricted theorem** (paper
proof, deduction) with `n ≤ 7` computational evidence. The general
non-selfdual case is **unresolved**: no counterexample is found up to `n = 7`,
but no proof is claimed. No Lean file and no complexity-class separation is
claimed. Companion program: `scripts/parallel_module_probe.py`; tests:
`tests/test_parallel_module.py`. Every number below is reproduced by the
program.

## Precise question

`docs/problem.md` fixes `S(n)` as the minimum worst-case number of adaptive
pairwise comparisons to sort `n` distinct labelled keys, and
`docs/upper-bound.md` / `SoringP1/Minimax.lean` (A24) identify it with the
partial-order minimax value `F(∅)`, where

    F(P) = 0                                                      if P is total,
    F(P) = 1 + min_{x ‖ y} max( F(P+x<y), F(P+y<x) )              otherwise.

Equivalently, `F(P) = adv (L(P))` is the minimum height of a decision tree
that identifies the unknown linear extension of `P` (the Lean `adv` on the
set `L(P)` of linear extensions).

The companion note `docs/research-orientation-modules.md` (branch
`research/comparability-structure-20261018`, PR #12) studies *module reversal*
`σ_S`, which reverses the internal relations of a Gallai module `S`. It finds
empirically that **every parallel-quotient module reversal preserves `F` for
`n ≤ 7`** (675 reversals at `n = 7`), but proves no theorem, and it falsifies
the general claim at `n = 7` for *prime* quotients (8 violations). This note
isolates the parallel case.

> For a disjoint union `P = A ‖ B` (every cross pair incomparable), is
> `F(A^op ‖ B) = F(A ‖ B)`? Reversing the module `A` of `P = A ‖ B` is exactly
> this operation, so the question is whether **reversing one component of a
> disjoint union preserves `F`**.

**Answer (this note).** A restricted theorem holds: if `B` is self-dual up to
relabelling, then `F(A^op ‖ B) = F(A ‖ B)`. This immediately proves the PR12
observation for parallel-quotient modules, because their complement is an
antichain, hence self-dual. The general case (both `A` and `B` non-selfdual)
is **unresolved**: the exhaustive `n ≤ 7` checks find no counterexample, but
we do not claim a theorem. The PR12 `n = 7` prime-quotient counterexample is
a different phenomenon and is not re-proved or contradicted here.

## Model and notation

A state is a strict partial order on the labelled keys `[n]`, stored as
successor bitmasks (`succ[i]` has bit `j` iff `i < j`). `x ‖ y` means
incomparable. Reachable states are the labelled posets (A001035); isomorphism
classes are A000112. `e(P)` is the number of linear extensions. **No P/NP
claim is made.**

**Disjoint union (parallel composition).** For posets `A`, `B` on disjoint
ground sets, `A ‖ B` is the poset on `A ∪ B` with `x < y` iff `x <_A y`,
`x <_B y`, or neither (so every cross pair is incomparable).

**Encoding invariant (the source of an earlier correction).** If `B` is
encoded on its own labels `0..|B|-1`, then the encoding of `A ‖ B` **must**
shift `B`'s masks left by `|A|`:

    succ_{A‖B}[|A| + i] = succ_B[i] << |A|.

Failing to shift produces relations from `B` back into `A`, which is not a
disjoint union. An early draft probe copied the second block verbatim and
reported `F(V ‖ Λ) = 7` versus `F(Λ ‖ Λ) = 8`; both values were spurious
artefacts of the unshifted encoding. With the correct shift, all four of
`V ‖ Λ`, `Λ ‖ V`, `V ‖ V`, `Λ ‖ Λ` have `e = 80` and `F = 7`. The corrected
values are the ones used throughout this note, and the tests
`test_unshifted_second_block_is_not_a_disjoint_union` and
`test_corrected_V_Lam_values` guard against the regression.

**Self-dual.** `P` is *self-dual* if `P^op ≅ P` (isomorphic up to relabelling).

## 1. Restricted theorem: self-dual complement (deduction)

**Theorem 1.** Let `A`, `B` be finite posets and suppose `B` is self-dual up to
relabelling (`B^op ≅ B`). Then

    F(A^op ‖ B) = F(A ‖ B).

*Proof.* Global order-duality invariance of `F` (Theorem 3 of
`docs/research-compression-next.md`) gives `F(A^op ‖ B) = F((A^op ‖ B)^op)`.
Duality commutes with disjoint union, `(A^op ‖ B)^op = A ‖ B^op`. Finally,
`B^op ≅ B` and relabelling invariance of `F` (Lemma 2 of the same note) give
`F(A ‖ B^op) = F(A ‖ B)`. Chaining the three equalities:

    F(A^op ‖ B) = F((A^op ‖ B)^op) = F(A ‖ B^op) = F(A ‖ B). ∎

**Corollary 2 (parallel-quotient module reversal).** If `S` is a module of `P`
whose quotient `P/S` is an antichain, then `σ_S` preserves `F`.

*Proof.* The complement `C = P ∖ S` is a set of pairwise-incomparable keys,
so `P = S ‖ C`. An antichain is self-dual (`C^op ≅ C`), so Theorem 1 with
`A = S`, `B = C` gives `F(S^op ‖ C) = F(S ‖ C)`, i.e. `F(σ_S(P)) = F(P)`. ∎

This proves, rather than merely observes, the PR12 parallel-quotient bucket
(0 violations at `n = 7`). The PR12 prime-quotient failures are unaffected:
their complement is not an antichain, so Theorem 1 does not apply.

**Why the hypothesis is asymmetric.** Theorem 1 requires the *complement* `B`
to be self-dual, not `A`. If `A` is self-dual then `A^op ≅ A` and
`F(A^op ‖ B) = F(A ‖ B)` is immediate by relabelling, so the interesting case
is exactly when `B` is the self-dual one.

## 2. Computational evidence, `n ≤ 7` (experiment)

The program enumerates every isomorphism class `A` of size `a` and `B` of size
`b` with `a + b = n` (using the isomorphism-quotient DP, never labelled
posets), and checks, for every pair:

* the encoding invariant (every relation of `A ‖ B` lies inside `A` or inside
  `B`);
* the linear-extension identity `e(A ‖ B) = binom(a+b, a) · e(A) · e(B)`;
* the restricted theorem (for pairs with `B` self-dual);
* the general (unproven) equalities `F(A^op ‖ B) = F(A ‖ B) = F(A ‖ B^op)`.

| n | pairs | restricted pairs | restricted violations | general violations | `e` violations | block violations |
|---|-------|------------------|-----------------------|--------------------|----------------|-------------------|
| 2 | 1 | 1 | 0 | 0 | 0 | 0 |
| 3 | 4 | 4 | 0 | 0 | 0 | 0 |
| 4 | 14 | 12 | 0 | 0 | 0 | 0 |
| 5 | 52 | 40 | 0 | 0 | 0 | 0 |
| 6 | 215 | 141 | 0 | 0 | 0 | 0 |
| 7 | 1048 | 612 | 0 | 0 | 0 | 0 |

The restricted theorem holds for every checked pair (0 violations, `n ≤ 7`).
The general equalities also hold for every checked pair, but this is recorded
as **evidence only** (Section 3). The `e` identity and the block invariant
hold for every pair.

The `n = 7` row uses 2045 isomorphism classes and runs in a few seconds; no
labelled-poset enumeration and no `n ≥ 8` exhaustive search is attempted. A
handful of targeted `n = 8` pairs (non-selfdual size-4 components) were also
checked and agreed, but they are not part of the reproducible default run.

## 3. The general non-selfdual case (unresolved)

If both `A` and `B` are non-selfdual, Theorem 1 does not apply, and we do not
claim `F(A^op ‖ B) = F(A ‖ B)`. The exhaustive checks above find **no**
counterexample up to `n = 7`, but finite checks do not establish a general
symmetry, and we label this case **unresolved**.

A candidate bijection argument suggests the general case may in fact hold:
reversing the relative order of the `B`-elements in a linear extension of
`A ‖ B` gives a linear extension of `A ‖ B^op`, and this map preserves each
comparison partition up to swapping the two outcomes of a within-`B`
comparison. Since decision-tree height is invariant under such a relabelling
of outcome blocks, this would give `F(A ‖ B) = F(A ‖ B^op)`, and then
`F(A^op ‖ B) = F(A ‖ B)` by global duality. We record this as a **hypothesis
and a next step**, not as a theorem: it has not been checked as carefully as
Theorem 1, and the scoped remit for this note is the restricted theorem and
the `n ≤ 7` evidence.

## 4. What was learned, failed ideas, next hypotheses

**Learned.**

1. Reversing a component of a disjoint union preserves `F` whenever the
   *complement* is self-dual (Theorem 1, proof above).
2. This proves the PR12 parallel-quotient observation (Corollary 2), whose
   complement is an antichain. The PR12 prime-quotient `n = 7` failures are a
   separate phenomenon.
3. The disjoint-union encoding must shift the second block's bitmasks; the
   early unshifted probe produced spurious values that are **not** published.
4. `e(A ‖ B) = binom(a+b, a) · e(A) · e(B)` and the block invariant hold
   exhaustively for `n ≤ 7`.

**Failed / unresolved.**

* "Reversing a component of a disjoint union always preserves `F`" — plausible
  and supported by `n ≤ 7`, but **unproven** here; the general non-selfdual
  case is open.
* The bijection argument of Section 3 — a candidate proof, not verified as a
  theorem.

**Next hypotheses.**

1. Prove or refute the general non-selfdual case; if it holds, the restricted
   hypothesis is unnecessary and parallel-quotient reversal is a special case.
2. Determine whether a sound *state* quotient for `F` can be built from
   disjoint-union reversals (the `docs/research-compression-next.md` definition
   of a sound state quotient requires an equivariant transition, not just a
   class-invariant value).
3. Check whether the bijection argument extends to reversal of an arbitrary
   *parallel* module (complement an antichain) inside a larger poset, beyond
   the pure disjoint-union case.

## 5. Literature grounding

* **Gallai, *Transitiv orientierbare Graphen*, Acta Math. Acad. Sci. Hungar.
  18:25–66 (1967).** Modules / substitution decomposition; the same reference
  as the companion module-reversal note.
* **McConnell–Spinrad, *Modular decomposition and transitive orientation*,
  Discrete Math. 201:189–241 (1999).** Canonical modular decomposition and the
  parallel (antichain) quotient.
* **Jain–Klauck–Sántha, *Optimal Direct Sum Results for Deterministic and
  Randomized Decision Tree Complexity*, IPB 110(20):893–897 (2010).** The
  deterministic direct-sum theorem used for the ordinal-sum additivity in
  `docs/research-series-decomposition.md`; it does **not** apply to parallel
  composition (the counterexample `F(a ⊔ b) = 1 ≠ 0 = F(a) + F(b)`), which is
  why the parallel case needs its own argument.

Model caveats: none of these references is a statement about the complexity of
evaluating `S(n)`. Theorem 1 and Corollary 2 are this note's own deductions;
the `n ≤ 7` table is this note's own experiment.

## 6. Reproduce

    python3 scripts/parallel_module_probe.py --max-n 6          # ~1 s
    python3 scripts/parallel_module_probe.py --n7                # ~3 s
    python3 scripts/parallel_module_probe.py --max-n 6 --no-e    # faster
    python3 -m unittest tests.test_parallel_module -v

The `n = 7` part uses the isomorphism-quotient DP (2045 classes); it does
**not** enumerate the labelled posets. No `n ≥ 8` exhaustive search is
attempted.

## 7. Provenance and non-overlap

* Primary sources: Gallai (1967); McConnell–Spinrad (1999); Jain–Klauck–Sántha
  (2010). OEIS A001035, A000112 are used as reference sequences only.
* Definitions, the encoding invariant, Theorem 1, Corollary 2 and the `n ≤ 7`
  table are this note's own. The parallel-quotient observation is credited to
  `docs/research-orientation-modules.md` (PR #12) and is here *proved*, not
  re-claimed as new.
* No Lean file is added or modified; the kernel-checked model is untouched.
* This document and `scripts/parallel_module_probe.py` /
  `tests/test_parallel_module.py` are the only artifacts of this task.
