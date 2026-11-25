# excess-element-threshold-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

kuOGrAtFi8SOPcjycHVs27-seed

## exit_state

clearexit

## question

Is the minimum ground-set size g(n) of a poset with e(P)<=n! and m(P)>S(n) equal to n+1 for every sufficiently large n, or does every such threshold witness require at least (1+epsilon)n elements?

## basis

Monotonicity gives m(Q)<=S(n) for every poset on at most n elements, so g(n)>=n+1; the board #301 2026-11-07 threshold proof supplies only ordinal sums A_k with 6k elements, leaving g(n) open.

## falsifier

An explicit all-n family of (n+1)-element posets with e(P_n)<=n! and m(P_n)>S(n), certified by exact minimax or by matching upper and lower bounds.

## implication

Measures how far the universal threshold obstruction lies beyond the n-element reachable state space; g(n)=n+1 would make it a one-element extension phenomenon, while g(n)=Omega(n) separates it from any reachable state.

## finding_unverified

The current checkout is still clean; I’m checking the prior investigation’s runtime/output and the durable front record before deciding whether any report was actually posted. I will not retry a post unless the board confirms it is absent.
No board post or repository change is present. The previous work did produce a useful finite computational check: on six elements, exhaustive exact minimax finds no witness for the n=4 threshold, while a seven-element poset gives one; it also finds seven-element witnesses for n=5. I’m verifying the enumeration logic and whether the candidate at n=5 is simply the already-known ordinal-sum example before reporting this as a limited finding.
**No all-\(n\) theorem or counterexample was established.** The front remains open; I found no basis to choose between \(g(n)=n+1\) eventually and a linear-size lower bound.

I independently reran a finite exact enumeration of unlabeled posets through seven elements. For \(n=4\), it found no six-element witness, but found seven-element witnesses with \(e(P)=21\) and \(m(P)=6>S(4)=5\). For \(n=5\), it found seven-element witnesses with \(e(P)\le120\) and \(m(P)=8>S(5)=7\). The recurrence computes the exact minimax value for each enumerated poset; the enumeration only covers these small ground-set sizes and does not establish \(g(n)\) for larger \(n\). The \(n=4\) witness is already among the board’s known examples, so this is a bounded check, not a new theorem.

The board’s threshold result uses ordinal sums with \(6k\) elements; that construction does not decide whether witnesses can be reduced to \(n+1\) elements or must be larger. General-poset minimax witnesses also do not by themselves provide complete certificates for \(S(n)\): verifying a supplied witness is a soundness check, not a completeness result.

No repository or Lean changes were made, and no board post was made. The checkout is clean. The attempted eight-element search was killed before completion, so it yields no conclusion.

## Other metadata

```json
{
  "finished_at": 1794084083.7073293,
  "started_at": 1794081338.3431263
}
```
