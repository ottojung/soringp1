# Source audit and the local-structure frontier for n = 12 non-tightness

**Status:** research note. It is an **audit plus a small independent
experiment**, not a Lean file and not a complexity-class result. Every item is
labelled `[literature]`, `[deduction]`, `[experiment]`, `[conjecture]` or
`[open]`. Companion program: `scripts/obstruction_probe.py`; regression test:
`tests/test_obstruction_audit.py`. This note is **distinct from** and does not
modify [`research-n12-nontightness.md`](research-n12-nontightness.md); it audits
that note and attacks the next mathematical question.

## 0. Model, notation and scope

`[definition]` From `docs/problem.md`. `S(n)` is the minimum height of a
deterministic **adaptive** binary comparison decision tree that sorts every
permutation of `n` distinct labelled keys; comparisons are the only tests;
worst case. A state is a transitively closed strict partial order `P` on the
labelled keys; `e(P)` is the number of its linear extensions; `m(P)` is the
minimum number of further worst-case comparisons that sorts every linear
extension of `P` (so `m(P) = 0` iff `P` is a total order and `m(P0) = S(n)` for
the antichain `P0`). `C(n) = ceil(log2 n!)`. The node-level information bound is
`m(P) >= ceil(log2 e(P))`; the global bound `S(n) >= C(n)` is its root case.

**Scope.** This note is about **local** poset structure (`m(P)` versus
`e(P)`), and about the accuracy of the staged draft's claims. It does **not**
prove `S(12) = 30`, does not reproduce Wells' search, and does not establish any
complexity-class statement. Finite computations on `n <= 6` cannot and do not
settle `n = 12`.

## 1. Source audit of the staged n = 12 draft

I checked the draft's claims against the primary sources (text extracted
locally from the PDFs) and against an independent reimplementation. Findings,
most important first.

### 1.1 Citation error: the venue is ALENEX 2023, not SEA 2023

`[literature]` The draft (§3, source 3) cites Stober–Weiss as
"arXiv:2206.05597 (2022) / SEA 2023". The paper appeared at **ALENEX 2023**
(SIAM Symposium on Algorithm Engineering and Experiments), pages **201–213**,
DOI `10.1137/1.9781611977561.ch17`. The authors' own bibliography file and the
DBLP/ORCID records confirm ALENEX 2023, and Knuth's errata for *Selected Papers
on Analysis of Algorithms* (p. 500) also cites it as
"SIAM Symposium on Algorithm Engineering and Experiments (2023), 201–213".
**Correction required** before integration.

### 1.2 Table 2 n = 12 row: `sortable = no`, not "both outcomes needed"

`[literature]` The draft (§4) reports the Stober–Weiss n = 12 row as
"... backward layers `C_f = 5`, 'both outcomes needed: no', about 6190 posets,
152 ms". The actual row of their Table 2 is

```
n   C(n)  eff. E_tot  efficiency bandwidth  full layers  sortable  posets   forward  backward  total
12  29    0.89        0.05                  5            no        6190 ‡   15 ms    137 ms    152 ms
```

The quoted column is **`sortable = no`**, i.e. the poset `P0` is *not* sortable
in `C(12) = 29` comparisons (`S(12) > 29`). It is **not** a column "both
outcomes needed". The statement that for `n = 12` "it is sufficient to check
only one outcome" is a *separate* remark in their introduction, describing
Wells' one-sided forward search (their §1 and §3); the draft has merged the two
into a single table entry. The numerical values `E_tot = 12!/2^29 = 0.8922`,
bandwidth `0.05`, layers `5`, `6190`, `152 ms` are all correct — only the
column label is wrong.

### 1.3 The 6190 figure is not a "bottleneck poset" count

`[literature]` The draft concludes that "the entire obstruction for `n = 12` is
concentrated in a narrow efficiency window `[0.892, 0.942)` and a small state
set." Two problems:

1. The efficiency **bandwidth** `0.05` is a *user-chosen search parameter*
   `E_thr - E_tot` of the partial backward search, not a measured window of
   bottleneck posets. The interval `[0.892, 0.942)` is therefore the threshold
   window the authors *searched*, not the empirical efficiency distribution of
   the obstruction.
