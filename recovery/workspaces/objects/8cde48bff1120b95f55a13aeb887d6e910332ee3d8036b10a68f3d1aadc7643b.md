# Exploration-first research agenda (2026-10-17)

**Status:** research notes and working hypotheses, **not** Lean theorems or new complexity-class classifications.

## Baseline before further formalization

The exact minimax sorting number `S(n)` is already studied extensively. For
`1 ≤ n ≤ 11`, the Ford–Johnson bound and the information-theoretic lower
bound coincide; the exact values are

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|----|----|----|
| S(n) | 0 | 1 | 3 | 5 | 7 | 10 | 13 | 16 | 19 | 22 | 26 | 30 |

At `n = 12`, the information-theoretic bound is `ceil(log₂(12!)) = 29`
but `S(12) = 30`. This is a known *structural obstruction*, not a new
result of this project. Understanding how the obstruction manifests in
comparison-state geometry could inform a more efficient exact evaluator.

**Sources:** Marcin Peczarski, *Towards optimal sorting of 16 elements*,
Acta Univ. Sapientiae Informatica 4(2), 2012, pp. 215–224,
https://real-j.mtak.hu/23036/2/Acta%20Info%202012_4_2.pdf
(especially the introduction, which attributes the n=12 proof to Wells);
OEIS A036604 https://oeis.org/A036604 is a sequence index, not a proof.
These are adaptive, worst-case pairwise-comparison sorting numbers, not
sorting-network sizes.

## A structural complexity warning: sparse threshold inputs

Consider the precise unary decision language from `docs/problem.md`:

`SORT-BOUND-U = {1^n # 1^k : S(n) ≤ k}`.

For strings of total length at most `m`, there are at most
`(m+1)^2` choices for the pair `(n,k)` (in fact fewer after accounting
for the delimiter). Thus the language is **sparse**.

Mahaney's theorem says a sparse set cannot be NP-hard under polynomial-time
many-one reductions unless `P = NP`. Therefore seeking an ordinary
many-one NP-hardness reduction to this *fixed unary language* is exceptionally
ambitious: success would imply `P = NP`, independently of whether we know
the language to be in NP. The theorem does **not** put this language in P or
NP; nor does it rule out other encodings, other forms of reduction, or
complexity classifications.

**Primary source:** Stephen R. Mahaney, *Sparse complete sets for NP:
Solution of a conjecture of Berman and Hartmanis*, JCSS 25(2), 1982,
pp. 130–143, https://doi.org/10.1016/0022-0000(82)90002-2 .
Open author manuscript:
https://ecommons.cornell.edu/entities/publication/02e42763-8a49-4dfe-9e73-59ccc016f74f

## Independent exploration fronts

These are **questions**, not a numbered queue of theorems to formalize.

### Structural compression of minimax states

Can symmetries, canonical partial-order states, decomposition, or restricted
classes of optimal decision trees reduce the worst-case state space? Develop
a candidate recurrence, state exactly when it preserves the optimum, and
try to falsify it with small examples and known sorting-number results.
Measure *state counts and computation time*, not only `S(n)` outputs.

### Complexity and certificate structure

What might a polynomially checkable certificate of `S(n) ≤ k` look like
without explicitly listing an exponential-size sorting tree? What would a
certificate for `S(n) > k` require? Explore limitations and succinct
representations on paper first; keep unary vs binary input length explicit.
Distinguish the complexity of *general decision-tree optimization* from
the single-parameter family `S(n)`.

### Explain non-tightness of information bounds

Study why `S(12) > ceil(log₂(12!))` despite equality at `n ≤ 11`.
Look for a reusable combinatorial invariant or obstruction stronger than
leaf counting. Audit precise primary sources before claiming novelty.

### Better exact computation (supporting, not the objective)

Use the Python evaluator for experiments and regression checks.
Compare search-space reduction ideas against known values and examples.
No amount of small-instance computation proves a complexity separation.

## Expected output from each investigation

Record a *precise question*, source and model, candidate claim or algorithm,
the smallest compelling example, one concrete falsification attempt,
what was learned, and the next unresolved obstacle. Distinguish literature
facts, deductions, experiments, conjectures, paper proofs, and Lean-checked
results. A useful negative result counts as progress.

## When to resume Lean

Keep the existing kernel-checked foundation. A new formalization should be
motivated by an independently justified, substantial result or an immediate
model-fidelity need, with a complete statement and an explicit explanation of
what verification will add. The previously missing minimax tree height
proof is now completed (A24); direct attention to structural research and
complexity-theoretic questions instead of routine proof-engineering.

## Deliverables produced (2026-10-17, exploration-first)

Three fronts investigated; research notes with companion programs (see the
README for the summary):

- **Structural compression** — `docs/research-state-compression.md`,
  `scripts/state_compression.py`. Reachable states are the labelled posets
  (A001035); the `S_n` quotient is exact and recomputes `S(8)=16`, `S(9)=19`.
- **Certificates and barriers** — `docs/research-certificates-barriers.md`.
  `SORT-BOUND-U ∈ PSPACE`, `SORT-BOUND-B ∈ EXPSPACE`; sparsity barrier is
  encoding-specific; no succinct tree certificate (`2·n! − 1` nodes).
- **Information-bound non-tightness** — `docs/research-n12-nontightness.md`,
  `scripts/nontightness_experiments.py`. No reusable scalar invariant; the
  obstruction is structural/global (smallest local failure at `e = 8`, `n = 5`).

These are hypotheses, falsifications and literature audits — not Lean theorems
and not a complexity classification. The minimax evaluator is now exact and
both-sided (A24: `S n = adv univ`); the still-open item is the complexity
classification of `SORT-BOUND-U`/`SORT-BOUND-B`, not the evaluator.
