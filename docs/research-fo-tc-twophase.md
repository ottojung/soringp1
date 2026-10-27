# Two-phase compositional barrier for exact-budget strategy programs

**Status:** proved small no-go lemma (paper proof) + exact executable
witnesses, independently auditable, not Lean-checked. **Model:** adaptive
comparison sorting of `n` distinct keys; `S(n)` is the optimal worst-case
comparison count (`docs/problem.md`). Coordinates with Antonina fervor
(FO(TC) strategy programs) and umbrella #301.

## Sharp question

Is there a *single* compositional program schema -- sort `n-1` keys, then
insert the last key -- that achieves the exact optimal budget `S(n)` for
every `n`? A YES would give the uniform-completeness shape the FO(TC)
program conjecture needs; a NO at any `n` forces every complete program
family to switch shapes with `n`.

## Lemma (PROVED, paper proof): strict two-phase lower bound

**[deduction]** A deterministic adaptive program that (phase 1) fully
determines the order of `n-1` fixed keys and (phase 2) then compares only
the remaining key against that sorted chain uses at least
`S(n-1) + ceil(log2(n))` comparisons worst-case.

*Proof.* Phase-1 cost depends only on the relative order of the `n-1`
keys, and some such order forces at least `S(n-1)` comparisons (definition
of `S`). Fix a program path attaining that cost; the remaining uncertainty
is only the rank of the last key among `n` slots. Phase 2 is therefore a
fixed binary decision tree with at least `n` leaves, hence height at least
`ceil(log2(n))`, attained on some rank. The adversary combines the
worst-case `(n-1)`-order with the worst-case rank independently, forcing at
least `S(n-1) + ceil(log2(n))` total. QED.

This rules out the one natural uniform compiler route (optimal-substructure
recurrence compilation); it does not bound general-root-optimal programs,
selective search, or state compression.

## Theorem (PROVED, paper proof): two-phase worst case is exactly `S(n-1) + ceil(log2 n)`, exactness fully characterized

**[deduction]** For every `n ≥ 2`, the optimal strict two-phase program has
worst case exactly `S(n-1) + ceil(log2(n))`, and it is exact-budget (worst
case `= S(n)`) **iff** `S(n) = S(n-1) + ceil(log2(n))`.

*Proof.* "≥" is the Lemma above.  For "≤": run any optimal `(n-1)`-key
sorting tree in phase 1 (cost `S(n-1)`); afterwards the only uncertainty is
the loose key's rank `r ∈ {1..n}`.  A phase-2 comparison of the loose key
against the `p`-th smallest chain element is a threshold query splitting the
unresolved rank interval: on a node whose unresolved ranks form a contiguous
interval `{a..b}` with `a < b`, asking chain position `p` with `a ≤ p < b`
answers `loose < p-th` (ranks `{a..p}`) or `≥` (ranks `{p+1..b}`).  Taking
`p` at any interior split point of the interval realizes every full binary
tree on the `n` ordered gaps; a complete such tree of height exactly
`ceil(log2 n)` exists since `2^ceil(log2 n) ≥ n`.  Phase 1's worst order and
phase 2's worst rank are chosen independently, so the worst case is the
sum.  QED.

*Consequence.* Strict two-phase exactness at `n` is a pure arithmetic
question about the increments `d(n) = S(n) - S(n-1)` versus
`ceil(log2 n)`, one at a time.  All-`n` exactness of the compositional
schema would require `d(n) = ceil(log2 n)` for every `n ≥ 2`.

## Finding: exactness classification over the known range (n ≤ 22)

**[literature + deduction]** Exact `S(n)` is known for all `n ≤ 22`
(Wells 1965 for 12; Peczarski 2002/2004 for 13-15; the pre-2023 works cover
15 and 19-22; Stober-Weiß ALENEX 2023 prove 46, 50, 54 for 16, 17, 18; the
full list is indexed as OEIS A036604).  Combined with the characterization
theorem (_vc-checks: `tests/test_twophase_independent_check.py`):

| `n` | hit (`d(n) = ceil(log2 n)`) | miss |
|---|---|---|
| 2-4 | 2, 3, 4 | |
| 5 | | 5 (miss by one: `5+3=8 > 7`) |
| 6-8 | 6, 7, 8 | |
| 9-10 | | 9 (`16+4=20 > 19`), 10 (`19+4=23 > 22`) |
| 11-16 | 11, 12, 13, 14, 15, 16 | |
| 17-21 | | 17, 18, 19, 20, 21 (all miss by one: `d = 4 < 5 = ceil(log2 n)`) |
| 22 | **22** (`d = 5 = ceil(log2 22)`) | |

