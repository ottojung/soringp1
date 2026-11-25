# antonina-KkiYnKoHMDs35AqoKbl8La-study

Session: ses_e45391363ffeOnW0Oh5kP4BVs7
Workspace: /home/lubko/soring-fronts/s-polynomial-size-lp-exact-value
Created: 1794134961347; updated: 1794136915538

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1bac6f00a001YWnXZT4ZvywG0M)

I'll start by studying the repository context, problem definition, and current board state.

## Output 58 (msg_1bac74a3a001gSnOwCjzuEmsz8)

I have the repository context. Now let me examine the literature for LP/decision-tree formulations and the existing board history on this front.

## Output 116 (msg_1bac92397001MsLyM5bydIuj45)

The key structural point is emerging. Let me now test a concrete relaxation: the optimal **average-depth** (fractional/randomized) sorting value, which is the LP value of the natural flow relaxation, and compare it with `S(n)` for small `n`.

## Output 147 (msg_1bacd3437001afYdegVykjvc7Y)

There is prior work on mixed-strategy gaps. I must inspect it before proceeding.

## Output 219 (msg_1bacf5aea001XujqzQL86f2K7v)

I found a promising unconditional obstruction. Let me check whether this randomized/relabeling argument is already known or on the board, and verify the exact computations.

## Output 290 (msg_1bad4ce850017aiotC73qCszw2)

The mathematical picture is now clear. Let me verify the board-posting interface and check the exact ledger entry before writing the report.

## Output 318 (msg_1bad62327001iG37PIIzTul8HS)

There is a prior "avgdepth-obstruction" packet. I must inspect it before claiming the average-depth result.

## Output 425 (msg_1bad83947001vOK6oUYFZGSvHa)

I found the relevant prior front and can now separate the new result from existing average-depth work. Let me draft the board report with the precise theorems and checks.

## Output 533 (msg_1badcd868001qi5y2zcwHfOrOo)

I have a complete, checkable result and have separated it from the prior average-depth front. Posting the report to board #301 now.

## Output 593 (msg_1badf48ea001C1cbzujiBO0OP4)

I caught a scope error in two phrases of the posted report: the lower bound that is open and implies a separation is for *poly-time-coefficient* LPs, not unrestricted polytopes (where the 1-variable counterexample applies). Posting a correction.

## Output 622 (msg_1bae099b4001O4EjY1VuKx3aAy)

**Attacked claim.** The front asks whether, for every `n`, `S(n)` is the exact optimum of a rational LP with `poly(n)` variables/constraints and coefficients computable in `poly(n)` time from `n`. I treated the literal claim and the natural strategy-faithful LP formulation separately.

## Finding 1 — the literal LP question is exactly FP

**Theorem [deduction].** An explicit polynomial-size rational LP family with poly-time-computable coefficients and optimum `S(n)` exists iff `S_unary ∈ FP`.

- If such an LP exists, solve it exactly in polynomial time. Exact rational LP with polynomial-bit data is in P (Khachiyan 1979; Karmarkar 1984; Grötschel–Lovász–Schrijver 1988), giving `S(n)`.
- Conversely, if `S ∈ FP`, use the one-variable LP `max x` subject to `0 ≤ x ≤ S(n)`: two constraints, optimum `S(n)`.

So the front is not an independent LP hypothesis; it is the central `S_unary ∈ FP` / `SORT-BOUND-U ∈ P` question. The nonuniform family is trivial for every `n`, so P/poly sparsity is irrelevant; uniformity of the coefficients is the whole content.

## Finding 2 — the stated falsifier is not viable

The unrestricted statement “every rational polytope whose optimum is `S(n)` for all `n` needs exponentially many facets or variables” is **false**: `[0, S(n)]` with objective `max x` has one variable, two constraints, and optimum `S(n)`. If coefficients must be poly-time computable, then a universal lower bound would prove `S_unary ∉ FP`, hence `SORT-BOUND-U ∉ P`, hence `P ≠ PSPACE` because `SORT-BOUND-U ∈ PSPACE`. So no unconditional extension/facet lower bound of the proposed form is available.

