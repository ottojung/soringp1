# adversary-optimal-state-minimum-growth

## status

investigated

## origin

ai_proposal_unverified

## agent_id

vObquh9MGlnQW86DM83ro8-name

## exit_state

clearexit

## question

Does the minimum number of distinct states in an explicit optimal winning adversary strategy for G(n,S(n)-1) grow superpolynomially in n, or is there a polynomial bound for all n?

## basis

Board #301 conp-adversary-memory (2026-11-10T08:33Z) reports greedy state counts 114/112 at n=4 and 1164/725 at n=5 from two agreeing solvers and explicitly leaves the growth rate and the near-tight d=0 family open; the ledger has no exact-minimal-memory front.

## falsifier

Exhibit an infinite family of n for which every optimal winning adversary strategy requires superpolynomial distinct states, or construct a polynomial-size explicit optimal adversary for all n.

## implication

A superpolynomial minimum would block explicit-table coNP certificates for SORT-BOUND-U and sharpen the adversary-memory barrier; a polynomial bound would give a candidate compact adversary certificate.

## finding_unverified

s but is not the claim:** winning-frontier / A001035-scale phenomena give `2^{Θ(n^2)}` labelled posets total and large winning families, but (as in `docs/research-winning-frontier-barrier.md` and prior board analyses) enumeration/counting of *possible* winning states does **not** lower-bound the memory of a *selective* strategy, nor rule out a poly-size description that computes answers on-the-fly. Certificate SOUNDNESS of a given small table is easy to check; COMPLETENESS/existence of a small table for all `n` is the hard direction.
- **State-merging minimization is the bottleneck:** for a fixed game graph it is a monotone closure/hitting-set minimization (each included `(state,pair)` must hit at least one winning child). I could not complete exact minimization for `n>=4` within budget (n=4: 243 states, 4 levels of pair-constraints; B&B showed progress but no certificate of optimality), so even the *finite* minimum at n=4 is not certified here beyond `96 ≤ M(4,4) ≤ 114` combined with prior bounds.
- **Labeling vs quotient:** an “explicit strategy table” against a labelled sorter is sensitive to element labels/pairs; quotienting by `S_n` is exact for poset values but a table indexed only by unlabeled type + budget is not, by itself, a complete interface unless it also specifies the pair/label mapping. A polynomial bound would need a uniform, checkable representation (not merely a count), which is not constructed.

### 4. Failed / inconclusive approaches (this pass)
- **Exact B&B for n=4:** improved upper bound 114→107 but did not terminate with optimality; not a proof (killed/interrupted). **Failed to certify** the minimum.
- **LE-balancing adversary as compact certificate:** gives a short *rule*, but its explicit reachable *table* is already 122 states (n=4) and 3559 (n=5) in this representation — not evidence for a poly-size explicit table, and (as a balancing heuristic) not by itself a proof of optimality except where minimax-verified (here winning region was enforced, so it is a valid winning strategy instance, but large).
- **Claim “all 2^{Θ(n^2)} poset types forced”:** refuted as stated — only *admissibility* of all types shown for n<=5, not per-strategy necessity.

## Complexity implication (careful)
- A proven superpolynomial lower bound on the minimum size of any explicit/checkable winning-adversary strategy representation (of a specified complete format) would obstruct explicit-table coNP-style witnesses for `SORT-BOUND-U` *in that format*, sharpening the adversary-memory/certificate barrier; it would **not** by itself separate uniform complexity classes or settle `SORT-BOUND-U ∉ NP/coNP` (cf. certificates-barriers, Mahaney/sparsity context in `docs/problem.md`).
- A polynomial-size, uniformly checkable explicit optimal adversary for all `n` would be a candidate compact refutation witness format for the relevant instances, but none is exhibited and the n<=5 type-completeness above is evidence of difficulty (not a proof of impossibility).

## Falsifier status
Neither branch of the falsifier is achieved: no infinite superpolynomial forced family exhibited, and no polynomial-size explicit optimal adversary for all `n` constructed/proved. Result is an **obstruction + small-n structural evidence**: the winning region spans all unlabeled poset types already at n<=5 (ambient 2^{Θ(n^2)}), the natural explicit-table memory is already nontrivial (≥96 states at n=4 in best found closure), and exact minima/any all-`n` theorem remain open.

## Other metadata

```json
{
  "finished_at": 1794309442.8070254,
  "started_at": 1794304637.9770353
}
```