- The run of five misses at 17-21 followed by a hit at 22 shows the pattern
  is non-monotone in a new regime: no finite extrapolation of the small-`n`
  hit/miss pattern settles all-`n` exactness.
- `n = 12` is exact for two-phase even though its information bound
  `C(12) = 29 < 30 = S(12)`: the two-phase chain inherits the exact budget
  through the increments, not through the information bound.

## Finding: independent verification of the pushed witnesses (this branch)

**[experiment]** `scripts/twophase_independent_check.py` re-verifies every
claim from commit 1f27d8e with an independently written implementation:
its own Ford-Johnson (Jacobsthal order derived from the closed form
`B(t) = (2^(t+1) + (-1)^t)/3`, each insertion's upper anchor re-found by
linear scan rather than tracked in a positions dict) and a different
program encoding: nodes are keyed by immutable transcript-prefix tuples in
plain dicts, with the constant-`Ask`/no-runtime-search property *asserted*
during construction (any two orders sharing a prefix must demand the same
next pair).  A cross-implementation mode additionally compares the emitted
outputs and per-order query counts of both implementations over every order.

- `n=5,6,7,8`: all claims reproduced; program sizes 119/719/5039/40319 ask
  nodes, leaves 120/720/5040/40320, worst queries 8/10/13/16 over all
  120/720/5040/40320 orders; worst steps = budget + 1, far below the
  polynomial clock; strictness rejections 119/719/5039/40319.
- **Zero discrepancies**: per-order query counts and outputs agree with the
  reviewed implementation on every tested order, and the independently
  derived Jacobsthal block order agrees with `upper_witness.fj_order` for
  all `k < 30`.
- `n=9` (new): an executable cross-checked witness over all 362,880 orders
  (362,879 ask nodes, 362,880 leaves, worst steps 21, single CPU core,
  ~5 min wall, no GPU) shows worst case exactly `20 = S(8) + ceil(log2 9)`,
  and since the information bound is `C(9) = ceil(log2 362880) = 19 < 20`,
  the strict two-phase schema **misses** `S(9) = 19` by one -- the
  non-monotonicity recurs at the predicted joint, now execution-backed.

## Finding: compositional exactness is non-monotone

| `n` | Two-phase bound | `S(n)` | Exact? |
|---:|---:|---:|:--|
| 4 | `S(3)+ceil(log2 4)=3+2=5` | 5 | yes |
| 5 | `S(4)+ceil(log2 5)=5+3=8` | 7 | **no** (misses by one) |
| 6 | `S(5)+ceil(log2 6)=7+3=10` | 10 | yes (self-certified below) |
| 7 | `S(6)+ceil(log2 7)=10+3=13` | 13 | yes (self-certified below) |
| 8 | `S(7)+ceil(log2 8)=13+3=16` | 16 | yes (self-certified below) |

So no single sort-then-insert schema is exact at all `n`: the shape that
works at `n=4` already fails at `n=5` and returns at `n=6`. Any all-`n`
exact-completeness proof for FO(TC)-style programs must use
globally non-decomposable structure at `n=5` (and wherever else the
recurrence overshoots), not one uniform compositional template.

## Experiments

**[experiment]** `scripts/fo_tc_twophase_barrier.py` compiles the two-phase
strategy (Ford-Johnson on the first `n-1` keys from in-repo
`scripts/upper_witness.py`, then binary insertion) into a constant-`Ask`
label program by transcript-prefix trie, exactly as the reviewed `n=8`
witness methodology does; the runtime performs no strategy search. The
outer verifier checks sorted permutation output and the query budget on
every hidden order, and a strictness probe rejects the zero-query constant
program on all non-identity orders.

- `n=5`: 119 `Ask` labels, 120 leaves, worst-case exactly 8 queries over
  all 120 orders -- tight for the two-phase class, hence optimal among
  strict compositions, but `8 > 7 = S(5)` (Knuth, TAOCP 5.3.1).
- `n=6`: 719 `Ask` labels, 720 leaves, worst-case exactly 10 queries over
  all 720 orders. Since `ceil(log2(6!)) = ceil(log2(720)) = 10`, this
  self-certifies `S(6) = 10` with no external table (consistent with the
  in-repo `tests/test_evaluate.py` pin and the Ford-Johnson exactness for
  `n <= 11` cited in `scripts/upper_witness.py`).
- `n=7`: 5,039 `Ask` labels, 5,040 leaves, worst-case exactly 13 queries
  over all 5,040 orders; maximum interpreter path is 14 steps. Since
  `2^12 < 7! = 5,040 <= 2^13`, the information lower bound is 13, so this
  witness self-certifies `S(7)=13`.
