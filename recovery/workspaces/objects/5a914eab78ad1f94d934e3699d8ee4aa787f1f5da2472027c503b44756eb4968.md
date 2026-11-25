# Structural lower bounds from extension monotonicity and merge factors

**Status (2026-10-18).** Two candidate pruning rules for the exact minimax
sorting number are stated and checked: extension monotonicity and a
compositional lower bound that strictly improves on the information bound.
The smallest explicit witness where the latter beats leaf counting is
`Merge(2, 4)` on `n = 6`. All checks are experimental and bounded to `n ≤ 5`
exhaustive plus targeted `n = 6`; no asymptotic or complexity-class claim is
made. The merge costs are used only inside literature-certified ranges; no
universal `a + b - 1` formula is assumed.

## 1. Model and definitions

Let `F(P)` be the worst-case minimum number of further pairwise comparisons
needed to identify the unknown linear extension of a finite poset `P` (the
algorithm knows `P`, the adversary chooses the extension). For the antichain
on `n` elements, `F(antichain_n) = S(n)`. This is the exact query complexity of
*sorting under partial information* (SUPI). A state is represented by the
transitive closure of the known relations as `n` successor bitmasks, exactly as
in `scripts/series_decomposition_probe.py`.

**Definition.** For a poset `P`, `e(P)` is its number of linear extensions and

```
info(P) := ceil(log2 e(P))
```

is the *information bound*. Any decision tree distinguishing the `e(P)` outcomes
has depth at least `log2 e(P)`, hence `F(P) ≥ info(P)` (`[standard]`).

**Definition (merge factor).** `Merge(a, b)` is the disjoint union of an
`a`-chain and a `b`-chain (parallel composition, *no* cross relations). Its
comparability graph is a disjoint union of two cliques. `F(Merge(a, b)) = M(a, b)`
is the exact minimax two-list merge cost, and the *merge gap* is

```
delta(a, b) := M(a, b) - ceil(log2 C(a+b, a)).
```

**Certified merge values (`[literature]`).** The probe uses only these ranges:

* `M(1, b) = ceil(log2(b+1))` (Hwang–Lin 1972).
* `M(a, b) = a + b - 1` for `a ≤ b ≤ floor(3a/2) + 1` (Stockmeyer–Yao 1980;
  Christen 1978; Murphy–Paull 1979).
* outside these ranges the value is `None` (uncertified). In particular
  `M(2, 5)`, `M(3, 6)` and `M(4, 8)` are **not** guessed.

## 2. Theorem A: extension monotonicity

**Claim (`[deduction]`).** If `P ⊆ Q` on the same labelled ground set, then
`F(P) ≥ F(Q)`.

*Proof.* `Q` has at least the relations of `P`, so `L(Q) ⊆ L(P)`. Any decision
tree that distinguishes every linear extension of `P` distinguishes every
element of the subset `L(Q)`. Hence the optimal tree for `P` is also a valid
tree for `Q`, giving `F(Q) ≤ F(P)`. ∎

The check `check_monotonicity_covers(5)` verifies the inequality for every
*cover* `P < Q` (one added comparability and its transitives) on `n ≤ 5`;
transitivity along cover chains gives all comparable pairs. Result: 36748
cover checks, 0 failures (`[experiment]`).

## 3. Theorem B: compositional structural lower bound

Let `P = P_1 ⊕ ⋯ ⊕ P_k` be the ordinal-sum (series) decomposition of `P` into
its incomparability-graph components. For each block define `delta_i` as the
certified merge gap when `P_i` is a certified `Merge(a_i, b_i)`, and `delta_i = 0`
otherwise.

**Claim (`[deduction]`).**

```
F(P) ≥ Σ_i ceil(log2 e(P_i)) + Σ_i delta_i
     ≥ info(P) + Σ_i delta_i .
```

*Proof.*

1. *Additivity.* `F(P) = Σ_i F(P_i)` (`[deduction]`; deterministic direct-sum
   for decision trees, see `docs/research-series-decomposition.md` §2, and the
   standard result of Jain–Klauck–Sántha 2010).
2. *Block bounds.*
   * Singleton or chain: `F = 0`, `e = 1`, `info = 0`, `delta = 0`.
   * Certified `Merge(a, b)`: `F = M(a, b) = ceil(log2 C(a+b, a)) + delta`
     `= info + delta` exactly.
   * Other block: `F ≥ info` by the information bound, `delta = 0`.
   Hence `F(P_i) ≥ info(P_i) + delta_i` for every `i`.
3. *Sum and combine.* `e(P) = Π_i e(P_i)`, so
   ```
   F(P) = Σ_i F(P_i) ≥ Σ_i info(P_i) + Σ_i delta_i
        ≥ info(P) + Σ_i delta_i,
   ```
   using `ceil(log2 x) + ceil(log2 y) ≥ ceil(log2(xy))`. ∎

