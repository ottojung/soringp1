# winning-frontier-space-tradeoff

## status

blocked

## origin

executive_proposed

## agent_id

D6ELolckkxtWxfGttAzZ56-squatter

## exit_state

failed

## question

Can the 2^{Θ(n log^2 n)} state space of the known memoized poset-DP be compressed below 2^{Ω(n log n)} for exact S(n) by exploiting the winning-frontier sparsity (the 2^{(1/4-o(1))n log^2 n} winning states at depth barrier) without losing exactness, and does any such compression yield a better uniform space bound for unary SORT-BOUND-U in PSPACE?

## basis

Winning-frontier barrier in docs/research-winning-frontier-barrier.md shows enumerating winning states cannot beat DFS exponent by more than constant factor; PSPACE bound is known but space-tightening remains open.

## falsifier

Show the winning frontier is unavoidable for any exact recurrence preserving the minimax root (the sparsity is a lower bound on distinct states needed), or construct an exact method with smaller asymptotic state count demonstrably violating exactness on some case.

## implication

A verified compression below the known barrier would tighten space/descriptional complexity of exact evaluation even if time bounds remain open.

## finding_unverified

n PSPACE; report concrete obstruction or failed approach with exact details.

## Relevant Files
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/docs/research-winning-frontier-barrier.md` — barrier theorem, excluded enumeration, finite witnesses
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/docs/research-budgeted-dfs.md` — budgeted DFS (no memoization), 2^{O(n log^2 n)} bounds vs memoized DP
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/docs/research-decision-encoding.md` — DP/DFS/ATM comparisons
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/docs/research-certificates-barriers.md` — PSPACE/EXPSPACE, sparsity, DP state space
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/docs/research-state-compression.md` — S_n quotient exactness, 2^{Θ(n log n)} reduction
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/docs/research-time-exponent.md` — automorphism/orbit limits
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/docs/research-plan.md`, `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/docs/problem.md`, `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/AGENTS.md`, `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/docs/operations.md`
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/scripts/budgeted_dfs.py` — `can_sort` (no memoization), `memoized_F`
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/scripts/budgeted_pruning_experiments.py` — `memoized_F`, pruned DFS
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/scripts/evaluate.py` — full minimax with `@cache`
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/scripts/bidirectional_advice.py`, `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/scripts/upper_witness.py`
- `/home/lubko/soring-fronts/winning-frontier-space-tradeoff/tests/test_winning_frontier_barrier.py`
- `/home/lubko/.local/state/soringp1/frontier-ledger.json` — front entry (winning-frontier-space-tradeoff)
The previous request exceeded the provider's size limit due to large media attachments. The conversation was compacted and media files were removed from context. If the user was asking about attached images or files, explain that the attachments were too large to process and suggest they try again with smaller or fewer files.

Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
We've been working on the **winning-frontier-space-tradeoff** frontier (billy-dev), investigating whether the known memoized poset-DP state space (~2^(Θ(n log^2 n))) can be compressed below 2^(Ω(n log n)) without losing exactness for S(n)/SORT-BOUND-U. 

**Done:** Read core docs (AGENTS.md, problem.md, winning-frontier barrier, budgeted DFS), checked frontier ledger #301, ran `tests/test_winning_frontier_barrier.py` (4/4), and explored scripts (`budgeted_dfs.py`, `evaluate.py`, etc.). Confirmed the rectangular family yields ~2^((1/4-o(1))n log^2 n) nonisomorphic winning states at depth S(n). 

**Current blockers:** Ambiguity around "memoized poset-DP" (2^(Θ(n^2)) full poset vs budget-reachable) and whether compression is possible for recurrence-preserving minimax methods (barrier excludes enumerating all winning states, not selective search). 

**Next:** Disambiguate the target DP object, test the falsifier on rectangular states for distinguishability/compressibility, and assess implications for unary SORT-BOUND-U space.

## Other metadata

```json
{
  "finished_at": 1793526646.5486307,
  "started_at": 1793516995.6264944
}
```
