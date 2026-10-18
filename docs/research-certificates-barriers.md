# Succinct certificates and complexity barriers for evaluating S(n)

**Status:** research note (paper-and-literature analysis plus one small
experiment). It is **not** Lean-checked. Every item is labelled
`[literature]`, `[deduction]`, `[experiment]`, `[conjecture]` or `[open]`.
No new Lean files, no commits.

This note responds to mandate M-019 (FRONT: succinct certificates and
complexity barriers). It supersedes nothing in `problem.md`; in particular
the deterministic upper bounds there are correct but **not tight** (see
Claim A below).

---

## 0. Model and encodings (fixed once, used throughout)

`[literature]`/definition. From `docs/problem.md`:

- `S(n)` = minimum height (worst-case number of pairwise comparisons) of a
  **deterministic adaptive comparison decision tree** that correctly sorts
  every permutation of `n` distinct labelled keys.
- `SORT-BOUND-U = { 1^n # 1^k : S(n) ≤ k }` — both parameters **unary**.
- `SORT-BOUND-B = { bin(n) # bin(k) : S(n) ≤ k }` — both parameters **binary**.
- Input length: for `SORT-BOUND-U`, `m = n + k + 1`; for `SORT-BOUND-B`,
  `m = Θ(log n + log k) = Θ(log n)` (since `k ≤ n(n-1)/2`).
- `S(n) ∈ [ ⌈log₂ n!⌉ , n log₂ n ]`; the interval has width `O(n)` in
  numeric `n`. Hence the only informative `k` lie in a window of `O(n)`
  consecutive integers.
- `SORT-BOUND-U ∈ P` iff `S_unary ∈ FP`; the same holds for the binary
  encoding (`problem.md`, by binary search against the merge-sort bound).
  `[deduction]`
- **Fixed sorting networks** (oblivious comparator sequences) are a
  different object: they are *not* adaptive trees and their minimal
  size/depth sequence is a different sequence from `S(n)`. `[literature]`

The key structural identity used below: a height-`≤k` correct tree is
exactly a *winning strategy* of the sorter in the following finite game.

> **Game `G(n,k)`.** State = a transitively closed partial order `P` on `n`
> labelled elements. Start at the empty (antichain) order. While `P` is not
> total and fewer than `k` comparisons have been made: the **sorter** picks
> an incomparable pair `{x,y}`; the **adversary** answers `x<y` or `y<x`;
> replace `P` by its transitive closure. Sorter wins iff a total order is
> reached within `k` comparisons.
>
> `S(n) ≤ k` iff the sorter wins `G(n,k)`. `[deduction]`

---

## 1. Precise question

1. **Upper-bound certificate.** What could a certificate for `S(n) ≤ k`
   look like that is *polynomially checkable in the input length* and does
   **not** explicitly list an exponential-size sorting tree? Is there any
   succinct (polynomial) witness at all?
2. **Lower-bound certificate.** What would a certificate for `S(n) > k`
   require? Can the information-theoretic bound `⌈log₂ n!⌉` be extended to
   a succinct witness in the hard regime `k ≥ ⌈log₂ n!⌉`?
3. **Classification.** What is the strongest defensible complexity claim
   for `SORT-BOUND-U` and `SORT-BOUND-B` (membership and non-membership),
   keeping unary vs binary input length and adaptive-tree vs network
   explicitly separate?

---

## 2. Sources (precise, with model noted)

- L. Hyafil, R. L. Rivest, *Constructing optimal binary decision trees is
  NP-complete*, Inform. Process. Lett. **5**(1) (1976) 15–17,
  doi:10.1016/0020-0190(76)90095-8. **Model:** arbitrary tests, minimize
  expected (and, same construction, worst-case) number of tests.
  `[literature]`
- E. S. Laber, L. T. Nogueira, *On the hardness of the minimum height
  decision tree problem*, Discrete Appl. Math. **144**(1–2) (2004) 209–212,
  doi:10.1016/j.dam.2004.06.002. **Result:** minimum-height decision trees
  are NP-hard even to approximate within `o(log n)`. **Model:** arbitrary
  tests, worst-case height. `[literature]`
