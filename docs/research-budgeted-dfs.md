# Budgeted DFS for exact S(n): a sharper deterministic time bound

**Status:** research note (paper analysis + small experiment). Not Lean-checked.
Every item is labelled `[definition]`, `[literature]`, `[deduction]`,
`[experiment]`, `[conjecture]` or `[open]`. Companion program:
`scripts/budgeted_dfs.py` (pure DFS, no memoization, no advice).

**Claim.** `S(n)` is computable by a uniform deterministic exhaustive DFS in
time `2^{O(n log^2 n)}` and space `O(n log^2 n)` **bits** (numeric `n`),
improving the recorded `2^{O(n^2)}` memoized-DP time bound of
`docs/upper-bound.md`. The space improvement is over a naive
matrix-per-frame implementation of the same DFS, which stores an `n×n`
transitive-closure bitmatrix per frame and costs `O(n^3 log n)` bits (§5); the
transcript-only implementation stores only the comparison path and decides
comparability by graph reachability. The unary threshold is decidable in
deterministic time `2^{O(n log^2 n)}` and polynomial space; the binary
threshold in time `2^{2^{O(N)}}` and space `2^{O(N)}`, where `N` is the actual
input length and `n ≤ 2^N` (see §7 for the trivial-`k` preprocessing). The
space bound is an **upper bound only** and is not claimed tight, optimal, or to
change any complexity class. No NP/hardness/optimality/class-separation claim
is made.

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

### 5.1 Naive matrix-per-frame implementation

The DFS keeps only the current recursion path. A direct implementation stores
the current poset as its `n×n` transitive-closure bitmatrix in each frame: at
most `d+1` frames, each `n²` bits plus `O(log n)` counters. On returning from a
child the frame is discarded before the next pair is tried. Hence

```
S_space^matrix(n,d) = O(d · n²) bits  ⇒  O(U(n)·n²) = O(n³ log n)  (numeric n).
```

### 5.2 Transcript-only implementation: `O(n log² n)` bits `[deduction]`

**Theorem.** The pure budgeted DFS `CanSort(∅, k)` can be implemented by a
uniform deterministic algorithm using `O((d+n) log(n+2))` bits of work space,
where `d ≤ U(n) = O(n log n)` is the budget it is called with. Consequently
`S(n)` is computable in space `O(n log² n)` bits (numeric `n`), and
`SORT-BOUND-U` is decidable in space `O(n log² n)` bits, which is polynomial in
the unary input length. This is an upper bound; no matching lower bound is
claimed.

**Representation.** A *transcript* is a sequence
`σ = ((a_1,b_1), …, (a_t,b_t))` of ordered pairs of distinct labels, read as
`a_s < b_s`. The poset it induces is `P(σ)`, the transitive closure of those
relations. The DFS state at a node is exactly `P(σ)`, where `σ` is the current
path, because `CanSort` only ever appends a relation along the path (it never
edits an earlier frame). The implementation stores `σ` — equivalently, the DFS
stack stores one comparison per frame — rather than a closure matrix.

**Work-space accounting.**

1. *Stack / transcript.* Each frame stores its comparison `(a_s,b_s)` (two
   labels in `[n]`, `2⌈log₂(n+1)⌉` bits) and a cursor into the `B = binom(n,2)`
   candidate pairs (`⌈log₂(B+1)⌉` bits). Both are `O(log n)` bits; there is no
   other per-frame data. The recursion depth is at most `d+1`, so the whole
   stack holds at most `O(d log n)` bits. All loop counters and the remaining
   budget are `O(log n)` bits and are covered by the same term.
2. *Comparability by reachability.* For labels `x,y`, `x ≺_{P(σ)} y` iff `y` is
   reachable from `x` in the digraph `([n], σ)`. Reachability is decided by
   BFS/DFS from `x` using a visited bit-vector (`n` bits) and a stack/queue of
   at most `n` labels (`O(n log n)` bits). It runs in time polynomial in `n`:
   either an adjacency list of the transcript is built/iterated once per search,
   or the transcript is scanned for the outgoing edges of each visited vertex.
   `P(σ)` is total iff for every pair `{x,y}` at least one of `x→y`, `y→x` is
   reachable.
3. *Incomparable-pair enumeration.* The cursor scans the `binom(n,2)` index
   pairs and tests comparability **on demand** with a fresh reachability search.
   No list of incomparable pairs and no `n×n` matrix is materialized, so this
   adds no storage beyond item 2.
