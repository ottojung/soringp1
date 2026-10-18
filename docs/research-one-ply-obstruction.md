# The one-ply adversarial information lower bound

**Status:** research note with a **proved** lower bound and a small reproducible
experiment. Not a Lean file and not a complexity-class result. Every item is
labelled `[definition]`, `[deduction]`, `[literature]`, `[experiment]` or
`[conjecture]`. Companion program: `scripts/one_ply_obstruction.py`; regression
test: `tests/test_one_ply_obstruction.py`. This note is **distinct from** the
staged drafts `research-obstruction-next.md` (local `e`-frontier audit) and
`research-structural-lower-bounds.md` (ordinal-sum/merge-factor compositional
bound); it attacks a different, *non-compositional* strengthening of leaf
counting.

## 0. Model, notation and scope

`[definition]` From `docs/problem.md`. `F(P)` is the minimum remaining
worst-case number of pairwise comparisons that identifies the unknown linear
extension of a finite poset `P` (the algorithm knows `P`, the adversary chooses
the extension). A state is a transitively closed strict partial order on
`{0, ..., n-1}`, represented by `n` successor bitmasks. `e(P)` is the number of
linear extensions; `F(P) = 0` iff `P` is total, and `F(antichain_n) = S(n)`.

`[definition]` The **information (leaf-counting) bound** is

```
L0(P) = ceil(log2 e(P)).
```

Any decision tree distinguishing the `e(P)` outcomes has depth `>= log2 e(P)`,
so `F(P) >= L0(P)`.

**Scope.** This note proves a *structural* lower bound `L1` that is (a) always
between `L0` and `F`, and (b) **strictly stronger than `L0`** on an infinite
family, the smallest witness being a single `n = 5` poset. It does **not**
prove `S(12) = 30`, any asymptotic bound, or any complexity-class statement. A
comparison lower bound on `S(n)` does **not** imply a complexity-theoretic lower
bound for *computing* `S(n)`; see `docs/problem.md`.

## 1. The one-ply bound and the two theorem inequalities

`[definition]` The **one-ply adversarial information bound** is

```
L1(P) = 0                                          if P is total,
L1(P) = 1 + min over incomparable pairs {i,j}
            of max( L0(P + i<j), L0(P + j<i) )    otherwise.
```

`L1` is a single minimax ply whose children are scored by `L0` instead of the
full recursion. It is the "adversary keeps the harder side, looked at one level
ahead" bound.

**Theorem 1 (soundness).** `[deduction]` For every poset `P`, `L1(P) <= F(P)`.

*Proof.* `F` satisfies the same recurrence with `F` in place of `L0` on the
children: `F(P) = 1 + min_{i,j} max(F(P+i<j), F(P+j<i))`. Since `L0 <= F`
pointwise (the information bound), `max(L0(left), L0(right)) <=
max(F(left), F(right))` for every pair. Taking `min` over pairs and adding `1`
gives `L1(P) <= F(P)`. Equivalently, `L1` is `F` with the child potentials
weakened from `F` to `L0`, so by monotonicity of the recurrence in the child
potential, `L1 <= F`. ∎

**Theorem 2 (dominance).** `[deduction]` For every poset `P`, `L0(P) <= L1(P)`.

*Proof.* Fix any incomparable pair `{i,j}`. The two children partition the
extensions, so `e(P) = e(P+i<j) + e(P+j<i)`, whence the larger child has
`e_child >= ceil(e(P)/2)`. Therefore

```
max(L0(left), L0(right)) >= ceil(log2 ceil(e/2)).
```

For every integer `e >= 1`, `ceil(log2 ceil(e/2)) >= ceil(log2(e/2)) =
ceil(log2 e) - 1`, so

```
1 + max(L0(left), L0(right)) >= 1 + (ceil(log2 e) - 1) = ceil(log2 e) = L0(P).
```

This holds for **every** pair, hence also for the `min` over pairs:
`L1(P) = 1 + min_{i,j} max(...) >= L0(P)`. ∎

`[deduction]` Together: `L0(P) <= L1(P) <= F(P)` for all `P`. Both inequalities
are non-strict in general; the content is that the gap `L1 - L0` is sometimes
strict (§3).

## 2. A safe budgeted pruning corollary

`[deduction]` In a budgeted decision procedure `CanSort(P, d)` (is `F(P) <= d`?),
if `d > 0` and **every** incomparable pair `{i,j}` has at least one outcome
child with `e(child) > 2^{d-1}`, then return `FALSE` immediately. This is
exactly the test `L1(P) > d`, so by Theorem 1 it never rejects a sortable
instance. It **strictly strengthens** the ordinary info prune `e(P) > 2^d`:
`L1 > d` can fire when `e(P) <= 2^d` (the `n = 5` witness below has `e = 8 =
2^3` yet is rejected at `d = 3`).

