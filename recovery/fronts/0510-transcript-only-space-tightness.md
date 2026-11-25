# transcript-only-space-tightness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4GSrwLTEKoXwXlnntrowtB-where

## exit_state

clearexit

## question

For the unary threshold language SORT-BOUND-U with input length N=n+k+1, does every transcript-only deterministic decider that replays only the comparison-outcome path (no poset-state memo) require Omega(N log N) work-tape bits on the infinite no-instance family k=ceil(log2(n!))-1, or is there a uniform o(N log N)-space transcript-only decider?

## basis

docs/problem.md section 5.3 gives transcript-only DFS in 2^{O(N log N)} time and O(N log N) bits; board #301 time-exponent barrier proves 2^{Theta(n log^2 n)} isomorphism-fine states are forced for canonical memoization but explicitly leaves sound coarser summaries open, distinguishing soundness of state identity from completeness.

## falsifier

Either prove an Omega(N log N)-bit lower bound for transcript-only deciders on the stated no-instances, or exhibit a uniform transcript-only algorithm using o(N log N) bits with correctness and space accounting; isomorphism-memoized bounds do not settle it.

## implication

Tightness would be the first space-optimality barrier for the budgeted-DFS upper bound and would force any improved SORT-BOUND-U evaluator to leave the transcript-only family; a smaller-space transcript algorithm would directly improve the known uniform space envelope for exact S(n).

## finding_unverified

at path among the possible comparison transcripts of length `t` (ordered pair choices from the current incomparable set, `\le B_n` possibilities per step before outcomes; outcomes give an additional factor) requires at least
`Omega(t log B_n)=Omega(t log n)` bits at that point (for `n>=3`), by counting/information.

On the front family, `t` reaches `k = ceil(log2(n!)) - 1 = Theta(n log n)` and `N=Theta(n log n)`, hence such an explicit-transcript representation requires `Omega(k log n)=Omega(N log N)` work-tape bits on paths of maximal depth. Numerically (raw pair-index encoding, no cursor): `(n,k,N, k*ceil(log2(B_n+1)) bits) = (10,21,32,126), (20,61,82,488), (50,214,265,2354), (100,524,625,6812)`, i.e. `~1.17 * N log2(N+1)` bits already at `n=100`, matching the `Theta(N log N)` scale of §5.2/§5.3.

**Consequence `[deduction]`.** The known `O(N log N)`-bit transcript-only DFS upper bound is **scale-tight relative to storing an explicit length-`k` comparison transcript**: it cannot be improved to `o(N log N)` by any method that materializes (or information-equivalently preserves) the full current comparison path. This directly targets the “replays only the comparison-outcome path” mechanism: replay requires the path.

## What this does **not** establish (honest limits)

- **Not a proved `Omega(N log N)` lower bound for every transcript-only deterministic decider** as an arbitrary Turing machine meeting the informal front description. A full theorem would need a formal definition of “transcript-only, replays only the comparison-outcome path, no poset-state memo” (what control state is allowed beyond the path? can the machine be in distinct configurations after different backtrack histories without storing them as a poset memo?). I did not produce such a model-and-proof.
- **No `o(N log N)` transcript-only algorithm exhibited.** I found no correctness-and-space-accounted construction; I also did not prove none exists outside the explicit-transcript/storage interpretation above.
- **No complexity-class consequence proved here.** Tightness in this restricted family would be a barrier only for *transcript-only/budgeted-DFS-style* evaluators (forcing any improved evaluator to leave that family), not a lower bound for `SORT-BOUND-U` or for `S(n)` in general, and not a separation.
- **No Lean/repo changes, no primary-new theorem.** Small experiments were limited to the arithmetic/bit-count sanity checks above; I did not run heavy enumeration (`n>=6` full minimax is infeasible here). Useful negative outcome preserved in this report: simple compression/implicit-cursor/outcome-only/recomputation angles did not yield a disproof.

## Bottom line
- **Disproof attempt:** no uniform `o(N log N)`-space transcript-only decider found.
- **Best supported mathematical point:** on the stated family, an explicit comparison-path transcript has unavoidable size `Theta(k log n)=Theta(N log N)` bits, so the §5.2/5.3 transcript-only upper bound is asymptotically tight *for algorithms that retain the full replayable comparison path*; any genuine `o(N log N)` improvement would have to avoid storing that path while still replaying/deciding correctly (and staying outside poset-state memoization), which remains the exact unresolved obstruction.
- **Status:** exact all-`n` falsifiable resolution (proved general lower bound or a concrete smaller-space transcript algorithm) **not achieved** here; I report the obstruction and failed disproofs rather than claiming a theorem.

## Other metadata

```json
{
  "finished_at": 1794435265.4321966,
  "started_at": 1794426078.681841
}
```
