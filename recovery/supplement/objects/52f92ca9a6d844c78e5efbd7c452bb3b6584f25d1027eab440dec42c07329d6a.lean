import SoringP1.Attainment
import SoringP1.LowerBound

/-!
# Exact small values of the sorting number S(n)

We pin the first values of `S` against the reference evaluator
(`scripts/evaluate.py`, which reports S(0..6) = 0,0,1,3,5,7):

* `S 0 = 0`, `S 1 = 0`, `S 2 = 1` (exact);
* `3 ≤ S 3` (the lower half of `S 3 = 3`).

Upper bounds come from explicit correct decision trees; lower bounds come from
the information bound `n! ≤ 2 ^ S n` (`SoringP1.LowerBound`).
-/

namespace SoringP1

/-! ## n = 0 and n = 1: a single leaf suffices. -/

theorem correct_leaf_zero :
    Correct (ComparisonTree.leaf (Equiv.refl (Fin 0)) : ComparisonTree 0) := by
  intro ranking
  exact Subsingleton.elim _ _

theorem hasBudget_zero : HasBudget 0 0 :=
  ⟨_, correct_leaf_zero, by simp [ComparisonTree.height]⟩

theorem S_zero : S 0 = 0 := by
  apply le_antisymm
  · rw [S_le_iff]; exact hasBudget_zero
  · exact Nat.zero_le _

theorem correct_leaf_one :
    Correct (ComparisonTree.leaf (Equiv.refl (Fin 1)) : ComparisonTree 1) := by
  intro ranking
  exact Subsingleton.elim _ _

theorem hasBudget_one : HasBudget 1 0 :=
  ⟨_, correct_leaf_one, by simp [ComparisonTree.height]⟩

theorem S_one : S 1 = 0 := by
  apply le_antisymm
  · rw [S_le_iff]; exact hasBudget_one
  · exact Nat.zero_le _

/-! ## n = 2: one comparison. -/

/-- The single-comparison sorting tree on two keys: compare positions `0` and `1`. -/
def treeTwo : ComparisonTree 2 :=
  .compare 0 1 (.leaf (Equiv.refl (Fin 2))) (.leaf (Equiv.swap 0 1))

theorem treeTwo_correct : Correct treeTwo := by
  intro ranking
  fin_cases ranking <;> decide

theorem hasBudget_two : HasBudget 2 1 :=
  ⟨treeTwo, treeTwo_correct, by decide⟩

theorem S_two : S 2 = 1 := by
  apply le_antisymm
  · rw [S_le_iff]; exact hasBudget_two
  · have h := factorial_le_two_pow_S 2
    by_contra hlt
    have h0 : S 2 = 0 := by omega
    rw [h0] at h
    norm_num at h

/-! ## n = 3: the lower bound half of `S 3 = 3`. -/

theorem three_le_S_three : 3 ≤ S 3 := by
  have h := factorial_le_two_pow_S 3
  norm_num at h
  by_contra hlt
  have h2 : S 3 ≤ 2 := by omega
  have hlt6 : 2 ^ S 3 < 6 := by
    calc 2 ^ S 3 ≤ 2 ^ 2 := Nat.pow_le_pow_right (by norm_num) h2
      _ = 4 := by norm_num
      _ < 6 := by norm_num
  omega

/-! ## n = 3: three comparisons, attaining the information bound. -/

/-- The optimal three-comparison sorting tree on three keys. -/
def treeThree : ComparisonTree 3 :=
  .compare 0 1
    (.compare 1 2
      (.leaf (Equiv.refl (Fin 3)))
      (.compare 0 2
        (.leaf (Equiv.swap 1 2))
        (.leaf (finRotate 3).symm)))
    (.compare 0 2
      (.leaf (Equiv.swap 0 1))
      (.compare 1 2
        (.leaf (finRotate 3))
        (.leaf (Equiv.swap 0 2))))

theorem treeThree_correct : Correct treeThree := by
  intro ranking
  fin_cases ranking <;> decide

theorem hasBudget_three : HasBudget 3 3 :=
  ⟨treeThree, treeThree_correct, by decide⟩

theorem S_three : S 3 = 3 := by
  apply le_antisymm
  · rw [S_le_iff]; exact hasBudget_three
  · exact three_le_S_three

end SoringP1