## Finding 3 — the natural LP relaxation has a strict gap for every `n ≥ 3`

This is the substantive structural result. Let `T_n` be the correct deterministic comparison trees and `d_T(π)` the comparisons of `T` on input `π`. Define

`R_rnd(n) = min_{μ ∈ Δ(T_n)} max_{π} Σ_T μ_T d_T(π)`,

the tree-selection LP value / zero-error randomized worst-case expected complexity. Let `f(n) = min_T (1/n!) Σ_π d_T(π)` be the minimum average depth (the board’s `f(n)`).

**Symmetry identity [paper proof].** `R_rnd(n) = f(n)` for every `n`.

- For any distribution `μ`, `max_π E_μ d(π) ≥` the uniform average `= Σ_T μ_T avg(T) ≥ f(n)`.
- Conversely, take `T*` attaining `f(n)`, and randomize by a uniform relabeling `σ ∈ S_n` before running `T*`. For fixed `π`, `σ(π)` is uniform over all `n!` permutations, so the expected depth is exactly `f(n)`.

**Strict gap [paper proof].** For `n ≥ 3`, `f(n) < S(n)`. An optimal height-`S(n)` tree, pruned to be full, has exactly `n!` leaves. If all leaves were at depth `S(n)`, a full binary tree would have `2^{S(n)}` leaves. Since `n!` is not a power of 2 for `n ≥ 3`, some leaf is shallower, so the tree’s average depth is `< S(n)`; hence `f(n) < S(n)`. Moreover `f(n)=W_n/n!` with integer `W_n`, so `S(n)-f(n) ≥ 1/n!`.

Exact values (n≤6 recomputed independently: brute-force closure for n≤5, BFS over 130,023 labeled posets for n=6, matching A001035; n=7,8 from the existing `s-optimal-tree-average-depth-gap` front):

| n | S(n) | f(n) | gap |
|---|---|---|---|
| 3 | 3 | 8/3 | 1/3 |
| 4 | 5 | 14/3 | 1/3 |
| 5 | 7 | 104/15 | 1/15 |
| 6 | 10 | 431/45 | 19/45 |
| 7 | 13 | 3901/315 | 194/315 |
| 8 | 16 | 323/21 | 13/21 |

The smallest explicit counterexample to the natural LP being exact is `n=3`: the tree LP value is `8/3`, while `S(3)=3`.

**Consequence.** The canonical tree-selection IP/LP relaxation cannot be exact for any `n ≥ 3`. More generally, any LP relaxation whose feasible region contains the convex hull of the pure depth vectors has value `≤ f(n) < S(n)` — regardless of size or extended formulation. The same convex argument applies to SDP/SOCP relaxations containing that hull. This is a value gap, not a facet-count bound, so it rules out the whole strategy-faithful class.

## Soundness vs completeness, and general posets

- The tree LP is **sound** for lower bounds: `f(n) ≤ S(n)`, and the uniform input distribution is an optimal adversary certificate for `f(n)`. It is **incomplete**: `f(n) < S(n)` for all `n ≥ 3`, so no dual certificate reaches `S(n)`.
- The integer program is complete, but its LP relaxation is not. A value-encoding LP with optimum `S(n)` is complete by construction, but it is not a strategy relaxation: it certifies a number, not a sorting tree, and collapses to FP if its coefficients are poly-time computable.
- The symmetry proof uses the transitive `S_n` action on the `n!` total orders at the antichain root. For a general poset, `Ext(P)` is not homogeneous, the uniform distribution need not be an optimal adversary, and the antichain conclusion does not transfer. General-poset LP/extension results are therefore not evidence for or against `S(n)`.

## Honest limits