`[deduction]` *Implementation without a `#P` exact-count table.* Enumerate the
linear extensions of `P` **once**, capped at `T = 2^d + 1`. If more than `2^d`
are seen, the ordinary info bound already rejects. Otherwise, while visiting
the `e(P) <= 2^d` extensions, maintain a counter `c_{ij}` = number of visited
extensions with `i` before `j`, for every unordered pair. This costs
`O(e(P) * n^2) = O(2^d n^2)` time and `O(n^2 (d+1) + n^2)` bits of space (one
counter per pair plus the DFS stack). Then for each incomparable pair the child
counts are `c_{ij}` and `e - c_{ij}`, and `L1(P) > d` exactly when every pair has
`max(c_{ij}, e - c_{ij}) > 2^{d-1}`. This subsumes the `e(P) > 2^d` prune and
avoids a separate capped `e`-counter per candidate pair. Worst-case overhead
`O(n^2 2^d poly(n))` per node, polynomial space; composed with a budgeted DFS
it stays within the existing `2^{O(n log^2 n)}` worst case of
`docs/research-budgeted-dfs.md`, but the constant-factor overhead is real and is
a pruning heuristic, not a faster exact algorithm. No EXPTIME/P-class claim.

## 3. The smallest strict witness

`[definition]` A poset is a **strict witness** if `L1(P) > L0(P)`.

`[experiment]` Exhaustive enumeration of all labelled posets on `n <= 4`
elements (1 + 3 + 19 + 219 = 242 posets) finds **zero** strict witnesses: `L1 =
L0` everywhere. The smallest strict witness is at `n = 5`. In bitmask form it
is

```
W = (26, 0, 10, 0, 8)
```

with elements `{0, 1, 2, 3, 4}` and successor sets `{1,3,4}, {}, {1,3}, {}, {3}`.
Its independent exact-minimax values are

```
e(W) = 8,   L0(W) = ceil(log2 8) = 3,   L1(W) = 4,   F(W) = 4.
```

The four incomparable pairs split the 8 extensions as

```
{0,2}: 5/3,   {1,3}: 5/3,   {1,4}: 6/2,   {2,4}: 6/2
```

(no pair splits 4/4), so every first comparison leaves a child with `>= 5`
extensions, forcing `1 + ceil(log2 5) = 4` further work. Thus `L1(W) = 4 >
3 = L0(W)`, and `F(W) = 4` confirms the bound is **tight** at the witness. This
is the one-ply mechanism, distinct from the merge-factor gap `Merge(2, 4)`
(`n = 6`) of `research-structural-lower-bounds.md`: the `e = 8` obstruction is
not a disjoint union of chains and is explained by the *pairwise split structure*
of the extension set, not by merge cost.

`[conjecture]` The gap `L1 - L0` is `0` for `n <= 4` and `>= 1` for all `n >= 5`;
i.e. the one-ply bound is exact below `n = 5` and first strictly stronger at
`n = 5`. The `n <= 4` half is `[experiment]`; the `n >= 5` half is open and is
**not** settled by the bounded check here.

## 4. Complexity caveats (explicit)

`[definition]` Exact `e(P)` is `#P`-complete to compute in general, so neither
`L0` nor `L1` is claimed to be polynomial-time computable. The one-ply `min`
costs `O(n^2)` extension-count subcalls per state; it is cheaper than the full
optimal min-max only empirically, and both are exact, not approximate. This note
makes no polynomial-time, EXPTIME, or P/NP claim. The pruning corollary of §2 is
a *safe* (never-false-negative) rejection test, not a decision procedure.

## 5. Reproducing

```
python3 scripts/one_ply_obstruction.py          # fast bounded report (n<=4 + witness + sample)
python3 -m unittest tests.test_one_ply_obstruction -q   # < 1 s
python3 -m unittest discover -s tests -v                  # full CI suite
```

The default CLI is deliberately **not** exhaustive at `n = 5`: it checks every
poset on `n <= 4`, the explicit witness `W`, and a fixed deterministic 40-poset
`n = 5` sample with shared memoized `F` (283 posets total, ~0.1 s). The
inequalities `L0 <= L1 <= F` have general proofs (§1), so no exhaustive `n = 5`
`F` computation is needed or performed. No randomness, no network.

## 6. Sources

1. Project model and the standing warning that a comparison lower bound on
   `S(n)` is **not** a complexity lower bound for computing `S(n)`:
   `docs/problem.md`.
2. Related proved bounds in this project: the ordinal-sum/merge-factor
   compositional bound and extension monotonicity,
   `docs/research-structural-lower-bounds.md` (smallest merge witness
   `Merge(2, 4)`, `n = 6`); the local `e`-frontier audit,
   `docs/research-obstruction-next.md` (same `e = 8` witness, local view).
3. Budgeted DFS worst case `2^{O(n log^2 n)}` that the §2 prune composes with:
   `docs/research-budgeted-dfs.md`.
4. The information bound and the `n = 12` non-tightness baseline:
   `docs/exploration-agenda.md`, `docs/literature.md`.

The one-ply definition, Theorems 1–2, the §2 pruning corollary, and the `n <= 4`
+ witness + sample checks are original to this note; the `e = 8`, `m = 4`
witness itself is already known to the staged audit (H3) and is reused only as
the smallest strict instance of the new bound.
