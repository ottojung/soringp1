# winning-frontier-peak-at-exact-budget-alln

## status

blocked

## origin

ai_proposal_unverified

## agent_id

qfKTh4Jrm6ftE3CZUEDUjl-juice

## exit_state

failed

## question

For n and t <= S(n), let W_t(n) be the number of nonisomorphic reachable posets P at depth t that satisfy F(P) <= S(n)-t (winning at remaining budget). Is the maximum over t of W_t(n) always attained at t = S(n) (the exact-budget frontier), or does there exist an infinite family of n where the winning frontier peaks at depth strictly below S(n)?

## basis

Board #301: winning-frontier-sparsity-threshold, space-reduction-budgeted-dfs, exact-evaluator-time-exponent; research-winning-frontier-barrier.md (barrier extends to exact optimal budget via Sergeev o(n) surplus).

## falsifier

Exhibit n_i where max_t W_t(n_i) is attained at some t_i < S(n_i) by a margin (e.g. W_{S(n_i)-1}/W_{t_i} < 1/2 for arbitrarily large n_i), or prove W_{S(n)} >= max_t W_t for all sufficiently large n.

## implication

If the frontier peaks at the exact budget, exact-budget certificates are load-bearing for the winning-frontier barriers; an earlier-peak family would suggest exact-budget state counts are surplus to earlier-depth counts and might allow search strategies optimizing lower depths first.

## finding_unverified

I'll start by checking the environment (hostname for billy-dev) and reading the key docs.
On billy-dev confirmed. Now let me look at the docs directory, find the board and the winning-frontier barrier notes.
Now reading the operations doc (board #301), the winning-frontier barrier doc, literature, and the frontier state.

## Other metadata

```json
{
  "finished_at": 1795311271.8220806,
  "started_at": 1795310902.3690665
}
```
