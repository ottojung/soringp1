# cofn-adversary-certificate-size

## status

investigated

## origin

ai_proposal_unverified

## agent_id

1KC7GFOrIitCm4GnYOsegn-founding

## exit_state

succeeded

## question

Does the no-instance direction admit a polynomial-size checkable certificate — that is, must every adversary strategy that forces a sorting tree of height above k on the n-element antichain admit a compact explicit representation (such as a framed poset-exchange schedule or polynomially-representable strategy invariant), so that SORT-BOUND-U would lie in coNP if it lies in NP?

## basis

docs/problem.md establishes neither NP nor coNP membership for SORT-BOUND-U and the certificate literature (framed DAG checker, scripts/check_framed_strategy.py) covers sound verification of yes-side strategies only; board #301 serial-leaf/extension-count work supplies the arithmetic machinery candidates would need to bound.

## falsifier

Show that for n and k below S(n) there exist minimax-forcing adversary trees whose minimal representation is 2^{omega(poly(n))} bits under any candidate explicit certificate format (forcing every internal node's joint distribution of comparisons to be exposed), or prove that no-poset families like the staircase attainable only at depth Theta(n^2) already contradict polynomial exchange schedules.

## implication

A verified compact adversary certificate combined with any completeness side for yes-instances would settle coNP-membership of SORT-BOUND-U — a class question distinct from the quantified-root-adversary front, which sought a single concrete lower-bound invariant rather than a bounded-size certificate format — and would be the first certificate-theoretic statement about the no side of the minimax game.

## finding_unverified

We're already on billy-dev (hostname matches). Proceeding with the study.
I inspected the prior turn: it reached local reading and analysis only; no board post, commit, or repository edit was attempted. I’ll verify the worktree and relevant board records before wrapping up, and won’t repeat any external action.
**Finding: no compact, complete adversary certificate is established.** The proposed “exponential bits under any candidate format” falsifier is not a well-defined theorem until the certificate formats are restricted; in that unrestricted form it asks for a representation-independent lower bound that would effectively rule out coNP certificates for this language.

The useful, proved localization is the information-bound gap. Let \(C(n)=\lceil\log_2(n!)\rceil\). For \(k<C(n)\), the input is certainly a no-instance, and that condition is decidable in polynomial time by computing \(n!\) and comparing it with \(2^k\). Thus any difficult no-side certificates are needed only for
\[
C(n)\le k<S(n).
\]
This is a window of at most \(O(n)\) budgets per \(n\), and it is nonempty at \(n=12\): \(C(12)=29\), \(S(12)=30\). The existing literature’s exhaustive proof of that gap is evidence of a lower bound, but does not by itself give a polynomial-size certificate. This localizes the obstacle; it does **not** settle coNP membership.

For the natural explicit adversary format, soundness is straightforward: provide a response and successor state for every sorter query at each reached state, and check that all resulting plays remain non-total through the budget. The strategy can be checked in time polynomial in its own encoding. The missing direction is completeness with polynomial encoding size. This is distinct from the framed DAG checker’s **yes-side** soundness, and also from general-poset results: neither supplies a complete certificate for the fixed antichain root.

The suggested staircase obstruction does not establish a lower bound on these certificates. Posets requiring \(\Theta(n^2)\) comparisons to reach cannot occur on a play of a no-instance: \(k<S(n)\le O(n\log n)\). As prior work warns, a reachable or asymmetric poset is not necessarily one the adversary can force against every sorter strategy. Conversely, this reachability limit does not prove polynomial compression of the adversary’s relevant states.

A fixed-hidden-permutation adversary is not a shortcut: it simply follows one actual ordering, leaving the same need to account for all sorter plays. And a large explicit tree—or many states in a particular DAG—would only lower-bound that representation, not every possible checkable certificate format.

**Limit:** I found no new theorem or counterexample resolving whether every gap-region no-instance has a polynomial-size certificate. Any claim that *no* such certificates exist would go beyond this analysis; the repository’s stated complexity barriers put that kind of separation out of reach. No board post, commit, or repository change was made.

## Other metadata

```json
{
  "finished_at": 1793130202.95872,
  "started_at": 1793127990.8325195
}
```
