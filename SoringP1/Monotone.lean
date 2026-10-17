import SoringP1.Attainment

/-!
# Monotonicity of the sorting number `S`

Milestone A8: `S n ≤ S (n + 1)`.

Given an optimal correct decision tree on `n + 1` keys, we prune it to a
correct decision tree on `n` keys of no greater height. The extra key
`Fin.last n` is treated as the largest, so every comparison against it has a
known outcome. This yields `HasBudget n (height T)` for any correct `T` on
`n + 1`, hence `S n ≤ S (n + 1)`.
-/

namespace SoringP1

open ComparisonTree

/-- Extend a ranking of `Fin n` to a ranking of `Fin (n + 1)` that fixes the
last position and agrees with `r` on the first `n` positions. -/
noncomputable def ext {n : ℕ} (r : Equiv.Perm (Fin n)) : Equiv.Perm (Fin (n + 1)) :=
  Equiv.ofBijective
    (fun i => Fin.lastCases (Fin.last n) (fun k => Fin.castSucc (r k)) i)
    (by
      constructor
      · intro a b hab
        cases a using Fin.lastCases with
        | last =>
          cases b using Fin.lastCases with
          | last => rfl
          | cast j =>
            simp only [Fin.lastCases_last, Fin.lastCases_castSucc] at hab
            exact absurd hab.symm (Fin.castSucc_ne_last (r j))
        | cast i =>
          cases b using Fin.lastCases with
          | last =>
            simp only [Fin.lastCases_last, Fin.lastCases_castSucc] at hab
            exact absurd hab (Fin.castSucc_ne_last (r i))
          | cast j =>
            simp only [Fin.lastCases_castSucc] at hab
            exact congrArg Fin.castSucc (r.injective (Fin.castSucc_inj.1 hab))
      · intro b
        cases b using Fin.lastCases with
        | last => exact ⟨Fin.last n, by simp⟩
        | cast k => exact ⟨Fin.castSucc (r.symm k), by simp⟩)

@[simp] lemma ext_last {n : ℕ} (r : Equiv.Perm (Fin n)) :
    ext r (Fin.last n) = Fin.last n := by
  change Fin.lastCases (Fin.last n) (fun k => Fin.castSucc (r k)) (Fin.last n) = Fin.last n
  simp

@[simp] lemma ext_castSucc {n : ℕ} (r : Equiv.Perm (Fin n)) (k : Fin n) :
    ext r (Fin.castSucc k) = Fin.castSucc (r k) := by
  change Fin.lastCases (Fin.last n) (fun k => Fin.castSucc (r k)) (Fin.castSucc k) =
    Fin.castSucc (r k)
  simp

/-- Restrict a permutation of `Fin (n + 1)` that fixes the last position to a
permutation of `Fin n`. If it does not fix the last position, return the
identity. -/
noncomputable def stripMax {n : ℕ} (σ : Equiv.Perm (Fin (n + 1))) : Equiv.Perm (Fin n) :=
  if h : σ (Fin.last n) = Fin.last n then
    Equiv.ofBijective
      (fun k : Fin n =>
        ⟨(σ (Fin.castSucc k)).val, by
          have hsymm : σ.symm (Fin.last n) = Fin.last n := by
            calc σ.symm (Fin.last n) = σ.symm (σ (Fin.last n)) := by rw [h]
              _ = Fin.last n := Equiv.symm_apply_apply σ _
          have hne : σ (Fin.castSucc k) ≠ Fin.last n := by
            intro hc
            have hcl : Fin.castSucc k = Fin.last n := by
              rw [← Equiv.symm_apply_apply σ (Fin.castSucc k), hc, hsymm]
            exact Fin.castSucc_ne_last k hcl
          exact Fin.val_lt_last hne⟩)
      (by
        constructor
        · intro a b hab
          have h1 : σ (Fin.castSucc a) = σ (Fin.castSucc b) := by
            apply Fin.ext
            have hv := congrArg Fin.val hab
            simpa only [] using hv
          exact Fin.castSucc_injective n (σ.injective h1)
        · intro b
          have hne : σ.symm (Fin.castSucc b) ≠ Fin.last n := by
            intro hc
            have hcl : Fin.castSucc b = Fin.last n := by
              rw [← Equiv.apply_symm_apply σ (Fin.castSucc b), hc, h]
            exact Fin.castSucc_ne_last b hcl
          refine ⟨Fin.castPred (σ.symm (Fin.castSucc b)) hne, ?_⟩
          apply Fin.ext
          change (σ (Fin.castSucc (Fin.castPred (σ.symm (Fin.castSucc b)) hne))).val = b.val
          rw [Fin.castSucc_castPred, Equiv.apply_symm_apply]
          rfl)
  else 1

/-- Restricting `(ext r).symm` recovers `r.symm`. -/
lemma stripMax_symm_ext {n : ℕ} (r : Equiv.Perm (Fin n)) :
    stripMax ((ext r).symm) = r.symm := by
  unfold stripMax
  have hfix : (ext r).symm (Fin.last n) = Fin.last n := by
    rw [Equiv.symm_apply_eq, ext_last]
  rw [dite_eq_left hfix]
  apply Equiv.ext
  intro k
  apply Fin.ext
  have h1 : ext r (Fin.castSucc (r.symm k)) = Fin.castSucc k := by
    rw [ext_castSucc, Equiv.apply_symm_apply]
  have h2 : (ext r).symm (Fin.castSucc k) = Fin.castSucc (r.symm k) := by
    rw [← h1, Equiv.symm_apply_apply]
  change ((ext r).symm (Fin.castSucc k)).val = (r.symm k).val
  rw [h2]
  rfl

