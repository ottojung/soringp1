# unary-threshold-linear-space-nondecomposition-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

fWSsuYDypdM5mVzVFXz3q5-ischial

## exit_state

clearexit

## question

Can SORT-BOUND-U be decided in O(N) work-tape bits for all N = n+k+1 by a uniform method that is not transcript DFS, such as catalytic or certificate-replay computation?

## basis

linear-space-unary-decision shows transcript DFS needs Omega(N log N) bits, while catalytic-reversible-exact-evaluation-space leaves non-transcript methods open.

## falsifier

Construct such an O(N)-space decider for all n,k, or prove an Omega(N log N) space lower bound for every uniform decider on the accepting family A = {1^n # 1^{S(n)}}.

## implication

Linear space would improve the PSPACE membership to a near-linear uniform space bound for this tally language; a matching lower bound would close the space question for SORT-BOUND-U.

## finding_unverified

Posted the finding to Antonina #301 (no repository/Lean/test changes).

**Result:** Neither horn of the falsifier was achieved. O(N) space for `SORT-BOUND-U` remains open; no Ω(N log N) lower bound for arbitrary uniform deciders was proved.

Key points:
- Transcript/play-simulating methods are forced to Ω(N log N) bits; reversible computation gives no improvement; alternating O(N) space would imply a 2^{O(N)}-time algorithm.
- Catalytic storage has capacity Ω(N log N), and encrypted-storage fails due to Ω(N log N) ordinary key bits; no catalytic algorithm is known.
- The winning-frontier barrier is enumeration-only: it rules out listing winning posets, not selective/symbolic/catalytic methods, and does not prove arbitrary-solver hardness.
- Certificate soundness is easy for explicit trees, but succinct sound certificates (NP membership) and completeness remain open; the frontier count does not rule out succinct certificates.
- General-poset hardness results do not transfer to the antichain root without a reduction.

Honest limit: O(N) space is at least as hard as improving the time bound from 2^{O(N log N)} to 2^{O(N)} (or proving a matching time lower bound). Next decisive check is whether S(n) is computable in 2^{O(n)} time.

## Other metadata

```json
{
  "finished_at": 1795309152.2656868,
  "started_at": 1795308570.8074217
}
```
