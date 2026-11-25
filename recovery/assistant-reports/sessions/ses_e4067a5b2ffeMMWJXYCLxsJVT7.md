# antonina-nOtkdl2ND0j6KG0BudExPP-proximal

Session: ses_e4067a5b2ffeMMWJXYCLxsJVT7
Workspace: /home/lubko/soring-fronts/curator
Created: 1794215795291; updated: 1794216579859

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 506 (msg_1bfa43c52001NlEgkHPhjbD9r8)

Wrote `/home/lubko/soring-fronts/curator/frontier-candidates.json` with two new fronts.

**Independent work done**
- Read `AGENTS.md`, `docs/problem.md`, operations, literature, ledger, and the newest #301 posts (`three-chain-insertion-gap`, `adaptive-network-size-gap`, `fulltree-capacity-deficit`, `near-optimal-partial-sorting-gap`).
- Ran exact minimax checks for the family `C_m ⊔ A_2` through `m = 20`; found `D = 1` at `m = 4, 9, 19, 20` and `D ∈ {0,1}`, consistent with the newest board result.
- Ran separate full-poset exact minimax checks for `C_m ⊔ A_r` at small sizes: `r=3` gives `D = 0,0,0,1,1` for `m = 0..4`; `r=4` gives `D = 0` for `m = 0..3`.

**Proposed fronts**
1. `two-key-merge-defect-infinity` — the open follow-up explicitly left by the newest #301 post: is the two-key insertion defect `1` infinitely often, and what is the density/closed form of that set?
2. `fixed-free-block-insertion-defect` — whether the fixed-`r` insertion defect is uniformly at most `1`, or grows with `r`; `r=3` is the first untested constant.

**Honest limits**
- No theorem or proof is claimed; the DP data are finite exact computations, not all-`m` results.
- I did not establish that the proposed claims are true; the second is deliberately framed as a dichotomy.
- No Lean files, commits, or board posts were created. The only worktree change is the required `frontier-candidates.json`.
