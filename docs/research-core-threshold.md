# Finite comparison thresholds via cores

**Status:** research note. Sections 1–3 are a **paper proof**; Sections 4–5 are
an **experiment** (an exhaustive census with independent checks) resting on the
implementation described there. Companion program:
`scripts/core_threshold_census.py`; tests: `tests/test_core_threshold.py`. This
note closes a small, precisely delimited part of the structural frontier; it is
not a Lean file, not a complexity-class result, and it does **not** prove the
all-`r` threshold conjecture.

## 0. Definitions

`e(P)` is the number of linear extensions of a finite poset `P`; `m(P)` is the
minimum worst-case number of further adaptive comparisons that sorts every
linear extension of `P` (so `m` of a total order is `0`). `T(r)` is the largest
`E` such that `e(P) <= E` implies `m(P) <= r`, when that maximum exists.

Write `F_1 = F_2 = 1` for the Fibonacci numbers. An element is **universal**
if it is comparable with every other element. A **core** is a *nonempty* finite
poset with no universal element. (The empty poset vacuously has no universal
element, but `e = 1` and `m = 0`, so it never affects `T(r)` for `r >= 1`; the
census omits it deliberately.) An **ordinal sum** `A (+) B`
puts every element of `A` below every element of `B` and adds no other
relations; `P` is **ordinal-indecomposable** when it is not such a sum of two
nonempty posets. A **proper ideal** of `A` is a down-set other than `A`.

## 1. Reduction to cores

**Lemma 1** `[deduction]`. If `x` is comparable with every other element of `P`,
then `e(P) = e(P - x)` and `m(P) = m(P - x)`.

*Proof.* In every linear extension of `P`, the set of elements below `x` is
fixed, so its position is fixed; deleting `x` gives a bijection between the
extensions of `P` and those of `P - x`, hence `e(P) = e(P - x)`.

For `m`: in any state of the comparison game on `P`, a comparison involving `x`
has a determined outcome (every extension of the state agrees on it), so it
transmits no information and cannot reduce the worst case. A strategy for
`P - x` of height `h` is a strategy for `P` of height `h` (it never needs `x`,
whose position is known once the rest is sorted). Conversely, a strategy for
`P` of height `h` becomes one for `P - x` after deleting comparisons with `x`.
Hence `m(P) = m(P - x)`. ∎

**Corollary.** Iterating Lemma 1 maps any finite poset `P` either to a
nonempty core `C` with `e(C) = e(P)`, `m(C) = m(P)` and `|C| <= |P|`, or to the
empty poset (`e = 1`, `m = 0`, which a total order reaches). The empty outcome
never constrains `T(r)` for `r >= 1`. So a census of nonempty cores determines
`T(r)` for every `r` in the range it covers.

## 2. Maximal deletions of cores

**Lemma 2** `[paper proof]`. If `P` is an ordinal-indecomposable core with
`|P| >= 3`, then some maximal element `x` has `P - x` a core.

*Proof.* Suppose, for contradiction, that `P - x` is not a core for every
maximal `x`. Then `P - x` has a universal element `y_x`; since `P` is a core,
`y_x` cannot be universal in `P`, so `y_x` is incomparable with `x`.

*No `y_x` is nonmaximal.* Suppose `y_x` is nonmaximal and pick a maximal
`w > y_x`. Then `w != x`, and `w` is incomparable with `x`: `x < w` contradicts
maximality of `x`, while `w < x` would give `y_x < w < x`, contradicting
`y_x` incomparable with `x`. Let `y_w` be universal in `P - w`, so `y_w` is
incomparable with `w`. Here `y_w != x`: otherwise `x` would be universal in
`P - w`, hence comparable with `y_x`, which lies in `P - w` and is distinct
from `x`. Since `x` is maximal, `y_w != x` forces `y_w < x`. Also `y_x < w`,
because `w` is maximal and `y_x < w` was assumed. Finally `y_x` is comparable
with `y_w`, since `y_x` is universal in `P - x` and `y_w != x`. Either order
fails: `y_x < y_w < x` contradicts `y_x` incomparable with `x`, and
`y_w < y_x < w` contradicts `y_w` incomparable with `w`.

