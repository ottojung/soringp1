# Quadratically many inequivalent comparison moves in asymmetric posets

**Status:** elementary structural theorem and bounded reference experiment
(2026-10-18). This is a rigorous *limitation of automorphism-orbit pruning*,
not a time-complexity lower bound for computing the optimal sorting number
`S(n)` and not a proof of complexity-class separation.

## 1. The staircase height-two family

For `m ≥ 1`, define `P_m` on `2m` elements
`b_0,...,b_{m-1}` and `t_0,...,t_{m-1}`, with the **only** strict order
relations

```
b_i < t_j    if and only if   0 ≤ j ≤ i < m.
```

All bottoms are mutually incomparable, all tops are mutually
incomparable, and the remaining cross pairs `b_i,t_j` with `j>i`
are incomparable. Because all relations go bottom-to-top, the
relation is transitive and defines a height-two poset.

**Theorem 1.** The automorphism group `Aut(P_m)` is trivial, yet
`P_m` has exactly `3·binom(m,2) = 3m(m−1)/2 = Θ(n²)`
incomparable pairs for `n=2m`. Consequently the automorphism
group has exactly this many **singleton orbits** on the possible
comparison pairs.

*Proof.* Every bottom `b_i` has no predecessors and exactly
`i+1` successors. Every top `t_j` has exactly `m−j`
predecessors and no successors. Automorphisms preserve predecessor
and successor counts. Within the bottoms the successor counts
`1,2,...,m` are distinct; within the tops the predecessor
counts `m,m−1,...,1` are distinct. Bottoms cannot map to tops:
the former have nonzero outdegree and zero indegree, the latter
the reverse. Thus every element is individually fixed.

Incomparable pairs comprise `binom(m,2)` bottom–bottom pairs,
`binom(m,2)` top–top pairs, and `binom(m,2)` cross pairs
`(b_i,t_j)` with `j>i`. Their sum is `3·binom(m,2)`.
Since `Aut(P_m)` contains only the identity, no two different
incomparable pairs lie in the same orbit. ∎

**Corollary 2 (odd sizes).** For `n=2m+1`, the ordinal sum
`Q_m=P_m ⊕ C_1` (add one new key above every original key) also
has trivial automorphism group and exactly `3·binom(m,2)`
incomparable pairs. The new greatest key is fixed, and the
restriction of any automorphism to `P_m` must fix all original
elements by Theorem 1. The new key is comparable with every old
key, so it adds no incomparable pairs.

In particular there are posets on every sufficiently large `n`
with **quadratically many pair orbits** even after perfect
within-state automorphism reduction.

## 2. What this does and does not imply

An exact minimax decision step considers possible incomparable
pair comparisons. Quotienting candidate pairs by `Aut(P)` is
sound, because relabelling by a poset automorphism maps each
outcome subtree to an equivalent one. But on this family
`Aut(P_m)=1`, so quotienting candidate moves removes **zero**
moves: the count remains `Θ(n²)`.

This **does not prove** a lower bound of `n²` comparisons,
`Ω(n²)` computational time, or
`2^{Ω(n log² n)}` runtime for computing `S(n)`:

- a smarter algorithm may select a good comparison without
  enumerating every candidate;
- other structural reductions, admissible pruning, and
  cross-state canonicalization may still help;
- being a possible intermediate poset does not establish that
  the worst-case exact search must visit it.

The theorem rules out only the **universal claim** that
within-state automorphism-orbit pruning alone makes the
number of candidate comparisons subquadratic at every state.

## 3. Reproducible finite checks

The reference code constructs `P_m` in successor-bitmask
form, verifies the exact count of incomparable pairs, and
enumerates every label permutation to count automorphisms for
small sizes `n≤8`. Values:

| `m` | `n=2m` | incomparable pairs | `|Aut(P_m)|` |
|---:|---:|---:|---:|
| 2 | 4 | 3 | 1 |
| 3 | 6 | 9 | 1 |
| 4 | 8 | 18 | 1 |

The proof is independent of the finite checks. Unlike
dynamic programming that memoizes every reachable state,
the small automorphism checks do not claim any general
upper or lower bound for the exact-search running time.

To reproduce:

```sh
python3 scripts/time_exponent_probe.py
python3 -m unittest tests.test_time_exponent -q
```

## 4. Relation to the main project

The currently published decision DFS has worst-case numeric-`n`
time `2^{O(n log² n)}` and polynomial space; for binary input
this is double-exponential in the input length. This note
does **not** improve or lower-bound that exponent. Symmetry,
duality and ordinal-sum simplifications are documented in
`docs/research-compression-next.md`,
`docs/research-orientation-modules.md`, and
`docs/research-series-decomposition.md`.
Their methods remain compatible with this obstacle.

**Source attribution:** The poset construction, proof and
bounded calculations are elementary deductions/experiments
in this note, not claimed original in the poset literature.
The exact-minimax model is Lean kernel-checked in
`SoringP1/Minimax.lean`. The worst-case sorting-search
literature includes Stober–Weiß, *Lower Bounds for Sorting
16, 17, and 18 Elements*, ALENEX 2023,
https://arxiv.org/abs/2206.05597.
