# antonina-Gyry0AZar3W7GDofv2uzvg-niece

Session: ses_e073ff09affewVBsbi3sMkY2Qo
Workspace: /home/lubko/soring-fronts/exec-sortbound-linear-space-20261120
Created: 1795174698890; updated: 1795174747882

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 89 (msg_1f8c09d66001wxReBisyNnSGSP)

**Result for #301: precise blocker, not an unconditional lower bound.**

For `SORT-BOUND-U`, with read-only input and `N=n+k+1`, the transcript DFS uses `O(k log(n+2))` bits for its path and per-frame search cursors. Its reachability workspace is `O(n log n)` bits with BFS. Replacing BFS with Savitch-style directed reachability can reduce that workspace to `O(log² n)` bits, with extra time still absorbable by the finite exponential DFS bound. But it leaves the path and cursor stack at `O(k log n)` bits. The resulting accounting is still `O(N log N)`, not `O(N)`.

The obstruction is specific to this compression route: a literal transcript of `t` comparisons uses Θ(`t log n`) bits, and the depth-first control stack also needs a candidate cursor at each active level. Removing the reachability workspace therefore does not remove the dominant stack cost when `k` is large. This rules out only the proposed “Savitch reachability + stored transcript DFS” route; it does **not** establish a space lower bound for `SORT-BOUND-U` or rule out a different algorithm.

This is the unary **threshold** problem, where the supplied budget is `k`. It does not establish an `O(n)`-space algorithm for computing numeric `S(n)` on input `1^n`, where evaluating thresholds may use budgets up to `U(n)=O(n log n)`.

I could not post to Antonina #301: the available `gh` command does not support `gh issue view`, and no board-posting command was available. No code, Lean, or repository files were changed.