4. *Acyclicity.* `CanSort` appends a comparison only between a currently
   incomparable pair, so the appended edge cannot close a directed cycle; `σ`
   stays acyclic and `P(σ)` is a strict partial order. This is exactly why both
   adversary answers are legal and why reachability terminates.
5. *Backtracking.* When a child returns, its frame is popped and the parent
   resumes its cursor, recomputing comparability from `σ` on demand. No child
   state is retained. Peak space is therefore the whole stack plus **one**
   reachability workspace, not one workspace per frame:
   `O(d log n) + O(n log n) = O((d+n) log(n+2))` bits. The `n log n` term is
   present for **every** call, including `d = 0`; it is *not* absorbed into
   `O(d log n)`. Only after taking `d ≤ U(n) = O(n log n)` does the whole
   expression become `O(n log² n)`. (For the *successful* calls, `d ≥ S(n) =
   Ω(n log n)` by the information bound, so there the per-call bound is
   `O(d log n)`; the binary search also makes failing calls with small `d`,
   hence the `+n` term is needed for the worst-case per-call statement.)

**Correctness.** Reachability computes exactly the transitive closure that the
matrix implementation stores, so `is_total`, `incomparable_pairs` and the
recursion are the same predicates on the same `P(σ)`; the induction of §3 gives
correctness unchanged.

**Time overhead.** Recomputing comparability per node costs time polynomial in
`n` (a polynomial number of reachability searches, each polynomial in `n`)
instead of the matrix implementation's `O(n²)`. This is a factor `poly(n)`,
which is absorbed by the node count `(2B)^d = 2^{O(d log n)}`: the total time
bound `2^{O(n log² n)}` of §4 is unchanged. No time improvement is claimed.

**Input encodings.** For `SORT-BOUND-U`, `n ≤ m = n+k+1`, so `O(n log² n)` bits
is polynomial in `m`. For `SORT-BOUND-B`, `n ≤ 2^N` for the actual input length
`N = |bin n| + |bin k| + O(1)`, so the space is `O(2^N·N²) = 2^{O(N)}` bits,
i.e. `EXPSPACE` (the `Θ(log n)` description holds only on the nontrivial
instances `k ≤ U(n)` selected by the preprocessing in §7). Neither bound changes
the class memberships established elsewhere; only the polynomial degree of the
unary work-space bound is lowered.

`[experiment]` Instrumenting `scripts/budgeted_dfs.py` confirms the maximum
recursion depth equals `d+1` for all `n ≤ 5`, `d ≤ 5` (e.g. `n=5, d=5` → depth
6), i.e. `O(d)` frames, **not** `(2B)^d`. No memoization table exists; the only
state is the stack. The transcript-only evaluator `scripts/transcript_dfs.py`
additionally records the maximum stored path length (equal to the depth) and
prints the bit accounting of §5.2. To realise the accounting it keeps a single
shared mutable transcript (append on descent, pop on return), never copies the
transcript per frame, materialises no incomparable-pair list, and allocates and
releases the reachability workspace inside a non-recursive helper before any
child call. The regression test `tests/test_transcript_dfs.py` reproduces
`S(0..5)` and agrees with the memoized minimax oracle on **all** `3/19/219`
labelled posets for `n = 2,3,4`.

### 5.3 What the space bound does *not* say

- It is an upper bound. No lower bound, tightness or optimality is claimed. In
  particular, this note does not assert that `O(n log² n)` bits is necessary,
  nor that storing a comparison path is the only way to decide the game.
- It does not improve the *time* bound, and it does not separate complexity
  classes: `SORT-BOUND-U` was already known to be in `PSPACE` and is already
  polynomial-space; the contribution is the smaller polynomial.
- It is lost if an implementation materializes an `n×n` closure matrix or the
  incomparable-pair list per frame.

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

- **Unary** (`m = n+k+1` bits, `n ≤ m`): time `2^{O(m log² m)}`, space
  `O(n log² n) = O(m log² m)` bits by §5.2 (the matrix-per-frame version costs
  `O(m³ log m)`), which is poly. So `S_unary ∈ FPSPACE` and `SORT-BOUND-U` is
  decidable in deterministic poly-space (consistent with, and more time-specific
  than, the `PSPACE` bound of `docs/research-certificates-barriers.md` Claim A,
  which gives no explicit time).
