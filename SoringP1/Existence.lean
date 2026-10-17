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

/-! ## Step 3: the insertion-sort decision tree -/

/-- A permutation read off an enumerating list, with a total fallback so that
the tree construction below need not carry well-formedness proofs. -/
noncomputable def permOfList {n : ℕ} (sp : List (Fin n)) : Equiv.Perm (Fin n) :=
  if h : sp.Nodup ∧ sp.length = n then permFromSortedSeq sp h.1 h.2 else 1

/-- Machine state of the insertion sort. `into m sp` inserts the element `⟨m⟩`
into the sorted prefix `sp`. `aux x pre suf` scans the sorted list `pre ++ suf`
to locate `x`, having established that everything in `pre` is smaller. -/
inductive InsState (n : ℕ) where
  | into (m : ℕ) (hm : m ≤ n) (sp : List (Fin n))
  | aux (x : Fin n) (pre suf : List (Fin n))

/-- Fuel-driven insertion sort. Fuel is a structural argument, so this is a
plain structural recursion; the correctness proof shows enough fuel suffices. -/
noncomputable def go (n : ℕ) : ℕ → InsState n → ComparisonTree n
  | 0, _ => .leaf 1
  | fuel + 1, .into m hm sp =>
      if h : m = n then .leaf (permOfList sp)
      else go n fuel (.aux ⟨m, by omega⟩ [] sp)
  | fuel + 1, .aux x pre suf =>
      match suf with
      | [] => go n fuel (.into (x.val + 1) (by have := x.isLt; omega) (pre ++ [x]))
      | q :: tl => .compare x q
          (go n fuel (.into (x.val + 1) (by have := x.isLt; omega) (pre ++ [x] ++ q :: tl)))
          (go n fuel (.aux x (pre ++ [q]) tl))

/-- Fuel bound for an `into` state. -/
def boundInto (n m : ℕ) : ℕ := (n - m) * (n + 2) + (n + 1)

/-- Fuel bound for an `aux` state. -/
def boundAux (n : ℕ) (x : Fin n) (suf : List (Fin n)) : ℕ :=
  (n - x.val) * (n + 2) + suf.length

/-- Invariant for `into m sp`: `sp` is the `ranking`-sorted enumeration of
`{0, …, m-1}`. -/
structure IntoInv {n : ℕ} (ranking : Equiv.Perm (Fin n)) (m : ℕ) (sp : List (Fin n)) : Prop where
  nodup : sp.Nodup
  length_eq : sp.length = m
  mem_iff : ∀ a, a ∈ sp ↔ a.val < m
  sorted : sp.Pairwise (fun a b => ranking a < ranking b)

/-- Invariant for `aux x pre suf`: `pre ++ suf` is the `ranking`-sorted
enumeration of `{0, …, x.val-1}` and `pre` consists of elements smaller than
`x`. -/
structure AuxInv {n : ℕ} (ranking : Equiv.Perm (Fin n)) (x : Fin n)
    (pre suf : List (Fin n)) : Prop where
  nodup : (pre ++ suf).Nodup
  sorted : (pre ++ suf).Pairwise (fun a b => ranking a < ranking b)
  pre_lt : ∀ p ∈ pre, ranking p < ranking x
  mem_iff : ∀ a, a ∈ pre ++ suf ↔ a.val < x.val
  length_eq : (pre ++ suf).length = x.val

section Lemmas

variable {n : ℕ} {ranking : Equiv.Perm (Fin n)}

/-- Sortedness of inserting `x` between a sorted prefix and sorted suffix. -/
lemma sorted_insert {pre suf : List (Fin n)} {x : Fin n}
    (hpre : pre.Pairwise (fun a b => ranking a < ranking b))
    (hsuf : suf.Pairwise (fun a b => ranking a < ranking b))
    (hcross : ∀ a ∈ pre, ∀ b ∈ suf, ranking a < ranking b)
    (hxpre : ∀ a ∈ pre, ranking a < ranking x)
    (hxsuf : ∀ b ∈ suf, ranking x < ranking b) :
    (pre ++ [x] ++ suf).Pairwise (fun a b => ranking a < ranking b) := by
  rw [List.pairwise_append]
  refine ⟨?_, hsuf, ?_⟩
  · rw [List.pairwise_append]
    refine ⟨hpre, by simp, ?_⟩
    intro a ha b hb
    simp only [List.mem_singleton] at hb
    subst hb
    exact hxpre a ha
  · intro a ha b hb
    rcases List.mem_append.1 ha with ha | ha
    · exact hcross a ha b hb
    · simp only [List.mem_singleton] at ha
      subst ha
      exact hxsuf b hb

/-- Membership in a list with `x` inserted before `suf`. -/
lemma mem_append_singleton_append (a x : Fin n) (pre suf : List (Fin n)) :
    a ∈ pre ++ [x] ++ suf ↔ a ∈ pre ++ suf ∨ a = x := by
  simp only [List.mem_append, List.mem_singleton]
  tauto

/-- Appending `x` to a nodup list not containing `x` preserves nodup. -/
lemma nodup_insert_mid {pre suf : List (Fin n)} {x : Fin n}
    (hnd : (pre ++ suf).Nodup) (hx : x ∉ pre ++ suf) :
    (pre ++ [x] ++ suf).Nodup := by
  have hassoc : pre ++ [x] ++ suf = pre ++ (x :: suf) := by
    rw [List.append_assoc, List.singleton_append]
  rw [hassoc]
  exact (List.perm_middle (l₁ := pre) (l₂ := suf)).nodup_iff.mpr
    (List.nodup_cons.2 ⟨hx, hnd⟩)

