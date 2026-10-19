# Compositional one-ply lower bounds and the failure of fixed-horizon lookahead

**Status (2026-10-18).** Research note with **proved** inequalities and a
small reproducible experiment. Not a Lean file and not a complexity-class
result. Every item is labelled `[definition]`, `[deduction]`,
`[literature]`, `[experiment]` or `[conjecture]`. Companion program:
`scripts/compositional_lookahead.py`; regression test:
`tests/test_compositional_lookahead.py`. This note **composes** the one-ply
adversarial information bound of `docs/research-one-ply-obstruction.md`
across ordinal-sum factors (the compositional bound `B`, §3), proves an
exact gap family `W^t` (§6), and derives a **negative result**: no fixed
lookahead horizon equals `F` on all posets (§5). It is distinct from
`docs/research-one-ply-obstruction.md` (global `L1` on a single state) and
from `docs/research-structural-lower-bounds.md` (merge-factor gaps of
`L0`); the object strengthened here is the *one-ply* bound, globally and
per factor.

## 1. Model and notation

`[definition]` From `docs/problem.md`. `F(P)` is the minimum remaining
worst-case number of pairwise comparisons that identifies the unknown linear
extension of a finite poset `P` (the algorithm knows `P`, the adversary
chooses the extension). A state is a transitively closed strict partial
order on `{0, ..., n-1}`, represented by `n` successor bitmasks. `e(P)` is
the number of linear extensions; `F(P) = 0` iff `P` is total, and
`F(antichain_n) = S(n)`.

`[definition]` For posets `A`, `B` on disjoint ground sets the **ordinal
sum** `A ⊕ B` places every element of `A` below every element of `B`; every
linear extension of `A ⊕ B` is an extension of `A` followed by one of `B`,
so `e(A ⊕ B) = e(A) · e(B)`. The **series decomposition** of `P` is
`P = P_1 ⊕ ⋯ ⊕ P_k` with the `P_i` the connected components of the
incomparability graph, totally ordered by the poset order
(Pouzet–Zaguia, Lemma 2.1 `[literature]`). Ordinal-sum additivity
`F(A ⊕ B) = F(A) + F(B)` (`docs/research-series-decomposition.md` §2,
Jain–Klauck–Sántha 2010 `[literature]`) gives the corollary

```
F(P) = F(P_1) + ⋯ + F(P_k).
```

## 2. The bounds

`[definition]` `L0(P) = ceil(log2 e(P))` — the information (leaf-counting)
bound; `F(P) >= L0(P)` because any decision tree distinguishing the `e(P)`
outcomes has depth `>= log2 e(P)` `[standard]`.

`[definition]` The **one-ply adversarial information bound** `L1` is a
single minimax ply whose children are scored by `L0` (see
`docs/research-one-ply-obstruction.md` §1 for the proof that
`L0 <= L1 <= F` pointwise).

`[definition]` The **horizon-r lookahead** `Lr(P, r)` generalises `L1` to
`r` minimax plies with leaves scored by `L0`:
`Lr(P, 0) = L0(P)`, `Lr(P, r+1) = 1 + min over incomparable {i,j} of
max(Lr(P+i<j, r), Lr(P+j<i, r))`, and `Lr(P, r) = 0` for total `P`.

`[definition]` The **compositional one-ply bound** is

```
B(P) = Σ_i L1(P_i),
```

the sum of the per-factor one-ply bounds over the series decomposition of
`P`. For a series-prime poset, `B(P) = L1(P)`.

## 3. Theorem 1: the soundness chain `L0 <= L1 <= B <= F`

`[deduction]` **Claim.** For every finite poset `P`,

```
L0(P) <= L1(P) <= B(P) <= F(P).
```

*Proof.*

1. `L0 <= L1`: Theorem 2 of `docs/research-one-ply-obstruction.md` (the
   larger child of any comparison has `>= ceil(e/2)` extensions).
2. `B <= F`: by Theorem 1 of the same note, `L1(P_i) <= F(P_i)` for every
   factor; summing and applying ordinal-sum additivity,
   `B(P) = Σ_i L1(P_i) <= Σ_i F(P_i) = F(P)`. ∎
