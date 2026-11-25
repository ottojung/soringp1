# antonina-OdOmwA3qUDKwzVwaFxA7lF-planks

Session: ses_e17d9d0acffebaCFt4y47UCbgl
Workspace: /home/lubko/soring301-exec-d3-smalln-20261117
Created: 1794896179137; updated: 1794897006847

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 194 (msg_1e8326a67001p8EevPrnhBNP15)

Inspected state before acting (recovery): worktree `/home/lubko/soring301-exec-d3-smalln-20261117` at HEAD 6a96398 was clean (`git status --short` empty), no pre-existing `./exec-report.md`. Read `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-winning-frontier-barrier.md`, `docs/operations.md`, and prior report `/home/lubko/soring301-exec-d-quotient-20261117/exec-report.md` (conceptual only; no small-`n` optimal-strategy quotient enumeration). Board duplicate check: `python3 /home/lubko/soring301/scripts/board_digest.py --contains "optimal-quotient-states-smalln-enum"` → no matches on page 1. No commits/PRs/Lean/tests or other external side effects performed; **no `#301` post made** (no confirmed interrupted duplicate found, and results are empirical small-`n` guidance, not a theorem-level/uniform new finding).

**Recorded work:** `./exec-report.md` (full methods, commands, results, interpretation, feasibility limits, falsifier discussion).

## Computation performed (n<=5)
- Baseline: `python3 scripts/strategy_dag_probe.py --max-n 5` (completed; logged to `/tmp/opencode/dag5.txt`). Inspected relevant scripts (`generate_optimal_tree.py`, `strategy_dag_probe.py`, `state_compression.py`, `benchmark_symmetry_quotients.py`). Py-compiled probe scripts successfully.
- Custom exact/heuristic enumeration in `/tmp/opencode/` (not in repo): `min_states.py`, `d3.py`, `exact_d3.py`, `exact_n3.py`, plus debug/canon checks. Found `strategy_dag_probe.py`’s `quotient_dag_nodes` can undercount isomorphism classes appearing in a strategy due to canon-dedup traversal pruning (e.g. n=3 first policy: actual 5 classes, probe reported 4); labelled DAG/union counts matched recomputation. Corrected d2 computed as `|{canon(s): s in strategy states}|`.

**Model/definitions:** successor-bitmask poset states, `F(P)` minimax / `S(n)=F(antichain)`, `S(1..5)=0,1,3,5,7`. d1 = distinct labelled poset node labels; d2 = distinct unlabelled isomorphism classes; node occurrences = `2*n!-1`; leaves = `n!`. d3 optimized over optimal **state-policies** (same poset→same optimal move), with caveat noted.

## Results (small n)

Corrected distinct states / union (n<=5):

| n | S(n) | occurrences `2*n!-1` | leaves `n!` | d1 (one first-choice policy) | d2 (same policy) | d1 union (all optimal strategies) | d2 union | leaf quotient classes | multi-choice optimal states | max choices |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| 2 | 1 | 3 | 2 | 3 | 2 | 3 | 2 | 1 | 0 | 1 |
| 3 | 3 | 11 | 6 | 11 | 5 | 19 | 5 | 1 | 7 | 3 |
| 4 | 5 | 47 | 24 | 47 | 8 | 181 | 12 | 1 | 73 | 6 |
| 5 | 7 | 239 | 120 | 239 | 19 | 1551 | 19 | 1 | 591 | 10 |

d3 (minimum over optimal strategies/state-policies):

| n | d3_l = min d1 | d3_u = min d2 | max d2 observed | method |
|---|---:|---:|---:|---|
| 1 | 1 | 1 | 1 | unique |
| 2 | 3 | 2 | 2 | unique |
| 3 | **11 (exact)** | **4 (exact)** | 5 (exact) | exhaustive, 192 optimal state-policies |
| 4 | 47 (best found; all sampled) | **≤ 7** (best found) | ≥ 8 (sampled) | first/last/random-200 policies; best (47,7) |
| 5 | 239 (best found; all sampled) | **≤ 14** (best found) | ≥ 19 (sampled) | first/last/random-50 policies; best (239,14) |

## Patterns / falsifier guidance (empirical, not all-n proofs)
- **Occurrences vs distinct states:** corrected; all total-order leaves collapse to 1 unlabelled class in every case.
- **Labelled reuse:** no labelled poset state repeated in any sampled optimal state-policy for n<=5, and none in any of the 192 policies for n=3 (d1 == `2*n!-1` throughout). Suggests `d3_l = 2*n!-1` may hold broadly for state-policies, but **not proved for all n**.
- **Unlabelled quotient (d2/d3_u):** much smaller than leaves/occurrences but grows (union 1,2,5,12,19; best-found minima 1,2,4,≤7,≤14). No evidence of bounded/very-small optimal quotient families (against “small quotient possible” in strong form); also no evidence forcing quotient near `n!`.
- **All-n context:** deduction already gives `d3_u <= d3_l <= 2*n!-1 = 2^{Θ(n log n)}`, so a super-`2^{Θ(n log n)}` lower bound on d3 is impossible (consistent with winning-frontier barrier: many global nonisomorphic winning states cannot all appear on one optimal strategy). Data show d3_u far below this trivial cap for n<=5.

## Feasibility limits
- n<=5 tractable in-memory with bitmask-poset minimax/union enumeration in this environment.
- Exact d3 over state-policies exhaustive for n=3; infeasible by brute force for n=4,5 (73/591 multi-choice states, up to 6/10 choices) — reported achieved upper bounds/sampling only.
- n=6 (`S(6)=10`, 720 leaves) not attempted; tight d3/union feasibility uncertain here. No history-dependent (non-state-uniform) tree enumeration attempted.

All evidence and claims are labeled in `exec-report.md` (definition/deduction/experiment); no primary-source or kernel-checked theorem claims added.