- I. Parberry, *Single-exception sorting networks and the computational
  complexity of optimal sorting network verification*, Math. Systems Theory
  **23** (1990) 81–93; and *On the computational complexity of optimal
  sorting network verification*, LNCS **506** (1991) 252–269.
  **Result:** `NONSORT` (does a given comparator network sort?) is
  NP-complete, so sorting-network verification is coNP-complete. **Model:**
  *fixed* comparator networks, zero-one principle. `[literature]`
- A. K. Chandra, D. C. Kozen, L. Stockmeyer, *Alternation*, J. ACM
  **28**(1) (1981) 114–133, doi:10.1145/322234.322243. **Result:**
  `APTIME = PSPACE` and `AEXPTIME = EXPSPACE` (Corollary 3.6).
  `[literature]`
- S. R. Mahaney, *Sparse complete sets for NP*, J. Comput. System Sci.
  **25**(2) (1982) 130–143, doi:10.1016/0022-0000(82)90002-2. **Result:**
  a sparse NP-hard set under polynomial-time many-one reductions implies
  `P = NP`; under Turing reductions the polynomial hierarchy collapses to
  `Δ₂P` (Ogiwara–Watanabe, SICOMP **20**(3) (1991) 471–483).
  `[literature]`
- G. Brightwell, P. Winkler, *Counting linear extensions is #P-complete*,
  STOC 1991, doi:10.1145/103418.103441. They explicitly remark that easy
  counting of linear extensions would let one determine the optimum next
  comparison. `[literature]`
- J. Kahn, M. Saks, *Every poset has a good comparison*, STOC 1984,
  doi:10.1145/800057.808694: `3/11 ≤ p(x<y) ≤ 8/11`; constant-factor
  tightness of the information bound. J. Kahn, J. H. Kim, *Entropy and
  sorting*, J. Comput. System Sci. **51**(3) (1995) 390–399: poly-time
  constant-factor algorithm. J. Cardinal, S. Fiorini, G. Joret,
  R. M. Jungers, J. I. Munro, *Sorting under partial information (without
  the ellipsoid algorithm)*, Combinatorica **33**(6) (2013) 655–697.
  M. L. Fredman, *How good is the information theory bound in sorting?*,
  Theoret. Comput. Sci. **1**(4) (1976) 355–361. `[literature]`
- Exact sorting numbers: Wells (1965) `S(12)=30`; Kasai et al. (1994)
  `S(13)=34`; M. Peczarski, *New results in minimum-comparison sorting*,
  Algorithmica **40** (2004) 133–145, and *Towards optimal sorting of 16
  elements*, Acta Univ. Sapientiae Inform. **4**(2) (2012) 215–224;
  F. Stober, A. Weiß, *Lower bounds for sorting 16, 17, and 18 elements*,
  arXiv:2206.05597 (2022) — `S(16)=46, S(17)=50, S(18)=54`, and
  `S(28) ≥ 99`. Jing et al. report `S(15)=42, S(19)=58`. OEIS A036604.
  `[literature]`
- OEIS A001035 (labelled posets `1,3,19,219,4231,130023,6129859,…`) and
  D. Kleitman, B. Rothschild, *Asymptotic enumeration of partial orders on
  a finite set*, Trans. AMS **205** (1975) 205–220: labelled posets number
  `2^{Θ(n²)}`. `[literature]`

---

## 3. What is actually known (literature facts)

- `[literature]` `S(n) = ⌈log₂ n!⌉` for `n ≤ 11` and `n = 20, 21`; the
  information bound is **not** tight in general (`S(12)=30 > 29`). Exact
  `S(n)` is known only for `n ≤ 22` (and `S(28) ≥ 99`). For `n ≥ 23` the
  value is open; the asymptotics of the "excess" `S(n) − log₂ n!` are
  open. There is **no** known polynomial-time algorithm computing `S(n)`.
