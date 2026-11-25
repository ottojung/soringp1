# cross-charge-merge-information-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

JgtaOubACeiBpH0BnOcLUl-seven

## exit_state

clearexit

## question

For every n, is the optimal adversary cross-component comparison charge for a reachable antichain-root composition at most the information-theoretic merge bound derived from the component linear-extension counts?

## basis

Newest board #301 defect-prune domination, transitivity-aware cross obstruction and adversary-composition results; docs/research-structural-lower-bounds.md Theorem B.

## falsifier

Exhibit a reachable composition whose optimal cross charge exceeds the merge information bound by at least two comparisons, or prove the uniform control for all n.

## implication

A proof would give a cross-charge certificate usable for the exact unary decision problem; a counterexample would defeat leaf-only pruning on reachable states.

## finding_unverified

 the local information excess
`χ(P) := F(P) − ⌈log₂ e(P)⌉ ≥ 0` (the information bound is `[deduction]`, sound). The uniform-control claim is "for every n, every composition reachable from the antichain root has χ bounded by the information-theoretic merge bound", with falsifier "reachable composition with χ ≥ 2".

**Verdict: the uniform-control reading is refuted all-n; the prescribed falsifier exists.**

### Falsifier (literature + exact arithmetic, independently checked)

Balanced merge `Merge(m,m)` = disjoint union of two `m`-chains (a parallel composition, i.e. merging two sorted lists), reachable from the `A_{2m}` antichain — at `m = 21` it has 40 cover relations, so it is reachable within 40 comparisons, far below any merge-sort bound.

- `F(Merge(m,m)) = M(m,m) = 2m−1` — certified (Graham–Karp; Stockmeyer–Yao 1980; Li–Sun–Zhang 2016), `[literature]`.
- `e = C(2m,m)`, so `info = ⌈log₂ C(2m,m)⌉`, `[deduction]`.
- `χ(m) = (2m−1) − ⌈log₂ C(2m,m)⌉`. Computed: `χ = 0` for `m ≤ 4`, `χ = 1` for `5 ≤ m ≤ 20`, and **`χ(21) = 41 − 39 = 2`** with `C(42,21) = 538 257 874 440`. So `Merge(21,21)` (n = 42) is a reachable composition whose optimal cross charge exceeds the merge information bound by exactly two comparisons; `χ(m) → ∞` (≈ ½ log₂(πm) − O(1)), so no uniform finite bound exists.

Local checks with the repository's exact minimax evaluator `[experiment]`: `Merge(2,4): e=15, info=4, F=5, χ=1`; `Merge(5,5): 252/8/9, χ=1`; `Merge(6,6): 924/10/11, χ=1` — all consistent with the certified merge values.

### Concrete failed approach / finite obstruction

I exhaustively scanned **all labelled posets** (hence all reachable states) for `n = 5` (4 231 posets) and `n = 6` (130 023 posets): `max χ = 1` in both, with no composition reaching `χ ≥ 2`. So small-instance enumeration **cannot** produce the required falsifier; the witness forces the structured balanced-merge family at `n = 42`. The `n = 7` census scan is unfinished (killed by the interruption) and I make no claim about it.

A second obstruction: for series compositions the cross charge is an identity, `F(⊕ Pᵢ) − Σ⌈log₂ e(Pᵢ)⌉ = Σ δᵢ` (Theorem B plus additivity), so combining component extension counts alone yields an *exact* cross charge, not a uniform control — any bound must come from bounding the merge gaps `δᵢ`, which are unbounded.

## Honest limits

- This is **not a new theorem**: the unboundedness of `F − ⌈log₂ e⌉` over balanced merges is already recorded in `docs/research-obstruction-next.md` §7. I therefore made **no repository, Lean or board changes**, per the publication gate.
- The front's wording is ambiguous. If "cross charge" instead means the disjoint-union defect `F(A⊔B) − F(A) − F(B)`, the balanced merge gives defect 1, not ≥ 2, and the min-size strengthening stays open; my falsifier is for the information-excess reading. This should be settled before the front is closed.
- The newest board results (defect-prune domination, transitivity-aware cross obstruction, adversary-composition, sign-flip adversary) concern *how to construct* a cross-charge/pruning rule. This computation neither confirms nor refutes them; it only addresses the numerical uniform bound.
- **Soundness ≠ completeness:** `F ≥ ⌈log₂ e⌉` is sound; the falsifier shows a leaf-count-only certificate cannot have zero cross charge on reachable states. It does not give a cross-charge certificate for `SORT-BOUND-U`, does not decide NP/P membership, and says nothing about `S(n)` itself beyond the merge component.

## Other metadata

```json
{
  "finished_at": 1795224818.4256034,
  "started_at": 1795224102.2167897
}
```
