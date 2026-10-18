# Reversing Gallai/autonomous modules of a poset: does it preserve the exact minimax value?

**Status:** research note (2026-10-18). A **falsification with a restricted theorem**.
No Lean file and no complexity-class separation is claimed. Companion program:
`scripts/orientation_modules_probe.py`; tests:
`tests/test_orientation_modules.py`. Every number below is reproduced by the
program.

## Precise question

`docs/problem.md` fixes `S(n)` as the minimum worst-case number of adaptive
pairwise comparisons to sort `n` distinct labelled keys, and
`docs/upper-bound.md` / `SoringP1/Minimax.lean` (A24) identify it with the
partial-order minimax value `F(∅)`, where

    F(P) = 0                                                      if P is total,
    F(P) = 1 + min_{x ‖ y} max( F(P+x<y), F(P+y<x) )              otherwise.

A **Gallai module** (autonomous set) of `P` is a set `S` of keys such that
every key outside `S` is uniform towards `S`: above all of `S`, below all of
`S`, or incomparable with all of `S`. The module structure is the object behind
Gallai's substitution decomposition and, for comparability graphs, behind the
"only two transitive orientations of a prime graph" theorem of Gallai/Golumbic.
The companion note `docs/research-compression-next.md` shows that the
**comparability graph does not determine `F`** (`n=7`) and that only
relabelling and order duality are known *exact* state quotients. The natural
next candidate is:

> Does reversing the internal order of a module `S` (an operation that
> preserves the comparability graph and the number of linear extensions)
> preserve the exact minimax value `F`?

**Answer (this note).** No. It preserves `F` for every module on `n ≤ 6`
(3308 reversals, exhaustive), but fails at `n = 7`: exactly `8` of the `22494`
module reversals change `F`, forming two mixed classes of size `4`. The smallest
counterexample is the *same* poset pair that defeats the comparability graph,
and it also defeats the modular decomposition tree. A clean **restricted
theorem** survives: reversing an *interval module* (one comparable to every
outside key) always preserves `F`.

## Model and notation

A state is a strict partial order on `[n]`, stored as successor bitmasks
(`succ[i]` has bit `j` iff `i < j`). `x ‖ y` means incomparable. Reachable
states are the labelled posets (A001035); isomorphism classes are A000112. The
state count is `2^{Θ(n²)}`; nothing here changes that. **No P/NP claim is
made.** `e(P)` is the number of linear extensions.

**Module reversal.** For `S ⊆ [n]`, let `σ_S(P)` be the relation that reverses
every relation internal to `S` and keeps every other relation (then closes
transitively). `σ_V(P) = P^op` is the order dual, so module reversal
generalises duality.

**Interval module.** `S` is an interval module when it is a module and every
outside key is *comparable* to `S` (no outside key is incomparable with `S`).
Series-quotient modules (quotient `P/S` a chain) are interval modules.

## 1. Module reversal stays inside the posets (deduction)

**Lemma 1.** If `S` is a module of `P`, then the flipped relation `σ_S(P)` is
already transitive and irreflexive, hence a strict partial order; no extra
closure relations are needed.

*Proof.* Irreflexivity is clear (the flip only reverses existing internal
relations). For transitivity take `x < y < z` in the flip and check `x < z`.
Write `R = P|_S` and `R* = (P|_S)^op` for the internal order before/after, and
let the outside relation be unchanged. Cases: (i) `x,y,z ∈ S`: `R*` is the dual
of a transitive relation, hence transitive. (ii) `x,z ∈ S`, `y ∉ S`: `x < y`
with `x ∈ S` forces `y` above all of `S` (module uniformity), while `y < z`
with `z ∈ S` forces `y` below all of `S`; impossible. (iii) `x ∈ S`, `y,z ∉ S`:
`x < y` and `y < z` are cross/outside relations, unchanged from `P`; `P`
transitive gives `x < z`, which is the unchanged cross relation. (iv) symmetric
to (iii). (v) all outside: `P` transitive. ∎

The program confirms that no module reversal is cyclic for `n ≤ 7` (the
non-module case *can* be cyclic; Section 6).

## 2. Reversal preserves the number of linear extensions (deduction)

**Theorem 2.** `e(σ_S(P)) = e(P)` for every module `S` of `P`.

