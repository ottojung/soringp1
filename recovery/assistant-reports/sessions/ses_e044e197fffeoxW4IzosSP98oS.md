# antonina-JgtaOubACeiBpH0BnOcLUl-seven

Session: ses_e044e197fffeoxW4IzosSP98oS
Workspace: /home/lubko/soring-fronts/cross-charge-merge-information-alln
Created: 1795224102558; updated: 1795224804806

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 425 (msg_1fbbc63b7001yZG53fQCvmlVI9)

## Recovery audit (first, as instructed)

- **Working tree:** `billy-dev`, clean, `HEAD = 6a96398d937d20977a91b9afa8619cb27feab269`. No commits, branches, Lean, tests, ledger or repository edits from this session.
- **Board #301:** fresh digest for `cross-charge` → 0 matches; no post by this front was made. Ledger entry `cross-charge-merge-information-alln` is still `running` with no finding recorded. No external side effects occurred.
- **Scratch only:** `/tmp/opencode/chi_scan.py` (and a short `chi_scan_n7.log`). A background `n=7` scan was started before the interruption and died with the previous turn (empty log, no process) — it is unfinished scratch work, not an external effect. I did not restart it.

## Claim attacked and verdict

I formalized the front's cross charge as the local information excess
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