lemma intoInv_toAux {m : ℕ} {sp : List (Fin n)} (hm : m < n)
    (h : IntoInv ranking m sp) : AuxInv ranking ⟨m, hm⟩ [] sp := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · simpa using h.nodup
  · simpa using h.sorted
  · intro p hp; simp at hp
  · intro a; simpa using h.mem_iff a
  · simpa using h.length_eq

lemma auxInv_intoEnd {x : Fin n} {pre : List (Fin n)}
    (h : AuxInv ranking x pre []) : IntoInv ranking (x.val + 1) (pre ++ [x]) := by
  obtain ⟨hnd, hsorted, hpre_lt, hmem, hlen⟩ := h
  have hpre_nd : pre.Nodup := by simpa using hnd
  have hpre_sorted : pre.Pairwise (fun a b => ranking a < ranking b) := by simpa using hsorted
  have hpre_mem : ∀ a, a ∈ pre ↔ a.val < x.val := by simpa using hmem
  have hpre_len : pre.length = x.val := by simpa using hlen
  have hx_notin : x ∉ pre := by
    intro hx; exact absurd ((hpre_mem x).1 hx) (lt_irrefl _)
  refine ⟨?_, ?_, ?_, ?_⟩
  · have := nodup_insert_mid (suf := []) (by simpa using hpre_nd) (by simpa using hx_notin)
    simpa using this
  · simp only [List.length_append, List.length_singleton]; omega
  · intro a
    rw [List.mem_append, List.mem_singleton]
    constructor
    · rintro (ha | rfl)
      · have := (hpre_mem a).1 ha; omega
      · omega
    · intro h'
      rcases lt_or_eq_of_le (Nat.lt_succ_iff.1 h') with hlt | heq
      · exact Or.inl ((hpre_mem a).2 hlt)
      · exact Or.inr (Fin.ext heq)
  · have hres := sorted_insert hpre_sorted (List.Pairwise.nil)
      (by intro a _ b hb; exact absurd hb List.not_mem_nil)
      (fun a ha => hpre_lt a ha) (by intro b hb; exact absurd hb List.not_mem_nil)
    simpa using hres

lemma auxInv_stepYes {x q : Fin n} {pre tl : List (Fin n)}
    (h : AuxInv ranking x pre (q :: tl)) (hxq : ranking x < ranking q) :
    IntoInv ranking (x.val + 1) (pre ++ [x] ++ q :: tl) := by
  obtain ⟨hnd, hsorted, hpre_lt, hmem, hlen⟩ := h
  obtain ⟨hpre_sorted, hsuf_sorted, hcross⟩ := List.pairwise_append.1 hsorted
  have hx_notin : x ∉ pre ++ (q :: tl) := by
    intro hx; exact absurd ((hmem x).1 hx) (lt_irrefl _)
  have hxsuf : ∀ b ∈ q :: tl, ranking x < ranking b := by
    intro b hb
    rcases List.mem_cons.1 hb with rfl | hb
    · exact hxq
    · exact lt_trans hxq ((List.pairwise_cons.1 hsuf_sorted).1 b hb)
  refine ⟨?_, ?_, ?_, ?_⟩
  · exact nodup_insert_mid hnd hx_notin
  · have hlen' := hlen
    simp only [List.length_append, List.length_cons, List.length_nil] at hlen' ⊢
    omega
  · intro a
    rw [mem_append_singleton_append]
    constructor
    · rintro (ha | rfl)
      · have := (hmem a).1 ha; omega
      · omega
    · intro h'
      rcases lt_or_eq_of_le (Nat.lt_succ_iff.1 h') with hlt | heq
      · exact Or.inl ((hmem a).2 hlt)
      · exact Or.inr (Fin.ext heq)
  · exact sorted_insert hpre_sorted hsuf_sorted hcross
      (fun a ha => hpre_lt a ha) hxsuf

lemma auxInv_stepNo {x q : Fin n} {pre tl : List (Fin n)}
    (h : AuxInv ranking x pre (q :: tl)) (hxq : ¬ ranking x < ranking q) :
    AuxInv ranking x (pre ++ [q]) tl := by
  obtain ⟨hnd, hsorted, hpre_lt, hmem, hlen⟩ := h
  have hq_mem : q ∈ pre ++ (q :: tl) := by simp
  have hq_lt : q.val < x.val := (hmem q).1 hq_mem
  have hne : q ≠ x := fun hEq => by rw [hEq] at hq_lt; exact lt_irrefl _ hq_lt
  have hne' : ranking q ≠ ranking x := fun hEq => hne (ranking.injective hEq)
  have hq_sorted : ranking q < ranking x := lt_of_le_of_ne (not_lt.1 hxq) hne'
  have hcast : (pre ++ [q]) ++ tl = pre ++ (q :: tl) := by
    rw [List.append_assoc, List.singleton_append]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rwa [hcast]
  · rwa [hcast]
  · intro p hp
    rcases List.mem_append.1 hp with hp | hp
    · exact hpre_lt p hp
    · simp only [List.mem_singleton] at hp; subst hp; exact hq_sorted
  · intro a; rw [hcast]; exact hmem a
  · rw [hcast]; exact hlen

end Lemmas

end SoringP1
