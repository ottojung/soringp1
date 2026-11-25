# antonina-4c5b5jCNF2MMFtrO7JurnX-peoples

Session: ses_e07100c1dffeLAyAYIFKl2bGqC
Workspace: /home/lubko/soring-fronts/exec-linear-space-20261120
Created: 1795177837633; updated: 1795177898208

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f8eff5e7001RleFMccT5gz6aV)

I’ll first inspect the current contract, the targeted research notes, and the #301 history so the investigation starts from the actual open frontier rather than revisiting prior checkpoint or recomputation attempts.

## Output 117 (msg_1f8f09092001t8HYfY2yD9Wj2G)

The prior #301 finding already isolates the main issue: Savitch-style reachability can shrink the temporary graph-search workspace, but not the explicit comparison-history/control stack. I’m checking the older transcript/recomputation notes and the exact input-length edge cases now; the remaining useful question is whether a distinct representation or evaluation order avoids that stack, not whether its current accounting is a lower bound.

## Output 136 (msg_1f8f0abbd001rB8G0Ffr5SYt07)

## Outcome: no O(N)-space algorithm found; the explicit-DFS obstacle is route-specific

**Model and encoding.** The target is the unary decision language `SORT-BOUND-U = {1^n # 1^k : S(n) ≤ k}`, with `N = n+k+1`. `S(n)` is the minimum worst-case height of a deterministic adaptive pairwise-comparison tree on distinct labelled keys. The minimax game in `docs/research-budgeted-dfs.md` preserves that semantics: the sorter chooses a currently incomparable pair, both adversary answers must succeed, and comparisons update the partial order by transitive closure.

**Evidence from the existing work and #301.** The current contract and notes establish a uniform transcript DFS using `O((n+k) log(n+2)) = O(N log N)` work bits for the threshold input. Its explicit path stores up to `k` comparisons, and its per-level search cursors also take `O(k log n)` bits. The 2026-11-20 #301 linear-space result observes that Savitch-style reachability can reduce the *separate* reachability workspace, but does not remove this path/control stack. Earlier transcript/backtracking analyses likewise recompute comparability after returning from a child, but retain the path needed to define the current state. **This identifies a limitation of these implementations, not an algorithmic lower bound.**

**Precise missing lemma / next step.** To improve this route to `O(N)` bits, one needs either:
- a representation of the current game state and branch progress using `O(N)` bits while retaining exact, adaptive minimax evaluation; or
- a recomputation/evaluation scheme that reconstructs the needed path or state in `O(N)` space, with its time cost explicitly bounded.

A falsifiable next step is to give such a representation or reconstruction procedure for arbitrary depth-`k` DFS nodes, prove its space bound independently of the reachability subroutine, and check that it preserves both the existential pair choice and universal two-answer condition. Merely replacing BFS with Savitch reachability does not discharge this obligation.

**Model sanity check.** The notes’ known values are `S(1)=0`, `S(2)=1`, `S(3)=3`, `S(4)=5`, `S(5)=7`, and `S(12)=30`; at `n=12`, the information bound is 29. The recurrence’s terminal-total-order and exhausted-budget cases agree with the threshold question. The trivial acceptance when `k` reaches a sorting upper bound handles large budgets without changing the input-length measure.

**Consequence.** There is no publication-gated algorithm or impossibility result here. An `O(N)`-space algorithm would improve the uniform resource bound for `SORT-BOUND-U`, already known to be in PSPACE; the present transcript-stack accounting proves neither that such an algorithm exists nor that it is impossible. No repository or Lean changes were made. I could read the prior #301 result, but did not post a new board update.
