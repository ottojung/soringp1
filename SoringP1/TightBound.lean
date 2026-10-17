import SoringP1.Existence
import SoringP1.Attainment

/-!
# A tight upper bound: `S n ≤ n (n - 1) / 2`

The insertion tree `sortTree` inserts positions `0, 1, …, n-1` one at a time;
inserting position `i` costs at most `i` comparisons, so the true height is at
most `0 + 1 + … + (n-1) = n(n-1)/2`. The existing `height_go` only gives
`height ≤ fuel` (counting structural steps too); here we prove the
comparison-exact bound with a length-only invariant (so both children of a
comparison node satisfy it).
-/

namespace SoringP1

/-- Comparisons to insert positions `m, m+1, …, n-1`: their sum. -/
def Hinto (n m : ℕ) : ℕ := ∑ i ∈ Finset.range (n - m), (m + i)

/-- Comparison budget for an `aux` state: scan `suf`, then insert `x+1`. -/
def Haux (n : ℕ) (x : Fin n) (suf : List (Fin n)) : ℕ :=
  suf.length + Hinto n (x.val + 1)

lemma Hinto_self (n : ℕ) : Hinto n n = 0 := by
  simp [Hinto]

lemma Hinto_succ (n m : ℕ) (hm : m < n) : Hinto n m = m + Hinto n (m + 1) := by
  have h : n - m = (n - (m + 1)) + 1 := by omega
  simp only [Hinto]
  conv_lhs => rw [h, Finset.sum_range_succ']
  rw [show (∑ i ∈ Finset.range (n - (m + 1)), (m + (i + 1)))
        = (∑ i ∈ Finset.range (n - (m + 1)), ((m + 1) + i)) from
      Finset.sum_congr rfl (fun i _ => by omega)]
  omega

lemma Hinto_zero (n : ℕ) : Hinto n 0 = n * (n - 1) / 2 := by
  rw [Hinto]
  simp only [Nat.sub_zero, Nat.zero_add]
  exact Finset.sum_range_id n

/-- Comparison-exact height bound for the fuel-driven insertion sort. -/
lemma height_go_tight (n : ℕ) : ∀ fuel,
    (∀ (m : ℕ) (hm : m ≤ n) (sp : List (Fin n)),
        sp.length = m → ComparisonTree.height (go n fuel (.into m hm sp)) ≤ Hinto n m) ∧
    (∀ (x : Fin n) (pre suf : List (Fin n)),
        pre.length + suf.length = x.val →
        ComparisonTree.height (go n fuel (.aux x pre suf)) ≤ Haux n x suf) := by
  intro fuel
  induction fuel with
  | zero =>
      refine ⟨?_, ?_⟩
      · intro m hm sp _; rw [go.eq_1]; simp [ComparisonTree.height]
      · intro x pre suf _; rw [go.eq_1]; simp [ComparisonTree.height]
  | succ k ih =>
      refine ⟨?_, ?_⟩
      · intro m hm sp hlen
        by_cases hmn : m = n
        · subst hmn
          rw [go.eq_2, dite_eq_left rfl]
          simp [ComparisonTree.height, Hinto_self]
        · rw [go.eq_2, dite_eq_right hmn]
          have hlt : m < n := by omega
          have h := ih.2 ⟨m, hlt⟩ [] sp (by simp only [List.length_nil, Nat.zero_add]; exact hlen)
          refine le_trans h ?_
          rw [Haux, hlen]
          exact le_of_eq (Hinto_succ n m hlt).symm
      · intro x pre suf hlen
        cases suf with
        | nil =>
            rw [go.eq_3]
            simp only [List.length_nil, Nat.add_zero] at hlen
            have h := ih.1 (x.val + 1) (by have := x.isLt; omega) (pre ++ [x])
              (by simp only [List.length_append, List.length_cons, List.length_nil]; omega)
            refine le_trans h ?_
            simp [Haux]
        | cons q tl =>
            rw [go.eq_4]
            simp only [ComparisonTree.height]
            simp only [List.length_cons] at hlen
            have h1 := ih.1 (x.val + 1) (by have := x.isLt; omega) (pre ++ [x] ++ q :: tl)
              (by simp only [List.length_append, List.length_cons, List.length_nil]; omega)
            have h2 := ih.2 x (pre ++ [q]) tl
              (by simp only [List.length_append, List.length_cons, List.length_nil]; omega)
            simp only [Haux, List.length_cons] at h2 ⊢
            omega

theorem sortTree_height_tight (n : ℕ) :
    ComparisonTree.height (sortTree n) ≤ n * (n - 1) / 2 := by
  unfold sortTree
  have h := (height_go_tight n (n * (n + 2) + (n + 1) + 1)).1 0 (Nat.zero_le n) [] (by simp)
  exact le_trans h (le_of_eq (Hinto_zero n))

/-- The tight upper bound on the sorting number. -/
theorem S_le_tight (n : ℕ) : S n ≤ n * (n - 1) / 2 :=
  (S_le_iff (n := n)).2 ⟨sortTree n, sortTree_correct n, sortTree_height_tight n⟩

end SoringP1
