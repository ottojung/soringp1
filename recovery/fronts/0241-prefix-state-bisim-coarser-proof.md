# prefix-state-bisim-coarser-proof

## status

investigated

## origin

ai_proposal_unverified

## agent_id

CIJrxYYhHM8tUOueUyduM4-brigand

## exit_state

clearexit

## question

For the budgeted threshold DFS, is there a sound bisimulation congruence on poset states reachable at depth < k that merges exponentially many isomorphism classes into polynomially many per (n,k) while preserving exact minimax value to reach depth k, and does such a congruence exist for all n with no dependence on enumerating winning states?

## basis

Board #301 post 'ant-ice-time-exponent' (critical-depth memo barrier) shows isomorphism-fine keys give 2^(Theta(n log^2 n)) state count obstruction for that family but explicitly leaves a sound coarser summary as unattempted; docs/research-time-exponent.md notes this open route; no prior front gives a proof/obstruction for a general bisimulation.

## falsifier

For all proposed sound prefix summaries, exhibit two budget-critical reachable states at the same prefix depth with identical summary but different forced extensions to a total order within budget k (or prove the quotient is necessarily exponential in n log n on an all-n reachable family).

## implication

A provably sound coarser bisimulation would give a uniform route to 2^(O(n log n)) exact evaluation without relying on heuristic pruning; a general obstruction would formalize the 'interface summary' barrier beyond the isomorphism-identity counting already noted in board #301.

## finding_unverified

Let us look at the current research frontiers and related docs.

Let us look at budgeted DFS implementation and research notes more.

Let us understand the exact game structure better and look up related work. Also look at the board digest more if possible - the user says "current board #301" but the digest I ran only showed recent posts. Maybe let us look up the actual board content differently? Or perhaps the "ant-ice-time-exponent" post is mentioned as context. Let us look up the full research-time-exponent more - it says "isomorphism-fine keys give 2^(Theta(n log^2 n)) state count obstruction for that family" - maybe in the context of memoizing by isomorphism classes in the DFS with certain pruning? Also look up how the DFS behaves.

Alternatively, look up scripts/evaluate.py to understand the memoized version.

Let us start by exploring the codebase more to understand the full picture of states and memoization.

Let us think carefully about this. The user wants to attack this front on billy-dev. Let us understand the full picture of the game/state.

Let us write up the findings.

Reported the mathematical finding with the falsifier obstruction using the winning frontier construction. The answer distinguishes value-soundness from bisimulation/congruence in the AND-OR game and shows why coarser summaries fail. No repo/Lean changes.

## Other metadata

```json
{
  "finished_at": 1793717036.9067736,
  "started_at": 1793715480.1873784
}
```
