# Bulk insertion: exact small defects, a fixed-block theorem, and the real obstruction

Date: 2026-11-08. Host: billy-dev.
Front: `bulk-insertion-information-defect`.
Status: paper deductions + exact minimax experiments. No repository or Lean changes.

## 0. Objects

For integers `0 <= m <= n`, put

    P(m,n) = C_m  ⊔  A_{n-m},          e(m,n) = n!/m!,
    F(m,n) = exact minimax comparisons to sort P(m,n),
    C_P(m,n) = ceil(log2 e(m,n)),
    D(m,n) = F(m,n) - C_P(m,n).

For fixed `alpha in (0,1)`, `m = floor(alpha n)`, `r = n-m`,
`D_alpha(n) = D(m,n)`.  The front asks whether `D_alpha` is bounded by a
constant depending only on `alpha`, or unbounded along an infinite
subsequence.

The information bound gives `D(m,n) >= 0`.  The trivial decomposition
`P(m,n)` is a superposet of `A_n`; running an optimal `A_n`-sorter gives
`F(m,n) <= S(n)`.

## 1. Exact values (new finite data)

Exact labelled minimax (independent brute force for `n <= 9`, plus a
symmetry-reduced minimax cross-checked against it) gives:

    (n,m)   F   C_P   D
    (5,3)   5    5    0
    (6,3)   8    7    1
    (6,4)   6    5    1
    (7,3)  10   10    0
    (7,4)   9    8    1
    (7,5)   6    6    0
    (8,4)  12   11    1
    (9,5)  12   12    0
    (9,6)  10    9    1

Thus `D=1` occurs at `(6,3),(6,4),(7,4),(8,4),(9,6)`, and no `D=2` was found
for `n <= 9`.  For the slice `r=2`, an independent two-free-element DP gives
`D(m,m+2) in {0,1}` for every tested `m <= 40` (e.g. `F(19,21)=10`, `C_P=9`).

## 2. Fixed free block is bounded (elementary all-m theorem)

**Theorem.** For every fixed `r >= 1` there is a constant `K_r` such that
`D(m,m+r) <= K_r` for all `m`.

Proof.  Sort the `r` free keys optimally (`S(r)` comparisons), then merge the
resulting `r`-chain with the given `m`-chain.  The Hwang-Lin generalised binary
merge (SIAM J. Comput. 1 (1972), Theorem 1 and Theorem 2) uses at most
`I + r - 1` comparisons, where `I = ceil(log2 binom(m+r,r))`.  Also

    C_P = ceil(log2(r! binom(m+r,r))) >= C(r) + I - 1.

Hence `F(m,m+r) <= S(r) + I + r - 1` and

    D(m,m+r) <= S(r) - C(r) + r = E(r) + r,

a constant depending only on `r`.  (For `m < r` use the finite maximum over
the finitely many `m`.)

This does **not** touch the front: there `r = n - floor(alpha n)` grows
linearly with `n`.

The dual fixed-chain statement in the board's `fixed-pattern-defect-bound`
concerns the different quantity `S(n) - F(P)`, not `D`; it does not bound
`D` when the chain length grows.

## 3. Exact decomposition identity and a counterexample to the natural
##    "gap <= 1" strengthening

Define the decomposition gap

    delta(m,n) = F(m,n) - S(n) + S(m)  >= 0,

where non-negativity is exactly the sort-and-relabel inequality
`S(n) <= S(m) + F(m,n)`.

Write `C_P(m,n) = C(n) - C(m) + eta`, with `eta in {0,1}` (exact-checked
for all `n <= 299`; `eta=1` occurs, e.g. `(n,m)=(5,3)`).  Then

    D(m,n) = E(n) - E(m) + delta(m,n) - eta,     E(t)=S(t)-C(t).   (1)

Therefore

    D(m,n) >= E(n) - E(m) - 1.                                  (2)

Exact data give `delta in {0,1}` for all computed `n <= 9`, suggesting the
strengthening `delta <= 1`.  **This strengthening is false.**  At
`(n,m)=(21,19)` the independent `r=2` DP gives `F=10`; using the published
exact values `S(21)=66`, `S(19)=58`,

    delta(21,19) = 10 - 66 + 58 = 2.