*All `y_x` are maximal.* A core has at least two maximal elements, since a
unique maximal element is above every other element. If there were three
maximal elements, choose two of them `x` and `z`; then `y_x` is maximal, lies in
`P - x`, and is distinct from `z`, so universality of `y_x` in `P - x` would
make it comparable with the distinct maximal element `z`, which is impossible.
Hence `P` has exactly two maximal elements `x, w`, and necessarily `y_x = w` and
`y_w = x`. Universality of `w` in `P - x` and maximality of `w` put every
element of `P - {x, w}` below `w`; symmetrically every such element is below
`x`. As `x` and `w` are incomparable, `P = (P - {x, w}) (+) {x, w}`, a
nontrivial ordinal sum (nontrivial because `|P| >= 3`), contradicting
indecomposability. ∎

## 3. Complete generation and the size bound

**Lemma 3** `[paper proof]`. If `P = A (+) B` is a core, then `A` and `B` are
cores and `|A|, |B| >= 2`.

*Proof.* If `a` is universal in `A` then `a` is below every element of `B` and
comparable with every element of `A`, hence universal in `P`. So `A`, and
symmetrically `B`, is a core. A one-element factor is comparable with everything
in the other factor, hence universal in `P`; so both factors have at least two
elements. ∎

**Lemma 4** `[paper proof]`. Every core is obtained from the 2-antichain by
repeatedly (i) adjoining a new maximal element above a proper ideal of a core
already obtained, or (ii) forming an ordinal sum of two cores already obtained.

*Proof.* Induct on `|P|`. For `|P| <= 3` the cores are the 2-antichain, the
3-antichain `e = 6`, and the one-relation-plus-isolated-element poset `e = 3`;
all are generated (the last two from the 2-antichain). The empty poset is
excluded by the definition of a core above. If `P = A (+) B`, use
Lemma 3 and the induction hypothesis. Otherwise `P` is indecomposable, so
Lemma 2 supplies a maximal `x` with `A = P - x` a core; by induction `A` is
generated. Let `I = {a in A : a < x}`. This is a down-set, and it is proper,
because `I = A` would make `x` universal in `P`. Adjoining `x` above `I`
reproduces `P`. ∎

**Lemma 5** `[paper proof]`. Every core satisfies `e(P) >= |P|`.

*Proof.* By induction on `|P|` along the generation of Lemma 4. Bases:
`e = 2, 6, 3` for sizes `2, 3, 3`.

*Ordinal sum*: `e(A (+) B) = e(A) e(B) >= |A| |B| >= |A| + |B|` for
`|A|, |B| >= 2`.

*Maximal insertion*: let `A` be a core with `|A| = a` and let `x` be adjoined
above the proper ideal `I`. For a linear extension `L` of `A`, let `p_L` be the
last position occupied by an element of `I`. Then `x` may occupy any of the
`a + 1 - p_L` slots after that position, each choice giving a distinct extension
of `P`, and every extension of `P` arises once this way. So
`e(P) = sum_L (a + 1 - p_L)`. Every summand is at least `1`. If `I` is empty,
`e(P) = (a + 1) e(A) >= a + 1`. Otherwise some maximal element `m` of `A` lies
outside the proper ideal `I`; a maximal element can be last in some linear
extension, so for that `L` we have `p_L <= a - 1` and the summand is at least
`2`; hence `e(P) >= e(A) + 1 >= a + 1`. ∎

**Corollary** `[deduction]`. A core with `e(P) <= E` has at most `E` elements,
so generating cores level by level up to size `E` and discarding those with
`e > E` enumerates *all* cores with `e <= E`, with no loss. (This is the only
use of Lemma 5; without it the level cap would be unjustified.)

## 4. Census and independent checks

`scripts/core_threshold_census.py` implements generation as `(up, extensions)`
pairs: extensions are propagated structurally by insertion and products, never
by scanning `n!` permutations, so large sparse cores stay cheap. Sections are
deduplicated by an isomorphism-canonical relabelling (refinement plus
backtracking). The bounded minimax decision is the exact comparison game on
extension sets with the usual information cut.

Known independent totals and cross-checks `[experiment]`:

| check | expected | obtained |
|---|---|---|
| core classes with `e <= 12` (independent full census) | 63 | 63 |
| core classes with `e <= 20` (independent full census) | 250 | 250 |
| all 250 cores at `e <= 20` sortable in 5 comparisons | yes | yes |
| cores with `e <= 33` for `n <= 8` from *all* unlabeled posets | — | equal sets |
| staircase `W_n`: `e = F_{n+1}`, `m = n - 1` | `n = 2..10` | matches |

