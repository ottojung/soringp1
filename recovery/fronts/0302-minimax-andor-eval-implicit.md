# minimax-andor-eval-implicit

## status

investigated

## origin

ai_proposal_unverified

## agent_id

TuqILGiWSE2O4K6Q6i8ZMP-backs

## exit_state

clearexit

## question

For the implicit AND-OR tree defined by the comparison game on n! leaves (sorter ORs, adversary ANDs), is there an all-n uniform obstruction to evaluating its minimax height faster than the best known uniform evaluators without exploiting the total-order/permutation symmetry structure, treating the tree as given only by the minimax recurrence?

## basis

Minimax is AND-OR over comparisons; AGENTS.md forbids super-polynomial lower bounds but allows barriers to whole families of methods and structural theorems about the minimax game.

## falsifier

Give a uniform algorithm that evaluates the implicit comparison-game AND-OR tree height for all large n in time sub-exponential in the description of the state graph (better than 2^(O(n log^2 n))) using only generic AND-OR evaluation (no sorting-specific combinatorial pruning by linear extensions beyond the recurrence).

## implication

Would distinguish generic AND-OR tree complexity from structure-exploiting combinatorics of sorting, informing whether upper bounds reflect the model or avoidable recurrence overhead.

## finding_unverified

if n is the input size, that's exponential in n log^2 n, so not sub-exponential. That would mean current best is exponential in n (times logs), and they want to do better than that, sub-exponentially in the description size. Also the description of the recurrence is polynomial in n.
Let us think about the question again carefully.
The question says: "evaluate its minimax height faster than the best known uniform evaluators without exploiting the total-order/permutation symmetry structure, treating the tree as given only by the minimax recurrence?"
The best known uniform evaluator gives 2^(O(n log^2 n)). The budgeted DFS achieves this - it's uniform, treats states as posets (given by recurrence), does pruning but no memoization across different (P,d) in a big table? It does have a counter but not memoization of results. The transcript DFS also no memo. The memoized version over all states gives worse asymptotics (2^(Θ(n^2))). The symmetry-quotient (state_compression) exploits symmetry (relabelling) - that's "exploiting the total-order/permutation symmetry structure" which the falsifier says NOT to do. So symmetry-quotient is excluded. Generic AND-OR evaluation on the recurrence - alpha-beta style pruning, maybe transposition tables (memoization) over (state,d)? But memoizing over all reachable (P,d) might be expensive; also is that "generic" or does it use symmetry? Memoization just caches results of same subproblem - that's generic. The budgeted DFS without memoization is already doing 2^(O(n log^2 n)). Can we do better by adding memoization in some smart way (not exploiting symmetry, just caching identical poset states reached again at same or larger budget)? Because different move orders can lead to same poset state. The budgeted DFS doesn't memoize - so it recomputes. Adding memoization would be a generic improvement.
Let us test. I tried earlier with memo key (succ,d) and got worse results? Let us look up what I did. In test_memo_dfs2.py, for each query (mid in binary search) I create a fresh memo dict and call can_sort_memo - so memoization is only within that single threshold test, not across binary search calls. Also key includes (succ,d). That seems reasonable for AND-OR with fixed depth budget? Or the recurrence is F(P,d). Memoizing across the whole computation (and possibly sharing across binary search) might help. Let us check.

Let us start by researching this specific question thoroughly.

I studied AGENTS.md/docs/problem.md, reviewed the minimax recurrence and existing evaluators. Attempted to construct the falsifier: a uniform generic AND-OR evaluator (iterative deepening + transposition tables over poset states, alpha-beta-style pruning, move ordering, killer moves) using only the recurrence, without global S_n symmetry or linear-extension pruning. Benchmarks show large practical gains over naive DFS but still exponential in n log^2 n (n=6: ~194k calls); full DAG DP visits all D_n states (worse asymptotically). The winning-frontier barrier excludes only algorithms that enumerate the full frontier (selective search not excluded), but pruning experiments show linear-extension pruning gives massive speedups (forbidden here) and do not reduce the exponent even when allowed. I could not produce a sub-exponential-in-n (description) algorithm; this is a failed attempt at the falsifier, not a proof of obstruction. No repo/Lean changes made; distinctions between general-poset results and certificate soundness/completeness noted.


## Other metadata

```json
{
  "finished_at": 1793856758.3615546,
  "started_at": 1793848575.8823836
}
```
