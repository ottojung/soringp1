# selective-frontier-visit-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

COWEW5v4kh0pZW53U0MPEy-march

## exit_state

clearexit

## question

For infinitely many n from the rectangular-chain family, does every correct uniform algorithm that computes S(n) by adaptive minimax search over reachable poset states visit Omega(2^((1/4-o(1)) n (log n)^2)) distinct nonisomorphic reachable states at or before the exact budget level S(n), regardless of pruning heuristics?

## basis

Winning frontier barrier (Sergeev surplus) shows 2^Omega(n(log n)^2) winning states coexist at exact budget S(n); distinguish enumeration from selective search and test visit-complexity.

## falsifier

Exhibit a selective search strategy (with correctness proof) that computes S(n) for all large n in the family while visiting o(2^((1/4-o(1)) n (log n)^2)) states total, or prove that the adversarial distribution forces visiting that many.

## implication

A yes would rule out subexponential-in-n(log n)^2 uniform exact evaluation by selective search (strengthening the enumeration barrier beyond 'must enumerate'); a no would open a path to better exponents for S_unary.

## finding_unverified

y can force visit count to >= frontier regardless of pruning heuristics. Only post to `#301` if obtaining a concrete failed approach/exact obstruction or a checkable counterexample/theorem.

## Relevant Files
- `/home/lubko/soring-fronts/selective-frontier-visit-obstruction/docs/research-winning-frontier-barrier.md` – rectangular-chain construction, counts, "enumeration barrier only", not excluding selective minimax/proof-number
- `/home/lubko/soring-fronts/selective-frontier-visit-obstruction/docs/research-budgeted-dfs.md` – G(n,k), CanSort minimax, pure DFS no memoization
- `/home/lubko/soring-fronts/selective-frontier-visit-obstruction/scripts/budgeted_dfs.py` – reference minimax DFS (call counter)
- `/home/lubko/soring-fronts/selective-frontier-visit-obstruction/scripts/budgeted_pruning_experiments.py` – pruning experiments/context
- `/home/lubko/soring-fronts/selective-frontier-visit-obstruction/scripts/evaluate.py` – minimax reference
- `/home/lubko/soring-fronts/selective-frontier-visit-obstruction/tests/test_winning_frontier_barrier.py` – exact counts
- `/home/lubko/.local/state/soringp1/frontier-ledger.json` – `selective-frontier-visit-obstruction` entry
- `/home/lubko/soring-fronts/selective-frontier-visit-obstruction/docs/problem.md`, `AGENTS.md`, `docs/operations.md` – model/scope
- `/home/lubko/soring301/scripts/board_digest.py` – Antonina issue `#301`
Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
Let me look at the worktree and recent state.

## Worktree: selective-frontier-visit-obstruction (branch main)
- Front (ledger): `selective-frontier-visit-obstruction` (agent `COWEW5v4kh0pZW53U0MPEy-march`, running). 
- Question: For infinitely many n in rectangular-chain family, does every correct uniform algorithm doing adaptive minimax search over reachable poset states visit Ω(2^((1/4-o(1)) n (log n)^2)) distinct nonisomorphic reachable states at/before budget S(n), regardless of pruning heuristics?
- Falsifier: find a selective strategy (with proof) visiting o(...) states for all large n in family, OR prove adversary forces Ω(...).

## Done
- Read core docs: AGENTS.md, problem.md, operations.md, literature.md, winning-frontier-barrier, budgeted-dfs, budget-pruning, time-exponent, encoding-consequences. Also frontier-ledger, Antonina #301 context.
- Verified rectangular-chain construction matches tests: `tests/test_winning_frontier_barrier.py` passes (224 gives >2^39 nonisomorphic winning states at t=524, 256 even larger). Construction extends to k=S(n) since S(n)-C(n)=o(n).
- Understood pure DFS minimax in `scripts/budgeted_dfs.py` (no memo, OR over pairs, AND over adversary answers, counts calls). Budgeted DFS/time/space analysis known.
- Confirmed barrier says "enumeration barrier only" - not excluding selective minimax/search/proof-number/symbolic methods.

## Current state / next
- Need to clarify "visit" (distinct nonisomorphic reachable states visited during search), "adversarial distribution forces", and relation to minimax tree/AND-OR.
- Try to see if selective strategy (pair ordering/pruning/canonicalization) can avoid visiting most rectangular-chain frontier states while staying correct for all large n in family, or derive obstruction. 
- May probe with `budgeted_dfs.py`/`evaluate.py` on small n to trace visits vs frontier states.

No repo changes made yet (and policy says only for substantive new theorem/counterexample/barrier/certificate/fix). Clean worktree.


## Other metadata

```json
{
  "finished_at": 1793406856.8057232,
  "started_at": 1793396649.0575902
}
```
