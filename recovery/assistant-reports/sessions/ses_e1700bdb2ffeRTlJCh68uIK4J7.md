# antonina-FJ0DjTykqd4m123hvokfHb-dutch

Session: ses_e1700bdb2ffeRTlJCh68uIK4J7
Workspace: /home/lubko/soring301-exec-ms-dag-n4-20261117
Created: 1794910405260; updated: 1794910532498

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 89 (msg_1e9010605001LfY6besLdoDh8y)

## Deliverables
- **Report:** [`exec-report.md`](exec-report.md) — construction basis (per §2 merge schedule/`(a,b)` states/explicit slot permutations), methods/commands, witness stats, checker result, confirmation (no obstruction), and next step.
- **Witness artifact:** [`artifacts/merge-sort-framed-dag-n4.json`](artifacts/merge-sort-framed-dag-n4.json) — explicit permutation-framed merge-sort strategy DAG for `n=4` (topologically numbered, forward edges).

## Construction (per docs/research-framed-certificate-frontier.md §2)
- Binary merge schedule: `(1,1)` + `(1,1)` + `(2,2)` merges (comparison-state count `pq`: `1+1+4=6`; path depth `1+1+3=5 = S(4)`).
- Pair merges: compare heads; `lt` identity, `gt` explicit swap permutation; sequential composition into next query.
- Top merge states `(a,b)` with prefix `t=4-a-b`: compare left head `t` vs right head `t+a`; `lt` identity → `(a-1,b)`; `gt` explicit rotation permutation (winner moved to prefix) → `(a,b-1)`; empty queue appends as terminals. States identified by `(a,b)` (path-independent prefix/remainder slot invariant), with shared child `(1,1)` as a DAG join.

## Methods / commands
1. Programmatic construction of the framed DAG from the merge schedule and `(a,b)` recurrence with explicit permutations, followed by topological renumbering of reachable nodes (checker forward-edge requirement).
2. Saved witness: `artifacts/merge-sort-framed-dag-n4.json`
3. Verification:
   - `python3 scripts/check_framed_strategy.py artifacts/merge-sort-framed-dag-n4.json`

## Witness stats and checker result
- `n=4`, `budget=5`
- DAG: `10` nodes total (`6` comparison/query, `4` leaf), `12` directed edges; merge states `(2,2),(1,2),(2,1),(1,1)` + 4 terminal completions
- Longest path depth: `5`
- Checker: `ACCEPT: n=4, depth=5, nodes=10`

## Outcome
**Confirmed (no obstruction):** sound explicit permutation-framed merge-sort DAG certificate for `n=4` at exact budget `S(4)=5`, accepted by `scripts/check_framed_strategy.py`. Instance-level confirmation only; §2 all-`n` construction remains independently pending audit and does not imply exact optimality/all-`n` completeness. Next step: generalize the `(a,b)` generator to balanced schedules for larger `n` and audit against the checker.