3. `L1 <= B` (new). Fix any block `P_i` containing an incomparable pair
   (if `P` is total, `L1 = 0 <= B` trivially). Every incomparable pair of
   `P` lies inside some block. For a pair `{u,v}` inside block `P_i`, the
   two children are `(P_i + u<v) ⊕ ⊕_{j≠i} P_j` and `(P_i + v<u) ⊕ ⊕_{j≠i} P_j`,
   so by the product structure of the ordinal sum and
   `e(P_j) <= 2^{L0(P_j)}`,

   ```
   e(child) = e(P_i±) · Π_{j≠i} e(P_j) <= e(P_i±) · 2^{Σ_{j≠i} L0(P_j)},
   hence  L0(child) <= L0(P_i±) + Σ_{j≠i} L0(P_j).
   ```

   Taking `max` over the two children and then `min` over the pairs of
   block `P_i`,

   ```
   L1(P) <= 1 + (L1(P_i) - 1) + Σ_{j≠i} L0(P_j)
         = L1(P_i) + Σ_{j≠i} L0(P_j)
         <= L1(P_i) + Σ_{j≠i} L1(P_j) = B(P),
   ```

   using `L0 <= L1` per factor. ∎

`[experiment]` Exhaustive check of the full chain on every poset with
`n <= 5` elements (1 + 3 + 19 + 219 + 4231 = 4474 posets, shared memoized
`F`): **0 failures**. On the same range `B = L1` everywhere.
However, the earlier claim that the first strict example occurs at `n=10`
was **false**: already `A ⊕ V` with `A=(0,0)` (a 2-antichain)
and `V=(0,0,1,3,7)` (five keys) has `n=7` and

```
A:     e=2, L1=F=1
V:     e=8, L1=F=4
A⊕V:   e=16, L0=4, L1=4, B=5, F=1+4=5.
```

The full successor-mask tuple is `(124,124,0,0,4,12,28)`. The first
two components are incomparable within themselves but all keys in `A`
are below all keys in `V`. A bounded independent enumeration of all
series combinations with block-size splits `2+2`, `2+3`, `2+4`,
`3+3`, and `2+2+2` found no strict example for total size at most six;
the `n=7` construction is the **smallest found**. The `n=10`
family `W⊕W` remains useful because its gap extends to an explicit
unbounded additive family (§6).

## 4. Amplification along series powers

`[deduction]` **Claim.** For every poset `Q` and all `t, r >= 0`,

```
e(Q^t) = e(Q)^t,        F(Q^t) = t · F(Q),        Lr(Q^t, r) <= ceil(t · log2 e(Q)) + r,
```

where `Q^t = Q ⊕ Q ⊕ ⋯ ⊕ Q` (`t` copies).

*Proof.* The first two equalities are the product structure of the ordinal
sum and ordinal-sum additivity (§1). For the third, we first bound the
horizon-`r` lookahead on an **arbitrary** poset `P`:

```
Lr(P, r) <= ceil(log2 e(P)) + r          (*)
```

by induction on `r`. Base `r = 0` is equality. For the step, the two
children of any comparison partition the extensions, so
`max(e_left, e_right) <= e(P)`; hence for **every** pair,
`max(L0(left), L0(right)) <= ceil(log2 max(e_left, e_right)) <= L0(P)`.
Combining with the induction hypothesis on the children,

```
Lr+1(P) <= 1 + min_pairs max(Lr(child)) <= 1 + r + L0(P). ∎
```

Applying `(*)` to `P = Q^t` and using `e(Q^t) = e(Q)^t` gives
`Lr(Q^t, r) <= ceil(t · log2 e(Q)) + r`. ∎

`[experiment]` Direct exact checks of `e(Q^t) = 3^t` and
`Lr(Q^t, r) <= ceil(t log2 3) + r` for `Q = (2,0,0)`, `t <= 3`,
`r <= 2` (9 checks, `n <= 9`): all pass.

## 5. Negative result: no fixed horizon equals `F`

