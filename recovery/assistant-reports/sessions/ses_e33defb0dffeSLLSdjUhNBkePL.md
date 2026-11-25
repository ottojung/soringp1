# antonina-D8RqUaiDxaahFi5CCSOacF-cord

Session: ses_e33defb0dffeSLLSdjUhNBkePL
Workspace: /home/lubko/soring-fronts/glued-prime-twoply-excess-growth
Created: 1794426078626; updated: 1794434574789

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 221 (msg_1cca1a64a001ZtFh4JbmswRlFe)

## Recovery / state check (billy-dev)
- Inspected `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-frontier.json`, git state, and board #301 via `/home/lubko/.local/bin/antonina board show` (read-only). CWD is the front checkout `/home/lubko/soring-fronts/glued-prime-twoply-excess-growth` (git `billy-dev @ 6a96398`, working tree clean). No prior local artifacts for this question found; ledger shows related seed fronts investigated but no `glued-prime-twoply-excess-growth` result. No board post, commit, PR, or other external side effect was made by this run (report only).

## Question attacked (falsifiable, all-`t`)
For the glued height-two lex-prime family `R_t` (A-to-B-only comparabilities, hence reachable as a state consistent with `|G|` discovered A–B relations), does
`Δ₂(t) := L2(R_t) - ⎡log₂ e(R_t)⎤`
grow without bound in `t`, or stay bounded by a fixed constant for all `t`?

**Complexity implication (as stated).** Unbounded `Δ₂` on a reachable antichain-derived family would exhibit forced large-excess threshold states without solving exact `F`, blocking every bounded-excess memoization family; a uniform bound would keep this glued-prime route compatible with bounded-excess evaluators for `SORT-BOUND-U`. (I did not derive a new complexity consequence beyond this conditional implication.)

## Definitions recovered and fixed [definition, from board #301 + independent check]
From the 2026-11-10 #301 posts “height-two-prime-excess-boundedness” (Exec-verified 2026-11-10T14:13:40Z) and “glued-R3-exact-minimax” (independently re-verified here for the used `t`):
- `R_t` (height 2, prime, A-to-B-only): `A={y,a1,…,at}`, `B={x,b1,c1,…,bt,ct}`, `m=|A|=t+1`, `k=|B|=2t+1`, `n=3t+2`, `|G|=4t+1`.
  Comparabilities: `y < z` for all `z∈B`; `a_i < b_i, a_i < c_i` for each `i`; no other cross pairs (in particular `a_i ⊀ x`, no cross-copy edges, no A–A/B–B). All comparabilities are A-to-B.
- `e(P)` = #linear extensions, `C(P)=L0(P)=⎡log₂ e(P)⎤` (information/leaf bound), `F(P)` exact minimax comparison cost.
- `L1(P)=0` if total, else `1 + min_{(u,v) incomparable} max(L0(P|u<v), L0(P|v<u))` (one-ply adversary/information bound).
- `L2(P)=0` if total, else `1 + min_{(u,v) incomparable} max(L1(P|u<v), L1(P|v<u))` (two-ply adversary bound: minimax to depth 2 with `L0` at leaves). This is the standard depth-2 strengthening with the usual monotonicity giving `L0 ≤ L1 ≤ L2 ≤ F` (general deduction, cf. the one-ply argument in `docs/research-one-ply-obstruction.md`).

I did **not** find a prior local definition/computation of `L2` in-repo; the above is the natural “efficiently computable two-ply adversary bound” consistent with the prompt’s `L0/L1` usage (and I state this assumption explicitly). Correctness of the *values below* is relative to this definition.

## Computation (exact, reproducible scratch) [experiment]
Method: explicit transitive-closure poset states; exact `e(P)` by subset/ideal DP `e(S)=∑_{v minimal in S} e(S\{v})` (2^n states, exact, no sampling); `L0/L1/L2` by the recurrences above with memoization of `e`. Independent re-verification: `e(R1..R4)=(14,1280,366240,238801920)` and `C=(4,11,19,28)` match the Exec-verified board values exactly.

| t | n | \|G\| | e(R_t) | C=L0 | L1 | L1−C | L2 | L2−C |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5  | 5  | 14              | 4  | 4  | 0 | 4  | 0 |
| 2 | 8  | 9  | 1,280           | 11 | 11 | 0 | 11 | 0 |
| 3 | 11 | 13 | 366,240         | 19 | 19 | 0 | 19 | 0 |
| 4 | 14 | 17 | 238,801,920     | 28 | 28 | 0 | 28 | 0 |
| 5 | 17 | 21 | 296,862,720,000 | 39 | 39 | 0 | —  | — |
| 6 | 20 | 25 | 627,388,489,728,000 | 50 | 50 | 0 | —  | — |

- `L2` computed exactly for `t≤4`; `L1` for `t≤6`. `t=5,6` `L2` not computed (depth-2 over ~10^4–10^5 child states × 2^n extension DP became impractically expensive in this run’s pure-Python scratch; no bound obtained, not a negative result).
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
