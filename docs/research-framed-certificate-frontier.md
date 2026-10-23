# Framed sorting certificates: verified boundary and research frontier

**Status (2026-10-22):** paper constructions and open conjectures; not
Lean-checked. An executable *soundness checker* exists at
[`scripts/check_framed_strategy.py`](../scripts/check_framed_strategy.py).
The claims below concern deterministic adaptive comparison sorting of
**distinct labelled elements**, not fixed sorting networks, and the active
complexity target is **unary** `SORT-BOUND-U = {1^n#1^k : S(n) <= k}`.
The key unresolved implication is whether every true instance has a
polynomial-size certificate at the **exact** budget `S(n)`.

This note consolidates the useful part of
[issue #47](https://github.com/ottojung/soringp1/issues/47) without turning
the issue's exploratory comments into established complexity claims.

## 1. Certificate grammar, soundness, and missing completeness

A certificate is an acyclic directed graph of comparison instructions.
Every arc specifies a comparison outcome and a permutation of the n
current slots. At the root the guaranteed strict order `R` is empty.
At an outgoing arc, extend `R` with that comparison, take transitive
closure, and apply the supplied permutation. At a join, intersect the
guaranteed relations of all feasible incoming arcs. At a terminal node,
the resulting guarantee must be a total order; the longest execution
path must have at most k comparisons.

**[Paper theorem; implemented checker]** This is sound and checkable in
time polynomial in the *explicit* graph length and n: all real input
orders are included in the abstract set represented by `R`, and
intersection never adds unjustified knowledge. Feasible/infeasible
outcomes and permutations are checked locally; depth is computed in
DAG order. If, for every n, **some** graph of polynomial size attains
height `S(n)`, then `SORT-BOUND-U ∈ NP`. No such all-n
polynomial-size completeness theorem is known.

An arbitrary correct comparator network need **not** be accepted if
its comparison outcomes are joined immediately: intersection may
discard disjunctive correlations used later. An optimal five-comparison
network for four elements already gives such a counterexample.
Conversely the grammar accepts a quadratic-size bubble-sort witness
for all n (issue #47); this says nothing about optimality.

Parberry's coNP-completeness result for *correctness of arbitrary
sorting networks* is another reason to avoid demanding polynomial-size
proofs for **all** programs. It does not rule out a polynomial
certificate for one optimal adaptive sorter for each n.

## 2. All-n polynomial DAG for adaptive merge sort

**[Paper construction; independent all-n implementation audit pending]**
For one merge of sorted contiguous queues of lengths p and q,
represent a state by remaining queue lengths (a,b), with
`1 <= a <= p`, `1 <= b <= q`. A prefix has already been
output in increasing order and is smaller than both queues. Compare
the queue heads; move the chosen smaller head to the end of the
prefix by an explicitly specified slot permutation. When a queue is
empty, append the other sorted queue without more comparisons.
The meet/intersection invariant is exactly the ordered output
prefix together with two ordered remaining queues.

There are pq comparison states for this merge, although a path
performs at most p+q-1 comparisons. Sequentially compose all merges
of a binary merge schedule and join their completed states. The
combinatorial identity

`sum_{merge nodes with child sizes p,q} pq = n(n-1)/2`

follows because every unordered pair of input elements is split
between the two children at exactly one merge. Hence the graph has
O(n²) comparison nodes and, for balanced merges, O(n log n)
**path length** (not O(n²)). Explicit full-slot permutations produce
a polynomial-bit witness.

**Important limit:** independent complete sorting of two equal
halves followed by an optimal equal-chain merge uses
`n log₂(n) - n + 1` comparisons for n a power of two. This exceeds
`log₂(n!)` by `(log₂(e)-1)n + O(log n)`; Sergeev's
`S(n) = log₂(n!) + o(n)` therefore excludes this architecture
from exact optimality for all sufficiently large powers of two.
Improving DAG sharing alone cannot repair this comparison deficit.

## 3. Rank-envelope joins for pending insertions

**[Paper construction; exact Ford–Johnson embedding needs independent
frame/boundary review]** Suppose a known increasing chain consists
of m current slots and pending elements x_j have certified rank
windows between original chain positions `ell_j` and `u_j`
(allowing boundary sentinels). If t other elements have been inserted,
the old `u_j` endpoint has shifted right by at most t positions;
the old `ell_j` endpoint has shifted right by at least zero.
It is therefore sound to retain the common weak invariant

`current[ell_j] < x_j < current[u_j+t]`

whenever those sentinel indices make sense. Inserting a chosen x_j
by binary search requires at most

`ceil(log₂(u_j - ell_j + t))`

comparisons. Expand this stage's search as a tree with O(n)
query nodes and permute slots to put the inserted element into its
selected rank. Regardless of the chosen rank, the other pending
elements satisfy the next stage's relaxed windows. Thus the leaves
can join with a *locally checkable* guarantee. With at most n
insertions the resulting graph has O(n²) query nodes.

For the standard Ford–Johnson winner/loser pairing construction, once
the winners a_i are sorted, each pending loser b_i satisfies
`b_i < a_i`; after t other insertions the paired winner is at
rank at most i+t. The next b_i can be inserted in at most
`ceil(log₂(i+t))` comparisons, independent of insertion history.
Frames used while recursively sorting winners can permute their
associated loser slots together with the winner slots; the odd
unpaired element requires a full-range insertion. Jacobsthal order
chooses i so that these bounds are cheap. These observations give a
plausible all-n polynomial framed certificate for the *standard
Ford–Johnson upper bound*, subject to checking the complete
recursive frame construction and odd case. The bound is

`F_FJ(n) = sum_{j=1}^n ceil(log₂(3j/4))`,

which is **not** equal to `S(n)` for every n. Nothing here proves
NP membership.

### A warning about counting states

A sorted chain with r pending pendant elements constrained by
`x_j < c_{a_j}`, with increasing anchor ranks `a_j`, has

`e(P) = product_{j=1}^r (a_j+j-1)`

linear extensions (the rooted-forest hook-length formula).
For explicit insertion schedules with anchors `a_j = 3j` or
`3j+1` independently, there are 2^r different isomorphism
types, yet forgetting all choices to the weaker anchors `3j+1`
costs only

`log₂ product_{j=1}^r (4j/(4j-1)) = (1/4) log₂ r + O(1)`

bits. Thus even exponentially many nonisomorphic reachable
histories do **not** imply that a forgetful DAG has to be large.
This is a supporting generic-poset construction; it is **not**
proved to be forced along any optimal root sorting strategy.

## 4. Entropy and information loss across joins

**[Paper identity; no e(P) counting algorithm claimed]**
For a node with annotation P let `m = e(P)`. If the next
comparison has a feasible outcome b with
`m_b = e(TC(P + outcome_b))`, set `q_b = m_b/m`.
At the child annotation Q, soundness gives `e(Q) >= m_b`.
The nonnegative **forgetting loss** is

`lambda_b = log₂(e(Q)/m_b)`,

and the binary outcome entropy is
`H = -sum_b q_b log₂(q_b)`.

Consider the following **auxiliary** random walk through a sound
certificate: sample each outgoing arc with probability `q_b`
*computed from its current annotation*. This walk effectively
resamples the compatible order after each forgetful join; it
need not equal the execution distribution of a single uniformly
chosen input permutation. For its path length D <= k,

`E[sum_over_queries (1 - H + lambda_b)] = E[D] - log₂(n!) <= k-log₂(n!).`

**Proof:** On one edge,
`log₂ e(Q) - log₂ e(P) = log₂ q_b + lambda_b`.
Conditioning on the current node makes the expected first term
`-H`. Sum along the DAG walk: the root has `e=n!` and every
accepted terminal has `e=1`. Subtract from the expected number of
comparisons. Both `1-H` and `lambda` are nonnegative.

On an **annotation-majority** path, always choosing `q_b>=1/2`,
the stronger deterministic telescoping identity is

`sum_edges (log₂(2q_b) + lambda_b) = D - log₂(n!) <= k - log₂(n!).`

A near-information-bound certificate therefore has only
`o(n)` *expected total* imbalance and forgetting under the
auxiliary walk; linear information loss would falsify that
particular compression scheme. Counting e(P) can be #P-hard, so
these are analytic **necessary conditions**, not polynomial-time
verification rules.

## 5. Decisive open investigations

1. **Exact optimality:** Does *some* optimal root sorter for every
   n admit a polynomial-size, sound framed certificate at height S(n)?
   An all-n positive theorem would yield unary NP membership.
2. **Sergeev compatibility:** His group-insertion construction
   gives `S(n) <= log₂(n!) + O(n/(log n)^(1/5))`, but stores
   pending keys in coupled interval containers. Specify a
   polynomial-state rank-envelope or nested-subroutine grammar
   with sound joins and an `o(n)` total comparison surplus, or
   explicitly falsify one such proposed grammar. Short *local*
   insertion routines do not automatically yield polynomial
   *global* control states.
3. **Adversarial root forcing:** For lower bounds, distinguish a
   bad reachable poset from one an adversary can **force against
   every height-k root strategy**; see
   [issue #48](https://github.com/ottojung/soringp1/issues/48).
4. **Independent checking:** Audit the Ford–Johnson lifted
   permutations and exact stage widths, and audit join/cost
   accounting before classifying an assertion as a theorem.

**Do not Lean-formalize these constructions solely to accumulate
lemmas or examples.** The next formalization should validate a mature,
substantial *all-n complexity theorem* and its machine-cost correspondence.

### Primary sources

- I. Sergeev, [*On the asymptotic complexity of sorting*](https://eccc.weizmann.ac.il/report/2020/096/) (ECCC TR20-096, 2020), group insertion and the sublinear comparison surplus.
- Stober and Weiß, [*Lower Bounds for Sorting 16, 17, and 18 Elements*](https://arxiv.org/abs/2206.05597), ALENEX 2023; finite optimality, not uniform certificates.
- I. Parberry, [*On the Computational Complexity of Optimal Sorting Network Verification*](https://ianparberry.com/research/sortingnetworks/), PARLE 1991; generic-network verification barrier, not fixed-root S(n).
- Stober and Weiß, [*On the Average Case of MergeInsertion*](https://doi.org/10.1007/s00224-020-09987-4); precise Ford–Johnson/Jacobsthal insertion schedule.
- J. Cremer, [*Selecting the 7th Smallest of 16 Elements Takes Exactly 28 Comparisons*](https://arxiv.org/abs/2610.18740) (2026); finite, proof-carrying DAG precedent for selection, not all-n optimal sorting.
