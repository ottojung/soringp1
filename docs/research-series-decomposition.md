# Series (ordinal-sum) decomposition of the exact minimax sorting number

**Status (2026-10-18).** The identity `F(A ⊕ B) = F(A) + F(B)` is a *deduction*
from the deterministic direct-sum theorem for decision trees applied to the
ordinal sum of posets. The associated decomposition is a *standard literature
result*. The practical DP finding is a *negative empirical observation* for
`n ≤ 5`: the rule is exact but does not reduce the state space, and the fraction
of decomposable states decreases over the measured range. No Lean formalization
is proposed.

## 1. Model and definitions

The exact minimax evaluator `SoringP1/Minimax.lean` computes

```
adv S = 0                                    if |S| ≤ 1
      = 1 + min over splitting pairs (i,j) of
            max (adv {r ∈ S : r i < r j}, adv {r ∈ S : r j < r i})
```

for a finite set `S` of rankings (`Equiv.Perm (Fin n)`).  For a finite poset
`P` on ground set `X`, let `L(P)` be its set of linear extensions, viewed as
rankings of `X`.  Define

```
F(P) := adv L(P),
```

the worst-case minimum number of further pairwise comparisons needed to identify
the unknown linear extension of `P` (the algorithm knows `P`, the adversary
chooses the linear extension).  For the antichain on `n` elements, `F(antichain_n)
= S(n)`.  This is the exact query complexity of *sorting under partial
information* (SUPI), not the `O(log e(P))` approximation studied in the SUPI
literature.

**Definition (ordinal sum).** For posets `A`, `B` on disjoint ground sets, the
ordinal sum `A ⊕ B` is the poset on `A ∪ B` with `x < y` iff `x <_A y`, or
`x <_B y`, or `x ∈ A` and `y ∈ B`.  Every linear extension of `A ⊕ B` is a
linear extension of `A` followed by a linear extension of `B`, so `L(A ⊕ B)` is
in bijection with `L(A) × L(B)`.

**Definition (incomparability graph).** `Inc(P)` has vertex set `P` and an edge
`{x,y}` iff `x` and `y` are incomparable.  `Comp(P)` is its complement.

## 2. Additivity under ordinal sum (paper proof, standard)

**Theorem 1.** For finite posets `A`, `B` on disjoint ground sets,
`F(A ⊕ B) = F(A) + F(B)`.

*Upper bound.* Run an optimal tree for `L(A)` (height `F(A)`) and then one for
`L(B)` (height `F(B)`).  Cross-block order is already fixed, so this distinguishes
every element of `L(A) × L(B)`; the height is `F(A) + F(B)`.  Hence
`F(A ⊕ B) ≤ F(A) + F(B)`.

*Lower bound (adversary).* The adversary maintains the current knowledge
`W ⊆ L(A ⊕ B)`, initially `W = L(A) × L(B)`.  Because cross-block order is
fixed, `W` is always a product `W_A × W_B` with `W_A ⊆ L(A)`, `W_B ⊆ L(B)`.
Define the potential `Φ = F(W_A) + F(W_B)`, initially `Φ = F(A) + F(B)`.

- A cross-block comparison gives no information: `W` and `Φ` are unchanged.
- A within-block comparison `(u,v)` in `A` splits `W_A` into
  `W_A^<`, `W_A^>`.  The compare-`(u,v)`-first tree shows
  `F(W_A) ≤ 1 + max(F(W_A^<), F(W_A^>))`, so
  `max(F(W_A^<), F(W_A^>)) ≥ F(W_A) - 1`.  The adversary answers the outcome
  with the larger value, so `Φ` drops by at most `1`.  (If one side is empty the
  comparison is already determined and `Φ` is unchanged.)  The same holds in
  `B`.

After `t` comparisons, `Φ ≥ F(A) + F(B) - t`.  The algorithm can terminate only
when `|W| = 1`, i.e. `|W_A| = |W_B| = 1`, i.e. `F(W_A) = F(W_B) = 0`, i.e.
`Φ = 0`.  Therefore at least `F(A) + F(B)` comparisons are necessary.

