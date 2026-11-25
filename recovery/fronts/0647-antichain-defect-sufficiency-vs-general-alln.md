# antichain-defect-sufficiency-vs-general-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Ua2y0n2a2z5K5Nm6Ohcud3-polygamy

## exit_state

clearexit

## question

Does the antichain-only superadditivity bound S(a+b) >= S(a)+S(b)+min(a,b)+1 logically imply the general disjoint-union defect inequality F(A u B) >= F(A)+F(B)+min(|A|,|B|)+1 for arbitrary finite posets A,B, or is the general statement strictly stronger than anything needed for exact unary S(n)?

## basis

Newest #301 potential no-go applies to arbitrary cross-augmented states; the antichain root is the only family bearing on S(n); AGENTS.md bars general-poset hardness from transferring without an encoding-preserving reduction.

## falsifier

Separate the two statements: exhibit posets A,B whose defect falls below min+1 while every antichain split satisfies the bound, or prove that refinement monotonicity carries the antichain case to arbitrary A and B.

## implication

Determines whether the board's general-poset defect campaign is necessary for S(n) or reducible to antichain data, and draws the soundness/completeness line between general minimax theorems and the fixed antichain root.

## finding_unverified

fting a single report, and verify my key numbers once more.
I have a solid finding. Before posting, let me re-confirm no prior post under my exact author tag, then post exactly once.
## Recovery & side-effect audit

- Worktree clean on `billy-dev` at `6a96398`; no repo/Lean/test/CI/ledger/main changes.
- My front `antichain-defect-sufficiency-vs-general-alln` (agent `Ua2y0n2a2z5K5Nm6Ohcud3-polygamy`) had **no prior #301 post** on pages 1–3 and no scratch artifacts — the interrupted turn performed no side effects. I made exactly **one** board comment (verified: 1 hit, `2026-11-21T16:42:52Z`), with `--json` redirected to a file as required. Stale duplicate search processes from earlier tool timeouts were cleaned up.

## Mathematical finding

Let `F(P)` be the exact adaptive minimax comparison count, `S(n)=F(A_n)`, `δ(A,B)=F(A⊔B)−F(A)−F(B)`, `Z_n` the staircase (`i<j` iff `j≥i+2`). Let **A** = antichain-only bound `δ(A_a,A_b) ≥ min(a,b)+1`; **D** = general `δ(A,B) ≥ min(|A|,|B|)+1`.

**1. The only valid implication direction is D ⇒ A.** `A_a ⊔ A_b = A_{a+b}`, so A is exactly D specialized to two antichains. Since the antichain root has no internal comparabilities, **A is the only disjoint-union defect instance that ever enters the superadditivity recursion for `S(n)`**. So A alone supplies every superadditivity lower bound for `S(n)`; D is strictly stronger than anything needed there.

**2. Refinement monotonicity is FALSE — the claimed bridge is refuted.** Independent from-scratch evaluator (validated `S(n)=0,0,1,3,5,7,10`, `F(C_n)=0`, `F(Z_n)=n−1`, `e(Z_n)=Fib(n+1)`):
- `δ(A₁,Z₅)=6−4=2` but `δ(A₁,A₅)=S(6)−S(5)=10−7=3` — refining `A₅→Z₅` *lowers* the defect.
- Conversely `δ(A₁,C₄)=3 > δ(A₁,A₄)=S(5)−S(4)=2`.

So `δ(A₁,B)` is **neither** monotone under refinement **nor** antichain-extremal: the antichain defect is neither a lower nor an upper envelope of general defects. This kills the falsifier's second option ("refinement monotonicity carries A to D") and matches the board's proved **T1** (the extremal host is the chain `C_b`, `F=0`, not the antichain). No reduction of D to antichain data exists.

**3. Falsification attempt on the first option (direct D-counterexample):** exhaustive exact minimax over *all* unlabeled posets with `|A|+|B| ≤ 6` (counts 1,1,2,5,16,63) found **zero** violations; minimum surplus `δ−(min+1)=0`. High-excess families `Z_a⊔Z_b` are also tight. A size-7 sweep was stopped by compute budget before producing output — so **D is not refuted**.

## Soundness / completeness line

A, T1/T2, theorem [T], and D (if proved) are **sound** minimax statements, not **completeness** results for computing `S(n)`: the A-based recursion equals `S` only through `n≤6` (`L(22)=58 < S(22)=71`, board). General-poset theorems do not transfer to the fixed antichain root or to `SORT-BOUND-U` complexity without an encoding-preserving reduction (AGENTS.md), and sparsity blocks many-one hardness transfer.

## Honest limits

- **D is not refuted** and **A is not proved** here (separate live front). Material implication "A ⇒ D" cannot be disproved unless D itself is false; what *is* refuted is the reductive monotonicity bridge and the claimed necessity of the general campaign.
- No new bound/algorithm for `S(n)`, no class separation. `S(n)` and `SORT-BOUND-U` remain **open**. The decisive obstacle is the cross-transitivity coupling at all-cross roots (board's 15:47Z/16:01Z/16:29Z findings), which is exactly where antichain data gives no leverage.

## Other metadata

```json
{
  "finished_at": 1795279426.9228024,
  "started_at": 1795278210.5931444
}
```