`[definition]` `Q = Merge(2, 1) = (2, 0, 0)`, the disjoint union (parallel
composition, `||`) of a 2-chain and a singleton. Its certified merge cost
is `F(Q) = M(1, 2) = ceil(log2 3) = 2` (Hwang–Lin 1972 `[literature]`; the
same poset `A = Merge(2,1)` with `e = 3`, `F = 2` appears in
`docs/research-structural-lower-bounds.md` §4a), and `e(Q) = 3`.

`[deduction]` **Claim.** For every fixed horizon `r >= 0` there exist
posets on which `Lr` is strictly below `F`: with `Q^t` as in §4,

```
Lr(Q^t, r) <= ceil(t · log2 3) + r  <  2t = F(Q^t)
```

as soon as `ceil(t · log2 3) + r < 2t` (note `log2 3 ≈ 1.585 < 2`).
Hence no fixed-horizon adversarial-information lookahead equals `F` on
all posets; the hierarchy `{Lr}_r` does not collapse to `F` at any finite
horizon.

`[experiment]` Minimal such `t` per horizon (pure arithmetic, plus the
direct §4 checks):

| r | minimal t | `Lr(Q^t) <=` | `F(Q^t) = 2t` |
|---|-----------|--------------|----------------|
| 0 | 3         | 5            | 6              |
| 1 | 5         | 9            | 10             |
| 2 | 8         | 15           | 16             |
| 3 | 10        | 19           | 20             |
| 4 | 13        | 25           | 26             |
| 5 | 15        | 29           | 30             |

`[conjecture]` On the family `Q^t` itself, `Lr` never catches `F` at fixed
`r` (the bound is asymptotically tight there: both sides are
`Θ(t)`), but this is not proved; the claim above only exhibits, per `r`,
single powers where the horizon fails.

## 6. Theorem 2: the exact gap family `W^t`

`[definition]` `W = (26, 0, 10, 0, 8)` is the smallest strict one-ply
witness (`docs/research-one-ply-obstruction.md` §3):
`e(W) = 8`, `L0(W) = 3`, `L1(W) = 4 = F(W)`, the four incomparable pairs
splitting the 8 extensions as `5/3, 5/3, 6/2, 6/2`.

`[deduction]` **Claim.** For every `t >= 1`, the `t`-fold series power
`W^t` satisfies

```
L1(W^t) = 3t + 1   (exactly),     B(W^t) = F(W^t) = 4t.
```

*Proof.* In `W^t`, two elements of different copies are comparable (cross
block order is fixed), so the incomparable pairs are exactly the within
copy pairs — four per copy, isomorphic to the pairs of `W`. Comparing a
pair inside copy `i` affects only that copy: the children are
`(W + u<v) ⊕ ⊕_{j≠i} W_j` and `(W + v<u) ⊕ ⊕_{j≠i} W_j`, with extension
counts `e(W±) · 8^{t-1}`. Since `8^{t-1} = 2^{3(t-1)}` is a power of two,

```
L0(child) = ceil(log2 e(W±)) + 3(t - 1).
```

For every pair of `W` the larger child has `e ∈ {5, 6}`, so
`ceil(log2 e) = 3` and `max(L0(left), L0(right)) = 3 + 3(t-1) = 3t`.
Every incomparable pair of `W^t` therefore yields exactly `1 + 3t`, the
minimum over pairs is `3t + 1`, and `L1(W^t) = 3t + 1`. Factorwise,
`B(W^t) = Σ_i L1(W) = 4t`, and additivity gives `F(W^t) = t · F(W) = 4t`. ∎

So on `W^t` the whole chain of Theorem 1 is simultaneously strict from the
second link onward:

```
t >= 2:   L0 = 3t   <   L1 = 3t+1   <   B = F = 4t,    gap B - L1 = t - 1 → ∞.
```

The **decomposed** one-ply bound is exactly tight on the whole family,
while the **global** one-ply bound falls behind by `t - 1`: composing
one-ply lookahead across series factors recovers `F` exactly here, which
no single-state one-ply ply (and, by §5, no fixed horizon at all) can do.

