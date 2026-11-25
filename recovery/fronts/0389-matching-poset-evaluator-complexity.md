# matching-poset-evaluator-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yWTWpHFxQMUT87ZZbPbU4g-ascending

## exit_state

clearexit

## question

For the extreme matching poset M_n = floor(n/2)C2 disjoint-union A_{n mod 2} from the newest board reduction, is F(M_n) computable uniformly in time 2^{O(n)} (or polynomial in n), improving on the generic 2^{O(n log^2 n)} poset DP, and does the matching-prefix normal form S(n) = floor(n/2) + F(M_n) hold for every n?

## basis

Board #301 matching-prefix post proves F(C2 disjoint-union A_{n-2}) = S(n)-1 and the sandwich S(n)-t <= F(tC2 disjoint-union A_{n-2t}) <= M(n)-t; docs/research-budgeted-dfs.md gives the 2^{O(n log^2 n)} baseline; docs/research-series-decomposition.md covers disjoint-union structure.

## falsifier

Exhibit an all-n lower bound showing that every exact algorithm for F(M_n) needs 2^{Omega(n log n)} time, or compute an n with F(M_n) != S(n) - floor(n/2).

## implication

A 2^{O(n)} evaluator together with the matching-prefix normal form would give the first 2^{O(n)} algorithm for S(n); a lower bound would isolate this structured disjoint-union family as the obstruction and would also refute the normal form.

## finding_unverified

rging optimally, it is a matching-prefix algorithm whenever `n` is odd. The two blocks’ initial pair phases total

`floor(m/2) + floor((n-m)/2) = floor(n/2)`

disjoint comparisons, covering all but one key. So the same algorithm is a strategy from `M_n`, and its total cost `H` satisfies `F(M_n) <= H - floor(n/2)`.

**Consequence at n=47.** The published 200-comparison Ford–Johnson improvement at `n=47` is the split-merge construction (Manacher 1979/1989; Peczarski 2007 studies exactly this class). Front-loading gives

`F(M_47) <= 200 - 23 = 177`,

not the FJ-continuation value `M(47)-23 = 178`. Hence `E_M(47) <= 2`, while `E_FJ(47)=3`. The board’s line `E_M(47)=178-(198-23)=3` uses the FJ upper bound, not the best split-merge value. In particular, **the n=47 FJ non-optimality is not a counterexample to the normal form**: if `S(47)=200`, the sandwich forces `F(M_47)=177` and the normal form holds at 47.

**First genuine open cell.** At `n=23`, `C=75`, `M=76`, `k=11`, `F(M_23) in {64,65}`, `S(23) in {75,76}`. The normal form fails exactly at `(F,S)=(65,75)`. A 64-comparison strategy from `M_23` would prove `S(23)=75` and make the normal form hold there; proving `F(M_23)>=65` alone does not settle `S(23)`. Peczarski’s no-beat-below-47 result says the split-merge class gives nothing at 23, so any counterexample must come from a non-matching-prefix optimal sorter.

## Failed approach / obstruction

I did not obtain an unconditional counterexample or a `2^{Omega(n log n)}` lower bound. The proposed complexity falsifier is not accessible with current techniques: `F(M_n)` is a unary sequence with a `2^{O(n log^2 n)}` evaluator, and an all-algorithm superpolynomial lower bound would be a major complexity separation. Even an exact `F(M_n)` evaluator yields `S(n)` only through the front identity, whose first unresolved instance is the `n=23` cell above.

**Caveat:** I did not open the paywalled Peczarski table, so the exact split/merge numbers at 47 were not independently reproduced. The `F(M_47)<=177` conclusion is conditional on the 200 bound being the cited split-merge construction; if that bound comes from a different algorithm, it needs rechecking. General-poset hardness and certificate soundness were kept separate from completeness.
Recovery audit complete. I did not repeat the prompt or create any new external effects.

**Verified state**
- Host: `billy-dev`
- Working directory: `/home/lubko/soring-fronts/matching-poset-evaluator-complexity`
- Git: clean worktree at `6a96398`; no commits, branches, edits, or Lean changes
- Board #301: exactly **one** matching post from this front, at `2026-11-08T19:07:19.309Z`, titled with the n=47 correction. Digest reports one unique match; no duplicate was posted.
- Durable ledger: `matching-poset-evaluator-complexity` is still `status: running` with no finding recorded. That transition belongs to the keeper; I did not edit it.
- Scratch artifacts only: `/tmp/opencode/matching-poset-evaluator-post.md` and `/tmp/opencode/matching-poset-board-result.json`.

**Unfinished work**
None. The previous turn completed the investigation and posted its finding once: the front-loading lemma, the corrected `F(M_47) <= 177` / `E_M(47) <= 2` bound, the conclusion that the n=47 Ford–Johnson improvement is not a normal-form counterexample, and the precise open `n=23` failure cell `(F,S)=(65,75)`. The honest caveat about the paywalled Peczarski table remains part of that post.

No uncertain external effect requires review.

## Other metadata

```json
{
  "finished_at": 1794164980.841424,
  "started_at": 1794163550.996081
}
```
