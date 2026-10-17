import SoringP1.SmallValues
import SoringP1.SmallValues4
import SoringP1.SmallValues5
import SoringP1.SmallValues6
import SoringP1.Bounds

/-!
# The information bound is tight for `n ≤ 6`

For `n ≤ 6` the exact value equals `⌈log₂ n!⌉`; the lower bound is A15/A2 and the
upper bound is the explicit optimal trees of A4/A5/A7.
-/

namespace SoringP1

theorem S_eq_clog_of_le_six (n : ℕ) (h : n ≤ 6) : S n = Nat.clog 2 n.factorial := by
  interval_cases n
  · rw [S_zero]; decide
  · rw [S_one]; decide
  · rw [S_two]; decide
  · rw [S_three]; decide
  · rw [S_four]; decide
  · rw [S_five]; decide
  · rw [S_six]; decide

end SoringP1