- **Binary** (`bin(n) # bin(k)`): first test `k ≥ U(n) = O(n log n)` and accept
  immediately (merge-sort witnesses `S(n) ≤ U(n)`), so the search runs only on
  nontrivial instances with `k ≤ U(n)`. There `log k = O(log n)` and the input
  length is `N = |bin n| + |bin k| + O(1) = Θ(log n)`; unconditionally
  `n ≤ 2^N`. Then `n log² n = 2^{Θ(N)}·N² = 2^{Θ(N)}`, giving time
  `2^{2^{O(N)}}` and space `O(n log² n) = 2^{O(N)}` (the matrix-per-frame
  version costs `O(n³ log n)`, the same `2^{O(N)}` class). Hence
  `S_binary ∈ FEXPSPACE` and `SORT-BOUND-B` in deterministic `EXPSPACE` —
  matching Claim A. **This is not an EXPTIME result.** The trivial-accept step
  matters because for unbounded `k` the raw input length is not `Θ(log n)`; the
  class statement itself is unconditional via `n ≤ 2^N`.

### 7.1 Dense-matrix `GEN-SORT` in sublinear space `[deduction]`

The same transcript-only DFS applies to the **generalized** dense-matrix
language of `docs/research-hardness-boundaries.md` §0:
`GEN-SORT = { ⟨P⟩ # bin(k) : S(P) ≤ k }`, where `⟨P⟩` is an explicit labelled
`n×n` directed comparability matrix with `n` in a header, so the input length is
`N = Ω(n²)`. Suppose `⟨P⟩` is supplied on a **read-only input tape** (the
standard Turing-machine space model, in which input cells are not counted as
work space) and accessed by indexed queries: `P` therefore contributes `0` to
the counted work space, and the only cost associated with reading it is the
`O(log N)`-bit input head position. (If input cells were counted as work space,
the bound would be the trivial `O(N)`.)

> **Corollary.** `GEN-SORT` is decidable in deterministic work space
> `O(n log² n) = O(√N · log² N)` bits — **sublinear** in `N` — with the same
> time bound `2^{O(n log² n)} = 2^{O(√N log² N)}` as the matrix-encoded
> budgeted DFS. This is an upper bound only.

*Proof.* Run the DFS of §5.2 with the initial poset `P` read from the input
instead of the empty order.

- **Stack.** Only the sorter's transcript `σ` of added comparisons is stored on
  the work tape: `O(d log n)` bits with `d ≤ U(n) = O(n log n)` after clamping
  `k` (`k ≥ U(n)` is a trivial accept; the information bound covers the
  trivial-no region). The matrix `P` is never copied to a work tape.
- **Comparability.** `x ≺ y` in the current knowledge iff `y` is reachable from
  `x` in the digraph with edges (i) the input relations `P(i,j)` and (ii) the
  transcript edges. Transcript edges are on the work stack; input edges `(u,j)`
  are found by scanning row `u` of the read-only input via indexed queries.
  One reachability search uses a visited bit-vector (`n` bits) and a
  queue/stack of at most `n` labels (`O(n log n)` bits), plus an `O(log N)`-bit
  input head position, and runs in time polynomial in `n`.
- **Enumeration and backtracking.** Incomparable pairs are enumerated on demand
  over the `binom(n,2)` index pairs, each tested by a fresh reachability search;
  no `n×n` matrix and no pair list is materialized, and child frames are popped
  on return, so only **one** reachability workspace exists at a time.
- **Well-formedness.** Indexed queries check irreflexivity/antisymmetry in
  `O(n²)` time and transitivity in `O(n³)` time, in `O(log N)` work space;
  invalid encodings are rejected there.

Peak work space is the stack `O(d log n)` plus one reachability workspace
`O(n log n)`, i.e. `O((d+n) log(n+2))` bits. With `d ≤ U(n) = O(n log n)` this
is `O(n log² n)` bits. Since `N = Ω(n²)` we have `n = O(√N)` and
`n log² n = O(√N log² N) = o(N)`, so the bound is sublinear. The per-node
reachability overhead is `poly(n)`, absorbed by the node count
`2^{O(n log² n)}`, so the time bound is unchanged. ∎