/-- Prune an `(n + 1)`-key decision tree to an `n`-key tree by treating the
last key as the largest: comparisons against it have a known outcome. -/
noncomputable def prune {n : ℕ} : ComparisonTree (n + 1) → ComparisonTree n
  | .leaf σ => .leaf (stripMax σ)
  | .compare i j yes no =>
      if hi : i = Fin.last n then prune no
      else if hj : j = Fin.last n then prune yes
      else .compare (Fin.castPred i hi) (Fin.castPred j hj) (prune yes) (prune no)

lemma height_prune {n : ℕ} (U : ComparisonTree (n + 1)) :
    height (prune U) ≤ height U := by
  induction U with
  | leaf σ => simp only [prune, height]; exact le_refl 0
  | compare i j yes no ihyes ihno =>
      by_cases hi : i = Fin.last n
      · subst i
        have hp : prune (.compare (Fin.last n) j yes no) = prune no := by
          simp only [prune]
          rw [dite_eq_left trivial]
        rw [hp]
        simp only [height]
        omega
      · by_cases hj : j = Fin.last n
        · subst j
          have hp : prune (.compare i (Fin.last n) yes no) = prune yes := by
            simp only [prune]
            rw [dite_eq_right hi, dite_eq_left trivial]
          rw [hp]
          simp only [height]
          omega
        · have hp : prune (.compare i j yes no) =
              .compare (Fin.castPred i hi) (Fin.castPred j hj) (prune yes) (prune no) := by
            simp only [prune]
            rw [dite_eq_right hi, dite_eq_right hj]
          rw [hp]
          simp only [height]
          exact Nat.add_le_add_left (max_le_max ihyes ihno) 1

/-- Running the pruned tree on `r` mirrors running the original tree on the
extension `ext r`, as long as the original run is correct. -/
lemma run_prune {n : ℕ} (U : ComparisonTree (n + 1)) (r : Equiv.Perm (Fin n))
    (h : run (ext r) U = (ext r).symm) : run r (prune U) = r.symm := by
  induction U with
  | leaf σ =>
      simp only [run] at h
      simp only [prune, run]
      rw [h]
      exact stripMax_symm_ext r
  | compare i j yes no ihyes ihno =>
      by_cases hi : i = Fin.last n
      · subst i
        have hp : prune (.compare (Fin.last n) j yes no) = prune no := by
          simp only [prune]
          rw [dite_eq_left trivial]
        rw [hp]
        have hlt : ¬ (ext r (Fin.last n) < ext r j) := by
          rw [ext_last]
          exact not_lt_of_ge (Fin.le_last _)
        have hh := h
        simp only [run] at hh
        rw [ite_eq_right hlt] at hh
        exact ihno hh
      · by_cases hj : j = Fin.last n
        · subst j
          have hp : prune (.compare i (Fin.last n) yes no) = prune yes := by
            simp only [prune]
            rw [dite_eq_right hi, dite_eq_left trivial]
          rw [hp]
          have hlt : ext r i < ext r (Fin.last n) := by
            rw [← Fin.castSucc_castPred i hi, ext_castSucc, ext_last]
            exact Fin.castSucc_lt_last _
          have hh := h
          simp only [run] at hh
          rw [ite_eq_left hlt] at hh
          exact ihyes hh
        · have hp : prune (.compare i j yes no) =
              .compare (Fin.castPred i hi) (Fin.castPred j hj) (prune yes) (prune no) := by
            simp only [prune]
            rw [dite_eq_right hi, dite_eq_right hj]
          rw [hp]
          simp only [run]
          have hi' : ext r i = Fin.castSucc (r (Fin.castPred i hi)) := by
            conv_lhs => rw [← Fin.castSucc_castPred i hi]
            rw [ext_castSucc]
          have hj' : ext r j = Fin.castSucc (r (Fin.castPred j hj)) := by
            conv_lhs => rw [← Fin.castSucc_castPred j hj]
            rw [ext_castSucc]
          have hcond : (ext r i < ext r j) ↔
              (r (Fin.castPred i hi) < r (Fin.castPred j hj)) := by
            rw [hi', hj', Fin.castSucc_lt_castSucc_iff]
          by_cases hc : r (Fin.castPred i hi) < r (Fin.castPred j hj)
          · rw [ite_eq_left hc]
            have hh := h
            simp only [run] at hh
            rw [ite_eq_left (hcond.mpr hc)] at hh
            exact ihyes hh
          · rw [ite_eq_right hc]
            have hh := h
            simp only [run] at hh
            rw [ite_eq_right (fun hx => hc (hcond.mp hx))] at hh
            exact ihno hh

/-- Feasibility is monotone in `n`: a budget feasible for `n + 1` keys is
feasible for `n` (prune the extra key). -/
lemma hasBudget_prune {n k : ℕ} (h : HasBudget (n + 1) k) : HasBudget n k := by
  obtain ⟨T, hcorr, hheight⟩ := h
  exact ⟨prune T, fun r => run_prune T r (hcorr (ext r)), le_trans (height_prune T) hheight⟩

/-- The sorting number is monotone: `S n ≤ S (n + 1)`. -/
theorem S_mono (n : ℕ) : S n ≤ S (n + 1) := by
  obtain ⟨T, hTcorr, hTheight⟩ := exists_tree_S (n + 1)
  have hbudget : HasBudget n (height T) :=
    ⟨prune T, fun r => run_prune T r (hTcorr (ext r)), height_prune T⟩
  exact le_trans ((S_le_iff (n := n) (k := height T)).2 hbudget) hTheight

end SoringP1
