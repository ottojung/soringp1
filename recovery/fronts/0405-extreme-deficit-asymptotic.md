# extreme-deficit-asymptotic

## status

investigated

## origin

ai_proposal_unverified

## agent_id

TvoyX6oZHijnDMC2lYSX2A-latest

## exit_state

clearexit

## question

Is the extreme-move deficit D(n)=S(n)-R(n) of the n-element antichain o(n) for every n, or is liminf_{n->infinity} D(n)/n strictly positive, where R(n) is the minimum over height-S(n) trees of the maximum number of non-extreme comparisons on a root-leaf path?

## basis

Board #301 extreme-move-deficit-sortnumber status-loss lemma, the independently checked sandwich S(n)-2n+2<=R(n)<=S(n), and its exact small R values.

## falsifier

Prove an all-n upper bound D(n)<=g(n) with g(n)=o(n), or exhibit an infinite family n_i with certified D(n_i)>=c n_i for a fixed c>0.

## implication

If D(n)=o(n), asymptotically optimal trees can be made almost entirely from extreme comparisons, constraining adversary lower bounds; if D(n)=Theta(n), the status-loss budget is asymptotically necessary and extreme-only minimax DPs lose a linear fraction of optimal height.

## finding_unverified

h, or on “every optimal path must carry `n-1` extreme comparisons,” cannot settle either horn.

I also tested the two most natural all-poset potentials for a linear lower bound:

- `g(P)=floor((|Min(P)|+|Max(P)|-2)/2)`: fails at `n=6`; states with `|Min|+|Max|=4`, `F(P)=4`, `W(P)=0 < g(P)=1`.
- `W(P) >= c(P)-1`, with `c(P)` the number of comparability components: fails already at `n=7`; `74,550` violating visited states, e.g. `W(P)=0`, `c(P)=2`. Even restricting to disjoint unions of chains leaves `10,290` violations.

Here `W(P)=F(P)-R(P)` is the max–min game value at `P`. Thus neither status loss nor component count supplies the missing induction.

## Model-fidelity correction

Under the stated definitions the front’s complexity implication for the `o(n)` horn is inverted. Since `R` counts **non-extreme** comparisons and `D=S−R`:

- `D(n)=o(n)` means the critical path is almost entirely **non-extreme** (`e=o(n)` extreme), not almost entirely extreme.
- `D(n)=Theta(n)` means `Theta(n)` extreme comparisons on the critical path, still only a `1/log n` fraction of `S(n)`.

Also, “`D=o(n)`” versus “`liminf D/n>0`” is not exhaustive without a convergence/monotonicity assumption; `liminf=0` alone only gives an infinite subsequence with `D/n -> 0`.

## Honest limits

The all-`n` dichotomy remains **open**. The only all-`n` bound established remains

\[
0 \le D(n) \le 2n-2.
\]

The status-loss lemma is general-poset **soundness**; it does not give completeness of extreme-only trees at height `S`. No general-poset hardness is transferred to the antichain. The precise remaining obstacle is a new invariant stronger than `Min`/`Max` or component count, or an all-`n` construction of an optimal tree whose long paths all carry only `o(n)` extreme comparisons.

Board #301 now records the main finding (`2026-11-08T23:52Z`) and the `n=7` potential counterexample addendum (`2026-11-08T23:58Z`). No repository or Lean changes were made.
## Recovery audit complete

I did not repeat the research prompt or create any new external effects.

**Effects confirmed to have happened**
- Two board #301 comments by `SoringP1 frontier: extreme-deficit-asymptotic`:
  - main finding: `2026-11-08T23:52:35.964Z`
  - addendum on the failed component potential: `2026-11-08T23:58:01.185Z`
- I checked pages 1–10: exactly these **two** posts exist from this front. No duplicate was posted.
- Viche independently checked the table through `n=6` and confirmed the model-fidelity/quantifier warnings. It explicitly did **not** recompute `R(7)=5` or the two obstruction computations.

**Effects confirmed not to have happened**
- No repository change: `git status --porcelain` is empty.
- No commit: `HEAD` is still `6a96398d937d20977a91b9afa8619cb27feab269`.
- No Lean, test, note, or source-file modification.
- No new board post was made during this recovery turn.

**Durable record state**
- The frontier ledger still shows `extreme-deficit-asymptotic` as `status: running`. That is the normal pre-exit state; the keeper reconciles it from the agent exit, so I did not edit it manually.

**Remaining uncertainty / honest limit**
- The new value `R(7)=5`, `D(7)=8` is supported by our two independent exact DPs, but has not been recomputed by an independent reviewer because of state-space size.
- The two obstruction counterexamples (`Min`/`Max` potential at `n=6`, component potential at `n=7`) are likewise recorded but not independently reproduced by Viche.

No unfinished external action remains.

## Other metadata

```json
{
  "finished_at": 1794182374.464239,
  "started_at": 1794180599.7753615
}
```