**Assumptions.** (a) Read-only input tape, input cells not counted as work
space (standard); `P` stays on the input tape and is never copied, so the
`O(√N log² N)` work-space bound excludes it (counting the input would give the
trivial `O(N)`). (b) `P` is given as a **transitive comparability matrix**
(`P(i,j)=1` iff `i ≺ j`, so the relation is irreflexive, antisymmetric and
transitive); the well-formedness check of the proof enforces this, and
reachability over it returns the same relation. (c) `k` is clamped to
`O(n log n)`. (d) The time overhead is polynomial per search node. This refines
the `GEN-SORT ∈ PSPACE ∩ EXPTIME` statement of
`docs/research-hardness-boundaries.md` Remark 1.5 to
`GEN-SORT ∈ DSPACE(O(√N log² N)) ∩ DTIME(2^{O(√N log² N)})` for the dense-matrix
encoding. It is **encoding-specific** and a space upper bound only: no hardness,
completeness, class separation, tightness, or time improvement is claimed. For
a sparse edge-list encoding with binary `n`, `N = O(log n)` and the same method
gives only the exponential-space bound recorded there.

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
- The `O(n log² n)`-bit space accounting of §5.2 is also standard in substance:
  a poset can be represented by a generating relation (here the comparison
  transcript) and its comparability decided by graph reachability, and
  reachability itself is in `NL` (hence in deterministic `O(log² n)` space by
  Savitch's theorem; a plain BFS uses a visited bit-vector plus a queue of at
  most `n` labels, `O(n log n)` bits). With BFS, the per-call accounting is the
  transcript plus one reachability workspace, `O((d+n) log(n+2))`; a
  Savitch-based reachability could remove the `+n` term at the cost of
  quasi-polynomial time per query (still absorbed). We record this as a
  `[deduction]`, not as a novelty, and claim no tightness.
- **Sharper bounds are not ruled out.** The `2^{O(n log² n)}` time bound is the
  worst-case for *this specific* DFS (possible branching up to `2B`, depth at
  most `S(n)`). Whether a uniform algorithm can do better is open: pruning,
  canonicalization (e.g. an `S_n`-quotient DFS without a memoization table), or
  a decomposition theorem could reduce the effective branching or depth. We
  claim only the `2^{O(n log² n)}` upper bound, not optimality of the DFS
  `[open]`. Likewise the `O(n log² n)`-bit space bound is not shown optimal.

## 12. What this does *not* establish `[deduction]`

- No NP/coNP membership or hardness (the unary language is sparse; Mahaney
  blocks many-one NP-hardness unless `P = NP` — `docs/exploration-agenda.md`).
- No *class* improvement to the `PSPACE`/`EXPSPACE` space claims: the DFS was
  already polynomial-space unary, and §5.2 only lowers the polynomial degree
  (from `O(n³ log n)` to `O(n log² n)` bits); the sublinear-space `GEN-SORT`
  corollary of §7.1 is likewise an upper bound within `PSPACE`. The
  deterministic *time* contribution remains `2^{O(n log² n)}` in numeric `n`,
  replacing `2^{O(n²)}`.
- No lower bound; the algorithm's exponential time is not shown optimal, and
  neither the time nor the `O(n log² n)`-bit space bound is shown tight.

## 13. Next obstacle `[open]`

§4 already shows the number of posets reachable within `S(n)` comparisons is at
most `(2B)^{S(n)} = 2^{O(n log² n)} = 2^{o(n²)}`, so the DFS explores a
`2^{o(n²)}` subset of the `2^{Θ(n²)}` posets the memoized DP materializes. The
finer open question is whether the *upper-bound exponent* `n log² n` can be reduced:
can a canonical-form DFS on the `S_n` quotient (no memoization table), a
symmetry/pruning argument, or a decomposition theorem push the worst-case below
`2^{O(n log² n)}`? The quotient's raw state count is still `2^{Θ(n²)}`, so a
better bound would need new structure, not just canonicalization. On the space
side, whether `SORT-BOUND-U` can be decided in `o(n log² n)` bits, or whether
some compression avoids storing the full comparison path, is open; §5.2 gives
only an upper bound and makes no tightness claim.

**Reproduce:** `python3 scripts/budgeted_dfs.py --max-n 5`;
`python3 scripts/transcript_dfs.py --max-n 5`;
`python3 -m unittest tests.test_transcript_dfs -v`.