*Proof.* A linear extension `L` of `P` is determined by (a) the relative order
of the non-`S` keys (a linear extension of `P|_{[n]∖S}`), (b) the relative order
of the `S` keys (a linear extension of `P|_S`), and (c) an interleaving of the
two that respects the cross relations. Because `S` is a module, the cross
relations are uniform: each outside key lies above all of `S`, below all of
`S`, or incomparable with all of `S`, so the interleaving constraint depends
only on the *positions* occupied by `S`, not on their order. Replacing the
`S`-subsequence by its reversal keeps all positions, keeps (a), and turns (b)
into a linear extension of `(P|_S)^op`; hence it is a linear extension of
`σ_S(P)`. The map is an involution, so it is a bijection `Ext(P) → Ext(σ_S(P))`. ∎

This is the module-level analogue of the fact that `e` is a comparability
invariant: `σ_S` preserves the comparability graph (below), so `e`-invariance
is expected. The point is that `F` behaves differently.

## 3. Restricted theorem: interval modules preserve `F` (deduction)

**Theorem 3.** If `S` is an interval module of `P` (every outside key is
comparable to `S`), then `F(σ_S(P)) = F(P)`.

*Proof.* An interval module `S` divides the outside keys into `A`, those
below every member of `S`, and `B`, those above every member of `S`.
There are no cross-incomparabilities. Moreover transitivity forces every
element of `A` below every element of `B` (when `S` is nonempty).
Consequently `P = P|_A ⊕ P|_S ⊕ P|_B` is an **ordinal sum**. Reversal
replaces only the middle factor `P|_S` by its order dual. The exact
ordinal-sum additivity theorem, proved in `docs/research-series-decomposition.md`,
and the exact order-duality invariance of `F`, proved in
`docs/research-compression-next.md`, give

    F(σ_S(P)) = F(P|_A) + F((P|_S)^op) + F(P|_B)
              = F(P|_A) + F(P|_S) + F(P|_B) = F(P).

This also covers incomparable pairs entirely *outside* `S`, which a
recurrence argument must not omit. Empty outside factors have cost zero;
if `S` is all of `P`, the result reduces to order-duality invariance. ∎

**Corollary 4.** If `P/S` is a chain (series quotient) then `σ_S` preserves
`F`. ∎ (A chain quotient is an interval module.)

The program verifies Theorem 3 exhaustively at `n = 7` (2612 interval-module
reversals, `0` failures); for `n ≤ 6` it is subsumed by the all-module check in
Section 4. `e`-invariance is checked for `n ≤ 6`.

## 4. Main falsification: prime-quotient modules fail at `n = 7` (experiment)

The program enumerates every isomorphism class and every nontrivial module,
reverses it, and compares `F`.

| n | iso classes | nontrivial modules | reversals | cyclic | F violations | e violations |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 2 | 4 | 4 | 0 | 0 | 0 |
| 3 | 5 | 23 | 23 | 0 | 0 | 0 |
| 4 | 16 | 115 | 115 | 0 | 0 | 0 |
| 5 | 63 | 579 | 579 | 0 | 0 | 0 |
| 6 | 318 | 3308 | 3308 | 0 | 0 | 0 |
| 7 | 2045 | 22494 | 22494 | 0 | **8** | — |

So a search restricted to `n ≤ 6` would wrongly conclude that module reversal
is an exact symmetry. At `n = 7` there are exactly two mixed classes, each of
size `4` (values are `F`):

* class I: `(0,0,0,2,1,21,55)` F6, `(0,0,2,1,1,9,59)` F7,
  `(0,0,1,1,3,5,45)` F7, `(0,0,1,3,5,5,37)` F6;
* class II: `(0,0,0,0,1,14,47)` F7, `(0,0,2,1,1,1,59)` F8,
  `(0,0,1,1,1,3,29)` F8, `(0,0,1,3,5,5,5)` F7.

The two posets `A = (0,0,1,3,5,5,37)` (`F=6`) and `B = (0,0,2,1,1,9,59)`
(`F=7`) from `docs/research-compression-next.md` lie in class I: they are
connected by a chain of two module reversals. Every violating module is a
**strong** module of size `4` with **prime quotient** (`|outside| = 3`); all
eight failures have this profile.

Bucketing all `n = 7` reversals by the quotient type `P/S`:

| quotient | reversals | F violations |
|---|---|---|
| series (chain) | 933 | 0 |
| parallel (antichain) | 675 | 0 |
| prime | 20886 | **8** |