2. Footnote ‡ of their Table 2 says of the `6190`: *"The number of posets
   explored for `n = 12` is significantly larger than the numbers given in
   [6, 11]. In this case the bidirectional search increased the search space:
   most of the posets can be attributed to the backward search."* So `6190` is
   the number of posets **stored during both searches**, and for `n = 12` the
   bidirectional method actually **increased** the space. Describing these as
   "bottleneck posets" that localise the obstruction is an over-reading of the
   source.

Consequently draft hypothesis **H5** ("all bottleneck posets lie in a narrow
efficiency window just above `E_tot`, supported by literature") is **too
strong**: what Stober–Weiss support is an algorithmic *parameter*, not a
measured confinement of the obstruction. `[deduction]`

### 1.4 §8 needs a same-`e` witness; H2 alone is weaker

`[deduction]` The draft's §8 states: "no invariant that is a function only of
the number of linear extensions ... can explain the gap." This is a statement
that `m(P)` is **not a function of `e(P)`**, which requires two posets with the
*same* `e` and *different* `m`. The draft's H2 witness, however, has
`e(P1) = 13 < e(P2) = 14` with `m(P1) = 5 > m(P2) = 4` — this only falsifies
*monotonicity* in `e`, a strictly weaker statement.

The needed same-`e` witness exists already at `n = 5` `[experiment]`:
among the `360` labelled posets on 5 elements with `e(P) = 8`, exactly `240`
have `m(P) = 3 = ceil(log2 8)` and `120` have `m(P) = 4`. Explicit witnesses:
`succ = (8, 12, 8, 0, 12)` (`m = 3`) and `succ = (26, 0, 10, 0, 8)` (`m = 4`).
So `m` is not a function of `e` at `n = 5`, one level below the draft's
`n = 6` monotonicity witness. (The companion note
`research-state-compression.md` states the same fact via two `L = 8` posets;
the n = 12 draft does not.) The audit conclusion: the draft's §8 is *true* but
*not established by its own H2*; the fix is to cite the `n = 5`, `e = 8`
same-`e` pair.

### 1.5 Claims verified as accurate

`[experiment]` Independent reimplementation reproduces, without importing the
draft's script:

* H1 slack ratios: `n = 5: 1.0667`, `n = 10: 1.1558`, `n = 11: 1.6812`,
  `n = 12: 1.1208`, `n = 20: 1.8955`, `n = 22: 1.0503`, with tightness
  `yes, yes, yes, NO, yes, NO`. ✔
* H2 witnesses: `P1 = (20,16,0,23,0,22)` has `e = 13, m = 5`;
  `P2 = (0,37,1,39,1,0)` has `e = 14, m = 4`. ✔
* H3 witness: `succ = (0,0,1,3,7)` has `e = 8, m = 4 > ceil(log2 8) = 3`. ✔
* H4 numbers: forced threshold `F = 2^(h-1)/n!` equals `0.5333` (`n=5`),
  `0.5779` (`n=10`), `0.8406` (`n=11`), `0.5604` (`n=12`); the `2/3` split at
  depth 1 is inadmissible for `n = 5, 10, 12` and admissible for `n = 11`; the
  perfect-matching `5/6` split is inadmissible for `n = 10, 12`. ✔
* `E_tot = 12!/2^29 = 0.8922`. ✔
* Peczarski quotes: *"Wells reported [10] that for `n = 12` only the set `S24`
  is empty"* and the `P16`/`Q'16` passage — both match the extracted PDF text
  verbatim. Note Peczarski's own (both-outcomes) method empties `S23` for
  `n = 12` and `S40` for `n = 22`; the draft correctly attributes `S24` to
  Wells. ✔
* "efficiency refinement is equivalent to leaf counting": Stober–Weiss
  Observation 2.2 explicitly says it "follows by the same argument as the
  information theoretic lower bound". ✔

### 1.6 Minor reproducibility note

`[experiment]` The draft reports Experiment B at `n = 6` as taking "~15 min".
The independent implementation here enumerates all `130023` labelled posets on
6 elements and computes `m` for every one in about **10–25 s** on the same
machine class (global memoization of `m`; `linear_extensions` memoized). This is
a performance observation only, not a correctness issue.

## 2. Sharpening the local frontier: Hanamura–Iwata and the e <= 7 base

`[literature]` S. Hanamura and S. Iwata, *Posets with seven linear extensions
sortable by three comparisons*, Information Processing Letters **111**(8)
(2011), 365–369, DOI `10.1016/j.ipl.2011.01.004`, prove:

> every finite poset `P` with `e(P) = 7` linear extensions is sortable using
> three comparisons.

Since `ceil(log2 7) = 3`, this is exactly the statement that the local
information bound is *tight* for every poset with seven extensions, uniformly
in the number of elements. The authors note the result "may speed up exhaustive
computation to derive the lower bound of the minimum number of comparisons in
sorting".

**Definition (uniform tightness threshold).** `[definition]` For `r >= 0` let

```
T(r) = max { E : every poset P with e(P) <= E satisfies m(P) <= r }.
```

`T(r) <= 2^r` always. `T(3) >= 7` follows from two cited facts: for `e <= 6`,
the Kahn–Saks bound `3/11 <= Pr[x<y] <= 8/11` guarantees a comparison whose
heavier child has at most `(8/11)·6 = 4.36`, hence at most `4` extensions, and
a poset with `<= 4` extensions needs at most `2` comparisons (so `1 + 2 = 3`
suffices); for `e = 7`, Hanamura–Iwata give `3` directly. Conversely `T(3) <= 7`
because the `e = 8` witness below is not sortable in `3`. Hence `T(3) = 7`
exactly. `[literature]` + `[deduction]`

`[experiment]` Exhaustive enumeration for `n <= 6` gives the following
(thresholds for `r >= 4` are only certified for `n <= 6` here; the *first
failing e-level* is an upper bound on `T(r)+1`):

| r | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| `T(r)` (n <= 6) | 4 | **7** | 12 | 29 | 56 |
| first failing `e` | 5 | **8** | 13 | 30 | 57 |

**The frontier is sharp at `e = 8`.** `[experiment]` The first `e` for which the
local information bound fails is `e = 8`, with witnesses on both 5 and 6
elements (e.g. `n = 5`: `succ = (0,0,1,3,7)`, `e = 8`, `m = 4`; `n = 6`:
`succ = (28,20,0,4,4,30)`, `e = 8`, `m = 4`). No poset with `e <= 7` on `n <= 6`
elements has `m > ceil(log2 e)`. At `n <= 6`, `e = 7` is realised by `2880`
posets, **all** with `m = 3`, corroborating Hanamura–Iwata on this finite range.

So the *largest uniform (e-only) extension* of the information bound is exactly
`e <= 7`. This is the natural "small-e exact base" for an exact search; §4 turns
it into a pruning criterion and shows why it cannot be extended by simple
invariants.

## 3. Smallest counterexamples to tempting scalar hypotheses

All experiments below are exhaustive over all labelled posets on `n <= 6`
elements; the `n = 6` run visits `130023` posets.

### 3.1 `(e, width)` determines `m` at `n <= 5` but fails at `n = 6`

`[experiment]` At `n <= 5`, grouping all posets by `(e(P), width(P))` yields
**zero** collisions: `m` is a function of `(e, width)` on this range. (In
particular, at `n = 5` all `e = 8` posets of width `2` are loose, and all of
width `3` are tight.) This is a genuinely tempting scalar hypothesis.

It is **falsified at `n = 6`**, with 5 collisions. The smallest is
`(e, width) = (8, 2)`, where both `m = 3` and `m = 4` occur:

* tight: `succ = (2,0,43,3,43,0)`, `n = 6`, `e = 8`, `width = 2`, `m = 3`;
* loose: `succ = (26,0,10,0,8)`, `n = 5`, `e = 8`, `width = 2`, `m = 4`.

Other `n = 6` collisions: `(13,2)`, `(14,2)`, `(30,3)`, `(60,4)`.

### 3.2 Adding `#min, #max` still does not determine `m`

`[experiment]` Grouping by `(e, #min, #max)` gives 7 collisions at `n = 6`;
grouping by `(e, width, #min, #max)` still gives 4, e.g.
`(e, width, #min, #max) = (13, 2, 2, 2)` realises both `m = 4` and `m = 5`
(witnesses `succ = (8,24,57,0,0,9)` with `m = 4` and `succ = (20,16,0,23,0,22)`
with `m = 5`). No low-dimensional scalar signature of this kind determines
`m`. `[deduction]`

### 3.3 Merge posets are a structural source of local non-tightness

`[deduction]` Let `Merge(a, b)` be the disjoint union of a chain of `a`
elements and a chain of `b` elements; sorting it is exactly merging two sorted
lists. Its linear extensions number `e = C(a+b, a)`, and `m(Merge(a,b))` is the
minimum worst-case merge cost `M(a,b)`.

`[literature]` The exact value of `M(a,b)` "has been solved completely only for
a few special cases" (Li–Sun–Zhang, ISAAC 2016). The elementary **tape
(linear) merge** gives the upper bound `M(a,b) <= a+b-1`, and this bound is
*optimal in balanced ranges*: `M(m,m) = 2m-1` (Graham–Karp; Stockmeyer–Yao
1980), and `M(m,n) = m+n-1` for `m <= n <= floor(3m/2)+1` (Stockmeyer–Yao 1980;
Murphy–Paull 1979; Christen 1978), extended to `n <= 1.52 m` by Li–Sun–Zhang
(2016). For unbalanced sizes the tape bound is **not** optimal: Hwang–Lin
(1972) give better algorithms, e.g. `M(1,n) = ceil(log2(n+1))`, which is far
below the tape bound `n` for large `n`. There is therefore **no universal
formula** `M(a,b) = a+b-1`; the equal-size value `M(m,m) = 2m-1` is the special
case used below.

`[experiment]` Exact minimax on the two-chain posets (no formula used) gives,
for small sizes:

| `(a,b)` | (1,4) | (2,4) | (2,6) | (3,5) | (4,4) | (5,5) | (6,6) |
|---|---|---|---|---|---|---|---|
| `e = C(a+b,a)` | 5 | 15 | 28 | 56 | 70 | 252 | 924 |
| `ceil(log2 e)` | 3 | 4 | 5 | 6 | 7 | 8 | 10 |
| `M(a,b)` | 3 | **5** | **6** | **7** | 7 | **9** | **11** |
| tight? | yes | **NO** | **NO** | **NO** | yes | **NO** | **NO** |

The smallest two-chain local violation is `Merge(2,4)` (`n = 6`): `e = 15`,
information bound `4`, but `M(2,4) = 5`; this value is itself covered by the
`m <= n <= floor(3m/2)+1` optimality theorem. The table also shows the
*balanced* family eventually violating (`Merge(5,5)`, `Merge(6,6)`), while
`Merge(4,4)` is still tight. So the tempting criterion "decomposable /
disjoint-union-of-chains posets are tight" is **false**, and the mechanism is
the exact merge cost `M(a,b)`, which leaf counting cannot see.

`[deduction]` The smallest local failure overall (`e = 8`, §2) is **not**
explained by the merge family: the frontier witness `succ = (0,0,1,3,7)` is not
a disjoint union of chains (its comparability graph is connected but not a
clique), so the merge family gives one mechanism of local non-tightness but not
the frontier.

`[experiment]` Disjoint unions of *three or more* chains (multi-way merge) are
a separate family; for `n <= 6` the loose cases are `(3,1,1,1)` (`e = 120`,
`m = 8 > 7`), `(3,2,1)` (`e = 60`, `m = 7 > 6`) and `(4,1,1)` (`e = 30`,
`m = 6 > 5`), while `(2,2,2)` (`e = 90`, `m = 7`) and `(3,3)` are tight.

## 4. Proposed pruning criterion, and why it cannot be extended naively

### 4.1 The criterion (certified small-budget base)

`[literature]` + `[deduction]` In an exact backward search that decides, for
each poset `P`, whether `m(P) <= r` (the Stober–Weiss/Peczarski backward layer),
use as **base cases**:

* `r = 0`: `P` total;
* `r = 1`: `e(P) <= 2`;
* `r = 2`: `e(P) <= 4` (so `T(2) = 4`);
* `r = 3`: **`e(P) <= 7`** — sortable in 3 by Hanamura–Iwata 2011.

Any poset with `e(P) <= 7` at remaining budget `3` can therefore be declared
sortable **without expansion to budget 0**. The bound `e <= 7` is exactly the
largest *uniform* base case of this form, by the sharpness in §2. `[experiment]`

This is a sound, externally certified pruning rule. It is *not* the same as the
"efficiency" refinement of the staged draft: the efficiency condition
`e(P) <= 2^r` is the information bound and is a *necessary* condition, whereas
`e <= 7 => m <= 3` is a *sufficient* condition that strictly strengthens the
base of the search (it certifies sortability of posets that the leaf count alone
cannot certify, e.g. `e = 7` with `2^2 < 7 <= 2^3`).

### 4.2 No-go: it cannot be extended by low-dimensional invariants

`[deduction]` `[experiment]` The following candidate extensions are all
falsified by the smallest explicit counterexamples above:

| Proposed extension | Status | Smallest counterexample |
|---|---|---|
| `e <= 8 => m <= 3` | **false** | `n = 5`, `succ = (0,0,1,3,7)`: `e = 8`, `m = 4` |
| `e <= 2^r` and `width <= 2` `=>` sortable in `r` | **false** | `n = 5`, `e = 8`, `width = 2`, `r = 3`, `m = 4` |
| `m` is a function of `(e, width)` | **false** | `n = 6`: `(8,2)` with `m in {3,4}` |
| `m` is a function of `(e, width, #min, #max)` | **false** | `n = 6`: `(13,2,2,2)` with `m in {4,5}` |
| every disjoint union of chains is tight | **false** | `Merge(2,4)`: `e = 15`, `m = 5 > 4` |
| monotone in `e` | **false** | `n = 6`, `P1`/`P2` (`e = 13 < 14`, `m = 5 > 4`) |

The one remaining "shape" with a *provable* reason is the merge family, whose
failure is explained by the exact merge cost `M(a,b)` (§3.3); but the smallest
failure (`e = 8`) is not of that shape, so even a decomposition-aware criterion
would not close the gap at `e = 8`.

**Conclusion (partial no-go).** There is a unique, sharp uniform small-budget
base case (`e <= 7`) beyond the trivial information bound, and it cannot be
extended by any of the natural low-dimensional scalar invariants `e`, `width`,
`#min`, `#max`, nor by the decomposable (merge) class. This is consistent with,
and gives a concrete local face to, the draft's observation that the `n = 12`
obstruction is non-scalar. It does **not** by itself locate or prove the global
`n = 12` gap.

## 5. What this note does *not* establish

`[deduction]` Explicitly, to prevent over-reading:

* It does **not** prove `S(12) = 30` or `S(12) > 29`. Those are literature
  facts (Wells 1965; reconfirmed by Peczarski and Stober–Weiss). No finite
  computation on `n <= 6` can settle `n = 12`, and none is offered.
* It does **not** give a reusable invariant that predicts global
  non-tightness. The local frontier `e = 8` is at `n = 5`; the first *global*
  gap is at `n = 12`. Local failures do not imply a global gap (`S(5) = 7` is
  tight despite the `e = 8` local failure).
* It does **not** reproduce Wells' `n = 12` search. The `6190`-poset count is
  read from Stober–Weiss Table 2, not recomputed.
* It does **not** claim any complexity-class statement about `S` or the
  threshold language.

## 6. Open hypotheses and next obstacles

* `[conjecture]` `T(r)` is a genuine, strictly increasing integer sequence
  (`4, 7, 12, 29, 56, ...` for `r = 2..6`, computed for `n <= 6`). Is there a
  closed form or a recurrence? `T(3) = 7` is certified for all `n`; the values
  for `r >= 4` are only certified here up to `n = 6`. A proof that `T(4) = 12`
  for all `n` would be a small but genuine strengthening of the local base.
* `[open]` Is the *first global* gap (`n = 12`) attributable to a merge-type
  substructure (a sub-poset `Merge(a,b)` appearing in every height-29 search)?
  The merge bound is the only local failure mechanism we can explain from first
  principles; testing this would require the actual bottleneck posets from the
  `n = 12` search, which are not published.
* `[open]` Is the maximum local gap `m(P) - ceil(log2 e(P))` unbounded in `n`?
  It is `1` for `n <= 6` here. Using the **balanced** merge family, where the
  exact value is known, `M(m,m) = 2m-1` and `e = C(2m,m)`, so
  `m - ceil(log2 e) >= 2m-1 - (log2 C(2m,m) + 1) = 0.5 log2(pi m) - O(1) ->
  infinity` by Stirling. Hence **yes**, the local gap is unbounded; the merge
  family alone witnesses `m(P) - ceil(log2 e(P)) -> infinity`. `[deduction]`
  (This answers the draft's §9 "Max local gap" question. It uses only the
  equal-size value `M(m,m) = 2m-1`, not any universal `a+b-1` formula.)
* `[open]` A human-readable certificate of `S(12) > 29` remains unknown; this
  note does not produce one.

## 7. Reproducing the audit

```
python3 scripts/obstruction_probe.py          # prints all witnesses above
python3 -m unittest tests.test_obstruction_audit -v
python3 -m unittest discover -s tests -v      # full suite (CI)
```

The probe is self-contained and does not import the staging draft. The `n <= 5`
enumeration is exhaustive and takes about 3 s; the `n = 6` facts in this note
come from a full enumeration of the `130023` labelled posets (about 10–25 s);
the two-chain merge table in §3.3 is computed by exact minimax in the probe
(about 15 s for `a, b <= 6`). The regression test only re-evaluates the named
witnesses, so CI stays fast.

## 8. Sources

1. F. Stober, A. Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements*,
   **ALENEX 2023**, SIAM, pp. 201–213, DOI `10.1137/1.9781611977561.ch17`;
   preprint arXiv:2206.05597v2 (2022). Tables 2–3 and Observations 2.2–2.3
   audited from the extracted text.
2. M. Peczarski, *Towards optimal sorting of 16 elements*, Acta Univ. Sapientiae
   Informatica **4**(2) (2012), 215–224. §3–§4 audited; `S24`/Wells and the
   `P16`/`Q'16` passage quoted verbatim.
3. M. Wells, *Applications of a language for computing in combinatorics*,
   Information Processing 65 (Proc. 1965 IFIP Congress), 1966, 497–498; and
   *Elements of Combinatorial Computing*, Pergamon, 1971. Original
   `S(12) > 29`.
4. S. Hanamura, S. Iwata, *Posets with seven linear extensions sortable by
   three comparisons*, Information Processing Letters **111**(8) (2011),
   365–369, DOI `10.1016/j.ipl.2011.01.004`.
5. D. E. Knuth, *The Art of Computer Programming*, Vol. 3, §5.3.1
   (merge-insertion; sorting-number history) and §5.3.2 (minimum-comparison
   merging; tape merge and its optimality conditions). Also *Selected Papers on
   Analysis of Algorithms* errata, p. 500 (ALENEX 2023 reference; `S(n)` known
   for `n <= 22`, `n = 23` open), <https://cs.stanford.edu/~knuth/aa.html>.
6. L. R. Ford Jr., S. M. Johnson, *A Tournament Problem*, Amer. Math. Monthly
   **66**(5) (1959), 387–389. The `30`-comparison upper bound at `n = 12`.
7. OEIS [A036604](https://oeis.org/A036604) (values; index only) and
   [A003070](https://oeis.org/A003070) (information bound; index only).
8. J. Kahn, M. Saks, *Every poset has a good comparison*, STOC 1984,
   DOI `10.1145/800057.808694`: every non-total poset has a pair with
   `3/11 <= Pr[x<y] <= 8/11`. Used in §2 for `T(3) >= 7` on `e <= 6`.
9. F. K. Hwang, S. Lin, *A Simple Algorithm for Merging Two Disjoint Linearly
   Ordered Sets*, SIAM J. Comput. **1**(1) (1972), 31–39,
   DOI `10.1137/0201004`. Unbalanced merges beat the tape bound; e.g.
   `M(1,n) = ceil(log2(n+1))`.
10. P. K. Stockmeyer, F. F. Yao, *On the Optimality of Linear Merge*,
    SIAM J. Comput. **9**(1) (1980), 85–90, DOI `10.1137/0209006`. Tape merge is
    optimal for `m <= n <= floor(3m/2)+1`, in particular `M(m,m) = 2m-1`.
11. Q. Li, X. Sun, J. Zhang, *On the Optimality of Tape Merge of Two Lists with
    Similar Size*, ISAAC 2016, LIPIcs **64**, pp. 51:1–51:17,
    DOI `10.4230/LIPIcs.ISAAC.2016.51`. Extends tape-merge optimality to
    `n <= 1.52 m`; confirms `M(a,b)` is known only in special cases; attributes
    equal-size optimality to Graham and Karp.

All sources treat **adaptive, worst-case pairwise comparisons**, not sorting
networks and not average case. The values `S(n)` for `n >= 7` are literature
facts, not computed here.
