# Symmetry quotients of the exact minimax state space: duality and move orbits

**Status:** research note (2026-10-18). This is a **nonoverlapping** companion to
the state-compression draft (which studies relabelling quotients, linear-extension
coarsening and balanced-greedy trees). Everything here is a **definition**,
**literature result**, **deduction**, **experiment**, or **conjecture**, as
labelled inline. No Lean file and no complexity-class separation is claimed.
Companion program: `scripts/benchmark_symmetry_quotients.py`; tests:
`tests/test_symmetry_quotients.py`. The program reproduces every number below.

## Precise question

`docs/problem.md` fixes `S(n)` as the minimum worst-case number of adaptive
pairwise comparisons needed to sort `n` distinct labelled keys, and
`docs/upper-bound.md` / `SoringP1/Minimax.lean` (A24) identify it with the
partial-order minimax value `F(∅)`. This note asks:

> Besides key relabelling, which symmetries of the comparison problem give
> **exact** (optimum-preserving) state or move quotients? When is a quotient a
> legitimate **DP state**, as opposed to merely a value that happens to be
> class-invariant? How much do the automorphism orbits of moves shrink the
> transition set?

The new contributions are the **order-duality** quotient (Theorem 3), the
**states-versus-moves** distinction (Section 4), the **Aut(P) move-orbit**
reduction (Theorem 5), and several concrete falsifications (Section 6),
including that the comparability graph does not determine `F` (`n=7`).

## Model and notation

A state is a strict partial order `P` on the labelled keys `[n]`, stored as
successor bitmasks. `extend(P, x, y)` is the transitive closure after adding
`x < y`. Write `x ‖ y` when `x, y` are incomparable, and

    F(P) = 0                                                      if P is total,
    F(P) = 1 + min_{x ‖ y} max( F(P+x<y), F(P+y<x) )              otherwise,

with `S(n) = F(∅)`. This is exactly `adv univ` (A24). Reachable states are the
labelled posets on `[n]`, counted by OEIS A001035; isomorphism classes by
A000112. The state count is `2^{Θ(n²)}` in the numeric parameter `n`; nothing
below changes that exponent. **No P/NP claim is made.**

## 1. Poset sufficiency (deduction)

**Lemma 1.** The remaining minimax cost depends only on the transitive closure
`P` of the comparisons made so far, not on their order or history.

*Proof.* A history is consistent, so its outcomes are exactly the relations of
some poset `P`; the inputs still possible are the linear extensions `Ext(P)`.
The remaining problem — finish sorting an input known to lie in `Ext(P)` — is a
function of the set `Ext(P)` alone. Conversely `P` is recovered from `Ext(P)`
as the intersection of those linear orders, so `P ↦ Ext(P)` is injective and `P`
is a sufficient statistic. ∎

**Reachability (deduction).** Every labelled poset is reachable: starting from
`∅`, repeatedly add any relation `x<y` of `P` not yet in the current closure.
The current closure is always a subset of `P` (a transitive superset-closed set),
so if `x<y ∈ P` is missing then `y<x` is missing too (`P` is antisymmetric);
hence `x ‖ y` in the current state and the comparison is legal. Repeating until
the closure equals `P` reaches `P`. Hence the reachable state space is exactly
the set of labelled posets, `A001035(n)` — not the naive `2^{n!}` subsets of
permutations.

This is the baseline compression already built into any partial-order DP; it is
independently derived in the staging draft (Finding 1) and measured there. It is
recorded here only to fix the object on which the quotient acts.

## 2. Relabelling invariance (deduction)

Let `S_n` act by `(πP): π(x) <' π(y) ⟺ x < y`.

**Lemma 2.** `F(πP) = F(P)`, and `extend` is `S_n`-equivariant:
`π·extend(P, x, y) = extend(πP, πx, πy)`.

*Proof.* `π` is an isomorphism of the comparison model (`Ext(πP) = π·Ext(P)`),
so decision trees and their heights correspond. Equivalently, induction on the
number of relations using equivariance of `extend`. ∎

Thus `F` descends to isomorphism classes; the class count is `A000112(n)`. This
is the quotient studied in the staging draft (its Finding 2), so we do not
re-derive its measured gains here.

## 3. Order-dual invariance (deduction — new)

Let `P^op` be the order dual: `x <^op y ⟺ y < x`.

**Theorem 3.** `F(P^op) = F(P)` for every finite poset `P`.

