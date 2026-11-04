# The realizability window: what posets on height-S(n) optimal plays satisfy

**Date:** 2026-11-04
**Front:** poset-class-reachability-restriction (issue #301)
**Status:** Theorem 1 is a paper proof; the realizable-class computations are
experiments (`scripts/realizability_window.py`,
`tests/test_realizability_window.py`); Conjectures W and K are conjectures
verified for every poset class at `n <= 6`.

## Question and payoff

The front asks whether there is a nontrivial all-`n` property, other than
"being a partial order", that every poset occurring on some height-`S(n)`
optimal play from the antichain must satisfy, and whether it disables a
trivial poly-time counting/certificate transfer. An effective restriction
would separate "hardness of arbitrary posets" from the fixed antichain-root
game and could license cheaper exact evaluation of `S(n)`.

## Definitions

Fix `n` labelled keys. States are strict posets transitively closed,
represented by successor bitmasks. `F(P)` is the minimax continuation cost
(docs/upper-bound.md). `covers(P)` is the number of cover relations.
For a linear extension `L` of `P` let `a(L)` be the number of adjacent pairs
`(L[k], L[k+1])` that are relations of `P`, and define

    pi(P) = (n-1) - max_{L linear extension of P} a(L)
          = min over total extensions T of |covers(T) \ P|.

Say `P` occurs **at depth `d`** if it is the state after `d` comparisons on
some branch of the decision tree of *some* sorting strategy whose worst-case
height is at most `S(n)`, from the antichain. Melons/wasted comparisons
(comparing an already comparable pair, leaving the state unchanged) are
allowed; the class without them is smaller, so necessary conditions below
apply a fortiori to it. Let `R(P, d)` denote occurrence, and
`R_n = { P : R(P, d) for some d }`.

The exact criterion used in the experiment (and which the DP computes
exactly):

    R(P, d)  iff  exists a comparison chain A = P_0 (partial order inclusion)
    from the antichain to P of length exactly d -- where steps add one
    declared pair plus closure, or repeat (padding) -- such that
    F(P_k) <= S(n) - k for every prefix state P_k.

**[experiment]** The DP verifies `R(P, d)` exhaustively for `n <= 6`. Padding
matters: at `n = 5`, 11 of the 29 realizable classes realize depths strictly
beyond `covers(P)` (by 1-3 wasted comparisons; e.g. class `(0,1,3,7,15)`
realizes every depth in `[4, 7]` from `covers = 4` up to `S - F = 7`), and
at `n = 6`, 71 of 157 do. Window-size variation is real, so any all-`n`
treatment must keep the padded (larger) class in view; Theorem 1 holds for
the padded class and hence a fortiori for honest play.

## Theorem 1 (window necessity; paper proof)

**Lemma 1 (cover cost).** Reaching `P` from the antichain needs at least
`covers(P)` declared comparisons. *Proof.* If the final state is `P` then
every declared pair belongs to `P` (states grow monotonically and the final
state is the closure of all declared pairs). A cover `(x, y)` of `P` cannot
arise by closure from other declared pairs, since that needs an intermediate
`z` with `x < z < y`, contradicting covers. So every cover of `P` is itself
declared, and each declaration is one comparison. ∎

**Lemma 2 (insertion cost).** After reaching `P` at depth `d` with budget
remaining `b = S(n) - d`, the tree below must reach a total order `T`
extending `P`, and every cover of `T` that is not a relation of `P` must be
declared below the node (again no intermediate exists). Hence
`b >= |covers(T) \ P| >= pi(P)`.

**Lemma 3 (budget).** The subtree below the node is a strategy for `P`, so
`F(P) <= b`.

**Theorem 1.** If `P` occurs at depth `d`, then

    covers(P)  <=  d  <=  S(n) - max(F(P), pi(P)),      (W)

in particular `covers(P) + max(F(P), pi(P)) <= S(n)`.
(The extension-count bound `e(P) <= 2^{S(n)-d}` is redundant here since
`F(P) >= ceil(log2 e(P))` always. These conditions strictly refine all
previously recorded necessary conditions `F(P) <= S(n) - d`,
`d + F(P) <= S(n)`, `e(P) <= 2^{S(n)-d}`, and the odd-order
antichain-to-star reset obstruction of `docs/research-exact-reset-realizability.md`
applied to even `n` as well.)

**Corollary 1 (star exclusion, all `n >= 4`).** Let `V_n` be the star (one
key below the other `n-1`, nothing else). `covers(V_n) = n - 1` and
`F(V_n) = S(n-1)`: comparisons with the known minimum are worthless by
projection, so any strategy from `V_n` costs at least a strategy for the
`n-1`-antichain, and ignoring `V`'s bottom key gives one. Binary insertion
of the `n`-th key gives `S(n) <= S(n-1) + ceil(log2 n)`, and
`ceil(log2 n) < n - 1` for `n >= 4`, so the window in (W) is empty:
`V_n` occurs on no optimal play for **all** `n >= 4`.
**[experiment]** `V_3` is realizable at depth exactly `2 = S(3) - S(2)`
(and `S(3) - S(2) = 2 = n - 1` is fine there); `V_4, V_5, V_6` are
unrealizable, matching the corollary.

**Correction to a ledger note.** The frontier ledger entry
`quantified-root-adversary-proof` recorded the claim that the ordinal sum
`C_2 ⊕ A_3` (chain below a 3-element antichain, `n = 5`) "cannot occur on a
height-7 sorting tree". **Refuted (experiment):** it occurs at depth
exactly `4` (declared in order `b < a`, `a < x`, `a < y`, `a < z` with
budget `3 = F`), and its window `[covers, S - max(F, pi)] = [4, 4]` is a
singleton. Its sibling states all fit their budgets, so no root-quantifier
argument excludes it; the ledger's example does not support the claimed
root obstacle.

## Theorem 2 (verified, `n <= 6`) and Conjecture W

**Conjecture W (window sufficiency).** For all `n`, `P`:

    R(P, d)  iff  covers(P) <= d <= S(n) - max(F(P), pi(P)).

If true, realizability is decided by `P` alone (via `F`): the reachable
class is exactly the feasible-window class, realizability needs no game
search, and "which posets can appear" collapses to a cheap interval test.

**[experiment]** The window is exact — both directions, at every depth —
for all poset classes at every `n <= 6`:

| n | classes | realizable | share |
|---|---------|-----------|-------|
| 1 | 1   | 1   | 1.00 |
| 2 | 2   | 2   | 1.00 |
| 3 | 5   | 5   | 1.00 |
| 4 | 16  | 12  | 0.75 |
| 5 | 63  | 29  | 0.46 |
| 6 | 318 | 157 | 0.49 |

At `n = 5, 6` about half of all poset classes are excluded, all excluded
ones violate the window, and conversely.

**Falsification attempts on W (not yet successful).**
1. *Intermediate-budget obstruction (the serious one).* A naive
   construction - declare the covers of `P` one by one - can fail because
   prefix states `P_k` have larger `F` than `P`, and may violate
   `F(P_k) <= S(n) - k`. Greedy cover-ordering is not a proof; the theorem,
   if true, is a proper minimax fact. Counterexamples were not found at
   `n <= 6`; the `n = 7` check (2045 classes; needs faster canonical
   labelling) is the immediate next falsification step.
2. *Divisibility obstruction.* The odd-order antichain-tree reset argument
   (a single comparison splits the extension set exactly in half, leaf
   classes have fixed sizes) does not transfer to occurrence: occurrence
   asks only that both children fit, not that certificate classes have
   equal sizes. No parity obstruction was found in the data (`n <= 6`).

## Conjecture K (summary soundness inside `R_n`)

**[experiment]** Within the realizable classes at `n <= 6`, the pair
`(e(P), covers(P))` determines `F(P)`:

- `n = 5`: 29 realizable classes, 14 `e`-keys, 16 `(e, covers)`-keys, no
  `F` split.
- `n = 6`: 157 realizable classes, 35 `e`-keys (3 keys split, resolutions
  below), 59 `(e, covers)`-keys, 75 `(e, covers, pi)`-keys, no `F` split.

The three splitting `e`-keys at `n = 6`, all `e = 15`:
`F = 4` with `covers = 5` (`(0,0,0,1,11,31)`, `(0,1,1,3,3,11)`) vs
`F = 5` with `covers = 4` (`(0,0,1,2,5,21)`), plus two `F = 4, covers = 6`
classes. Covers separates them.

Contrast with unrestricted posets (prior folklore, verified): the
documented `n = 5` pair with `e = 8, F = 3` vs `4`
(`docs/research-state-compression.md`) *does* split `F` at fixed `e` — but
the `F = 4` member is **not in `R_5`** (experiment). The new restricted
question is correspondingly sharper.

**Conjecture K.** For all `n` and all `P` in `R_n`, `F(P)` is a function of
`(e(P), covers(P))`.
Why it matters: if true, a sound memo key of `O(n log n)` bits exists for
the *reachable part* of the minimax state space — while the full state
space provably needs `Theta(n log^2 n)` bits per key
(`docs/research-winning-frontier-barrier.md`). This is a candidate route
around the decade-old state-space barrier, restricted to the states that
optimal play actually visits. It does **not** yet yield an algorithm: `e`
is #P-hard in general and not known easy on `R_n`, and the transition
structure (needed by the recursion) is not a function of the key.

## Assessment of the front's dichotomy

1. **Yes, explicit all-n restrictions exist beyond "poset".** Theorem 1
   (window necessity) is proved for all `n`, is strictly stronger than all
previously recorded necessary conditions, and yields a clean all-`n`
exclusion family (stars, `Corollary 1`) plus an exact excluded-class
census at `n <= 6` (excludees: 4 at `n = 4`, 34 at `n = 5`, 161 at
`n = 6`; every excluded class violates the window, and vice versa).
2. **The positive side is not yet closed.** Conjecture W would be a real
   structural theorem about `S(n)` (feasibility = realizability), with
   algorithmic value for bidding/bidirectional exact solvers.
3. **The transfer side (front's second half).** No known poly-time
   counting or certificate transfer is *enabled* by these restrictions:
   counting `e` stays #P-hard in general, `R_n`-membership itself is
   only characterized through the hypotheses being tested. Evidence
   argues *against* the falsifier direction: `R_n` is a small (~49%),
   information-tight, (e, covers)-rigid subfamily, with no #P-hardness
   witness in it and none expected from the transfer tools. **The exact
   evidence-backed blocker:** the two all-`n` questions on which the front
   hinges — window sufficiency (Conjecture W) and summary soundness
   (Conjecture K) — are verified only up to `n = 6`; the `n = 7, 8` data
   (both cheap once canonical labelling is accelerated) should be the
   next falsification pass before either conjecture is claimed as
   risk-bearing.

## Evidence labels

- Theorem 1, Lemmas 1-3, Corollary 1: **paper proof (deduction)**; only
  the classical `S(n) <= S(n-1) + ceil(log2 n)` insertion bound is used
  (deduction from the model, also literature).
- Star realizability at `n <= 6`, window-exactness table, `(e, covers)`
  summary data, refutation of the ledger's `C_2 ⊕ A_3` claim:
  **experiment**, exact exhaustive DP over all poset classes
  (`scripts/realizability_window.py`, asserts in
  `tests/test_realizability_window.py`).
- Conjectures W and K: **experiment + conjecture**, all-`n` status open.

## Reproduction

    python3 -m unittest discover -s tests        # n <= 5 checks
    python3 scripts/realizability_window.py -n 6  # full n <= 6 census (~1 min)

Limitations: exact for `n <= 6` only; `n = 7` requires a faster
canonicalizer than the `n!`-permutation one used here; no claim is made
about optimality of the DP definition (padded/wasted comparisons are
allowed, making the realizable class *larger*, which strictly strengthens
Theorem 1 but weakens Conjecture W's usefulness if padding turns out to
matter at larger `n`).