So the safe zone is exactly the series/parallel quotients (and, by Theorem 3,
all interval modules); failure needs a **prime quotient**.

## 5. `e` versus `F`, comparability graph versus module reversal (deduction + experiment)

* `σ_S` **preserves the comparability graph**: internal comparability is
  reversed, cross comparability is unchanged (module uniformity), outside
  comparability is unchanged. Hence `σ_S` also preserves `e` (Theorem 2 is the
  direct argument).
* The comparability graph is a **comparability invariant for `e`** but **not
  for `F`** (`n=7` witness `A,B`; companion note).
* Therefore module reversal is a *graph-preserving* operation that fails to
  preserve `F` on **the same witness pair** `A, B`. It is a `e`-symmetry, not
  an `F`-symmetry.

**The modular decomposition tree also fails.** The program computes the Gallai
modular decomposition and its canonical form *up to reversal at every node*.
`A` and `B` have the **same** reversal-canonical tree, and the whole mixed
class I is a single tree-up-to-reversal class; yet `F` varies. Hence the
modular decomposition tree does **not** determine `F` either. (This is the
sharp form of the obstruction: even recording every prime quotient up to its
two Gallai orientations is insufficient.)

State-quotient sizes (`iso`; `iso+dual`; MDT up to reversal; `iso × module
reversal`), with exactness of `F` on classes:

| n | iso (A000112) | iso+dual | MDT up-to-reversal | iso × module-reversal | `F` exact? |
|---|---|---|---|---|---|
| 4 | 16 | 12 | 12 | 11 | yes |
| 5 | 63 | 39 | 38 | 33 | yes |
| 6 | 318 | 184 | 168 | 144 | yes |
| 7 | 2045 | 1082 | 931 | 824 | **no** (2 mixed classes each) |

`iso+dual` is exact (duality theorem). Module reversal gives the strongest
compression but is **not sound**; MDT up to reversal is in between and is also
**not sound**. Quotienting by **arbitrary** module reversals is not exact at `n = 7`; the restricted interval-module reversal quotient is sound by Theorem 3.

## 6. Falsifications and the role of the hypotheses

* **The module condition is essential (experiment).** Smallest cyclic flip:
  `n=3`, `P = (0,1,3)`, `S = {0,2}`; smallest value change with a valid poset:
  `n=3`, `P = (0,1,1)`, `S = {0,1}` (then `2 < 0` but `2 ‖ 1`, so `S` is not a
  module), `F` goes `1 → 0`. So `σ_S` is only a poset, and only
  `F`-preserving, under the module hypothesis.
* **The interval hypothesis in Theorem 3 is sufficient, not necessary.**
  Parallel-quotient modules are not interval modules (outside keys are
  incomparable with `S`), yet all `675` parallel reversals at `n = 7` preserve
  `F`. This is an **empirical observation** (`n ≤ 7`), not proven here.
* **Prime quotient is necessary but not sufficient for failure.** All `8`
  failures have prime quotient, but `20878` of the `20886` prime-quotient
  reversals at `n = 7` are fine.
* **`n ≤ 6` is a false positive.** Any claim that "module reversal is an exact
  symmetry" must be checked at `n ≥ 7`.

## 7. Literature grounding

* **Gallai, *Transitiv orientierbare Graphen*, Acta Math. Acad. Sci. Hungar.
  18:25–66 (1967).** Introduced the substitution/modular decomposition of
  comparability graphs and proved that a prime graph has at most two transitive
  orientations, reverses of each other. This is the reason the only freedom at a
  prime module is *reversal*: prime comparability graphs have a single
  orientation up to duality. Our failures live exactly at prime quotients.
* **Golumbic, *Algorithmic Graph Theory and Perfect Graphs*, Ch. 5
  "Comparability Graphs".** Standard reference for modules, `Γ`-chains,
  implication classes and the prime-graph orientation theorem (cited as
  Theorem 4.1 in McConnell–Spinrad, attributed to Golumbic); the section "The
  Number of Transitive Orientations" is the direct source for the orientation
  count used here.
* **McConnell–Spinrad, *Modular decomposition and transitive orientation*,
  Discrete Math. 201:189–241 (1999), doi:10.1016/S0012-365X(98)00319-7.** Gives
  the canonical modular decomposition and shows transitive orientation reduces
  to the prime quotients; states the prime-graph two-orientation theorem and
  that the canonical decomposition represents exactly the transitive
  orientations.
