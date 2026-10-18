# Strategy DAGs and certificate complexity for exact S(n)

**Status:** research note (paper-and-literature analysis plus reproducible
experiments for `n ≤ 6`). It is **not** Lean-checked. Every item is labelled
`[literature]`, `[deduction]`, `[experiment]`, `[conjecture]` or `[open]`.
No unconditional separation is claimed, and no NP-hardness is claimed.

This note responds to the exploration-first mandate (2026-10-17) and
supplements `research-certificates-barriers.md` and
`research-encoding-consequences.md` with a concrete study of the
**strategy DAG** representation: a hash-consed directed acyclic graph whose
nodes are poset states and whose edges encode comparison choices and both
child outcomes. We construct tiny optimal policies from the reference
minimax, count DAG nodes, quotient under label symmetries, and seek a
concrete no-go for naive polynomial certificates.

---

## 0. Model and definitions (fixed once, used throughout)

`[literature]`/definition. From `docs/problem.md`:

- `S(n)` = minimum height (worst-case number of pairwise comparisons) of a
  **deterministic adaptive comparison decision tree** that correctly sorts
  every permutation of `n` distinct labelled keys.
- `SORT-BOUND-U = { 1^n # 1^k : S(n) ≤ k }` — both parameters **unary**.
- `SORT-BOUND-B = { bin(n) # bin(k) : S(n) ≤ k }` — both parameters **binary**.

`[deduction]`. A **state** is a transitive, antisymmetric relation `P` on
`[n] = {0,…,n−1}`; equivalently, for every unordered pair `{x,y}` exactly one
of `x<y`, `y<x`, "unknown" holds and the relation is transitively closed.
Represent `P` by the `n×n` boolean successor matrix `M` with `M[i]` having
bit `j` set iff `i<j`. The minimax value is:

```
F(P) = 0                                   if P is total,
F(P) = 1 + min_{(x,y) incomparable}
         max( F(P+x<y), F(P+y<x) )         otherwise.
```

`S(n) = F(∅)`. An **optimal policy** is a strategy achieving this minimum.

### 0.1 The strategy DAG representation

`[deduction]`. A **strategy DAG** is a hash-consed directed acyclic graph:

- **Nodes** are poset states (transitively closed partial orders on `[n]`).
- **Edges** from a non-total node `P` are triples `((x,y), P₁, P₀)` where
  `{x,y}` is incomparable in `P`, `P₁ = P+x<y` (transitive closure), and
  `P₀ = P+y<x`. The edge encodes: "compare `x` and `y`; if `x<y` go to `P₁`,
  else go to `P₀`."
- **Hash-consing** means identical posets share the same node: if two
  different paths reach the same state, the DAG has one node for it, not two.
- **Leaves** are total orders (no incomparable pairs); they need no outgoing
  edges.

A strategy DAG is **optimal** if from every non-total node `P`, every edge
`((x,y), P₁, P₀)` satisfies `F(P) = 1 + max(F(P₁), F(P₀))`.

### 0.2 One policy vs union of all strategies

`[deduction]`. Two variants:

- **Single-policy DAG**: from each node, keep exactly one optimal move. This
  encodes one specific optimal strategy.
- **All-optimal DAG**: from each node, keep *all* optimal moves. This encodes
  the union of all optimal strategies.

The single-policy DAG is a tree (no node has two parents, because each node
corresponds to a unique path of comparison outcomes). The all-optimal DAG
can have sharing: different paths can reach the same poset state.

---

## 1. Polynomial-in-DAG-size verifier

`[deduction]` **Theorem 1.1 (verifier).** Given a strategy DAG `D` for `n`
keys and a budget `k`, there is a deterministic algorithm running in time
`O(|D| · n² · log k)` that decides whether `D` encodes a correct sorting
strategy of height `≤ k`.

*Proof.* The verifier performs four checks:

1. **Well-formedness**: Each node is a valid poset (check transitivity and
   antisymmetry of the successor matrix). `O(n²)` per node.