`[experiment]` Finite checks (no `n >= 15` minimax search; `F` at `t = 3`
comes from additivity):

| t | n  | e (direct DP) | L0 | L1 (direct, `t <= 2`) | B   | F   | gap `B - L1` |
|---|----|---------------|----|-----------------------|-----|-----|--------------|
| 1 | 5  | 8             | 3  | 4                     | 4   | 4   | 0            |
| 2 | 10 | 64            | 6  | 7                     | 8   | 8   | 1            |
| 3 | 15 | 512           | 9  | 10 (proved formula)   | 12  | 12  | 2            |

At `t = 3` the exact mechanism behind `L1 = 3·3 + 1 = 10` is verified
directly: the representative pairs `{0,2}` and `{2,4}` of the first copy
have children with `e = 320, 192` and `384, 128` respectively
(`= 3·64, 5·64` and `2·64, 6·64`), each with `ceil(log2 e) = 9 = 3t`.

## 7. The capped linear-extension polynomial-space prune (implemented)

`[definition]` `docs/research-one-ply-obstruction.md` §2 states a safe
pruning rule for a budgeted decision procedure `CanSort(P, d)`: if `d > 0`
and **every** incomparable pair has an outcome child with
`e(child) > 2^{d-1}`, return `FALSE`. The note proved this is exactly the
test `L1(P) > d` and described a polynomial-space implementation by
capped extension enumeration, explicitly **not** implemented there. It is
now implemented in `scripts/compositional_lookahead.py`
(`capped_pair_census`, `prune_verdict`).

`[deduction]` **Exact equivalence.** With `e <= 2^d` extensions enumerated
once and pair counters `c_ij` = extensions with `i` before `j`, the child
counts are `c_ij` and `e - c_ij`, so

```
L1(P) > d   ⟺   every pair has max(c_ij, e - c_ij) > 2^(d-1)
```

(`ceil(log2 m) >= d ⟺ m > 2^(d-1)`), and if more than `2^d` extensions
are seen the ordinary information bound already rejects. Soundness
(`prune fires ⟹ F > d`) is Theorem 1 of the one-ply note. Edge cases: a
total poset has no incomparable pairs and `F = 0 <= d` for all `d >= 0`, so
it is never rejected; at `d = 0` the prune fires exactly on the non-total
posets, matching `L1 > 0`; `d < 0` rejects outright.

**Positive space constraint.** `capped_pair_census` enumerates linear
extensions by DFS with a cap of `2^d + 1`, using one counter per pair:
`O(n^2 (d+1))` bits of counters plus an `O(n)`-deep stack — polynomial
space, never allocating a full-downset array. Amortized time: every prefix
of a linear extension of a finite poset extends to at least one whole
extension, so the DFS visits at most `n · (2^d + 1)` prefixes and at most
`2^d + 1` leaves; each prefix tests `O(n)` candidate minimal elements
against predecessor masks and each leaf does `O(n^2)` counter work —
conservative worst case `O(n^2 · 2^d)`. Composed with the budgeted DFS of
`docs/research-budgeted-dfs.md` it stays within the existing
`2^{O(n log^2 n)}` worst case.

**Negative space constraint (prototype distinction).** The reference exact
tool `linear_extensions` (downset DP) uses `Theta(2^n)` space; it is a
*prototype* for the bounded regression and experiments, not a
polynomial-space tool, and the two are kept explicitly distinct in the
script (the census allocates no `2^n` array).

`[experiment]` Prune regression, all posets `n <= 4`, `0 <= d <= 4`
(1210 checks): `prune_verdict(P, d)` returns `False` **iff** `L1(P) > d`
in every check; the prune fires 471 times and always with `F > d`. At the
`n = 5` witness `W` it fires at `d = 3` even though `e(W) = 8 <= 2^3` (the
ordinary information prune is silent there), and is inconclusive at
`d = 4 = L1(W)`.

## 8. Complexity caveats (explicit)

