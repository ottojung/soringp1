# antonina-Zq3jaGw7rAcKjwPGzDEiIa-religion

Session: ses_df5c44790ffeehTO6Jkqp3lVIT
Workspace: /home/lubko/soring-fronts/annotated-deck-state-count-exponent-alln
Created: 1795468015795; updated: 1795469713621

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20a3bba4c001NpDc71TgsXwpY1)

I'll start by understanding the environment and the referenced materials. Let me explore in parallel.

## Output 25 (msg_20a3bc6870010BENTngXRHnE2A)

I'm on the `billy-dev` branch as required, clean worktree. Let me read the board digest and remaining reference materials.

## Output 44 (msg_20a3bd95e001NFpP6WGIWvVgnN)

Let me find the exact front definition in the ledger and check for prior work on this slug.

## Output 59 (msg_20a3becb20013VsoLp9Jo2ZGbb)

I need the precise definition of Dstar(P). Let me pull the full board posts that define it.

## Output 97 (msg_20a3c2e3100127Lafgm6pe6Gga)

I now understand the setup. Let me check for prior scratch work on this slug and available tooling, and read the research plan.

## Output 112 (msg_20a3cbbd0001hWzTJMVnI0EmZW)

Prior scratch exists from other agents. Let me read the winning-frontier barrier (highly relevant) and the prior deck audit code to nail the exact definition and avoid duplication.

## Output 123 (msg_20a3cce25001h0ZJhJr6SR6tDS)

Let me inspect the prior deck code for the exact definition, find the board-posting mechanism, and check literature availability.

## Output 138 (msg_20a3dabbd001KFvjC5nalLClFa)

Let me look at the posting mechanism and gather primary literature grounding in parallel.

## Output 175 (msg_20a3e14e1001SAcioCeMTAttXQ)

I have what I need on definitions. Let me build a from-scratch computation engine for nonisomorphic posets, decks, and F values, testing it first against known poset counts.

## Output 433 (msg_20a428a4a001qIVSDpuihfGV3R)

Found the bug: canonical forms were computed with global `N` fixed at target size while enumerating smaller levels. Let me fix the level-wise `N`.

## Output 467 (msg_20a42f212001nqj3m7iT0acghH)

The construction used a down-set condition but the new element is placed *below* S, so S must be an up-set. Fixing.

## Output 485 (msg_20a43c412001F2UuZsRAw1qfi2)

Counts now match A000112 exactly through n=9. Let me extend to compute e, F, decks, and the reachable-state census.

## Output 519 (msg_20a446316001aD0THgyBy7o795)

Independent computation reproduces Adec(6)=155, Adec(7)=915 with zero mixed-F groups. Let me push to n=8 and n=9.

## Output 571 (msg_20a54bc72001fRYSzW5146i80V)

## Recovery audit

- **Host/branch/worktree**: `billy-dev`, branch `billy-dev` at `6a96398d937d20977a91b9afa8619cb27feab269`, `git status --short --branch` clean before and after.
- **External side effects**: none performed by me. No board post/comment, no commit, no push, no PR, no Antonina action, no ledger/case/CI/test/Lean change. I searched board #301 for `annotated-deck` (0 matches on page 1) and `Dstar` (0 matches). A prior Viche Executive post (2026-11-23T20:45:00Z) independently verified the `n<=7` child-(e,F)-deck F-completeness census; I did not duplicate it.
- **Interrupted local work**: an `n=9` unlabelled-poset deck census in `/tmp/opencode/annotated_deck_20261123/` was killed by `SIGKILL` (likely memory/time on this host). I did not rerun it. All reported numbers below are from completed runs `n<=8`.

## Front

`annotated-deck-state-count-exponent-alln` (ledger `running`, agent `Zq3jaGw7rAcKjwPGzDEiIa-religion`).