*Degenerate cases.* If `A` or `B` is empty, `P` equals the other summand and the
identity is trivial (`F(∅) = 0`).  If a summand has at most one linear extension
(e.g. a chain, or a singleton) then its `F` value is `0`, and the identity again
holds.  During the game `W ≠ ∅` and `W = W_A × W_B`, so both factors are
non-empty and `F(W_A)`, `F(W_B)` are defined.

**Relation to the literature.** This is an instance of the *deterministic direct
sum theorem* for decision-tree complexity: for independent relations on disjoint
variable sets, the exact decision-tree complexity of the joint relation is the
sum of the individual complexities (R. Jain, H. Klauck, M. Sántha, *Optimal
Direct Sum Results for Deterministic and Randomized Decision Tree Complexity*,
arXiv:1004.0105, 2010, Theorem 1).  Here the two "variables" are the `A`-order
and the `B`-order, which are independent because cross-block order is fixed.
The proof above is the textbook adversary potential argument specialized to
ordinal sums.

## 3. Maximal series decomposition and poly-time cut detection

**Theorem 2 (standard).** Every finite poset `P` has a *unique* decomposition
`P = P_1 ⊕ ⋯ ⊕ P_k` into nonempty ordinally indecomposable posets, and the
ground sets of the `P_i` are exactly the connected components of `Inc(P)`,
totally ordered by the poset order.  See Pouzet–Zaguia, *Metric properties of
incomparability graphs*, Lemma 2.1 (they call this folklore of ordered sets);
Erné–Stege, *Combinatorial Applications of Ordinal Sum Decompositions*, Ars
Combinatoria 40 (1995) 65–88; and the electronic journal of combinatorics note
*On the number of distributive lattices* (2002), Lemma 1, which states the same
correspondence.

**Corollary.** `F(P) = F(P_1) + ⋯ + F(P_k)`.

**Poly-time detection (deduction).** Given the transitive closure of the known
relations as `n` successor bitmasks, the incomparability graph is its complement,
so `Inc(P)` and its connected components are computable in `O(n^2)` time.  Two
elements in different components are comparable; the components are totally
ordered, and the bottom-to-top order can be recovered by a comparison sort over
the at most `n` components, again `O(n^2)`.  Thus the decomposition is
detectable from the transitive closure in polynomial time.  The implementation
in `scripts/series_decomposition_probe.py` (`ordered_blocks`) does exactly this
and raises `ValueError` on a state that is not a genuine ordinal sum.

## 4. A counterexample to the naive subset generalisation

The additivity identity requires the *full product* `L(A) × L(B)`.  It fails for
arbitrary subsets `S ⊆ L(A ⊕ B)`, because cross-block correlations can make a
single comparison resolve both blocks.

**Example.** Let `A = B` be a two-element antichain, so `P = A ⊕ B` and
`F(P) = 1 + 1 = 2`.  Take the correlated subset
`S = {0123, 1032}` (two linear extensions coupled across blocks).  A single
comparison of the two `A`-elements resolves `S`, so `F(S) = 1`, while the
projections satisfy `F(S_A) + F(S_B) = 1 + 1 = 2`.  The probe reports
`F(L(P)) = 2`, `F(S) = 1`, `F(S_A) + F(S_B) = 2`.  This is why the DP must
test `S = L(P)` (all linear extensions of the forced poset), not merely a block
product superset.

## 5. DP experiments at n ≤ 5

The state is the transitive closure of the known relations; for the antichain
start the set of consistent rankings is always `L(P)` for the current poset `P`,
so the poset DP computes `F(P)` exactly.  Applying the rule means: when a state
is decomposable, return the sum of the component values without exploring its
children.  `scripts/series_decomposition_probe.py` compares this against the
plain DP.  All runs are deterministic and bounded to `n ≤ 5`.

| n | S(n) | states plain → decomposed | expansions plain → decomposed | decomposition hits |
|---|------|---------------------------|-------------------------------|--------------------|
| 2 | 1    | 3 → 4                     | 1 → 1                         | 2                  |
| 3 | 3    | 19 → 23                   | 13 → 8                        | 14                 |
| 4 | 5    | 219 → 230                 | 195 → 105                     | 124                |
| 5 | 7    | 4231 → 4381               | 4111 → 2356                   | 2024               |

