# antonina-PWoF0WgZjHwPuxIs42QCVM-opposed

Session: ses_e035dc5e7ffeCQEAlfRnniilaV
Workspace: /home/lubko/soring-fronts/signflip-larger-e-optimality-alln
Created: 1795239852747; updated: 1795242693559

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 564 (msg_1fccb6c3a0013vaw7mYHull39l)

Let me verify my actual data points are solid before posting to #301.


## Output 575 (msg_1fcccfa37001T4BOz3Wlotq88k)

All data points confirmed. Now let me post to #301.


## Output 622 (msg_1fccd6eae001qpQVvhdU0GbvKc)

The comment was posted to #301 at 2026-11-21T06:31:14.973Z. Let me verify the worktree is clean.


## Output 633 (msg_1fccd7a4e001ELtP6gIxNFXeOO)

Assignment complete. Here is my honest finding.

## Summary

**What I studied:** the sign-flipped / `larger_e` cross-rule adversary for disjoint composition `A ⊔ B` — the question of whether `larger_e` always attains `F(A ⊔ B)` (the minimax value) or whether an all-n family forces strictly less.

**Validation (experiment, rebuilt from scratch):**
- `F(A_n)` n=1..8 = 0,1,3,5,7,10,13,16; canonical-form counts match OEIS A000112 exactly through n=8.
- C1 counterexample reproduced exactly: A = singleton, B on 5 elements (comparabilities 3<0, 3<1, 4<0, 4<1): `F(union)=8`, `H=7` for `larger_e`/`first`/`smaller_e`.
- `A_3 ⊔ A_3`: `F=10`, `H=10` for `larger_e`/`larger_global_F`; `first`/`smaller_e` give 9 — tie-break sensitivity confirmed independently by Viche.
- Merge families `chain_a ⊔ chain_b` (a,b≤4) and antichain unions up to total size 6: `H=F` on every tested case (positive instances only).

**Concrete finite failures (experiment):**
- L=(2 lowers), U=(2 uppers), all lower<all upper, plus s isolated elements, disjoint-unioned with singleton A:
  - s=1 (n=6): `F=8`, `H=7` → FAIL (strictly below F)
  - s=2 (n=7): `F=11`, `H=10` → FAIL (strictly below F)
- L=3,U=2,s=1 (n=7): `F=10`, `H=10` → tight.
- These are **finite failures of the local rule**, not an all-n family. No infinite family where `larger_e` forces strictly less than `F(A ⊔ B)` is exhibited.

**Computational wall (budget-exceeded):** s=3 (n=8): `F=14` computed in ~503 s, but H did not finish within the timeout. Budget-exceeded result, not a proof or disproof; no n=8 H value obtained.

**Connection to prior work:** corroborates `exec-du-adversary-composition-20261120` — non-circular local composition of component adversaries fails because cross-transitivity couples the components; subgame scalars are blind to that coupling. No all-n refutation of the disjoint-union defect inequality `F(A⊔B) ≥ F(A)+F(B)+min(|A|,|B|)+1` was obtained; it remains open (H ≥ target in every tested pair).

**Honest limits:** No all-n theorem for `larger_e` optimality; no all-n counterexample family; no theorem-completion claim for `S(n)`/`SORT-BOUND-U`; no complexity-class separation claimed.

**Repository state:** worktree clean — no repo/Lean/test/workflow/ledger/canonical-main changes; all scratch under `/tmp/opencode/work`. The single external write is the finding posted to Antonina issue #301 (author tag `SoringP1 researcher: signflip-larger-e-optimality-alln`, timestamp 2026-11-21T06:31:14.973Z).

The central question remains open: whether *any* simple extension-count-style tie-break (or a different all-n score ranking answers by global F without computing F) attains `F(A ⊔ B)` for every disjoint union.
