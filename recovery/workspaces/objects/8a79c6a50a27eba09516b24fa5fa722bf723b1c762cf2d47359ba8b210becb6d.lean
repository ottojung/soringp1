import Mathlib
import SoringP1.Attainment

/-!
# Information-theoretic lower bound for the sorting number

We prove the classic result that any correct comparison decision tree for
sorting `n` distinct keys has at least `n!` leaves, and therefore height at
least `log₂(n!)`. Combined with the attainment theorem, this yields
`n! ≤ 2 ^ S n`, i.e. `S n ≥ log₂(n!)`.
-/

namespace SoringP1

namespace ComparisonTree

/-- The number of leaves in a comparison tree. -/
def numLeaves {n : ℕ} : ComparisonTree n → ℕ
  | .leaf _ => 1
  | .compare _ _ yes no => numLeaves yes + numLeaves no

/-- The finset of permutations stored at leaves. -/
def leafSet {n : ℕ} : ComparisonTree n → Finset (Equiv.Perm (Fin n))
  | .leaf p => {p}
  | .compare _ _ yes no => leafSet yes ∪ leafSet no

/-- A tree of height `k` has at most `2^k` leaves. -/
theorem numLeaves_le_two_pow_height {n : ℕ} (tree : ComparisonTree n) :
    numLeaves tree ≤ 2 ^ height tree := by
  induction tree with
  | leaf _ => simp [numLeaves, height]
  | compare _ _ yes no ih_yes ih_no =>
      show numLeaves yes + numLeaves no ≤ 2 ^ (1 + max (height yes) (height no))
      have h1 : 2 ^ height yes ≤ 2 ^ max (height yes) (height no) :=
        Nat.pow_le_pow_right (by omega) (le_max_left _ _)
      have h2 : 2 ^ height no ≤ 2 ^ max (height yes) (height no) :=
        Nat.pow_le_pow_right (by omega) (le_max_right _ _)
      have h3 : 2 ^ (1 + max (height yes) (height no))
          = 2 ^ max (height yes) (height no) + 2 ^ max (height yes) (height no) := by
        rw [Nat.one_add, Nat.pow_succ, Nat.mul_two]
      omega

/-- The number of leaves is at least the cardinality of the leaf-set. -/
theorem leafSet_card_le_numLeaves {n : ℕ} (tree : ComparisonTree n) :
    (leafSet tree).card ≤ numLeaves tree := by
  induction tree with
  | leaf _ => simp [leafSet, numLeaves]
  | compare _ _ yes no ih_yes ih_no =>
      show (leafSet yes ∪ leafSet no).card ≤ numLeaves yes + numLeaves no
      have h1 : (leafSet yes ∪ leafSet no).card ≤ (leafSet yes).card + (leafSet no).card :=
        Finset.card_union_le _ _
      omega

/-- Running a tree against any ranking reaches a leaf. -/
theorem run_mem_leafSet {n : ℕ} (ranking : Equiv.Perm (Fin n)) :
    ∀ tree : ComparisonTree n, run ranking tree ∈ leafSet tree := by
  intro tree
  induction tree with
  | leaf _ => simp [run, leafSet]
  | compare i j yes no ih_yes ih_no =>
      show (if ranking i < ranking j then run ranking yes else run ranking no)
        ∈ leafSet yes ∪ leafSet no
      split
      · next h => exact Finset.mem_union.mpr (Or.inl ih_yes)
      · next h => exact Finset.mem_union.mpr (Or.inr ih_no)

end ComparisonTree

open ComparisonTree

/-- A correct tree has at least `n!` leaves. -/
theorem factorial_le_numLeaves {n : ℕ} (tree : ComparisonTree n) (h : Correct tree) :
    n.factorial ≤ numLeaves tree := by
  have hinj : Function.Injective (fun r => run r tree) := by
    intro a b hab
    have ha := h a
    have hb := h b
    have hab' : run a tree = run b tree := hab
    rw [ha, hb] at hab'
    calc a = a.symm.symm := (Equiv.symm_symm a).symm
      _ = b.symm.symm := by rw [hab']
      _ = b := Equiv.symm_symm b
  have h1 : ((@Finset.univ (Equiv.Perm (Fin n)) _).image (fun r => run r tree)).card
      = n.factorial := by
    rw [Finset.card_image_of_injective _ hinj, Finset.card_univ,
      Fintype.card_perm, Fintype.card_fin]
  have h2 : ((@Finset.univ (Equiv.Perm (Fin n)) _).image (fun r => run r tree))
      ⊆ leafSet tree := by
    intro r hr
    obtain ⟨x, _, hxr⟩ := Finset.mem_image.1 hr
    have hxr' : run x tree = r := hxr
    rw [← hxr']
    exact run_mem_leafSet x tree
  have h3 : ((@Finset.univ (Equiv.Perm (Fin n)) _).image (fun r => run r tree)).card
      ≤ (leafSet tree).card := Finset.card_le_card h2
  have h4 : (leafSet tree).card ≤ numLeaves tree := leafSet_card_le_numLeaves tree
  omega

/-- The classic information-theoretic lower bound. -/
theorem factorial_le_two_pow_height {n : ℕ} (tree : ComparisonTree n)
    (h : Correct tree) : n.factorial ≤ 2 ^ height tree :=
  le_trans (factorial_le_numLeaves tree h) (numLeaves_le_two_pow_height tree)

/-- The certified sorting number satisfies `S n ≥ log₂(n!)`. -/
theorem factorial_le_two_pow_S (n : ℕ) : n.factorial ≤ 2 ^ S n := by
  obtain ⟨tree, hcorrect, hheight⟩ := hasBudget_S n
  have h1 := factorial_le_two_pow_height tree hcorrect
  have h2 : 2 ^ height tree ≤ 2 ^ S n := Nat.pow_le_pow_right (by omega) hheight
  omega

end SoringP1
