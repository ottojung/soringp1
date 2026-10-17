import SoringP1.Attainment

/-!
# The partial-order minimax evaluator

`S n` is an infimum over (infinitely many) trees. This file sets up the
partial-order minimax recurrence `adv` (the standard exact evaluator): the least
worst-case comparison count for sorting a set of rankings, computable by
recursion on the cardinality of that set.
-/

namespace SoringP1

open scoped Classical

/-- Comparison pairs `(i, j)`, `i ≠ j`, that split `S` into two nonempty parts. -/
def splitPairs {n : ℕ} (S : Finset (Equiv.Perm (Fin n))) : Finset (Fin n × Fin n) :=
  Finset.univ.filter (fun p =>
    p.1 ≠ p.2 ∧
    (S.filter (fun r => r p.1 < r p.2)).Nonempty ∧
    (S.filter (fun r => r p.2 < r p.1)).Nonempty)

lemma card_filter_lt {n : ℕ} (k : Fin n) :
    (Finset.univ.filter (fun v : Fin n => v < k)).card = k.val := by
  rw [show (Finset.univ.filter (fun v : Fin n => v < k)) = Finset.Iio k by
        ext v; simp [Finset.mem_Iio]]
  simp

lemma split_of_lt {n : ℕ} {S : Finset (Equiv.Perm (Fin n))}
    {r1 r2 : Equiv.Perm (Fin n)} (h1 : r1 ∈ S) (h2 : r2 ∈ S) {a : Fin n}
    (hlt : r1 a < r2 a) : (splitPairs S).Nonempty := by
  set A := Finset.univ.filter (fun c : Fin n => r1 c < r1 a) with hA
  set B := Finset.univ.filter (fun c : Fin n => r2 c < r2 a) with hB
  have hAcard : A.card = (r1 a).val := by
    rw [hA, show (Finset.univ.filter (fun c : Fin n => r1 c < r1 a)) =
        (Finset.Iio (r1 a)).image r1.symm by
      ext c
      simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_image, Finset.mem_Iio]
      constructor
      · intro hc; exact ⟨r1 c, hc, by simp⟩
      · rintro ⟨v, hv, rfl⟩; simpa using hv]
    rw [Finset.card_image_of_injective (Finset.Iio (r1 a)) r1.symm.injective]; simp
  have hBcard : B.card = (r2 a).val := by
    rw [hB, show (Finset.univ.filter (fun c : Fin n => r2 c < r2 a)) =
        (Finset.Iio (r2 a)).image r2.symm by
      ext c
      simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_image, Finset.mem_Iio]
      constructor
      · intro hc; exact ⟨r2 c, hc, by simp⟩
      · rintro ⟨v, hv, rfl⟩; simpa using hv]
    rw [Finset.card_image_of_injective (Finset.Iio (r2 a)) r2.symm.injective]; simp
  have hcard : A.card < B.card := by rw [hAcard, hBcard]; exact hlt
  obtain ⟨b, hbB, hbA⟩ := Finset.exists_mem_notMem_of_card_lt_card hcard
  have hbB' : r2 b < r2 a := (Finset.mem_filter.mp hbB).2
  have hbA' : ¬ r1 b < r1 a := fun hc => hbA (Finset.mem_filter.mpr ⟨Finset.mem_univ _, hc⟩)
  have hbne : b ≠ a := fun hc => by subst hc; exact absurd hbB' (lt_irrefl _)
  have hbgt : r1 a < r1 b := by
    rcases lt_trichotomy (r1 b) (r1 a) with h' | h' | h'
    · exact absurd h' hbA'
    · exact absurd (r1.injective h') hbne
    · exact h'
  refine ⟨(b, a), ?_⟩
  simp only [splitPairs, Finset.mem_filter, Finset.mem_univ, true_and]
  exact ⟨hbne, ⟨r2, Finset.mem_filter.mpr ⟨h2, hbB'⟩⟩,
    ⟨r1, Finset.mem_filter.mpr ⟨h1, hbgt⟩⟩⟩

/-- If `S` has at least two rankings, some comparison splits it. -/
lemma splitPairs_nonempty {n : ℕ} {S : Finset (Equiv.Perm (Fin n))} (h : 2 ≤ S.card) :
    (splitPairs S).Nonempty := by
  obtain ⟨r1, h1, r2, h2, hne⟩ := Finset.one_lt_card.mp (by omega : 1 < S.card)
  obtain ⟨a, ha⟩ : ∃ a, r1 a ≠ r2 a := by
    by_contra hc; simp only [not_exists, not_not] at hc; exact hne (Equiv.ext hc)
  rcases lt_or_gt_of_ne ha with hlt | hlt
  · exact split_of_lt h1 h2 hlt
  · exact split_of_lt h2 h1 hlt

lemma filter_card_lt {n : ℕ} {S : Finset (Equiv.Perm (Fin n))}
    {q : Equiv.Perm (Fin n) → Prop} [DecidablePred q] {r : Equiv.Perm (Fin n)}
    (hrS : r ∈ S) (hrq : ¬ q r) : (S.filter q).card < S.card :=
  Finset.card_lt_card (Finset.filter_ssubset.mpr ⟨r, hrS, hrq⟩)

/-- The partial-order minimax value for a set of rankings. -/
noncomputable def adv {n : ℕ} (S : Finset (Equiv.Perm (Fin n))) : ℕ :=
  if h : S.card ≤ 1 then 0
  else
    1 + ((splitPairs S).attach.image (fun pp =>
          max (adv (S.filter (fun r => r pp.1.1 < r pp.1.2)))
              (adv (S.filter (fun r => r pp.1.2 < r pp.1.1))))).min'
        (by
          rw [Finset.image_nonempty, Finset.attach_nonempty_iff]
          exact splitPairs_nonempty (by omega : 2 ≤ S.card))
termination_by S.card
decreasing_by
  · have hpred := pp.property
    unfold splitPairs at hpred
    rw [Finset.mem_filter] at hpred
    obtain ⟨r, hr⟩ := hpred.2.2.2
    exact filter_card_lt (Finset.mem_filter.mp hr).1
      (fun hq => absurd (Finset.mem_filter.mp hr).2 (not_lt.mpr (le_of_lt hq)))
  · have hpred := pp.property
    unfold splitPairs at hpred
    rw [Finset.mem_filter] at hpred
    obtain ⟨r, hr⟩ := hpred.2.2.1
    exact filter_card_lt (Finset.mem_filter.mp hr).1
      (fun hq => absurd (Finset.mem_filter.mp hr).2 (not_lt.mpr (le_of_lt hq)))

/-- `T` sorts every ranking in `S`. -/
def Sorts {n : ℕ} (S : Finset (Equiv.Perm (Fin n))) (T : ComparisonTree n) : Prop :=
  ∀ r ∈ S, ComparisonTree.run r T = r.symm

/-- Adversary lower bound: any tree sorting `S` has height at least `adv S`. -/
theorem adv_le_height {n : ℕ} (S : Finset (Equiv.Perm (Fin n))) (T : ComparisonTree n)
    (hT : Sorts S T) : adv S ≤ ComparisonTree.height T := by
  induction T generalizing S with
  | leaf π =>
      have hcard : S.card ≤ 1 := by
        rw [Finset.card_le_one]
        intro r1 h1 r2 h2
        have h : r1.symm = r2.symm := (hT r1 h1) ▸ (hT r2 h2)
        have h2' := congrArg Equiv.symm h
        rwa [Equiv.symm_symm r1, Equiv.symm_symm r2] at h2'
      rw [adv, dite_eq_left hcard]
      simp [ComparisonTree.height]
  | compare i j yes no ihyes ihno =>
      by_cases hcard : S.card ≤ 1
      · rw [adv, dite_eq_left hcard]; simp [ComparisonTree.height]
      · rcases eq_or_ne i j with hij | hne
        · subst hij
          refine le_trans (ihno S ?_) (le_trans (le_max_right _ _) (Nat.le_add_left _ _))
          intro r hr
          simpa [ComparisonTree.run] using hT r hr
        · rcases Finset.eq_empty_or_nonempty (S.filter (fun r => r j < r i)) with hno | hno
          · refine le_trans (ihyes S ?_) (le_trans (le_max_left _ _) (Nat.le_add_left _ _))
            intro r hr
            have h := hT r hr
            have hrj : ¬ (r j < r i) := fun hc => by
              have hm : r ∈ S.filter (fun r => r j < r i) := Finset.mem_filter.mpr ⟨hr, hc⟩
              rw [hno] at hm; exact Finset.notMem_empty r hm
            have hlt : r i < r j := lt_of_le_of_ne (not_lt.mp hrj) (fun he => hne (r.injective he))
            simpa [ComparisonTree.run, hlt] using h
          · rcases Finset.eq_empty_or_nonempty (S.filter (fun r => r i < r j)) with hy | hy
            · refine le_trans (ihno S ?_) (le_trans (le_max_right _ _) (Nat.le_add_left _ _))
              intro r hr
              have h := hT r hr
              have hri : ¬ (r i < r j) := fun hc => by
                have hm : r ∈ S.filter (fun r => r i < r j) := Finset.mem_filter.mpr ⟨hr, hc⟩
                rw [hy] at hm; exact Finset.notMem_empty r hm
              have hlt : r j < r i := lt_of_le_of_ne (not_lt.mp hri) (fun he => (Ne.symm hne) (r.injective he))
              simpa [ComparisonTree.run, not_lt.mpr (le_of_lt hlt)] using h
            · rw [adv, dite_eq_right hcard]
              set m := ((splitPairs S).attach.image (fun pp =>
                    max (adv (S.filter (fun r => r pp.1.1 < r pp.1.2)))
                        (adv (S.filter (fun r => r pp.1.2 < r pp.1.1))))).min' _ with hm
              have hsplit : (i, j) ∈ splitPairs S := by
                simp only [splitPairs, Finset.mem_filter, Finset.mem_univ, true_and]
                exact ⟨hne, hy, hno⟩
              have hmem : max (adv (S.filter (fun r => r i < r j)))
                    (adv (S.filter (fun r => r j < r i)))
                  ∈ (splitPairs S).attach.image (fun pp =>
                    max (adv (S.filter (fun r => r pp.1.1 < r pp.1.2)))
                        (adv (S.filter (fun r => r pp.1.2 < r pp.1.1)))) := by
                refine Finset.mem_image.mpr ⟨⟨(i, j), hsplit⟩, Finset.mem_attach _ _, ?_⟩
                rfl
              have hmin : m ≤ max (adv (S.filter (fun r => r i < r j)))
                                  (adv (S.filter (fun r => r j < r i))) := by
                rw [hm]; exact Finset.min'_le _ _ hmem
              have h1 := ihyes (S.filter (fun r => r i < r j)) (fun r hr => by
                have h := hT r (Finset.mem_filter.mp hr).1
                rw [ComparisonTree.run, ite_eq_left (Finset.mem_filter.mp hr).2] at h
                exact h)
              have h2 := ihno (S.filter (fun r => r j < r i)) (fun r hr => by
                have h := hT r (Finset.mem_filter.mp hr).1
                rw [ComparisonTree.run,
                  ite_eq_right (not_lt.mpr (le_of_lt (Finset.mem_filter.mp hr).2))] at h
                exact h)
              have hmax : max (adv (S.filter (fun r => r i < r j)))
                    (adv (S.filter (fun r => r j < r i)))
                  ≤ max (ComparisonTree.height yes) (ComparisonTree.height no) :=
                max_le (le_trans h1 (le_max_left _ _)) (le_trans h2 (le_max_right _ _))
              calc 1 + m ≤ 1 + max (adv (S.filter (fun r => r i < r j)))
                                    (adv (S.filter (fun r => r j < r i))) :=
                    Nat.add_le_add_left hmin 1
                _ ≤ 1 + max (ComparisonTree.height yes) (ComparisonTree.height no) :=
                    Nat.add_le_add_left hmax 1
                _ = ComparisonTree.height (ComparisonTree.compare i j yes no) := rfl

/-- The adversary bound for a correct tree. -/
theorem adv_le_height_correct {n : ℕ} (T : ComparisonTree n) (h : Correct T) :
    adv (Finset.univ : Finset (Equiv.Perm (Fin n))) ≤ ComparisonTree.height T :=
  adv_le_height _ T (fun r _ => h r)

/-- A comparison pair achieving the minimax value at `S`. -/
noncomputable def bestPair {n : ℕ} (S : Finset (Equiv.Perm (Fin n)))
    (hne : (splitPairs S).Nonempty) : {p : Fin n × Fin n // p ∈ splitPairs S} :=
  ⟨Classical.choose (Finset.exists_min_image (splitPairs S)
      (fun p => max (adv (S.filter (fun r => r p.1 < r p.2)))
                    (adv (S.filter (fun r => r p.2 < r p.1)))) hne),
   (Classical.choose_spec (Finset.exists_min_image (splitPairs S)
      (fun p => max (adv (S.filter (fun r => r p.1 < r p.2)))
                    (adv (S.filter (fun r => r p.2 < r p.1)))) hne)).1⟩

lemma bestPair_le {n : ℕ} {S : Finset (Equiv.Perm (Fin n))} {hne} {p : Fin n × Fin n}
    (hp : p ∈ splitPairs S) :
    max (adv (S.filter (fun r => r (bestPair S hne).1.1 < r (bestPair S hne).1.2)))
        (adv (S.filter (fun r => r (bestPair S hne).1.2 < r (bestPair S hne).1.1)))
    ≤ max (adv (S.filter (fun r => r p.1 < r p.2))) (adv (S.filter (fun r => r p.2 < r p.1))) :=
  (Classical.choose_spec (Finset.exists_min_image (splitPairs S)
    (fun p => max (adv (S.filter (fun r => r p.1 < r p.2)))
                  (adv (S.filter (fun r => r p.2 < r p.1)))) hne)).2 p hp

/-- The minimax sorting tree for a set of rankings: compare an optimal pair, recurse. -/
noncomputable def minimaxTree {n : ℕ} (S : Finset (Equiv.Perm (Fin n))) : ComparisonTree n :=
  if h : S.card ≤ 1 then
    .leaf (if hne : S.Nonempty then (Classical.choose hne).symm else 1)
  else
    let p := (bestPair S (splitPairs_nonempty (by omega))).1
    .compare p.1 p.2 (minimaxTree (S.filter (fun r => r p.1 < r p.2)))
                      (minimaxTree (S.filter (fun r => r p.2 < r p.1)))
termination_by S.card
decreasing_by
  · have hp := (bestPair S (splitPairs_nonempty (by omega))).2
    unfold splitPairs at hp
    rw [Finset.mem_filter] at hp
    obtain ⟨r, hr⟩ := hp.2.2.2
    exact filter_card_lt (Finset.mem_filter.mp hr).1
      (fun hq => absurd (Finset.mem_filter.mp hr).2 (not_lt.mpr (le_of_lt hq)))
  · have hp := (bestPair S (splitPairs_nonempty (by omega))).2
    unfold splitPairs at hp
    rw [Finset.mem_filter] at hp
    obtain ⟨r, hr⟩ := hp.2.2.1
    exact filter_card_lt (Finset.mem_filter.mp hr).1
      (fun hq => absurd (Finset.mem_filter.mp hr).2 (not_lt.mpr (le_of_lt hq)))

/-- The adversary lower bound in infimum form: `adv univ ≤ S n`. -/
theorem adv_univ_le_S (n : ℕ) :
    adv (Finset.univ : Finset (Equiv.Perm (Fin n))) ≤ S n := by
  rw [S]
  apply le_csInf
  · exact ⟨_, sortTree n, sortTree_correct n, le_refl _⟩
  · rintro k ⟨T, hcorr, hheight⟩
    exact le_trans (adv_le_height_correct T hcorr) hheight

/-- `minimaxTree S` sorts every ranking in `S`. -/
theorem minimaxTree_sorts {n : ℕ} (S : Finset (Equiv.Perm (Fin n))) :
    Sorts S (minimaxTree S) := by
  induction S using Finset.strongInductionOn with
  | _ S ih =>
  rw [minimaxTree]
  by_cases h : S.card ≤ 1
  · rw [dite_eq_left h]
    by_cases hS : S.Nonempty
    · rw [dite_eq_left hS]
      intro r hr
      rw [ComparisonTree.run,
        Finset.card_le_one.mp h r hr (Classical.choose hS) (Classical.choose_spec hS)]
    · rw [dite_eq_right hS]
      have hempty : S = ∅ := Finset.not_nonempty_iff_eq_empty.mp hS
      intro r hr
      rw [hempty] at hr
      exact (Finset.notMem_empty r hr).elim
  · rw [dite_eq_right h]
    set bp := bestPair S (splitPairs_nonempty (by omega)) with hbp
    have hpmem : bp.1 ∈ splitPairs S := bp.2
    have hpne : bp.1.1 ≠ bp.1.2 := by
      have := hpmem; unfold splitPairs at this; rw [Finset.mem_filter] at this; exact this.2.1
    have hnne : (S.filter (fun r => r bp.1.2 < r bp.1.1)).Nonempty := by
      have := hpmem; unfold splitPairs at this; rw [Finset.mem_filter] at this; exact this.2.2.2
    have hyne : (S.filter (fun r => r bp.1.1 < r bp.1.2)).Nonempty := by
      have := hpmem; unfold splitPairs at this; rw [Finset.mem_filter] at this; exact this.2.2.1
    have hssub1 : S.filter (fun r => r bp.1.1 < r bp.1.2) ⊂ S :=
      Finset.filter_ssubset.mpr (let ⟨r, hr⟩ := hnne
        ⟨r, (Finset.mem_filter.mp hr).1,
          fun hq => absurd (Finset.mem_filter.mp hr).2 (not_lt.mpr (le_of_lt hq))⟩)
    have hssub2 : S.filter (fun r => r bp.1.2 < r bp.1.1) ⊂ S :=
      Finset.filter_ssubset.mpr (let ⟨r, hr⟩ := hyne
        ⟨r, (Finset.mem_filter.mp hr).1,
          fun hq => absurd (Finset.mem_filter.mp hr).2 (not_lt.mpr (le_of_lt hq))⟩)
    intro r hr
    rcases lt_or_gt_of_ne (fun he => hpne (r.injective he)) with hlt | hlt
    · rw [ComparisonTree.run, ite_eq_left hlt]
      exact ih _ hssub1 r (Finset.mem_filter.mpr ⟨hr, hlt⟩)
    · rw [ComparisonTree.run, ite_eq_right (not_lt.mpr (le_of_lt hlt))]
      exact ih _ hssub2 r (Finset.mem_filter.mpr ⟨hr, hlt⟩)

end SoringP1
