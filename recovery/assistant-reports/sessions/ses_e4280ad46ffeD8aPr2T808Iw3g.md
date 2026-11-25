# antonina-TvoyX6oZHijnDMC2lYSX2A-latest

Session: ses_e4280ad46ffeD8aPr2T808Iw3g
Workspace: /home/lubko/soring-fronts/extreme-deficit-asymptotic
Created: 1794180600653; updated: 1794182349854

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 553 (msg_1bd9908f800147LdAULzVtJp3y)

## Recovery / side-effect audit

I inspected the checkout, Git state, durable ledger, and board #301 before doing anything. The prior turn’s board post was for the **older** front `extreme-move-deficit-sortnumber`; no post existed for the current front `extreme-deficit-asymptotic`. I did not duplicate it. Repository worktree stayed clean, no commit or Lean change was made. I posted **one** finding plus **one** addendum for this front.

## Mathematical finding

New exact values, computed by two independent exact DPs (different state encodings, both reproducing the independently checked values through `n=6`):

| n | S(n) | R(n) | D(n)=S−R |
|---|---:|---:|---:|
| 2 | 1 | 0 | 1 |
| 3 | 3 | 0 | 3 |
| 4 | 5 | 1 | 4 |
| 5 | 7 | 3 | 4 |
| 6 | 10 | 4 | 6 |
| 7 | 13 | 5 | **8** |

So `R(7)=5`, `D(7)=8`, and `D(7)/7>1`. This is consistent with the `liminf D(n)/n>0` horn, but it is **not** an asymptotic proof.

## Concrete failed approach / exact obstruction

The natural proof route is to show that every optimal path has many extreme comparisons. That is false in the needed strong form. For `n=6`, `S=10`, there is a full path inside an optimal height-10 tree with comparison/outcome sequence

`(0,1,<),(2,3,<),(0,2,<),(2,4,<),(2,5,<),(3,4,<),(1,3,<),(1,2,>),(3,5,>),(1,5,<)`

using only **4** extreme comparisons and **6** non-extreme comparisons. It is genuinely optimal-tree-compatible: at every prefix both children satisfy `F <= remaining-1`. Yet

\[
D(6)=\max_T \min_{p} (e(p)+\mathrm{slack}(p))=6.
\]

So `D` is a genuine **max–min over trees**, not a minimum over paths. Any argument based on one cheap compatible path, or on “every optimal path must carry `n-1` extreme comparisons,” cannot settle either horn.

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

## Output 609 (msg_1bd99f152001m72zYYs6vrjCQC)

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
