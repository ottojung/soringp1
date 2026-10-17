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

theorem log2_factorial_le_S (n : ℕ) : Nat.log2 n.factorial ≤ S n := by
  by_contra h
  have hle : S n + 1 ≤ Nat.log2 n.factorial := by omega
  have h2 : 2 ^ (S n + 1) ≤ n.factorial :=
    (Nat.le_log2 (Nat.factorial_ne_zero n)).1 hle
  have h3 : n.factorial ≤ 2 ^ S n := factorial_le_two_pow_S n
  have hlt : 2 ^ S n < 2 ^ (S n + 1) :=
    Nat.pow_lt_pow_right (by norm_num) (Nat.lt_succ_self _)
  exact absurd (le_trans h2 h3) (not_le.mpr hlt)

/-- A usable form of the information lower bound: if `2 ^ (k-1) < n!` then
`k ≤ S n`. (Take `k` a lower bound on `log₂ n!`.) -/
lemma le_S_of_pow_lt (n k : ℕ) (h : 2 ^ (k - 1) < n.factorial) : k ≤ S n := by
  by_contra hlt
  have h2 : S n ≤ k - 1 := by omega
  have h3 : n.factorial ≤ 2 ^ S n := factorial_le_two_pow_S n
  have h4 : 2 ^ S n ≤ 2 ^ (k - 1) := Nat.pow_le_pow_right (by norm_num) h2
  omega

theorem sixteen_le_S_eight : 16 ≤ S 8 := le_S_of_pow_lt 8 16 (by norm_num)

/-- The information lower bound in ceiling-logarithm form:
`S n ≥ ⌈log₂ n!⌉`. -/
theorem clog_factorial_le_S (n : ℕ) : Nat.clog 2 n.factorial ≤ S n :=
  (Nat.clog_le_iff_le_pow (by norm_num : 1 < 2)).2 (factorial_le_two_pow_S n)

end SoringP1
