# Budgeted DFS for exact S(n): a sharper deterministic time bound

**Status:** research note (paper analysis + small experiment). Not Lean-checked.
Every item is labelled `[definition]`, `[literature]`, `[deduction]`,
`[experiment]`, `[conjecture]` or `[open]`. Companion program:
`scripts/budgeted_dfs.py` (pure DFS, no memoization, no advice).

**Claim.** `S(n)` is computable by a uniform deterministic exhaustive DFS in
time `2^{O(n log^2 n)}` and space `O(n^3 log n)` (numeric `n`), improving the
recorded `2^{O(n^2)}` memoized-DP bound of `docs/upper-bound.md`. The unary
threshold is decidable in deterministic time `2^{O(n log^2 n)}` and polynomial
space; the binary threshold in time `2^{2^{O(N)}}` and space `2^{O(N)}`
(`N = Θ(log n)`). No NP/hardness/optimality claim is made.

---

## 1. Model and game `[definition]`+`[deduction]`

From `docs/problem.md`: `S(n)` = minimum height (worst-case number of
pairwise comparisons) of a deterministic adaptive comparison tree sorting `n`
distinct labelled keys. A comparison transcript induces a strict partial order
`P` (kept as its transitive closure) on the keys.

The key identity (game `G(n,k)`, `docs/research-certificates-barriers.md` §0):

> State = transitively closed poset `P` on `n` labelled elements; start at the
> empty order. While `P` is not total and fewer than `k` comparisons remain:
> the **sorter** picks an incomparable pair `{x,y}`; the **adversary** answers
> `x<y` or `y<x`; replace `P` by its transitive closure. The sorter wins iff a
> total order is reached within `k` comparisons.
>
> `S(n) ≤ k` iff the sorter wins `G(n,k)`. `[deduction]`

This is exactly the minimax recurrence `F(P) = 1 + min_{x,y incomparable}
max(F(P+x<y), F(P+y<x))`, `F(total)=0`, `F(∅)=S(n)` of
`docs/upper-bound.md` (kernel-checked equal to `S n` as `adv univ`, A24).

## 2. Pseudocode (pure budgeted DFS) `[definition]`

`CanSort(P, d)` decides "sorter wins `G` from state `P` with budget `d`":

```
CanSort(P, d):
    if P is total:            return True        # order already determined
    if d = 0:                 return False       # out of budget, not done
    for each incomparable pair (i, j):            # sorter chooses (OR)
        if CanSort(closure(P, i<j), d-1)          # adversary answer 1
           and CanSort(closure(P, j<i), d-1):     # adversary answer 2
            return True                           # one pair works for both
    return False                                  # no pair works
```

To compute `S(n)`: binary-search `k` in `[0, U(n)]` with the constructive
merge-sort upper bound `U(n) = n·⌈log₂ max(2,n)⌉` (exact integer
`⌈log₂ n⌉ = (n-1).bit_length()` for `n ≥ 2`, no floating point). `CanSort` is
monotone in `d` (more budget never hurts), so the search returns the least `k`
with `CanSort(∅, k) = True`, i.e. `S(n)`. `O(log U(n)) = O(log n)` invocations.

The DFS is **uniform** (one procedure for all `n`), **deterministic**, uses
**no memoization** and **no nonuniform advice**.

## 3. Correctness `[deduction]`

**Theorem.** `CanSort(P, d) = True` iff the sorter can determine the total
order from state `P` within `d` comparisons. Hence `CanSort(∅, k) = True` iff
`S(n) ≤ k`.

*Proof by induction on `d`.*
- **Base `d = 0`.** Returns `True` iff `P` is total. With no comparisons the
  sorter wins iff the order is already determined. ✓
- **Step `d ≥ 1`.** The sorter's first comparison is some incomparable pair
  `(i,j)` (a comparable pair gains nothing). For a fixed `(i,j)` the adversary
  picks the worse of the two answers, so the sorter wins within `d` via `(i,j)`
  iff it wins within `d-1` from **both** `closure(P,i<j)` and
  `closure(P,j<i)`. Taking the OR over all pairs (the sorter chooses) gives the
  recurrence. By the induction hypothesis each recursive call is correct, so
  the conjunction/OR is correct. ✓

Adaptivity is captured: each branch may choose a *different* next pair.
Minimax is correct: the existential "∃ pair" is the OR-loop; the universal
"both answers" is the `and`. No `max`/`min` value bookkeeping is needed for the
decision version.

## 4. Time `[deduction]`

At any non-total state with budget `d>0` there are `B = binom(n,2)` incomparable
pairs and two adversary answers, so at most `2B = n(n-1)` children per node.
Depth is at most `d`. Hence the DFS tree has at most `(2B)^d` nodes:

