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

`[deduction]` **Theorem 1.1 (verifier).** Given a strategy DAG `D = (V, E)` for
`n` keys and a budget `k`, there is a deterministic algorithm running in time
`O((|V| + |E|) · n³ + |E| · log k)` that decides whether `D` encodes a correct
sorting strategy of height `≤ k`.

*Proof.* The verifier performs five checks:

1. **Root check**: Verify the root node is the empty poset (antichain). `O(n²)`.
2. **Well-formedness**: Each node is a valid poset (check transitivity and
   antisymmetry of the successor matrix). Naive transitivity checking costs
   `O(n³)` per node (for each pair `(i,j)`, check that `j ∈ succ[i]` implies
   `succ[j] ⊆ succ[i]`). Total: `O(|V| · n³)`.
3. **Terminal check**: Each leaf (node with no outgoing edges) is a total
   order. `O(n²)` per leaf.
4. **Edge validity**: For each edge `((x,y), P₁, P₀)` from node `P`, check:
   (a) `{x,y}` is incomparable in `P` (both `succ[x]` and `succ[y]` lack the
   other's bit); (b) `P₁ = P+x<y` and `P₀ = P+y<x` (transitive closure);
   (c) `P₁` and `P₀` are referenced nodes in `V`. Naive transitive closure
   costs `O(n³)` per edge. Total: `O(|E| · n³)`.
5. **Height bound**: Dynamic programming over the DAG in topological order
   (computed in `O(|V| + |E|)`):
   - `height(leaf) = 0` for each terminal node.
   - For a non-terminal node `P` with moves `m₁, …, mᵣ` (each `mᵢ` is an edge
     `((x,y), P₁, P₀)`), compute:
     `height(P) = min over moves mᵢ of (1 + max(height(P₁), height(P₀)))`.
   - Check `height(root) ≤ k`.
   The max-plus arithmetic on values `≤ k` costs `O(log k)` per edge.
   Total: `O(|E| · log k)`.

The `n³` factor in checks 2 and 4 is conservative (naive matrix operations). ∎

`[deduction]` **Remark 1.2 (what the verifier does and does not prove).**
The verifier proves: *if* a DAG of size `|D|` is given, *then* we can check
in `poly(|D|, n, log k)` time whether it is a correct height-`k` sorting
strategy. It does **not** prove that such a DAG exists, and it does **not**
prove that `|D|` is polynomial in the input length. The verifier is a
**certificate checker**, not a **certificate existence proof**.

`[deduction]` **Remark 1.3 (no NP membership without a size bound).** To
conclude `SORT-BOUND-U ∈ NP` from the verifier, one would need:
(a) a proof that a polynomial-size DAG always exists for yes-instances
(certificate existence), and
(b) the verifier is polynomial-time (already established in Theorem 1.1).
No condition on no-instances is needed for NP membership: the verifier's
soundness ensures that no-instances are correctly rejected (if no poly DAG
exists for a no-instance, the verifier rejects it). `coNP` membership would
require *separate* polynomial certificates of unsortability, not merely the
nonexistence of a DAG. Neither NP nor coNP membership is known. The verifier
alone establishes only that `SORT-BOUND-U ∈ NEXP` (unary) / `N2EXP` (binary),
because the DAG itself may be exponential in the input length. This does not
improve on the `PSPACE`/`EXPSPACE` game bounds of
`research-certificates-barriers.md`.

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

The ratio `log2(DAG(all))/n` is **increasing** over this range, which is
*consistent with* super-polynomial growth, but `n ≤ 6` is too small to
distinguish `2^{Θ(n log n)}`, `2^{Θ(n²)}`, or even `n^{Θ(log n)}` from
polynomial growth. No asymptotic claim is made.

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

`[deduction]` **Theorem 2.6 (distinct nodes have distinct labelled posets).**
In a reduced deterministic sorting comparison tree, distinct reachable nodes
have distinct labelled poset states.

*Proof.* Let `u`, `v` be distinct reachable nodes with path posets `P_u`,
`P_v` (transitive closures of comparisons on the root-to-node paths). Let
`L(P_u)`, `L(P_v)` be their linear extensions (the permutations reaching
them).

In a tree, the permutation sets of distinct nodes are either disjoint or
nested (one node is an ancestor of the other):

- **Disjoint case**: `u` and `v` are in different subtrees. Then
  `L(P_u) ∩ L(P_v) = ∅`, so `L(P_u) ≠ L(P_v)`, hence `P_u ≠ P_v`.
- **Nested case**: `u` is an ancestor of `v`. Since the tree is **reduced**,
  every comparison on the path from `u` to `v` is informative: it strictly
  shrinks the permutation set. Thus `L(P_v) ⊂ L(P_u)` (strict subset), so
  `L(P_u) ≠ L(P_v)`, hence `P_u ≠ P_v`.

The poset determines its linear extensions, so equal posets would imply
equal permutation sets, a contradiction. ∎

`[deduction]` **Corollary 2.7 (hash-consing saves zero in a single policy).**
In a single optimal policy (a tree), no two nodes have the same labelled poset
(Theorem 2.6). Therefore, hash-consing — merging nodes with identical posets —
saves **zero** nodes. This explains the observed `DAG(1) = unshared(1) =
2n! − 1` for all `n ≤ 6`.

`[deduction]` **Corollary 2.8 (quotient can compress).** The `S_n` quotient
identifies posets that are isomorphic under relabelling. Different nodes can
have isomorphic (but not identical) posets, so the quotient **can** compress.
This is distinct from hash-consing, which only merges identical posets.

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

`[deduction]` **Remark 3.3 (quotient certificate is poly-checkable).** A
symmetry-quotient policy DAG **can** be verified in polynomial time in its
own encoding **without** solving graph isomorphism. The certificate includes
an explicit permutation `σ` (`n⌈log₂ n⌉` bits) for each outcome edge, witnessing
that the computed successor poset maps onto the stored canonical child node.

The verifier performs:
1. **Root check**: labelled root is the empty antichain.
2. **Node check**: each non-terminal quotient node has one chosen comparison.
3. **Edge check**: for each outcome edge, verify `σ` is a valid permutation,
   compute the successor poset, apply `σ`, and check it equals the stored
   canonical child. Naive transitive closure costs `O(n³)` per edge.
4. **Both outcomes**: each non-terminal node has both outgoing edges.
5. **Acyclicity**: topological sort.
6. **Terminal totals**: each leaf is a total order.
7. **Height bound**: DP over the DAG: `height(leaf) = 0`,
   `height(P) = 1 + max(height(P₁), height(P₀))` for the chosen comparison.
   Check `height(root) ≤ k`.

Total: `O((|V| + |E|) · n³ + |E| · log k)` = polynomial in the certificate
size. Graph isomorphism is **not** an obstacle for this witness model: the
permutations are given in the certificate, not computed. The only open
question is whether the **number** of quotient nodes is polynomially bounded
(see §6).

### 3.1 Quotient certificate needs explicit relabelling maps

`[deduction]` **Theorem 3.4 (one explicit, polynomially checkable quotient certificate).**
There is a certificate format for a relabelling-quotient sorting policy with
one representative poset per state class, one selected comparison per
nonterminal representative, and a *supplied* relabelling permutation `σ`
for each of the two outcomes. The size of this encoding is at most

```
O(|V|·n² + |E|·(n·log₂(n+1) + log₂(|V|+1)) + log₂(k+1)) bits.
```

The `|V|·n²` term stores representative posets, the edge term includes
permutations, comparison labels and target-node indices, and the last term
stores the budget. The permutation-and-comparison **edge overhead** alone is
`|E|·(n⌈log₂(max(2,n))⌉ + 2⌈log₂(max(2,n))⌉)` bits; it is *not*
the size of the whole certificate.

*Proof.* A representative poset is stored on the abstract labels `[n]`.
After a comparison, explicitly compute each labelled successor and use
the edge's supplied permutation to verify that it is isomorphic to the
stored target representative. At execution time, composing these maps
translates the chosen comparison back to the concrete input labels.
The verifier checks all permutations directly, so graph isomorphism
needs no search. The encoding costs follow by counting matrices, edge
descriptions, indices and the budget. Supplying permutations is one
**sufficient** witness format, not a claim that every imaginable compressed
encoding must use them. ∎

`[experiment]` **Table 3: Quotient edge-relabel overhead estimates for `n ≤ 6` (not full certificate size).**

```
 n   q(all) nodes   qedges   perm bits/edge   edge overhead bits (est.)
  1             1        0               0               0
  2             2        1               2               4
  3             5        7               6              70
  4            12       23               8             276
  5            19       35              15             735
  6           134      415              18            9960
```

`[experiment]` **Observation 3.5 (edge-relabel overhead).** The estimated
edge overhead grows from 4 bits (`n=2`) to 9960 bits (`n=6`). For unary
encoding with informative `k = S(n)`, the input length is `L = n + k + 1 =
Θ(n log n)`. At `n=6`, `L = 17`; testing polynomial-size certificates would require a proven asymptotic size bound, not just this finite overhead. A polynomial certificate would need
`poly(17)` bits; 9960 bits is roughly `17³`, which is not obviously polynomial.
The growth rate is *consistent with* super-polynomial growth, but `n ≤ 6` is
too small to distinguish `n^{Θ(log n)}` from `2^{Θ(n)}` from polynomial growth.
No asymptotic claim is made.

`[deduction]` **Remark 3.6 (no NP membership from quotient).** Even if the
quotient certificate were polynomially bounded, it would establish only that
`SORT-BOUND-U ∈ NP` (unary encoding), **not** `SORT-BOUND-B ∈ NP` (binary
encoding). The binary encoding compresses `n` exponentially, so a certificate
polynomial in `n` is exponential in `L_B = Θ(log n)`. Mahaney's theorem
(Theorem 4.1) still blocks the NP-hardness route for the unary language.

---

## 4. Concrete no-go for naive polynomial certificates

`[deduction]` **Theorem 4.1 (general sparse-set barrier via Mahaney).** This
is a general fact about sparse languages, independent of any certificate
format. If `SORT-BOUND-U` were NP-hard under polynomial-time many-one
reductions, then `P = NP` (Mahaney's theorem, since `SORT-BOUND-U` is sparse
by Lemma 3.1 of `research-encoding-consequences.md`).

This barrier applies to **any** route to NP-hardness for `SORT-BOUND-U`,
whether via DAG certificates, explicit trees, or any other witness format.
It is **not** specific to the DAG approach. It does **not** prove that no
polynomial DAG exists, and it does **not** prove that `SORT-BOUND-U` is not
in NP.

`[experiment]` **Observation 4.2 (DAG(all) growth).** The experiment shows
`DAG(all)` growing from 19 to 65551 for `n = 3,…,6`. The ratio
`log2(DAG(all))/n` is increasing, which is *consistent with* super-polynomial
growth, but `n ≤ 6` is too small to establish any asymptotic claim. No
polynomial-size DAG certificate is known.

`[deduction]` **Remark 4.3 (DAG approach does not claim NP membership).**
The polynomial-in-DAG-size verifier (Theorem 1.1) does **not** establish
`SORT-BOUND-U ∈ NP` or `SORT-BOUND-B ∈ NP`, because:
- the DAG size is not bounded by a polynomial in the input length;
- the verifier checks a given DAG, but does not prove DAG existence;
- even if a poly DAG existed, membership in NP would not imply hardness
  (membership and hardness are separate questions).

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
   is a tree (Theorem 2.6, Corollary 2.7).
2. `DAG(all)` is larger than `DAG(1)` for `n ≥ 3` (more moves kept), but
   much smaller than `unshared(all)` (hash-consing helps).
3. The quotient by `S_n` reduces `DAG(all)` by a factor of ~500 at `n=6`,
   but the quotient itself grows (19 → 134 from `n=5` to `n=6`).
4. `log2(DAG(all))/n` is increasing over `n = 3,…,6`, which is *consistent
   with* super-polynomial growth, but no asymptotic claim is made.

---

## 6. Known vs conjectured vs open

| Statement | Status |
|---|---|
| Verifier runs in `O((\|V\|+\|E\|) · n³ + \|E\| · log k)` | `[deduction]` Thm 1.1 |
| Single-policy DAG = tree (`2n!−1` nodes) | `[deduction]` Thm 2.1, `[experiment]` Obs 2.5 |
| Distinct nodes have distinct posets (single policy) | `[deduction]` Thm 2.6, `[experiment]` Cor 2.7 |
| Hash-consing saves zero in single policy | `[deduction]` Cor 2.7 |
| Quotient by S_n can compress | `[experiment]` Obs 3.1 |
| Quotient certificate is poly-checkable | `[deduction]` Remark 3.3 |
| Quotient node count is polynomially bounded | `[open]`; evidence inconclusive |
| Poly-size DAG certificate exists | `[open]`; none known |
| `SORT-BOUND-U ∈ NP` via DAG | `[open]`; Thm 1.1 does not establish this |
| `SORT-BOUND-U` NP-hard ⇒ `P = NP` (general) | `[literature]` Mahaney |
| `SORT-BOUND-U` sparse | `[deduction]` Lem 3.1, `research-encoding-consequences.md` |

---

## 7. Next unresolved obstacle

The central question is whether the **all-optimal DAG size** is polynomially
bounded in `n`. The experiment is consistent with super-polynomial growth,
but `n ≤ 6` is too small to distinguish `2^{Θ(n log n)}`, `2^{Θ(n²)}`,
`n^{Θ(log n)}`, or even polynomial growth. No asymptotic claim is made.

Computing `DAG(all)` and `quotient(all)` for `n = 7` (A001035(7) = 6129859
posets) would provide one more data point, but the labelled DP over 6 million
posets is not automatically cheap on the target hardware (8 GB Phoebe) and
is not prescribed here. A memory-bounded or quotient-based computation might
be more appropriate.

The key open questions are:
1. Is `DAG(all)` polynomially bounded? (Unknown; evidence is inconclusive.)
2. Is `quotient(all)` polynomially bounded? (Unknown; evidence is inconclusive.)
3. Does there exist *any* polynomial-size certificate for `SORT-BOUND-U`?
   (Unknown; no such certificate is known.)

The DAG approach does **not** claim NP membership without a size bound
(Remark 4.3).

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
