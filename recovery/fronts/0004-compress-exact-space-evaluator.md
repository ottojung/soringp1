# compress-exact-space-evaluator

## status

investigated

## origin

reviewed_seed

## agent_id

bh8mr8uxTg1L47gwIGFp3t-crushing

## exit_state

succeeded

## question

Construct and rigorously analyze a uniform exact evaluation algorithm for S(n) with asymptotically smaller workspace than the existing recurrence, explicitly accounting for representation and branch recomputation.

## basis

docs/problem.md established unary PSPACE membership and prior recomputation analyses; focus on a genuinely improved bound.

## falsifier

Give a concrete state family forcing the proposed compact representation to store superpolynomial independent decisions, or find a hidden recursive stack-space violation.

## implication

A verified uniform smaller-space bound would strengthen the known upper bound for SORT-BOUND-U even without proving P or NP membership.

## finding_unverified

**Finding:** Canonical root-replay does not currently give a justified space improvement for the all-budget DFS. Storing a DFS-node rank has a straightforward worst-case cost of \(O(k\log n)\) bits, the same order as the path stack. Regenerating a target node from the root at each frame can repeatedly traverse earlier subtrees; the direct bound grows to \(2^{O(k^2\log n)}\), rather than the existing \(2^{O(k\log n)}\) time. This rules out that naive reconstruction strategy, but does **not** prove that every exact evaluator needs the path stack or rule out a better canonical encoding.

The prior Savitch-style reachability observation still only reduces reachability scratch space; it leaves the DFS path and pair-cursor stack. No concrete state family forcing independent decisions in every evaluator emerged. I posted this precise blocker to board #301. No repository or Lean changes were made.

## Other metadata

```json
{
  "failure_kind": "transient_backend_unavailable",
  "finished_at": 1792795805.5070848,
  "launch_error": "antonina: agent bh8mr8uxTg1L47gwIGFp3t-crushing is still running; use --steer to redirect it\n",
  "retry_after": 0,
  "started_at": 1792795713.7047305,
  "transient_failures": 7
}
```
