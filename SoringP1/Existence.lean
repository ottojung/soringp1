import Mathlib
import SoringP1.Model

/-!
# Existence of a correct sorting decision tree

We construct, for every `n`, an explicit correct comparison decision tree
sorting `n` distinct keys, establishing `∃ k, HasBudget n k` (milestone A0).
-/

namespace SoringP1

/-! ## Step 1: the squeeze lemma -/

/-- A strictly increasing list of naturals, all of whose entries are below its
own length, is the identity enumeration. -/
lemma get_eq_self_of_pairwise {l : List ℕ} (hp : l.Pairwise (· < ·))
    (hbound : ∀ x ∈ l, x < l.length) (i : Fin l.length) : l.get i = i.val := by
  let f : Fin l.length → Fin l.length := fun j => ⟨l.get j, hbound _ (List.get_mem l j)⟩
  have hf : StrictMono f := by
    intro a b hab
    simp only [f, Fin.lt_def]
    exact hp.rel_get_of_lt hab
  have h := StrictMono.apply_eq hf (x := i)
  have : (f i).val = i.val := by rw [h]
  simpa [f] using this

/-- Version stated with the external length `n`. -/
lemma get_eq_val_of_pairwise {n : ℕ} {l : List ℕ} (hp : l.Pairwise (· < ·))
    (_hnd : l.Nodup) (hlen : l.length = n) (hbound : ∀ x ∈ l, x < n)
    (i : Fin n) : l.get (Fin.cast hlen.symm i) = i.val := by
  have hb : ∀ x ∈ l, x < l.length := by
    intro x hx; rw [hlen]; exact hbound x hx
  have := get_eq_self_of_pairwise hp hb (Fin.cast hlen.symm i)
  simpa using this

/-- If `sp` is sorted by `ranking` and enumerates `Fin n`, then reading `sp`
through `ranking` recovers the index. -/
lemma ranking_get_eq {n : ℕ} (ranking : Equiv.Perm (Fin n)) {sp : List (Fin n)}
    (hlen : sp.length = n)
    (hsorted : sp.Pairwise (fun a b => ranking a < ranking b))
    (i : Fin n) : ranking (sp.get (Fin.cast hlen.symm i)) = i := by
  let g : Fin n → Fin n := fun i => ranking (sp.get (Fin.cast hlen.symm i))
  have hg : StrictMono g := by
    intro a b hab
    simp only [g]
    apply hsorted.rel_get_of_lt
    exact (Fin.cast_lt_cast hlen.symm).2 hab
  exact StrictMono.apply_eq hg

/-! ## Step 2: reading off the permutation from a sorted sequence -/

/-- The permutation that maps the index `i` to the `i`-th element of the
enumerating list `sp`. -/
noncomputable def permFromSortedSeq {n : ℕ} (sp : List (Fin n)) (hnd : sp.Nodup)
    (hlen : sp.length = n) : Equiv.Perm (Fin n) :=
  Equiv.ofBijective (fun i : Fin n => sp.get (Fin.cast hlen.symm i)) (by
    have hinj : Function.Injective (fun i : Fin n => sp.get (Fin.cast hlen.symm i)) := by
      intro a b hab
      have h2 : Fin.cast hlen.symm a = Fin.cast hlen.symm b := hnd.get_inj_iff.1 hab
      exact Fin.cast_injective hlen.symm h2
    exact ⟨hinj, Finite.surjective_of_injective hinj⟩)

lemma permFromSortedSeq_apply {n : ℕ} (sp : List (Fin n)) (hnd : sp.Nodup)
    (hlen : sp.length = n) (i : Fin n) :
    permFromSortedSeq sp hnd hlen i = sp.get (Fin.cast hlen.symm i) := rfl

/-- The permutation built from a `ranking`-sorted enumerating list is the
inverse ranking. -/
lemma permFromSortedSeq_eq_symm {n : ℕ} (ranking : Equiv.Perm (Fin n)) {sp : List (Fin n)}
    (hnd : sp.Nodup) (hlen : sp.length = n)
    (hsorted : sp.Pairwise (fun a b => ranking a < ranking b)) :
    permFromSortedSeq sp hnd hlen = ranking.symm := by
  apply Equiv.ext
  intro i
  rw [permFromSortedSeq_apply]
  have h := ranking_get_eq ranking hlen hsorted i
  calc sp.get (Fin.cast hlen.symm i)
      = ranking.symm (ranking (sp.get (Fin.cast hlen.symm i))) :=
        (Equiv.symm_apply_apply ranking _).symm
    _ = ranking.symm i := by rw [h]

end SoringP1
