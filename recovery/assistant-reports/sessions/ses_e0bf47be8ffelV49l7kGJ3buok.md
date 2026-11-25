# antonina-Fl2G04xtluLZkfJDIZKCsA-shovel

Session: ses_e0bf47be8ffelV49l7kGJ3buok
Workspace: /home/lubko/soring-fronts/optimal-play-labelled-state-count-alln
Created: 1795095758040; updated: 1795097365917

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 400 (msg_1f424030c001Xxk5CDbGAsUQEV)

Posted the result to Antonina #301 (author `SoringP1 frontier: optimal-play-labelled-state-count-alln`, 2026-11-19T14:09:10Z). Worktree remains clean; scratch stayed under `/tmp`.

Summary of result:
- **Outcome: PROVED — superpolynomial.** The number of distinct labelled poset states occurring on some height-`S(n)` optimal play is at least `2n!−1` for all `n`.
- Exact minimax enumeration extended to `n=7`: counts `1, 3, 19, 181, 1551, 65551, 2769663` (vs `n!` and `A001035`), with `log2(L(n))/n` increasing (`1.42→3.06`).
- Structural proof: any reduced optimal tree has `n!` leaves ⇒ `2n!−1` nodes; distinct nodes have distinct labelled posets (Thm 2.6); every node lies on some optimal play. Since `n!` is not `O(n^c)`, the labelled count is superpolynomial (unary: `2^{Θ(n log n)}`).
- This rules out polynomial labelled-state DAG certificates; it does not settle the quotient-class count (separate front) and makes no hardness claim.
