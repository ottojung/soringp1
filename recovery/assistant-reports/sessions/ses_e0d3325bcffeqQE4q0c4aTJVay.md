# antonina-DMfIzzj5PpsgrCiKdDJXYq-marrying

Session: ses_e0d3325bcffeqQE4q0c4aTJVay
Workspace: /home/lubko/soring-fronts/threshold-trigger-excess-window
Created: 1795074874023; updated: 1795076301216

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f2ccdd25001pE2ujv0sHJce0o)

I'll start by studying the repository state and the required documents. Let me gather the key context in parallel.

## Output 25 (msg_1f2cce937001snfliDt42vlUKV)

I'm on `billy-dev`. Let me read operations, literature, find board #301, and search for prior work on this exact front.

## Output 44 (msg_1f2ccffb9001gvbIkrF8BEA252)

Let me read the board digest (without flooding context), the frontier config, and search for prior work on the threshold table and excess bound.

## Output 63 (msg_1f2cd17fa001yWU8SIqaM81xAF)

The threshold notes are on `origin/main` (f89f6d0), not yet in my worktree. Let me check git state and read those notes plus search the board for this front's premise.

## Output 122 (msg_1f2cd77cf001HL75e7xqmb4e4j)

Now I have the threshold table. Let me examine the excess asymptotics literature and prior work on excess boundedness, then compute E(n) numerically.

## Output 163 (msg_1f2ce77da001SllWqWAH4SFtOX)

The front's numeric premise needs checking — D(n)=S(n)−⌈log₂n!⌉ is 1 for many n≤22, so E(n)=S(n)−log₂(n!) may exceed 1. Let me get authoritative S(n) values, compute E(n) vs g(r), and review related prior work.

## Output 195 (msg_1f2cf0cd5001pXFthkfYA6cdEq)

I've found the premise is likely flawed. Let me verify key computations, check the literature on balanced splits, and understand the board-posting mechanism.

## Output 223 (msg_1f2d108da001mhoTqTX0qeXaNN)

The premise is confirmed false numerically. Now let me try to actually construct an explicit reachable state (a genuine falsifier) via a balanced-split path using exact extension counting.

## Output 250 (msg_1f2d29b65001whogLsx8q673XD)

The greedy chose maximally *unbalanced* splits and collapsed to e=1 early. I need *balanced* splits following the larger branch so the path survives to depth t with minimal e. Let me fix.

## Output 275 (msg_1f2d4bde9001I7jt4zqlaPBrfl)

The balanced search is expensive. Let me optimize it and run just n=13 with a longer timeout.

## Output 341 (msg_1f2d59b7900154skZGclleDerh)

Now the counter is correct. Let me run the balanced path construction.

## Output 350 (msg_1f2d724d0001ihEq50qU2afT5f)

The `fib` helper was off by one (T values printed were wrong), and greedy follows a single path. Let me fix and run a beam search to find the minimal reachable e at depth t.

## Output 404 (msg_1f2e1a3c8001BeSPJIhRSAVEVh)

**Recovery/state inspection (per instruction):** billy-dev, `billy-dev` @ `6a96398` (origin/main `c865b23`), `git status` clean, no commits/PRs/board posts made by this session. Board #301 recent digest inspected (no prior post for this front id found). Only local scratch artifacts created in `/tmp/opencode` (`balanced_path.py`, `balanced_path2.py`, `beam_trigger.py`, plus `__pycache__`) from attempted constructions; no external side effects duplicated.

## Sources studied
- `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md` (this checkout).
- `git show f89f6d0:docs/research-core-threshold.md` (on `main`, not in local checkout): finite thresholds `T(2..8)=4,7,12,20,33,54,88 = F_{r+3}-1` for `r<=8` [experiment, conditional on the audited/cross-checked census there]; sharp witnesses `W_{r+2}` with `e(W_{r+2})=F_{r+3}`, `m(W_{r+2})=r+1`. The all-`r` statement `e(P)>=F_{m(P)+2}` remains open.
- Literature/index values used: `S(1..22)=0,1,3,5,7,10,13,16,19,22,26,30,34,38,42,46,50,54,58,62,66,71` (OEIS A036604; consistent with `docs/literature.md`/`docs/problem.md`, and Stober–Weiß 2023 for 16–18/known range ≤22) **[literature/index]**.
- Comparison model as in `docs/problem.md`/core-threshold note: `m(P)` = minimax comparison height for poset `P`, `e(P)` = #linear extensions.

## Precise claim attacked (all-`n` reading of the front)
For `r ∈ {7,8}`, let `t(n,r)=S(n)-r` and `E(n)=S(n)-log2(n!)`. The front states: every state reachable from the `n`-antichain at residual budget `r` obeys `e(P) >= 2^(r-E(n))`, hence a trigger `e(P) <= T(r)` is possible only when `E(n) >= g(r):=r-log2 T(r)`, and (evidence) since all exactly known `n<=22` have excess below 1 while `g(8)≈1.54`, `T(8)` never triggers on reachable states there.

