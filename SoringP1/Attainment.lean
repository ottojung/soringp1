import Mathlib
import SoringP1.Existence

/-!
# Attainment and minimality of the sorting-number specification

Milestone A0 (`SoringP1/Existence.lean`) proved that a correct comparison
decision tree exists within some finite worst-case budget for every `n`. Before
that, `S n = sInf {k | HasBudget n k}` was only a specification: `sInf ∅ = 0`
for naturals, so the infimum could in principle fail to be attained.

Here we certify that the infimum is attained, so `S n` is exactly the least
feasible worst-case budget, not merely a lower bound:

- `hasBudget_S` (`S n` is feasible): the feasible set is nonempty, so its
  infimum is a member by `Nat.sInf_mem`.
- `S_le_iff` (characterization): `S n ≤ k` if and only if `HasBudget n k`.
- `S_is_minimal`: `S n` is the minimum feasible budget.
- `S_le_explicit`: the explicit insertion-sort budget from A0 is an upper bound.
- `exists_tree_S`: a correct tree exists with height at most `S n` exactly.

Thus `S` is now certified as the intended minimum number of comparisons.
-/

namespace SoringP1

/-- The feasible budget set of `n` is nonempty, by the A0 existence theorem. -/
theorem hasBudget_set_nonempty (n : ℕ) : {k : ℕ | HasBudget n k}.Nonempty :=
  exists_hasBudget n

/-- The infimum budget `S n` is itself feasible: a correct tree of height at
most `S n` exists. -/
theorem hasBudget_S (n : ℕ) : HasBudget n (S n) :=
  Nat.sInf_mem (hasBudget_set_nonempty n)

/-- `S n` is the least feasible budget: `S n ≤ k` exactly when `k` is feasible. -/
theorem S_le_iff {n k : ℕ} : S n ≤ k ↔ HasBudget n k := by
  constructor
  · intro h
    exact hasBudget_mono (hasBudget_S n) h
  · intro h
    exact Nat.sInf_le h

/-- Minimality of `S n` among feasible budgets. -/
theorem S_is_minimal {n k : ℕ} (h : HasBudget n k) : S n ≤ k :=
  (S_le_iff (n := n) (k := k)).2 h

/-- The explicit insertion-sort budget of A0 bounds `S n`. -/
theorem S_le_explicit (n : ℕ) : S n ≤ n * (n + 2) + (n + 1) + 1 :=
  Nat.sInf_le ⟨sortTree n, sortTree_correct n, sortTree_height n⟩

/-- A correct tree with height at most the certified minimum `S n` exists. -/
theorem exists_tree_S (n : ℕ) :
    ∃ tree : ComparisonTree n, Correct tree ∧ ComparisonTree.height tree ≤ S n :=
  hasBudget_S n

end SoringP1
