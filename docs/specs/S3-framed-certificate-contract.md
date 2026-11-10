# Framed-certificate contract (S3, scoped draft, #47-aligned)

**Status:** scoped draft, docs-only. Aligned with
`docs/research-framed-certificate-frontier.md` and the executable checker
`scripts/check_framed_strategy.py`. Exact all-`n` completeness at `S(n)` is
**OPEN**. No `NP` membership for unrestricted `SORT-BOUND-U` is claimed.

## Grammar (summary; authority is the frontier note + checker)

- Certificate: acyclic directed graph of comparison instructions.
- Root: guaranteed strict order `R = ∅`.
- Arc: extend `R` with that comparison, take transitive closure, apply the
  supplied slot permutation.
- Join: intersect guaranteed relations of all feasible incoming arcs
  (never adds unjustified knowledge; feasible/infeasible outcomes and
  permutations checked locally).
- Terminal: resulting guarantee must be a total order.
- Depth: longest execution path has `≤ k` comparisons.

## Checker / soundness / size

- **[paper proof + implemented checker]** Sound: all real input orders are
  included in the abstract set `R`; intersection is conservative.
  Checkable in time polynomial in the **explicit** graph length and `n`.
- Size: explicit graph length (nodes + arcs + permutation bits). A claim
  "polynomial-size at exact budget" must state the polynomial in `N=n+k+1`
  and exhibit the encoding; full-slot permutations are polynomial-bit but
  must be counted.
- Known constructions **[paper construction]**: quadratic bubble-sort
  witness (says nothing about optimality); `O(n²)`-node merge-schedule DAG
  with `O(n log n)` path length (`Σ pq = n(n-1)/2`); rank-envelope joins
  for pending insertions (Ford–Johnson embedding needs frame/boundary
  review; bound `F_FJ(n) = Σ ⌈log₂(3j/4)⌉` subject to that review).
- Known limits **[paper proof / deduction]**: arbitrary comparator networks
  need not be accepted if outcomes join immediately (5-comparison 4-element
  counterexample in the frontier note); balanced-merge architecture exceeds
  `log₂(n!)` by `(log₂ e − 1)n + O(log n)`, excluded from exact optimality
  for large powers of two by Sergeev `S(n) = log₂(n!) + o(n)`.

## Completeness (explicitly OPEN)

**[open]**: whether for every `n` some graph of `poly(N)` size attains
height exactly `S(n)`. If proved, then `SORT-BOUND-U ∈ NP` would follow;
no such all-`n` theorem is known and none is claimed here. Parberry
coNP-completeness for arbitrary sorting-network correctness does not rule
out one optimal adaptive witness per `n`, and does not establish one either.

## Relation to S2 (no simulation claim)

Programs subsume DAGs schematically (a DAG is a scheduled-compare program),
and programs add transitive-closure-derived state plus adaptive choice, but
**whether programmatic state rules compress any family that explicit DAGs
cannot is OPEN**. In particular: whether an `FO(TC)_v` program simulates a
forgetful framed DAG with only constant overhead is unproved here; do not
cite it as established.
