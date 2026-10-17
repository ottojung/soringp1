# Kernel-checked results

Inventory of the machine-checked (Lean 4 + Mathlib) results for the sorting
number `S(n)`, the exact statement each proves, and the open fronts. Every
theorem below is kernel-checked with no `sorry`/`admit`/`axiom`/`native_decide`;
all modules build with `lake build --wfail` and replay under `leanchecker`.

Model (`SoringP1/Model.lean`): a deterministic adaptive comparison algorithm is
`ComparisonTree n` (`leaf (Equiv.Perm (Fin n)) | compare i j yes no`); `height`
is the worst-case comparison count; `run ranking tree` returns the leaf reached;
`Correct tree` means `∀ ranking, run ranking tree = ranking.symm`;
`HasBudget n k` means some correct tree has height `≤ k`; and
`S n := sInf {k | HasBudget n k}`.

## Achieved

### A0 — existence (`SoringP1/Existence.lean`)
- `exists_hasBudget (n) : ∃ k, HasBudget n k` — a correct sorting tree exists
  for every `n`, via an explicit fuel-driven insertion-sort tree `sortTree`.
  This makes `S n` a genuine (nonempty) infimum.
- `sortTree_correct`, `sortTree_height : height (sortTree n) ≤ n*(n+2)+(n+1)+1`.

### A1 — attainment and minimality (`SoringP1/Attainment.lean`)
- `hasBudget_S (n) : HasBudget n (S n)` — the infimum is attained.
- `S_le_iff {n k} : S n ≤ k ↔ HasBudget n k` — `S n` is exactly the minimum
  feasible budget.
- `S_is_minimal`, `S_le_explicit (n) : S n ≤ n*(n+2)+(n+1)+1`,
  `exists_tree_S (n) : ∃ tree, Correct tree ∧ height tree ≤ S n`.

### A2 — information lower bound (`SoringP1/LowerBound.lean`)
- `factorial_le_two_pow_height {n} (tree) (h : Correct tree) :
    n.factorial ≤ 2 ^ height tree`
- `factorial_le_two_pow_S (n) : n.factorial ≤ 2 ^ S n`
  (the classic `S(n) ≥ log₂ n!` bound, kernel-checked against the model).
- Supporting: `numLeaves_le_two_pow_height`, `leafSet_card_le_numLeaves`,
  `run_mem_leafSet`, `factorial_le_numLeaves`.

### A4 / A5 — exact small values (`SoringP1/SmallValues.lean`)
- `S_zero : S 0 = 0`, `S_one : S 1 = 0`, `S_two : S 2 = 1`, `S_three : S 3 = 3`.
- Explicit optimal trees `treeTwo` (1 comparison) and `treeThree`
  (3 comparisons), each proven `Correct`; lower bounds from A2.
- So `S(0..3) = 0, 0, 1, 3`, matching `scripts/evaluate.py`
  (`S(0..6) = 0,0,1,3,5,7`). The `n = 3` optimum attains `⌈log₂ 3!⌉ = 3`.

## Open fronts

1. **Tighter upper bound.** The proven bound is `n(n+2)+(n+1)+1`; the true
   insertion-sort worst case is `n(n−1)/2`. The current `go` proof counts every
   recursion step as fuel (so required fuel = comparisons + structural steps,
   not comparisons alone), which blocks the obvious tightening. Needs either a
   refactored fuel accounting or a separately constructed, tightly bounded tree.
2. **Exact value `S 4 = 5`** (and beyond): requires an explicit height-5 tree on
   four keys (up to 24 leaves); best generated programmatically rather than by
   hand.
3. **Evaluator correspondence (general).** A checked executable minimax /
   partial-order evaluator and a proof that it computes `S` on its domain.
4. **Complexity classes.** Encode `S` (or its threshold language) against a
   Turing-machine/resource model and prove an upper bound under a fixed
   encoding — distinguishing unary (`2^{O(n²)}` in `n`, i.e. EXPTIME) from
   binary input (`2^{O(2^m)}`, 2-EXPTIME). No `NP` membership or separation is
   claimed; the model is a decision-tree model, not yet a machine model.
5. **Structural characterization** of `S(n)` avoiding partial-order enumeration.

A theorem about a surrogate problem is not a theorem about `S`; each result
above states its exact object.