2. **Edge validity**: For each edge `((x,y), P₁, P₀)`, check that `{x,y}` is
   incomparable in `P`, and that `P₁ = P+x<y`, `P₀ = P+y<x` (transitive
   closure). `O(n²)` per edge.
3. **Acyclicity**: Topological sort; if a cycle exists, reject. `O(|D| + |E|)`.
4. **Height bound**: Dynamic programming over the DAG in topological order:
   `height(leaf) = 0`, `height(P) = 1 + max(height(P₁), height(P₀))` for each
   edge. Check `height(root) ≤ k`. `O(|E| · log k)` for the max-plus
   arithmetic.

Total: `O(|D| · n² · log k)`. ∎

`[deduction]` **Remark 1.2 (what the verifier does and does not prove).**
The verifier proves: *if* a DAG of size `|D|` is given, *then* we can check
in `poly(|D|, n, log k)` time whether it is a correct height-`k` sorting
strategy. It does **not** prove that such a DAG exists, and it does **not**
prove that `|D|` is polynomial in the input length. The verifier is a
**certificate checker**, not a **certificate existence proof**.

`[deduction]` **Remark 1.3 (no NP membership without a size bound).** To
conclude `SORT-BOUND-U ∈ NP` from the verifier, one would need:
(a) a proof that a polynomial-size DAG always exists for yes-instances, and
(b) a proof that no polynomial-size DAG exists for no-instances (for
`coNP`). Neither is known. The verifier alone establishes only that
`SORT-BOUND-U ∈ NEXP` (unary) / `N2EXP` (binary), because the DAG itself
may be exponential in the input length. This does not improve on the
`PSPACE`/`EXPSPACE` game bounds of `research-certificates-barriers.md`.

---

## 2. Distinguishing tree leaves from DAG states

`[deduction]` **Theorem 2.1 (unshared tree has `n!` leaves).** Every correct
comparison tree sorting `n` keys has at least `n!` reachable leaves (the `n!`
permutations reach pairwise distinct leaves). A reduced optimal tree has
exactly `n!` leaves and `2n! − 1` nodes.

*Proof.* See Lemma 5.1 of `research-encoding-consequences.md`. ∎

`[deduction]` **Theorem 2.2 (hash-consing can reduce nodes).** In the
all-optimal DAG, different paths can reach the same poset state. The number
of DAG nodes is at most the number of reachable poset states (A001035), and
can be much smaller than the tree node count (`2n! − 1`).

`[experiment]` **Table 1: Node counts for `n ≤ 6`.**

```
 n   S(n)   unshared(1)   unshared(all)   DAG(1)   DAG(all)   n!
 1     0             1              1         1          1     1
 2     1             3              3         3          3     2
 3     3            11             55        11         19     6
 4     5            47           1957        47        181    24
 5     7           239          26541       239       1551   120
 6    10          1439     (too large)      1439      65551   720
```

`[experiment]` **Observation 2.3 (single-policy DAG = tree).** For all
`n ≤ 6`, `DAG(1) = unshared(1)`. A single optimal policy has **no hash-consing
sharing**: it is a tree with `2n! − 1` nodes. This is because each node in a
single-policy DAG corresponds to a unique path of comparison outcomes, so no
two nodes share the same poset state.

`[experiment]` **Observation 2.4 (all-optimal DAG shrinks but stays large).**
`DAG(all)` is much smaller than `unshared(all)` (hash-consing helps), but
still grows rapidly:

```
 n   DAG(all)   DAG(all)/n!   log2(DAG(all))   log2/n
 3        19         3.17              4.25    1.42
 4       181         7.54              7.50    1.87
 5      1551        12.93             10.60    2.12
 6     65551        91.04             16.00    2.67
```

The ratio `log2(DAG(all))/n` is **increasing**, suggesting super-polynomial
growth. This is consistent with the hypothesis that the all-optimal DAG size
is `2^{Θ(n log n)}` (like `n!`) or `2^{Θ(n²)}` (like the full poset count).

