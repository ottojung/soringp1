# antonina-Ua2y0n2a2z5K5Nm6Ohcud3-polygamy

Session: ses_e011476feffebBepueuJpwJDUM
Workspace: /home/lubko/soring-fronts/antichain-defect-sufficiency-vs-general-alln
Created: 1795278211431; updated: 1795279418700

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1fef2f729001CnMYKJF6CDp5Bf)

I'll start by carefully inspecting the current state before doing anything, since this is a resumption after an infrastructure failure and I must not duplicate side effects.

## Output 28 (msg_1fef30820001GrYZnq5EYBXK5O)

I'm on `billy-dev` with a clean worktree. Let me inspect durable task records, the research board, and recent git history to understand what happened before the failure.

## Output 43 (msg_1fef317ef001Ol1nGFbyO6KJ6X)

Let me read the key documents and locate board #301 and any durable task records.

## Output 62 (msg_1fef3355c001IjAK39dIjkaApC)

Now let me check the research board digest, the durable frontier ledger, and the front's exact definition. I'll be careful not to flood context.

## Output 90 (msg_1fef359b800192vxkoFMv4ymtG)

The ledger is large. Let me locate my specific front and check whether the interrupted turn already recorded anything, plus verify Antonina availability.

## Output 105 (msg_1fef37a220015cgu33n7hZtiQ5)

Antonina is available. My front is `antichain-defect-sufficiency-vs-general-alln` (agent `Ua2y0n2a2z5K5Nm6Ohcud3-polygamy`, status `running`). Let me check whether the interrupted turn already posted to #301 or left scratch artifacts, so I don't duplicate side effects.

## Output 133 (msg_1fef3bca9001tWD6nSHe9O4Aqq)

No side effects from my front so far (clean worktree, no #301 post by my author tag). Let me study the newest board results and look for an existing scratch minimax evaluator I can reuse (scratch only, no repo changes).

## Output 148 (msg_1fef428f6001oNx2V8Dx1kgFga)

Let me read an existing from-scratch evaluator and the exact board statements of the key T1/T2 results, then build my own independent check (scratch only).

## Output 163 (msg_1fef4cec4001PhCuS3Yz1TghMc)

I now have the key background. Let me build an independent scratch evaluator to (a) verify the refinement-monotonicity counterexample and (b) search for a direct counterexample to the general defect inequality. Scratch only — no repo/Lean changes.

## Output 190 (msg_1fef56892001pgLhzTOa7kaDmD)

My evaluator independently confirms the monotonicity counterexample. Now let me generate all small posets up to isomorphism and search directly for a counterexample to the general defect inequality D.

## Output 260 (msg_1fef8f6c6001K6u558aXciRaoK)

Up to total size 6 there are no violations of D. Let me run the larger exhaustive search in the background while I probe structured families and think theoretically.

## Output 318 (msg_1fefc2f440015ommwo2jT0121A)

Let me check the exact Antonina board post syntax from prior scratch records before drafting a single report, and verify my key numbers once more.

## Output 351 (msg_1fefcac9d001yxH7YJ0rbrko4e)

I have a solid finding. Before posting, let me re-confirm no prior post under my exact author tag, then post exactly once.

## Output 405 (msg_1fefdcf28001rHwwkPPPQpsSR7)

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
