# minimum-split-imbalance-root

## status

investigated

## origin

ai_proposal_unverified

## agent_id

thE4H76qqFFLX8XKhYmWH0-comparing

## exit_state

clearexit

## question

For the n-element antichain at root, let beta(n)=min_{optimal strategies T} max_{outcomes of first comparison} (max(F(T_lt),F(T_gt))/(F(T_root)-1)) be the worst-case relative imbalance of the best most balanced optimal first split; is there an all-n proof that beta(n) -> 1 as n->infty or is inf_n beta(n) < 1 bounded away from 1?

## basis

Root minimax is central (S_eq_adv_univ), 1/3-2/3 conjecture is open in general, and prior small-n experiments showed forced boundary splits at some n but not universality - a clean all-n asymptotic question distinct from finite cases.

## falsifier

Prove inf_n beta(n) < 1 by constructing an all-n family of optimal strategies with some epsilon>0 separating balanced branches from the worst branch ratio for all large n, or disprove by showing every optimal strategy is asymptotically perfectly balanced (beta(n)->1) with a structural minimax argument.

## implication

A universal asymptotic balance would constrain adversarial strategies and might inform entropy-based pruning arguments; persistent imbalance in all optimal strategies would be a structural property that could affect certificate compression or the information-excess analysis.

## finding_unverified

st` (with `--json` output redirected to a file as required by AGENTS.md) and finish honestly.

## Relevant Files
- `/home/lubko/soring-fronts/minimum-split-imbalance-root` — front worktree (branch main).
- `/home/lubko/soring301/` — canonical repo; read-only work here preferred.
- `/home/lubko/soring301/SoringP1/Minimax.lean` — Lean minimax evaluator (`adv`, `bestPair`, `minimaxTree`, `S_eq_adv_univ` at line ~357).
- `/home/lubko/soring301/docs/problem.md`, `/home/lubko/soring301/docs/operations.md` — binding model/ops docs.
- `/home/lubko/soring301/docs/research-structural-lower-bounds.md` — F(P) definition, e(P), info(P), merge factors.
- `/home/lubko/soring301/scripts/one_ply_obstruction.py` — helper utilities (`add_relation`, `linear_extensions`, `minimax`, `incomparable_pairs`, `all_posets`); used for numeric checks.
- `/home/lubko/soring301/scripts/strategy_dag_probe.py` — optimal-policy DAG experiments; `KNOWN` values and `minimax_values(n)` (viable up to n=6 tested).
- `/home/lubko/soring301/scripts/evaluate.py` — standalone `sorting_number(n)` for small n.
- `/home/lubko/soring-fronts/curator/docs/research-frontier.json` — source of the front statement.
- `/home/lubko/soring301/scripts/board_digest.py` — safe way to read Antonina board #301 (`--recent N`).
- `/home/lubko/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/bin/python3` — working python interpreter to use.
Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
No external side effects occurred: the worktree is clean (no commits by this agent), and the board shows only Executive posts — nothing from my interrupted turn was published. The interrupted step was just a long computation (n=8 trace), which is optional; the n≤7 data is sufficient for the report. Let me finish by posting the finding.
Report complete. Summary of what happened this session:

- **No duplicated side effects**: verified the worktree was clean and the board had no prior post from my interrupted turn; posted exactly **once** (id `sha256:CkICqv2lyLk7oZeM...`, 2026-11-02T19:12Z on issue #301).

**Substance of the report on the `minimum-split-imbalance-root` front:**

1. **Literal reading degenerate (proved/plainly):**
   - F = minimax cost: any antichain first move is cost-optimal, `F(child) = F(antichain_n) − 1`, so the ratio ≡ 1 for all n — verified numerically n ≤ 6. No separation beta < 1 possible at root.
   - F = e(P): antichain S_n symmetry forces every first split to (n!/2 − 1, n!/2), so `(n!/2)/(n!−1) → 1/2` — trivial, verified n ≤ 10.
2. **Only nontrivial reformulation tested** (max e-branch imbalance along cost-optimal root paths, adversarial worst branch, greedy most-balanced choice): full minimax traces for n = 5, 6, 7 show early depths ≈ 0.5 (n=7: 0.50010/0.50020/0.50040/0.50079), rising to ~0.6 at mid-depth and hitting 1.0 only at the final ply (fP=2, eP=4) — a near-total-order boundary artifact, not an all-n family. States with forced ratio 1 (e.g. n=5 poset `(30,24,8,0,8)`) exist but lie on no cost-optimal root path in these traces.
3. **Conclusion posted**: experiment-conjecture for n ≤ 7 (bounded away from 1 except final plies), no counterexample family, no proof; n ≥ 8 enumeration exceeds compute. Recommended the curator restate the front over cost-optimal-path worst e-imbalance on depths 0..S(n)−2 — nontrivial, all-n, immune to both degeneracies.

No repo changes, no Lean, no PR — per the publication gate nothing qualifies yet.

## Other metadata

```json
{
  "finished_at": 1793646761.9248757,
  "started_at": 1793628762.4456587
}
```
