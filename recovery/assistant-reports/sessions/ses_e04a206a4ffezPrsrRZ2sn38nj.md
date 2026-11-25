# antonina-8fv8Xhiovp5070S1aN0LhA-suffer

Session: ses_e04a206a4ffezPrsrRZ2sn38nj
Workspace: /home/lubko/soring-fronts/exec-du-adversary-composition-20261120
Created: 1795218602424; updated: 1795219860229

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fb5dfb7c001C7JkCpHfpnjJri)

I'll start by understanding the repository, the contract, and how the Antonina board works.

## Output 111 (msg_1fb5e99b2001wOM3f7HMWSkNKm)

I have a thorough understanding of the context now. Let me look at earlier board posts on this exact defect inequality and search for prior adversary-composition attempts.

## Output 149 (msg_1fb5fdc0a001hO6kPPeXKv8Su4)

I now have the full research context. Let me verify my host/worktree state and build a scratch evaluator under `/tmp/opencode` (no repo changes).

## Output 185 (msg_1fb64c0550013nYYxSezBNcnyi)

The canonical form has a bug (rows not reordered by the permutation), so isomorphic states aren't merging. Let me fix it.

## Output 230 (msg_1fb65abb80018PtTZiS3iib75O)

Evaluator now matches F(A_n) through n=8. Let me verify A000112 counts via independent generation and time the n=9 computation.

## Output 251 (msg_1fb690462001G9nrDpr8w1vrdG)

F(A_9) didn't finish in 200s (honest limit); validation through n=8 is solid. Now let me build the adversary-composition machinery — the core of this front.

## Output 287 (msg_1fb6a48a2001HON6bTDtzUJiVI)

The first composition fails on tiny cases, but some look like tie-break artifacts. Let me refine the cross rule with an information tie-break and see whether the failure is fundamental.

## Output 314 (msg_1fb6b1a480017C4I7z8mlHCqzy)

The failure is at the **within-component** step: σ_B answers using only P_B and is indifferent between two answers, but cross-transitivity makes one answer finish the whole game. Let me test whether a global tie-break repairs it.

## Output 359 (msg_1fb6bc12d001gzr6etWNonzjvf)

I found a bug in my experiment: I used F(antichain) instead of F(actual component) in the target. Let me fix and rerun.

## Output 370 (msg_1fb6c90dc001u4PfcJJD5Ixnki)

The corrected experiment shows the natural composition fails at (A₃, A₃). Let me extract the exact failing path and verify it independently.

## Output 381 (msg_1fb6cd196001AR9XHSEQ7KEdkP)

A red flag: one step shows F dropping by 2, which is impossible. Let me audit the F evaluator against a brute-force labeled minimax before trusting any of this.

## Output 392 (msg_1fb6d04fe001TzM7lJvxijeGst)

Good — F is validated (0 mismatches vs brute force); the F-drop was legal. Let me nail down the exact failing step at (A₃,A₃) and test robustness across rule variants.

## Output 403 (msg_1fb6d67230016un7Gx8WNkDp71)

The failure is sharper than tie-breaking: the answer that **preserves subgame budget** (F_B stays 3) drops the global minimax value by 2, while the budget-degrading answer drops it by only 1. Let me test robustness across many compositional rules.

## Output 430 (msg_1fb6e14d2001LnlHB06t7DwU61)

Let me produce a checkable 9-comparison transcript against the natural composed adversary and independently verify each step.

## Output 450 (msg_1fb7008a2001yAGvBm67qd3KCz)

I have a complete result. Let me verify the worktree is still clean, check no prior post under this author tag, then compose and post the note.

## Output 524 (msg_1fb71111e001pJHObf9rcmSRYS)

Done. Research note posted to Antonina issue #301 on billy-dev under `SoringP1 researcher: exec-du-adversary-composition-20261120` (2026-11-21T00:10:41Z). Worktree remains clean at `6a96398`; scratch only in `/tmp/opencode/du`; no repo/Lean/CI/ledger changes.

## Result: OBSTRUCTED (method refuted, inequality not)

**What I did**

- Built a scratch evaluator (transitively closed successor masks, subset-DP `e`, memoized minimax with a complete canonical form). Validated `F(A_n)=0,1,3,5,7,10,13,16` for n=1..8, unlabelled counts `1,2,5,16,63,318,2045,16999` (A000112, not A001035), and 0 mismatches against a brute-force labelled minimax. Honest limits: F(A₉) recomputation time-boxed out at 200s; I verified only its information lower bound (e=9! ⇒ F≥19) and adopted the board value 19.
- Defined the composed adversary formally (within-A/B by the greedy subgame-optimal σ_A/σ_B; cross by "preserve subgame budgets") and computed `H_σ`, the height the sorter needs against that *fixed* adversary.

**Two explicit short plays break the composition**

1. **A = singleton, B = 2-antichain:** target 3 and true F=3, but H_σ=2. A within-B query is a tie for σ_B on B alone; cross-transitivity makes one answer end the whole game.
2. **A = B = 3-antichain:** target 10 and true F=10, but a checkable 9-step transcript exists. At the key cross step the two answers have subgame sums 3 vs 2 but global F 4 vs 5 — the "budget-preserving" rule strictly picks the globally worse answer (not a tie-break artifact).
3. Robustness sweep of 60 rules: every subgame-local rule fails (H∈5..9); only global-e or global-F rules succeed — those are the exhausted extension-count route or circular.

**Precise failing step:** cross-transitivity couples the components, but the subgame scalars F(N|_A), F(N|_B) are blind to it. Within-component answers can terminate the global game despite tying locally; cross answers that preserve subgame budget can lower global minimax by 2 while the alternative lowers it by only 1; and cross comparisons can consume information a sub-adversary needed (both answers strictly reducing F_A+F_B). The +min+1 surplus is lost because one cross comparison can create several derived cross relations for free.

**Not a counterexample:** true F equals the target at every witness, so the inequality stays open exactly where prior work left it (proved through total 11; at 12 all but (2,10)). No S(n)/SORT-BOUND-U claim. Next experiment proposed: a transitivity-aware rule charging each newly derived cross-pair comparability, tested on A₃⊔A₃ and (2,10).
