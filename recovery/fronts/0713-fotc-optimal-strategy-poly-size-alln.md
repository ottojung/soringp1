# fotc-optimal-strategy-poly-size-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

s6m988XI3qqEre4u0hvthq-cooked

## exit_state

clearexit

## question

For all integers n>=2, does every height-S(n) optimal adaptive comparison tree admit a fixed-interpreter FO(TC) strategy program of polynomial text size in n and polynomial per-input interpreter runtime on all permutations, enabling poly-time verification of that strategy’s worst-case depth S(n)?

## basis

docs/research-fo-tc-strategy-programs.md (conjecture, Sigma2^P framing) and docs/research-certificates-barriers.md; distinguish strategy soundness/completeness from general-poset hardness per AGENTS.md.

## falsifier

Exhibit infinitely many n and, for each, every height-S(n) optimal strategy such that any fixed-interpreter FO(TC) realization has superpolynomial text or superpolynomial runtime, via an explicit combinatorial or information obstruction.

## implication

Affirmative evidence would support a succinct-checkability route toward NP/coNP-style witnesses for SORT-BOUND-U; refutation would show optimal strategies resist polynomial FO(TC) compression despite uniform interpretability.

## finding_unverified

on-theoretically possible but still leave FO(TC) realizability and worst-case verification open.
- **Complexity implication (careful).** Affirmative evidence for *existence of a verifiable* succinct strategy witness would support NP/coNP-style certificate routes for `SORT-BOUND-U`; but this front as stated overclaims by bundling representation and universal verification. A refutation of the verification clause alone would not settle `SORT-BOUND-U ∉ NP`; it would only rule out this specific poly-time-verification-by-execution route.
I've verified the recovery state. Let me check the exact mandate this front was launched with, to determine whether a board post is an outstanding deliverable.
## Recovery audit — complete

I inspected the conversation, the working directory, Git state, the durable ledger, and board #301. Findings:

| Effect | Status |
|---|---|
| Repository files / Lean / tests / CI / ledger | **No changes.** Both worktrees clean at `6a96398`; `git log` unchanged. |
| Commits / PRs / branch pushes | **None.** |
| Board #301 posts | **None.** Searched all 11 pages for the front slug `fotc-optimal-strategy-poly-size-alln`, the distinctive phrase "every height-S(n) optimal tree", and the computed count `2,418,647,040` — zero matches. |
| Antonina agents / purchases / other external actions | **None.** The only CLI calls were read-only (`board show`, `board access`, `agent` capability check). |
| Ledger entry | Front `fotc-optimal-strategy-poly-size-alln` is still `running` with `finding_unverified: <none>` and agent `s6m988XI3qqEre4u0hvthq-cooked`. I did **not** modify it (keeper-managed). |
| Scratch | Only local `/tmp/count_optimal.py` from the counting experiment — not an external side effect. |

**Conclusion: the previous turn performed no external side effects.** Everything was reads plus a local computation; the mathematical report was already delivered in full at the end of that turn. Host is `billy-dev` (confirmed via `hostname`), so the original mandate's location requirement was satisfied.

## Unfinished work

None. The base mandate is "On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof" — that report was already produced. There is no outstanding board-post, commit, or ledger obligation: the front's outcome is an **honest inconclusive result** (no new theorem, no disproof), which under the research packet ("post only if an independently checked theorem/falsification truly changes the research picture; if no result, say no result and why") does not warrant a new external write — and the recovery instruction forbids inventing one under uncertainty.

## Finding being preserved (already reported, restated briefly)

- **Exact obstruction (deduction):** per-input polynomial FO(TC) execution gives a `coNP`/`Σ₂^P`-shaped worst-case verification, not poly-time verification of `S(n)`. The front's "enabling poly-time verification" clause fails as stated.
- **Failed disproof (experiment + deduction):** the "every optimal tree" clause is vulnerable to a counting obstruction, but I could not prove `N_opt(n) = 2^{ω(poly(n))}` for infinitely many `n`. Small-n counts (`N_opt(4)=27,744`, `N_opt(5)=2,418,647,040`) are calibration only. The all-n counting step remains the open subproblem.

No action taken this turn beyond verification. Nothing is duplicated, and no uncertain side effect is being papered over — the audit shows there was nothing to replay.

## Other metadata

```json
{
  "finished_at": 1795436148.464855,
  "started_at": 1795435620.114499
}
```
