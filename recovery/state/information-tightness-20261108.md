# Information tightness beyond n=21: Ford-Johnson arithmetic and a linear-depth leaf-count barrier

**Status:** paper proof + exact integer arithmetic + small exact checks. Not Lean-checked.
No repository changes. Labels: `[literature]`, `[deduction]`, `[experiment]`, `[open]`.

## 0. Claim under attack

Front: `S(n) > C(n) = ceil(log2 n!)` for every `n >= 22`, so information-tight
comparison sorting happens at only finitely many sizes.

Known values `[literature]` (OEIS A036604/A003070, Wells, Peczarski,
Stober-Weiss): `S(n)=C(n)` for `n<=11` and for `n=20,21`; `S(12)=30>C(12)=29`;
`S(n)=C(n)+1` for `12<=n<=19`; and `S(22)=71>C(22)=70`. Exact `S(n)` is open
for `n>=23`; `S(28)>=99`.

Falsifier sought: an explicit `n>=22` and a height-`C(n)` adaptive comparison
tree. This note does not find one. It proves two all-`n` results about the
natural routes to such a witness and to a non-tightness proof.

## 1. Ford-Johnson is never information-tight beyond n=21

Let `F(n)` be the comparison count of the Ford-Johnson merge-insertion
algorithm (OEIS A001768).

**Theorem A `[deduction]`.**
For every integer `n >= 23`, `F(n) > C(n)`. Moreover the complete set of
`n >= 23` with `F(n) = C(n)+1` is exactly

    {23, 24, 40, 41, 42, 43}.

For `n >= 122`, `F(n) >= C(n)+3`.

**Exact formula.** Put `M = ceil(log2(3n/4))`. Then

    F(n) = M*n - (2^(M+2) - 4 - floor(3M/2))/3.

*Derivation.* For `m>=0` let `A_m = floor(2^(m+2)/3)`. Since
`ceil(log2(3k/4)) = m` iff `A_{m-1} < k <= A_m`, summing the layers gives
`F(n)=M n - sum_{m=0}^{M-1} A_m`. The sum evaluates by
`floor(2^(m+2)/3)=(2^(m+2)-r_m)/3`, where `r_m=1` for even `m` and `r_m=2`
for odd `m`; hence `sum r_m = floor(3M/2)`.

**Finite part `[experiment, exact integer arithmetic].`** Direct evaluation of
the formula and of `C(n) = bit_length(n!-1)` for `23<=n<=121` gives
`F(n)-C(n)>=1`, with equality exactly at `23,24,40,41,42,43`.

**All-n part `[deduction].`** For `n` in the `M`-layer write `a=2^M` and
`x=3n/(4a)`, so `1/2 < x <= 1`. The formula becomes

    F(n) = n log2 n + n*(log2 3 - 2 - log2 x - 1/x)
             + (4 + floor(3M/2))/3.

Use the standard Stirling upper bound

    ln(n!) <= (n+1/2) ln n - n + (1/2) ln(2*pi) + 1/(12n).

The function `phi(x)=log2 3 - 2 - log2 x - 1/x + 1/ln 2` is concave on
`(1/2,1]` (its second derivative is negative there), and
`phi(1/2)=phi(1)=log2 3 - 3 + 1/ln 2 =: c0 = 0.0276575...`. Hence
`phi(x)>=c0`. Combining with `floor(3M/2)>=(3M-1)/2` and
`M>=log2(3n/4)` gives

    F(n) - log2(n!) >= c0*n - 0.3666 - 1/(12 n ln 2).

For `n>=122` the right side exceeds 3; since
`C(n)=ceil(log2 n!) < log2(n!)+1`, this gives `F(n)-C(n)>=3`.
Together with the finite check this proves Theorem A. (The finite threshold is
not optimized; the asymptotic coefficient `c0` is intrinsic to the
Ford-Johnson formula.)

**Consequence for the front.** No Ford-Johnson tree can falsify the claim at any
`n>=23`, and the earlier computational check to `2*10^6` is now an all-`n`
statement. Any falsifier must be a genuinely different algorithm. At the six
one-gap sizes `23,24,40,41,42,43` it would have to beat Ford-Johnson by exactly
one comparison; at every other `n>=23` by at least two.

## 2. A linear-depth barrier for leaf-count lookahead at the antichain

This separates *soundness* of an extension-count lower bound from its
*completeness* for proving non-tightness.