> Let `Adec(n)` be the number of distinct `(e,F)`-annotated one-step child decks `Dstar(P)` as `P` ranges over all poset states on `n` labelled elements, and let `Adec^reach(n)` be the same count restricted to states reachable in the budgeted minimax game at budget `S(n)`. Is `Adec^reach(n) = 2^{o(n log^2 n)}` for all `n`, or does `Adec(n)` grow at least `2^{Omega(n log^2 n)}` along an infinite family?

## Definitions used (checked against board/problem model)

- `P`: finite poset on `[n]`, represented by transitive closure. `[definition]`
- `e(P)`: number of linear extensions. `[definition]`
- `F(P)=0` if `P` total, else `F(P)=1+min_{(x,y) incomparable} max(F(P+x<y),F(P+y<x))`; `S(n)=F(antichain_n)`. `[definition, matches problem.md / minimax model]`
- One-step child: either orientation of an incomparable pair, transitively closed. `[definition]`
- `Dstar(P) = (e(P), sort(multiset{(e(C),F(C)) : C is a one-step child of P}))`. This matches the board's "child (e,F)-deck" / `Dstar` usage (Viche Executive 20:45Z: “grouping ... by (e(P), multiset of child (e(C),F(C)) over both orientations of every incomparable pair)”). `[definition, board-aligned]`
- `Adec(n)`: number of distinct `Dstar(P)` over all **unlabelled** `n`-element posets `P`. (Unlabelled is the right quotient for state-count; labelled would inflate by `n!` orbit factors but not change the exponent question at `n log^2 n` scale.)
- `Adec^reach_tight(n)`: same, restricted to states with `delta(P)+F(P)=S(n)`, where `delta(P)` is minimum comparisons from antichain to reach `P` by legal one-step outcomes. This is the tight/optimal-budget reachable set. **Caveat**: the front text says “reachable in the budgeted minimax game at budget `S(n)`”; depending on convention that can mean `delta(P)+F(P)<=S(n)` along some winning play or the tight equality. I report the tight equality, which is the stricter/standard “on an optimal play” proxy; it gives `Adec^reach_tight <= Adec^reach_budget` in general. `[definition/caveat]`

## Method (from-scratch, reproducible in /tmp, no repo change)

- Enumerated unlabelled posets by the standard maximal-element/up-set extension, with lex-min adjacency-matrix canonicalization by individualisation/refinement. Sanity: counts match A000112 for `n=1..9` (`1,2,5,16,63,318,2045,16999,183231`); `n=9` enumeration completed but the downstream deck census was SIGKILLed. `[experiment]`
- `e(P)` by ideal/downset DP over subsets (`2^n` states). `[experiment]`
- `F(P)` by memoized minimax on the unlabelled-poset DAG, processing states in descending relation-count order so children are ready. Sanity: `S(6)=10`, `S(7)=13`, `S(8)=16`, matching literature/problem baseline. `[experiment]`
- For each state, formed `Dstar(P)` from all incomparable-pair child orientations, canonicalized children to unlabelled keys, sorted the annotated child multiset, and grouped by exact deck key. `[experiment]`
- Reachability proxy `delta` by BFS over legal comparison outcomes from antichain. `[experiment]`

Code was compiled with system GCC toolchain in Guix store; scratch only under `/tmp/opencode/annotated_deck_20261123/`. No external artifact reused.

## Results (small n)

| n | A000112 unlabelled posets | S(n) | Adec(n) | mixed-F deck groups, all | Adec^reach_tight(n) | tight states | mixed-F, tight |
|---:|---::|---:|---:|---:|---:|---:|---:|
| 6 | 318 | 10 | 155 | 0 | 48 | 86 | 0 |
| 7 | 2045 | 13 | 915 | 0 | 222 | 440 | 0 |
| 8 | 16999 | 16 | 7569 | 0 | 1330 | 2705 | 0 |

Ratios (experiment, only 3 points, **not** asymptotic evidence):

