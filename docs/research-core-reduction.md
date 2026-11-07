# Core reduction for uniform tightness thresholds

**Status.** This note records a structural lemma about posets, a reduction that
turns any uniform tightness threshold `T(r)` into a finite check over *cores*,
and an independent finite confirmation of the known values `T(4)=12` and
`T(5)=20`. The thresholds `T(4)` and `T(5)` were already recorded through the
Kahn--Saks route in `docs/research-t4-threshold.md` and on issue #301; the
route here does not use Kahn--Saks, so it is a genuinely separate check. This
note does **not** advance the all-`n` `S(n)`/`SORT-BOUND-U` theorems or issues
#47/#48.

## Definitions

`e(P)` is the number of linear extensions of a finite poset `P`; `m(P)` is the
minimax adaptive pairwise-comparison depth needed to identify one. A **universal
element** is one comparable with every other element. A poset is a **core** if
it has no universal element. For `r >= 0`,

```
T(r) = max { E : every finite poset P with e(P) <= E has m(P) <= r }.
```

## 1. The core lemma

**Lemma.** If `P` has `n` elements and no universal element, then `e(P) >= n`.

Two independent proofs were obtained; both were audited case by case here. A
third, unrelated proof of the same statement was also supplied and audited. The
statement is sharp: the chain on `n-1` elements plus one isolated point has
`e = n` and no universal element.

### Proof A (single-deletion gain plus exact pair structure)

**Lemma A1.** If `x` is not universal, then `e(P) >= e(P-x) + 1`.

*Proof.* Let `Q = P-x`, `D = {d in Q : d < x}`, `A = {a in Q : x < a}`, and
choose `u` in `Q` with `u || x`. No `d` in `D` satisfies `u < d` (else
`u < x`), and no `a` in `A` satisfies `a < u` (else `x < u`). Every `d` in `D`
is below every `a` in `A`. Hence `Q` plus the relations `d < u` (`d` in `D`)
and `u < a` (`a` in `A`) is acyclic: a cycle would need a `Q`-path `u -> D`, an
`A -> u`, or an `A -> D`, none of which exists. Extend it to a linear extension
`L`. Inserting `x` immediately before `u`, or immediately after `u`, gives two
distinct extensions of `P`. Conversely every extension `M` of `Q` has all of
`D` before all of `A`, so `x` can be inserted in some slot between the last
element of `D` and the first element of `A`; distinct `M` give distinct
extensions of `P`. Therefore `e(P) >= e(Q) + 1`. ∎

**Lemma A2.** Suppose `P` has no universal element and every `P-x` has a
universal element. Then every element of `P` has exactly one incomparable
partner, `P` is a chain of `n/2` two-element antichain blocks, and
`e(P) = 2^(n/2) >= n`.

*Proof.* Choose `u_x` universal in `P-x`. Since `P` has no universal element,
`u_x || x`, so `Inc(u_x) = {x}`. The map `x -> u_x` is injective because
`u_x = u_y` forces `{x} = Inc(u_x) = Inc(u_y) = {y}`, and hence bijective. Every
`z` therefore equals `u_x` for a unique `x`, and `Inc(z) = {x}`. The partner map
is a fixed-point-free involution, so `P` splits into pairs `{z,z'}` with
`z || z'` and all cross-pair elements comparable. If `z < w` for two different
pairs, transitivity forces `z' < w`, `z < w'`, `z' < w'`; otherwise `z < z'` or
`w' < w`. The pairs are therefore totally ordered as blocks, and a linear
extension is the forced block order with one of two internal orders per block,
so `e(P) = 2^(n/2)`, and `2^p >= 2p` for `p >= 1`. ∎

**Proof of the lemma.** Induct on `n`. The case `n=2` is the antichain (`e=2`).
For `n >= 3`, either some `P-x` has no universal element, and Lemma A1 with the
induction hypothesis gives `e(P) >= (n-1) + 1 = n`, or every `P-x` has a
universal element, and Lemma A2 gives `e(P) = 2^(n/2) >= n`. ∎

### Proof B (maximal-deletion case analysis)

Choose a counterexample `P` of minimum size, `e(P) < n`, with no universal
element. For `n >= 3` there are at least two maximal elements. For a maximal
`x`, if `P-x` had no universal element then minimality gives `e(P-x) >= n-1`,
and for another maximal `y` the sets of extensions of `P` ending in `x`,
respectively `y`, are disjoint, so `e(P) >= e(P-x) + e(P-y) >= n`, a
contradiction. Hence every maximal deletion has a universal element `u_x`,
which must satisfy `u_x || x`.

Take distinct maximal `x,y`, `u = u_x`, `v = u_y`. Since `y` is maximal,
`u = y` or `u < y`; similarly `v = x` or `v < x`.

1. `u != y`, `v != x`: `u,v` lie in `P-x`, hence are comparable. `u < v < x`
   (as `v < x`) contradicts `u || x`; `v < u < y` contradicts `v || y`.
2. `u != y`, `v = x`: `x` is universal in `P-y` and `u` lies there, so `u < x`
   by maximality of `x`, contradicting `u || x`.
3. `u = y`, `v != x`: `y` universal in `P-x` gives `v < y`; `x` universal in
   `P-y` gives `v < x`; and `v` is comparable with every other element of
   `P-y`, so `v` is universal in `P`, a contradiction.
4. `u = y`, `v = x`: for `Q = P - {x,y}`, every `z` in `Q` satisfies `z < x`
   and `z < y`, while `x || y`. Hence `e(P) = 2 e(Q)`. `Q` has no universal
   element, since one would be universal in `P`. For `n >= 4`, minimality gives
   `e(Q) >= n-2`, so `e(P) >= 2(n-2) >= n`. For `n = 3`, `Q` is a singleton and
   therefore universal, so this case cannot occur.

