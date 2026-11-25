import SoringP1.StrictMonotone

/-!
# One-sided Lipschitz bound for the sorting number

The intended construction sorts the first `n` keys optimally and then inserts
the last key by binary search among the `n + 1` possible ranks.
-/

namespace SoringP1

open ComparisonTree
open scoped Classical

namespace ComparisonTree

/-- Among the first `n` labels, the number below label `a` in `ρ`. -/
noncomputable def relRankCount {n : ℕ} (ρ : Equiv.Perm (Fin (n + 1))) (a : Fin n) : ℕ :=
  (Finset.univ.filter (fun b : Fin n => ρ b.castSucc < ρ a.castSucc)).card

lemma relRankCount_lt {n : ℕ} (ρ : Equiv.Perm (Fin (n + 1)))
    {a b : Fin n} (h : ρ a.castSucc < ρ b.castSucc) :
    relRankCount ρ a < relRankCount ρ b := by
  apply Finset.card_lt_card
  rw [Finset.ssubset_iff_subset_ne]
  refine ⟨?_, ?_⟩
  · intro c hc
    rw [Finset.mem_filter] at hc ⊢
    exact ⟨hc.1, lt_trans hc.2 h⟩
  · intro heq
    have hb : a ∈ Finset.univ.filter (fun c : Fin n => ρ c.castSucc < ρ b.castSucc) := by
      rw [Finset.mem_filter]
      exact ⟨Finset.mem_univ _, h⟩
    have ha : a ∈ Finset.univ.filter (fun c : Fin n => ρ c.castSucc < ρ a.castSucc) := by
      rw [← heq] at hb
      exact hb
    exact (lt_irrefl _ (Finset.mem_filter.mp ha).2)

/-- Restrict an `(n+1)`-key ranking to the first `n` keys and renumber them in
their relative increasing order. -/
noncomputable def rel {n : ℕ} (ρ : Equiv.Perm (Fin (n + 1))) :
    Equiv.Perm (Fin n) :=
  Equiv.ofBijective
    (fun a : Fin n => ⟨relRankCount ρ a, by
      have hsub : (Finset.univ.filter (fun b : Fin n => ρ b.castSucc < ρ a.castSucc))
          ⊆ Finset.univ.erase a := by
        intro b hb
        rw [Finset.mem_filter] at hb
        rw [Finset.mem_erase]
        refine ⟨?_, Finset.mem_univ _⟩
        intro hba
        subst b
        exact (lt_irrefl _ hb.2)
      have hcard := Finset.card_le_card hsub
      have herase : (Finset.univ.erase a : Finset (Fin n)).card = n - 1 := by
        rw [Finset.card_erase_of_mem (Finset.mem_univ a), Finset.card_univ, Fintype.card_fin]
      rw [relRankCount]
      rw [herase] at hcard
      have haLt : a.val < n := a.isLt
      omega⟩)
    (by
      rw [Fintype.bijective_iff_injective_and_card]
      refine ⟨?_, by simp⟩
      intro a b hab
      by_contra habne
      have hrankne : ρ a.castSucc ≠ ρ b.castSucc := by
        intro heq
        exact habne (Fin.castSucc_injective n (ρ.injective heq))
      rcases lt_or_gt_of_ne hrankne with hlt | hgt
      · have hcount := relRankCount_lt ρ hlt
        have hv := congrArg Fin.val hab
        change relRankCount ρ a = relRankCount ρ b at hv
        omega
      · have hcount := relRankCount_lt ρ hgt
        have hv := congrArg Fin.val hab
        change relRankCount ρ a = relRankCount ρ b at hv
        omega)

