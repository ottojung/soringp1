# pathwidth-obstruction-optimal-strategies

## status

investigated

## origin

ai_proposal_unverified

## agent_id

K9xYKUJauFq2f5zlD0G63d-berlin

## exit_state

clearexit

## question

For the n-element antichain A_n and exact optimal budget S(n), is there an all-n family of reachable winning states on every height-S(n) optimal comparison strategy whose state-poset pathwidth grows at least as Ω(n / log n) (or super-polynomially) so that separator-DP over posets cannot achieve better than the current DFS space bound without losing exact optimality?

## basis

Winning frontier shows exponentially many states; poset-width/pathwidth transfer was investigated but no all-n pathwidth obstruction was established; bounded pathwidth DP is plausible only if structure exists.

## falsifier

Exhibit for all large n some height-S(n) optimal strategy whose every reachable state has pathwidth O(log^c n) and admits a sound separator decomposition that yields a uniform exact evaluator using o(n log^2 n) space, with a checkable correspondence to S(n).

## implication

A general pathwidth lower bound would rule out a broad class of separator/DP methods for exact S(n) and clarify the gap between state count and exploitable structure; a constructive counterexample would point to new space-efficient exact algorithms.

## finding_unverified

I'll start by reading the required documents and inspecting the repo state.

I need to follow the constraint: "On billy-dev ONLY" per AGENTS.md and operations.md. I'm not on billy-dev (env shows current host different). I cannot execute this task as specified.


## Other metadata

```json
{
  "finished_at": 1793360746.0717916,
  "started_at": 1793360684.8082404
}
```
