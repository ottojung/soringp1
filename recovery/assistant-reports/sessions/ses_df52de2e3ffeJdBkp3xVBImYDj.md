# antonina-EG3MKFfW4sNqMVkL2sx1wU-cooper

Session: ses_df52de2e3ffeJdBkp3xVBImYDj
Workspace: /home/lubko/soring-fronts/cospectral-gap-antichain-reachability-alln
Created: 1795477872070; updated: 1795480399612

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20ad22096001kBpizP6XLHwaCI)

I'll start by verifying my environment and reading the required documents.

## Output 17 (msg_20ad22b4a001K62Pc8xQXhQuAu)

I'm on `billy-dev` on the right branch. Let me read the required documents.

## Output 32 (msg_20ad2341e001nwNo22Z8uT9xeO)

Now let me find the research board and other key docs.

## Output 51 (msg_20ad23f3e001vF5UfinW9Q5N8u)

Let me read the board digest and key research docs in parallel.

## Output 66 (msg_20ad24e160011reNzOAp1kRDUJ)

Let me read the full relevant board posts and key research notes.

## Output 97 (msg_20ad273c800199TrKHdOp1ljuE)

Let me search for the reachability window definitions and related invariants.

## Output 108 (msg_20ad2a180001CgfGD1k1hT4hPS)

Let me read the full 23:46Z post (directly relevant) and the key asymptotic/structural docs.

## Output 136 (msg_20ad3a37f001LXBLHR90UBuSSu)

Let me read the full 23:46Z board post via the raw board data and check available scripts.

## Output 165 (msg_20ad4c480001h0adzjdxjwPx20)

Let me use the shell tool directly.

## Output 217 (msg_20ad5f086001o44q3p3G1fgVje)

Let me check for prior work on this specific front (in case of infrastructure failure) and inspect scratch/repo scripts.

## Output 276 (msg_20ad6ba3600117W4EagHCRVc1d)

I now have a thorough picture. Let me set up scratch and verify the family facts computationally before attempting a decisive reachability computation.

## Output 318 (msg_20adaff1700178n7HltYuZ7XfL)

The Python F evaluator is too slow at n=14. Let me look at the faster C++/pruned engines from prior scratch.

## Output 351 (msg_20add13d70012ErSq6cKSk0z3F)

The Python F evaluator is too slow at n=14. Let me write a fast C++ engine (mirroring the one the board used) to compute F and then attempt a backward reachability search.

## Output 537 (msg_20ae1dd94001ZnN9Y0WCXmLUxm)

F now works fast (matches board: 3103 states for P²). Let me implement the backward F-tight reachability search.

## Output 598 (msg_20ae5358c001fG7rTdh3V9Db6l)

Found the bug — `inc` array too small (up to 91 incomparable pairs vs N=14). Let me fix both engines.

## Output 801 (msg_20af7535500101KtESEgLny6ql)

## Recovery / audit

- **Host/repo**: `billy-dev`, `/home/lubko/soring-fronts/cospectral-gap-antichain-reachability-alln`, branch `billy-dev...origin/billy-dev`, clean worktree before and after (`git status --short --branch` empty except branch line). No commits, no pushes, no #301 post, no Lean/repo file changes. Scratch only under `/tmp/opencode/cg_reach_task/`.
- **Board check**: scanned recent #301 digest and searched for `cospectral-gap-antichain-reachability` on page 1; no prior post with this exact front slug found. I did not duplicate any external action.

## Front attacked

