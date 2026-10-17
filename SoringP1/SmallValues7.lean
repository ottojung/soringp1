import SoringP1.TightBound
import SoringP1.Bounds

/-!
# A bracket for `S 7`

`S 7` is beyond the range the reference evaluator and the minimax generator
reach, but the general bounds still pin it: the information lower bound gives
`S 7 ≥ 13` (`2^12 = 4096 < 7! = 5040`), and the tight insertion upper bound
(A10) gives `S 7 ≤ 21`.
-/

namespace SoringP1

theorem thirteen_le_S_seven : 13 ≤ S 7 := by
  have h : (7 : ℕ).factorial ≤ 2 ^ S 7 := factorial_le_two_pow_S 7
  norm_num at h
  by_contra hlt
  have h2 : S 7 ≤ 12 := by omega
  have hle : 2 ^ S 7 ≤ 2 ^ 12 := Nat.pow_le_pow_right (by norm_num) h2
  have hlt' : (2 : ℕ) ^ 12 < 2 ^ S 7 :=
    lt_of_lt_of_le (show (2 : ℕ) ^ 12 < 5040 by norm_num) h
  omega

theorem S_seven_le : S 7 ≤ 21 := by
  have h := S_le_tight 7
  norm_num at h
  exact h

/-- `13 ≤ S 7 ≤ 21`. -/
theorem S_seven_bracket : 13 ≤ S 7 ∧ S 7 ≤ 21 :=
  ⟨thirteen_le_S_seven, S_seven_le⟩

end SoringP1