```
T(n,d) ≤ (2B)^d · poly(n) = (n(n-1))^d · poly(n) = 2^{O(d log n)} · poly(n).
```

The `poly(n)` covers `is_total` `O(n^2)`, `incomparable_pairs` `O(n^2)`, and
`closure` `O(n^2)` per node; all budget/index counters are `O(log n)` bits.
The DFS short-circuits: for a pair, if the first branch fails it skips the
second, and on success it returns immediately, so a node may make fewer than
`2B` recursive calls. The bound `(2B)^d` is a valid worst-case upper bound
regardless (a node never makes more than `2B` calls). *Branching does not store
all choices* — the DFS backtracks (§5).

**Total for `S(n)`.** With `d = U(n) = O(n log n)` and `O(log n)` binary-search
probes (each `≤ U(n)`, sum dominated by the largest):

```
T_total(n) = O(log n) · 2^{O(U(n) log n)} = 2^{O(n log² n)}.
```

This improves the recorded deterministic bound `2^{O(n²)}` of
`docs/upper-bound.md`, since `n log² n = o(n²)`.

## 5. Space `[deduction]`+`[experiment]`

The DFS keeps only the current recursion path: at most `d+1` frames, each
holding one `n×n` bitmatrix (`n²` bits) plus `O(log n)` counters. On returning
from a child the frame is discarded before the next pair is tried. Hence

```
S_space(n,d) = O(d · n²) bits  ⇒  O(U(n)·n²) = O(n³ log n)  (numeric n).
```

`[experiment]` Instrumenting `scripts/budgeted_dfs.py` confirms the maximum
recursion depth equals `d+1` for all `n ≤ 5`, `d ≤ 5` (e.g. `n=5, d=5` → depth
6), i.e. `O(d)` frames, **not** `(2B)^d`. No memoization table exists; the only
state is the stack.

## 6. Query complexity `[deduction]`

Computing `S(n)` makes `O(log U(n)) = O(log n)` threshold queries (one
`CanSort(∅,·)` each). In the **monotone blackbox model** — the only access to
`S(n)` is a yes/no oracle for `S(n) ≤ k` that is monotone in `k` — binary
search over the `O(n log n)`-wide window `[0, U(n)]` is optimal up to
constants, since each query is one bit and `Θ(log n)` bits are needed to
distinguish `Θ(n log n)` candidate values.

## 7. Numeric `n` vs input length `[deduction]`

The exponent `n log² n` is in **numeric `n`**, so the bound is sensitive to
encoding:

- **Unary** (`m = Θ(n)` bits): time `2^{O(m log² m)}`, space `O(m³ log m)` =
  poly. So `S_unary ∈ FPSPACE` and `SORT-BOUND-U` is decidable in deterministic
  poly-space (consistent with, and more time-specific than, the `PSPACE` bound of
  `docs/research-certificates-barriers.md` Claim A, which gives no explicit time).
- **Binary** (`bin(n) # bin(k)`): the informative case is `k ≤ U(n)`, where
  `log k = O(log n)`, so total input `N = Θ(log n)` bits and `n ≤ 2^N`. Then
  `n log² n = 2^{Θ(N)}·N² = 2^{Θ(N)}`, giving time `2^{2^{O(N)}}` and space
  `O(n³ log n) = 2^{O(N)}`. For `k ≥ U(n)` we preprocess a trivial accept
  (merge-sort witnesses `S(n) ≤ U(n)`), so such inputs need no search and do
  not affect the worst case. Hence `S_binary ∈ FEXPSPACE` and `SORT-BOUND-B` in
  deterministic `EXPSPACE` — matching Claim A. **This is not an EXPTIME result.**

## 8. Worst-case comparison with the memoized DP `[deduction]`

The memoized DP of `docs/upper-bound.md` visits **all** labelled posets
(`A001035(n) = 2^{Θ(n²)}`), including posets needing more than `S(n)`
comparisons to build. The budgeted DFS restricts to posets reachable within
`d = S(n)` comparisons — at most `(2B)^d = 2^{O(n log² n)}` distinct — and
revisits them without storing them. So the DFS's *asymptotic worst-case
upper bounds* on time (`2^{O(n log² n)}` vs `2^{Θ(n²)}`) and space
(poly vs `2^{Θ(n²)}`) are both smaller than the DP's.

This is a statement about **worst-case upper bounds only**. It is *not* a
per-instance runtime claim: on particular inputs a memoized search can be
faster (it never revisits a state), and the two algorithms are different
objects, so no dominance relation between their exact running times is
asserted. We record only that the proven worst-case bounds improve.

## 9. Edge cases `[deduction]`

