# antonina-RDwpQXKKC5FR0kb8lIon4A-missouri

Session: ses_e1896eea3ffeIii2cu5xk1Mn53
Workspace: /home/lubko/soring301-exec-entropy-balance-conditional-necessity-20261117
Created: 1794883785192; updated: 1794884412052

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 284 (msg_1e77297bf001ZeTjWhGLwDja5u)

Completed. Wrote `exec-report.md` in the worktree and posted one non-duplicate summary to Antonina #301.

Key result: the average-case entropy balance cannot be turned into a sound deterministic worst-case pruning/move rule using only aggregate locally computable potentials. Exhaustive `n≤5` enumeration found 60 posets where the greedy extension-count-balanced comparison is non-optimal and 164 where the one-ply L1-minimizing comparison is non-optimal. Smallest witness `W=(0,0,9,0,3)` has `e(W)=16`, `F(W)=4`; comparisons `{1,3}` and `{2,4}` both split `8/8` (ratio `1/2`, entropy `1.0`, L0-max `3`), but `{1,3}` costs `5` while `{2,4}` costs `4`. Since aggregate splits are identical, no threshold on ratio/entropy/L0-max can separate them; the difference is structural. Independent checks (brute-force `e`, separate recursive `F`, transitive-closure validation) agree. No Lean, repository code, or PR changes were made.