* **Bollobás–Brightwell, *Transitive orientations of graphs*, SIAM J. Comput.
  17(6):1119–1133 (1988), doi:10.1137/0217072** (and *Graphs whose every
  transitive orientation contains almost every relation*, Israel J. Math.
  59(1):112–128, 1987). The comparison model: for a graph `G` on `X` and an
  unknown total order `<`, ask for each edge `xy` whether `x < y`; the deduced
  partial order is `P(G;<)`. This is the fixed-graph, transitive-orientation
  version of sorting under partial information and grounds the observation that
  orientation choice (not just graph shape) carries the comparison information.

Model caveats: none of these references is a statement about the complexity of
evaluating `S(n)`. They concern poset/comparability structure and sorting under
partial information. Theorems 2–3, Lemma 1 and the `n=7` falsification are this
note's own.

## 8. What was learned, failed ideas, next hypotheses

**Learned.**

1. Module reversal is **not** an exact symmetry of `F`, even though it
   preserves the comparability graph and `e`. Smallest counterexample `n = 7`;
   `n ≤ 6` is misleading.
2. The failure is localised at **prime quotients**: series/parallel quotients
   are safe, and Theorem 3 proves the larger class of interval modules.
3. The **modular decomposition tree up to reversal does not determine `F`**:
   the same `n=7` pair defeats both it and the comparability graph.
4. Reversal of a module is only a valid operation (a poset) when `S` is a
   module; otherwise the flip can be cyclic or change `F` (already `n=3`).

**Failed / unresolved.**

* "Module reversal is an exact state quotient" — false at `n=7`; the quotient
  `iso × module-reversal` has two mixed classes.
* "MDT up to reversal is a sound canonical form for `F`" — false at `n=7`.
* A proof that **parallel**-quotient reversal preserves `F` (empirically true
  `n ≤ 7`); the cross moves `x ∈ S, y ∉ S` are exactly the case the interval
  induction cannot handle.

**Next hypotheses.**

1. **Characterise the exact failure set.** Is `F(σ_S(P)) = F(P)` decidable from
   `(P|_S, P/S)` alone, and is the failure of prime quotients always of the
   form "the prime quotient's two orientations give different values"?
2. **A value invariant below the comparability graph but above `iso`.** Both
   the graph and the MDT fail at `n=7`; is there a cheap invariant that tracks
   `F` on the two mixed classes (e.g. the prime quotient's two orientations
   weighted by internal `F`-profiles)?
3. **Interval-module quotient.** Since interval reversal is proven sound, the
   `iso × interval-reversal` quotient is an exact, cheap compression; measure it
   and combine with the `Aut`-orbit move reduction of the companion note.
4. **Larger `n`.** Check whether the mixed classes grow; `n=8` needs the labelled
   or meet-in-the-middle machinery, not attempted here.

## 9. Reproduce

    python3 scripts/orientation_modules_probe.py --max-n 6            # ~40 s
    python3 scripts/orientation_modules_probe.py --max-n 6 --n7       # + n=7
    python3 scripts/orientation_modules_probe.py --max-n 6 --no-e     # faster
    python3 -m unittest tests.test_orientation_modules -v

The `n=7` part uses the isomorphism-quotient DP (2045 classes, a few MB); it
does **not** enumerate the labelled posets. No `n ≥ 8` DP is attempted.

## 10. Provenance and non-overlap

* Primary sources: Gallai (1967); Golumbic, *Algorithmic Graph Theory and
  Perfect Graphs*, Ch. 5; McConnell–Spinrad, doi:10.1016/S0012-365X(98)00319-7;
  Bollobás–Brightwell, doi:10.1137/0217072 and doi:10.1007/BF02779671. OEIS
  A001035, A000112 are reference sequences only.
* The `n=7` comparability-graph witness `A, B` and the `iso+dual` quotient are
  from `docs/research-compression-next.md` and are reused, not re-claimed.
* Lemma 1, Theorems 2–3, the `n=7` module-reversal falsification and the
  MDT-failure observation are this note's own.
* No Lean file is added or modified; the kernel-checked model is untouched.
* This document, `scripts/orientation_modules_probe.py` and
  `tests/test_orientation_modules.py` are the only artifacts of this task.
