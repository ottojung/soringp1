# linear-space-unary-decision

## status

investigated

## origin

ai_proposal_unverified

## agent_id

SAUHS1hnicN6eTH0ll7CUh-delivery

## exit_state

clearexit

## question

Does SORT-BOUND-U admit a deterministic linear-space decision procedure, i.e. O(N) work-tape bits on unary input 1^n # 1^k of length N, improving the established O(N log(N+2))-space budgeted transcript DFS without any time blowup change?

## basis

docs/research-budgeted-dfs.md section 5.3 derives the current O(N log(N+2)) space bound; the exact-evaluator-time-exponent front forced state identity at Theta(n log^2 n) bits but never targeted the space exponent of the decision procedure itself, and no linear-space claim appears in problem.md or on board #301.

## falsifier

Attempt to replace every multi-bit component of the transcript DFS (the path stack, the pair cursors, and the counter bookkeeping) by an O(1)-bits-per-level encoding, and isolate a specific concrete state family at some fixed n where the encoding is forced to spend log N bits per remaining level; failure to fit O(N) bits refutes the improvement for this algorithm family.

## implication

Proving the O(N) bound would tighten the PSPACE membership of the unary language to a linear-space bound, a strictly stronger uniform result; an authenticated forced-stack lower bound for the DFS family is a barrier theorem showing that only fundamentally different traversal or symbolic methods can close the gap further.

## finding_unverified

The transcript-DFS family cannot achieve O(N) bits: its path stack has depth k ≤ N levels, and each level must store a cursor over binom(n,2)=Ω(n²) candidate pairs, requiring Ω(log n)=Ω(log N) bits per level, giving Ω(N log N) bits total. The reachability workspace adds another Ω(N log N)-bit term. Hence the established O(N log(N+2)) bound is the best this algorithm family yields; only a fundamentally different traversal/symbolic method could close the gap. No repository changes made.

## Other metadata

```json
{
  "finished_at": 1793232026.9983149,
  "started_at": 1793155086.3081763
}
```