> Can any member of an (e,M1)-cospectral, F-different poset family with unbounded F-gap (the board's 23:01Z ordinal-power construction) be realized up to isomorphism as a state reachable from the n-antichain along a height-S(n) optimal play, for some all-n family of sizes; equivalently, does the one-step extension-count invariant M1 fail to determine the exact minimax cost already on the optimal-play-reachable domain rather than only on arbitrary posets?

Falsifier asked for: a reachability invariant excluding every such family member at every n, or an explicit member on a height-S(n) path at some n.

## Definitions / model [definition]

- `P` is a finite strict poset state on labelled keys; `e(P)` its linear-extension count; `F(P)` the minimax remaining comparison count (`F` total = 0, else `1+min_{incomparable x,y} max(F(P+x<y),F(P+y<x))`); `A_n` antichain, `F(A_n)=S(n)`.
- `M1(P)` is the multiset of `e(C)` over both one-step children `C` of every incomparable pair (the one-step extension-count profile).
- **Optimal-play-reachable** (as in recent #301 fronts): reachable from `A_n` by comparisons each reducing `F` by exactly 1, i.e. on a height-`S(n)` minimax path. Depth of such a state is `d=S(n)-F(P)`.
- Ordinal sum `A(+)B`: disjoint union with every element of `A` below every element of `B`. `P_k = P(+)^k P`, `Q_k = Q(+)^k Q`.

## Reproduced family facts [experiment, independent scratch]

Using a from-scratch Python engine (`/tmp/opencode/cg_reach_task/engine.py`, own closure/downset-DP `e`/memoized `F`; also cross-checked F with a compiled C++ engine, same results): seed

- `P = closure(7,(0x3e,0x0c,0,0,0x04,0x08,0x3e))`, `Q = closure(7,(0x3e,0x0c,0,0,0x0c,0x04,0x1e))`
- `e(P)=e(Q)=32`, `M1(P)=M1(Q)`, `F(P)=5, F(Q)=6`.
- `P^2=P(+)P, Q^2=Q(+)Q` on 14: `e=1024`, `M1` equal, `F(P^2)=10, F(Q^2)=12` (C++ direct minimax: 3103 states for `P^2`, 90418 for `Q^2`, consistent with board 23:01Z/23:05Z).

Literature/repo-deduction used as context (not re-proved here): ordinal-sum additivity `F(A(+)B)=F(A)+F(B)` (`docs/research-series-decomposition.md` Thm 1) and the M1-preservation lemma for ordinal powers give the all-k family `e=32^k, M1(P_k)=M1(Q_k), F(P_k)=5k, F(Q_k)=6k`, gap `k` unbounded. This is the 23:01Z gapspan result; I did not re-prove the general lemma, only spot-checked k=1,2.

## Mathematical findings

### 1. Cover-count reachability invariant [deduction]

Let `cov(P)` be the number of cover relations (Hasse edges) of poset `P`. For any comparison outcome adding an incomparable pair `(x,y)` to a reachable state `R_{i-1}` to get `R_i` after transitive closure, `cov(R_i) <= cov(R_{i-1}) + 1`.

*Proof sketch*: adding relations never makes an old non-cover a cover. An old cover is destroyed only when a middle is added. Any newly comparable pair other than `(x,y)` itself is added by closure through `x` or `y` and therefore has `x` or `y` as a middle, so it cannot be a new cover. Hence only `(x,y)` can be a new cover, giving the +1 bound. ∎

Starting at `cov(A_n)=0`, induction gives `cov(P) <= d` for every state reachable in `d` comparisons. Therefore optimal-play reachability implies the necessary window

`cov(P) <= d = S(n)-F(P)`.  [deduction]

### 2. Cover-count excludes k=1 but not k>=2 [deduction + small experiment]

For an ordinal sum, covers are internal covers plus cross covers between `Max(A)` and `Min(B)`: `cov(A(+)B)=cov(A)+cov(B)+|Max(A)||Min(B)|` (a Max–Min cross pair has no middle by maximality/minimality; internal covers remain covers for the same reason). For the seed, `cov(P)=10, |Max(P)|=|Min(P)|=2` (verified by engine). Thus

`cov(P_k)=k*cov(P)+(k-1)*|Max(P)||Min(P)| = 10k+4(k-1)=14k-4`, and similarly `cov(Q_k)=14k-4`.

Optimal-play window for `P_k` on `n=7k`: `14k-4 <= S(7k)-5k`, i.e. `S(7k) >= 19k-4`.

- `k=1`: `10 <= S(7)-5 = 13-5 = 8` is **false**. So the seed members `P,Q` are excluded by the cover-count window. [deduction, using S(7)=13 literature]
- `k>=2`: `S(7k) >= ceil(log2 (7k)!) = Omega(k log k)` (information bound, literature), so the inequality holds for all sufficiently large k; it is also satisfied at small k using A036604 index values (e.g. k=2,n=14: `24 <= S(14)-10 = 38-10 = 28` under A036604 `S(14)=38`; the exact S(14) value should be treated as a literature index, not re-proved here). Thus the simple cover-count invariant does **not** exclude `k>=2`. [deduction + literature index]

For `Q_k`, the bound is `14k-4 <= S(7k)-6k`, i.e. `S(7k)>=20k-4`; k=1 excluded (`10<=7` false), k>=2 not excluded by this count.

### 3. No stronger excluding invariant found; no reachable witness found [honest limit]

I tried to disprove reachability (negative answer) by stronger invariants:

- **Width / Max / Min**: `w(P_k)=w(P)=3`, `|Max(P_k)|=2`, `|Min(P_k)|=2`, constant in k — no exclusion.
- **Cross-comparison cost**: establishing all A<B in an ordinal sum needs only `|Max(A)||Min(B)|` comparisons per adjacent block boundary by transitivity, so `4(k-1)` total cross comparisons, linear and cheap.
- **F-tight backward reachability (decisive test)**: attempted a backward DFS from `P^2` (n=14, F=10) upward through F-tight predecessors to `F=S(14)`. It is computationally obstructed: F-valuation explodes along the upward F ladder (observed 1,496,573 fstates at node 4, F=13, before timeout/OOM-kill; process produced no reachability answer). I did not obtain a reachable/unreachable certificate for `P^2` or any `k>=2`.

I also tried to disprove non-reachability (positive answer) by constructing an explicit F-tight path. I did **not** find one. A non-F-tight construction exists (build P on 7, P on 7, 4 cross covers = 24 comparisons, then finish in F=10; total 34 on that line, not a height-S(14) optimal-play witness), which only shows the state is easy to finish from, not optimal-play-reachable.

## Verdict

**OPEN (not settled by this attack).**

- The asked front is neither proved nor refuted here.
- I **disproved the k=1 instance** of optimal-play reachability by a simple cover-count window invariant: `cov(P)=10 > S(7)-F(P)=8` and `cov(Q)=10 > S(7)-F(Q)=7`. [deduction]
- I **did not** exclude `k>=2`; the same cover-count invariant becomes too weak (superlinear S(7k) vs linear 14k-4).
- I **did not** exhibit any `P_k/Q_k`, `k>=2`, on a height-`S(7k)` optimal play. The decisive F-tight backward reachability test for P^2 was computationally infeasible with the naive F-memoized DFS.
- **Complexity implication remains conditional**: a positive witness would rule out (e,M1)-only certificates, even O(1)-additive, on the optimal-play-reachable domain; a negative all-k exclusion would isolate a stronger reachability invariant under which M1 remains sound. Neither is established.

## Failed approaches / obstructions

1. **Naive backward F-tight DFS from P^2**: infeasible because exact F computation is memoized over the explored subgame and explodes as F increases (1.5M fstates at F=13 after 4 nodes). Needs either a much stronger F oracle, a symbolic/structural reachability argument, or meet-in-middle with tight bounds. [experiment]
2. **Simple counting invariants** (covers, width, Max/Min, cross-comparison count): all linear/constant and dominated by superlinear S(7k) for k>=2. [deduction]
3. **Non-F-tight construction**: reaching P^2 in 24 comparisons gives a 34-comparison line, not a height-S(14)=38 optimal-play witness; it cannot certify optimal-play reachability. [deduction]

## Limits / next decisive step

The natural next falsifiable step is a **structural F-tight reachability invariant for ordinal-sum normal forms**: either prove that any F-tight optimal-play path reaching an ordinal sum A(+)B must pass through (or be reducible to) block-wise F-tight plays, giving an inductive obstruction for P^k/Q^k; or find an explicit F-tight path for P^2 by a constrained backward search that avoids full F recomputation (e.g. certify F(R0)=F(R)+1 by local witness/sibling bounds, or use SAT/IDA* over the narrow cover-removal frontier). I did not complete that step.

## Output 812 (msg_20af886fc001ZMp71RGlQbKGXV)

No unfinished external actions to repeat. I inspected the state: `billy-dev`, clean worktree on `billy-dev...origin/billy-dev`, no repo/Lean/test/CI/ledger changes, no #301 post made, and scratch work only in `/tmp/opencode/cg_reach_task/`.

The front remains **OPEN**. My completed finding:

- **Derived invariant [deduction]**: `cov(P) <= d` for any state reachable in `d` comparisons from `A_n`, since only the directly added comparison can become a new Hasse cover. Thus optimal-play reachability requires `cov(P) <= S(n)-F(P)`.
- **Applied to the gapspan ordinal-power family [deduction + small experiment]**: for `P_k=P(+)^k P`, `Q_k` on `n=7k`, `cov=14k-4`, `F(P_k)=5k, F(Q_k)=6k`. The cover window excludes `k=1` (`10 > S(7)-F`, S(7)=13 literature) but does **not** exclude `k>=2` because `S(7k)=Omega(k log k)` dominates linear `14k-4`.
- **Not settled**: I found no stronger excluding reachability invariant and no explicit `k>=2` member on a height-`S(7k)` optimal play. A naive backward F-tight DFS for `P^2` (n=14, F=10) was computationally obstructed by F-valuation explosion (1.5M fstates at F=13 after 4 nodes), so no reachability certificate either way.
- **Complexity implication**: remains conditional; a positive witness would rule out (e,M1)-only O(1)-additive certificates on the optimal-play-reachable domain, a negative all-k exclusion would isolate a stronger reachability invariant. Neither established.
