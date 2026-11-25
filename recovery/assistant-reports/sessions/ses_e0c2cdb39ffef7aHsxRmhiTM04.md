# antonina-35TAVoGR7NDgZUGkl3AlmK-enhanced

Session: ses_e0c2cdb39ffef7aHsxRmhiTM04
Workspace: /home/lubko/soring-fronts/depth-balance-threshold-constant-cstar
Created: 1795092063482; updated: 1795094235910

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 694 (msg_1f3f43f8b0011VbGTzINPdje6X)

Posted a single #301 deliverable for `depth-balance-threshold-constant-cstar`. Summary:

- **Finding:** No B-failing poset was found. Exhaustive unlabeled isomorphism classes through `n=8` (`16999` classes) and labelled posets through `n=6` (`130023`) all satisfy depth-balance `B`; all tested merge/ordinal-sum families also satisfy `B`, including the ratio-`5/8` cases `Merge(1,4)` and `Merge(3,3)`.
- **Failed construction:** Perturbing `P5` or using merge/ordinal-sum families always retains a balanced optimal comparison. The `5/8` family `P_m = P5 ⊕ T_{m-5}` itself satisfies `B`, so it is a barrier for the one-step inequality, not a B-counterexample.
- **Obstruction:** The one-step information-bound method is capped at `5/8` by that family. A strict improvement would require a global condition that *all* optimal moves are unbalanced; the `n=5`/`n=7` easy-child lift failures show a one-child local exchange cannot supply it.
- **Honest limit:** This does not prove that B-failing posets do not exist, and `c*` remains undetermined (degenerate if `B` is universal; otherwise an unknown supremum ratio bounded above by `5/8`). No repository, Lean, test, or complexity claim was made.
