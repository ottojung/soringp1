# Independent review: PR #22 (compositional one-ply lookahead)

**Reviewer artifact.** Independent peer review of
`research/compositional-lookahead-20261018`, head
`4abf2a6e047b4c4d4a4309c9e663c89ed4636387` ("Correct earliest
compositional gap with seven-key witness"), signed by Otto Jung. Reviewed
files: `docs/research-compositional-lookahead.md`,
`scripts/compositional_lookahead.py`, `tests/test_compositional_lookahead.py`.

**Verdict: YES — the mathematics is sound and the finite claims reproduce.**
One trivial arithmetic correction is needed in the note (below). No
counterexample to any mathematical claim was found.

The reviewer did not modify the source branch. Independent primitives live
in `scripts/review_compositional_lookahead.py`, pinned by
`tests/test_review_compositional_lookahead.py`.

## Method (disjoint from the author's code)

Every finite fact was re-derived with reviewer-owned primitives before
comparison:

* transitive closure by naive fixpoint (not the author's `add_relation`);
* `e(P)` by enumerating all permutations (`n <= 7`) — independent of the
  downset DP;
* `F(P)` by a separate minimax recursion over `frozenset` comparable-pair
  states (not the author's `minimax`);
* incomparability components by plain BFS (not union-find);
* the capped census/prune by independent permutation enumeration.

Bounded by design: exhaustive only for `n <= 4`; the `n <= 6` no-gap claim
is the complete targeted ordinal-sum enumeration; `n = 7` and the `W^t`,
`Q^t` families are direct. No exhaustive `n >= 6` poset enumeration and no
unbounded scan (Phoebe 8 GB constraint).

Commands run:

```
python3 -m unittest tests.test_compositional_lookahead -q        # 14 tests OK, ~0.4 s
python3 -m unittest tests.test_review_compositional_lookahead -q # 9 tests OK
python3 scripts/compositional_lookahead.py --prune               # 1210 checks, 471 fires
python3 scripts/review_compositional_lookahead.py                # ALL INDEPENDENT CHECKS PASSED
```

## Claim-by-claim

### 1. Soundness chain `L0 <= L1 <= B <= F` — CONFIRMED

The new link `L1 <= B` is correct. For a pair inside factor `P_i`, the
child has `e = e(P_i±)·Π_{j≠i} e(P_j)`, so

`L0(child) <= ceil(log2 e(P_i±)) + Σ_{j≠i} ceil(log2 e(P_j))`
`          = L0(P_i±) + Σ_{j≠i} L0(P_j)`,

using `ceil(a + integer) = ceil(a) + integer` (each `ceil(log2 e(P_j))`
is an integer). Taking `min` over the pairs of one factor and then `min`
over factors, `L1(P) <= L1(P_i) + Σ_{j≠i} L0(P_j) <= B(P)` because
`L0 <= L1` per factor. `B <= F` is per-factor `L1 <= F` plus ordinal-sum
additivity. The induction in §4 (`Lr(P,r) <= ceil(log2 e(P)) + r`, hence
`Lr(Q^t,r) <= ceil(t log2 e(Q)) + r`) is also correct: the two children of
any comparison partition the extensions, so `max(e_left,e_right) <= e(P)`
and the `r+1` step adds one.

Independent checks: exhaustive chain for `n <= 4` (242 posets, 0
violations); `n = 5` chain and `B = L1` re-checked over all 4231 posets
(0 violations, 0 strict `B > L1`), reproducing the note's `n <= 5`
regression. `B <= F` at `n = 5` rests on the general proof (a full `n = 5`
minimax re-run was intentionally skipped under the 8 GB bound).

### 2. Maximal series decomposition — CONFIRMED

`incomparability_components` matches an independent BFS for every poset
`n <= 4`. For those posets: every cross-component pair is comparable in a
single consistent direction, every component with `> 1` element is itself
series-prime (its incomparability graph is connected), and both
`e(P) = Π e(P_i)` and `F(P) = Σ F(P_i)` hold (1247 checks). The `n <= 4`
components are exactly the ordinal-sum blocks; the maximality argument is
the standard "incomparability graph disconnected iff series-decomposable"
fact, correctly invoked. The time claim (polynomial-time detection via
union-find, `O(n^2 α(n))`) is accurate.

### 3. The corrected `n = 7` witness — CONFIRMED

`P = (124,124,0,0,4,12,28) = A ⊕ V` with `A = (0,0)` (2-antichain) and
`V = (0,0,1,3,7)`. Independently:

```
e = 16, L0 = 4, L1 = 4, B = 5, F = 5
```

`F = 5` was obtained **directly** by the reviewer's minimax (not only via
additivity), and `e = 16` also by permutation enumeration. So the note's
correction of the earlier "first strict example at `n = 10`" claim is
right, and the strict gap already exists at `n = 7`.

**`n = 7` is in fact globally minimal.** A strict `B > L1` needs at least
two series factors and at least one strict one-ply factor (`L1 > L0`); the
reviewer's complete targeted enumeration of every ordinal sum of series
factors with parts `>= 2` and total size `<= 6` (1111 combinations, sizes
`2+2`, `2+3`, `2+4`, `3+3`, `2+2+2`) found **0** strict instances. Posets
with a single series factor have `B = L1` by definition, and size-1 factors
contribute nothing, so this covers all `n <= 6` posets. The note only
claims "smallest found", which is safe; the stronger statement is now
independently supported. (As a cross-check, the reviewer's first pass had a
bug in its own ordinal-sum helper — a missing `<< off` — which produced
spurious `n = 6` "strict" cases; after fixing the helper the count is 0.
The author's `ordinal_sum` is correct.)

### 4. `W^t` family and fixed-horizon failure — CONFIRMED

* `W = (26,0,10,0,8)`: `e = 8`, `L0 = 3`, `L1 = 4`, `F = 4` (independent
  `e` by permutations, independent `F`). The four pair splits are
  `(0,2):5/3`, `(1,3):5/3`, `(1,4):2/6`, `(2,4):6/2`, so every larger child
  has `ceil(log2) = 3` — exactly the mechanism the proof uses.
* `W^1`: `L1 = 4`; `W^2`: `e = 64`, `L0 = 6`, `L1 = 7`, `B = F = 8`;
  `W^3`: `e = 512`, `L0 = 9`, `B = F = 12`, `L1 = 10` (formula). Matches
  `L1(W^t) = 3t+1`, `B = F = 4t`, gap `t-1`.
* `Q = Merge(2,1) = (2,0,0)`: `e = 3`, `F = 2`; `Q^t`: `e = 3^t` (and
  independently `F = 2t` via additivity); the direct `Lr(Q^t,r) <=
  ceil(t log2 3)+r` checks pass, and the minimal `t` per horizon are
  exactly `{0:3, 1:5, 2:8, 3:10, 4:13, 5:15}`. This establishes the
  claimed negative result: for every fixed `r` some `Q^t` has `Lr < F`, so
  no fixed lookahead horizon equals `F` on all posets. Correctly labelled
  as a statement about lookahead strength, not a complexity-class result.

### 5. Capped enumeration and `L1`-prune — CONFIRMED

* `capped_pair_census` is correct: for `n <= 4` and `d <= 5` it matches an
  independent permutation census, including the `None` (over-`2^d`)
  behaviour and the full `c[i][j]` pair counts.
* Equivalence `prune_verdict(P,d) is False  <=>  L1(P) > d` holds in all
  1452 independent checks (`n <= 4`, `d <= 5`); the reviewer's independent
  prune agrees with the author's in every case, and every fire has
  `F > d` (soundness). The doc's `1210`-check `n <= 4, d <= 4` regression
  and 471 fires also reproduce.
* Edge cases are right: total poset is never rejected (returns `None`,
  `F = 0 <= d`); `d < 0` rejects outright; `d = 0` fires exactly on the
  non-total posets; at `W`, `d = 3` fires although `e(W) = 8 <= 2^3` (so
  the ordinary info prune is silent) and `d = 4` is inconclusive.
* Space/time: by inspection `capped_pair_census` allocates no `2^n`
  array — only `O(n^2)` counters of `<= d` bits plus an `O(n)` stack — so
  the polynomial-space claim holds; the `O(n^2 · 2^d)` amortized bound is
  consistent with a DFS that stops after `2^d + 1` leaves (a tree with `L`
  leaves has `< L·n` internal nodes). The note correctly keeps this
  distinct from the `Θ(2^n)`-space prototype `linear_extensions`.

## Needed fixes

1. **Arithmetic in `docs/research-compositional-lookahead.md` §3.** The
   count is written `1 + 3 + 19 + 219 + 4231 = 4474`; the sum is **4473**
   (`1+3+19+219 = 242`, `+4231 = 4473`). Either fix the total to 4473 or
   drop the total. Purely cosmetic; no mathematical content depends on it.

## Minor observations (no fix required)

* The note §3 states an exhaustive `n <= 5` chain regression, but the
  committed test (`test_exhaustive_n_le_4`) only runs `n <= 4`. The
  reviewer re-ran the `n <= 5` `L0 <= L1 <= B` and `B = L1` facts (4231
  posets, 0 violations); the note could either mention the CI cap or bump
  the test. Not a correctness issue.
* §3's `B = L1` on `n <= 5` and the single-factor `W` at `n = 5` are
  consistent; no contradiction with the strict gap at `n = 7`.

## Scope limits

This review covers the note, script and tests as mathematics and finite
experiments. It makes no complexity-class claim and confirms none: `e` is
`#P`-complete, so `L0/L1/Lr/B` are not claimed polynomial-time. The
reviewer did not merge the branch, did not modify it, and did not run any
exhaustive `n >= 6` poset enumeration or `n >= 15` computation.

## Sources / provenance

* Reviewed head: `4abf2a6e047b4c4d4a4309c9e663c89ed4636387` (signed).
* Base: `330cfa1`.
* Model/notation: `docs/problem.md`; one-ply bound and prune:
  `docs/research-one-ply-obstruction.md`; additivity and series
  decomposition: `docs/research-series-decomposition.md`; merge values:
  Hwang–Lin 1972, Stockmeyer–Yao 1980 (via
  `docs/research-structural-lower-bounds.md`).
* Reviewer artifacts: `scripts/review_compositional_lookahead.py`,
  `tests/test_review_compositional_lookahead.py`.
