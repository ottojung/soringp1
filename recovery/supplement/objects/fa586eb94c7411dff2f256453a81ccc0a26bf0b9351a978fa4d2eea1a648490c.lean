import SoringP1.Monotone
import SoringP1.Bounds

/-!
# Strict monotonicity of the sorting number

For `n ≥ 1`, `S n + 1 ≤ S (n + 1)`.

The syntactic height `ComparisonTree.height` takes the maximum over every
syntactic branch, including branches that no ranking can reach. Hence the
inequality `height (prune U) + 1 ≤ height U` is *false* for an arbitrary
correct tree `U` on `n + 1` keys: an unreachable branch may be deeper than any
reachable one and may never compare the distinguished extra key. We therefore
use an operational measure — the execution length `runLen` of a single ranking —
and trim each tree down to the part reachable from a finite candidate set of
rankings.

The argument has two steps.

1. *Every maximal-key execution compares the maximal key.* For a correct
   `(n+1)`-key tree and any ranking `ρ` with `ρ (Fin.last n) = Fin.last n`, the
   execution path of `ρ` contains a comparison involving `Fin.last n`. Otherwise
   swapping the ranks `n` and `n-1` yields a different ranking that follows the
   same path but has a different inverse, contradicting correctness.

2. *Pruning lowers the reachable height by one.* For every `n`-key ranking `r`,
   the execution length of `r` in `prune U` equals the execution length of
   `ext r` in `U` minus the number of last-key comparisons on that path. Since
   that number is at least one and the execution length is at most the syntactic
   height, every `r` has execution length at most `height U - 1` in `prune U`.

Trimming `prune U` to the reachable part then yields a correct `n`-key tree of
syntactic height at most `height U - 1`, giving `S n + 1 ≤ S (n + 1)`.
-/

namespace SoringP1

open ComparisonTree

open scoped Classical

namespace ComparisonTree

/-- Number of comparisons on the execution path of `r`. -/
def runLen {n : ℕ} (r : Equiv.Perm (Fin n)) : ComparisonTree n → ℕ
  | .leaf _ => 0
  | .compare i j yes no => 1 + (if r i < r j then runLen r yes else runLen r no)

/-- Number of comparisons involving the last key on the execution path of `r`. -/
def lastCount {n : ℕ} (r : Equiv.Perm (Fin (n + 1))) : ComparisonTree (n + 1) → ℕ
  | .leaf _ => 0
  | .compare i j yes no =>
      (if i = Fin.last n ∨ j = Fin.last n then 1 else 0) +
        (if r i < r j then lastCount r yes else lastCount r no)

lemma runLen_le_height {n : ℕ} (r : Equiv.Perm (Fin n)) (T : ComparisonTree n) :
    runLen r T ≤ height T := by
  induction T with
  | leaf _ => simp [runLen, height]
  | compare i j yes no ihyes ihno =>
      have h : (if r i < r j then runLen r yes else runLen r no) ≤
          max (height yes) (height no) := by
        split
        · exact le_trans ihyes (le_max_left _ _)
        · exact le_trans ihno (le_max_right _ _)
      simp only [runLen, height]
      omega

lemma lastCount_le_runLen {n : ℕ} (r : Equiv.Perm (Fin (n + 1)))
    (T : ComparisonTree (n + 1)) : lastCount r T ≤ runLen r T := by
  induction T with
  | leaf _ => simp [lastCount, runLen]
  | compare i j yes no ihyes ihno =>
      have h1 : (if i = Fin.last n ∨ j = Fin.last n then 1 else 0) ≤ 1 := by
        split <;> omega
      have h2 : (if r i < r j then lastCount r yes else lastCount r no) ≤
          (if r i < r j then runLen r yes else runLen r no) := by
        split
        · exact ihyes
        · exact ihno
      simp only [lastCount, runLen]
      omega

end ComparisonTree

open ComparisonTree

/-! ## Pruning shortens every maximal-key execution by at least one -/