| n | log2 Adec(n) | log2 Adec / (n log2^2 n) | log2 Adec^reach_tight / (n log2^2 n) |
|---:|---:|---:|---:|
| 6 | 7.276 | 0.1815 | 0.1393 |
| 7 | 9.838 | 0.1783 | 0.1413 |
| 8 | 12.886 | 0.1790 | 0.1441 |

## Mathematical findings

1. **Dstar F-completeness confirmation, n<=8 (experiment; extends board n<=7).** Every observed deck group has a single `F` value: `Dstar(P)` determines `F(P)` for all unlabelled posets on `n<=8`, and also on the tight reachable subset. This confirms the Viche Executive 20:45Z independent n<=7 verification and extends it by one size. It is **not** an all-`n` theorem; the board already records the all-`n` question as open and notes no mixed-F obstruction found. `[experiment]`

2. **Trivial upper bound (deduction).** Since `Dstar` is a function of the unlabelled poset, `Adec^reach_tight(n) <= Adec(n) <= A000112(n)`. Kleitman–Rothschild give `A000112(n)=2^{n^2/4 + 3n/2 + O(log n)}`. Therefore
   `Adec(n) <= 2^{O(n^2)}`.
   This upper bound is **above** the `2^{O(n log^2 n)}` threshold: it does **not** imply the subexponent horn, and it is consistent with either horn. `[deduction, literature: Kleitman–Rothschild asymptotic for posets]`

3. **No nontrivial all-n lower bound proved (obstruction).** Proving `Adec(n) >= 2^{c n log^2 n}` would require exhibiting, for infinitely many `n`, that many nonisomorphic posets have pairwise distinct `(e,F)`-annotated child decks. Distinct posets can share invariants (the board has many e/F-collision examples), so A000112 is not a lower bound. I did not find a constructive infinite family forcing distinct `Dstar` at the needed rate. Conversely, proving `Adec^reach(n)=2^{o(n log^2 n)}` would require a uniform deck-collision/compression argument; I did not find one. `[obstruction]`

4. **Small-n data is inconclusive for the exponent question.** The `n=6..8` ratios `log2(Adec)/(n log2^2 n) ~ 0.179` are stable but cover only three tiny sizes; this cannot distinguish `2^{Theta(n log^2 n)}`, `2^{Theta(n^2)}`, or intermediate growth. The relevant comparison is `2^{O(n log^2 n)}` current exact-evaluation time (problem.md) versus poset-space `2^{Theta(n^2)}`: the deck count sits between “same as all posets” and “small enough to explain the evaluator” and is unresolved here. `[experiment + deduction]`

## Why this does not settle the front

- **No all-n theorem either way.** Neither the `2^{o(n log^2 n)}` upper horn nor the `2^{Omega(n log^2 n)}` lower horn is proved.
- **No evaluator improvement.** Even a subexponent `Adec^reach` count would only “support/open a route” if one also has a way to enumerate/transition by deck classes efficiently and prove `Dstar`-completeness of F for the relevant states; I have not produced such an evaluator. The front already states this implication boundary.
- **No complexity-class separation.** As the front notes, neither horn by itself separates complexity classes or proves a new `S(n)` value.
- **Reachability notion caveat.** I used tight `delta+F==S(n)`. A looser budget-reachable definition could make `Adec^reach` larger; a stricter actual-play definition could make it smaller. The all-n exponent question should pin this down.
- **n=9 incomplete.** The n=9 unlabelled enumeration completed (183231 classes, matching A000112) but deck/F census was killed by SIGKILL; no n=9 Adec number is reported.

## Concrete next falsification target

A decisive next step would be either (a) a rigorous counting/lower-bound argument producing `2^{c n log^2 n}` distinct reachable `Dstar` values on an explicit family (even a general-poset family, clearly labelled as such, would be a barrier signal but would not directly settle the reachable-S(n) question), or (b) a provable compression of `Dstar` classes on the tight reachable set below `2^{o(n log^2 n)}` together with a sound transition argument. Small-n enumeration beyond n=8 should use a memory-efficient streaming/indexed representation rather than holding full per-state deck objects in maps.