- `n=8`: 40,319 `Ask` labels, 40,320 leaves, worst-case exactly 16 queries
  over all 40,320 orders; maximum interpreter path is 17 steps. Since
  `2^15 < 8! = 40,320 <= 2^16`, the information lower bound is 16, so this
  witness self-certifies `S(8)=16` (consistent with `docs/problem.md`).

**[deduction]** Each rule is constant (`Ask` a fixed pair, `Emit`, `Halt`),
so per-step interpreter work is `O(1)`; total runtime is linear in the
program path length, far below the fixed polynomial clock
`(n+k+|p|)^2` asserted in `tests/test_fo_tc_twophase_barrier.py`. This
concerns only these finite witnesses, not all-`n` completeness.

## Findings

- **PROVED:** strict sort-then-insert needs `>= S(n-1)+ceil(log2(n))`.
- **REFUTED:** the single-schema compositional route to all-`n` exact
  budget (counterexample `n=5`: `8 > 7`).
- **PROVED (finite):** `S(6) = 10` by self-certifying two-phase witness.
- **PROVED (finite):** `S(7) = 13` by the analogous two-phase witness and
  information lower bound; verification covers every one of 5,040 orders.
- **PROVED (finite):** `S(8) = 16` by the analogous two-phase witness and
  information lower bound; verification covers every one of 40,320 orders.
- **PROVED (independent, finite):** the pushed `n=5..8` claims and all
  per-order counts re-verified with independent implementation; zero
  discrepancies.  `n=9` witness executed: two-phase worst exactly
  `20 = S(8) + ceil(log2 9)`, missing `S(9) = 19` by one.
- **PROVED (paper proof):** strict two-phase worst case is exactly
  `S(n-1) + ceil(log2 n)`; exactness at `n` holds iff
  `S(n) = S(n-1) + ceil(log2 n)`.  Over the fully known range `n ≤ 22`
  (Wells, Peczarski, Stober-Weiß; OEIS A036604 indexes the list):
  exact at `n ∈ {4, 6, 7, 8, 11, 12, 13, 14, 15, 16, 22}`, misses at
  `n ∈ {5, 9, 10, 17, 18, 19, 20, 21}`; the miss pattern is non-monotone
  (five consecutive misses 17-21, then a hit at 22), so no finite-testing
  extrapolation of the schema settles all-`n` exactness.
- **CONDITIONAL:** all-`n` exact completeness of FO(TC)-style programs, if
  true, requires shape-switching (compositional and global) families.
- **NOT CLAIMED:** unrestricted `SORT-BOUND-U` membership, hardness of
  computing `S(n)`, or any bound on general optimal trees.

## Next step

The characterization reduces the fate of the compositional route to the
increment sequence `d(n) = S(n) - S(n-1)` versus `ceil(log2 n)`.  The
decisive all-`n` questions are now:

1. Is `d(n) < ceil(log2 n)` for all `n ≥ N` for some `N` (then two-phase
   fails ultimately and uniformly)?  Or is `d(n) = ceil(log2 n)`
   infinitely often?  Known data (`n ≤ 22`) answers nothing beyond the
   table above; `n = 23`, where `S(n)` itself is open, is the first
   undecided cell for both.
2. **The cumulative miss mass grows at least linearly (proved).**
   `τ(n) = sum_{k=2..n} (ceil(log2 k) - d(k)) = T(n) - S(n)` where
   `T(n) = sum_{k=2..n} ceil(log2 k)` (`τ ≥ 0`, `τ(22) = 8`; a miss never
   pays for later: a one-off later hit cannot bank the deficit).  An
   elementary dyadic-block count gives `T(n) - log2(n!) ≥ n/4 - O(1)`
   (within each block `(2^{j-1}, 2^j]` a fraction `1 - 1/√2 > 1/4` of the
   keys have `ceil(log2 k) - log2 k ≥ 1/2`); Sergeev's
   `S(n) - log2(n!) = O(n / (log n)^{1/5})` (see
   `research-sergeev-asymptotic.md`) therefore yields
   `τ(n) ≥ n/4 - O(n / (log n)^{1/5}) = Ω(n)`.  The strict two-phase
   construction, at its per-level optimum, drifts linearly far from the
   optimum in aggregate; yet a linear-drift accumulation is compatible
   with `d(n) = ceil(log2 n)` holding at infinitely many
   `n` (even at `n = 22`), so aggregate drift still does not decide
   exactness at any single `n`.

Both remain open; neither is resolvable by more small-`n` witnesses.
