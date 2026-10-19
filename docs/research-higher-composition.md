# Higher composition: the decomposed bound `B_r` dominates global `L_r`

**Status (2026-10-18).** Research note with a **proved** theorem and a
small reproducible experiment. Not a Lean file and not a complexity-class
result. Every item is labelled `[definition]`, `[deduction]`,
`[literature]`, `[experiment]` or `[conjecture]`. Companion program:
`scripts/higher_composition.py`; regression tests:
`tests/test_higher_composition.py`. This note **composes** the
horizon-`r` adversarial information bound `L_r` of
`docs/research-lookahead-hierarchy.md` across maximal ordinal-sum factors
(the higher-composition bound `B_r`, §2), proves that `B_r` dominates the
global `L_r` while staying below `F` (§3), and derives a **negative
result**: on the families `Q^t` and `W^t` the decomposed bound is exactly
tight while the global one falls behind by an unbounded margin at every
fixed horizon (§5–6). It is distinct from
`docs/research-compositional-lookahead.md` (one-ply only, `B = Σ L_1`)
and from `docs/research-lookahead-hierarchy.md` (global hierarchy only);
the object strengthened here is the whole hierarchy, factorwise.

## 1. Model and notation

`[definition]` From `docs/problem.md`. `F(P)` is the minimum remaining
worst-case number of pairwise comparisons that identifies the unknown linear
extension of a finite poset `P` (the algorithm knows `P`, the adversary
chooses the extension). A state is a transitively closed strict partial
order on `{0, ..., n-1}`, represented by `n` successor bitmasks. `e(P)` is
the number of linear extensions; `F(P) = 0` iff `P` is total, and
`F(antichain_n) = S(n)`.

`[definition]` For posets `A`, `B` on disjoint ground sets the **ordinal
sum** `A ⊕ B` places every element of `A` below every element of `B`;
every linear extension of `A ⊕ B` is an extension of `A` followed by one
of `B`, so `e(A ⊕ B) = e(A) · e(B)`. The **series decomposition** of `P`
is `P = P_1 ⊕ ⋯ ⊕ P_k` with the `P_i` the connected components of the
incomparability graph, totally ordered by the poset order (Pouzet–Zaguia,
Lemma 2.1 `[literature]`). Ordinal-sum additivity
`F(A ⊕ B) = F(A) + F(B)` (`docs/research-series-decomposition.md` §2,
Jain–Klauck–Sántha 2010 `[literature]`) gives `F(P) = Σ_i F(P_i)`.

`[definition]` The **adversarial lookahead hierarchy** (`r ≥ 0`):
`L_0(P) = ceil(log2 e(P))` (information bound) and
`L_{r+1}(P) = 0` if `P` is total, else
`1 + min` over incomparable `{i,j}` of `max(L_r(P+i<j), L_r(P+j<i))`.
`L_1` is the one-ply bound of `docs/research-one-ply-obstruction.md`;
`L_0 ≤ L_1 ≤ ⋯ ≤ L_r ≤ F` pointwise
(`docs/research-lookahead-hierarchy.md` Theorem 1) and
`L_r ≤ L_0 + r` (derivative bound, Theorem 2 there).

## 2. The higher-composition bound

`[definition]` The **higher-composition bound** is

```
B_r(P) = Σ_i L_r(P_i),
```

the sum of the per-factor horizon-`r` bounds over the series
decomposition of `P`. For a series-prime poset, `B_r = L_r`. It is the
`r`-fold generalisation of the compositional one-ply bound `B = Σ L_1` of
`docs/research-compositional-lookahead.md` §3.

## 3. Theorem: the chain `L_r ≤ B_r ≤ F` and monotonicity

`[deduction]` **Claim.** For every `r ≥ 0` and every finite poset `P`,

```
L_r(P) ≤ B_r(P) ≤ F(P),
```

and `B_r` is nondecreasing in `r`.

*Proof.* We use one lemma and the two standing facts `L_r ≤ F` and
`L_r ≤ L_{r+1}` (hierarchy Theorems 1).

*Lemma (ordinal-sum subadditivity).* For all finite posets `A`, `B` and all
`r ≥ 0`, `L_r(A ⊕ B) ≤ L_r(A) + L_r(B)`.