lemma rel_lt_iff {n : ℕ} (ρ : Equiv.Perm (Fin (n + 1)))
    (a b : Fin n) : rel ρ a < rel ρ b ↔ ρ a.castSucc < ρ b.castSucc := by
  change relRankCount ρ a < relRankCount ρ b ↔
    (ρ a.castSucc).val < (ρ b.castSucc).val
  by_cases heq : a = b
  · subst b
    simp
  · have hvalne : ρ a.castSucc ≠ ρ b.castSucc := by
      intro h
      exact heq (Fin.castSucc_injective n (ρ.injective h))
    rcases lt_or_gt_of_ne hvalne with hlt | hgt
    · constructor
      · intro _; exact Fin.lt_def.mp hlt
      · intro h; exact relRankCount_lt ρ (Fin.lt_def.mpr h)
    · refine ⟨?_, ?_⟩
      · intro h
        have hrev := relRankCount_lt ρ (Fin.lt_def.mpr hgt)
        omega
      · intro h
        have hrev := Fin.lt_def.mp hgt
        omega

/-- The rank of an item is the number of items below it. -/
lemma rank_val_eq_card_lt {N : ℕ} (ρ : Equiv.Perm (Fin N)) (x : Fin N) :
    (ρ x).val = (Finset.univ.filter (fun y : Fin N => ρ y < ρ x)).card := by
  have himage : (Finset.Iio (ρ x)).image ρ.symm =
      Finset.univ.filter (fun y : Fin N => ρ y < ρ x) := by
    ext y
    rw [Finset.mem_image, Finset.mem_filter]
    constructor
    · rintro ⟨z, hz, rfl⟩
      refine ⟨Finset.mem_univ _, ?_⟩
      simpa using (Finset.mem_Iio.mp hz)
    · rintro ⟨_, hy⟩
      refine ⟨ρ y, Finset.mem_Iio.mpr ?_, ?_⟩
      · simpa using hy
      · simp
  rw [← himage, Finset.card_image_of_injective _ ρ.symm.injective]
  simp