*Proof.* Strong induction on the **number of incomparable pairs**
`c(P) = binom(n,2) - r(P)`, where `r(P)` counts comparable unordered pairs.
If `P` is total then so is `P^op` and both values are `0`. Otherwise fix an
incomparable pair `{x, y}`. Incomparability is self-dual, so `P` and `P^op`
have the same incomparable pairs. Since `(P + x<y)^op = P^op + y<x` and adding a
relation strictly **decreases** `c`, the induction hypothesis applies and gives

    F(P + x<y) = F(P^op + y<x),      F(P + y<x) = F(P^op + x<y).

Hence `max(F(P+x<y), F(P+y<x)) = max(F(P^op+x<y), F(P^op+y<x))` for every pair,
and the minima over the common pair set coincide; the recurrence yields
`F(P^op) = F(P)`. ∎

**Remark 4 (group structure).** Dualisation `δ(P) = P^op` is an involution and
commutes with relabelling (`δπ = πδ`), so `S_n` and `δ` generate
`S_n × Z_2`. Quotienting by the full group is therefore exact. Measured class
counts (up to relabelling and duality) are

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| A000112(n) (iso) | 1 | 1 | 2 | 5 | 16 | 63 | 318 |
| up to iso+dual | 1 | 1 | 2 | 4 | 12 | 39 | 184 |

so duality removes roughly a factor of two (a constant factor, not asymptotic).
This is the duality analogue of the relabelling factor.

## 4. Quotienting states versus quotienting moves (new)

A quotient can be sound at two logically different levels.

**Definition (sound state quotient).** An equivalence `~` on states is a *sound
DP quotient* when (i) `F` is constant on classes and (ii) the **multiset of
unordered successor-class PAIRS**, one pair per unordered incomparable move,
is well defined on classes. In symbols, whenever `P ~ Q`, the multiset

    {{ [P+x<y], [P+y<x] } : {x,y} incomparable in P}

of unordered *two-element multisets* of classes must equal the analogous
multiset for `Q`. Flattening all successor classes into one multiset is
insufficient: minimax takes a `max` **inside each move** and then a `min`
**between moves**, and flattening loses that grouping.

Condition (ii) supports the recursive minimax transition on the quotient;
(i) alone only says that the value happens to be class-invariant. Relabelling and duality satisfy
both: `π` and `δ` are automorphisms of the move graph (bijections on states
commuting with `extend`). The comparability-graph collapse satisfies (i)
empirically but **fails (ii)** (Section 6c); it is therefore a value collapse,
not a usable DP state.

**Theorem 5 (move-orbit reduction).** Let `Aut(P)` be the automorphism group of
`P`, acting on keys. For an unordered incomparable pair `{x, y}` put
`T({x,y}) = max(F(P+x<y), F(P+y<x))`. If `{x',y'} = {φx, φy}` for some
`φ ∈ Aut(P)`, then `T({x,y}) = T({x',y'})`.

*Proof.* `φ` is an isomorphism `P → P`, so it extends to an isomorphism
`P + x<y → P + φx<φy`; hence `F(P+x<y) = F(P+φx<φy)` and likewise with the
orientations swapped. The two maxima agree. ∎

Consequently the inner `min` may range over **one representative per
`Aut(P)`-orbit** of unordered incomparable pairs, with no change to `F`. Two
further facts sharpen the picture:

* The orbit partition **refines** the successor-class partition: equal orbits
  give equal successor classes, but distinct orbits may still give isomorphic
  successors, so orbit reduction is sound but possibly conservative. Example
  (`n=3`, `P = {1<2}` with `0` isolated): the four ordered incomparable pairs
  give only three successor classes, because `P+0<1` and `P+2<0` are both total
  even though `(0,1)` and `(2,0)` are in different `Aut(P)`-orbits.
* If some `φ ∈ Aut(P)` swaps `x` and `y`, then `φ` is an isomorphism
  `P+x<y → P+y<x`, so `max` collapses to one value. The converse held for
  `n ≤ 5` (experiment); it is not needed for soundness.

**States and moves are independent axes.** The state quotient (Sections 2–3)
shrinks the number of stored classes; the move quotient (Theorem 5) shrinks the
number of transitions per class. In a canonical-form implementation, skipping
the move quotient recomputes the *same* successor class once per orbit member,
paying redundant canonicalisation. Both are needed for the combined algorithm.

## 5. Microbenchmarks (experiment)