*Proof of lemma*, by induction on `r`. Base `r = 0`: `e(A⊕B) = e(A)e(B)`
and `ceil(log2(xy)) ≤ ceil(log2 x) + ceil(log2 y)`, since
`xy ≤ 2^{a}·2^{b}` with `a = ceil(log2 x)`, `b = ceil(log2 y)`. Step:
the incomparable pairs of `A ⊕ B` are exactly those of `A` and those of
`B` (all cross pairs are comparable). For a pair `{i,j}` inside `A` the
children are `(A+i<j) ⊕ B` and `(A+j<i) ⊕ B`, so by the induction
hypothesis `max(L_r children) ≤ max(L_r(A±)) + L_r(B)`. Taking the minimum
over the pairs of `A` gives `L_{r+1}(A⊕B) ≤ L_{r+1}(A) + L_r(B)`; the same
argument with `B` gives the symmetric bound, hence
`L_{r+1}(A⊕B) ≤ L_{r+1}(A) + L_{r+1}(B)`. ∎

*Main claim*, by induction on `r`.

*Base `r = 0`.* With `P = P_1 ⊕ ⋯ ⊕ P_k`,
`L_0(P) = ceil(log2 Π_i e(P_i)) ≤ Σ_i ceil(log2 e(P_i)) = B_0(P)` by the
`r = 0` case of the lemma (applied `k − 1` times, or directly: `Π e_i ≤
Π 2^{ceil(log2 e_i)}`). Upper: `B_0(P) = Σ L_0(P_i) ≤ Σ F(P_i) = F(P)`.

*Step.* Assume `L_r(P) ≤ B_r(P) ≤ F(P)` for all `P`. For non-total `P`,
every incomparable pair lies inside a unique factor `P_i`; its two
children are `(P_i+i<j) ⊕ ⊕_{j≠i} P_j` and `(P_i+j<i) ⊕ ⊕_{j≠i} P_j`, so
by the lemma at horizon `r`,

```
L_r(child) ≤ L_r(P_i±) + Σ_{j≠i} L_r(P_j).
```

Taking `max` over the two children of any pair of factor `i` and then
`min` over the pairs of that factor,

```
L_{r+1}(P) ≤ 1 + max(L_r(P_i±)) + Σ_{j≠i} L_r(P_j)
           = L_{r+1}(P_i) + Σ_{j≠i} L_r(P_j)
           ≤ Σ_j L_{r+1}(P_j) = B_{r+1}(P),
```

using `L_r ≤ L_{r+1}` per factor. Upper: `B_{r+1}(P) = Σ L_{r+1}(P_i) ≤
Σ F(P_i) = F(P)` since `L_{r+1} ≤ F` pointwise. Monotonicity of `B_r` in
`r`: `B_{r+1} − B_r = Σ_i (L_{r+1} − L_r)(P_i) ≥ 0`. ∎

*Edge cases.* Empty `n = 0` and total `P`: one factor, no pairs,
`L_r = B_r = F = 0`. Multi-component `P`: covered verbatim — the proof
only ever uses the series decomposition. Series-prime `P`: `B_r = L_r`, so
the chain collapses to the hierarchy chain and no strictness arises.

`[experiment]` Exhaustive check of `L_r ≤ B_r ≤ F` and of the monotonicity
`B_r ≤ B_{r+1}` on every labelled poset with `n ≤ 4` (1 + 3 + 19 + 219 =
242 posets), `r ≤ 4`: **0 failures** (in CI). An offline run extended to
`n ≤ 5` (4473 posets): again 0 failures. Moreover `B_r = L_r` on **every**
poset with `n ≤ 5`: for `r ≥ 1` this is forced by the literature fact
`L_1 = F` for `n ≤ 5` (`docs/research-lookahead-hierarchy.md` §5.1), since
then `L_r = F` and `B_r ≤ F`; for `r = 0` the exhaustive run also found
no rounding strictness `Σ ceil(log2 e_i) > ceil(Σ log2 e_i)` at `n ≤ 5`.
Strict examples exhibited here (minimality not established in general):
`r = 0` at `Q^3` (`n = 9`): `L_0 = 5 < 6 = B_0 = F`; `r = 1` at `A ⊕ V`
(`n = 7`, the strict one-ply witness of
`docs/research-compositional-lookahead.md` §3, where no strict example of
total size ≤ 6 exists); and `r ≥ 2` at `W^2` (`n = 10`): `L_1 = L_2 = 7 < 8
= B_1 = B_2 = F`.

## 4. Amplification along series powers

`[deduction]` **Claim.** For every poset `Q` and all `t, r ≥ 0`,