`[definition]` Exact `e(P)` is `#P`-complete to compute in general, so
neither `L0`, `L1`, `Lr` nor `B` is claimed to be polynomial-time
computable: `B` needs the (polynomial-time detectable, §1) series
decomposition plus one exact `L1` per factor, each requiring exact
extension counts. The one-ply minimum costs `O(n^2)` extension-count
subcalls per state; it is cheaper than the full optimal min-max only
empirically.

* **Not established:** any asymptotic bound, any complexity-class
  statement, any polynomial-time exact algorithm, and `S(12) = 30`. A
  comparison lower bound on `S(n)` is not a complexity lower bound for
  *computing* `S(n)` (`docs/problem.md`).
* The §5 no-fixed-horizon result concerns the **strength of lookahead
  lower bounds**, not the depth at which some other method computes `F`;
  it is not a hardness result for any language.
* The §7 prune is a *safe* (never-false-negative) rejection test inside a
  budgeted search, not a decision procedure.

## 9. Novelty assessment

* **Standard:** `L0 <= L1 <= F` (one-ply note); ordinal-sum additivity and
  the series decomposition (§1); the capped-enumeration prune (one-ply
  note §2); certified merge values (Hwang–Lin 1972;
  Stockmeyer–Yao 1980).
* **Deductions in this note:** the chain `L0 <= L1 <= B <= F` (Theorem 1,
  including the new `L1 <= B`); the amplification inequalities (§4); the
  no-fixed-horizon negative result (§5); the exact `W^t` computation
  `L1 = 3t + 1` vs `B = F = 4t` with unbounded gap (Theorem 2); the
  implementation and amortized analysis of the polynomial-space prune (§7).
* **Empirical in this note:** the `n <= 5` chain regression (0 failures), the strict
  `n=7` witness `A⊕V`, the `W^t` table, the amplification
  table, and the 1210-check prune equivalence regression.

## 10. Reproducing

```
python3 scripts/compositional_lookahead.py            # bounded fast regression (~0.2 s)
python3 scripts/compositional_lookahead.py --prune   # + capped polynomial-space prune checks
python3 -m unittest tests.test_compositional_lookahead -q   # < 1 s
python3 -m unittest discover -s tests -v              # full CI suite
```

The default CLI is deliberately bounded: exhaustive chain regression for
`n <= 4` (extendable to `n <= 5` via `--regression-max-n 5`), the witness
family `W^t` for `t <= 2` directly (`t <= 3` with the proved-formula
mechanism, `--witness-t 3`), and no exhaustive `n >= 6` minimax search and
no `n >= 15` computation of any kind. No randomness, no network.

## 11. Sources

1. Project model and the standing warning that a comparison lower bound on
   `S(n)` is not a complexity lower bound for computing `S(n)`:
   `docs/problem.md`.
2. The one-ply bound `L1`, its theorems `L0 <= L1 <= F`, the §2 pruning
   corollary and its polynomial-space implementation sketch, and the
   smallest strict witness `W = (26, 0, 10, 0, 8)`:
   `docs/research-one-ply-obstruction.md`.
3. Ordinal-sum additivity `F(A ⊕ B) = F(A) + F(B)`, the series
   decomposition (Pouzet–Zaguia Lemma 2.1; Erné–Stege 1995), and the
   subset counterexample: `docs/research-series-decomposition.md`.
4. `Merge(2,1)` with `e = 3`, `F = 2` (§4a) and the certified merge ranges
   used for `M(1, 2) = ceil(log2 3) = 2`:
   `docs/research-structural-lower-bounds.md`.
5. Budgeted DFS worst case `2^{O(n log^2 n)}` that the §7 prune composes
   with: `docs/research-budgeted-dfs.md`.
6. Sorting-number literature baseline (`S(7) = 13`, `S(8) = 16`,
   `S(12) = 30`): `docs/literature.md`.

The definitions of `Lr` and `B`, Theorems 1–2, the §4–5 amplification and
no-fixed-horizon argument, the §7 implementation/amortization, and all
tables are original to this note; the `e = 8`, `m = 4` witness `W` is the
smallest strict instance of the one-ply bound, reused as the base of the
`W^t` family.