`scripts/benchmark_symmetry_quotients.py --max-n 6` (fixed `seed=0`; the
algorithms are deterministic, and `--shuffle-moves` only reorders moves and must
not change values). Four variants, all of which must return the same `S(n)`:

* `labelled` — memoised DP over labelled posets;
* `iso` — quotient by `S_n`;
* `iso+dual` — additionally quotient by `Z_2` (Theorem 3);
* `iso+dual+orbits` — additionally reduce moves to `Aut(P)`-orbits (Theorem 5).

Correctness and cost (one run; times are wall-clock, memory is peak traced
Python allocation):

| n | S(n) | labelled (states, time, mem) | iso (classes, time) | iso+dual (classes, time) | +orbits (moves, time) |
|---|---|---|---|---|---|
| 0 | 0 | 1, 0.000 s, 0 K | 1 | 1 | 0 |
| 1 | 0 | 1, 0.000 s, 0 K | 1 | 1 | 0 |
| 2 | 1 | 3, 0.000 s, 1 K | 2 | 2 | 1 |
| 3 | 3 | 19, 0.000 s, 6 K | 5 | 4 | 4 |
| 4 | 5 | 219, 0.006 s, 28 K | 16 | 12 | 23 |
| 5 | 7 | 4231, 0.202 s, 477 K | 63 | 39 | 126 |
| 6 | 10 | 130023, 9.633 s, 16294 K | 318 | 184 | 928 |

All values match the known `S(0..6) = 0,0,1,3,5,7,10`; the class counts match
A000112 and the computed iso+dual counts. The move-term totals on the classes
actually visited by the `iso+dual` DP fall from `0,0,1,6,34,182,1287` to
`0,0,1,4,23,126,928` when orbit reduction is enabled.

Automorphism pair-orbit statistics over all isomorphism classes:

| n | classes | incomparable pairs | `Aut`-orbits | reduction | classes with nontrivial `Aut` | Σ Aut |
|---|---|---|---|---|---|---|
| 2 | 2 | 1 | 1 | 0.0% | 1 | 3 |
| 3 | 5 | 7 | 5 | 28.6% | 3 | 12 |
| 4 | 16 | 44 | 30 | 31.8% | 11 | 59 |
| 5 | 63 | 286 | 200 | 30.1% | 44 | 325 |
| 6 | 318 | 2195 | 1599 | 27.2% | 216 | 2060 |

The move reduction is a real but modest ~30% at these sizes, concentrated in
symmetric posets. It does not change the number of classes and is not
asymptotic; its value is structural (it is exactly the set of distinct
successor classes) and as a safeguard against redundant canonicalisation.

## 6. Falsification attempts

### (a) Duality does **not** license dropping a comparison branch (falsified)

Theorem 3 might tempt one to keep only one orientation `x<y` per comparison,
arguing the reverse is "dual". This is **false**: the two children of a single
comparison can have different values. Smallest witness at `n = 3`: the poset
`{0<1}` with key `2` isolated; for the pair `{0,2}`,

    F(P + 0<2) = 1      (state {0<1, 0<2}: 0 minimal, 1‖2)
    F(P + 2<0) = 0      (state {2<0<1}: total).

So `max` cannot be replaced by either branch, and duality applies to whole
states, not to the two orientations of a move. (Reproduced by
`falsify_dual_branch`.)

### (b) Degree-based move identification is unsound (falsified)

A cheap substitute for `Aut(P)`-orbits is to identify incomparable pairs whose
endpoints have matching `(in,out)`-degrees. This is **unsound**. Witness at
`n = 6`, poset with successors `(0,0,0,3,5,15)`: two pairs share the endpoint
degree signature `((0,2),(0,3))` but have move values `4` and `5`. Degree is a
coarsening of the automorphism orbit and cannot replace it. (Reproduced by
`falsify_degree_move`.)

### (c) The comparability graph does **not** determine `F` (falsified at `n=7`)

It is a **literature result** that the comparability graph determines the number
of linear extensions `e(P)` — a *comparability invariant* (Stanley's
order/chain-polytope identity; stated explicitly in McDiarmid–Penman–Iliopoulos,
arXiv:1603.02901). It is tempting to go further and quotient states by their
comparability graph. This is **unsound**.

**Witness at `n = 7`.** Two posets with isomorphic comparability graphs:

* `A`, successors `(0,0,1,3,5,5,37)`, relations `2<0, 3<0, 3<1, 4<0,
  4<2, 5<0, 5<2, 6<0, 6<2, 6<5` (as the bitmasks encode: bit `j` in
  `succ[i]` means `i<j`), has `F(A) = 6`;
* `B`, successors `(0,0,2,1,1,9,59)`, has `F(B) = 7`.

Their comparability graphs are isomorphic (explicit isomorphism
`(6,2,0,1,4,3,5)`), yet the values differ. Both values are computed by the exact
`S_n` quotient, and both `A, B` are canonical representatives. Hence the graph
is a comparability invariant for `e` but **not** for `F`. (Reproduced by
`falsify_comparability_graph`; checked in
`tests/test_symmetry_quotients.py`.) A bucket-based scan first finds the two
graphs at `n=7` with mixed `F`; the earlier `n ≤ 6` data showed none, so `n=7`
is the smallest size at which this compression fails.

**A second, independent obstruction (states vs moves).** Even setting
value-invariance aside, the graph transition is not well defined. Witness at
`n = 5`: two posets `P, Q` with the same comparability graph and the common
non-edge `{2,4}` yield successor comparability graphs differing by the edge
`{3,4}` (because `3<2` holds in `Q` but `2<3` in `P`). Hence Definition (ii)
fails. (Reproduced by `falsify_graph_transition`.) Together these show that
class-invariant *value* is insufficient and that a class must support an
equivariant *transition* to be a legitimate DP state.

### (d) Colour-pair-signature move quotient: survives `n ≤ 6`, unproven

Using the 2-dimensional colour-refinement signature of a pair as a cheap
surrogate for its `Aut(P)`-orbit found **no** counterexample for `n ≤ 6`
(`refine_colors` pair signature determines the move value for every class). It
is *not* proven sound and is a coarsening of the true orbit relation; it is
recorded as a hypothesis, not a reduction to rely on.

### (e) Complementary falsifications (staging, cited)

The staging draft already falsifies two stronger compressions that we do not
repeat: (i) states compressed to the linear-extension count `L(P)` do not
determine `F` (two `n=5` posets with `L=8` and `F=3` vs `F=4`); (ii) the
balanced-greedy restricted tree class returns `S(9)=20 > 19`. Both are
consistent with the picture here: `F` needs more than leaf counting, and the
`min` over all incomparable pairs cannot be replaced by a move-selection rule.

## 7. Literature grounding

* **Stober–Weiss, *Lower Bounds for Sorting 16, 17, and 18 Elements*,
  arXiv:2206.05597 (2022).** Exact adaptive worst-case comparison model. By
  exhaustive computer search extending Wells and Peczarski, using among other
  ideas a **bidirectional search**, they proved `S(16)=46`, `S(17)=50`,
  `S(18)=54` and a lower bound of 99 for `n=28`. This is exact-minima
  literature, not a symmetry quotient; it shows the state space is attacked by
  meet-in-the-middle and pruning. *Next hypothesis:* combine their bidirectional
  search with the `S_n × Z_2` quotient and `Aut`-orbit move reduction, since the
  meet-in-the-middle frontier is a set of poset classes.

* **Hanamura–Iwata, *Posets with seven linear extensions sortable by three
  comparisons*, Inform. Process. Lett. 111(8):365–369 (2011),
  doi:10.1016/j.ipl.2011.01.004.** Sorting under partial information. They
  characterise which posets with exactly seven linear extensions can be
  finished in `⌈log₂ 7⌉ = 3` comparisons. This is a small-scale witness that the
  information bound is not automatically tight, and it grounds our refusal to
  use `e(P)` (or `L(P)`) as a sufficient statistic. It concerns a restricted
  class (`e(P)=7`), not `S(n)`.

* **Kahn–Saks, *Balancing poset extensions*, Order 1(2):113–126 (1984),
  doi:10.1007/BF00565647.** Every finite non-total poset has an incomparable
  pair with `3/11 ≤ Pr(x<y) ≤ 8/11`; consequently sorting under partial
  information needs at most `C·log₂ e(X)` comparisons, `C ≈ 2.17`. This is an
  **upper bound** via a *move-selection* heuristic. It must not be conflated
  with exact minimax: balancing gives good trees, not optimal ones (cf. the
  staging balanced-greedy counterexample). It is precisely a move-level
  statistic of the kind whose quotients Theorem 5 makes exact and Section 6b
  shows can be made unsound by coarsening.

