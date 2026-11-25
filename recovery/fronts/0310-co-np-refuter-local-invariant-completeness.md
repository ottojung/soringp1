# co-np-refuter-local-invariant-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

mqBpe9r6E9Rv3KDSShO9Xl-problems

## exit_state

clearexit

## question

Is there a polynomial-time verifiable local refuter invariant I(P,c,b) on partial orders P, comparison c, and remaining budget b such that for all n and k<S(n), I certifies from the antichain root that every adaptive sorter fails within k comparisons, without enumerating winning-frontier classes?

## basis

problem.md leaves coNP/NP membership open; docs/research-winning-frontier-barrier.md and research-hardness-boundaries.md separate state explosion from verification, while prior fronts addressed adversary compression/duality but not a fixed local refuter-invariant completeness claim.

## falsifier

Produce either (a) an infinite all-n family with k_n < S(n) but no invariant in a fixed natural local class (e.g. width/rank/linear-extension-potential summaries with poly-size certificates) is complete, or (b) a concrete sound invariant whose root completeness would imply a known-unlikely collapse via a checkable reduction.

## implication

A sound and complete polynomially checkable local refuter invariant would place SORT-BOUND-U in coNP; a completeness obstruction for natural invariant classes would be a barrier theorem distinct from winning-frontier enumeration and from NP certificate soundness.

## finding_unverified

T-BOUND-U` in `coNP` via a local refuter, a candidate object must certify `∀` sorter strategies `∃` failing path (adversary win). Two precise local forms and their obstructions:

1. **Deterministic poly-time local adversary rule** `o = A(P,c,b)`, sound and complete: complete means `S(P)>b => ∀c A(P,c,b)` gives an outcome with `S(P|o)>b-1`. Such `A` would be a polynomial-time winning adversary oracle; iterated from `A_n` it would decide/refute by play but, as a *static* poly-checkable certificate for the whole `∀` strategy tree, it still requires witnessing all sorter moves unless compressed into a proof. A single local rule is not by itself a short coNP certificate unless accompanied by a polynomial proof that it wins against all `c` at all reached states.
2. **Inductive invariant predicate** `J(P,b)` with local conditions `J(P,0)=>¬total(P)`, `J(P,b+1)=>∀c ∃o J(P|_{c,o},b)`, `J(A_n,k)` : sound by induction, and root completeness is equivalent to `k<S(n)=>J(A_n,k)`. Verifying the `∀c∃o` clause *as a certificate* is the hard part: checking it for one stated `P` is local, but proving `J(A_n,k)` by exhibiting a fully verified strategy/invariant object can still be exponentially large (the winning-frontier/strategy explosion documented in `docs/research-winning-frontier-barrier.md`). Thus “local” soundness is cheap; “local + poly-checkable + complete from root” is exactly the missing compression.

**Consequence (deduction).** No theorem here gives `coNP` membership; the obstruction is: natural local potentials fail completeness (Finding 1), exact extension counts fail local checkability (Finding 2), and universal strategy refutation needs a compressed `∀`-moves proof not supplied by local soundness alone (Finding 3). Conversely, exhibiting any sound, root-complete, genuinely polynomial-size polynomial-time verifiable LRI certificate system would be a substantive `coNP` upper-bound result (not claimed).

## Failed/discriminating approaches
- **Info/log-extension potential as complete refuter:** refuted at `n=12,k=29` (`S(12)=30`, `⎡log2 12!⎤=29`).
- **General-poset exact counting as local check:** blocked by `#P`-completeness (Brightwell–Winkler); antichain-only counting is not the issue.
- **Conflating certificate soundness with completeness:** a local rule may be sound on reached states yet certify no root refutation in the non-tight regime; this is the same soundness/completeness gap emphasized in the frontier basis.
- **Winning-frontier enumeration:** explicitly excluded by assumption and already known to explode (`docs/research-winning-frontier-barrier.md`).

## Exact obstruction / honest limit
I did **not** produce (and do not claim) an all-`n` infinite family defeating *every* fixed natural local class beyond the information-potential class formalized above, nor a sound invariant whose root completeness yields a standard unlikely collapse via a fully checkable reduction. The clean all-`n`-relevant obstruction established here is: **any refuter invariant dominated by the extension-count information bound is root-incomplete**, witnessed at `n=12`; and general local use of extension counts is not polynomially checkable. A stronger “no fixed poly-checkable local `I(P,c,b)` is root-complete” theorem would require either (a) a uniform infinite family of `(n,k_n<S(n))` pairs provably outside a precisely defined invariant class, or (b) a reduction from completeness to a collapse — both open from this analysis. No Lean/repository changes made.

## Other metadata

```json
{
  "finished_at": 1793866257.682521,
  "started_at": 1793866034.6711557
}
```
