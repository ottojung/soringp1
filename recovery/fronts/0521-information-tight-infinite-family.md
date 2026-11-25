# information-tight-infinite-family

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Wwj0ucIAgWY7NTVIKboCJG-howl

## exit_state

clearexit

## question

Do there exist infinitely many integers n >= 1 such that the exact sorting number meets the information bound, i.e. S(n) = ceil(log2(n!))?

## basis

Known exact values show equality for small n and gaps at n=12,16,17,18 (Peczarski; Stober-Weiß per docs/literature.md), leaving the infinite-family question open.

## falsifier

Prove there is some N with S(n) >= ceil(log2(n!)) + 1 for all n >= N, giving a uniform eventual gap above the information-theoretic lower bound.

## implication

Infinitely many tight cases or an eventual uniform gap would sharpen structural understanding of optimal comparison trees and constrain certificate or search lower-bound arguments for exact S(n).

## finding_unverified

 of the minimax function `S(n)` at the antichain root (general-poset/partial-order states appear only as reachable search states, not as an arbitrary-poset optimization claim transferred without reduction). No certificate claim is made: local/heuristic bounds on `g(n)` may be *sound* upper windows in special cases but are not, from evidence here, complete or uniform all-`n` invariants tracking exact `S(n)` (cf. `info-bound-gap-invariant-alln` / `computable-entropy-balance-surrogates` notes on board: non-certification/insufficiency barriers, not theorems).

**Mathematical finding.** [deduction from primary/indexed values] The eventual-uniform-gap claim F is **false for every threshold `N<=21`** (counterexamples `n=20,21` with `S(n)=C(n)`), while **open for `N>=23`**; combined with the non-scalar/non-monotone obstruction evidence (`research-n12-nontightness.md`, Peczarski’s `n=13` phenomenon), this leaves the infinite-tight-family question (FRONT) and eventual-gap question genuinely unresolved in both directions by current evidence.

**Failed approach / exact obstruction.** Failed/refuted routes to a decisive answer: predicting tightness by initial slack `2^{C(n)}/n!`, by any monotone function of `e(P)` or by local efficiency/symmetry, or by forced-prefix alone (all non-predictive or not globally sufficient). Exact obstruction: known `n=12` non-tightness and local failures are certified strategically/exhaustively with no published compact reusable invariant; `n>=23` values are unknown, so no finite case analysis and no known uniform invariant currently settles “infinitely many `n` with `g(n)=0`” versus “eventual `g(n)>=1`”.

**Honest limits.** No proof or disproof of FRONT/F for large `n`; no new all-`n` theorem or counterexample found; no Lean/repository changes made (nothing met the publication gate). Any claim beyond the table above for `n>=23` would be conjecture.
**Recovery check (billy-dev).**
- Repo: working tree clean; no uncommitted changes; HEAD `6a96398`.
- No new files were added to the repository by the interrupted turn.
- Board #301: searched for my content (`"infinitely many integers n"`) — no matching post found on page 1. A failed board attempt in `/tmp/opencode/ibgi_board_result.json` ("Message author is required") appears to be from a different process/agent (`iceman-contributor-free` at 04:14Z), not this session.
- Therefore: **no external side effect from this session is confirmed** (no post, no commit, no repo change). The prior output was a text report only.

**Unfinished work.** The research task itself was completed as a text finding in the prior turn; the only possible unfinished external action is a board #301 update, but I cannot confirm it was intended or attempted by this session, so I am not duplicating it. Summary of the finding (from the prior turn) is unchanged:

- **Claim attacked:** eventual uniform gap `∃N ∀n≥N: S(n) ≥ ceil(log₂(n!))+1` (F).
- **Result:** F is **false for every N≤21** (counterexamples `n=20,21` with `S(n)=C(n)`), and **open for N≥23** (`S(n)` unknown). No proof/disproof of infinitely many tight `n` (FRONT) either.
- **Obstruction:** no scalar/invariant of `n!`, `e(P)`, efficiency, symmetry, or forced prefix predicts tightness; `n=12` non-tightness is certified only by exhaustive search with no compact reusable invariant.

If you want a board #301 post for this result, I can prepare and post it (with proper author) — otherwise this remains a clean worktree with no external action taken.

## Other metadata

```json
{
  "finished_at": 1794918220.1027021,
  "started_at": 1794918089.6273606
}
```
