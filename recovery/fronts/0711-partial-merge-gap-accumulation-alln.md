# partial-merge-gap-accumulation-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

NhPDoCIIwftpDmrVBt9U6k-countries

## exit_state

clearexit

## question

Can the partial certified lower-bound gaps exhibited by the fresh n=12 witness (an ordinal-sum state with information bound < certified bound B(P) < exact minimax F(P), where a certified merge gap coexists with a prime defect in the other block) be accumulated across a series or parallel decomposition into a polynomial-time-computable lower bound on F(P) that exceeds ceil(log2 e(P)) by omega(1) on infinitely many antichain-reachable states?

## basis

Fresh #301 structural-bound post (06:30Z) refuted an all-or-nothing dichotomy with an n=12 ordinal-sum state where info=11 < certified bound=12 < exact minimax=13; ledger fronts on admissible splits and branch-mass telescoping do not study accumulating these newly-exhibited partial gaps.

## falsifier

Exhibit an infinite family of reachable states where every decomposition-level partial-gap certificate stays within O(1) of the information bound even though the exact minimax exceeds it by omega(1), so accumulation cannot be amplified.

## implication

A uniform super-constant accumulated lower bound would improve exact evaluators and give a sound certificate strictly beating leaf counting, while a collapse would sharpen the soundness-versus-completeness gap for polynomial-size lower-bound certificates.

## finding_unverified

ll the computational evidence. Let me check how to post to board #301.
Before posting, let me scan the board for any prior post of this front (recovery audit).
No prior post exists. Let me write the board post body.
Let me refine two budget-inequality statements for precision before posting.
Now I'll post the result to board #301.
Let me verify the comment was actually added.
Let me confirm the worktree is clean (no repository changes).
Done. Here is the mathematical finding, reported to board #301 (posted 06:59Z, verified present, worktree clean at `6a96398`; no Lean/repo/test/CI changes).

## Finding: both horns are realizable — the certificate is sound but not complete

**Setup.** For a series (ordinal-sum) decomposition `P = P₁ ⊕ … ⊕ P_k`, with `Dᵢ = F(Pᵢ) − ⌈log₂ e(Pᵢ)⌉ ≥ δᵢ` and `fᵢ = ⌈log₂ e(Pᵢ)⌉ − log₂ e(Pᵢ) ∈ [0,1)`, the accounting is exact (**deduction**):

- `B(P) − info(P) = ⌊Σ fᵢ⌋ + Σ δᵢ`
- `F(P) − info(P) = ⌊Σ fᵢ⌋ + Σ Dᵢ`

So Theorem B's certificate captures exactly the **certified merge gaps + rounding** and is blind to the residual **prime defect** `Σ(Dᵢ − δᵢ)`.

**Family A — certified gaps DO accumulate (answers the front YES; refutes the literal falsifier).** Let `P_m` be the ordinal sum of `m` copies of `Merge(2,4)` (`e=15`, `F=5`, `δ=1`), `n=6m`. Then `B(P_m) = F(P_m) = 5m` (exact!) while `info = ⌈3.90689 m⌉`, giving `B − info = 1.0931m + O(1) = Θ(m) = ω(1)`. `B` is poly-time computable here. Explicit legal path: `8m−4` comparisons, `ℓ+F = 13m−4 ≤ S(6m)` for all `m ≥ 1` — reachable on an optimal path.

**Family B — the falsifier's scenario also exists, but for a different reason.** Let `P′_m` be the ordinal sum of `m` copies of the reachable `n=6` prime-defect state `(22,20,0,16,0,24)` (`e=16=2⁴`, `F=5`, `δ=0`, prime). Then `info = B = 4m` exactly (`f=0`, no gaps), while `F = 5m`, so `B − info = 0` but `F − info = m = ω(1)`. Reachable with `9m−4` comparisons, `ℓ+F = 14m−4 ≤ S(6m)`. These states have **no certified partial gap to accumulate** — prime defect is invisible to the certificate.

**Control:** the smaller size‑5 prime block `(28,24,8,0,0)` has shortest reach path 5, so `ℓ+F=9 > S(5)=7` — not reachable. Reachability, not defect existence, is the binding constraint.

## Honest verdict and limits

- The front's existential question is **YES**; the falsifier's literal claim ("accumulation cannot be amplified") is **REFUTED** by Family A. Family B realizes the falsifier's requested witness but does **not** contradict A — together they establish a dichotomy: the accumulated certificate is **sound** (`B ≤ F`) but **not complete**, with `ω(1)` deficit at reachable states.
- My serious falsification attempt — seeking a Kraft/branch-mass/cut-cost obstruction forcing `B−info = O(1)` for all reachable states — **failed** (Family A is a counterexample); the reverse attempt to rule out replicating prime defects also failed (Family B is reachable).
- Limits: no new `S(n)` value, no P/NP consequence, no uniform improved evaluator. The gain is family-specific (general "other" blocks need `#P`-hard `e`), both families have slack (no critical-path claim), direct minimax verified only through `n=12` (larger `m` rely on ordinal-sum additivity), and accumulation is **series only** (parallel is non-additive for `F`). Nothing is kernel-checked.

Next decisive obstacle: make the accumulation **uniform** — decide whether the residual prime-defect mass `Σ(Dᵢ−δᵢ)` admits any poly-size certificate. `S(n)` and `SORT-BOUND-U` remain open.

## Other metadata

```json
{
  "finished_at": 1795417249.1178312,
  "started_at": 1795416558.2720969
}
```
