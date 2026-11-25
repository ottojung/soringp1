# antonina-VIZCByJ0i5MpHqxy4aXCHe-disfavor

Session: ses_e49b50288ffe70XfAaRT427Ki1
Workspace: /home/lubko/soring-fronts/exec-sorting-pns-transposition-20261107
Created: 1794059730354; updated: 1794059941064

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b64aff960019raIyeVEl3Jj9C)

I’ll first inspect the local recurrence/evaluator and the prior PNS artifact, then implement and test only an untracked experiment in this worktree. I’ll keep the search capped and treat any cap hit as UNKNOWN.

## Output 31 (msg_1b64b1423001Xwq63U1UGnxtge)

The key correctness issue is budgeted transpositions: a poset reached with different remaining budgets is not the same game node, so the exact table key must include `d`. I’ll use canonical closed posets plus budget; solve propagation will be monotone three-valued AND/OR logic, while proof/disproof numbers only choose what to expand.

## Output 146 (msg_1b64d62600015b0RQ37cuei5Tz)

All four threshold outcomes now match `evaluate.py`, including the previously cap-limited `n=5,d=7` case. A caveat in the first measurements: process-wide peak RSS was contaminated by the earlier high-memory run, so I’m rerunning comparisons in fresh processes and checking the prior artifact’s exact tree counts under the same caps.

## Output 169 (msg_1b64e0ccb0012XhB7dIOOaKAS4)

Implemented `scripts/billy_pns_transposition.py` as an **untracked experiment**. It models CanSort with sorter choices as OR nodes and adversary answers as AND nodes; refutation uses the exact dual. Its table shares nodes by canonical closed poset and remaining budget (plus node kind and comparison for AND nodes). Solved results propagate over all parents; proof/disproof numbers only guide expansion. Any cap hit returns UNKNOWN.

All requested thresholds matched `scripts/evaluate.py`: n=4,d=4 DISPROVED; n=4,d=5 PROVED; n=5,d=6 DISPROVED; n=5,d=7 PROVED. The local budgeted DFS regression also passed.

At equal caps (1,000,000 expansions / 2,000,000 edges; wall limit 120s), the transposition search used:
- n=4,d=4: 66 distinct nodes, 113 edges, 89 canonicalization calls, 0.008s.
- n=4,d=5: 79 nodes, 135 edges, 107 calls, 0.010s.
- n=5,d=6: 520 nodes, 1,093 edges, 797 calls, 0.289s.
- n=5,d=7: 631 nodes, 1,329 edges, 979 calls, 0.390s.

The ordinary prior PNS tree used 2,504 expansions / 3,581 generated nodes at n=4,d=4, and 780,819 / 1,358,403 at n=5,d=7 (26.56s). This is a substantial finite reduction in search work versus that PNS tree; it is **not** an asymptotic claim. Accounting caveat: transposition counts include both OR and AND nodes, while prior PNS’s `expanded` counts expanded nodes and its `generated` counts tree nodes; DFS calls count entered positions only. Reported RSS was unreliable after a prior high-memory run contaminated process peak measurements, so no memory comparison is claimed.

The only worktree change is the untracked script. No Lean, CI, n≥6 run, commit, or board post.
