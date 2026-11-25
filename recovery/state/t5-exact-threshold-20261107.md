# Exact universal tightness thresholds: T(4)=12 and T(5)=20

**Status:** research note, 2026-11-07. Evidence type: exhaustive finite
computation (`[experiment]`) plus paper deductions (`[deduction]`); not Lean,
not kernel-checked, and not a complexity-class result. This note corrects the
front claim `T(5)=27` and the earlier `n<=6` extrapolation `T(5)=29`.

## 0. Definitions and result

For a finite poset `P`, let `e(P)` be its number of linear extensions and
`m(P)` its exact worst-case adaptive comparison depth (the minimax value; `m=0`
iff `P` is total). Define the uniform tightness threshold

    T(r) = max { E : every finite poset P with e(P) <= E has m(P) <= r }.

**Theorem.** `T(4)=12` and `T(5)=20`.

Sharp witnesses are the staircase posets `S_n` on `n` elements with predecessor
masks

    S_n : pred[i] = 0 for i=0,1, and pred[i] = (1<<(i-1))-1 for i>=2.

Equivalently, `S_n` has `i < j` exactly when `j >= i+2`; consecutive elements
are incomparable, and `Inc(S_n)` is the path `0-1-...-(n-1)`.
Exact values (two independent methods, see §4):

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| `e(S_n)` | 2 | 3 | 5 | 8 | 13 | 21 | 34 |
| `m(S_n)` | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

Thus `S_6` has `e=13, m=5` (so `T(4)<=12`) and `S_7` has `e=21, m=6` (so
`T(5)<=20`). In particular the 8-element `Merge(2,6)` (`e=28, m=6`) is **not**
the sharp failing instance; it only gives `T(5)<=27`. The staircase witness has
seven elements and `e=21`.

## 1. Why the `n<=6` table is not the answer

The table in `docs/research-obstruction-next.md` §2 reports the first failing
`e` for `r=5` as `30` at `n<=6`, hence `T(5)=29` on that finite range. The
seven-element `S_7` has `e=21` and `m=6`, so the first failing `e` drops from
`30` to `21` as soon as the ground set reaches seven elements. Ground-set size
is essential; the `n<=6` value does not extend.

## 2. Exhaustive computation of all ordinal-indecomposable cores

Use the standard ordinal-sum decomposition (repository
`docs/research-series-decomposition.md`, Theorem 2): every finite poset is a
unique ordinal sum `P = P_1 ⊕ ... ⊕ P_k` of ordinally indecomposable posets,
whose ground sets are exactly the connected components of `Inc(P)`; moreover
`e(P)=∏ e(P_i)` and `m(P)=Σ m(P_i)` (Theorem 1 there).

So it suffices to compute `m` for every ordinally indecomposable poset with
`e<=20`.

**Enumeration.** Generate posets by maximal-element insertion. A natural
labelling is obtained by repeatedly removing a maximal element. Conversely,
starting from the empty poset, add a new maximal element `k` whose predecessor
set `D` is an order ideal of the current poset; insert `k` after the last
element of `D` in every current linear extension. This generates every finite
poset with every natural labelling (duplicates allowed, coverage complete).
Adding a maximal element cannot decrease `e`, so pruning at `e>20` is safe.
For a connected incomparability graph, the spanning-tree inequality gives
`n<=e` (each of the `n-1` spanning-tree edges is an incomparable pair, and
`e>=1+#incomparable pairs`); hence every connected core with `e<=20` has
`n<=20`, and depth 20 covers all of them.

**Exact minimax.** For every recorded core, `m` is computed by memoized
recursion over reachable posets: for each incomparable pair add either
orientation, take the transitive closure, and minimize `1+max(child values)`.
The maximum witnesses below were independently recomputed by extension-subset
DP (all agree); the 144 `e=11,12` records of the independent T(4) audit were
also recomputed from their saved extension lists and all give `F=4`.

**Counts.** 2022 connected-core representations, by `e` and maximum exact `m`:

| e | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| count | 1 | 1 | 3 | 4 | 10 | 10 | 21 | 24 | 45 | 45 |
| max m | 0 | 1 | 2 | 2 | 3 | 3 | 3 | 4 | 4 | 4 |

| e | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| count | 66 | 78 | 91 | 161 | 165 | 160 | 204 | 324 | 304 | 305 |
| max m | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |

The `e=11,12` counts and their `n`-distribution
(`e=11`: n=5:11, 6:22, 7:22, 11:11; `e=12`: n=4:6, 6:60, 12:12) match the
independent T(4) audit's 144 saved records exactly.

## 3. Thresholds from the table

Read off the first `e` at which a core of depth `d` appears:

    s(1)=2, s(2)=3, s(3)=5, s(4)=8, s(5)=13,

