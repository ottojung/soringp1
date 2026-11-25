# antonina-wQuq9bgqeEGoBcTgGJksNF-burned

Session: ses_e0b6cdb5dffeJmMjX6jLSFUsYu
Workspace: /home/lubko/soring-fronts/framed-join-info-condition-sufficiency
Created: 1795104646371; updated: 1795106257666

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f49326bb001jgf4qg7vUMWqL0)

I'll start by exploring the repository structure and reading the key documents in parallel.

## Output 31 (msg_1f494acb4001fZOrtIlbcjKE8W)

Let me examine the board, the working directory state, and search for earlier work on this front.

## Output 50 (msg_1f495b5290012kbxd8Js2MY4zl)

Let me find the specific board #301 post (15:02Z) and read the framed-DAG frontier doc.

## Output 65 (msg_1f496f980001YgxLXqPTIg7vg6)

Let me find how to read the full board post and check the script's capabilities.

## Output 80 (msg_1f49824750018MfpgsaUk5vCFF)

I'll extract the full 15:02Z board post via a small script rather than dumping the whole board.

## Output 95 (msg_1f499a98c0017LpYhjbor0q9yJ)

Let me read the Viche verification and the checker/strategy docs to nail down the exact definitions.

## Output 118 (msg_1f49c270d001HHZnmY3YzMrE8T)

Now I have the exact definitions. Let me build an independent computational probe to test the sufficiency claim: I'll enumerate reachable posets, compute exact sorting numbers F(P), and search for pairs whose intersection satisfies the information bound but is not sortable within budget.

## Output 136 (msg_1f49ceaf9001OA6ZcOEAurl5P3)

No counterexamples for n≤5. Let me extend to n=6 with a more efficient approach, and separately search all small posets for information-bound gaps.

## Output 154 (msg_1f49e1e62001bIv0SsxkQ1LUua)

Let me check whether reachable states are information-tight and how many aligned pairs satisfy the info condition at all.

## Output 176 (msg_1f49e7db0001mJlEbAZljfCnGK)

Interesting: all reachable states are information-tight, and satisfying pairs are always completable. Let me examine the extension counts of reachable states to understand the structural reason.

## Output 196 (msg_1f49ed338001ozb0TyDQmnegPZ)

Let me search whether general (not necessarily reachable) tight posets can have an info-satisfying intersection that is not sortable, to isolate the role of reachability.

## Output 222 (msg_1f49f94ad001bGKwz2HT84C4h1)

Found general-poset counterexamples. Now the decisive check: are those posets reachable in optimal play from the n=5 antichain?

## Output 240 (msg_1f49fbdcd001300hGrWtp2RNfC)

Let me inspect the satisfying pairs in detail—specifically whether R equals one of the parents or is itself reachable.

## Output 258 (msg_1f4a0152d0014UKQwxlF6aqnL8)

I've found the key structural picture. Let me verify n=6 reachability and pair-search to push the computational boundary.

## Output 283 (msg_1f4a82e9a001KKLaFJFTNDf6rL)

## Scope / side effects inspected (recovery)

- **Repo:** `/home/lubko/soring-fronts/framed-join-info-condition-sufficiency`, branch `billy-dev`, clean worktree, HEAD `6a96398` (git status clean; no commits made by me). No repository, Lean, test, workflow, or ledger files changed.
- **External actions:** none (no board posts, no commits, no PRs). Only scratch files created under `/tmp/opencode` (`join_probe.py`, `join_probe6.py`, `join_probe_stats.py`, `reach_e.py`, `general_pair.py`, `check_reach_pair.py`, `inspect_pairs.py`, `reach6.py`) and local computations run there.
- **Interrupted work:** an attempted exhaustive reachable-pair/alignment search for `n=6` (`/tmp/opencode/reach6.py`, all 720 slot permutations per pair over optimal-play reachable states) produced no output and was killed (SIGKILL/timeout). **No `n>=6` reachable counterexample or exhaustive-negative claim follows from that incomplete run.**
- **Sources read:** `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-framed-certificate-frontier.md`, `scripts/check_framed_strategy.py`, board #301 digest and the full 15:02:11Z `exact-budget-framed-dag-alln` post and 15:15:48Z Viche verification (extracted locally).

## Front (as stated, [definition])