All cases contradict `e(P) < n`. ∎

## 2. The reduction

If `z` is universal, let `L = {w : w < z}` and `U = {w : z < w}`. Then
`P = L (+) {z} (+) U` with every element of `L` below every element of `U`, so
`P - z = L (+) U`. Ordinal sums multiply extension counts and add minimax
depths (both proved in `docs/research-series-decomposition.md`), hence

```
e(P - z) = e(P),      m(P - z) = m(P).
```

Consequently, repeatedly deleting universal elements turns any poset into a
core with the same `e` and `m`, and the lemma bounds its size by `e`. Therefore

```
T(r) >= E   iff   every core Q with e(Q) <= E and |Q| <= E has m(Q) <= r.
```

A failure of `T(r) >= E` is witnessed either by such a core or by nothing. This
turns each threshold into a finite check over isomorphism classes of posets with
`e <= E` and `|P| <= E`. Only the lemma, ordinal-sum additivity and the finite
enumeration are used; in particular the checks below do **not** use Kahn--Saks.

## 3. Enumeration and its validation

Every finite poset is obtained from the empty poset by repeatedly adjoining a
new **maximal** element whose predecessor set is an ideal of the current poset,
and this construction is exhaustive. Since `e` cannot decrease when an element
is adjoined, pruning a branch as soon as `e > E` is sound and complete for
enumerating all posets with `e <= E`. Isomorphism classes are deduplicated by a
canonical form computed with colour refinement and individualization.

`scripts/core_reduction/` contains two independent implementations: an
extension-set enumerator (`core_sets.py`, states are exact linear-extension sets,
so comparisons split them directly) and a subset-DP enumerator
(`dp_reference.py`). Both agree on all class counts and on every computed
minimax depth. `validate_core_sets.py` re-checks:

- every stored extension set is exactly the extension set of its poset, its size
  equals the independent subset-DP count, and for `n <= 6` it equals a
  brute-force topological enumeration;
- the canonical form is invariant under all relabellings for `n <= 6`;
- the labelled census with `e <= 12` is `218, 3110, 42330` for `n = 4,5,6`, and
  the orbit-size sums of the computed classes match those labelled counts
  (a check of both the generator and the canonical form);
- for `E = 20`, the same orbit-size check at `n = 5` gives `3920`, matching the
  labelled census of posets with `e <= 20`.

## 4. Results

### `T(4) = 12`

`python3 scripts/core_reduction/run_core_sets.py 12 12 4` enumerates all
isomorphism classes of posets with `e <= 12` and `|P| <= 12` and finds exactly
`63` cores, whose minimax depth is at most `4`:

| n | classes | cores | max m |
|---:|---:|---:|---:|
| 2 | 2 | 1 | 1 |
| 3 | 5 | 2 | 3 |
| 4 | 15 | 7 | 4 |
| 5 | 41 | 15 | 4 |
| 6 | 93 | 21 | 4 |
| 7 | 169 | 10 | 4 |
| 8 | 273 | 3 | 4 |
| 9 | 409 | 1 | 4 |
| 10 | 581 | 1 | 4 |
| 11 | 793 | 1 | 4 |
| 12 | 1049 | 1 | 4 |

The unique `n = 12` core is the chain on 11 elements plus an isolated point:
`e = 12`, `m = 4`. Sharpness is the known witness `(20,16,0,23,0,22)` with
`e = 13`, `m = 5`, recomputed here. Hence `T(4) = 12`, confirming the earlier
Kahn--Saks-based package by an independent route.

### `T(5) = 20`

`python3 scripts/core_reduction/run_core_sets.py 20 20 5` enumerates all
isomorphism classes with `e <= 20` and `|P| <= 20` (18576 classes at `n = 20`)
and finds `250` cores, all with `m <= 5`; the unique `n = 20` core is the
20-chain minus one element plus an isolated point (`e = 20`, `m = 5`). The
witness `(0,0,1,3,7,15,31)` has `e = 21`, `m = 6`, recomputed here. Hence
`T(5) = 20`, independently confirming the conditional result recorded on
#301 (sha256 `WirodT7Kr-ytPSboX9NWxrIqoOuWPHSLuc-92xZmKaE`), again without
Kahn--Saks or the connected-incomparability-graph enumeration.

### `T(6)` is still open

Kahn--Saks with `T(5) = 20` gives `T(6) >= 27`: for `e <= 27` some comparison
has both children with at most `floor(8e/11) <= 19` extensions, and `T(5)=20`
sorts each child in at most five more comparisons. Conversely `Merge(3,5)`, the
disjoint union of a 3-chain and a 5-chain, has `e = 56` and `m = 7` (computed
here), so `T(6) <= 55`. The value `T(6) = 56` in
`docs/research-obstruction-next.md` is only the `n <= 6` table and is not the
unbounded threshold. Closing the gap `27 <= T(6) <= 55` needs a finite core
check up to `E = 55` or a new structural argument.

## 5. Scope

These are local threshold theorems about `e(P)` and `m(P)`. They do not give a
faster evaluator for `S(n)`, any new bound for the unary language
`SORT-BOUND-U`, or any statement about issues #47/#48. The proofs are paper
arguments; the finite parts are reproducible computations with a stated
completeness argument and independent validation, not a Lean formalization.

## Reproduction

```sh
python3 scripts/core_reduction/validate_core_sets.py          # ~75 s
python3 scripts/core_reduction/run_core_sets.py 12 12 4       # ~5 s
python3 scripts/core_reduction/run_core_sets.py 20 20 5       # ~6 min
```
