# optimal-play-balanced-comparison-existence

## status

investigated

## origin

ai_proposal_unverified

## agent_id

MoGnFiMoDG1X5Gnn1MkQSh-average

## exit_state

clearexit

## question

For every n >= 1 and every poset state P reachable from the n-element antichain along some comparison strategy of minimax height S(n), does there exist an optimal next comparison pair {x,y} with min(e(P+x<y), e(P+y<x)) / e(P) >= 3/11 (a Kahn-Saks-balanced move that is also minimax-optimal)?

## basis

Kahn-Saks 1984 gives a 3/11-balanced comparison in every poset; S(n)=F(empty)=adv(univ) (Minimax.lean A24). Independent exhaustive check over all optimal-play states for n<=5 (1,3,19,181,1551 states) found every state admits a >=3/11-balanced optimal move (root moves are 1/2-splits).

## falsifier

Exhibit some n and an optimal-reachable state P from the n-antichain such that every incomparable pair {x,y} satisfying min(e(P+x<y), e(P+y<x)) / e(P) >= 3/11 has 1 + max(F(P+x<y), F(P+y<x)) > F(P).

## implication

A positive all-n answer would show optimal root strategies can be confined to Kahn-Saks-balanced moves, yielding a structural pruning/normal-form constraint on minimax play relevant to exact evaluators and to succinct strategy descriptions; a refutation would separate extension-balance heuristics from exact optimality on antichain-root states.

## finding_unverified

i) >= ceil(log2 e(P_i))` (information lower bound). A 3/11-balanced pair keeps `max(e(P+x<y),e(P+y<x)) <= (8/11)e(P)`, so its child information lower bounds are, if anything, *favored* relative to a highly unbalanced split (which can force one child to retain most extensions). Meanwhile `F(P)=1+min_{x‖y} max(F(P+x<y),F(P+y<x))` depends on exact minimax values of both children, not just extension counts. This yields no separation in either direction and no all-`n` counterexample construction: Kahn–Saks prevents an "all-balanced-pairs make one child total" shortcut once `e(P)` is nontrivial, but does not control `F` tightly enough to force a non-optimal balanced move.

### 2) Computational falsification attempt (experiment, discriminating)
Exhaustive check in `/tmp` (Python; exact `F` by minimax DP over all reachable labelled posets, linear-extension counts by subset DP, union over **all** optimal moves at each reached state = every state reachable along *some* height-`S(n)` strategy):

| n | `S(n)` | all reachable posets | optimal-reachable states | non-total checked | states where no 3/11-balanced move is minimax-optimal |
|---|---:|---:|---:|---:|---:|
| 5 | 7 | 4231 | 1551 | 1431 | 0 |
| 6 | 10 | 130023 | 65551 | 64831 | 0 |

`n<=5` reproduces the stated evidence (1551 states). `n=6` extends it to the full optimal-reachable union and finds **no counterexample** (no state where every pair with `min(e(P+x<y),e(P+y<x))/e(P) >= 3/11` has `1+max(F(P+x<y),F(P+y<x)) > F(P)`).

## Mathematical finding / status
- **Finding (negative/inconclusive on the front):** I found **no falsifier** and **no proof**. The all-`n` claim remains **open**.
- **What was seriously tried:** primary-source/model separation (Kahn–Saks balance existence is not minimax-optimality completeness), an information-lower-bound sanity check for a forced separation (inconclusive, leans against an easy disproof), and an exhaustive optimal-reachable-state search extended to `n=6` (65551 states, 0 counterexamples). No structural theorem was obtained that would imply all-`n` truth.
- **Concrete obstruction / honest limits:** A proof would need a global invariant linking extension-balance (Kahn–Saks 3/11 split) to the exact minimax value `F` along *every* optimal-reachable antichain-root state for all `n`; I do not have such an invariant. A disproof would require an explicit optimal-reachable state (hence an explicit height-`S(n)` witnessing path) whose every 3/11-balanced split is minimax-suboptimal; exhaustive search found none for `n<=6`, but this is finite evidence only. I did **not** verify the union-of-all-optimal-strategies reachability against a stronger "reachable on some fixed optimal policy under adversarial optimal replies" refinement beyond the standard `1+max(F(child1),F(child2))==F(P)` optimal-move characterization used here, though this is the natural minimax-DAG notion consistent with the prompt. No independently checkable new all-`n` theorem/counterexample emerged, so no Lean/repository changes are warranted.

**Complexity implication (conditional, as stated):** a positive all-`n` answer would be a structural pruning/normal-form constraint confining optimal root strategies to Kahn–Saks-balanced moves (relevant to exact evaluators/succinct strategy descriptions) but would **not** by itself yield a complexity-class separation for unary `S(n)`; a refutation would separate extension-balance heuristics from exact antichain-root optimality. Current status: unresolved.

## Other metadata

```json
{
  "finished_at": 1794564690.1426225,
  "started_at": 1794555475.5439756
}
```
