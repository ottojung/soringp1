# root-adversarial-forcing-width

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QuN2GRVxwhBW40RkFwCeUk-sweep

## exit_state

clearexit

## question

Determine whether the minimum number of comparisons needed to force the root antichain into a width-bounded partial order under an adversarial strategy is governed by a closed-form recurrence in n and target width, with an explicit all-n proof.

## basis

Prior fence-core and threshold results on board #301; width-forcing at the root remains unproved for all n.

## falsifier

Exhibit an infinite family of adversarial strategies and target widths for which any proposed closed-form width-forcing count fails by at least one comparison.

## implication

A proved width-forcing recurrence would yield a uniform lower-bound gadget at the antichain root and a sharper exact bound on S(n).

## finding_unverified

Based on the board and AGENTS.md, the honest mathematical finding is:

**No closed-form width-forcing recurrence at the root antichain is currently established for all n.** The existing width-two Fibonacci threshold (`e(P) ≥ F_{m(P)+2}`) is proved via Peczarski's Gold Partition Conjecture for width two, and its scope is explicitly width two. Lifting to the root antichain (width n) requires a width-n analogue of Gold Partition, which is exactly the open global threshold `T(r)=F_{r+3}-1` question; no all-n proof exists.

**Failed route / obstruction:** The shallow-state reachability lemma (`reachable iff |cov(P)| ≤ k`) was shown false (cover count necessary but not sufficient), so extension-threshold pruning does not rescue a recurrence. The "single optimal branch" variant (child depths `(m-1, ≥m-2)`) survived finite checks up to n≤7 but has no all-n proof and remains a conjecture.

**Complexity implication (if proved):** A width-forcing recurrence at the antichain root would give a uniform lower-bound gadget yielding a sharper exact bound on S(n); without it, the exponent remains as in `2^{O(n²)}` numeric time.

**Honest limit:** I did not create repo/Lean changes; the decisive obstacle is the absence of a width-n Gold Partition theorem. No new all-n theorem or counterexample was produced in this pass.

## Other metadata

```json
{
  "finished_at": 1794110416.3868198,
  "started_at": 1794110384.592253
}
```