/-- The `m`-th smallest of the first `n` keys has rank `m` if it lies below the
last key, and rank `m+1` otherwise. -/
lemma rel_symm_castSucc_val {n : ℕ} (ρ : Equiv.Perm (Fin (n + 1)))
    (m : Fin n) :
    (ρ (Fin.castSucc ((rel ρ).symm m))).val =
      if m.val < (ρ (Fin.last n)).val then m.val else m.val + 1 := by
  let p : Equiv.Perm (Fin n) := (rel ρ).symm
  let x : Fin (n + 1) := Fin.castSucc (p m)
  have hcount : relRankCount ρ (p m) = m.val := by
    have hrel : rel ρ (p m) = m := Equiv.apply_symm_apply (rel ρ) m
    have h := congrArg Fin.val hrel
    change relRankCount ρ (p m) = m.val
    exact h
  have hwhole := rank_val_eq_card_lt ρ x
  have hdecomp : (Finset.univ.filter (fun y : Fin (n + 1) => ρ y < ρ x)).card =
      relRankCount ρ (p m) +
        (if ρ (Fin.last n) < ρ x then 1 else 0) := by
    have huniv : (Finset.univ : Finset (Fin (n + 1))) =
        {Fin.last n} ∪ (Finset.univ.map Fin.castSuccEmb) := by
      rw [Fin.univ_castSuccEmb]
      simp
    have hlastnot : Fin.last n ∉ Finset.univ.map Fin.castSuccEmb := by
      simp [Finset.mem_map, Fin.castSucc_ne_last]
    have hdisj : Disjoint ({Fin.last n} : Finset (Fin (n + 1)))
        (Finset.univ.map Fin.castSuccEmb) := by
      rw [Finset.disjoint_left]
      intro y hy hz
      have hy' : y = Fin.last n := Finset.mem_singleton.mp hy
      subst y
      exact hlastnot hz
    have hfilterMap :
        (Finset.univ.map Fin.castSuccEmb).filter (fun y : Fin (n + 1) => ρ y < ρ x) =
          (Finset.univ.filter (fun b : Fin n => ρ b.castSucc < ρ x)).map
            Fin.castSuccEmb := by
      rw [Finset.filter_map]
      rfl
    have hdisjFilter : Disjoint
        (Finset.filter (fun y : Fin (n + 1) => ρ y < ρ x) {Fin.last n})
        (Finset.filter (fun y : Fin (n + 1) => ρ y < ρ x)
          (Finset.univ.map Fin.castSuccEmb)) := by
      rw [Finset.disjoint_left]
      intro y hy hz
      have hymem : y ∈ ({Fin.last n} : Finset (Fin (n + 1))) := (Finset.mem_filter.mp hy).1
      have hy' : y = Fin.last n := Finset.mem_singleton.mp hymem
      subst y
      exact hlastnot (Finset.mem_filter.mp hz).1
    have hsingle :
        (Finset.filter (fun y : Fin (n + 1) => ρ y < ρ x) {Fin.last n}).card =
          if ρ (Fin.last n) < ρ x then 1 else 0 := by
      rw [Finset.filter_singleton]
      by_cases h : ρ (Fin.last n) < ρ x <;> simp [h]
    rw [huniv, Finset.filter_union, Finset.card_union_of_disjoint hdisjFilter,
      hfilterMap, Finset.card_map, hsingle]
    simp [relRankCount, x, Nat.add_comm]
  have hval : (ρ x).val = m.val + (if ρ (Fin.last n) < ρ x then 1 else 0) := by
    rw [hwhole, hdecomp, hcount]
  have hne : ρ (Fin.last n) ≠ ρ x := by
    intro h
    have : Fin.last n = x := ρ.injective h
    exact Fin.castSucc_ne_last (p m) this.symm
  have hneq : (ρ (Fin.last n)).val ≠ (ρ x).val := by
    intro h
    apply hne
    exact Fin.ext h
  rcases lt_or_gt_of_ne hneq with hlast | hkey
  · have hlastFin : ρ (Fin.last n) < ρ x := Fin.lt_def.mpr hlast
    have hjm : (ρ (Fin.last n)).val ≤ m.val := by
      rw [ite_eq_left hlastFin] at hval
      omega
    have hnot : ¬ m.val < (ρ (Fin.last n)).val := by omega
    rw [ite_eq_right hnot]
    rw [ite_eq_left hlastFin] at hval
    omega
  · have hkeyFin : ρ x < ρ (Fin.last n) := Fin.lt_def.mpr hkey
    have hlastNot : ¬ ρ (Fin.last n) < ρ x := not_lt_of_gt hkeyFin
    have hmj : m.val < (ρ (Fin.last n)).val := by
      rw [ite_eq_right hlastNot] at hval
      omega
    rw [ite_eq_left hmj]
    rw [ite_eq_right hlastNot] at hval
    omega

/-- The output permutation obtained by inserting the last input label at rank `j`
in an already sorted order `p` on the first `n` labels. -/
noncomputable def insertResultFun {n : ℕ} (p : Equiv.Perm (Fin n)) (j : ℕ)
    (hj : j ≤ n) : Fin (n + 1) → Fin (n + 1) := fun t =>
  if ht : (t : ℕ) < j then Fin.castSucc (p ⟨t, by omega⟩)
  else if ht2 : (t : ℕ) = j then Fin.last n
  else Fin.castSucc (p ⟨(t : ℕ) - 1, by omega⟩)

lemma insertResultFun_of_lt {n : ℕ} {p : Equiv.Perm (Fin n)} {j : ℕ} {hj : j ≤ n}
    {t : Fin (n + 1)} (ht : (t : ℕ) < j) :
    insertResultFun p j hj t = Fin.castSucc (p ⟨t, by omega⟩) := by
  simp [insertResultFun, ht]

lemma insertResultFun_of_eq {n : ℕ} {p : Equiv.Perm (Fin n)} {j : ℕ} {hj : j ≤ n}
    {t : Fin (n + 1)} (ht : (t : ℕ) = j) :
    insertResultFun p j hj t = Fin.last n := by
  simp [insertResultFun, ht]

