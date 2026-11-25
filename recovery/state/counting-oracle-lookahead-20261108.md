# Extension-count lookahead and the unary S(n) front

Date: 2026-11-08. Host: billy-dev. Front: `counting-oracle-sortbound-complexity`.
Status: paper proof + finite experiment. No repository, Lean, or commit changes.

## Question

`SORT-BOUND-U = {1^n # 1^k : S(n) <= k}`. Is it in `P^{#P}`? Equivalently, can
the minimax height be recovered from polynomially many exact linear-extension
counts `e(P)`?

## The `t`-ply count lookahead

For a finite poset `P`, let `e(P)` be the number of linear extensions and

    L_0(P) = ceil(log2 e(P)),
    L_{t+1}(P) = 0                                   if P is total,
    L_{t+1}(P) = 1 + min_{x || y} max( L_t(P+x<y), L_t(P+y<x) ) otherwise.

`L_1` is exactly the one-ply bound of `docs/research-one-ply-obstruction.md`.
`L_t(P)` is the value of the depth-`t` minimax recurrence whose leaves are
scored by the information bound; it uses at most `(n choose 2)^t` leaf
extension counts.

### Fact 1. `L_t(P) <= F(P)` for every `P,t`.

Induction on `t`: `L_0 <= F` is the information bound; the recurrence for `F`
and the induction hypothesis give the step.

### Fact 2. `L_t(P) <= L_0(P) + t` for every `P,t`.

Induction on `t`. If `Q` is a child of `P`, then `e(Q) <= e(P)`, hence
`L_0(Q) <= L_0(P)`. Therefore every `L_{t-1}(Q)` is at most
`(t-1) + L_0(P)`, and adding the root comparison gives `t + L_0(P)`.

### Corollary. Write `d(P) = min{t : L_t(P) = F(P)}`. Then

    F(P) - L_0(P) <= d(P) <= F(P).

The upper bound follows by following an optimal strategy of depth `F(P)`.
The lower bound is immediate from Fact 2 and `L_d(P) = F(P)`.

## The staircase family gives unbounded lookahead depth

Let `W_n` be the `n`-element staircase (fence): `i < j` iff `j - i >= 2`.
The only incomparable pairs are the `n-1` consecutive pairs `(i,i+1)`.

- `e(W_n) = F_{n+1}` (Fibonacci). Linear extensions correspond to independent
  sets of the path of consecutive pairs: an extension is determined by which
  adjacent pairs are inverted, and no two consecutive inversions are possible.
- `F(W_n) = n-1`. Comparable nonconsecutive pairs give no information, so only
  the `n-1` consecutive pairs are useful; each query resolves at most one of
  them, and the adversary can answer so that none is resolved for free.

Hence

    d(W_n) >= (n-1) - ceil(log2 F_{n+1}) = Omega(n),

because `log2 F_{n+1} <= (n+1) log2(phi) < 0.7(n+1)`.

Consequently, for every fixed `t`, all sufficiently large `n` satisfy
`L_t(W_n) < F(W_n)`. No fixed-ply extension-count lookahead is exact on all
posets, and the `t`-ply evaluator needs at least `Omega(n)` plies on `W_n`
(about `0.3 n` by this bound).

### Experiment (exact)

Exact computation for `5 <= n <= 13` gives `d(W_n) = n-4`:

    n    L_0 ... L_{n-1}                                  d
    5    3,4,4,4,4                                        1
    6    4,4,5,5,5,5                                      2
    7    5,5,5,6,6,6,6                                    3
    8    6,6,6,6,7,7,7,7                                  4
    9    6,7,7,7,7,8,8,8,8                                5
    10   7,7,8,8,8,8,9,9,9,9                              6
    11   8,8,8,9,9,9,9,10,10,10,10                        7
    12   8,9,9,9,10,10,10,10,11,11,11,11                  8
    13   9,9,10,10,10,11,11,11,11,12,12,12,12             9

The values also satisfy the ordinal-sum convolution recurrence
`R_0(n) = ceil(log2 F_{n+1})`,
`R_{t+1}(n) = 1 + min_{0 <= i <= n-2} (R_t(i+1) + R_t(n-i-1))`,
on this range. The equality `d(W_n) = n-4` for all `n` is open; only the
`Omega(n)` lower bound is proved here.

## The antichain root

At `A_n`, every first comparison gives the same child (a two-chain plus an
`(n-2)`-antichain) with `e = n!/2`. For `n >= 3`, `n!` is even and not a power
of two, so `ceil(log2(n!/2)) = ceil(log2 n!) - 1`. Therefore

    L_1(A_n) = 1 + ceil(log2(n!/2)) = ceil(log2 n!) = L_0(A_n)

for all `n >= 3` (and for `n = 2` separately). One ply of count lookahead
gives exactly the information bound at the root and cannot certify the excess.

A direct exact computation gives

    L_2(A_12) = 29 < 30 = S(12).

So even two plies fail at the first known non-tight root. The general bound
`d(A_n) >= S(n) - ceil(log2 n!)` is only as strong as the (open) question
whether the excess `S(n) - ceil(log2 n!)` is unbounded. Thus this does not
settle `d(A_n)` or the P^{#P} question.

## Structural-information objection is false

An `e`-oracle actually reveals the whole poset in `O(n^2)` queries. Given `P`
and `e(P)`, for each ordered pair `(a,b)` query the transitive closure
`Q = tc(P + a<b)` (rejecting cycles). If `a<b` already in `P`, then `Q = P` and
`e(Q) = e(P)`. If `a || b`, then `Q` is a strict extension and `e(Q) < e(P)`
(one orientation of the pair is excluded). If `b<a`, the query is cyclic.
Thus one query per ordered pair reconstructs the relation matrix.

This matters for the front: a lower bound cannot be based on the #P oracle
"hiding the poset". It also means a P^{#P} algorithm could, in principle,
recognise the staircase family and output `F(W_n) = n-1` by formula, so the
lookahead barrier above is **not** a lower bound against arbitrary P^{#P}
algorithms.

## Complexity status and barriers

- A proof that `SORT-BOUND-U` is not in `P^{#P}` would show
  `PSPACE` is not contained in `P^{#P}` (since `SORT-BOUND-U` is in `PSPACE`),
  hence `P != PSPACE`. So the negative direction is at least as hard as a
  major open separation.
- `SORT-BOUND-U` is sparse. If it were `P^{#P}`-hard under polynomial-time
  Turing reductions, then `P^{#P} <= P/poly` (a sparse oracle is in `P/poly`,
  and `P/poly` is closed under polynomial-time Turing reductions), hence
  `PH <= P/poly` by Toda, hence `PH = Sigma_2` by Karp-Lipton. So the front
  cannot be resolved by `P^{#P}`-completeness either.
- No P^{#P} algorithm and no query lower bound against arbitrary P^{#P}
  algorithms was obtained. The front remains open.

## Reproduction

Scripts (temporary, not repository):
`/tmp/opencode/ply_probe.py` (all posets `n <= 6`),
`/tmp/opencode/staircase_vals.py` (exact `L_t(W_n)`),
`/tmp/opencode/lookahead_antichain.py` (exact `L_t(A_12)` for `t <= 2`).
The `n = 12` check was independently recomputed by the direct formula
`L_2(A_12) = 1 + L_1(C)` with `C = A_12` plus one relation.
