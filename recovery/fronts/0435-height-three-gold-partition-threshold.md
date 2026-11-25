# height-three-gold-partition-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

54mt6l3z3OSfQvBhU78Uvn-pondered

## exit_state

clearexit

## question

Does every finite poset of height at most three satisfy the Gold Partition inequality e(P) >= F_{m(P)+2}, so that the Fibonacci extension threshold T(r)=F_{r+3}-1 holds throughout height three for every r?

## basis

Board #301 t10-census-232 and the universal-Fibonacci thread; Peczarski, Order 23 (2006); Gupta, arXiv:2607.23926 (GPC through fourteen elements); the height-two GPC front; no ledger front covers height three.

## falsifier

Exhibit an explicit height-three poset with e(P) < F_{m(P)+2}, certified by exact integer linear-extension counting and exact minimax; the reported GPC census through fourteen elements forces any such counterexample to have at least fifteen elements.

## implication

A positive all-n theorem extends the Fibonacci threshold to the first unbounded-width, unbounded-dimension height class above height two and tests whether extension-count pruning is height-limited; a counterexample locates the minimal height at which GPC and that sound pruning rule fail.

## finding_unverified

**Recovery.** Worktree is clean at `6a96398` on billy-dev. No prior #301 post existed for this front. The only external effect was one new #301 comment at `2026-11-09T12:28:10Z`; no duplicate, commit, Lean file, or repository change.

**Mathematical finding (posted to #301).**

Let `P` have height exactly three, with height levels `A,B,C` of sizes `a,b,c`. Every concatenation of level orders is a linear extension, so

\[
e(P)\ge a!b!c!\ge e_{\min}(n),
\]

where `e_min(n)` is the balanced minimum. Also `m(P) ≤ S(n) ≤ FJ(n)`, the Ford–Johnson bound.

An exact integer check for `85 ≤ n ≤ 20000` gives

\[
e_{\min}(n)>F_{FJ(n)+2},
\]

and the Stirling/FJ margin is positive and increasing beyond `20000`. Therefore **every height-three poset on at least 85 elements satisfies `e(P) ≥ F_{m(P)+2}`**. Gupta’s GPC census through 14 elements, combined with the board’s GPC ⇒ Fibonacci induction, excludes `n ≤ 14`. Hence a height-three counterexample can only have

\[
\boxed{15\le |P|\le 84}.
\]

This is a real finite reduction, not an all-`n` theorem.

**Falsification attempt.** No counterexample was found. I checked:

- Complete ordinal sums `A_a ⊕ A_b ⊕ A_c`, where `e=a!b!c!` is minimal and `m=S(a)+S(b)+S(c)` exactly: no violation for any split with `15≤n≤200`, with the asymptotic tail also safe.
- One-relation deletion from `A_4⊕A_4⊕A_4`: `e=14688`, exact `m=15`, `F_17=1597`.
- `W_5⊔W_5`: `e=16128`, exact `m=15`; `W_4⊔W_4`: `e=1750`, exact `m=12`.
- Random layered height-three posets at `n=9`: no ratio above `0.14`.

**Exact obstruction.** The level-counting proof closes `n≥85` but not `15..84` because it treats extensions and merge depth independently. The complete ordinal sum minimizes `e` but has small `m=S(a)+S(b)+S(c)`; deleting cross relations raises `e` and the three-list merge cost together. Closing the remaining window needs a quantitative trade-off between missing cross relations and merge depth, or a new GPC class covering height three. Height-two GPC and lexicographic-sum preservation do not supply this.

**Honest limits.** No all-`n` proof and no counterexample. The `n≤14` input relies on Gupta’s preprint and the Peczarski/height-two literature. The window `15..84` was not exhaustively searched; exact minimax at `n=15` near-ordinal states exceeded the local budget. No Lean or repository change was made.
Recovery inspection completed; no action was repeated.

- **Git:** worktree clean at `6a96398`; no commits, branches, or repository files were created.
- **Board #301:** exactly one post exists for this front, at `2026-11-09T12:28:10.968Z`, author `SoringP1 frontier: height-three-gold-partition-threshold`. I did not repost it.
- **Durable ledger:** the front is still `running` with no `finding_unverified`/`finished_at`; this is keeper-managed, so I did not edit it manually.
- **Scratch artifacts:** only under `/tmp/opencode/h3gpc/`.

There is no unfinished mathematical work from the prior turn. The reported result remains:

- height-three Fibonacci inequality holds for all `n ≥ 85` by the level-factorial lower bound `e(P) ≥ a!b!c!` and `m(P) ≤ S(n) ≤ FJ(n)`;
- `n ≤ 14` is covered by Gupta’s GPC census through 14 elements plus the GPC ⇒ Fibonacci deduction;
- the unresolved finite window is `15 ≤ |P| ≤ 84`;
- no counterexample was found, and the exact obstruction is the missing trade-off between deleted cross-relations (raising `e`) and the three-level merge depth (raising `m`).

No further external side effects are needed.

## Other metadata

```json
{
  "finished_at": 1794227404.6228435,
  "started_at": 1794225186.3283556
}
```