`[experiment]` **Observation 2.5 (DAG(1) = 2n! − 1 exactly).** For all
`n ≤ 6`, `DAG(1) = 2n! − 1`:

```
 n   DAG(1)   2n! − 1
 1        1        1
 2        3        3
 3       11       11
 4       47       47
 5      239      239
 6     1439     1439
```

This confirms Theorem 2.1: a single optimal policy is a reduced tree with
exactly `n!` leaves.

---

## 3. Symmetry quotient under label symmetries

`[deduction]`. The symmetric group `S_n` acts on posets by relabelling: for
`σ ∈ S_n`, the image of poset `P` has `σ(i) < σ(j)` iff `i < j` in `P`.
This action preserves the minimax value `F`. We can quotient the DAG by
`S_n`: identify nodes whose posets are isomorphic.

`[experiment]` **Table 2: Quotient counts for `n ≤ 6`.**

```
 n   DAG(1)   quotient(1)   DAG(all)   quotient(all)
 1        1             1          1             1
 2        3             2          3             2
 3       11             4         19             5
 4       47             7        181            12
 5      239            11       1551            19
 6     1439            27      65551           134
```

`[experiment]` **Observation 3.1 (quotient reduces but does not compress to
polynomial).** The quotient `quotient(all)` grows as `1, 2, 5, 12, 19, 134`
for `n = 1,…,6`. The jump from `n=5` to `n=6` (19 → 134, a 7× increase)
suggests the quotient is not polynomially bounded. However, the quotient is
much smaller than the DAG: at `n=6`, `134` vs `65551` (a 489× reduction).

`[experiment]` **Observation 3.2 (quotient(1) is very small).** The quotient
of the single-policy DAG grows as `1, 2, 4, 7, 11, 27`. This is the number of
isomorphism classes of posets on a single optimal play. It is smaller than
A000112 (unlabelled posets: `1, 2, 5, 16, 63, 318, 2045`), as expected
since optimal play visits only a subset of all posets.

`[deduction]` **Remark 3.3 (quotient is not a certificate).** Even if the
quotient were polynomially bounded, it would not immediately give a
polynomial certificate. The quotient identifies isomorphic posets, but the
verifier would need to check that the quotient structure is consistent with
some lift to labelled posets. This is a graph isomorphism problem, which is
not known to be polynomial-time solvable (though it is in `quasi-poly`).

---

## 4. Concrete no-go for naive polynomial certificates

`[deduction]` **Theorem 4.1 (conditional barrier via Mahaney).** If a
polynomial-size DAG certificate existed for `SORT-BOUND-U`, then
`SORT-BOUND-U ∈ NP`. But `SORT-BOUND-U` is sparse (Lemma 3.1 of
`research-encoding-consequences.md`). By Mahaney's theorem, a sparse set is
not NP-hard under polynomial-time many-one reductions unless `P = NP`.
Therefore:

> **If** a polynomial-size DAG certificate exists for `SORT-BOUND-U`, **and**
> `SORT-BOUND-U` is NP-hard, **then** `P = NP`.

This is a **conditional** barrier. It does **not** prove that no polynomial
DAG exists. It shows that the naive route to NP-hardness (exhibit a poly
DAG, then prove NP-hardness) would imply `P = NP`, so such a proof cannot
be routine.

`[deduction]` **Theorem 4.2 (no poly DAG known for all-optimal).** The
experiment shows `DAG(all)` grows super-polynomially for `n ≤ 6`. This is
**evidence** (not a proof) that no polynomial-size all-optimal DAG exists.
The growth rate `log2(DAG(all))/n ≈ 1.42, 1.87, 2.12, 2.67` for
`n = 3,4,5,6` suggests exponential or super-exponential growth.

`[deduction]` **Remark 4.3 (DAG approach does not claim NP membership).**
The polynomial-in-DAG-size verifier (Theorem 1.1) does **not** establish
`SORT-BOUND-U ∈ NP` or `SORT-BOUND-B ∈ NP`, because:
- the DAG size is not bounded by a polynomial in the input length;
- the verifier checks a given DAG, but does not prove DAG existence;
- even if a poly DAG existed, Mahaney's theorem blocks the NP-hardness
  route (Theorem 4.1).