```
e(Q^t) = e(Q)^t,        F(Q^t) = t · F(Q),
        L_r(Q^t) ≤ ceil(t · log2 e(Q)) + r.
```

*Proof.* The first two are the product structure of the ordinal sum and
ordinal-sum additivity (§1); never recompute `F(Q^t)` by direct minimax on
the large state. For the third, the hierarchy derivative bound
(`docs/research-lookahead-hierarchy.md` Theorem 2) gives
`L_r(P) ≤ L_0(P) + r = ceil(log2 e(P)) + r` for *every* `P`; apply it to
`P = Q^t`. ∎

## 5. Negative result I: `Q^t`

`[definition]` `Q = Merge(2, 1) = (2, 0, 0)`, the disjoint union of a
2-chain and a singleton: `e(Q) = 3`, `F(Q) = 2` (Hwang–Lin 1972
`[literature]`; `docs/research-structural-lower-bounds.md` §4a).
Since `L_0(Q) = ceil(log2 3) = 2 = F(Q)` and the hierarchy is nondecreasing
and bounded by `F`, `L_r(Q) = 2` for **every** `r`.

`[deduction]` **Claim.** For every `r ≥ 0` and every `t ≥ 1`,

```
B_r(Q^t) = F(Q^t) = 2t        (exact, for all r),
          L_r(Q^t) ≤ ceil(t · log2 3) + r.
```

`log2 3 ≈ 1.585 < 2`, so `ceil(t log2 3) + r < 2t` once `t` is large
enough **for each fixed `r`**: the global horizon-`r` bound falls behind the
exact value by an unbounded margin, while the decomposed bound is tight
everywhere on the family. This is a strong form of the no-fixed-horizon
negative result of `docs/research-compositional-lookahead.md` §5, now at
every horizon and with the decomposed bound matching `F` exactly.

`[experiment]` Direct exact checks (`t ≤ 3`, `r ≤ 2`, `n ≤ 9`): `e(Q^t) =
3^t`, `L_r(Q^t) ≤ ceil(t log2 3) + r`, `B_r(Q^t) = 2t` in all checks;
`L_r(Q) = 2` for `r ≤ 3`. The minimal `t` per horizon (pure arithmetic):

| r | minimal t | `L_r(Q^t) ≤` | `F(Q^t) = 2t` |
|---|-----------|--------------|----------------|
| 0 | 3         | 5            | 6              |
| 1 | 5         | 9            | 10             |
| 2 | 8         | 15           | 16             |
| 3 | 10        | 19           | 20             |
| 4 | 13        | 25           | 26             |
| 5 | 15        | 29           | 30             |

## 6. Negative result II: `W^t`

`[definition]` `W = (26, 0, 10, 0, 8)`, the smallest strict one-ply
witness (`docs/research-one-ply-obstruction.md` §3): `e(W) = 8`,
`L_0(W) = 3`, `L_1(W) = 4 = F(W)`. By monotonicity and `L_r ≤ F`,
`L_r(W) = 4` for **every** `r ≥ 1`.

`[deduction]` **Claim.** For every `t ≥ 1` and every `r ≥ 1`,

```
B_r(W^t) = F(W^t) = 4t        (exact),
          L_r(W^t) ≤ L_0(W^t) + r = 3t + r.
```

Since `3t + r < 4t` once `t > r`, the global bound falls behind by an
unbounded margin at every fixed horizon `r ≥ 1` (at `r = 0`,
`B_0(W^t) = 3t < 4t = F(W^t)` already). The decomposed bound at horizon
`r = 1` recovers `F` exactly on the whole family, while the exact global
one-ply value is `L_1(W^t) = 3t + 1`
(`docs/research-compositional-lookahead.md` §6).

`[experiment]` Direct exact checks (`t ≤ 2`, `r ≤ 2`, `n ≤ 10`): `e(W^t) =
8^t`; `W^2`: `L_0 = 6`, `L_1 = 7`, `L_2 = 7`, `B_0 = 6`, `B_1 = B_2 = 8 =
F(W^2)`; strict global gap `L_r(W^2) < B_r(W^2)` at every `r ≥ 1` (at
`r = 0` both equal `6`: `W^2` has two factors so `B_0 = 2·L_0(W) = 6`
with no rounding slack). `F` at the powers comes from additivity
(`t · F(W) = 4t`), never from a minimax search on the 10-element state.

## 7. Complexity caveats (explicit)

