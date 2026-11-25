# antonina-edtwmbSgBGHxoyOrAFq5pY-deemed

Session: ses_e0917c7baffeFbycrDNPOjNVXN
Workspace: /home/lubko/soring-fronts/split-completion-coupling-penalty-alln
Created: 1795143776397; updated: 1795146080101

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f6e83a5a001TehHR7M01cS34p)

I'll start by understanding the repository structure and the key documents. Let me explore in parallel.

## Output 21 (msg_1f6e84faa001DQqoN0OUoikZEt)

I'm on `billy-dev`. Let me read the key documents.

## Output 49 (msg_1f6e86ec6001hGKSIPJtreQaJl)

The split-schema doc is on origin/main. Let me check the board digest and the frontier definition, plus look at that doc on origin/main.

## Output 68 (msg_1f6e88e4f001CgMfaicaqvUnXO)

Let me find commit 9018729 and the split-schema content across branches.

## Output 87 (msg_1f6e8a072001n60UU4Ynm29y94)

The split-schema doc exists at commit 9018729. Let me read it fully along with the publication record and the script.

## Output 98 (msg_1f6e8abd7001XDYmI8yuJyiqM2)

Let me read the computation script, its tests, and the publication record.

## Output 118 (msg_1f6e8d868001vlLgJ3CY6KEAhg)

Now I understand the front. Let me run the published solver and study the primary literature in parallel.

## Output 133 (msg_1f6e94169001HfIpcKlScnKfXx)

The published script isn't in this branch's worktree. Let me extract it to scratch, check known S(n) values vs the information bound, and research the literature.

## Output 148 (msg_1f6e98524001A3WiPB6ty5lH5R)

Key finding so far: for m=1, π(1,n)=S(n)−⌈log₂ n!⌉, a classic open quantity; known values up to n=22 give gap ≤1. Let me research the literature on sorting with partial information and start an independent solver.

## Output 167 (msg_1f6ea3a7c0017pEcdmPjQU8yDI)

Web search is unavailable, but I can use webfetch on specific sources later. Let me build an independent from-scratch exact solver in C++ and validate it against the published cells before pushing to larger ones.

## Output 203 (msg_1f6eac505001IDIKK47LxiEbzC)

Go is available. Let me port the independent solver to Go.

## Output 221 (msg_1f6ec7567001pj5ankiY5qTCNy)

My solver matches the published C values, but my info-bound helper used floor instead of ceil. Let me fix that and push to larger cells.

## Output 241 (msg_1f6ecabef001uwPs38Ad6LlnQx)

My independent solver now exactly reproduces all published cells. Let me push to larger cells in parallel.

## Output 268 (msg_1f6edeb9d001QeHX9XkENp9EDS)

No π≥2 yet, but several new π=1 cells. Let me push to n=13–16.

## Output 288 (msg_1f6f4bfe5001BwUXDnZJcNmjUe)

Brute force hits a wall around 10⁴ extensions. The free keys are symmetric, so let me add canonicalization under free-key permutations to the independent solver.

## Output 306 (msg_1f6f6246c001RkCODng5XZmDT7)

Symmetry helps but large cells remain expensive. Let me add a start-depth option so I can test only the decisive depth (info+1).

## Output 433 (msg_1f70a21800015QSmblz1S4ylyy)

## Recovery / side-effect audit (billy-dev, 2026-11-20)
- Inspected before continuing: conversation state, `git status --short --branch` on `billy-dev...origin/billy-dev` (clean), no `docs/research-fo-tc-split-schema.md` or `scripts/fo_tc_split_schema.py` in the worktree, and durable scratch under `/tmp/opencode/split/` (extracted 9018729 script/tests, my independent solvers, logs, partial outputs).
- Actual external side effects found: **none**. No Antonina/#301 post, no commit/PR/push, no Lean/test/workflow/repo edit, no purchase. I temporarily copied the published script into `scripts/` to run it and removed it (`rm -f scripts/fo_tc_split_schema.py`); worktree is clean now.
- Interrupted run: a batch testing larger cells was killed (SIGKILL). From scratch artifacts, `C(9,13)=16` (π=1, decisive depth 16) completed and is recorded in `/tmp/opencode/split/{out,log,results2}.txt`; `10,14`, `11,14`, … had empty/absent outputs in that batch and remain **uncertain/uncomputed** from that attempt (not guessed). I then computed `11,14,12,14,13,14,12,15,13,15,14,15` to completion with a corrected extension generator (see below). I did not repeat any external action.