I treat “reachable … at residual budget `r`” as: `P` is reachable in `t=S(n)-r` comparisons from the antichain and still sortable within `r` further comparisons on that continuation (`m(P)<=r`), i.e. a node at depth `t` on some height-`S(n)` sorting strategy. (A stricter reading `m(P)=r` is discussed below.)

## 1. Refutation of the stated universal lower bound [deduction]
**Claim “every such state obeys `e(P) >= 2^(r-E(n))`” is false** for arbitrary reachable states at depth `t=S(n)-r` (even with `m(P)<=r`).

- **Model fact.** A comparison on state `P` splits extensions into disjoint branches `P1,P2`, so `e(P)=e(P1)+e(P2)` and the taken branch has `e(P_i) <= e(P)`. Along any path, `e` can drop below any positive lower bound before `t` (down to `1`). Conversely, for *any* decision strategy/tree, choosing at each step the branch with larger `e` yields a root-to-leaf path with
  `e(P_d) >= e(P_{d-1})/2 >= … >= n!/2^d` for every depth `d`. [deduction, standard adversary/information argument]
- **Concrete counterexample to the universal bound.** `n=3, S(3)=3, E(3)=3-log2(6)=0.415037`, `t=2, r=1`. Path: compare `(0,1)` take `0<1` (`e=3`); compare `(0,2)` take `2<0` gives total order `2<0<1` with `e(P)=1`, `m(P)=0 <= 1`, but `2^(r-E)=2^0.58496 ≈ 1.5 > 1`. So the stated inequality fails as “every reachable state”. [deduction]

**Sound form.** For every height-`S(n)` sorting tree there exists some state at depth `t=S(n)-r` with `e(P) >= n!/2^t = 2^(r-E(n))` and `m(P) <= r`. Therefore `e(P) <= T(r)` is *information-compatible on such an adversary-balanced branch* only when `2^(r-E(n)) <= T(r)`, i.e. `E(n) >= g(r)`. This is a necessary condition for a trigger on that balanced branch, not a universal property of all reachable states and not sufficient for existence of any `e(P)<=T(r)` state. [deduction]

## 2. Correction of the numeric evidence / excess window [deduction, literature/index]
Using `g(7)=7-log2 54 = 1.245112`, `g(8)=8-log2 88 = 1.540568` and OEIS A036604 `S(n)`:

| r | g(r) | n with `E(n)>=g(r)` (n<=22) | `E(n)` | `e_min = floor(n!/2^(S(n)-r))` | `T(r)` | window `e_min<=T(r)` |
|---|---:|---|---:|---:|---:|:--:|
| 7 | 1.245112 | 13 | 1.464105 | 46 | 54 | yes |
| 7 |  | 14 | 1.656750 | 40 | 54 | yes |
| 7 |  | 15 | 1.749860 | 38 | 54 | yes |
| 7 |  | 16 | 1.749860 | 38 | 54 | yes |
| 7 |  | 17 | 1.662397 | 40 | 54 | yes |
| 7 |  | 18 | 1.492472 | 45 | 54 | yes |
| 8 | 1.540568 | 14 | 1.656750 | 81 | 88 | yes |
| 8 |  | 15 | 1.749860 | 76 | 88 | yes |
| 8 |  | 16 | 1.749860 | 76 | 88 | yes |
| 8 |  | 17 | 1.662397 | 80 | 88 | yes |

(`e_min` is the adversary-balanced extension count at depth `t=S(n)-r`.) Thus the prompt’s evidence is **incorrect as stated**: real excess `E(n)=S(n)-log2(n!)` exceeds `1` for `n>=12` in many known cases and exceeds `g(8)` for `n=14,15,16,17`, so the information window for a trigger at `r=8` is nonempty on balanced branches for those `n`. The statement “excess below 1” holds instead for the integer ceiling gap `D(n)=S(n)-ceil(log2 n!) <= 1` on known `n<=22`, which is a different quantity and does not by itself imply `E(n) < g(8)`. [deduction, literature/index]

(For `r=7`, `n=19` has `E≈1.24454 < g(7)` so `e_min=54 == T(7)` is a boundary by this count but the strict inequality `E>=g(7)` needed for `e_min <= T(7)` via the continuous bound fails marginally; integer `e_min=54` equals `T(7)`.)

## 3. Attempt to DISPROVE “inert for all n” by exhibiting a genuine trigger [experiment — inconclusive]
Falsifier sought: a genuinely reachable `P` at residual budget `r>=7` with `e(P) <= T(r)`.