---

## 5. Summary of experimental data

`[experiment]` **Complete data for `n ≤ 6`.**

```
 n   S(n)   unshared(1)   DAG(1)   DAG(all)   q(1)   q(all)   n!
 1     0             1        1          1      1        1     1
 2     1             3        3          3      2        2     2
 3     3            11       11         19      4        5     6
 4     5            47       47        181      7       12    24
 5     7           239      239       1551     11       19   120
 6    10          1439     1439      65551     27      134   720
```

Key observations:
1. `DAG(1) = unshared(1) = 2n! − 1` for all `n ≤ 6`: a single optimal policy
   is a tree.
2. `DAG(all)` is much smaller than `unshared(all)` but still grows
   super-polynomially.
3. The quotient by `S_n` reduces `DAG(all)` by a factor of ~500 at `n=6`,
   but the quotient itself grows (19 → 134 from `n=5` to `n=6`).
4. `log2(DAG(all))/n` is increasing, suggesting no polynomial bound.

---

## 6. Known vs conjectured vs open

| Statement | Status |
|---|---|
| Verifier runs in `O(\|D\| · n² · log k)` | `[deduction]` Thm 1.1 |
| Single-policy DAG = tree (`2n!−1` nodes) | `[deduction]` Thm 2.1, `[experiment]` Obs 2.5 |
| All-optimal DAG < unshared tree | `[deduction]` Thm 2.2, `[experiment]` Obs 2.4 |
| All-optimal DAG grows super-polynomially | `[experiment]` Obs 2.4 (evidence, not proof) |
| Quotient by S_n reduces DAG size | `[experiment]` Obs 3.1 |
| Quotient is polynomially bounded | `[open]`; evidence suggests no |
| Poly-size DAG certificate exists | `[open]`; evidence suggests no |
| `SORT-BOUND-U ∈ NP` via DAG | `[open]`; Thm 1.1 does not establish this |
| `SORT-BOUND-U` NP-hard ⇒ `P = NP` | `[literature]` Mahaney (conditional) |
| `SORT-BOUND-U` sparse | `[deduction]` Lem 3.1, `research-encoding-consequences.md` |

---

## 7. Next unresolved obstacle

The central question is whether the **all-optimal DAG size** is polynomially
bounded in `n`. The experiment suggests it is not, but `n ≤ 6` is too small
to distinguish `2^{Θ(n log n)}` from `2^{Θ(n²)}` from `n^{Θ(log n)}`. The
next informative experiment is:

1. Compute `DAG(all)` and `quotient(all)` for `n = 7` (A001035(7) = 6129859
   posets; feasible with the labelled DP but may take minutes).
2. Fit the growth rate: is `log2(DAG(all))` closer to `n log n` or `n²`?
3. If `DAG(all)` is `2^{Θ(n log n)}`, then even the all-optimal DAG is
   super-polynomial, and the DAG certificate route is closed (conditionally,
   via Mahaney).
4. If `DAG(all)` is `2^{Θ(n)}`, then a polynomial-size certificate might
   exist for a *subset* of optimal strategies (not all).

Either outcome is a useful, falsifiable result. The DAG approach does
**not** claim NP membership without a size bound (Remark 4.3).

---

## 8. Sources

- S. R. Mahaney, *Sparse complete sets for NP*, J. Comput. System Sci.
  **25**(2) (1982) 130–143. (Sparse-set barrier; Theorem 4.1.)
- M. Peczarski, *Towards optimal sorting of 16 elements*, Acta Univ.
  Sapientiae Inform. **4**(2) (2012) 215–224. (Exact sorting numbers.)
- OEIS A001035 (labelled posets), A000112 (unlabelled posets), A036604
  (sorting numbers).
- `docs/problem.md`, `docs/research-encoding-consequences.md`,
  `docs/research-certificates-barriers.md` (this repository).
- `scripts/strategy_dag_probe.py` (this repository; reproducible experiment).