- `[literature]` Optimal decision-tree construction with arbitrary tests is
  NP-complete (Hyafil–Rivest) and min-height is NP-hard to approximate
  within `o(log n)` (Laber–Nogueira). Sorting-network verification is
  coNP-complete (Parberry). **None of these is a statement about `S(n)`.**
- `[literature]` For sorting a *given* poset `P`, `log₂ e(P) ≤ S(P) ≤
  c·log₂ e(P)` with `c` a small constant (Kahn–Saks; Kahn–Kim; Cardinal et
  al.). The exact optimum `S(P)` is not known to be polynomial-time
  computable; counting `e(P)` is #P-complete, and Brightwell–Winkler note
  that a poly-time exact `e(P)` would immediately yield the optimal next
  comparison.
- `[literature]` `APTIME = PSPACE`, `AEXPTIME = EXPSPACE`
  (Chandra–Kozen–Stockmeyer). Mahaney: sparse NP-hard ⇒ `P = NP`.

---

## 4. Candidate claims with evidence and proof sketches

### Claim A (upper bounds; **improves** `docs/upper-bound.md`). `[deduction]`

> `SORT-BOUND-U ∈ PSPACE` and `SORT-BOUND-B ∈ EXPSPACE`.

**Proof sketch.** Decide `G(n,k)` with an alternating Turing machine. The
ATM keeps the current poset as an `n×n` ternary matrix (space `O(n²)`).
Each round: existentially guess an incomparable pair (`2 log n` bits),
universally branch on the two outcomes, and update the transitive closure
in `O(n²)` time; repeat while the order is not total and the budget `k` is
not exhausted; at the end check totality.

- **Unary.** `m = n + k + 1`, so `n ≤ m`, `k ≤ m` and the ATM runs in time
  `O(k·n²) = O(m³)`, i.e. `ATIME(poly(m)) = APTIME = PSPACE`.
- **Binary.** `m = Θ(log n)`, so `n = 2^{Θ(m)}` and (unless `k` is trivially
  large, in which case accept immediately) `k = O(n log n) = 2^{Θ(m)}`.
  The ATM runs in time `2^{Θ(m)}`, i.e. `ATIME(2^{O(m)}) ⊆ DSPACE(2^{O(m)})
  = EXPSPACE`.

Because `PSPACE ⊆ EXPTIME` and `EXPSPACE ⊆ 2-EXPTIME`, Claim A strictly
improves the `EXPTIME`/`2-EXPTIME` bounds recorded in `upper-bound.md`.
(The old bounds are not wrong; they are just weaker. The old bound came
from materializing the whole poset DP, which visits **all** labelled
posets — see §5.) Both `PSPACE` and `EXPSPACE` are closed under
polynomial-time Turing reductions, so `S_unary ∈ FPSPACE` and
`S_binary ∈ FEXPSPACE` follow by binary search on `k`.

**What this does *not* say.** It gives no NP/coNP membership and no
hardness. In particular `APTIME = PSPACE` needs the *polynomially many*
alternations supplied by the unary horizon; the binary horizon is
exponential, which is exactly why the binary case lands in `EXPSPACE` and
not `PSPACE`.

### Claim B (sparsity barrier; unary only). `[literature]` + `[deduction]`

> `SORT-BOUND-U` is sparse. Consequently it is not NP-hard under
> polynomial-time many-one reductions unless `P = NP`; under polynomial-
> time Turing reductions, NP-hardness would collapse the polynomial
> hierarchy to `Δ₂P` (Ogiwara–Watanabe). `SORT-BOUND-B` is **not** sparse,
> so Mahaney's barrier does **not** apply to it.