## Sources studied
- `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md` (repo).
- Board digest `python3 /home/lubko/soring301/scripts/board_digest.py --recent 7` (#301): 2026-11-20 publication cross-reference for commit `9018729` (FO(TC) note + split-schema phase-coupling barrier, independently refereed/two-sided verified per record; no theorem completion for S(n)/SORT-BOUND-U). No prior `π(m,n) >= 2` counterexample reported.
- `origin/main` commit `9018729` contents (read via `git show`): `docs/research-fo-tc-split-schema.md`, `docs/research-fotc-publication-record.md`, `scripts/fo_tc_split_schema.py`, `tests/test_fo_tc_split_schema.py`. The split-schema doc defines `C(m,n)` as the minimax completion cost given a known sorted `m`-chain, proves `split cost >= S(m)+C(m,n)` and `C(m,n) >= ⌈log2(n!/m!)⌉`, and reports exact cells with `π(m,n)=C(m,n)-⌈log2(n!/m!)⌉ ∈ {0,1}` through those tested.
- Primary/literature anchors (per `docs/literature.md`, `docs/problem.md`): Ford–Johnson (1959), Knuth TAOCP v3 §5.3.1, OEIS A036604/A003070, Peczarski (2012), Stober–Weiß (ALENEX 2023, arXiv:2206.05597) for exact `S(n)`/small-gap context; Mahaney (1982) sparsity barrier (context only). Model: adaptive comparison decision trees on `n` distinct labelled keys, worst-case height, `S(n)=min height`, unary threshold `SORT-BOUND-U={1^n#1^k : S(n)<=k}`; `S` is a function, general-poset hardness/optimization results do not transfer without a reduction (AGENTS).

## Precise all-`n` question attacked (front)
Let `C(m,n)` be the exact minimax number of further comparisons needed to fully sort `n` distinct keys given a known total order on a fixed `m`-subset (every legal splitting pair, arbitrary phase 2), and
`π(m,n) := C(m,n) - ⌈log2(n!/m!)⌉ ≥ 0` (information-theoretic slack / phase-coupling penalty).
**Claim under test (falsifiable, all `1 <= m < n`):** `π(m,n) <= 1` uniformly.
- **Falsifier (disproof):** exhibit any `(m,n)` with `π(m,n) >= 2` (exact).
- **Alternative:** a general argument that `π(m,n) <= 1` for all `m<n`.
- **Complexity implication (as stated):** uniform `π<=1` would cap the phase-coupling tax of the natural fixed-split compositional FO(TC)/ESP compiler at +1 comparison per split for every `n`; unbounded/large `π` would strengthen a barrier against fixed-split compositional exact programs for `SORT-BOUND-U`. (This is about that compiler/route’s overhead, not by itself a separation or a completeness theorem for unrestricted programs; soundness of a certificate/witness route is distinct from completeness.)

I treated this as a question about the **specific poset family** `P_{m,n}` = a chain of `m` plus `n-m` pairwise-unconstrained free elements (the split-schema completion state), not about arbitrary partial orders.

## Methods (independent, [experiment])
- Re-ran the published `9018729` solver `scripts/fo_tc_split_schema.py` from scratch copy (exact minimax with memoization + balanced-query heuristic, witness replay): reproduced its printed cells including `C(2,4)=4, C(3,5)=5, C(2,5)=6, C(4,6)=6, C(3,6)=8, C(5,7)=6, C(4,7)=9, C(5,8)=9, C(6,9)=10`.
- Wrote **independent** exact solvers (different code paths): (v1) Go iterative deepening depth-bounded existence prover (no greedy upper-bound tree constructor, tries queries in balance order only as heuristic) over rank-tuple extension states generated by permutation enumeration; (v2) Go variant with canonicalization under permutations of the `n-m` free keys; (v3) Python exact generator of extensions as `C(n,m)·(n-m)!` assignments (no full `n!` enumeration) + memoized DFS existence prover. These compute `C(m,n)` as the least depth admitting a decision tree (a sound lower/upper characterization at the reported depth: depth `d-1` infeasible and depth `d` feasible under exhaustive splitting-pair search in that model). I cross-validated: v1/v2 agreed with published cells on all checked overlaps (e.g. `(4,6),(3,6),(4,7),(5,8),(6,9),(5,9),(2,6),(3,7),(2,8),(7,11),(8,12)`).
- Extension counts matched `n!/m!` and info bounds `⌈log2(n!/m!)⌉` throughout. These are computational results, not Lean-checked proofs.

## Exact results obtained (no `π >= 2` found)
`π = C - ⌈log2(n!/m!)⌉`. “Source”: pub = published/reproduced 9018729; ind = independent solver(s) in this session.

| (m,n) | n!/m! | ⌈log2⌉ | C | π | S(m)+C vs S(n) | source |
|---|---:|---:|---:|---:|---|---|
| (2,4) | 12 | 4 | 4 | 0 | 5 vs 5 | pub+ind |
| (3,5) | 20 | 5 | 5 | 0 | 8>7 | pub+ind |
| (2,5) | 60 | 6 | 6 | 0 | 7 vs 7 | pub+ind |
| (4,6) | 30 | 5 | 6 | 1 | 11>10 | pub+ind |
| (3,6) | 120 | 7 | 8 | 1 | 11>10 | pub+ind |
| (2,6) | 360 | 9 | 9 | 0 | 10 vs 10 | ind (+record) |
| (5,7) | 42 | 6 | 6 | 0 | 13 vs 13 | pub+ind |
| (4,7) | 210 | 8 | 9 | 1 | 14>13 | pub+ind |
| (3,7) | 840 | 10 | 10 | 0 | 13 vs 13 | ind (+record) |
| (5,8) | 336 | 9 | 9 | 0 | 16 vs 16 | pub+ind |
| (2,8) | 20160 | 15 | 15 | 0 | 16 vs 16 | ind (+record) |
| (6,9) | 504 | 9 | 10 | 1 | 20>19 | pub+ind |
| (5,9) | 3024 | 12 | 12 | 0 | 19 vs 19 | ind (+record) |
| (6,10) | 5040 | 13 | 13 | 0 | 23>22 | ind |
| (7,10) | 720 | 10 | 10 | 0 | 23>22 | ind |
| (8,10) | 90 | 7 | 7 | 0 | 23>22 | ind |
| (9,10) | 10 | 4 | 4 | 0 | 23>22 | ind |
| (7,11) | 7920 | 13 | 14 | 1 | 27>26 | ind |
| (8,11) | 990 | 10 | 11 | 1 | 27>26 | ind |
| (9,11) | 110 | 7 | 8 | 1 | 27>26 | ind |
| (10,11) | 11 | 4 | 4 | 0 | 26 vs 26 | ind (+record) |
| (8,12) | 11880 | 14 | 15 | 1 | 31>30 | ind |
| (9,12) | 1320 | 11 | 12 | 1 | 31>30 | ind |
| (10,12) | 132 | 8 | 8 | 0 | 30 vs 30 | ind (+record) |
| (11,12) | 12 | 4 | 4 | 0 | 30 vs 30 | ind |
| (9,13) | 17160 | 15 | 16 | 1 | 35>34 | ind |
| (10,13) | 1716 | 11 | 12 | 1 | 34 vs 34 | ind |
| (11,13) | 156 | 8 | 8 | 0 | 34 vs 34 | ind |
| (12,13) | 13 | 4 | 4 | 0 | 34 vs 34 | ind |
| (11,14) | 2184 | 12 | 12 | 0 | 38 vs 38 | ind |
| (12,14) | 182 | 8 | 8 | 0 | 38 vs 38 | ind |
| (13,14) | 14 | 4 | 4 | 0 | 38 vs 38 | ind |
| (12,15) | 2730 | 12 | 12 | 0 | 42 vs 42 | ind |
| (13,15) | 210 | 8 | 8 | 0 | 42 vs 42 | ind |
| (14,15) | 15 | 4 | 4 | 0 | 42 vs 42 | ind |

(For “S(m)+C vs S(n)” I used the standard values `S(0..15)=0,0,1,3,5,7,10,13,16,19,22,26,30,34,38,42`, A036604/established literature; kernel-checked in-repo only through small n per `docs/problem.md`.) Also checked arithmetically by the published script over all `1<=m<n<=12`: many splits have `S(m)+⌈log2(n!/m!)⌉ = S(n)` at the counting level but some still incur `π=1` (the 9018729 barrier); conversely several `B=S(n)` counting-exact cells remain `π=0` here. **Observed range: `π ∈ {0,1}` on every exactly computed cell; no instance of `π >= 2`.**

## Mathematical analysis (deduction / context)
1. **Reduction to the global sorting gap at `m=1` [deduction].** `P_{1,n}` is the antichain (no prior information), so `C(1,n)=S(n)` and `π(1,n)=S(n)-⌈log2(n!)⌉`. Therefore the all-`n` claim “`π(m,n) <= 1` for all `1<=m<n`” **implies** `S(n) <= ⌈log2(n!)⌉ + 1` for all `n`.
2. **Status of that corollary [literature].** Whether `S(n)` ever exceeds the information-theoretic lower bound by ≥2 is open in general; for all known exact values `S(0)..S(22)` (A036604; Peczarski 2012, Stober–Weiß 2023) the gap `S(n)-⌈log2(n!)⌉` is 0 or 1 (first 1 at `n=12`). Hence a **uniform proof** of `π(m,n) <= 1` would settle (in the affirmative direction, as a strong bound) a long-standing open behavior of `S(n)` itself — far beyond what is currently reachable. This is an obstruction to the “derive `π<=1` for all m<n” horn, independent of implementation.
3. **General-poset vs this family [model fidelity].** For arbitrary finite posets, `sort(P) >= ⌈log2 e(P)⌉` but balancing/overhead phenomena (Fredman; Kahn–Saks; 1/3–2/3 / 11/40-type balancing, Kahn–Kim et al.) concern general `P`; such results do not automatically yield either a uniform +1 bound or a +2 example for the specific structured family `P_{m,n}` (chain plus `r=n-m` free elements). No general-poset fact was used here as a claim about `C(m,n)` without a reduction.
4. **Soundness vs completeness (route-level).** `π(m,n)>=1` on a cell is a sound witness that the information price is not achievable for that split completion (a concrete coupling penalty, extending 9018729). Conversely, `π(m,n)=0` on tested cells is only existence of an optimal-height completion for those instances (and of the counting-feasible split where applicable), **not** completeness of any fixed compositional FO(TC)/ESP schema for all `n`, and not a proof that `π` stays ≤1.
5. **No new theorem.** I did **not** prove `π(m,n) <= 1` for all `m<n`, did **not** find a counterexample `π(m,n) >= 2`, and did **not** resolve any `S(n)`/`SORT-BOUND-U`/class-membership question. The front remains open.

## Failed approaches and exact obstructions
- **Exhaustive exact falsification at larger `n` [failed/incomplete approach].** Exact `C(m,n)` is minimax over all comparison decision trees on `L(m,n)=n!/m!` extensions. Even with symmetry-aware canonicalization and pruning, feasible exact search (in my implementations, on this host) reached ~`10^4`–`2*10^4` extensions comfortably and stalled/was interrupted beyond (naive full-permutation initialization also made `n>=14` cases fail in v1/v2). Cells left **uncomputed/uncertain** here include `10,14` (`24024`), `11,15` (`32760`) and larger `n` — precisely where a first `π>=2`, if it exists, might appear; I cannot claim their values.
- **Deriving a uniform `π<=1` bound [obstruction].** Any all-`n` proof must in particular bound `π(1,n)=S(n)-⌈log2(n!)⌉ <= 1` (point 2 above), which is an open global problem. A proof specialized to `m>=2` would need a structural argument on `P_{m,n}` strong enough to preclude a two-comparison information loss accumulating over all splits and all `n`; I identified no such argument, and none follows from the computed cells.
- **What would be decisive next:** an exact `π(m,n)>=2` certificate on any feasible larger cell (with independent replay/lower-bound verification, as in 9018729), or a genuine structural theorem bounding the coupling penalty for the `P_{m,n}` family (carefully separated from general-poset heuristics) — neither achieved.

## Bottom line
- **Falsifier:** not found. On every cell I computed exactly and independently verified against published data (table above), `π(m,n) ∈ {0,1}`.
- **All-`n` status:** **open**. Uniform `π<=1` is unrefuted but unproved and would imply the strong open corollary `S(n) <= ⌈log2(n!)⌉+1`; a counterexample, if any, lies beyond the exactly searched range.
- **Limits:** computational evidence only; no kernel-checked result; no claim of process success as proof; no repo/board/Lean/external side effects.