Model caveats: all three references are about adaptive worst-case pairwise
comparisons (Hanamura–Iwata additionally about partial information), not about
sorting networks; none is a complexity-class statement about evaluating `S`.

## 8. What was learned, failed ideas, next hypotheses

**Learned.**

1. Duality is a genuine second exact symmetry: `F(P^op)=F(P)`, giving the
   `S_n × Z_2` quotient (factor ~2, constant, not asymptotic).
2. A sound *state* quotient needs an equivariant *transition*, not merely a
   class-invariant value. Relabelling and duality are sound states; the
   comparability graph fails **both** tests (value non-invariant at `n=7`,
   transition ill defined at `n=5`).
3. `e(P)` is a comparability invariant (literature) but `F` is **not**
   (`n=7` witness): the minimax value is strictly more refined than the
   comparability graph, so leaf/extension counting is not a route to it.
4. Move orbits under `Aut(P)` are an exact (~30% here) transition reduction; the
   orbit partition refines the successor-class partition, so states and moves
   are independent axes and orbit reduction is sound but not maximally coarse.
5. Duality must not be used to drop comparison branches (witness at `n=3`).

**Failed / unresolved ideas.**

* Comparability graph as a DP state — `F` is not graph-invariant (`n=7`
  witness) and the transition is ill defined (`n=5` witness).
* Degree-based and colour-signature move quotients — first is unsound (`n=6`),
  second unproven beyond `n=6`.
* Disjoint-union / series-parallel decomposition: `F` is not additive over
  components because comparisons may be interleaved; a sound merge recurrence is
  not known.
* Automorphism computation is currently `O(n!)`; it is the practical bottleneck
  for the move quotient at larger `n`.

**Concrete next hypotheses.**

1. **Characterise the coarsest sound state quotient.** Relabelling + duality is
   exact; the comparability graph is not (value fails at `n=7`, transition at
   `n=5`). Is there an intermediate invariant, and what is the smallest poset on
   which `F` is not a comparability invariant (`n=7` here; `n ≤ 6` is fine)?
2. **Cheap exact move orbits.** Replace `O(n!)` automorphism computation by a
   canonical-labelling routine (nauty-style / colour-refinement with individual
   search) and test whether colour-signature move reduction is exact in
   practice up to `n=10`.
3. **Quotient + bidirectional search.** Run a meet-in-the-middle search on
   `S_n × Z_2` classes with orbit-reduced moves, targeting the known `n=12`
   obstruction (`S(12)=30 > ⌈log₂ 12!⌉ = 29`).
4. **A value invariant strictly between `e(P)` and the full poset** that still
   determines `F`: the comparability graph is ruled out, but the `n=7` witness
   is small and its graph has only two mixed classes, so a finer, still cheap
   invariant may exist.
5. **Coarser move reduction.** The successor-class partition is coarser than the
   `Aut(P)`-orbit partition; can it be computed directly (canonicalise the two
   children, no full automorphism group) to skip even more transitions?

## 9. Reproduce

    python3 scripts/benchmark_symmetry_quotients.py --max-n 5
    python3 scripts/benchmark_symmetry_quotients.py --max-n 6 --seed 0
    python3 scripts/benchmark_symmetry_quotients.py --max-n 5 --shuffle-moves --seed 12345
    python3 scripts/benchmark_symmetry_quotients.py --max-n 5 --falsify
    python3 -m unittest tests.test_symmetry_quotients -v

The `n=7` comparability-graph witness is reached through
`--falsify` (about 55 s, dominated by the `n=7` quotient and graph
canonicalisation); it is kept out of the default benchmark path to respect the
small host. `n ≥ 8` labelled DP is not attempted.

## 10. Provenance and non-overlap

* Primary sources: Stober–Weiss arXiv:2206.05597; Hanamura–Iwata
  doi:10.1016/j.ipl.2011.01.004; Kahn–Saks doi:10.1007/BF00565647; the
  comparability-invariant fact and its references via McDiarmid–Penman–
  Iliopoulos arXiv:1603.02901. OEIS A001035, A000112 are used as reference
  sequences only.
* Definitions, deductions and the duality/move-orbit theorems are this note's
  own; the relabelling quotient and the two complementary falsifications are
  credited to the staging draft and are not re-claimed.
* No Lean file is added or modified; the kernel-checked model is untouched.
* This document and `scripts/benchmark_symmetry_quotients.py` /
  `tests/test_symmetry_quotients.py` are the only artifacts of this task.
