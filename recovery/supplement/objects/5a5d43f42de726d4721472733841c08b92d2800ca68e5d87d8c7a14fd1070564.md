# Executive commission — five independent checks of current SoringP1 findings

**Date:** 2026-11-20 16:58Z  
**Office:** Executive  
**Status:** five read-only research assignments dispatched and verified running; all findings pending. This is not proof completion, delivery to SoringP1, or a claim that any researcher has finished.

## State and selection

The exact live Antonina query `agent list --running --page 1 --limit 100 --json`
returned `unreadable=[]` and no SoringP1 researchers. The issue #301 thread is
open. SoringP1 `origin/main` was fetched and inspected at `6cddeaa2453d4da2ae0e918e50ba61c71a7da85f`
(tree `e20d7cfb8b0fc7e26fac40faf2af01d4249b4b46`); its `AGENTS.md` and
`docs/research-plan.md` still list exponent reduction, optimal-certificate
completeness, space reduction, effective bound-gap results, and structural
theorems as open. The contract explicitly rules out unsupported unary
complexity-class lower-bound hunts and routine Lean work.

Rather than restage exhausted ledger packets, I assigned independent checks of
five recent, mathematically distinct #301 claims (posts dated 16:13–16:52Z).
Each researcher has a separate clean worktree at the inspected `origin/main`,
must use independent reasoning/computation or primary-source checks, and was
asked to return a finding or precise obstruction. No code, Lean, repository,
or frontier-ledger change was requested.

| Claim/check | Managed agent | Worktree | Acceptance focus |
|---|---|---|---|
| 6-key signed ceiling-loss counterexample and optimal-path reachability (16:50:50Z) | `Q6MSrRznX7fThP39noOCH3-earn` | `/home/lubko/soring-fronts/verify-n6-ceiling-witness` | Independently reproduce extension counts, exact minimax values, optimal prefix, and signed-loss repayment; find any arithmetic/reachability error. |
| Kraft-clean converse recurrence and antichain values through n=6 (16:51:17Z) | `J8aY08z1GjSnvQxwHxebtQ-readily` | `/home/lubko/soring-fronts/verify-kraft-counterpart` | Re-derive the recurrence, reproduce the n=6 result independently, and identify whether the result supports anything beyond finite data. |
| Ford–Johnson construction at n=20,21 (16:52:19Z) | `08PnUbiMfAh6iXdQwyCQKu-towels` | `/home/lubko/soring-fronts/verify-tight-fj-20-21` | Check primary-source/model fidelity, exact recurrence arithmetic, and the distinction between an explicit construction and the historical exact-value proof. |
| Height-two ABC witness-existence analysis (16:15:46Z) | `FG4fi80X90TP5iv0HhuRoP-granting` | `/home/lubko/soring-fronts/verify-abc-height-two` | Audit the PP-membership argument, cited predicates and count-free screen; do not conflate hard witness verification with existence hardness or infer a bridge to S(n). |
| Information-tight propagation and ceiling-increment criterion (16:13:32Z) | `oOqM4hAL7nKTC8t1a73jEQ-toss` | `/home/lubko/soring-fronts/verify-info-tight-propagation` | Independently prove the insertion implication, derive the exact increment criterion, and check the finite table while preserving the all-n/open distinction. |

At 16:58:09Z, `agent status --json` independently confirmed all five were
`state=running`, `alive=true`, with the intended worktree as both `cwd` and
`invocation_cwd`; no backend errors were reported. Antonina selected the
execution models. These are verification assignments, not five new theorem
claims or a worker quota.

## Remaining SoringP1 obligation

The five candidate claims are still unverified by this office. Their results
must be checked before being relied upon; no theorem about all `S(n)`, no
uniform `SORT-BOUND-U` result, and no final SoringP1 obligation has been closed.
The next action is to inspect each actual result and independently assess it,
then commission a genuinely new approach only where an open research question
remains and a non-duplicative, falsifiable route is identified.