**Proof sketch.** For total length `≤ m` the unary encoding admits at most
`O(m²)` pairs `(n,k)`, so `SORT-BOUND-U` is sparse. For the binary
encoding, put `U(n) = n⌈log₂(n+1)⌉`, a valid merge-sort upper bound on
`S(n)`. For large `m`, choose each `n` in
`[2^{m/4-1}, 2^{m/4}]` (round endpoints to integers) and each `k` in
`[U(n), 2U(n)]`. **Every one of these strings belongs to the language**
because `k ≥ U(n) ≥ S(n)`. Their encodings have total length
`≤ m/4 + O(1) + m/4 + O(log m) < m` for sufficiently large `m`.
There are `2^{Ω(m)}` such pairs, so `SORT-BOUND-B` is not sparse.
Unlike a count of `k` in the *uncertain* window between the information
bound and the sorting upper bound, this counts guaranteed **yes** inputs. ∎

This is the sharpest *difference* between the two encodings: the binary
threshold language is a genuine dense language and is not blocked by the
sparse-set barrier.

### Claim C (no succinct tree certificate; size of explicit witnesses). `[deduction]` + `[experiment]`

> Every correct comparison tree for `n` keys must distinguish all `n!`
> permutations, so it has **at least** `n!` distinct *reachable* leaves
> and at least `2·n! − 1` nodes (comparison trees are full binary trees).
> A non-reduced tree may have more leaves, including unreachable ones.
> Pruning comparisons with only one feasible outcome produces a reduced
> correct tree with exactly `n!` leaves and `2·n! − 1` nodes.
> Thus an explicit tree witness need not be polynomial-sized:
> - on informative **unary** inputs, with `S(n) ≤ k ≤ n⌈log₂(n+1)⌉`,
>   the input length is `m=n+k+1=Θ(n log n)`, so `n!=2^{Θ(m)}`;
> - on informative **binary** inputs, `m=Θ(log n)`, so
>   `n!=2^{2^{Θ(m)}}`.
> For trivially large `k`, acceptance needs no explicit tree.
>
> The standard full-tree certificate can be verified in time polynomial
> **in its own size**, not polynomial in the original input length.
> It therefore yields at most a naive `NEXP` (unary) /
> `N2EXP` (binary) verifier, not an `NP` proof. This does **not**
> preclude an entirely different succinct certificate.

**Proof sketch.** A deterministic tree sends each input permutation to
exactly one reached leaf. Distinct permutations cannot share a reached
leaf in a correct sorting tree, because the same leaf output cannot sort
both, so at least `n!` leaves are reached. For a full binary tree,
`nodes = 2·leaves − 1`. For a *reduced* tree, at each comparison
node both outcomes are possible under the path constraints; whenever
only one outcome is feasible, remove that node and retain the feasible
subtree. This does not increase the height or compromise correctness,
and after pruning every leaf is reached by exactly one permutation,
so there are exactly `n!` leaves. For verification, check feasibility
of each path's comparisons (acyclicity) and, on each feasible path, that
their transitive closure determines a unique total order and that the
leaf's output is correct. This is polynomial in `n` and the explicit
tree size. The experiment confirms the *reduced optimal* count for
`n ≤ 6`; it does not claim all possible trees have that size. ∎

**Candidate succinct forms, and their status:**

| Candidate witness for `S(n) ≤ k` | Checkability | Size | Status |
|---|---|---|---|
| explicit adaptive tree | poly in tree size | at least `2n!−1`; achievable after pruning | not polynomial; `[deduction]` |
| DAG / branching-program compression | poly in DAG size | `≥ #` distinct reachable posets | worst case `2^{Θ(n²)}`; no poly bound `[open]` |
| program computing the strategy | not known poly (universal over `n!` inputs) | poly possible | `[open]` |
| inductive invariant / potential | not known | ? | `[open]`; information bound is the only known potential and it is not tight |
| non-uniform advice `S(n)` per length | — | `2^{Θ(m)}` bits (one value per `n`) | trivial advice is exponential `[deduction]` |

### Claim D (general hardness does **not** transfer). `[deduction]`