- **Necessary structural facts [deduction + literature/experiment for thresholds].** `e(P) <= 2^{m(P)} <= 2^r` always. For `r<=8`, `e(P) <= T(r)=F_{r+3}-1 => m(P)<=r` (core-threshold table). Conversely, if one required the critical case `m(P)=r`, that would force `e(P) >= T(r-1)+1 = F_{r+2}` (e.g. `>=34` for `r=7`, `>=55` for `r=8`), so a critical trigger would live in a narrow band `[F_{r+2}, F_{r+3}-1]`. A reachable state with `m(P)<r` could also satisfy `e(P)<=T(r)` (including trivial `e=1` leaves on early-finishing branches), but leaves/fully-determined states are not informative base cases in the same way; the substantively interesting case is a nonterminal state resolvable by the table within the remaining budget.
- **Explicit construction attempts (scratch, `/tmp/opencode`).** Exact linear-extension counting over partial orders (predecessor-mask DP, verified on antichains/small splits) with path search from the `n`-antichain to depth `t=S(n)-r`:
  - `balanced_path.py` / `balanced_path2.py`: greedy choice of the most balanced incomparable comparison, following the larger branch (to stay on an adversary-balanced/high-`e` path). Results: `(n,r)=(13,7,t=27)-> e=72 (T=54)`, `(14,8,t=30)-> e=128 (T=54 reported in one buggy print but correct T is 88; e=128>88)`, `(15,8)->156`, `(16,8)->156`, `(17,8)->160`, `(18,7)->90` — **no trigger found**. (These are single heuristic paths, not exhaustive.)
  - `beam_trigger.py`: beam search over comparisons/branches (dedup by poset state) to minimize `e` at depth `t`. Run on `(13,7),(14,8),(14,7),(15,8)` with width 12; process was **SIGKILLed** before completion (n=13/14 state spaces too large for this naive exact enumeration in the time/resources available). **No witness found, no exhaustion.** [experiment, failed/incomplete approach]

I did **not** obtain an `n` and genuinely reachable `P` at residual budget `r>=7` with `e(P)<=T(r)`, nor a proof that none exists.

## 4. Obstruction / limits (honest)
- **Open for the window cases.** For `n∈{14,15,16,17}, r=8` (and analogous `r=7` cases) the global/adversary information condition is satisfiable and even `e_min ∈ [76,81] ⊂ [1,88]`, so nothing in the comparison/information counting above rules out a trigger state. Deciding existence seems to require either (a) an explicit reachable poset `P` at depth `t` with `e(P)<=T(r)` and a certificate that `P` lies on some `S(n)`-feasible strategy (or at least is reachable with `m(P)<=r`), or (b) a structural argument that no poset in the threshold family/low-`e` regime is reachable from `A_n` within `t` comparisons under any optimal/budget-feasible play. I have neither. [open]
- **Why nontrivial.** `T(r)` is tiny (`54,88`) while reachable states at those depths are highly constrained by ~27–34 prior comparisons; the realizable set of `(P,e(P),m(P))` from the antichain root is not characterized. General-poset threshold facts (core-threshold) give the `e=>m` implication but not root-reachability/completeness for triggering. [distinction: soundness of threshold vs reachability/completeness of trigger]
- **Asymptotic note (caution).** `g(r) ~ (1-log2 φ)r ≈ 0.306 r`. Sergeev’s bound gives `E(n)=O(n/(log n)^{1/5})` **[literature]**, so for sufficiently large `n` the condition `E(n)>=g(r)` is compatible with larger `r` (within that asymptotic allowance), but actual growth/values of `E(n)$ for `n>=23` are open and `T(r)` is verified here only for `r<=8`; no asymptotic trigger can be concluded.

## 5. Complexity implication (conditional) [deduction]
- **If inert (no reachable/encountered state has `e(P)<=T(r)` in the relevant evaluation regime):** the finite `T(r<=8)` table cannot act as a base-case/pruning shortcut for exact evaluation of `S(n)` in that regime — a **barrier to this specific threshold/base-case method**, not to all methods and not a separation result.
- **If it triggers:** it identifies a narrow window where such base cases can help, but (per the sound adversary form) compatibility at fixed `r` is tied to `E(n)>=g(r)`; for known `n<=22` this window is nonempty at `r=7,8` despite the front’s stated evidence, so triggering is not excluded by the global-excess argument (though no instance was found).
- This does **not** by itself yield a new uniform bound for `SORT-BOUND-U` / `S_unary`, nor any `P/NP/PSPACE` separation; `SORT-BOUND-U ∈ PSPACE` remains the baseline constraint (`AGENTS.md`/`docs/problem.md`).

## Bottom line
**Mathematical finding:** the front’s key inequality `e(P) >= 2^(r-E(n))` for every reachable state at residual budget `r` is **false** (counterexample `n=3,r=1,e=1`); the correct adversary statement gives only existence of some balanced-path state with that bound. With the correct `E(n)$, the `r=8` (and `r=7`) information window is **nonempty for several exactly known `n`** (`n=14..17` for `r=8`), contradicting the provided evidence. A **concrete reachable trigger state was not found** (greedy/partial beam search inconclusive) and **nonexistence was not proved**; the exact answer “for which `n` does `T(7),T(8)` trigger on genuinely reachable states?” remains **open** from this analysis. No substantive new theorem/counterexample warranting a repo or Lean change was established.