For a poset `P`, let `e(P)` be its number of linear extensions, `F(P)` its exact
minimax sorting depth, and `L_0(P)=ceil(log2 e(P))`. Define the `t`-ply
extension-count lookahead

    L_0(P) = ceil(log2 e(P)),
    L_{t+1}(P) = 0                                      if P is total,
    L_{t+1}(P) = 1 + min_{x||y} max(L_t(P+x<y), L_t(P+y<x))  otherwise.

`L_1` is the one-ply bound in `docs/research-one-ply-obstruction.md`.

**Lemma `[deduction].`** For every `P` and `t>=0`,
`L_0(P) <= L_t(P) <= F(P)`.

*Proof.* `L_t<=F` is induction from `L_0<=F`. For `L_t>=L_0`: assume it at
`t`. For any incomparable pair, the larger child has at least `e(P)/2`
extensions, and `ceil(log2 ceil(e/2)) >= ceil(log2 e)-1`; hence the `max` over
the two children is at least `L_0(P)-1`, and adding one gives `L_{t+1}(P)>=L_0(P)`.
(The same calculation is the dominance theorem of the one-ply note.)

**Theorem B `[deduction].`** Let `A_n` be the antichain on `n` keys and
`C(n)=ceil(log2 n!)`. For every integer `t` with `0<=t<=floor(n/2)`,

    L_t(A_n) = C(n).

In particular, for every `t<=n/2` the `t`-ply leaf-count potential is exactly
the information bound and cannot certify `S(n)>C(n)`.

*Proof.* The lower bound is the lemma. For the upper bound let `P_s` be the
poset consisting of `s` disjoint 2-chains and `n-2s` isolated keys
(`0<=s<=floor(n/2)`). Then `e(P_s)=n!/2^s`, so
`L_0(P_s)=C(n)-s`. For `s<t`, `P_s` has two isolated keys; comparing them gives
two children isomorphic to `P_{s+1}`. Hence

    L_t(A_n) <= 1 + L_{t-1}(P_1) <= ... <= t + L_0(P_t)
             = t + (C(n)-t) = C(n).  ∎

Exact checks `[experiment]` for `n=3,4,5,6` and all `t<=floor(n/2)` reproduce
`L_t(A_n)=C(n)` (and `L_2(A_12)=29` was already checked on #301).

**Consequence.** If `S(n)>C(n)`, the convergence depth of this hierarchy at the
antichain is strictly larger than `n/2`. Thus a proof of strictness through
this natural family of sound lower-bound potentials needs at least linear
lookahead in `n`. The general-poset fence family `W_n` (`d(W_n)=Omega(n)`, #301)
does **not** give this antichain statement and does not transfer to `A_n`;
Theorem B is proved directly from the matching structure of `A_n`.

## 3. Falsification attempt and exact obstruction

- No explicit height-`C(n)` strategy is known for any `n>=23`. The first
  possible sizes are `n=23,24`, where `F(n)=C(n)+1`. Peczarski (2007) proved
  that no split-and-merge algorithm beats Ford-Johnson for `n<47`
  `[literature]`; this excludes the most obvious algorithmic family at the six
  one-gap sizes, but not all algorithms.
- An exhaustive forward/bidirectional search at `n=23` and budget `C(23)=75`
  is far outside the state sizes handled by Wells-Peczarski-Stober-Weiss
  (`n=18` already required days and large memory). No such search was run.
- The standard Wells one-sided forward search is **sound but not complete**:
  emptiness of a layer certifies `S(n)>C(n)`, but non-emptiness does not
  produce a tree. Stober-Weiss record that one-sided search suffices at
  `n=12` but not at `n=13,14` `[literature]`. Theorem B gives a stronger
  structural version of this incompleteness at the antichain for the
  adversarial `L_t` hierarchy: it is exactly `C(n)` for `t<=n/2`.

## 4. Honest limits

- The front remains `[open]`. This note proves neither `S(n)>C(n)` nor
  `S(n)=C(n)` for any `n>=23`, and does not determine `S(23)` or `S(24)`.
- Theorem A is arithmetic about the Ford-Johnson upper bound, not a lower
  bound on `S(n)`. Manacher's theorem that `F(n)>S(n)` for infinitely many `n`
  does not imply `S(n)>C(n)`.
- Theorem B is a barrier to a family of lower-bound methods (extension-count
  lookahead), not a statement that no proof exists. It does not rule out a
  certificate using global structure, a different potential, or a direct
  construction of a height-`C(n)` tree.
- General-poset results (fences, arbitrary partial orders, decision-tree
  hardness) are kept separate; none is used as a statement about `A_n`.