The `n <= 8` row is a genuine independent check: an all-poset enumerator
(validated against the class counts `1, 2, 5, 16, 63, 318, 2045, 16999`), with
its own canonical form and extension counter, yields exactly the same 593 core
classes with `e <= 33` as the generator, level by level. The same check has
since been extended to `n = 9` (all `183,231` classes, class count validated):
`765` classes on both sides, zero missing, zero extra, per-level counts equal.
So the implementation is independently corroborated for `n <= 9`; the remaining
unreplicated range is `n = 10..33` for `E = 33` and `n = 10..54` for `E = 54`. The counts `63` and
`250` are the totals reported by the older direct census in this repository's
research log, which uses a different enumeration order.

## 5. Verified thresholds

**Result** `[experiment, conditional on the implementation matching §4]`.

* `T(6) = 33`: all 1,053 cores with `e <= 33` are sortable within 6
  comparisons, and the staircase `W_8` has `e = 34`, `m = 7` (it fails at 6 and
  succeeds at 7).
* `T(7) = 54`: all 4,829 cores with `e <= 54` are sortable within 7
  comparisons, and the staircase `W_9` has `e = 55`, `m = 8`.
* `T(8) = 88`: all 22,120 cores with `e <= 88` are sortable within 8
  comparisons, and the staircase `W_10` has `e = 89`, `m = 9`, so no larger `E`
  carries the same guarantee.

Together with the previously established `T(2..5) = 4, 7, 12, 20` (see
`docs/research-obstruction-next.md` and the SoringP1 #301 research record), this
gives `T(r) = F_{r+3} - 1` for `2 <= r <= 8` (`4, 7, 12, 20, 33, 54, 88`), the
cases `r = 6, 7, 8` being new here.

## 6. Limits, and the open all-`r` statement

The census is **conditional on implementation faithfulness**. The generator was
audited against an independent all-poset enumeration only for `n <= 9` and
against the known totals at `E = 12, 20`; the ranges `n = 10..33` (for
`E = 33`), `n = 10..54` (for `E = 54`) and `n = 10..88` (for `E = 88`) rest on
the generator alone. A second, dual generator (minimal insertion below proper
filters, independent canonical form) is the natural check and is being run
separately; until it agrees on those sets, `T(6) = 33`, `T(7) = 54` and
`T(8) = 88` should be cited as *verified by one audited implementation*, not as
independently replicated.

The general statement behind all of this,

    e(P) >= F_{m(P)+2} for every finite poset P,

**remains open**. It is equivalent to the *lower* half of
`T(r) = F_{r+3} - 1`, namely `T(r) >= F_{r+3} - 1` for every `r`: every poset
with `e <= F_{r+3} - 1` has `m <= r`. The matching upper half needs the
staircase family `W_n` to have `e(W_n) = F_{n+1}` and `m(W_n) = n - 1` for
every `n`, which yields `T(r) <= F_{r+3} - 1` via `W_{r+2}` (`e = F_{r+3}`,
`m = r + 1`). Those staircase values are **verified computationally** for
`n <= 10` (Section 4; `W_11 = (144, 10)` was checked with the same script), not
proved for all `n` here; so the two halves are not
interchangeable, and neither is claimed for all `r`. A sufficient route is the balancing statement (*Lemma A*):
every `P` with `m(P) >= 2` has a comparison whose two children both have depth
at least `m(P) - 2`. That is unproved; if it holds, the Fibonacci induction is
straightforward, since both children of a needed comparison must be large.
Nothing in this note proves Lemma A, and the finitely many verified `r` do not
imply it.

**Why it matters, and what it does not give.** Bounds on `T(r)` are statements
about the minimax game on *partial* orders: they say that no poset whose
extension count is small can be much harder than the information bound. They
sharpen the search landscape for exact evaluation of `S(n)` (a state with
`e <= 33` never needs more than six further comparisons, so such states can be
resolved by table lookup instead of full minimax), but the root state of `S(n)`
is the antichain with `e = n!`, far outside the threshold range for `n >= 6`.
They therefore do not by themselves yield a better uniform bound for `S(n)`.

## 7. Reproduce

```sh
python3 -m unittest tests.test_core_threshold -v
python3 scripts/core_threshold_census.py --E 33 --h 6 --levels   # 1053 cores, 0 failures
python3 scripts/core_threshold_census.py --E 54 --h 7            # 4829 cores, 0 failures
python3 scripts/core_threshold_census.py --E 88 --h 8            # 22120 cores, 0 failures
SORINGP1_SLOW_TESTS=1 python3 -m unittest tests.test_core_threshold -v  # adds the T(8) check
```
