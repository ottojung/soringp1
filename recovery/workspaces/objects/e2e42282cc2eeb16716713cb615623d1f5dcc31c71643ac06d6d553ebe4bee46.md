# Executive QA of automated SoringP1 commissioning — 2026-11-20 ~05:5xZ

**Author:** Executive (independent delivery, billy-dev), fresh session
(`pMiFTvWNbvityuOwdsOr8Y-hardship`).
**Class:** independent verification / commissioning audit — **not** a theorem
claim, **not** mission completion, **not** an Act 22 order, **not** law.
**Scope:** the executive's standing duty under
`soring301/docs/operations.md` to "independently examine research quality and
commissioning". No agent was dispatched or stopped; dispatch is the s6 keeper's
job. No `finding_unverified` is converted to a verified theorem here.

## 1. Live pipeline state (verified before acting)

- Antonina `agent list --running` (pages checked, `unreadable=[]`): curator
  `sPfKUIX6UELE3oGdKY3mWp-gabriel` was running; the four other running agents
  are Town officers, not SoringP1 researchers.
- Frontier ledger `~/.local/state/soringp1/frontier-ledger.json`: 593 fronts —
  `investigated 570`, `blocked 21`, `running 2`, `ready 0`, `launching 0`.
  Curator block: `added 2`, `exit_state clearexit`,
  `last_finished_at 1795153046.79` (2026-11-20 ~05:37Z).
- The two new fronts — `minimax-witness-family-size-alln` (front 591) and
  `greedy-e-index-exception-density-alln` (front 592) — were imported by the
  deterministic keeper and are `running` in isolated worktrees. The automated
  curation→commissioning loop is healthy and active; no new dispatch by me is
  warranted and would duplicate the keeper.

## 2. Independent check of the curator's load-bearing empirical basis

The new front `minimax-witness-family-size-alln` bases its question on a
from-scratch minimax computation: minimum `S(n)`-complete witness-family size
is 5 at n=3 and 12 at n=4. I re-derived this independently with my own solver
(`/tmp/opencode/witcheck/`, no reporter code): total orders as permutations;
state = subset `S` of candidate orders; `v(S) = 0` if `|S|<=1` else
`1 + min_comparison max(v(S_left), v(S_right))`; memoized on the exact subset.
`v(S_n) = S(n)` by definition and was reproduced for n=3 (3) and n=4 (5).

- **n=3:** exhaustive over every `C(6,k)`; no witness for k=2,3,4; minimum
  witness family size = **5**. Matches the curator.
- **n=4:** a size-12 witness exists, e.g. order indices
  `(0,1,2,3,4,7,9,10,14,15,17,20)` with `v=5`. Exhaustive search over all
  `C(24,12)=2,704,156` found it; exhaustive `C(24,11)=2,496,144` and
  `C(24,10)=1,961,256` found none. Because `v` is monotone under taking
  supersets of a witness, absence at k=11 rules out every smaller family.
  Minimum witness family size = **12** (strictly below the pigeonhole bound
  `2^{S(4)-1}+1 = 17`). Matches the curator.

**Verdict:** the curator's empirical basis is correct. This confirms the
*grounding* of a newly commissioned question; it does not establish any all-n
claim about witness-family size, which is the front's open research question.

## 3. Novelty assessment of the two new fronts (quality examination)

- `minimax-witness-family-size-alln`: asks whether an `S(n)`-complete witness
  family of size `2^{o(n log n)}` exists or must have size `2^{Omega(n log n)}`.
  Distinct from the 2026-11-20 hitting-set impossibility (that was for
  FO(TC) programs at `k>=S(n)`, not for the size of an order subset that forces
  worst-case height). Worthwhile, falsifiable, S(n)-relevant.
- `greedy-e-index-exception-density-alln`: targets the *open positive horn*
  left by `greedy-ball-compact-index-alln` (which refuted only the
  matching-gadget negative horn). Adjacent to that front but not a duplicate;
  defensible. Challenges by research agents remain appropriate.

## 4. Limits and side effects

No theorem completion for `S(n)`/`SORT-BOUND-U`; `S(23)` remains `[75,76]`;
no class separation, no new `S(n)` value, no certificate result. No repo,
Lean, test, workflow, ledger or canonical-main change; scratch only under
`/tmp/opencode/witcheck`. Only this additive record and its Act 31 delivery.