- The literal positive claim is **not disproved**; it is equivalent to `S_unary ∈ FP`, which is open.
- I did not prove any lower bound for **explicit** LPs with poly-time coefficients; that would imply `P ≠ PSPACE`.
- The unconditional gap is only `≥ 1/n!`; the asymptotic size of `S(n)-f(n)` is open.
- `n=7,8` values rely on the cited prior board/literature work, not an independent recomputation here.
- The unrestricted polytope lower bound is false (one-variable interval), and the original board post was corrected on that scope point.

Recorded on board #301 at 11:13Z and 11:16Z (correction). No repository, Lean, test, or ledger changes; the verification scripts were kept only under `/tmp/opencode`.

## Output 742 (msg_1bae457ab001sExoBTZhmQxcLL)

**Recovery audit — no duplicate actions taken.**

- **Board #301:** the front’s report is already posted at `2026-11-08T11:13:35Z`, and the scope correction at `2026-11-08T11:16:20Z`. I did **not** repost either.
- **Git:** the worktree is clean at `6a96398`; no commits, repo files, Lean files, or tests were changed.
- **Scripts:** `/tmp/opencode/lp_sort_probe.py`, `/tmp/opencode/lp_sort_check.py`, and the post draft remain outside the repository. I re-ran the exact checks: `W=16,112,832,6896` for `n=3,4,5,6`, with the `n=6` census at 130,023 labeled posets.
- **Ledger:** `s-polynomial-size-lp-exact-value` is still `status=running`, `exit_state=null`. This is expected: `research_frontier.py` reconciles the entry when the managed agent exits with `clearexit`/terminal status. I did **not** edit the ledger manually, to avoid bypassing the claim-once reconciliation.
- **Provider log:** the previous turn’s final response was emitted; the subsequent failures were provider usage-limit errors, not mathematical or tool failures.

**Mathematical result (unchanged, already recorded).**

1. **Literal LP question = FP.** An explicit polynomial-size rational LP family with poly-time-computable coefficients and optimum `S(n)` exists iff `S_unary ∈ FP`. Exact rational LP is in P; conversely, `0 ≤ x ≤ S(n)`, maximize `x`, is a two-constraint LP.
2. **The stated falsifier is not viable.** The unrestricted facet/variable lower bound is false (`[0,S(n)]` has one variable and two constraints). The poly-time-coefficient version would imply `S_unary ∉ FP`, hence `SORT-BOUND-U ∉ P`, hence `P ≠ PSPACE`.
3. **Strict gap for the natural strategy-faithful LP.** With `R_rnd(n)` the tree-selection LP/randomized worst-case value and `f(n)` the minimum average depth, `R_rnd(n)=f(n)`. For every `n ≥ 3`, `f(n)<S(n)`, so the canonical tree-selection LP relaxation cannot be exact at any `n ≥ 3`, regardless of size. The gap is at least `1/n!`. Exact values through `n=8` are in the board post; the smallest explicit counterexample is `n=3` (`8/3` versus `S(3)=3`).
4. **Soundness vs completeness.** The LP gives a sound lower bound `f(n) ≤ S(n)` (uniform input is an optimal adversary certificate), but it is incomplete. The IP is complete; a value-encoding LP with optimum `S(n)` is complete by construction but is not a strategy certificate and collapses to the FP question.
5. **General posets.** The proof uses the transitive `S_n` action on the antichain’s `n!` total orders. It does not transfer to arbitrary posets, where the uniform extension distribution need not be an optimal adversary.

**Honest limits.** The literal positive claim is not disproved; it is equivalent to the open `S_unary ∈ FP` question. No lower bound for explicit poly-time-coefficient LPs was proved; it would imply `P ≠ PSPACE`. The asymptotic size of `S(n)-f(n)` remains open; `n=7,8` rely on the cited prior board/literature values.

**Status:** all external effects from the interrupted turn are present and verified; no unfinished external action remains. The only pending operational item is keeper reconciliation of the ledger entry on agent exit.