> The NP-completeness of optimal decision-tree construction
> (Hyafil–Rivest), the `o(log n)` inapproximability of minimum-height
> decision trees (Laber–Nogueira), and the coNP-completeness of
> sorting-network verification (Parberry) are **not** theorems about
> `SORT-BOUND-U`/`SORT-BOUND-B`.

Reasons, one per result:

- Hyafil–Rivest / Laber–Nogueira use **arbitrary tests** and an arbitrary
  test/item incidence structure. `S(n)` fixes the test set to all pairwise
  comparisons and the item set to `S_n`; the instance is the single
  parameter `n`. No reduction is known and none is implied.
- The sparse-set barrier (Claim B) shows that a many-one NP-hardness proof
  for the **unary** language would prove `P = NP`, so such a proof cannot
  be routine.
- Parberry's result is about **fixed networks** (`∀` inputs, zero-one
  principle, coNP). Adaptive trees existentially choose the next
  comparison; that extra quantifier is exactly what turns the problem from
  coNP-shaped into a game (Claim A). The two models must not be conflated.

### Claim E (counting barrier). `[literature]` + `[deduction]`

> The natural "greedy-optimal" comparison rule (choose `{x,y}` minimizing
> `max(e(P+xy), e(P+yx))`) requires counting linear extensions `e(P)`, which
> is #P-complete (Brightwell–Winkler), so this specific route to an optimal
> strategy is not known to be polynomial. This is a barrier to a *specific*
> algorithmic route, **not** a hardness theorem for `S(n)` or for exact
> optimal comparison selection.

---

## 5. Experiment (falsification / size accounting)

Small script (kept out of the repository; reproduced here) computing, for
`n ≤ 6`, (i) the number of distinct partial orders visited by the memoized
minimax recurrence of `upper-bound.md`, and (ii) the node/leaf count of an
optimal tree.

```
 n  S(n)  reachable posets        n!        2^S   3^(n(n-1)/2)
 1     0                 1         1          1              1
 2     1                 3         2          2              3
 3     3                19         6          8             27
 4     5               219        24         32            729
 5     7              4231       120        128          59049
 6    10            130023       720       1024       14348907

 n  height  nodes  leaves        n!
 1       0      1       1          1
 2       1      3       2          2
 3       3     11       6          6
 4       5     47      24         24
 5       7    239     120        120
 6      10   1439     720        720
```

- `[experiment]` The reachable-poset counts `1, 3, 19, 219, 4231, 130023`
  are exactly OEIS **A001035** (all labelled posets on `n` elements). So
  the memoized DP of `upper-bound.md` enumerates **every** labelled poset;
  the crude `3^{n(n-1)/2}` count is not the bottleneck — the true state
  count is `2^{Θ(n²)}` (Kleitman–Rothschild).
- `[experiment]` `nodes = 2·n! − 1` exactly for `n ≤ 6`, confirming
  Claim C's witness-size accounting. `leaves = n!`.
- `[experiment]` `n! ≤ 2^{S(n)}` always (information bound), with slack
  growing: for `n=6`, `720 ≤ 1024`; the slack is the non-tightness that
  first bites at `n=12`.

No finite computation here proves a complexity separation; the experiment
only calibrates witness sizes and the DP state space.

---

## 6. Known vs conjectured vs open

