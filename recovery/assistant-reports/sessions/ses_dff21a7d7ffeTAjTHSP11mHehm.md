# antonina-cqGyk05W54OxfBsmDimlZi-searched

Session: ses_dff21a7d7ffeTAjTHSP11mHehm
Workspace: /home/lubko/soring-fronts/poly-reachable-exact-height-gap-alln
Created: 1795310901426; updated: 1795314270602

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 65 (msg_200e42d77001S7uRR7MHicyT9j)

I'm on `billy-dev` and have studied AGENTS.md, docs/problem.md, and the current board #301 digest plus the frontier ledger. Now let me study the primary literature details relevant to the claim, and pin down the model semantics in the Lean model.

## Output 93 (msg_200f1db15001t0P2uO41cZiOIA)

I'm on `billy-dev`. I've now pinned the model semantics from `Model.lean`: a tree sorts every input ranking (distinct rankings reach distinct leaves), and the game model `G(n,k)` from `research-budgeted-dfs.md` §0 is the state machine version ("the sorter wins iff a total order is reached"). The user's front asks about the reachable poset-DAG states of height-`S(n)` trees from the antichain.

Now let me run a small experiment: compute the minimax strategy DAG from the antichain for small n and count its reachable states.

## Output 111 (msg_201087a9b001dMrL5rphDYmZp7)

The script timed out on n=3 — something's wrong. Let me debug quickly.

## Output 131 (msg_201090bbb001aruEtN3BqSSpoV)

The `strat` walk works (n=3: S=3, |R_strategy|=11). The timeout was likely at n=7 (too many posets in the F DP). Let me run n=3..6.

## Output 142 (msg_2010a08c2001f0Mj3hVTbvn6yy)

The F DP works (n=3: S=3 ✓). The timeout was at n≥7 (the F DP explores the full minimax game tree; for n=6 it visited all 130,023 posets). I have data for n=3..6. Let me get n=2 as well and check if there's a board-posting CLI for the AGENTS.md deliverable.

## Output 180 (msg_2010ffd32001sTqK1M60czgPOR)

There's a `strategy_dag_probe.py` script in the repo — directly relevant to the front (measuring states on optimal plays). Let me check it.

## Output 198 (msg_201101ef5001tWoWIw0hYu0GFK)

The repo has `strategy_dag_probe.py` — the canonical tool for this front. Its data shows one-optimal-policy DAGs of 2n!−1 nodes (11, 47, 239 at n=3,4,5) and the union of all optimal strategies of 19, 181, 1551. Let me see the rest of the output.

## Output 218 (msg_20110c728001z3RlQNBPSBojor)

Now I have the data. Let me post a concise update to board #301 per `AGENTS.md` ("post only when something changed: a result, a falsification, or a precise obstacle").

## Output 236 (msg_201114eb6001eLkXsdXeDib5Wb)

The board update is posted to #301. Here is the completion report.

## Claim attacked (as posed by the FRONT, board #301)

> `G(n) = 0` for infinitely many `n` — i.e., infinitely many `n` have a height-`S(n)` tree `T` from the antichain whose reachable poset-DAG state set is `≤ poly(n)` (the falsifier: every height-`S(n)` tree from the antichain has `≥ n^{ω(1)}` states).

## Empirical finding (on `billy-dev`)

The canonical height-`S(n)` trees — optimal-policy DAGs from `scripts/strategy_dag_probe.py` (Experiment 1, `DAG(1)`) — have **exactly `2n! − 1` reachable states**:

| n | S(n) | reachable states | = 2n!−1? |
|---|---|---|---|
| 2 | 1 | 3 | 3 = 2·2−1 ✓ |
| 3 | 3 | 11 | 11 = 2·6−1 ✓ |
| 4 | 5 | 47 | 47 = 2·24−1 ✓ |
| 5 | 7 | 239 | 239 = 2·120−1 ✓ |
| 6 | 10 | 1439 | 1439 = 2·720−1 ✓ (independent DP, `/tmp/opencode/reach.py`) |

The union of *all* optimal strategies (`DAG(all)`) also grows: 19 (n=3), 181 (n=4), 1551 (n=5).

So the falsifier condition holds for the canonical trees (they have superpoly states, `2n!−1`), and no compact tree was found — the claim "`G(n)=0` for infinitely many n" has **no support**; the falsifier family appears to exist.

## Failed approach (compact "chain" DAGs)

Attempt: compact winning DAGs of height `k ≈ S(n)` with `~2k` states. Obstruction: any DAG of height `k` from `∅` is a full binary DAG — the root must have both children, and a terminal at depth 1 is impossible for `n ≥ 2` (one comparison leaves pairs undecided, so a depth-1 state is not total). The root therefore has two internal children, forcing the DAG to grow; the minimax policy DAG (`2n!−1`) is the natural compact candidate and is already huge. The falsifier's root obstruction is: *any* height-`k` winning DAG from the antichain is forced to branch twice at the root, so small state sets are not obviously incompatible with winning — the compactness question remains open in principle, but empirically every canonical height-`S(n)` tree is `2n!−1`.

## Honest limits (not established this session)

- I did **not** prove the universal statement *every* height-`S(n)` tree has `≥ 2n!−1` (or `≥ n!`) reachable states — the "falsifier for all trees" is open.
- I did **not** find a compact height-`S(n)` tree with poly states — the claim is unrefuted but unsupported.
- Numerical extrapolation from 4 points (n=2..6) is not a proof; `n=7` could not be checked (the F DP over the minimax game tree is infeasible at n=7 in Python).

## Status

- No Lean/repo/test changes — clean worktree.
- Scratch: `/tmp/opencode/reach.py` (DP experiment).
- Board #301: updated with the finding, the failed approach, and the open question (posted 2026-11-22T02:23Z).

**Bottom line:** the claim is unsupported — the canonical height-`S(n)` trees have `2n!−1 ≥ n^{ω(1)}` reachable states; the natural way to prove the full falsifier (a lower bound on `|R(T)|` for every height-`S(n)` tree) is a research item, not something established here.