lemma runLen_prune_add {n : ℕ} (U : ComparisonTree (n + 1)) (r : Equiv.Perm (Fin n)) :
    runLen r (prune U) + lastCount (ext r) U = runLen (ext r) U := by
  induction U with
  | leaf σ => simp [prune, runLen, lastCount]
  | compare i j yes no ihyes ihno =>
      by_cases hi : i = Fin.last n
      · subst hi
        have hp : prune (.compare (Fin.last n) j yes no) = prune no := by
          simp only [prune]; rw [dite_eq_left trivial]
        rw [hp]
        have hnot : ¬ (ext r (Fin.last n) < ext r j) := by
          rw [ext_last]; exact not_lt_of_ge (Fin.le_last _)
        have hlc : lastCount (ext r) (.compare (Fin.last n) j yes no) =
            1 + lastCount (ext r) no := by
          simp only [lastCount]
          rw [ite_eq_left (Or.inl trivial), ite_eq_right hnot]
        rw [hlc]
        simp only [runLen]
        rw [ite_eq_right hnot]
        omega
      · by_cases hj : j = Fin.last n
        · subst hj
          have hp : prune (.compare i (Fin.last n) yes no) = prune yes := by
            simp only [prune]; rw [dite_eq_right hi, dite_eq_left trivial]
          rw [hp]
          have hlt : ext r i < ext r (Fin.last n) := by
            rw [← Fin.castSucc_castPred i hi, ext_castSucc, ext_last]
            exact Fin.castSucc_lt_last _
          have hlc : lastCount (ext r) (.compare i (Fin.last n) yes no) =
              1 + lastCount (ext r) yes := by
            simp only [lastCount]
            rw [ite_eq_left (Or.inr trivial), ite_eq_left hlt]
          rw [hlc]
          simp only [runLen]
          rw [ite_eq_left hlt]
          omega
        · have hp : prune (.compare i j yes no) =
              .compare (Fin.castPred i hi) (Fin.castPred j hj) (prune yes) (prune no) := by
            simp only [prune]; rw [dite_eq_right hi, dite_eq_right hj]
          rw [hp]
          have hi' : ext r i = Fin.castSucc (r (Fin.castPred i hi)) := by
            conv_lhs => rw [← Fin.castSucc_castPred i hi]; rw [ext_castSucc]
          have hj' : ext r j = Fin.castSucc (r (Fin.castPred j hj)) := by
            conv_lhs => rw [← Fin.castSucc_castPred j hj]; rw [ext_castSucc]
          have hiff : (ext r i < ext r j) ↔
              (r (Fin.castPred i hi) < r (Fin.castPred j hj)) := by
            rw [hi', hj', Fin.castSucc_lt_castSucc_iff]
          have hind : ¬ (i = Fin.last n ∨ j = Fin.last n) := by simp [hi, hj]
          have hlc : lastCount (ext r) (.compare i j yes no) =
              (if ext r i < ext r j then lastCount (ext r) yes else lastCount (ext r) no) := by
            simp only [lastCount]; rw [ite_eq_right hind, Nat.zero_add]
          rw [hlc]
          simp only [runLen]
          by_cases hc : r (Fin.castPred i hi) < r (Fin.castPred j hj)
          · simp only [ite_eq_left hc, ite_eq_left (hiff.mpr hc)]
            omega
          · simp only [ite_eq_right hc, ite_eq_right (fun h => hc (hiff.mp h))]
            omega

/-! ## Every maximal-key execution compares the maximal key -/

lemma swap_last_lt_iff {n : ℕ} (hpred : n - 1 < n + 1) {u v : Fin (n + 1)}
    (hu : u ≠ Fin.last n) (hv : v ≠ Fin.last n) :
    (u < v) ↔ (Equiv.swap (Fin.last n) ⟨n - 1, hpred⟩ u <
               Equiv.swap (Fin.last n) ⟨n - 1, hpred⟩ v) := by
  set c : Fin (n + 1) := ⟨n - 1, hpred⟩
  have hcval : c.val = n - 1 := rfl
  have hswap : ∀ w : Fin (n + 1), w ≠ Fin.last n →
      Equiv.swap (Fin.last n) c w = if w = c then Fin.last n else w := by
    intro w hw
    rw [Equiv.swap_apply_def, ite_eq_right hw]
  have hwc_lt : ∀ w : Fin (n + 1), w ≠ Fin.last n → w ≠ c → w < c := by
    intro w hw hw'
    have h1 : w.val < n := by
      have := (Fin.lt_last_iff_ne_last (n := n)).mpr hw
      rwa [Fin.lt_def, Fin.val_last] at this
    have h2 : w.val ≠ n - 1 := by
      intro h
      exact hw' (Fin.ext (h.trans hcval.symm))
    rw [Fin.lt_def]
    omega
  rw [hswap u hu, hswap v hv]
  by_cases huc : u = c
  · rw [ite_eq_left huc]
    by_cases hvc : v = c
    · rw [ite_eq_left hvc]
      subst huc; subst hvc; simp
    · rw [ite_eq_right hvc]
      subst huc
      have hvltc : v < c := hwc_lt v hv hvc
      constructor
      · intro h; exact absurd h (not_lt_of_ge (le_of_lt hvltc))
      · intro h; exact absurd h (not_lt_of_ge (Fin.le_last v))
  · rw [ite_eq_right huc]
    by_cases hvc : v = c
    · rw [ite_eq_left hvc]
      subst hvc
      have hultc : u < c := hwc_lt u hu huc
      constructor
      · intro _; exact lt_of_le_of_ne (Fin.le_last u) hu
      · intro _; exact hultc
    · rw [ite_eq_right hvc]