lemma insertResultFun_of_gt {n : ℕ} {p : Equiv.Perm (Fin n)} {j : ℕ} {hj : j ≤ n}
    {t : Fin (n + 1)} (ht : j < (t : ℕ)) :
    insertResultFun p j hj t = Fin.castSucc (p ⟨(t : ℕ) - 1, by omega⟩) := by
  simp [insertResultFun, not_lt.mpr (Nat.le_of_lt ht), Nat.ne_of_gt ht]

lemma insertResultFun_injective {n : ℕ} (p : Equiv.Perm (Fin n)) (j : ℕ) (hj : j ≤ n) :
    Function.Injective (insertResultFun p j hj) := by
  intro a b hab
  rcases lt_trichotomy (a : ℕ) j with ha | ha | ha
  · rw [insertResultFun_of_lt ha] at hab
    rcases lt_trichotomy (b : ℕ) j with hb | hb | hb
    · rw [insertResultFun_of_lt hb] at hab
      have hv := congrArg Fin.val hab
      simp only [Fin.val_castSucc] at hv
      have hp : p ⟨a, by omega⟩ = p ⟨b, by omega⟩ := Fin.ext hv
      have hab' : (⟨a, by omega⟩ : Fin n) = ⟨b, by omega⟩ := p.injective hp
      exact Fin.ext (by simpa using congrArg Fin.val hab')
    · rw [insertResultFun_of_eq hb] at hab
      exact absurd hab (Fin.castSucc_ne_last _)
    · rw [insertResultFun_of_gt hb] at hab
      have hv := congrArg Fin.val hab
      simp only [Fin.val_castSucc] at hv
      have hp : p ⟨a, by omega⟩ = p ⟨(b : ℕ) - 1, by omega⟩ := Fin.ext hv
      have hab' : (⟨a, by omega⟩ : Fin n) = ⟨(b : ℕ) - 1, by omega⟩ := p.injective hp
      have hv' : (a : ℕ) = (b : ℕ) - 1 := by simpa using congrArg Fin.val hab'
      omega
  · rw [insertResultFun_of_eq ha] at hab
    rcases lt_trichotomy (b : ℕ) j with hb | hb | hb
    · rw [insertResultFun_of_lt hb] at hab
      exact absurd hab.symm (Fin.castSucc_ne_last _)
    · exact Fin.ext (by omega)
    · rw [insertResultFun_of_gt hb] at hab
      exact absurd hab.symm (Fin.castSucc_ne_last _)
  · rw [insertResultFun_of_gt ha] at hab
    rcases lt_trichotomy (b : ℕ) j with hb | hb | hb
    · rw [insertResultFun_of_lt hb] at hab
      have hv := congrArg Fin.val hab
      simp only [Fin.val_castSucc] at hv
      have hp : p ⟨(a : ℕ) - 1, by omega⟩ = p ⟨b, by omega⟩ := Fin.ext hv
      have hab' : (⟨(a : ℕ) - 1, by omega⟩ : Fin n) = ⟨b, by omega⟩ := p.injective hp
      have hv' : (a : ℕ) - 1 = (b : ℕ) := by simpa using congrArg Fin.val hab'
      omega
    · rw [insertResultFun_of_eq hb] at hab
      exact absurd hab (Fin.castSucc_ne_last _)
    · rw [insertResultFun_of_gt hb] at hab
      have hv := congrArg Fin.val hab
      simp only [Fin.val_castSucc] at hv
      have hp : p ⟨(a : ℕ) - 1, by omega⟩ = p ⟨(b : ℕ) - 1, by omega⟩ := Fin.ext hv
      have hab' : (⟨(a : ℕ) - 1, by omega⟩ : Fin n) = ⟨(b : ℕ) - 1, by omega⟩ := p.injective hp
      have hv' : (a : ℕ) - 1 = (b : ℕ) - 1 := by simpa using congrArg Fin.val hab'
      omega

/-- The inserted output permutation. -/
noncomputable def insertResult {n : ℕ} (p : Equiv.Perm (Fin n)) (j : ℕ) (hj : j ≤ n) :
    Equiv.Perm (Fin (n + 1)) :=
  Equiv.ofBijective (insertResultFun p j hj) (by
    rw [Fintype.bijective_iff_injective_and_card]
    exact ⟨insertResultFun_injective p j hj, by simp⟩)

@[simp] lemma insertResult_apply {n : ℕ} (p : Equiv.Perm (Fin n)) (j : ℕ) (hj : j ≤ n)
    (t : Fin (n + 1)) : insertResult p j hj t = insertResultFun p j hj t := rfl

lemma insertResult_irrel {n : ℕ} (p : Equiv.Perm (Fin n)) (j : ℕ)
    (h₁ h₂ : j ≤ n) : insertResult p j h₁ = insertResult p j h₂ := by
  apply Equiv.ext
  intro t
  simp [insertResult, insertResultFun]

lemma insertResult_rel_symm {n : ℕ} (ρ : Equiv.Perm (Fin (n + 1))) :
    insertResult (rel ρ).symm (ρ (Fin.last n)).val (by
      have h := (ρ (Fin.last n)).isLt
      omega) = ρ.symm := by
  let p : Equiv.Perm (Fin n) := (rel ρ).symm
  let j : ℕ := (ρ (Fin.last n)).val
  have hj : j ≤ n := by dsimp [j]; have h := (ρ (Fin.last n)).isLt; omega
  change insertResult p j hj = ρ.symm
  apply Equiv.ext
  intro t
  by_cases hlt : (t : ℕ) < j
  · rw [insertResult_apply, insertResultFun_of_lt hlt]
    apply ρ.injective
    rw [Equiv.apply_symm_apply]
    let m : Fin n := ⟨t.val, by omega⟩
    have hval := rel_symm_castSucc_val ρ m
    have hmt : m.val < (ρ (Fin.last n)).val := by dsimp [j, m]; exact hlt
    rw [ite_eq_left hmt] at hval
    apply Fin.ext
    simpa [p, m, j] using hval
  · by_cases heq : (t : ℕ) = j
    · rw [insertResult_apply, insertResultFun_of_eq heq]
      apply ρ.injective
      rw [Equiv.apply_symm_apply]
      apply Fin.ext
      simpa [j] using heq.symm
    · have hgt : j < (t : ℕ) := by omega
      rw [insertResult_apply, insertResultFun_of_gt hgt]
      apply ρ.injective
      rw [Equiv.apply_symm_apply]
      let m : Fin n := ⟨(t : ℕ) - 1, by omega⟩
      have hval := rel_symm_castSucc_val ρ m
      have hmj : ¬ m.val < (ρ (Fin.last n)).val := by dsimp [j, m]; omega
      rw [ite_eq_right hmj] at hval
      apply Fin.ext
      have ht : m.val + 1 = t.val := by dsimp [m]; omega
      rw [ht] at hval
      simpa [p, m] using hval

/-- Balanced binary search on the insertion-rank interval `[lo, hi]`. -/
noncomputable def bsTreeAux {n : ℕ} (p : Equiv.Perm (Fin n)) :
    (fuel lo hi : ℕ) → lo ≤ hi → hi ≤ n → hi - lo ≤ fuel → ComparisonTree (n + 1)
  | 0, lo, hi, hlo, hhi, hf =>
      .leaf (insertResult p lo (by omega))
  | fuel + 1, lo, hi, hlo, hhi, hf =>
      if h : lo < hi then
        .compare (Fin.castSucc (p ⟨(lo + hi) / 2, by omega⟩)) (Fin.last n)
          (bsTreeAux p fuel ((lo + hi) / 2 + 1) hi (by omega) hhi (by omega))
          (bsTreeAux p fuel lo ((lo + hi) / 2) (by omega) (by omega) (by omega))
      else
        .leaf (insertResult p lo (by omega))

/-- Balanced binary search over all `n + 1` possible insertion ranks. -/
noncomputable def bsTree {n : ℕ} (p : Equiv.Perm (Fin n)) : ComparisonTree (n + 1) :=
  bsTreeAux p n 0 n (by omega) le_rfl (by omega)

lemma clog_half (L : ℕ) (hL : 2 ≤ L) :
    Nat.clog 2 ((L + 1) / 2) + 1 ≤ Nat.clog 2 L := by
  let q := Nat.clog 2 L
  have hq : 1 ≤ q := Nat.clog_pos (by norm_num) (by omega)
  have hLpow : L ≤ 2 ^ q := Nat.le_pow_clog (by norm_num) L
  have hpow : 2 ^ q = 2 * 2 ^ (q - 1) := by
    rw [← Nat.pow_pred_mul (x := 2) (w := q) (by omega)]
    ring
  have hhalf : (L + 1) / 2 ≤ 2 ^ (q - 1) := by omega
  have hclog : Nat.clog 2 ((L + 1) / 2) ≤ q - 1 :=
    (Nat.clog_le_iff_le_pow (by norm_num : 1 < 2)).2 hhalf
  have hres : Nat.clog 2 ((L + 1) / 2) + 1 ≤ q := by omega
  simpa [q] using hres

lemma clog_mono {a b : ℕ} (h : a ≤ b) : Nat.clog 2 a ≤ Nat.clog 2 b := by
  apply (Nat.clog_le_iff_le_pow (by norm_num : 1 < 2)).2
  exact le_trans h (Nat.le_pow_clog (by norm_num : 1 < 2) b)

lemma bsTreeAux_height_le {n : ℕ} (p : Equiv.Perm (Fin n)) (fuel : ℕ) :
    ∀ (lo hi : ℕ) (hlo : lo ≤ hi) (hhi : hi ≤ n) (hf : hi - lo ≤ fuel),
      ComparisonTree.height (bsTreeAux p fuel lo hi hlo hhi hf) ≤
        Nat.clog 2 (hi - lo + 1) := by
  induction fuel with
  | zero =>
      intro lo hi hlo hhi hf
      have heq : lo = hi := by omega
      subst hi
      simp [bsTreeAux, ComparisonTree.height]
  | succ fuel ih =>
      intro lo hi hlo hhi hf
      simp only [bsTreeAux]
      by_cases h : lo < hi
      · rw [dite_eq_left h]
        simp only [ComparisonTree.height]
        let mid := (lo + hi) / 2
        have hmidlo : lo ≤ mid := by dsimp [mid]; omega
        have hmidhigh : mid < hi := by dsimp [mid]; omega
        have hL : 2 ≤ hi - lo + 1 := by omega
        have hright : hi - (mid + 1) + 1 ≤ (hi - lo + 1 + 1) / 2 := by
          dsimp [mid]
          omega
        have hleft : mid - lo + 1 ≤ (hi - lo + 1 + 1) / 2 := by
          dsimp [mid]
          omega
        have hrightIH := ih (mid + 1) hi (by omega) hhi (by omega)
        have hleftIH := ih lo mid (by omega) (by omega) (by omega)
        have hrightLog : Nat.clog 2 (hi - (mid + 1) + 1) ≤
            Nat.clog 2 ((hi - lo + 1 + 1) / 2) := clog_mono hright
        have hleftLog : Nat.clog 2 (mid - lo + 1) ≤
            Nat.clog 2 ((hi - lo + 1 + 1) / 2) := clog_mono hleft
        have hstep := clog_half (hi - lo + 1) hL
        have hrightBound :
            ComparisonTree.height
                (bsTreeAux p fuel ((lo + hi) / 2 + 1) hi (by omega) hhi (by omega)) ≤
              Nat.clog 2 ((hi - lo + 1 + 1) / 2) := by
          exact le_trans (by simpa [mid] using hrightIH) hrightLog
        have hleftBound :
            ComparisonTree.height
                (bsTreeAux p fuel lo ((lo + hi) / 2) (by omega) (by omega) (by omega)) ≤
              Nat.clog 2 ((hi - lo + 1 + 1) / 2) := by
          exact le_trans (by simpa [mid] using hleftIH) hleftLog
        omega
      · rw [dite_eq_right h]
        have heq : lo = hi := by omega
        subst hi
        simp [ComparisonTree.height]

lemma bsTreeAux_run {n : ℕ} (p : Equiv.Perm (Fin n))
    (ρ : Equiv.Perm (Fin (n + 1))) (j : ℕ) (hj : j ≤ n)
    (hcmp : ∀ m : Fin n,
      (ρ (Fin.castSucc (p m)) < ρ (Fin.last n) ↔ m.val < j)) :
    ∀ (fuel lo hi : ℕ) (hlo : lo ≤ hi) (hhi : hi ≤ n) (hf : hi - lo ≤ fuel)
      (_hlj : lo ≤ j) (_hjh : j ≤ hi),
      ComparisonTree.run ρ (bsTreeAux p fuel lo hi hlo hhi hf) = insertResult p j hj := by
  intro fuel
  induction fuel with
  | zero =>
      intro lo hi hlo hhi hf _hlj _hjh
      have heq : lo = hi := by omega
      have hloj : lo = j := by omega
      subst hi
      subst lo
      simp only [bsTreeAux, ComparisonTree.run]
  | succ fuel ih =>
      intro lo hi hlo hhi hf _hlj _hjh
      simp only [bsTreeAux]
      by_cases h : lo < hi
      · rw [dite_eq_left h]
        let mid := (lo + hi) / 2
        let m : Fin n := ⟨mid, by omega⟩
        have hmidlo : lo ≤ mid := by dsimp [mid]; omega
        have hmidhigh : mid < hi := by dsimp [mid]; omega
        have hcmpMid : (ρ (Fin.castSucc (p m)) < ρ (Fin.last n)) ↔ mid < j := by
          simpa [m] using hcmp m
        by_cases hmidj : mid < j
        · have hquery := hcmpMid.mpr hmidj
          rw [ComparisonTree.run, ite_eq_left hquery]
          apply ih (mid + 1) hi (by omega) hhi (by omega) (by omega) _hjh
        · have hquery : ¬ (ρ (Fin.castSucc (p m)) < ρ (Fin.last n)) :=
            fun hq => hmidj (hcmpMid.mp hq)
          rw [ComparisonTree.run, ite_eq_right hquery]
          apply ih lo mid (by omega) (by omega) (by omega) _hlj (by omega)
      · rw [dite_eq_right h]
        have heq : lo = hi := by omega
        have hloj : lo = j := by omega
        subst hi
        subst lo
        simp only [ComparisonTree.run]

lemma bsTree_run {n : ℕ} (ρ : Equiv.Perm (Fin (n + 1))) :
    ComparisonTree.run ρ (bsTree ((rel ρ).symm)) =
      insertResult ((rel ρ).symm) (ρ (Fin.last n)).val
        (by have h := (ρ (Fin.last n)).isLt; omega) := by
  let p : Equiv.Perm (Fin n) := (rel ρ).symm
  let j : ℕ := (ρ (Fin.last n)).val
  have hj : j ≤ n := by dsimp [j]; have h := (ρ (Fin.last n)).isLt; omega
  have hcmp : ∀ m : Fin n, (ρ (Fin.castSucc (p m)) < ρ (Fin.last n) ↔ m.val < j) := by
    intro m
    have hval := rel_symm_castSucc_val ρ m
    constructor
    · intro hlt
      have hlt' := Fin.lt_def.mp hlt
      rw [hval] at hlt'
      by_cases hmj : m.val < (ρ (Fin.last n)).val
      · simpa [j] using hmj
      · rw [ite_eq_right hmj] at hlt'
        dsimp [j]
        omega
    · intro hmj
      apply Fin.lt_def.mpr
      rw [hval]
      have hmj' : m.val < (ρ (Fin.last n)).val := by simpa [j] using hmj
      rw [ite_eq_left hmj']
      exact hmj'
  have hrun := bsTreeAux_run p ρ j hj hcmp n 0 n (by omega) le_rfl (by omega)
    (by omega) hj
  simpa [bsTree, p, j] using hrun

end ComparisonTree

open ComparisonTree

/-- Lift a sorting tree on the first `n` labels, replacing each leaf with the
binary search that inserts the last label into that leaf's output order. -/
noncomputable def insertTree {n : ℕ} : ComparisonTree n → ComparisonTree (n + 1)
  | .leaf σ => bsTree σ
  | .compare i j yes no =>
      .compare i.castSucc j.castSucc (insertTree yes) (insertTree no)

lemma insertTree_height_le {n : ℕ} (T : ComparisonTree n) :
    ComparisonTree.height (insertTree T) ≤
      ComparisonTree.height T + Nat.clog 2 (n + 1) := by
  induction T with
  | leaf σ =>
      have h := bsTreeAux_height_le σ n 0 n (by omega) le_rfl (by omega)
      simpa [insertTree, bsTree, ComparisonTree.height] using h
  | compare i j yes no ihyes ihno =>
      simp only [insertTree, ComparisonTree.height]
      omega

lemma insertTree_correct_of_run {n : ℕ} (T : ComparisonTree n) :
    ∀ (ρ : Equiv.Perm (Fin (n + 1))),
      ComparisonTree.run (rel ρ) T = (rel ρ).symm →
      ComparisonTree.run ρ (insertTree T) = ρ.symm := by
  induction T with
  | leaf σ =>
      intro ρ h
      have hσ : σ = (rel ρ).symm := h
      rw [insertTree, hσ]
      exact (bsTree_run ρ).trans (insertResult_rel_symm ρ)
  | compare i j yes no ihyes ihno =>
      intro ρ h
      simp only [insertTree, ComparisonTree.run]
      have hiff := rel_lt_iff ρ i j
      by_cases hc : rel ρ i < rel ρ j
      · have hchild : ComparisonTree.run (rel ρ) yes = (rel ρ).symm := by
          simpa [ComparisonTree.run, hc] using h
        rw [ite_eq_left (hiff.mp hc)]
        exact ihyes ρ hchild
      · have hchild : ComparisonTree.run (rel ρ) no = (rel ρ).symm := by
          simpa [ComparisonTree.run, hc] using h
        rw [ite_eq_right (fun h' => hc (hiff.mpr h'))]
        exact ihno ρ hchild

lemma insertTree_correct {n : ℕ} (T : ComparisonTree n)
    (hT : Correct T) : Correct (insertTree T) := by
  intro ρ
  exact insertTree_correct_of_run T ρ (hT (rel ρ))

/-- **One-sided Lipschitz bound:** inserting one new key costs at most a binary
search among the `n + 1` possible ranks. -/
theorem S_lipschitz (n : ℕ) :
    S (n + 1) ≤ S n + Nat.clog 2 (n + 1) := by
  obtain ⟨T, hT, hheight⟩ := exists_tree_S n
  let U := insertTree T
  have hU : Correct U := by
    dsimp [U]
    exact insertTree_correct T hT
  have hUheight : ComparisonTree.height U ≤
      ComparisonTree.height T + Nat.clog 2 (n + 1) := by
    dsimp [U]
    exact insertTree_height_le T
  apply (S_le_iff (n := n + 1)).2
  exact ⟨U, hU, le_trans hUheight (Nat.add_le_add_right hheight _)⟩

end SoringP1