**Exactness (empirical).** `verify_additivity` checks `F(P) = Σ F(P_i)` for
*every* poset on `n` labelled elements: `n = 2,3,4` give `2/2`, `12/12`,
`122/122` non-series-prime states, with zero failures; `verify_decomposition`
confirms the components always form a genuine ordinal sum (`219/219` at `n=4`).
The decomposed DP returns the same `S(n)` as the plain DP for `n ≤ 5`.

**Practical impact (negative observation).** The rule does *not* reduce the
state count: it *increases* it, because the component states (induced subposets
on proper subsets) are additional memo entries.  It reduces the number of
child expansions by roughly 40% at `n = 5`, but the extra work of computing
components and induced states offsets this at these tiny sizes.  With
isomorphism canonicalisation the decomposed run is faster than the plain run
(e.g. `0.065 s` vs `0.103 s` at `n = 5`), but canonicalisation dominates and the
decomposition is not the main factor.

**Asymptotic warning.** Counting posets by series-primality (incomparability
graph connected) gives:

| n | all posets | series-prime | fraction |
|---|-----------|--------------|----------|
| 1 | 1         | 1            | 100%     |
| 2 | 3         | 1            | 33%      |
| 3 | 19        | 7            | 37%      |
| 4 | 219       | 97           | 44%      |
| 5 | 4231      | 2251         | 53%      |

The fraction of *decomposable* states is decreasing (67%, 63%, 56%, 47% for
`n = 2..5`).  Since the DP explores all posets reachable from the antichain,
the pruning benefit of the rule therefore shrinks with `n` over the measured
range; it is a small constant-factor device at best, not an asymptotic
compression.  (The trend is consistent with the fact that a random poset is
almost surely incomparability-connected, but this note does not prove the
limit.)

## 6. More general series decomposition

The ordinal-sum decomposition of Theorem 2 is already the *unique maximal*
series decomposition; there is no finer additive series decomposition.  The
parallel (disjoint-union) decomposition into comparability-graph components is a
different, non-additive operation for `F`: for two singletons,
`F(a ⊔ b) = 1` but `F(a) + F(b) = 0`.  Thus no general series-parallel recurrence
for `F` follows from the ordinal rule alone.

## 7. Structural identity is not a poly-time exact algorithm

The identity `F(A ⊕ B) = F(A) + F(B)` is an exact *structural* fact.  It does
**not** yield a polynomial-time exact algorithm for arbitrary `S(n)`:

- The initial antichain on `n` is itself series-prime, so the rule does not
  decompose the root.
- The exact DP must still evaluate `F` on the series-prime posets reachable from
  the antichain, whose count is exponential in `n` (and, per §5, a growing
  fraction of all posets).
- No complexity-class consequence follows.  This note makes no claim about
  `SORT-BOUND-U`, `P`, `NP`, or any separation.

The honest reading is that the ordinal-sum rule is a useful *identity* and a
minor constant-factor pruning device, but not a route to compressing exact
minimax evaluation.

## 8. Novelty assessment

- **Standard:** ordinal sum and its unique decomposition into incomparability
  components (Pouzet–Zaguia Lemma 2.1; Erné–Stege, Ars Combinatoria 40 (1995)
  65–88; EJC 2002 Lemma 1); deterministic direct-sum additivity for decision
  trees (Jain–Klauck–Sántha 2010); the SUPI model and its `log e(P)` lower
  bound (Fredman 1976; Kahn–Saks 1984; Kahn–Kim 1992/1995; Cardinal et al.
  2009/2010; Bose et al. 2024; van der Hoog–Rutschmann 2024).
- **Deduction in this note:** the specialisation to `F(A ⊕ B) = F(A) + F(B)`
  and the `O(n^2)` cut detection.
- **Empirical in this note:** the `n ≤ 5` DP measurements and the shrinking
  decomposable fraction.
- **Not established:** any complexity-class statement, any polynomial-time exact
  algorithm, and any Lean kernel-checked theorem.

## 9. Reproducibility

```
python3 scripts/series_decomposition_probe.py          # bounded n ≤ 5 report
python3 -m unittest discover -s tests -v              # CI regression suite
```

`tests/test_series_decomposition.py` checks additivity and decomposition over
all posets for `n ≤ 4`, the subset counterexample, `S(n)` invariance under the
rule for `n ≤ 5`, and that the benchmark values agree.  No randomness, no
network, no `n ≥ 6` exhaustive search.
