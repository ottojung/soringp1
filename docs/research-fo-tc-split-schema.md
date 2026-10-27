# Split-schema phase-coupling barrier for strategy programs

**Status:** proved general no-go lemma (paper proof) + exact executable
minimax completion costs with independent two-sided verification, not
Lean-checked. **Model:** adaptive comparison sorting of `n` distinct keys;
`S(n)` optimal worst-case count (`docs/problem.md`). Coordinates with
Antonina fervor (FO(TC) strategy programs) and umbrella #301. Follows the
strict two-phase barrier (`docs/research-fo-tc-twophase.md`).

## Sharp question

Is there a *single* compositional program schema -- fully sort a fixed
`m`-subset of keys, then finish with arbitrary comparisons -- that achieves
the exact optimal budget `S(n)` for the interesting `(m, n)`? A YES would
give the uniform-completeness shape the FO(TC) program conjecture needs; a
NO forces every complete program family to use non-compositional state.

## Lemma (PROVED, paper proof): split-schema lower bound with coupling

**[deduction]** A deterministic adaptive program that (phase 1) fully
determines the order of a fixed `m`-subset using only comparisons inside
that subset, and (phase 2) then performs arbitrary further comparisons,
uses at least `S(m) + C(m,n)` comparisons worst-case, where `C(m,n)` is the
minimax completion cost: the minimum, over all binary decision trees
querying arbitrary pairs, of the worst-case number of further comparisons
needed to fully sort given a known sorted `m`-chain.

*Proof.* Phase-1 outcomes depend only on the relative order of the
`m`-subset, so some `m`-order forces at least `S(m)` comparisons on a fixed
phase-1 path `P`. Every full order extending that `m`-order generates path
`P`, hence faces one fixed phase-2 tree `T_P`, which must sort all `n!/m!`
extensions. By key symmetry the extension family is isomorphic for every
fixed `m`-order, so `height(T_P) >= C(m,n)`, attained on some extension
whose phase-1 cost is the same path cost `>= S(m)`. The adversary plays
that combination. QED.

Since `C(m,n) >= ceil(log2(n!/m!))` (a tree sorting `n!/m!` extensions
needs that height), this strengthens the counting bound
`B(m,n) = S(m) + ceil(log2(n!/m!))`. For `m = n-1` it reproduces the
strict two-phase lemma exactly.

## Finding: phase coupling makes the counting bound unachievable (NEW)

**[experiment, two-sided]** `scripts/fo_tc_split_schema.py` computes exact
`C(m,n)` by exhaustive minimax search over knowledge states (every
splitting pair tried; memoization + information-bound pruning), emitting a
witness tree per cell. `tests/test_fo_tc_split_schema.py` replays every
tree over all extensions (upper bound, independently checked) and re-proves
each lower bound with an independent depth-bounded existence prover (plain
recursion, no memoization/greedy -- different code path). Positive
controls: the prover finds trees at height `C` and rules out `C-1`.

| `(m,n)` | info price | `C(m,n)` | true split cost `S(m)+C` | `S(n)` | verdict |
|---|---|---|---|---|---|
| (2,4) | 4 | 4 | 5 | 5 | exact (tight) |
| (3,5) | 5 | 5 | 8 | 7 | miss (counting) |
| (2,5) | 6 | 6 | **7** | 7 | **exact (tight) -- NEW positive** |
| (4,6) | 5 | **6** | **11** | 10 | **miss by coupling -- NEW barrier** |
| (3,6) | 7 | **8** | **11** | 10 | **miss by coupling -- NEW barrier** |
| (5,7) | 6 | 6 | 13 | 13 | exact (tight) |
| (4,7) | 8 | **9** | **14** | 13 | **miss by coupling -- NEW barrier** |

- Three cells -- (4,6), (3,6), (4,7) -- where the counting bound `B(m,n)`
  looked *exact* (`B = S(n)`) are in fact missed by every split-schema
  program: phase coupling adds a strict +1 penalty the counting argument
  cannot see. The exactness pattern of compositional schemas is therefore
  non-monotone in a second, finer sense than the strict two-phase result.
- Positive contrast: split-(2,3) **achieves** `S(5) = 7` (sort any 2 keys,
  then optimally complete in 6), exactly where strict two-phase (4,1)
  provably misses. Compositional exactness depends on the *split point*,
  not just on `n`.
- Arithmetic table `B(m,n)` vs `S(n)` for all `1 <= m < n <= 12` (from
  `S(0)..S(12)` = 0,0,1,3,5,7,10,13,16,19,22,26,30) is printed by the
  script; `B(n-1,n)` reproduces the strict two-phase column.

## Why this matters for the central question

Every uniform compiler route that sorts a sub-key first and completes
afterwards -- the natural shape for a compositional FO(TC) program -- now
carries *two* stacked obstructions: the counting bound and a computed
coupling penalty. A completeness theorem for polynomial-size exact
strategy programs must either avoid fixed splits entirely or switch split
points with `n` in a way no single schema captures. Next decisive cells:
`C(5,8)`/`C(6,9)` (does the penalty grow?), and whether any fixed-`m`
family stays exact past the computed range.