where `s(d)` is the least `e` of a poset with `m=d`; equivalently, every poset
with `e<s(d)` has `m<d`. (These are the Fibonacci values; see §5.)

**T(4)=12.** Let `e(P)<=12`, with factors `P_i`. Each factor is a connected
core with `e_i<=12`, so the table gives `m_i<=4`. If `Σm_i>=5`, then the depths
must contain `(4,1)` or `(3,2)` or a longer split. The minimal possible
extension products are `s(4)s(1)=8·2=16`, `s(3)s(2)=5·3=15`, and larger for
longer splits; all exceed 12. Contradiction. Hence `Σm_i<=4`, so `m(P)<=4`.
Together with `S_6` (`e=13,m=5`), `T(4)=12`.

**T(5)=20.** Let `e(P)<=20`, with factors `P_i`. Each `e_i<=20`, so the table
gives `m_i<=5`. If `Σm_i>=6`, the possible depth splits have minimal extension
products

    (5,1): 13·2=26,  (4,2): 8·3=24,  (3,3): 5·5=25,

and longer splits are larger. All exceed 20. Contradiction. Hence `Σm_i<=5`,
so `m(P)<=5`. Together with `S_7` (`e=21,m=6`), `T(5)=20`.

The use of `s(5)=13` is not circular: `s(5)=13` is exactly `T(4)=12`, proved
in the preceding paragraph from `s(1..4)`.

## 4. Independent checks

* `S_7` predecessor masks `[0,0,1,3,7,15,31]`: `e=21`, `m=6` by both
  poset-state recursion and extension-subset DP.
* `Merge(2,6)`: `e=28`, `m=6`; `Merge(2,5)`: `e=21`, `m=5`.
* The maximum witness for every `e=1..20` in the table was recomputed by
  extension-subset DP; all agree.
* The 144 saved `e=11,12` records of the T(4) audit were re-evaluated from
  their extension lists; all have `F=4`.

## 5. Structural pattern (equality for r>=6 is open)

The staircase `S_n` has `e(S_n)=F_{n+1}` (Fibonacci with `F_1=F_2=1`). The
board post of 2026-11-07T20:20Z gives the all-`n` proof of `m(S_n)=n-1`,
which I checked independently:

* `e(S_n)=F_{n+1}`: only adjacent pairs can be inverted, and two consecutive
  inversions are impossible, so extensions correspond to independent sets of
  the path on `n-1` edges.
* `m(S_n)=n-1`: nonconsecutive pairs are already comparable, so only the
  `n-1` adjacent pairs are informative. The adversary answers "not inverted"
  to every query; if edge `i` is never queried, the empty inversion set and
  `{i}` are both consistent, so every edge must be queried. Querying all
  `n-1` edges suffices.

Hence, for `r=n-1`, `S_{r+2}` has `e=F_{r+3}` and `m=r+1`, so

    T(r) <= F_{r+3}-1  for every r >= 2.

The computed exact values are

    T(2)=4=F_5-1, T(3)=7=F_6-1, T(4)=12=F_7-1, T(5)=20=F_8-1.

**Conjecture (not proved here):** `T(r)=F_{r+3}-1` for every `r>=2`, with
`S_{r+2}` extremal. The upper bound is now a theorem for all `r`; only the
matching lower bound for `r>=6` (equivalently, a Fibonacci splitting
induction) remains open. Only `r=2,3,4,5` are established by the computation
above.

## 6. Limits

* This is an exhaustive finite computation plus paper deductions, not a Lean
  proof. Its completeness rests on the insertion enumeration and the `n<=e`
  spanning-tree bound; both are stated above.
* It does not improve the uniform complexity of computing `S(n)` or
  `SORT-BOUND-U`. `T(5)` is a local pruning base for exact search, not a
  complexity-class separation.
* `T(5)=20` does not by itself say anything about `S(5)=7`; the relevant
  threshold at the root of `S(n)` is `T(S(n))`. It affects the `n=4` case
  (`S(4)=5`) and internal budget-5 nodes.
* The Fibonacci all-`r` formula remains a conjecture.

## 7. Reproduction

    go run ~/.local/state/soringp1/t5verify/enum_t5.go 20
    python3 ~/.local/state/soringp1/t5verify/verify.py
    python3 ~/.local/state/soringp1/t5verify/family.py

Source hashes:

    enum_t5.go   d71b1d5842e093b9ee274a7ded308429ec8641d6678dfa2164e4180d9c355a27
    verify.py    9f5a79c29a7c951258d7e635935529eda4aa62b036b89904483e59ae6146dff6
    family.py    b7f115607cda23e5d3a94455e089630d079326c20352e0f219a9a8f86cdcf6c2
    t4check.go   0f9d80d0b8a5350d0bf9bc8b36e2b25668533036dfaacadf0dd85c402f3c3a53

The enumeration takes a few minutes; `t4check.go` is the focused `e<=12`
variant.