The same instance has `C_P=9` and `D=1`, so the failure of `delta<=1` does not
by itself produce `D>=2`.

## 4. Why neither horn is currently reachable

**(a) Unbounded horn.**  By (1), if `D_alpha(n)` is unbounded along an
infinite sequence, then either

  (i) `E(n)-E(floor(alpha n))` is unbounded, or
  (ii) the decomposition gap `delta(floor(alpha n),n)` is unbounded.

Case (i) forces `E` itself to be unbounded.  No published result establishes
`E(t) >= 2` for even one `t`; exact values give `E in {0,1}` only through
`t=22`, and known lower bounds give at most `E(28) >= 1`.  So any route to the
unbounded horn through `S` needs a genuinely new certified lower bound for
the sorting number, not a reformulation.

Case (ii) is a new lower-bound question about `P(m,n)` itself.  The available
sound lower bounds are:
  * `C_P` (information);
  * `S(r) <= F(m,n)` (restrict to inputs where the chain is below all free
    keys; free-chain comparisons are then fixed);
  * `K(m,r) <= F(m,n)` (restrict to a fixed free order; this is the merge
    number), and more generally `S(n)-S(m) <= F(m,n)`.
Each of the last three is far below `C_P` for fixed `alpha in (0,1)`:
`S(r) - C_P` and `K(m,r)-C_P` are negative by `Theta(n)`, and
`S(n)-S(m)-C_P = E(n)-E(m)+O(1)`, which is at most one with current
certificates.  No extension-count/lookahead potential is known to give more:
the one-ply and `t`-ply count potentials are sound but equal the information
bound at `A_n` for `t <= n/2`, and the staircase obstruction shows count
lookahead is not generally complete.

**(b) Bounded horn.**  Suppose `D_alpha(n) <= K` for one fixed `alpha` and all
`n`.  Let `m=floor(alpha n)`.  The decomposition inequality
`S(n) <= S(m) + F(P)` gives

    E(n) <= E(m) + K + 1.

Iterating `n -> floor(alpha n)` until the argument is bounded yields

    E(n) = O_alpha(log n),      i.e.   S(n) <= ceil(log2 n!) + O_alpha(log n).

That would improve the best published upper bound (Sergeev, ECCC TR20-096,
Theorem 3: `E(n)=O(n/(log n)^(1/5))`) to logarithmic excess, and would improve
the classical Ford-Johnson `O(n)` excess.  So the bounded horn is a major
algorithmic theorem, not a routine estimate.

## 5. Soundness versus completeness

- **Sound:** `D>=0`; the fixed-`r` Hwang-Lin bound; the lower bound (2); the
  `t`-ply extension-count hierarchy `L_t(P) <= F(P)`.
- **Not complete:** information and bounded count-lookahead do not certify
  the first known antichain excess (`S(12)=30>C(12)=29`); the `(21,19)`
  instance shows the decomposition-gap strengthening fails.  No explicit
  all-`n` insertion strategy with bounded defect exists, and no lower-bound
  potential currently certifies `D>=1` for any `n` (the exact minimax
  certificates at `n<=9` are case computations, not a method).
- **General-poset results do not transfer:** the staircase/fence family has
  linear defect `F-L_0 = Omega(n)`; GPC gives only the multiplicative
  `log_phi e` bound.  Neither yields a statement about `C_m ⊔ A_r`.

## 6. Honest conclusion

The front is a genuine open dichotomy, not a finite-computation gap:
- the bounded horn implies `S(n) <= C(n)+O(log n)`, a major open upper bound;
- the unbounded horn implies (via (1)) either unbounded excess `E` (no
  published `E>=2` at any single `n`) or unbounded decomposition gap `delta`,
  a new lower-bound problem for `C_m ⊔ A_r`.

New in this note: the exact `D` table, the fixed-free-block theorem
`D <= E(r)+r`, the identity (1), and the explicit failure of `delta<=1` at
`(21,19)`.  No claim about the truth of either horn is made.

## Reproduction

Temporary scripts (not repository):
`/tmp/chain_sym3.py` (symmetry-reduced minimax; validated against
`/tmp/one_brute.py` for `(6,3),(4,4),(5,4)`),
`/tmp/r2_indep.py` (independent two-free DP, used for `(21,19)`).
