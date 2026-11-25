# adversary-strategy-certificate-conp

## status

investigated

## origin

ai_proposal_unverified

## agent_id

gx5BTBqXqVzbTuT3IfYyHN-macerated

## exit_state

clearexit

## question

For all integers n,k with S(n)>k, does there exist a polynomial-in-(n+k+1)-size, polynomial-time-checkable adversary winning-strategy certificate for the minimax comparison game G(n,k)?

## basis

Deduction from docs/problem.md and docs/research-certificates-barriers.md: S(n)>k iff the adversary wins G(n,k), but no succinct no-instance certificate or coNP membership is known.

## falsifier

Exhibit an infinite family (n_i,k_i) with S(n_i)>k_i such that every correct adversary strategy witness for G(n_i,k_i) requires superpolynomial size in n_i+k_i.

## implication

A uniform yes answer with a verifier would place SORT-BOUND-U in coNP, strengthening its known position below PSPACE for the unary threshold language.

## finding_unverified

ories (tree/DAG/branching program of states) is checkable in time polynomial in its size if it carries enough local information, but its size is the obstruction: worst-case reachable/state counts are `2^{Theta(n^2)}` (A001035-scale), and large winning frontiers exist at fixed depths (`research-winning-frontier-barrier.md`: `2^{Omega(n (log n)^2)}` nonisomorphic winning states for constructed families). Crucially, those enumeration barriers exclude methods that must list the whole frontier, **not** every possible selective/symbolic adversary certificate.
   - Therefore the explicit-strategy route fails as a *known* succinct certificate, but does not establish the requested falsifier (“every correct adversary strategy witness requires superpolynomial size”).

## Concrete failed approach (attempted refutation direction)
- **Attempt:** derive the falsifier by forcing any correct adversary witness to encode/visit a superpolynomial winning frontier (or all optimal adversary responses), using the `2^{Omega(n (log n)^2)}` winning-frontier phenomenon and the optimal-play/DAG state explosion. 
- **Why it failed / did not close:** (i) a certificate need not enumerate states; it may compress play by an invariant, proof, or symbolic object; (ii) the frontier theorems are existence/counting statements about states, not lower bounds on the description complexity of *some* valid certificate for the corresponding `(n,k)`; (iii) I found no argument that every poly-time-checkable proof of “adversary wins” must implicitly separate or list superpolynomially many cases. Hence no infinite superpolynomial witness-size family was exhibited. [`deduction`]

## Exact obstruction
To answer the front affirmatively one needs a **sound, complete, polynomial-size, polynomial-time-checkable** object certifying `F(antichain_n) > k` for the relevant unary instances (or, equivalently for the decision gap, for all true `S(n)>k` instances); to answer it negatively (the stated falsifier) one needs an unconditional/absolute lower bound against **all** correct certificate formats for an infinite family. The obstruction is:
- known potentials/certificates split into *sound-but-uncheckable* (general `e(P)`), *sound-but-incomplete* (information/entropy in the non-tight regime), or *complete-but-nonsuccinct* (explicit strategies/exhaustive search); and
- no compact canonical invariant stronger than `log2 e(P)` is known for the exact minimax adversary at the antichain root (`research-certificates-barriers.md` §8.2), while proving impossibility of every succinct witness would be a major proof-complexity/coNP-barrier result not available here and not implied by current enumeration/frontier theorems.

## Honest limits
- **Not proved:** `SORT-BOUND-U ∈ coNP`, `SORT-BOUND-U ∉ coNP`, existence of any uniform succinct adversary certificate, or existence of the requested infinite superpolynomial witness-size family. No new theorem or counterexample is claimed.
- **No experiment discriminated** a hypothesis here beyond what the cited documents/literature already establish (the critical gap is logical/certificate-theoretic, not a small-`n` enumeration gap I could close).
- **Process note:** this is a mathematical/status report only; no Lean or repository source changes were made (no substantive independently checkable new theorem/counterexample to integrate). Any board posting of this assessment should follow `docs/operations.md` and only if it adds a non-duplicative, precise obstacle record.

## Other metadata

```json
{
  "finished_at": 1794296323.5521111,
  "started_at": 1794296162.8586507
}
```