- `n = 0, 1`: the empty/singleton poset is total, so `CanSort` returns `True`
  for any `d ≥ 0` and `S(0) = S(1) = 0`. The script special-cases `n ≤ 1`.
- Already-total `P`: caught by the first line, returns `True` regardless of
  remaining budget. ✓
- `k ≥ U(n)`: `CanSort(∅, k) = True` immediately (merge-sort tree witnesses it).
  The binary search never returns a value above `U(n)`. ✓
- Monotonicity in `d` (needed for binary search): more budget never hurts, so
  `CanSort(P,d) ⇒ CanSort(P,d+1)`. ✓

## 10. Experiment `[experiment]`

`scripts/budgeted_dfs.py` (pure DFS, `sys.setrecursionlimit` for depth; no
memoization in `can_sort`; a separate memoized oracle is used only to
cross-check). Run: `python3 scripts/budgeted_dfs.py --max-n 5`.

- **Values** `S(0..5) = 0,0,1,3,5,7` via DFS binary search — all match
  `scripts/evaluate.py` and the literature. `n=5` took 261,662 calls / 0.65 s.
- **Boundary** `CanSort(∅, S(n)) = True`, `CanSort(∅, S(n)-1) = False` for
  `n = 2..5` — all correct.
- **Adversarial posets** (antichain, total, chain+isolated, 2-chains, crown,
  plus random posets; `n ≤ 5`): 172 checks of `CanSort(P,d) ≡ (F(P) ≤ d)`
  against the memoized oracle — **all pass**.
- **Call counts** (empty poset, `False` answers) grow ~`2·binom(n,2)`-per-level
  and stay well below the `(2B)^d` worst case because added relations shrink the
  incomparable set with depth; the proven bound `(2B)^d` remains valid.
- **Depth** max = `d+1` frames (backtracking confirmed, §5).

No `n ≥ 6` full-value run (`CanSort(∅, S(6)=10)` would be `≥ 20^10` nodes);
`n ≤ 5` only, per the no-heavy-workload constraint.

## 11. Literature check `[literature]`+`[open]`

- The `2^{O(n²)}` DP bound is `docs/upper-bound.md` (crude ternary count);
  the `PSPACE`/`EXPSPACE` bounds are Claim A of
  `docs/research-certificates-barriers.md` (game + `APTIME = PSPACE`,
  `AEXPTIME = EXPSPACE`). Neither records a `2^{O(n log² n)}` *deterministic
  time* bound.
- The budgeted DFS is a standard, textbook decision-tree search; the bound
  `2^{O(S(n) log n)} = 2^{O(n log² n)}` is a straightforward consequence of the
  game formulation and is very likely *known* informally, but it is **not**
  written in this repository and **is** sharper than the recorded deterministic
  `2^{O(n²)}`. We record it as a `[deduction]`, not a claimed novelty.
- **Sharper bounds are not ruled out.** The `2^{O(n log² n)}` bound is the
  worst-case for *this specific* DFS (possible branching up to `2B`, depth at most `S(n)`).
  Whether a uniform algorithm can do better is open: pruning, canonicalization
  (e.g. an `S_n`-quotient DFS without a memoization table), or a decomposition
  theorem could reduce the effective branching or depth. We claim only the
  `2^{O(n log² n)}` upper bound, not optimality of the DFS `[open]`.

## 12. What this does *not* establish `[deduction]`

- No NP/coNP membership or hardness (the unary language is sparse; Mahaney
  blocks many-one NP-hardness unless `P = NP` — `docs/exploration-agenda.md`).
- No improvement to the `PSPACE`/`EXPSPACE` *space* claims (DFS is already
  poly-space unary); the contribution is the explicit deterministic *time*
  `2^{O(n log² n)}` in numeric `n`, replacing `2^{O(n²)}`.
- No lower bound; the algorithm's exponential time is not shown optimal.

## 13. Next obstacle `[open]`

§4 already shows the number of posets reachable within `S(n)` comparisons is at
most `(2B)^{S(n)} = 2^{O(n log² n)} = 2^{o(n²)}`, so the DFS explores a
`2^{o(n²)}` subset of the `2^{Θ(n²)}` posets the memoized DP materializes. The
finer open question is whether the *upper-bound exponent* `n log² n` can be reduced:
can a canonical-form DFS on the `S_n` quotient (no memoization table), a
symmetry/pruning argument, or a decomposition theorem push the worst-case below
`2^{O(n log² n)}`? The quotient's raw state count is still `2^{Θ(n²)}`, so a
better bound would need new structure, not just canonicalization.

**Reproduce:** `python3 scripts/budgeted_dfs.py --max-n 5`
