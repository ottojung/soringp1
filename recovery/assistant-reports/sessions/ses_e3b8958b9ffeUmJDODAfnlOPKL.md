# antonina-MI8IbEAPWahX3GoQFOjhBb-modified

Session: ses_e3b8958b9ffeUmJDODAfnlOPKL
Workspace: /home/lubko/soring-fronts/conp-adversary-memory-20261110
Created: 1794297473224; updated: 1794299631366

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 219 (msg_1c49739ec001P5g6uhg0a6uBKy)

## State (recovery)
- Host/worktree: `billy-dev`, `/home/lubko/soring-fronts/conp-adversary-memory-20261110`, clean detached at `6a96398` (no repo changes, no commits/PR/Lean).
- Inspected docs (`AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/research-certificates-barriers.md`, `docs/research-winning-frontier-barrier.md`) and #301 digest: no prior post for front `conp-adversary-memory` found; no duplicated external actions.
- Scratch only: `/tmp/opencode/conpmem` (`known.py`, `impl1.py`/`impl1b.py`, `mem1.py`, `minmem.py`, `impl2.py`, outputs, `post.txt`).

## Work completed (front `conp-adversary-memory`)
**Model [definition/literature].** Adaptive game `G(n,k)`; adversary wins iff `S(n)>k`. Used published `S(n)` for `n<=22` (docs/literature). Smallest budget `k=S(n)-1`: surplus `d=k-C(n)=-1` for tight cases and `d=0` for `n=12..19`. “Memory” treated as number of distinct internal states in an explicit strategy table `(state,pair)->(answer,next)` with state merging; state = `(poset, remaining budget r=k-t)`.

**Key deduction [deduction].** An oblivious 1-value adversary fixing a total order `π` and answering by `π` is *not* winning in adaptive `G(n,k)` (a sorter can follow `π`’s chain in `n-1` comparisons and totalize that fixed `π`), so adaptive dependence is necessary and the memory question is nontrivial. A winning adversary strategy exists when `S(n)>k` (minimax), needs `>=1` state.

**Exact/greedy exhaustive game solving with state merging [experiment]** (two independent implementations in `/tmp/opencode/conpmem`):
- **Impl1:** transitively-closed bitmask posets (minimax + admissible adversary-winning reachable graph + greedy state-reuse closure).
- **Impl2:** linear-extension-set states (different representation/logic), same pipeline.

Results for `k=S(n)-1`:

| n | S(n) | C(n) | k | admissible reachable | exact (poset,r)/posets | greedy1 (poset,r)/posets | greedy2 (poset,r)/posets |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0 | 1 | 1/1 (I1,I2) | - | - |
| 3 | 3 | 3 | 2 | 13 | 8/8 (I1,I2) | - | - |
| 4 | 5 | 5 | 4 | 243 | open (B&B unfinished) | 114/101 | 112/99 |
| 5 | 7 | 7 | 6 | 7821 | open | 1164/725 | 1159/725 |
| 6 | 10 | 10 | 9 | 367383 (I1) | open | greedy incomplete (timeout) | - |

- I1,I2 agree exactly for `n<=3` and on admissible counts for `n<=5` (243, 7821); greedy poset counts match at `n=5` (725) with small heuristic variance in `(poset,r)` states.
- `n=7,8,9`: not computed. No superpolynomial-growth witness found or refuted on this data.

## Acceptance / honest blocker
- **(a) Exact minimal-memory table for `n<=8` with two independent implementations agreeing:** not met (exact minima obtained only for `n<=3`; `n>=4` exact B&B unfinished, greedy gives upper bounds only).
- **(b) Proved superpolynomial memory lower bound for an explicit infinite family:** not met.
- **(c) Honest precise blocker with finite data:** met in substance — bottleneck is exhaustive game solving + state-merging minimization/closure: `n=4` exact B&B over ~450 binary choice points not completed in time; `n=6` greedy closure over 367,383 admissible states timed out in Python; `n=7,8,9` infeasible here (rapid state-space growth, e.g. `n=8, k=15`). Stronger solver needed (compiled, symmetry/quotient reduction, incremental closure).

## Board
- Posted once to Antonina #301 (RC=0) as author **"SoringP1 frontier: conp-adversary-memory"** with State, Result, Proof/experiment, Honest limits, Next question (no survey duplication). Body archived at `/tmp/opencode/conpmem/post.txt`.
- **Next question:** can symmetry reduction (on-the-fly relabeling quotient) or a compiled exact minimizer settle `n=4` and tighten `n=5,6` to reveal growth, and does any explicit family (e.g. near-tight `n=12, d=0`) force superpolynomial distinct adversary states under an optimal winning strategy?