In a sound permutation-framed DAG at exact budget `k = S(n)`, a forgetful join of reachable posets `P,Q` at depth `d` is sound only if `e(P ∩ Q) <= 2^(k-d)` (necessity, board #301 2026-11-19 15:02Z). Question: is this information condition also sufficient for all `n` — i.e. must any two reachable equal-depth posets with `e(P ∩ τ(Q)) <= 2^(k-d)` (for some slot bijection/alignment `τ`) admit compatible slot bijections and a sound height-`k` framed-DAG join completing to a total order?

## Model-level reduction (soundness vs completable join) [deduction]

- `e(R)` = number of linear extensions of a (transitively closed strict) poset/state `R`; `F(R)` = minimax comparison-sorting number of `R` (minimum worst-case comparisons to sort every linear extension of `R`, adaptive decision tree / poset game), with `F(·)=0` iff total and `F=1+min_{(x,y)} max(F(R∪{x<y}),F(R∪{y<x}))`.
- **Necessity (counting / soundness).** Any sound completion of a joined state `R = P ∩ τ(Q)` placed at depth `d` within total budget `k` has a decision-tree unfolding of height `<= r := k-d`, each leaf certifies at most one linear extension, hence `e(R) <= 2^r`. This is the board lemma; it is a necessary soundness condition, not a completeness guarantee.
- **Completability criterion.** A sound height-`k` framed-DAG join at depth `d` exists for aligned intersection `R` iff `F(R) <= r` (a height-`<=r` certificate/strategy sorts `R`; conversely unfolding any such DAG gives a decision tree of height `<=r`). Therefore the front’s sufficiency question is equivalent to: for reachable equal-depth `P,Q` (depth `d`, `k=S(n)`), does `∃τ: e(P ∩ τ(Q)) <= 2^r  =>  ∃τ' : F(P ∩ τ'(Q)) <= r`?
- **Monotonicity [deduction].** `R ⊆ P` (fewer constraints) implies `LinExt(P) ⊆ LinExt(R)` and hence `F(R) >= F(P)` and `e(R) >= e(P)` (any algorithm correct on all extensions of `R` is correct on all extensions of `P`). So for `R=P∩τ(Q)`, `F(R) >= max(F(P),F(Q))`. If a state is on an optimal play with remaining value `r`, `F` cannot decrease below that parent value under intersection.
- **Why counting alone is not, in general, sorting completability.** `e(R) <= 2^r` only gives the information-theoretic/counting lower bound `ceil(log2 e(R)) <= r`; it implies `F(R) <= r` only for posets with no information gap at that level. General posets can have `F(R) > ceil(log2 e(R))`.

## Finite separation: information condition is not sufficient for arbitrary posets [experiment/deduction, independently recomputed]

Exhaustive enumeration of posets on `n<=6` elements up to labeled isomorphism class representatives (closure of all orientations; `e` by ideal/linear-extension DP, `F` by memoized minimax over incomparable pairs), with intersection tested over all `n!` slot alignments:

- `n=4`: 16 posets up to iso, **0** information-gap posets.
- `n=5`: 63 posets up to iso, **1** information-gap poset (`e=8, F=4, ceil(log2 e)=3`).
- `n=6`: 318 posets up to iso, **36** information-gap posets (examples include `e=8,F=4`; `e=13,F=5`; `e=15,F=5`; `e=30,F=6`).

Concrete **general-poset** counterexample to the implication “`e(R) <= 2^r  =>  F(R) <= r`” (hence to join-completability from the count alone), `n=5, r=3, 2^r=8` (rows are bitmasks: element `i < j` iff bit `j` is set in row `i`, elements `0..4`):
- `P = (28,28,8,0,0)`, `e(P)=6`, `F(P)=3`.
- `Q = (30,24,8,0,0)`, `e(Q)=5`, `F(Q)=3`, `τ = id`.
- `R = P ∩ Q = (28,24,8,0,0)` has **`e(R)=8 <= 8` but `F(R)=4 > 3`**.

Thus the information/counting condition is necessary but not sufficient as a general poset principle: an intersection can remain within the extension-count budget while becoming an information-gap state that is unsortable within `r` comparisons. (13 such aligned tight-pair instances found over all poset pairs with `F=r` at `n=5` in this enumeration.) This is a **general-poset** separation only; the `P,Q` above are **not** reachable in optimal play from the `n=5` antichain (checked against the reachable set, below).

## Reachable-case evidence and exact obstruction (n <= 5) [experiment, independently recomputed]

I recomputed `S(2..5)=1,3,5,7`, optimal-play reachability from the `n`-antichain by BFS following only optimal moves (`1+max(F(child_<),F(child_>)) == F(parent)`), and tested **all** ordered pairs of distinct equal-depth reachable states over **all** `n!` slot alignments:

| n | S(n) | reachable states (all depths) | depths with any aligned pair satisfying `e(R)<=2^r` | satisfying pairs with `F(R)>r` |
|---|---:|---:|---|---:|
| 2 | 1 | 2 | none | 0 |
| 3 | 3 | 5 | d=2 (r=1): 8 of 36 | 0 |
| 4 | 5 | 12 | d=2: 8/288, d=3: 34/288, d=4: 4/48 | 0 |
| 5 | 7 | 19 | d=5 (r=2): 4/2400, d=6 (r=1): 16/2400 | 0 |

(Counts are aligned ordered-pair instances `(P, Q!=P, τ)` with `e(P∩τ(Q)) <= 2^(S(n)-d)`.)

Additional observations from the same computations:
- **No reachable info-gap states observed:** every reachable state had `F(P)=ceil(log2 e(P))` for `n<=5`.
- **Slack in extension count but not in `F`:** reachable extension counts can be strictly below `2^r` while `F` remains `r` (e.g. `n=5`: `d=3,r=4 -> e=15`; `d=4,r=3 -> e∈{7,8}`; `d=5,r=2 -> e∈{3,4}`).
- **All satisfying reachable intersections were trivial in effect:** in every satisfying instance found (`n<=5`), `R = P ∩ τ(Q)` equaled `P` or equaled `τ(Q)` (hence `F(R)<=r` held because the intersection did not create a strictly weaker/harder state). Nontrivial satisfying joins (`R` strictly below both parents, within count budget) did **not** occur in this range.
- Consistent with Viche’s all-`n` strengthening on board #301 (15:15Z): distinct **strongly** information-tight states with `e(P)=e(Q)=2^r` admit no nontrivial feasible forgetful join (`R ⊊ P => e(R)>2^r`), so any feasible join, if one exists, must involve extension-slack states; but the observed feasible joins collapsed to a parent rather than producing a new slack intersection.

## Assessment of the falsifier / exact obstruction

- **Status: OPEN for all `n` (neither proved nor disproved).** I did **not** exhibit an infinite family (nor any verified instance) of reachable equal-depth `P_n,Q_n` with `e(P_n ∩ τ(Q_n)) <= 2^(S(n)-d)` but `F(P_n ∩ τ(Q_n)) > S(n)-d`, and I did **not** prove sufficiency for all `n`.
- **Viable falsification mechanism (if it occurs):** a reachable aligned intersection `R` that is an information-gap poset with `ceil(log2 e(R)) <= k-d < F(R)` while still satisfying `e(R) <= 2^(k-d)`. By monotonicity this requires `F(R) >= max(F(P),F(Q))` and, in particular, a strict increase of sorting difficulty above a parent whose remaining budget is already `r` in the tight case. General-poset instances of the count-vs-`F` gap exist (above), but **reachability from the antichain under optimal play is the critical unverified constraint** and no reachable instance was found for `n<=5`.
- **Why small `n` is weak evidence here:** `n<=5` reachable states are few and extension-tight; moreover (as noted on board 15:02Z) `F_FJ(n)=S(n)` through the computable exact range historically relevant, so small cases cannot separate exact-optimal joins from known polynomial framed constructions. `n=6` exhaustive reachable alignment check was not completed here (interrupted run), so the first unchecked small case in this session remains `n=6`.
- **Complexity implication (unchanged, conditional):** sufficiency would make tight/count-feasible joins constructible in principle but would **not by itself** yield a polynomial-size exact-budget framed DAG or `SORT-BOUND-U ∈ NP` without an additional polynomial bound on the number/control of reachable states and joins (the missing polynomial-state invariant for exact-optimal play). A verified reachable counterexample would be a necessity-only separator (soundness/counting vs actual completability) for framed joins, blocking this specific join route; it would not by itself settle `SORT-BOUND-U ∈ NP` or any separation.

## Failed / incomplete approaches

- **Exhaustive `n=6` reachable join search over all alignments:** attempted (`/tmp/opencode/reach6.py`), did not complete (killed, no result). Inconclusive.
- **Direct sufficiency proof from `e(R)<=2^r`:** blocked by the existence of general information-gap posets (`F > ceil(log2 e)`), so any all-`n` sufficiency theorem would have to exploit reachability/optimal-play structure nontrivially.

**Bottom line:** necessity `e(R)<=2^(k-d)` is sound; sufficiency of that counting condition for reachable exact-budget framed joins is **open**. I established (by small explicit computation) that sufficiency fails for general posets but found no reachable counterexample for `n<=5` (all feasible reachable joins collapsed to a parent state). The decisive obstacle is whether optimal-play reachability can ever force an information-gap intersection within the count budget; resolving this for all `n` (or exhibiting one reachable/infinite family counterexample) remains unproved. No theorem-completion claim for `S(n)` or `SORT-BOUND-U` is made.