| Statement | Status |
|---|---|
| `SORT-BOUND-U ∈ PSPACE`, `SORT-BOUND-B ∈ EXPSPACE` | `[deduction]` Claim A |
| `SORT-BOUND-U` sparse; not many-one NP-hard unless `P=NP` | `[literature]`+`[deduction]` Claim B |
| `SORT-BOUND-B` not sparse; Mahaney inapplicable | `[deduction]` Claim B |
| reduced explicit tree has `2n!−1` nodes; general tree may be larger | `[deduction]`+`[experiment]` Claim C |
| general decision-tree/network hardness does not transfer | `[deduction]` Claim D |
| exact `S(n)` known for `n ≤ 22`; open for `n ≥ 23`; asymptotics open | `[literature]` |
| `SORT-BOUND-U ∈ P` (i.e. `S` poly-time computable) | `[open]`; no poly algorithm known, widely doubted |
| `SORT-BOUND-B ∈ P` | `[open]` |
| `SORT-BOUND-U ∈ NP` or `∈ coNP` | `[open]`; no succinct certificate known |
| `SORT-BOUND-B ∈ NP` or `∈ coNP` | `[open]`; Mahaney gives no obstruction |
| `SORT-BOUND-U` or `-B` hard for `NP`/`PSPACE`/`EXPSPACE` | `[open]`; unary many-one hardness would give `P=NP` |
| poly-size certificate for `S(n) ≤ k` or `S(n) > k` | `[open]`; none known (Claim C) |
| `S(n)` determined by `e(P)` (or by entropy) alone | `[conjecture, likely false]`; not tested here |

---

## 7. Strongest defensible complexity claim (summary)

> **Theorem (informal, deduction).** `SORT-BOUND-U ∈ PSPACE` and
> `SORT-BOUND-B ∈ EXPSPACE`. The unary language is sparse and cannot be
> NP-hard under polynomial-time many-one reductions unless `P = NP`; the
> binary language is not sparse and no such barrier applies. Neither
> language is known to be in `NP` or `coNP`, and neither is known hard for
> any class above `P`. The natural explicit witness (a sorting decision
> tree) has `2·n! − 1` nodes — super-polynomial in the unary input length
> and doubly exponential in the binary input length — so the obvious
> nondeterministic certificate does not establish `NP` membership.

Proof sketches are Claims A–E. The improvement over `docs/upper-bound.md`
is the replacement of `EXPTIME`/`2-EXPTIME` by `PSPACE`/`EXPSPACE`, via the
game formulation `G(n,k)` and `APTIME = PSPACE` /
`AEXPTIME = EXPSPACE`.

---

## 8. Next unresolved obstacle

The central obstruction is **the absence of any succinct certificate in
either direction**, and its likely cause is the *absence of a compact
canonical object* describing optimal comparison play:

1. **Upper bound.** We need a polynomial-size object from which the
   existence of a height-`k` tree follows, checkable in polynomial time.
   The standard known witness is a reduced comparison tree of size `2n!−1`. A
   plausible route is a *canonical branching program / DAG* whose states
   are reachable posets; its worst-case size is the number of labelled
   posets (`2^{Θ(n²)}`), and it is **open** whether optimal play confines
   the DAG to polynomially many states. Testing this requires measuring
   the number of *distinct states on optimal plays* (not all reachable
   states) for `n = 7…10`, which is a concrete next experiment.
2. **Lower bound.** For `k ≥ ⌈log₂ n!⌉` (e.g. `n=12, k=29`) no succinct
   witness for `S(n) > k` is known; the published proofs are exhaustive
   searches over posets (Wells, Peczarski, Stober–Weiß). A polynomial
   certificate would likely require a new potential function stronger than
   `log₂ e(P)`, which does not exist yet (this is the same gap as
   non-tightness of the information bound).
3. **Classification.** The `PSPACE`/`EXPSPACE` upper bounds leave a large
   gap to the only known lower bounds (trivial decidability and the
   sparse-set barrier). The specific obstacle to closing it is that `S(n)`
   is a *single-parameter family*: no known reduction exploits the
   symmetric, fixed-test-set structure, and the unary sparse-set barrier
   rules out the most direct many-one route to NP-hardness.

**Smallest compelling next step (non-Lean):** instrument the minimax
search to record, for each `n ≤ 10`, the number of distinct poset states
that lie on *some* height-`S(n)` optimal play (the "optimal-play state
count"), and compare it to `n!`, to A001035, and to `poly(n)`. If that
count is polynomially bounded, a succinct certificate route becomes
plausible; if it matches the full poset count, it is strong evidence
against succinct tree/DAG certificates. Either outcome is a useful,
falsifiable research result.
