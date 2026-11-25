# Polynomial-time constructive upper witnesses for partial-order sorting

**Status:** research note / executable reference experiment (2026-10-18). The
upper-bound proofs below are paper deductions, not additional Lean theorems.
They provide **valid sorting strategies**, not a faster algorithm for computing
the exact optimum `S(n)`, and no complexity-class separation is claimed.

## 1. Two safe upper bounds

Let `P` be a transitively closed strict poset of `n` labelled elements and
`F(P)` its minimum worst-case additional comparison count.

**Unconditional Ford–Johnson bound.** The classical merge-insertion strategy
sorts any `n` distinct elements with at most

```
M(n) = sum_{i=1}^n ceil(log2(3i/4))  comparisons,
```

with the `i=1` term interpreted as zero. Ignore all already-known relations
and run this sorting strategy; hence `F(P) ≤ S(n) ≤ M(n)`. The script includes
an executable Ford–Johnson reference and checks all permutations for `n≤6`.
The source of the algorithm and the bound is Ford–Johnson/Knuth, not this
research project.

**Binary insertion with partial information (BIPI).** Pick any fixed linear
extension `x_0,…,x_{n-1}` of `P` (lexicographic topological order is an
effective choice). Define

```
m_k = |{ j<k : x_j and x_k incomparable in P }|,
U_BIPI(P) = sum_{k=1}^{n-1} min(m_k, ceil(log2(k+1))).
```

**Proposition.** `F(P) ≤ U_BIPI(P)`.

*Proof.* Insert `x_k` by standard binary search into the dynamically sorted
chain of the previous `k` elements. At each examined position, if the
comparison outcome is already implied by `P`, traverse the appropriate
half **without issuing a paid comparison**. Otherwise compare the elements.
The usual binary search visits at most `ceil(log2(k+1))` distinct predecessors.
Only predecessors incomparable with `x_k` in the original `P` can require a
paid comparison, and there are `m_k` of them. Each insertion therefore uses
at most the minimum of those two bounds, uniformly over all linear extensions
consistent with `P`. Summing gives the stated worst-case upper bound. ∎

This bound is computable in polynomial **numeric-`n`** time from the relation
matrix; it never needs to count the linear extensions. Its value may be loose,
and it need not improve Ford–Johnson. A safe combined acceptance certificate is

```
U(P) = min(M(n), U_BIPI(P)).
If d ≥ U(P), the exact budget question CanSort(P,d) is TRUE.
```

The certificate is a *specific deterministic strategy with proved height*,
not a heuristic estimate of the optimal minimax recursion.

## 2. Incorrect shortcut and its repair

An earlier prototype estimated the number of necessary comparisons using
the relative positions of keys in the **initial** topological order. That
does not upper-bound a binary-insertion strategy: after early insertions,
the search chain is rearranged, and the examined midpoints can change.

The corrected `U_BIPI` counts **all earlier incomparable keys**, independently
of their positions in the dynamic chain. This is conservative but justified
by the preceding proof. The regression state
`P=(0,0,0,0,5)` (successor bitmasks, `n=5`) has `e(P)=40` and exact
`F(P)=6`; the corrected experiment reports `U_BIPI(P)=8`,
`M(5)=7`, and an actual binary-insertion strategy height of 7.
Thus `U(P)=7` is safe but not optimal on this example. The previously
estimated smaller bound and inconsistent claimed policy height are rejected.

## 3. Experiments and limitations

The companion `scripts/upper_witness.py` implements Ford–Johnson, BIPI,
a leaf-count-greedy experimental policy, and a decision solver with optional
upper-bound acceptance. `tests/test_upper_witness.py` contains bounded tests
including all small labelled posets through `n=5`, known `M(n)` values,
strategy correctness, and comparison with the exact minimax evaluator.
The initial run completed 13 tests successfully.

The greedy rule chooses an incomparable pair whose two outcomes split the
linear-extension count most evenly; its *exact policy height* can be measured
by recursive search on tiny posets. The greedy rule is **not** claimed
polynomial-time in general because evaluating `e(P)` exactly is #P-hard.

These constructive bounds can accept some budget-DFS states without
exploring both outcomes, but the probe has not established a uniform
improvement to the existing `2^{O(n log² n)}` worst-case time. In particular,
constant-factor `O(log e(P))` comparison guarantees for sorting under
partial information do **not** establish the exact minimum `F(P)`.

## 4. Reproduction and provenance

```sh
python3 -m unittest tests.test_upper_witness -q
python3 scripts/upper_witness.py --help
```

Primary sources: L. R. Ford and S. M. Johnson, *A tournament problem*,
American Mathematical Monthly 66 (1959), 387–389; D. E. Knuth,
*The Art of Computer Programming*, Vol. 3 §5.3.1;
Haeupler, Hladík, Iacono, Rozhoň, Tarjan, Tětek,
*Fast and Simple Sorting Using Partial Information*, Algorithmica 88(3)
(2026), DOI [10.1007/s00453-026-01387-3](https://doi.org/10.1007/s00453-026-01387-3).

The Ford–Johnson and recent partial-information algorithms are **literature**.
The simple BIPI bound and its regression tests are this project's
**deductions and experiments**; novelty relative to all existing literature
is not claimed.