* **No class separation, no algorithm lower bound.** The §5–6 results
  concern the *strength of lookahead lower bounds*, not the resources of
  any algorithm and not the depth at which some other method computes `F`.
  Nothing here bears on the membership of `S_unary`, `S_binary`,
  `SORT-BOUND-U` or `SORT-BOUND-B` in `P`, `NP`, `EXPTIME` or any other
  class, and no separation is claimed (`docs/problem.md`).
* **No asymptotic computation claim.** Exact `e(P)` is #P-complete in
  general (Brightwell–Winkler 1991 `[literature]`), so neither `L_r` nor
  `B_r` is claimed polynomial-time computable; `B_r` needs the
  series decomposition (polynomial-time detectable, §1) plus one exact
  `L_r` per factor.
* **Finiteness of the experiments.** The regressions cover all labelled
  posets with `n ≤ 4` and the targeted powers `Q^t` (`t ≤ 3`), `W^t`
  (`t ≤ 2`); these are finite consistency checks of the proved
  inequalities, not asymptotic evidence. The gap statements §5–6 are
  proved for all `t`, `r` by the arithmetic of §4–6, independent of the
  experiments.

## 8. Novelty assessment

* **Standard:** `L_0 ≤ L_r ≤ F`, `L_r ≤ L_0 + r`, `L_r ≤ L_{r+1}`
  (hierarchy note); ordinal-sum additivity, the series decomposition
  (§1); `Merge(2,1)` with `e = 3`, `F = 2` (Hwang–Lin 1972);
  the witness `W` and `L_1(W^t) = 3t + 1` (one-ply note, compositional
  note §6).
* **Deductions in this note:** the ordinal-sum subadditivity lemma for
  `L_r` (§3); the chain `L_r ≤ B_r ≤ F` and monotonicity of `B_r` for all
  `r ≥ 0` (§3, Theorem); the exact tightness `B_r(Q^t) = F(Q^t) = 2t`
  (§5) and `B_r(W^t) = F(W^t) = 4t` for `r ≥ 1` (§6), with the global
  gap `ceil(t log2 3) + r < 2t` resp. `3t + r < 4t` at every fixed
  horizon.
* **Empirical in this note:** the `n ≤ 4` chain regression (0 failures,
  in CI), its offline extension to `n ≤ 5`, and the `Q^t`, `W^t` direct
  checks locating the first strict examples (`Q^3` at `r = 0`, `W^2` at
  `r ≥ 1`).

## 9. Reproducing

```
python3 scripts/higher_composition.py                 # bounded fast regression (~1 s)
python3 -m unittest tests.test_higher_composition -q  # < 5 s
python3 -m unittest discover -s tests -v               # full CI suite
```

The CLI is deliberately bounded: exhaustive chain regression for
`n ≤ 4` (extendable to `n ≤ 5` via `--max-n 5`), direct checks of `Q^t`
for `t ≤ 3` and `W^t` for `t ≤ 2` at horizons `r ≤ 2` (via `--q-t`,
`--q-r`, `--w-t`, `--w-r`), and no exhaustive `n ≥ 6` minimax search and
no `n ≥ 10` direct minimax. No randomness, no network.

## 10. Sources

1. Project model, encodings, and the standing warning that a comparison
   lower bound on `S(n)` is not a complexity lower bound for computing
   `S(n)`: `docs/problem.md`.
2. The hierarchy `L_0 ≤ L_1 ≤ ⋯ ≤ L_r ≤ F`, monotonicity, and the
   derivative bound `L_r ≤ L_0 + r`: `docs/research-lookahead-hierarchy.md`.
3. The one-ply bound `L_1`, its theorems, the witness `W`, and the exact
   `L_1(W^t) = 3t + 1`: `docs/research-one-ply-obstruction.md`,
   `docs/research-compositional-lookahead.md`.
4. Ordinal-sum additivity `F(A ⊕ B) = F(A) + F(B)`, the series
   decomposition (Pouzet–Zaguia Lemma 2.1; Erné–Stege 1995):
   `docs/research-series-decomposition.md`.
5. `Merge(2,1)` with `e = 3`, `F = 2`: `docs/research-structural-lower-bounds.md`.
6. #P-completeness of exact linear-extension counting: Brightwell–Winkler
   1991 (quoted in `docs/research-lookahead-hierarchy.md` §7).

The definition of `B_r`, the subadditivity lemma, the §3 Theorem, the
§5–6 exact-tightness and gap computations, and all tables are original to
this note.