lemma run_eq_of_lastCount_zero {n : ℕ} (T : ComparisonTree (n + 1))
    (ρ ρ' : Equiv.Perm (Fin (n + 1))) (hlc : lastCount ρ T = 0)
    (hagree : ∀ i j, i ≠ Fin.last n → j ≠ Fin.last n → (ρ i < ρ j ↔ ρ' i < ρ' j)) :
    run ρ' T = run ρ T := by
  induction T with
  | leaf σ => rfl
  | compare i j yes no ihyes ihno =>
      have hsum : (if i = Fin.last n ∨ j = Fin.last n then 1 else 0) +
          (if ρ i < ρ j then lastCount ρ yes else lastCount ρ no) = 0 := by
        simpa only [lastCount] using hlc
      have hind : ¬ (i = Fin.last n ∨ j = Fin.last n) := by
        intro h; rw [ite_eq_left h] at hsum; omega
      have hbranch : (if ρ i < ρ j then lastCount ρ yes else lastCount ρ no) = 0 := by
        rw [ite_eq_right hind, Nat.zero_add] at hsum; exact hsum
      have hi : i ≠ Fin.last n := fun h => hind (Or.inl h)
      have hj : j ≠ Fin.last n := fun h => hind (Or.inr h)
      have hiff := hagree i j hi hj
      simp only [run]
      by_cases hc : ρ i < ρ j
      · rw [ite_eq_left hc, ite_eq_left (hiff.mp hc)]
        exact ihyes (by rw [ite_eq_left hc] at hbranch; exact hbranch)
      · rw [ite_eq_right hc, ite_eq_right (fun h => hc (hiff.mpr h))]
        exact ihno (by rw [ite_eq_right hc] at hbranch; exact hbranch)

theorem one_le_lastCount_ext {n : ℕ} (hn : 1 ≤ n) {T : ComparisonTree (n + 1)}
    (hT : Correct T) (r : Equiv.Perm (Fin n)) : 1 ≤ lastCount (ext r) T := by
  by_contra hcon
  have h0 : lastCount (ext r) T = 0 := by omega
  let ρ : Equiv.Perm (Fin (n + 1)) := ext r
  have hρlast : ρ (Fin.last n) = Fin.last n := ext_last r
  have hpred : n - 1 < n + 1 := by omega
  let c : Fin (n + 1) := ⟨n - 1, hpred⟩
  have hclast : c ≠ Fin.last n := by
    intro h
    have := congrArg Fin.val h
    simp only [c, Fin.val_last] at this
    omega
  let b : Fin (n + 1) := ρ.symm c
  have hbval : ρ b = c := by
    dsimp only [b]; exact Equiv.apply_symm_apply ρ c
  let ρ' : Equiv.Perm (Fin (n + 1)) := ρ.trans (Equiv.swap (Fin.last n) c)
  have hρ'apply : ∀ x, ρ' x = Equiv.swap (Fin.last n) c (ρ x) := fun x => rfl
  have hagree : ∀ i j, i ≠ Fin.last n → j ≠ Fin.last n → (ρ i < ρ j ↔ ρ' i < ρ' j) := by
    intro i j hi hj
    have hρi : ρ i ≠ Fin.last n := by
      intro h; exact hi (ρ.injective (h.trans hρlast.symm))
    have hρj : ρ j ≠ Fin.last n := by
      intro h; exact hj (ρ.injective (h.trans hρlast.symm))
    rw [hρ'apply i, hρ'apply j]
    exact swap_last_lt_iff hpred hρi hρj
  have hrun : run ρ' T = run ρ T := run_eq_of_lastCount_zero T ρ ρ' h0 hagree
  have h1 : run ρ T = ρ.symm := hT ρ
  have h2 : run ρ' T = ρ'.symm := hT ρ'
  have heq : ρ'.symm = ρ.symm := by rw [← h2, hrun, h1]
  have hperm : ρ' = ρ := by
    have := congrArg Equiv.symm heq
    simpa using this
  have hb' : ρ' b = Fin.last n := by
    rw [hρ'apply b, hbval, Equiv.swap_apply_right]
  have hb_eq : ρ' b = ρ b := by rw [hperm]
  rw [hb'] at hb_eq
  exact hclast (hb_eq.trans hbval).symm

/-! ## Reachable height and trimming -/

/-- The worst-case execution length over a candidate set of rankings. -/
noncomputable def rheight {n : ℕ} (C : Finset (Equiv.Perm (Fin n)))
    (T : ComparisonTree n) : ℕ :=
  C.sup (fun r => runLen r T)

lemma sup_eq_max_nat (a b : ℕ) : a ⊔ b = max a b := rfl

lemma sup_one_add {α : Type*} (s : Finset α) (f : α → ℕ) (h : s.Nonempty) :
    s.sup (fun a => 1 + f a) = 1 + s.sup f := by
  apply le_antisymm
  · exact Finset.sup_le fun a ha => Nat.add_le_add_left (Finset.le_sup ha) 1
  · obtain ⟨m, hm, hmval⟩ := Finset.exists_mem_eq_sup s h f
    rw [hmval]
    exact Finset.le_sup (f := fun a => 1 + f a) hm

lemma sup_one_add_eq {α : Type*} (s : Finset α) (f : α → ℕ) :
    s.sup (fun a => 1 + f a) = if s.Nonempty then 1 + s.sup f else 0 := by
  by_cases h : s.Nonempty
  · rw [ite_eq_left h, sup_one_add s f h]
  · rw [ite_eq_right h, Finset.not_nonempty_iff_eq_empty.mp h]
    simp

lemma sup_runLen_compare {n : ℕ} (C : Finset (Equiv.Perm (Fin n))) (i j : Fin n)
    (yes no : ComparisonTree n) :
    C.sup (fun r => runLen r (.compare i j yes no)) =
      (C.filter (fun r => r i < r j)).sup (fun r => 1 + runLen r yes) ⊔
      (C.filter (fun r => ¬ r i < r j)).sup (fun r => 1 + runLen r no) := by
  conv_lhs => rw [← Finset.filter_union_filter_not_eq (s := C)
    (p := fun r => r i < r j)]
  rw [Finset.sup_union]
  congr 1
  · exact Finset.sup_congr rfl fun r hr => by
      rw [runLen, ite_eq_left (Finset.mem_filter.mp hr).2]
  · exact Finset.sup_congr rfl fun r hr => by
      rw [runLen, ite_eq_right (Finset.mem_filter.mp hr).2]

/-- Delete the branches of `T` unreachable from some ranking in `C`. -/
noncomputable def trim {n : ℕ} (C : Finset (Equiv.Perm (Fin n))) : ComparisonTree n → ComparisonTree n
  | .leaf σ => .leaf σ
  | .compare i j yes no =>
      if (C.filter (fun r => r i < r j)).Nonempty then
        (if (C.filter (fun r => ¬ r i < r j)).Nonempty then
          .compare i j (trim (C.filter (fun r => r i < r j)) yes)
            (trim (C.filter (fun r => ¬ r i < r j)) no)
        else trim (C.filter (fun r => r i < r j)) yes)
      else trim (C.filter (fun r => ¬ r i < r j)) no

lemma height_trim_le_rheight {n : ℕ} (C : Finset (Equiv.Perm (Fin n)))
    (T : ComparisonTree n) : height (trim C T) ≤ rheight C T := by
  induction T generalizing C with
  | leaf σ =>
      rw [trim, height, rheight]
      simp only [runLen]
      exact Nat.zero_le _
  | compare i j yes no ihyes ihno =>
      have hsup : rheight C (.compare i j yes no) =
          max (if (C.filter (fun r => r i < r j)).Nonempty then
              1 + rheight (C.filter (fun r => r i < r j)) yes else 0)
              (if (C.filter (fun r => ¬ r i < r j)).Nonempty then
              1 + rheight (C.filter (fun r => ¬ r i < r j)) no else 0) := by
        rw [rheight, sup_runLen_compare, sup_one_add_eq, sup_one_add_eq]
        rfl
      rw [hsup, trim]
      by_cases hCy : (C.filter (fun r => r i < r j)).Nonempty
      · by_cases hCn : (C.filter (fun r => ¬ r i < r j)).Nonempty
        · simp only [ite_eq_left hCy, ite_eq_left hCn, height]
          have h1 := ihyes (C.filter (fun r => r i < r j))
          have h2 := ihno (C.filter (fun r => ¬ r i < r j))
          omega
        · simp only [ite_eq_left hCy, ite_eq_right hCn]
          rw [max_eq_left (Nat.zero_le _)]
          exact le_trans (ihyes (C.filter (fun r => r i < r j))) (Nat.le_add_left _ _)
      · simp only [ite_eq_right hCy]
        by_cases hCn : (C.filter (fun r => ¬ r i < r j)).Nonempty
        · rw [ite_eq_left hCn, max_eq_right (Nat.zero_le _)]
          exact le_trans (ihno (C.filter (fun r => ¬ r i < r j))) (Nat.le_add_left _ _)
        · rw [ite_eq_right hCn, max_eq_right (Nat.zero_le _)]
          have hzero : rheight (C.filter (fun r => ¬ r i < r j)) no = 0 := by
            have heq : (C.filter (fun r => ¬ r i < r j)) = ∅ :=
              Finset.not_nonempty_iff_eq_empty.mp hCn
            rw [rheight, heq]; simp
          exact le_trans (ihno (C.filter (fun r => ¬ r i < r j))) hzero.le

lemma run_trim {n : ℕ} (C : Finset (Equiv.Perm (Fin n))) (T : ComparisonTree n) :
    ∀ r ∈ C, run r (trim C T) = run r T := by
  induction T generalizing C with
  | leaf σ => intro r hr; rfl
  | compare i j yes no ihyes ihno =>
      intro r hr
      rw [trim]
      by_cases hCy : (C.filter (fun r => r i < r j)).Nonempty
      · by_cases hCn : (C.filter (fun r => ¬ r i < r j)).Nonempty
        · simp only [ite_eq_left hCy, ite_eq_left hCn]
          by_cases hc : r i < r j
          · simp only [run, ite_eq_left hc]
            exact ihyes (C.filter (fun r => r i < r j)) r (Finset.mem_filter.mpr ⟨hr, hc⟩)
          · simp only [run, ite_eq_right hc]
            exact ihno (C.filter (fun r => ¬ r i < r j)) r (Finset.mem_filter.mpr ⟨hr, hc⟩)
        · simp only [ite_eq_left hCy, ite_eq_right hCn]
          have hc : r i < r j := by
            by_contra h; exact hCn ⟨r, Finset.mem_filter.mpr ⟨hr, h⟩⟩
          simp only [run, ite_eq_left hc]
          exact ihyes (C.filter (fun r => r i < r j)) r (Finset.mem_filter.mpr ⟨hr, hc⟩)
      · simp only [ite_eq_right hCy]
        have hc : ¬ r i < r j := by
          by_contra h; exact hCy ⟨r, Finset.mem_filter.mpr ⟨hr, h⟩⟩
        simp only [run, ite_eq_right hc]
        exact ihno (C.filter (fun r => ¬ r i < r j)) r (Finset.mem_filter.mpr ⟨hr, hc⟩)

/-- Every ranking has execution length at most `height T - 1` in the pruned tree. -/
lemma rheight_prune_le {n : ℕ} (hn : 1 ≤ n) {T : ComparisonTree (n + 1)}
    (hT : Correct T) :
    rheight (Finset.univ : Finset (Equiv.Perm (Fin n))) (prune T) ≤ height T - 1 := by
  rw [rheight]
  refine Finset.sup_le fun r _ => ?_
  have h1 := runLen_prune_add T r
  have h2 := one_le_lastCount_ext hn hT r
  have h3 := runLen_le_height (ext r) T
  omega

/-- **Strict monotonicity of the sorting number**: `S n + 1 ≤ S (n + 1)` for
`n ≥ 1`. -/
theorem S_strict_mono {n : ℕ} (hn : 1 ≤ n) : S n + 1 ≤ S (n + 1) := by
  obtain ⟨T, hTcorr, hTheight⟩ := exists_tree_S (n + 1)
  let U : ComparisonTree n :=
    trim (Finset.univ : Finset (Equiv.Perm (Fin n))) (prune T)
  have hUcorr : Correct U := by
    intro r
    show run r U = r.symm
    dsimp only [U]
    rw [run_trim (Finset.univ : Finset (Equiv.Perm (Fin n))) (prune T) r (Finset.mem_univ r)]
    exact run_prune T r (hTcorr (ext r))
  have hUheight : height U ≤ height T - 1 := by
    dsimp only [U]
    exact le_trans (height_trim_le_rheight _ _) (rheight_prune_le hn hTcorr)
  have hS : S n ≤ height U := (S_le_iff (n := n)).2 ⟨U, hUcorr, le_refl _⟩
  have hheight : 1 ≤ height T := by
    have h1 : n ≤ S (n + 1) := n_sub_one_le_S (n + 1)
    have h2 : S (n + 1) ≤ height T := (S_le_iff (n := n + 1)).2 ⟨T, hTcorr, le_refl _⟩
    omega
  omega

end SoringP1
