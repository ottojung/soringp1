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

## Finding: compositional exactness is non-monotone

| `n` | Two-phase bound | `S(n)` | Exact? |
|---:|---:|---:|:--|
| 4 | `S(3)+ceil(log2 4)=3+2=5` | 5 | yes |
| 5 | `S(4)+ceil(log2 5)=5+3=8` | 7 | **no** (misses by one) |
| 6 | `S(5)+ceil(log2 6)=7+3=10` | 10 | yes (self-certified below) |
| 7 | `S(6)+ceil(log2 7)=10+3=13` | 13 | yes (self-certified below) |
| 8 | `S(7)+ceil(log2 8)=13+3=16` | 16 | yes (self-certified below) |
| 9 | `S(8)+ceil(log2 9)=16+4=20` | 19 | **no** (misses by one; 2nd miss) |
| 10 | `S(9)+ceil(log2 10)=19+4=23` | 22 | **no** (misses by one) |
| 11 | `S(10)+ceil(log2 11)=22+4=26` | 26 | yes |
| 12 | `S(11)+ceil(log2 12)=26+4=30` | 30 | yes |

(S(n) values for `n <= 12` per `docs/research-plan.md`; small cases
`n=2,3` are also exact: `S(1)+1=1=S(2)`, `S(2)+2=3=S(3)`.)
Full characterization over known values: exact at
`n in {2,3,4,6,7,8,11,12}`, miss at `n in {5,9,10}`.

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

- `n=9`: strategy-level exhaustive run of the same two-phase decision
  procedure over all 362,880 orders gives worst-case exactly 20
  comparisons with every output sorted -- tight for the two-phase class,
  hence optimal among strict compositions, but `20 > 19 = S(9)`. This is
  the predicted second miss (verified by transcript counts, not by
  compiling the 362,880-leaf trie). `tests/test_fo_tc_twophase_barrier.py`
  also pins the full `n=2..12` exact/miss characterization arithmetically.

**[deduction]** Each rule is constant (`Ask` a fixed pair, `Emit`, `Halt`),
so per-step interpreter work is `O(1)`; total runtime is linear in the
program path length, far below the fixed polynomial clock
`(n+k+|p|)^2` asserted in `tests/test_fo_tc_twophase_barrier.py`. This
concerns only these finite witnesses, not all-`n` completeness.

## Findings

- **PROVED:** strict sort-then-insert needs `>= S(n-1)+ceil(log2(n))`.
- **REFUTED:** the single-schema compositional route to all-`n` exact
  budget (counterexamples `n=5`: `8 > 7`; `n=9`: `20 > 19`;
  `n=10`: `23 > 22` by lemma arithmetic).
- **PROVED (finite):** `S(6) = 10` by self-certifying two-phase witness.
- **PROVED (finite):** `S(7) = 13` by the analogous two-phase witness and
  information lower bound; verification covers every one of 5,040 orders.
- **PROVED (finite):** `S(8) = 16` by the analogous two-phase witness and
  information lower bound; verification covers every one of 40,320 orders.
- **PROVED (finite):** the two-phase lower bound `S(n-1)+ceil(log2(n))` is
  tight at strategy level for every `2 <= n <= 9`: the Ford-Johnson +
  binary-insertion decision procedure attains it exhaustively
  (`tests/test_fo_tc_twophase_barrier.py::test_two_phase_lower_bound_is_tight_strategy_level`
  for `n <= 8`; the `n=9` strategy run at 20 above). Hence each compiled
  budget is optimal within the strict two-phase class.
- **CONDITIONAL:** all-`n` exact completeness of FO(TC)-style programs, if
  true, requires shape-switching (compositional and global) families.
- **NOT CLAIMED:** unrestricted `SORT-BOUND-U` membership, hardness of
  computing `S(n)`, or any bound on general optimal trees.

## Next step

The `n=9` joint is now verified (strategy-level exhaustive: worst 20 >
`S(9) = 19`) and the `n=2..12` exact/miss pattern is characterized. The
decisive task remains an all-`n` completeness proof or refutation for the
full fragment, not further finite witnesses.
