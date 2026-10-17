import SoringP1.LowerBound

/-!
# Elementary general bounds for `S`

Additional general consequences of the information bound `n! ≤ 2 ^ S n`
(`SoringP1.LowerBound`) and the monotonicity `S n ≤ S (n+1)`
(`SoringP1.Monotone`).
-/

namespace SoringP1

/-- `2 ^ n ≤ (n + 1)!`. -/
lemma two_pow_le_factorial (n : ℕ) : 2 ^ n ≤ (n + 1).factorial := by
  induction n with
  | zero => norm_num
  | succ k ih =>
    calc 2 ^ (k + 1) = 2 * 2 ^ k := by ring
      _ ≤ 2 * (k + 1).factorial := Nat.mul_le_mul_left 2 ih
      _ ≤ (k + 2) * (k + 1).factorial :=
            Nat.mul_le_mul_right _ (by omega)
      _ = (k + 2).factorial := (Nat.factorial_succ (k + 1)).symm

/-- `2 ^ (n - 1) ≤ n!`. -/
lemma two_pow_pred_le_factorial (n : ℕ) : 2 ^ (n - 1) ≤ n.factorial := by
  rcases Nat.eq_zero_or_pos n with hn | hn
  · subst hn; norm_num
  · have h := two_pow_le_factorial (n - 1)
    rwa [Nat.sub_add_cancel (Nat.succ_le_of_lt hn)] at h

/-- `S n ≥ n - 1`: a correct tree performs at least `n - 1` comparisons. -/
theorem n_sub_one_le_S (n : ℕ) : n - 1 ≤ S n := by
  have h1 : 2 ^ (n - 1) ≤ n.factorial := two_pow_pred_le_factorial n
  have h2 : n.factorial ≤ 2 ^ S n := factorial_le_two_pow_S n
  exact (Nat.pow_le_pow_iff_right (by norm_num : 1 < 2)).1 (le_trans h1 h2)

end SoringP1