**Pruning rule.** In a minimax search with remaining budget `d`, prune if
`Σ_i info(P_i) + Σ_i delta_i > d`. This is at least as strong as the earlier
global-information formula `info(P)+Σ_i delta_i`. Crucially, even when every
`delta_i = 0`, adding the factor-wise ceilings can beat the global ceiling. This is a valid lower bound and
is the candidate rule checked here. It requires computing `e(P)` and the
series decomposition; its practical value is untested.

## 4. The smallest strict witness

`Merge(2, 4)` has `e = C(6, 2) = 15`, so `info = ceil(log2 15) = 4`. Its merge
cost is certified (`b = 4 ≤ floor(3·2/2) + 1 = 4`), `M(2, 4) = 5`, so
`delta = 1` and `F = 5`. The structural bound gives `4 + 1 = 5`, strictly
stronger than the information bound `4`. In bitmask form the witness is

```
(2, 0, 56, 48, 32, 0)
```

with elements `{0,1}` a 2-chain, `{2,3,4,5}` a 4-chain, all cross pairs
incomparable.

Exhaustive enumeration for `n ≤ 5` has **no** strict witness (4474 posets, 0
failures, 0 strict). On `n = 6` the 720 strict witnesses are exactly the
relabelings of `Merge(2, 4)` (`[experiment]`).

## 4a. Rounding alone can yield a strict bound

**An additional `n=7` witness (`[deduction]` + `[experiment]`).**
Take `A = Merge(2,1)`, the disjoint union of a 2-chain and an isolated key.
It has `e(A)=3` and `F(A)=2`. Let `B` be the four-key poset with successor
bitmasks `(2,0,0,6)`, for which the reference evaluator verifies
`e(B)=5` and `F(B)=3`. Then `P=A ⊕ B` has

```
 e(P)=15,  info(P)=ceil(log2 15)=4,
 block-local bound=ceil(log2 3)+ceil(log2 5)=2+3=5,
 F(P)=F(A)+F(B)=2+3=5.
```

Neither factor requires a positive certified merge gap. The improvement
comes entirely from taking the ceilings *before* multiplying the extension
counts. This is a structural lower-bound strengthening, not a faster
algorithm for arbitrary `S(n)`; computing each `e(P_i)` may itself cost
exponential time (although it uses smaller blocks than computing `e(P)`
directly). The main `n=6` `Merge(2,4)` witness remains the smallest
strict example examined in this project.

## 5. Experimental results

`python3 scripts/structural_lower_bounds.py` (`[experiment]`).

| n | posets | monotonicity cover checks | Theorem B failures | strict witnesses |
|---|--------|---------------------------|--------------------|------------------|
| 0 | 1      | —                         | 0                  | 0 |
| 1 | 1      | —                         | 0                  | 0 |
| 2 | 3      | —                         | 0                  | 0 |
| 3 | 19     | —                         | 0                  | 0 |
| 4 | 219    | —                         | 0                  | 0 |
| 5 | 4231   | 36748 total               | 0                  | 0 |

Targeted `n = 6` merge states (plain minimax):

| state | e | info | bound | F |
|-------|---|------|-------|---|
| `Merge(1, 5)` | 6 | 3 | 3 | 3 |
| `Merge(2, 4)` | 15 | 4 | 5 | 5 |
| `Merge(3, 3)` | 20 | 5 | 5 | 5 |
| `Merge(2, 3) ⊕ singleton` | 10 | 4 | 4 | 4 |
| `Merge(2, 2) ⊕ singleton ⊕ singleton` | 6 | 3 | 3 | 3 |

## 6. Scope, caveats, novelty

* **Not established:** any asymptotic bound, any complexity-class statement, or
  any polynomial-time exact algorithm. The bound is a structural lower bound,
  not a hardness result.
* **Merge costs.** Only the literature-certified ranges are used. The formula
  `M(a, b) = a + b - 1` is *not* universal; outside the certified ranges the
  probe returns `None` rather than guessing.
* **Tightness.** The bound is exact for certified merge factors
  (`F = M = info + delta`) but for "other" blocks it reduces to the
  information bound. It is therefore a strengthening of leaf counting only
  when certified merge factors occur.
* **Cost of the rule.** Computing `e(P)` and the decomposition is not free; the
  probe does not measure the trade-off in a search.
* **Novelty (`[literature]` / `[deduction]` / `[experiment]`).** Extension
  monotonicity and the information bound are standard; ordinal-sum additivity is
  the deterministic direct-sum theorem. The compositional combination of the
  two into Theorem B is a deduction; the `n ≤ 5` exhaustive and `n = 6`
  targeted checks are the empirical content of this note.

## 7. Reproducibility

```
python3 scripts/structural_lower_bounds.py
python3 -m unittest discover -s tests -v
```

`tests/test_structural_lower_bounds.py` checks the known `e`/`F` values, the
cover monotonicity, the structural bound over all `n ≤ 5` posets, the absence
of a strict witness below `n = 6`, the `Merge(2, 4)` witness, the certified
merge ranges, and that uncertified merge sizes return `None`. No randomness, no
network, no exhaustive `n ≥ 6` search.
