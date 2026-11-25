# antonina-0HeA5oe22Tre6ls2DidKLk-dare

Session: ses_df9dca7a2ffeYQdz2mFXJF4yHM
Workspace: /home/lubko/soring-fronts/poly-reachable-exact-height-gap-alln
Created: 1795399310039; updated: 1795399610895

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 192 (msg_20627dc06001InZWaXUDBzBTT6)

Posted a single result comment to Antonina issue #301 (front slug `poly-reachable-exact-height-gap-alln`). Verdict: **second horn** — for all sufficiently large n, every height-`S(n)` decision tree from the n-antichain has at least `2^{(1/2-o(1)) n log_2 n}` distinct reachable poset states, so no polynomial-reachable optimal tree exists for large n (`G(n)>S(n)` eventually). The counting proof uses `t=floor(log_2(n!)/2)`, the fact that all linear extensions of a depth-t poset follow the same path (so each distinct poset accounts for `e(P)` permutations with `e(P)≤2^{S(n)-t}`), and Sergeev's `S(n)=log_2(n!)+O(n/(log n)^{1/5})`. Worktree remains clean; no repo, Lean, test, CI, or ledger changes.
