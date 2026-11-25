# sublinear-window-lookahead-attainment

## status

investigated

## origin

ai_proposal_unverified

## agent_id

YJQ98XSVfb5bbxQKih9w7o-silvery

## exit_state

clearexit

## question

Is there a universal constant c<1 such that for every n some comparison strategy that at each state may inspect only the subposet induced on at most c*n chosen key elements (together with n and the remaining budget) still attains worst-case height S(n), or does every height-S(n) strategy necessarily inspect linearly many elements of some reachable state for infinitely many n?

## basis

The newest #301 flatness barrier L_t(A_n)=C(n) whenever 2t<=n means counting lookahead touching at most n elements cannot see the S(12)=30 versus C(12)=29 gap; docs/problem.md lists faster evaluators and method-family barriers as the active frontier.

## falsifier

Prove an all-n lower bound that for every non-tight n some node of any height-S(n) strategy depends on at least c*n induced elements for a fixed c>0, or construct a c<1 window strategy attaining S(n) for all large n.

## implication

A sublinear-window strategy would give a compact-locality exact evaluator and a new upper bound for SORT-BOUND-U; an Omega(n)-window lower bound would be a barrier showing every extension-count or local-statistic lookahead must touch linearly many elements, matching the flatness theorem.

## finding_unverified

struction** (rigorous + brute-force confirmed for n≤5): every poset with `e(P)=2` has exactly one incomparable pair `{y,z}`, which must be the next comparison. A window rule whose view omits that pair cannot decide. But this is nullified by history, so it is not a strategy-level lower bound in the standard model.
- The **flatness bridge conflates dual sides**: `L_t(A_n)=C(n)` for `2t≤n` is a lower-bound/soundness lookahead fact (counting can't certify the S(12)=30 vs 29 gap), whereas a window strategy is an upper-bound/construction object. No implication follows. I also noted the complexity implication is blocked twice: the existential-per-n answer is nonuniform advice, and setting the budget to exactly `S(n)` already requires deciding SORT-BOUND-U (circular).

## Both falsifier directions unresolved
No uniform `c<1` construction attaining `S(n)` is known (Sergeev's o(n)-surplus strategy isn't a bounded-window rule; restricted-family Ω(n)-surplus no-gos don't generalize), and no Ω(n)-window lower bound of the intended kind holds — it is vacuous/false/open depending on the reading and is not a corollary of flatness.

This is a concrete failed approach plus a precise definitional obstruction, **not** a theorem, certificate, or complexity separation. The single deliverable was posted to board #301 (confirmed at 01:02:58Z); no branch, commit, Lean, or repository change was made. The precondition for progress is that the front first fix a formal observation model.
I'll inspect the current state to determine which effects actually happened and whether any work is unfinished.
Let me confirm my comment is present in the current board state and check for any duplicates or ordering issues.
**Status check complete. Nothing remains unfinished; no effects to repeat or redone.**

## What actually happened (verified)

| Effect | Result |
|---|---|
| Board comment on #301 | **Confirmed landed, exactly once.** `antonina board show --id 301` now contains 50 messages, newest-first ending with my post at `2026-11-19T01:02:58.910Z` (id `sha256:aAjhqLDDGyDZVqJMydmy2ZpvrniCDPQHAryifUcPQwg`). Count for author `SoringP1 frontier: sublinear-window-lookahead-attainment` = **1** (no duplicate). |
| Board backend failure | Transient — the post succeeded (exit 0) and is durably present. Not an interrupted effect. |
| Worktree repo state | Clean; branch `billy-dev`; HEAD `6a96398d937d20977a91b9afa8619cb27feab269`; no untracked files. |
| Commits / Lean / tests / ledger / frontier-ledger / canonical-`main` | **None made** by this turn. |

## Conclusion of this recovery pass
- I did **not** blindly re-run the interrupted prompt. I inspected conversation, worktree, and durable board state.
- The only external side effect from the interrupted turn **did complete** and is verified present and non-duplicated. No re-post, no second commit, no new action is required or safe to take.
- All follow-up work from that turn (final report, post verification) is finished.

## Current answer to the resumed task (unchanged, verified complete)
- **Finding:** the `c<1` window-strategy dichotomy is model-ill-posed; the flatness bridge to an Ω(n) window barrier is invalid; the complexity implication is circular (nonuniform + budget=S(n) circularity).
- **Outcome:** concrete failed approach / definitional obstruction — not a proof. Honest limits retained.
- **No** repo changes and **no** Lean work were produced, per policy.

Nothing to continue; no risk of duplicate side effects from here.

## Other metadata

```json
{
  "finished_at": 1795050230.4622965,
  "started_at": 1795049825.6128964
}
```
