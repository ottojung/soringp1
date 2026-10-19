# The adversarial lookahead hierarchy for exact comparison sorting

**Status:** research note.  The structural facts below (monotonicity, the
derivative bound, finite convergence) are short paper proofs.  The finite
computations are reproducible experiments on **labelled** posets.  No
complexity-class, hardness, or running-time claim is made; see
[§7](#7-what-is-not-claimed).  Companion program:
`scripts/lookahead_hierarchy.py`; regression tests:
`tests/test_lookahead_hierarchy.py`.

## 1. Model and definitions

Fix the model of `docs/problem.md`: adaptive worst-case pairwise comparison
sorting of `n` distinct labelled keys.  A *state* is a transitively closed
strict partial order `P` on `{0, ..., n-1}`.  Write `e(P)` for the number of
linear extensions and

```
F(P) = minimum remaining worst-case comparisons that sorts every linear
       extension of P,
```

so `F(P) = 0` iff `P` is a total order, and `F(antichain_n) = S(n)`.
`F` obeys the minimax recurrence

```
F(P) = 0  if P total, else  1 + min over incomparable {i,j} of max(F(P+i<j), F(P+j<i)),
```

where `P+i<j` is the transitive closure of `P ∪ {(i,j)}`.

The **adversarial lookahead hierarchy** is the sequence of lower bounds

```
L0(P)     = ceil(log2 e(P))                                    (information bound)
L_{r+1}(P) = 0 if P total, else
             1 + min over incomparable {i,j} of max(L_r(P+i<j), L_r(P+j<i)).
```

Thus `L1` is the *one-ply* bound of `docs/research-one-ply-obstruction.md` and
`L2` the *two-ply* bound.  `L_{r+1}` scores a state by one minimax ply whose
children are scored by `L_r`; `L0` is the leaf-counting score at the bottom.

**Labelled vs. isomorphism classes.**  The experiments enumerate *labelled*
posets (OEIS [A001035](https://oeis.org/A001035)):
`1, 3, 19, 219, 4231, 130023` for `n = 1..6`.  The hierarchy is invariant under
relabelling (it only uses incomparability and extension counts, both
relabelling-invariant), so every statement transfers verbatim to isomorphism
classes (OEIS [A000112](https://oeis.org/A000112):
`1, 1, 2, 5, 16, 63, 318`).  All counts in this note are labelled-poset counts.

## 2. The chain `L0 ≤ L1 ≤ … ≤ Lr ≤ F`

**Theorem 1 (monotone chain).**  For every poset `P` and every `r ≥ 0`,
`L_r(P) ≤ L_{r+1}(P) ≤ F(P)`.

*Proof.*  We use two lemmas.

*Lemma 1a (`L0 ≤ F`).*  A correct decision tree for `P` has at least `e(P)`
leaves: every linear extension of `P` reaches exactly one leaf, and a leaf
reached by extension `π` must output `π` (the path outcomes are the order of
`π` on the compared pairs, and the tree must sort `π` correctly), so distinct
extensions reach distinct leaves.  A binary tree of height `h` has at most
`2^h` leaves, hence `F(P) ≥ ceil(log2 e(P)) = L0(P)`.  ∎

*Lemma 1b (`L0 ≤ L1`).*  If `P` is total, both sides are `0`.  Otherwise, for
*any* incomparable `{i,j}`, every linear extension of `P` extends exactly one
of `P+i<j`, `P+j<i`, so `e(P) = e(P+i<j) + e(P+j<i)` and
`max(e(P+i<j), e(P+j<i)) ≥ e(P)/2`.  Since `ceil(log2(x/2)) = ceil(log2 x) − 1`,
`max(L0(P+i<j), L0(P+j<i)) ≥ L0(P) − 1`.  Taking the minimum over `{i,j}` gives
`L1(P) = 1 + min max(L0 children) ≥ L0(P)`.  ∎

*Upper chain.*  By induction on `r`, assuming `L_r ≤ L_{r+1}` pointwise:
for non-total `P`,
`L_{r+2}(P) = 1 + min max(L_{r+1}(children)) ≥ 1 + min max(L_r(children)) = L_{r+1}(P)`,
because `max` and `min` are monotone.  By induction on `r`, assuming
`L_r ≤ F` pointwise: `L_{r+1}(P) = 1 + min max(L_r(children)) ≤ 1 + min max(F(children)) = F(P)`.
The base `L0 ≤ F` is Lemma 1a.  ∎

The proof shows the strictness of Lemma 1b is exactly the "unbalanced split"
phenomenon: `L1 > L0` at `P` iff every comparison leaves a child with more
than `2^{L0(P)-1}` extensions.  The smallest such `P` is the known `n = 5`
one-ply witness `(26, 0, 10, 0, 8)` (`e = 8`, `L0 = 3`, `L1 = 4 = F`).

## 3. The derivative bound `Lr ≤ L0 + r`

**Theorem 2 (derivative / Lipschitz bound).**  For every poset `P` and every
`r ≥ 0`, `L_r(P) ≤ L0(P) + r`.

*Proof.*  First, `L1 ≤ L0 + 1`: for every incomparable `{i,j}`,
`max(e(P+i<j), e(P+j<i)) ≤ e(P)` (the two extension sets partition those of
`P`), hence `max(L0 children) ≤ L0(P)`, and `L1(P) = 1 + min max(L0 children) ≤ L0(P) + 1`.
Now induct on `r`:
`L_{r+1}(P) = 1 + min max(L_r(children)) ≤ 1 + min max(L0(children) + r)`
(induction hypothesis) `= r + 1 + min max(L0(children)) = r + L1(P) ≤ L0(P) + r + 1`.  ∎

Combining Theorems 1 and 2: `L_r ≤ min(L0 + r, F)`.  The bound is tight in the
sense that the hierarchy can rise by one at a step (e.g. `L1 = L0 + 1` at the
`n = 5` witness), but it cannot outrun the information bound by more than one
per ply.

## 4. Finite convergence is **always exact**

**Theorem 3 (universal finite exactness).** For every finite poset `P`
and every integer `r ≥ 0`,

```
min(F(P), r + 1) ≤ L_r(P) ≤ F(P).
```

In particular, if `F(P) > 0`, then `L_r(P) = F(P)` for every
`r ≥ F(P)-1`. For total `P` (`F(P)=0`), equality holds for all
`r`. Uniformly over all posets on `n` keys, the hierarchy stabilizes
to `F` by horizon `r = max(0, S(n)-1)`.

*Proof.* The upper inequality is Theorem 1. We induct on `r` for the
lower bound.

At `r=0`, if `P` is total, `L_0(P)=F(P)=0`. Otherwise `P`
admits at least two linear extensions, hence
`L_0(P)=ceil(log2 e(P)) ≥ 1 = min(F(P),1)`.

Suppose the bound holds at horizon `r` for every poset. Let `P`
be non-total. For **every** incomparable pair `q` with two outcome
children `P_q^+` and `P_q^-`, the defining exact minimax recurrence
implies

```
max(F(P_q^+), F(P_q^-)) ≥ F(P)-1.
```

By the induction hypothesis on both children and monotonicity of
`min(·,r+1)`,

```
max(L_r(P_q^+), L_r(P_q^-))
    ≥ min(max(F(P_q^+), F(P_q^-)), r+1)
    ≥ min(F(P)-1, r+1).
```

Take the minimum over all legal `q`, then add one:

```
L_{r+1}(P) ≥ 1+min(F(P)-1,r+1) = min(F(P),r+2).
```

This finishes the induction. Thus `r≥F(P)-1` makes the two bounds
equal (including the terminal case separately). Finally
`F(P)≤S(n)` because any sorting tree for the antichain sorts every
linear extension of `P`, yielding the stated uniform horizon. ∎

**Corollary 4 (unique fixed point).** The minimax operator
`Φ(X)(P)=0` for total `P`, otherwise
`1 + min_q max(X(P_q^+),X(P_q^-))` has exactly one finite-valued
fixed point on the collection of posets with a given fixed number of
keys, namely `F`.

*Proof.* Every legal comparison strictly reduces `e(P)`; induct
on `e(P)`. For `e(P)=1`, every fixed point has value zero.
Assuming the value at every state with fewer extensions is uniquely
determined, the recurrence uniquely determines the value at `P`,
and it is `F(P)`. ∎

**Why this does not give an efficient algorithm.** The uniform horizon
`S(n)-1` can itself be `Θ(n log n)`, and evaluating `L_r` via
the game tree still branches over incomparable comparisons at each
level. Universal finite exactness is a structural theorem, **not** a
polynomial-time algorithm or an upper bound on the computational
complexity of exact `S(n)` beyond the already known brute-force search.

**A false stronger bound.** The earlier draft claimed the stabilization
horizon was at most `max_P(F(P)-L_0(P))` merely because the hierarchy
has finitely many integer values. This reasoning was **incorrect**:
several consecutive horizons can have the *same* value before a later
increase. The explicit six-key witness `P=(48,0,0,0,0,0)` has
`F(P)-L_0(P)=1` but `L_0=…=L_4=8` and `L_5=9`. No bound
on the number of *iterations* follows from the number of *distinct
values* unless strict increase at every iteration is proved.
The bound `r≥F(P)-1` established above is valid.

## 5. Experiments

### 5.1 Exhaustive `n ≤ 5` (in CI, 0.3 s)

Over all `1 + 3 + 19 + 219 + 4231 = 4473` labelled posets with `n ≤ 5`:

| quantity | value |
|---|---|
| chain `L0 ≤ L1 ≤ L2 ≤ L3 ≤ F` violations | `0` |
| derivative `L_r ≤ L0 + r` violations | `0` |
| `max(L1 − L0)` | `1` |
| `max(L2 − L1)` | `0` |
| `max(F − L1)` | `0` |
| strict `L2 > L1` witnesses | `0` |
| global stabilization `r*` | `1` |

So on `n ≤ 5` the **one-ply bound is already exact**: `L1 = L2 = L3 = F`
everywhere, and the only hierarchy strictness is `L1 > L0` (the known one-ply
obstruction, smallest witness the `n = 5` poset `(26, 0, 10, 0, 8)`).  In
particular no `L2 > L1` is possible for `n ≤ 5`.

### 5.2 Exhaustive `n = 6` (offline, ~26 s; **not** in CI)

Over all `130023` labelled posets with `n = 6` (together with the `n ≤ 5`
posets, `136516` states):

| quantity | value |
|---|---|
| global stabilization `r*` | `5` |
| chain violations | `0` |
| derivative violations | `0` |
| `max(L1 − L0)`, `max(L2 − L1)` | `1`, `1` |
| `max(F − L1)`, `max(F − L2)` | `1`, `1` |
| `max(F − L∞)` | `0` |
| posets with `L1 < F` | `10050` (all at `n = 6`) |
| posets with `L2 < F` | `3570` (all at `n = 6`) |
| posets with `L∞ < F` | `0` |
| strict `L2 > L1` witnesses | `6480` |
| level-increase profile `# {L_r < L_{r+1}}`, `r = 0..5` | `[5880, 6480, 2520, 930, 120, 0]` |

The main findings:

* **The first strict two-ply witnesses appear at `n = 6`.**  There are `6480`
  of them, all on `n = 6`; none exist for `n ≤ 5`.  Thus deeper lookahead is
  strictly stronger than one-ply lookahead, but only starting at `n = 6`.
* **The hierarchy converges to the exact value** for every poset on `n ≤ 6`:
  `max(F − L∞) = 0`, with global stabilization `r* = 5`.
* The hierarchy is genuinely multi-ply: `L2 < F` on `3570` posets and the last
  posets to stabilize need five plies (`120` posets have `L_4 < L_5`).

**Smallest strict `L2 > L1` witness** (lexicographically first in the sorted
labelled enumeration):

```
P = (0, 0, 0, 1, 3, 27)      e = 30,  L0 = 5, L1 = 5, L2 = 6, F = 6.
```

Relations: `3 > 0`, `4 > {0,1}`, `5 > {0,1,3,4}`; element `2` isolated.
The `L1`-optimal move is `compare {2,3}`, splitting `e = 30` into two children
with `L0 = 4` each, so `L1 = 5`.  Every move has a child with `L1 ≥ 5`, so
`L2 = 6 = F`: the two-ply bound is already exact here.

**Simplest strict `L2 > L1` witness** (fewest strict relations, `6`; it is the
disjoint union `C2 ⊔ P4` of a 2-chain with the poset `1,2 < 4 < 5`):

```
P = (0, 0, 0, 1, 6, 22)      e = 30,  L0 = 5, L1 = 5, L2 = 6, F = 6.
```

Relations: `3 > 0`, `4 > {1,2}`, `5 > {1,2,4}` (i.e. `5 > 4 > {1,2}` plus the
isolated chain `3 > 0`).  The `L1`-optimal moves are `compare {0,1}`, `{0,2}`,
`{1,2}`, each splitting `30` into `L0 = 4,4`; all nine moves have a child with
`L1 ≥ 5`, so `L2 = 6 = F`.

**Deepest stabilization witness** (needs five plies; `0 > {4,5}`, others
isolated):

```
P = (48, 0, 0, 0, 0, 0)      e = 240,  L0..L4 = 8, L5 = 9 = F.
```

The `L1`-optimal moves `{1,2}, {1,3}, {2,3}, {4,5}` each split `240` into
children with `L0 = 7,7`; the hierarchy stays at `8` through `L4` and only
reaches `F = 9` at `L5`.

### 5.3 Reproduction

```sh
python3 scripts/lookahead_hierarchy.py --max-n 5   # 0.3 s, in CI
python3 scripts/lookahead_hierarchy.py             # n <= 6, ~26 s, offline
python3 -m unittest tests.test_lookahead_hierarchy -v   # ~1.3 s
```

The `n = 6` audit is intentionally excluded from the CI test set (the main
suite is already ~45 s); the tests pin the `n ≤ 5` exhaustive facts plus the
two explicit `n = 6` witnesses above.

## 6. Comparison with Stober–Weiß (arXiv:2206.05597)

Florian Stober and Armin Weiß, *Lower Bounds for Sorting 16, 17, and 18
Elements*, [arXiv:2206.05597](https://arxiv.org/abs/2206.05597) (v2, 2022),
prove `S(16) = 46`, `S(17) = 50`, `S(18) = 54` (and `S(28) ≥ 99`) by an
exhaustive bidirectional search extending Wells and Peczarski.  Their model is
exactly ours (poset states, `e(P)`, adaptive worst-case comparison trees), and
their technical ingredients map onto ours as follows.

* Their *efficiency* `E(P) = n! / (2^c · e(P))` is a normalized version of our
  `L0`, and their Observation 2.2 (`e(P) > 2^r ⟹ P` is not sortable in `r`
  comparisons) is exactly Lemma 1a (`L0 ≤ F`).  Their pruning uses only this
  `L0` cutoff.
* Their Observation 2.3 (one of the two children has `e ≥ e(P)/2`) is exactly
  the `L0 ≤ L1` step (Lemma 1b).
* Their forward-search predicate
  `S_c(P) = ⋁_{(u,v)} (S_{c+1}(P+uv) ∧ S_{c+1}(P+vu))` is exactly our `F`
  recurrence; their backward search and "advice" are algorithmic devices for
  computing `F`, orthogonal to the lookahead bounds.
* **They do not iterate the bound.**  Their lower-bound certificates are
  `L0`-based; the hierarchy `L1, L2, …` and the finite-exactness theorem proved here
  are not part of their analysis.  When `L_r > L0`, the hierarchy is a
  strictly stronger family of lower bounds than their pruning, and it could in
  principle be used as extra pruning inside their forward search (we do not
  claim this yields a speed-up).

**A hand computation at `n = 16` (paper only, no script).**  Since
`ceil(log2 16!) = 45 < 46 = S(16)`, the antichain at `n = 16` is a natural test
of whether lookahead closes the gap.  For the antichain, a poset with `k`
independent relations has `e = 16!/2^k`, a "chain of three" has `e = 16!/6`, and
"one below two" has `e = 16!/3`; with `log2(16!) ≈ 44.25` this gives
`L0 ∈ {43, 43, 42}` for the relevant two-relation children.  One computes
`L1(antichain_16) = 1 + 44 = 45 = L0` and
`L2(antichain_16) = 1 + L1(antichain_16 + 0<1) = 1 + 44 = 45 < 46 = F`.
So the antichain does not witness lookahead strictness up to two plies, and
the exactness theorem above guarantees
`L_r(antichain_16)=46` for `r≥45`, although the *smallest*
horizon at which equality first holds remains uncomputed.  This is the same phenomenon as the
`n = 12` non-tightness (`L0 = 29 < 30 = S(12)`), studied in
`docs/research-n12-nontightness.md`.

## 7. What is *not* claimed

* No complexity-class, hardness, or separation statement.  In particular this
  note makes no claim that `S`, `L0`, or `L_r` is in or outside `P`, `NP`,
  `EXPTIME`, or any other class.  Counting linear extensions `e(P)` exactly is
  #P-complete in general (G. Brightwell and P. Winkler, *Counting linear
  extensions is #P-complete*, Order **8** (1991) 225–242); both the hierarchy
  and the Stober–Weiß pruning rely on `e(P)`, so neither inherits a
  polynomial-time guarantee from anything here.
* The script runtimes (`0.3 s`, `~26 s`) are empirical observations about the
  finite labelled posets `n ≤ 6`, not a complexity bound.
* `L∞ = F` is **proved for all finite posets** (Theorem 3). This
  fact is not a computational complexity-class result and does not
  imply that a bounded or efficiently evaluated lookahead is exact.

## 8. Interpretation and next steps

The hierarchy is a monotone sequence of sound lower bounds and is
**provably complete for every finite poset**, not merely for the small
instances explored here. Its significance is *when* each state
stabilizes, rather than *whether* it eventually does. The `n≤6`
experiments locate the first strict `L_2>L_1` witness at six elements.
They also illustrate how many plies can pass without a value increase,
invalidating the old proposed stabilization bound.

Concrete useful questions:

1. At `n=12` (where `S(12)=30>L_0=29`) or `n=16`
   (where `S(16)=46>L_0=45`), determine the **smallest** horizon
   `r` at which `L_r(antichain_n)=S(n)`; Theorem 3 guarantees
   `r≤S(n)-1`, but this does not make computation cheap.
2. Investigate whether small `r` gives useful additional pruning in
   Stober–Weiß-style exact forward searches and measure the full cost of
   evaluating the bound.
3. Investigate the effect of ordinal-sum factorization on these horizons:
   summing `L_r` over factors is sound and may be strictly stronger than
   a global `L_r`, as explored separately in PR #22 and follow-up work.
