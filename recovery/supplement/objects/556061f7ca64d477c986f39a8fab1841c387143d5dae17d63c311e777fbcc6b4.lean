import Mathlib

/-!
# Optimal adaptive comparison sorting

A ranking assigns a distinct rank to every labelled input position. A
leaf returns the sequence of input positions in ascending order, encoded
as a permutation of the rank positions. An internal node tests whether
the value at position `i` is smaller than the value at position `j`.

The minimax number of comparisons is specified as an infimum of feasible
worst-case heights. Existence of a correct tree for every n is proved in
`SoringP1/Existence.lean` and attainment in `SoringP1/Attainment.lean`;
the correspondence with the partial-order minimax evaluator is
`S_eq_adv_univ` in `SoringP1/Minimax.lean`.
-/

namespace SoringP1

/-- A deterministic adaptive comparison algorithm on `n` distinct keys. -/
inductive ComparisonTree (n : ℕ) where
  | leaf : Equiv.Perm (Fin n) → ComparisonTree n
  | compare : Fin n → Fin n → ComparisonTree n →
      ComparisonTree n → ComparisonTree n

namespace ComparisonTree

/-- Worst-case number of comparisons, counting all syntactic branches. -/
def height {n : ℕ} : ComparisonTree n → ℕ
  | .leaf _ => 0
  | .compare _ _ yes no => 1 + max (height yes) (height no)

/-- Run against a ranking: original item index ↦ its ascending rank. -/
def run {n : ℕ} (ranking : Equiv.Perm (Fin n)) :
    ComparisonTree n → Equiv.Perm (Fin n)
  | .leaf result => result
  | .compare i j yes no =>
      if ranking i < ranking j then run ranking yes else run ranking no

end ComparisonTree

/-- Every possible input ranking is sorted to the corresponding inverse. -/
def Correct {n : ℕ} (tree : ComparisonTree n) : Prop :=
  ∀ ranking : Equiv.Perm (Fin n),
    ComparisonTree.run ranking tree = ranking.symm

/-- A correct decision tree exists within worst-case comparison budget `k`. -/
def HasBudget (n k : ℕ) : Prop :=
  ∃ tree : ComparisonTree n,
    Correct tree ∧ ComparisonTree.height tree ≤ k

/--
The sorting-number specification. `sInf ∅ = 0` for natural numbers, so
this is the intended minimum only because `exists_hasBudget` proves
`∃ k, HasBudget n k` for every n.
-/
noncomputable def S (n : ℕ) : ℕ :=
  sInf {k : ℕ | HasBudget n k}

/-- Feasibility is monotone in the permitted number of comparisons. -/
theorem hasBudget_mono {n k l : ℕ}
    (h : HasBudget n k) (hkl : k ≤ l) : HasBudget n l := by
  obtain ⟨tree, hcorrect, hheight⟩ := h
  exact ⟨tree, hcorrect, le_trans hheight hkl⟩

end SoringP1
