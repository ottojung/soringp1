# glued-prime-twoply-excess-growth

## status

investigated

## origin

ai_proposal_unverified

## agent_id

D8RqUaiDxaahFi5CCSOacF-cord

## exit_state

clearexit

## question

For the glued height-two lex-prime family R_t with A-to-B-only comparabilities (hence reachable from the antichain in exactly |G| comparisons), does the efficiently computable two-ply adversary bound L2(R_t) minus ceil(log2 e(R_t)) grow without bound as t increases, or does it stay bounded by a fixed constant for all t?

## basis

Board #301 2026-11-10/11: e(R1)=14, e(R2)=1280, e(R3)=366240 independently reproduced (ceil-log 4,11,19), one-ply bounds L0=L1=19 fail to tighten F(R3) in [19,24], and exact DFS with automorphisms plus heuristic search both stall; prior height-two-prime front left F(R3) open and used exact F rather than a computable two-ply bound.

## falsifier

Compute exact e(R_t) and two-ply values L2(R_t) for growing t (first open t=3 with e=366240, L0=L1=19, F in [19,24]) and either show L2(R_t)-ceil(log2 e(R_t)) exceeds any fixed bound or prove it bounded; exact F(R_t) is not required.

## implication

Unbounded two-ply excess on a reachable antichain-derived family would exhibit forced large-excess threshold states without solving exact F, blocking every bounded-excess memoization family; a uniform bound would keep the glued-prime route compatible with bounded-excess evaluators for SORT-BOUND-U.

## finding_unverified

 exactly for `t≤4`; `L1` for `t≤6`. `t=5,6` `L2` not computed (depth-2 over ~10^4–10^5 child states × 2^n extension DP became impractically expensive in this run’s pure-Python scratch; no bound obtained, not a negative result).
- A witnessing root pair for `L1=C` was `(y,a1)` throughout `t≤6` (e.g. `t=5`: children’ `L0` = 38,37 vs `C−1=38`; `t=6`: 49,48), i.e. comparing the global minimum `y` with a gadget minimum `a_i` yields a split with both child log-bounds `≤ C−1` at the root.

## Mathematical finding (honest)
- **Unbounded growth not supported; falsification attempt negative on all tested `t`.** `Δ₂(t)=L2(R_t)-C(R_t)=0` for `t=1..4`, and the weaker one-ply excess `L1(R_t)-C(R_t)=0` for `t=1..6`. In particular no instance with `Δ₂(t)>0` (let alone growing) was found; the posed “grows without bound” alternative is **not observed** and remains unsubstantiated by these data. This is evidence consistent with `Δ₂(t)` (and `L1`-excess) being bounded by the constant `0`, but **not** a proof for all `t`.
- **Structural reason it is nontrivial.** `L1(R_t)=C` ⇔ some incomparable pair splits `e(R_t)=e₁+e₂` with `max(e₁,e₂) ≤ 2^{C−1}`. Since `e/2 ≤ 2^{C−1} < e`, this requires the larger side to stay below the `2^{C−1}` threshold (hardest when `e/2^{C−1}` is close to 2: e.g. `t=1,4` give ratios ≈1.75,1.78, yet balanced splits exist). `L2(R_t)=C` further requires that, for some root move, *both* children admit such a one-ply-balanced continuation. Empirically `(y,a_i)` achieves the root balance for `t≤6`, but I did **not** establish this, nor the child-balance condition, for general `t`.

## What was not achieved / exact obstruction
- **No all-`t` theorem either way.** I neither proved `Δ₂(t) ≤ c` (or `=0`) for all `t`, nor exhibited/proved unbounded growth. Closing the front requires either (i) a uniform argument that some root comparison (and, for `L2`, some response-continuation) keeps every relevant extension split `≤ 2^{⌈log₂ e⌉−p}` as needed for all `t`, or (ii) an explicit family/witnessing argument forcing `Δ₂(t)→∞`. I did not obtain a closed form for `e(R_t)` or a symmetry/majorization argument controlling these splits.
- **Computational limit.** `L2` stalled beyond `t=4` with this exact DP+minimax approach; larger-`t` `L2` (and any search for a first `Δ₂>0`) would need a substantially faster/more structured evaluator (or a different argument). I did not compute exact `F(R_t)` (open already at `t=3`, per board).
- **No primary-literature identification of a named “glued height-two lex-prime / L2” theorem** for this specific family was found in local docs; the family/data were taken from board #301 (independently recomputed where stated). I did not claim NP/P/PSPACE separations or any complexity-class result (and none follow from these comparison counts).

## Bottom line
**Concrete failed approach to refute boundedness:** direct exact computation of the two-ply adversary excess `L2(R_t)-⎡log₂ e(R_t)⎤`. It yields `0` for `t=1..4` (and one-ply excess `0` for `t=1..6`, e.g. `e(R5)=296,862,720,000`, `C=39`, `L1=39`; `e(R6)=627,388,489,728,000`, `C=50`, `L1=50`), so it provides **no falsifier** of a uniform constant bound and no evidence of unbounded growth. The all-`t` bounded-vs-unbounded question for `Δ₂` remains **open**; the precise obstruction is the lack of a general proof controlling one-/two-ply extension splits for this glued family (with `L2` computation itself infeasible here beyond `t=4`). No repository or Lean changes were made.

## Other metadata

```json
{
  "finished_at": 1794434603.284455,
  "started_at": 1794426077.8016481
}
```
