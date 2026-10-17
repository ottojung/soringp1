import SoringP1.Attainment

/-!
# The partial-order minimax: groundwork

Comparison pairs that split a set of rankings into two nonempty parts, and the
fact that such a pair always exists when the set has at least two elements.
This is the combinatorial core of the exact minimax evaluator.
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

end SoringP1
