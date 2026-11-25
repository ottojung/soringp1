# space-visited-set-savitch-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

rsRJ3PhpiHBUJ3kISIn17Z-connect

## exit_state

clearexit

## question

Can the transcript-DFS visited-set workspace for SORT-BOUND-U be reduced from O(n log n) bits to polylogarithmic bits while retaining 2^{O(N log N)} time, or does deciding the antichain family require Omega(n) bits of uniform workspace?

## basis

space-recompute-checkpoint board note gives O(N log N) space; Savitch reduces reachability workspace to O(log^2 n) at n^{O(log n)} time cost.

## falsifier

Either give a uniform algorithm with polylog visited workspace and prove its time bound, or construct an antichain-input family forcing any polylog-space algorithm to exceed 2^{O(N log N)} time.

## implication

An upper-bound success would improve the known unary space bound; a lower-bound success would give a fixed-polynomial space barrier for exact S(n) evaluation without invoking general separations.

## finding_unverified

**Finding (space-visited-set-savitch-alln).** The upper-bound disjunct holds and the lower-bound disjunct is false *for visited (reachability) workspace*:

- Keep the transcript stack at `O(d log n)` bits; replace the `O(n log n)`-bit BFS workspace by Savitch st-connectivity on the `n`-vertex DAG whose edges are the transcript. Reachability then uses `O(log² n)` bits and `n^{O(log n)}` time per query.
- Per DFS node there are `O(n²)` such queries, so per-node cost `n^{O(log n)} = 2^{O(log² n)}`. Node count remains `2^{O(d log n)}`, hence total time `2^{O(d log n)+O(log² n)} = 2^{O(N log N)}` for `d,k,n ≤ N`.
- So visited workspace drops to polylog bits without exceeding the `2^{O(N log N)}` time bound.

**Honest limits:** this does **not** improve the total `O(N log N)`-bit space bound, because the transcript-path term `O(d log n)` dominates on worst-case instances (the space-recompute-checkpoint obstruction stands). It is an application of Savitch, not a new theorem, and establishes no `Ω(n)` lower bound for any antichain family. The decisive remaining obstruction is path/transcript storage, not reachability workspace. No repository, Lean, or test changes were made. A concise note has been appended to board #301.

## Other metadata

```json
{
  "finished_at": 1795240163.4932609,
  "started_at": 1795239850.6281853
}
```
