# antonina-IuaKozBlPKJv12U5gQk6N4-wyoming

Session: ses_e0f8aa62fffeqgWTa3yzuoCbRG
Workspace: /home/lubko/soring-fronts/kply-lookahead-certificate-20261118
Created: 1795035585020; updated: 1795036268342

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f0755f53001GmSb1EPRdsQITK)

I'll start with the mandatory recovery audit before any external side effect.

## Output 21 (msg_1f0756ee2001XrXEXo50JtXCIg)

Worktree is clean at HEAD `6a96398` on branch `research/kply-lookahead-certificate-20261118`. Now the duplicate-report scan on Antonina #301.

## Output 36 (msg_1f0758262001HTcTtmT46phWLc)

No matches on page 1. Let me scan all pages to be thorough, as other reports did.

## Output 47 (msg_1f075cf40001bLYhfb4LhKUQbs)

Page 1 now shows 1 match — this could be a mention by another agent. Let me inspect the actual content.

## Output 58 (msg_1f075e20b00177V1fhNTQkbIKT)

The 1 match is a Viche Executive dispatch *mentioning* this front, not a report by this author. Let me confirm by reading the full message and checking exact authors across all pages.

## Output 78 (msg_1f075f9bd001rGvgMwFwyek6HE)

Let me fetch all board pages to `/tmp/opencode` (scratch only) and scan exact authors to be fully certain.

## Output 268 (msg_1f07f6749001Shw7Y1EY3Mxn1g)

## Recovery audit (before any external side effect)
- Worktree: clean at `6a96398` on `research/kply-lookahead-certificate-20261118` (`git status --porcelain=v1` empty).
- Antonina #301 scanned (all pages): **0** prior reports authored `SoringP1 frontier: kply-lookahead-certificate`; 1 phrase match was the Viche Executive dispatch naming this front (not a duplicate report). No repost.
- No repo/Lean/tests/PRs/workflows touched. All scratch work kept in `/tmp/opencode/`.

## Background / addendum handled
- Read `docs/problem.md`, `docs/research-plan.md`, `docs/research-one-ply-obstruction.md`, `docs/research-structural-lower-bounds.md`, `docs/research-n12-nontightness.md`, and board review `research/review-composition-20261018` (PR #22 context, #301).
- Stated `B` correctly in the report as a **compositional** lower bound with `L0 ≤ L1 ≤ B ≤ F` (maximal series decomposition plus certified small-budget/per-factor base; e.g. `B(P)=∑_i b(P_i)` with `B≤F` by per-factor bounds + ordinal-sum additivity), and distinguished it from the untried bounded-depth adversarial lookahead hierarchy `L_t` (level-by-level minimax refinement, non-compositional).

## Investigation (scratch, `/tmp/opencode`)
- Implemented exact big-integer linear-extension counting and `L_t` with memoization on canonical transitive-closure states (relabelling symmetry/automorphism orbits), using `e_n(R ⊔ I_m)=e(R)·n!/k!` and `O(k 2^k)` subset DP per active core (`lt_n12.py`, `check_l4b.py`, `check_l5.py`, `validate_lt.py`).
- **Validation [experiment]:** `L_0 ≤ L_1 ≤ L_2 ≤ F = S(n)` for antichains `n ≤ 6` (`n=0..4: 0,0,0,0 / 0,0,0,0 / 1,1,1,1 / 3,3,3,3 / 5,5,5,5`; `n=5: 7,7,7,7 (S=7)`; `n=6: 10,10,10,10 (S=10)`), and `L_1(A_12)=29` reproduced (matches analytic `1+⌈log2(12!/2)⌉=C(12)=29`).

## Results
- **(a) Exact `L_t(A_12)` for feasible `t` [experiment]** (`C(12)=29`, `S(12)=30` literature): `L_0=29, L_1=29, L_2=29, L_3=29, L_4=29, L_5=29` (largest computed; `t>=6` not computed). No `t ≤ 5` certifies `S(12)=30`; no `>=30` witness tree.
- **Checkable intermediates (n=12):** `P1=A_12+(a<b)` has `e=239,500,800, L_0=28, L_1..L_4=28`. Depth-2 representatives from `P1`: `V={a<b,a<c}` (`k=3,m=9,e=159,667,200`) `L_0..L_3=28`; `C3={a<b,b<c}` (`e=79,833,600`) `L_0..L_3=27`; `2E={a<b,c<d}` (`k=4,m=8,e=119,750,400`) `L_0..L_3=27`. Hence `L_{t}(P1)=28` for `t=1..4` and `L_{t+1}(A_12)=1+L_t(P1)=29` for `t=1..4` [deduction from symmetry/values]. An adversarial branch (V-like) keeps the 5-ply information potential at `C(12)`.
- **(b) Bounded lookahead in general:** `L_1(A_n)=C(n)` for all `n` [deduction]. For fixed `t>=2`, **open** — neither a proof that `L_t(A_n)>C(n)` infinitely often nor an argument that `L_t(A_n)=C(n)` for all `n` at every fixed `t>=2` established; finite evidence `n=12,t<=5` shows no separation from `C(12)` (consistent with a barrier, not a proof).

## Deliverable posted
- Single concise report posted to Antonina #301 as comment `sha256:F9cUFGe20RQPHLACNFlvPsLw9hDnfnEns7ZaSWE02ZI` (2026-11-18T21:10:32.694Z), authored **"SoringP1 frontier: kply-lookahead-certificate"**. Includes recovery/B-addendum, definitions, labelled evidence/validation, (a)/(b) status, consequence, next decisive obstacle, and model-fidelity caveats (comparison bounds on `S(n)`, not complexity lower bounds). No theorem completion claimed.

## Consequence / next decisive obstacle
- `L_{<=5}` gives no structural lower-bound certificate separating `S(12)=30` from `C(12)=29` (distinct from compositional `B`). Decisive next step: determine if any finite `t` yields `L_t(A_12)=30` (compact min/max certificate) or prove `L_t(A_12)=29` for all finite `t` (instance-level barrier), via deeper/optimized exact computation or a theoretical control of the `L_0`-potential; resolving (b) needs an all-`n` argument.

## Worktree state
- Clean at `6a96398`, branch `research/kply-lookahead-certificate-20261118` (no local changes).
