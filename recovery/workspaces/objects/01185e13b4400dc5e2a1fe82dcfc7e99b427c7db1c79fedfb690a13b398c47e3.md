# The realizability window: what posets on height-S(n) optimal plays satisfy

**Date:** 2026-11-04
**Front:** poset-class-reachability-restriction (issue #301)
**Status:** Theorem 1 is a paper proof. Corrected finite reachability
experiments are in `scripts/realizability_window.py` and
`tests/test_realizability_window.py`. Window sufficiency is refuted at
`n=5,6`; Conjecture K remains open beyond the finite corrected census.

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

The exact occurrence criterion is:

    R(P, d) iff there is a comparison chain from the antichain to P of
    length d such that at each informative comparison from Q to children
    C0,C1, max(F(C0),F(C1)) <= S(n)-k-1, where k is the current depth.
    A wasted comparison at Q is permitted only when F(Q) <= S(n)-k-1.

The previous implementation incorrectly filtered only the selected child
after an informative comparison. This omits the sibling subtree, which is
part of the same strategy and must fit the same height bound. The corrected
experiment below uses the joint-child criterion. Wasted comparisons remain
allowed when their unchanged continuation fits.

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

**Correction to the prior correction.** The earlier version of this note
claimed that `C_2 ⊕ A_3` (chain below a 3-element antichain, `n=5`) refuted
the `quantified-root-adversary-proof` ledger claim. That was incorrect: the
proposed declaration order `b<a, a<x, a<y, a<z` fails at its third
comparison. At the state after `b<a, a<x`, comparing `b` with `x` has child
continuation costs 4 and 5 with only 4 comparisons remaining. The corrected
reachability census does not contain this poset at depth 4. Its necessary
window is a singleton, which is not sufficient for occurrence. This finite
check supports, but does not prove, the ledger's non-occurrence claim.

## Window sufficiency: finite counterexamples and open conjecture

**Conjecture W (window sufficiency).** For all `n`, `P`:

    R(P, d)  iff  covers(P) <= d <= S(n) - max(F(P), pi(P)).

If true, realizability is decided by `P` alone (via `F`): the reachable
class is exactly the feasible-window class, realizability needs no game
search, and "which posets can appear" collapses to a cheap interval test.

The corrected exact reachability census confirms window necessity but
refutes sufficiency at `n=5,6`:

| n | classes | realizable | share |
|---|---------|-----------|-------|
| 1 | 1   | 1   | 1.00 |
| 2 | 2   | 2   | 1.00 |
| 3 | 5   | 5   | 1.00 |
| 4 | 16  | 12  | 0.75 |
| 5 | 63  | 19  | 0.30 |
| 6 | 318 | 136 | 0.43 |

There are 24 feasible-window depth/state pairs not realized at `n=5` and 78
at `n=6`. For example, canonical state `(0,0,0,1,9)` has
`(e,covers,pi,F)=(20,2,2,5)` and satisfies the proposed window at depth 2,
but is not reachable there. It is a child of `(0,0,0,0,1)` after comparing
`(0,1)`; the two children have continuation costs 5 and 6 although only 5
comparisons remain. Thus the comparison cannot occur in a height-7 strategy.
Conjecture W's former finite sufficiency evidence is withdrawn; its
algorithmic value does not follow.

**Falsification of W.** The joint-child recurrence gives counterexamples
already at `n=5,6` (above). The issue is not a subtle large-`n` minimax
obstruction: the previous DP discarded the sibling-budget obligation at each
step. Further work on interval sufficiency is not warranted in this form.

## Conjecture K (summary soundness inside `R_n`)

**[corrected experiment]** Within the corrected realizable classes at `n <= 6`, the pair
`(e(P), covers(P))` determines `F(P)`:

- `n = 5`: 19 realizable classes, 10 `e`-keys, 11 `(e, covers)`-keys, no
  `F` split.
- `n = 6`: 136 realizable classes, 32 `e`-keys (1 key splits), 52
  `(e, covers)`-keys, no `F` split.

The single splitting `e`-key at `n=6` is `e=15`; adding `covers` separates
the values in the corrected reachable census.

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
   exclusion family (stars, `Corollary 1`).
2. **The positive side is refuted in its interval-only form.** Conjecture W
   fails at `n=5,6`; interval feasibility does not decide realizability.
3. **The transfer side (front's second half).** No known poly-time
   counting or certificate transfer is *enabled* by these restrictions:
   counting `e` stays #P-hard in general, `R_n`-membership itself is
   only characterized through the hypotheses being tested. Evidence
   argues *against* the falsifier direction: the corrected `R_n` is a
   restricted subfamily and `(e,covers)` remains sound in the finite census.
   Conjecture K is only a finite observation; no algorithmic transfer follows.

## Evidence labels

- Theorem 1, Lemmas 1-3, Corollary 1: **paper proof (deduction)**; only
  the classical `S(n) <= S(n-1) + ceil(log2 n)` insertion bound is used
  (deduction from the model, also literature).
- Corrected reachability, star realizability and `(e, covers)` summary data,
  plus the refutation of the ledger's `C_2 ⊕ A_3` claim:
  **experiment**, exact exhaustive DP over all poset classes
  (`scripts/realizability_window.py`, asserts in
  `tests/test_realizability_window.py`).
- Conjecture W: **refuted at `n=5,6`**; interval sufficiency is false.
- Conjecture K: **corrected finite experiment + conjecture**, all-`n` status open.

## Reproduction

    python3 -m unittest discover -s tests        # n <= 5 checks
    python3 scripts/realizability_window.py -n 6  # full n <= 6 census (~1 min)

Limitations: reachability census exact for `n <= 6` only; `n = 7` requires a faster
canonicalizer than the `n!`-permutation one used here; no claim is made
about any all-`n` summary property of the corrected reachable class.
