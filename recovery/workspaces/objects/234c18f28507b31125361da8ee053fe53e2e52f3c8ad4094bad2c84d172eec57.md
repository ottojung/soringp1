# Judiciary fact-finding — dispatch cycle feb575fa5b9211bf7c928a719de65fbe

Recorded 2026-11-19T09:21:46Z. Verdicts filed at epoch 1795080063
(2026-11-19T09:21:03Z). Independent judicial audit under Acts 4, 8, 9, 15, 16,
21 and 26. No law, policy, measurement machinery, case state, mailbox item,
correction or reform proposal was made. Mailbox inbox is empty; the mandatory
cross-branch corrective-case list for this dispatch is empty (`open_cases: []`).

This is a **new** four-case cycle (new token, new frozen sample), distinct from
the prior `13ca158e…` cycle whose report already landed on `main`.

## Method

- Read all four frozen case files under `state/oversight/random/cases/` and
  re-fetched each named board issue with `antonina board show --id … --page N
  --json` across every available page, scanning every message for an author
  exactly `Vitalik`, host-assignment text, and terminal state.
- Host assignment was taken from each issue's own description and board
  history, never from an executive list. GitHub-hosted CI is treated as
  permitted; Viche/OpenClaw managed-agent execution on `marceline-dev` is not
  CI and does not become CI merely because the work involves GitHub PRs.
- Public remote Git was reachable this cycle. I used `git ls-remote` on
  `ottojung/antonina`, `ottojung/skrynia-tools` and `ottojung/Skrynia`, plus one
  bounded blobless clone of `ottojung/antonina`, to verify claimed commits and
  ancestry independently of reporter handoffs. No local repository test suite
  was re-run except the hermetic Act 26 smoke test below (which is a
  self-contained fixture and needs no project source).
- Canonical lawfulness/effect was checked in `/var/lib/lubko/wd/viche` with
  `git show`, `git merge-base --is-ancestor`, `git log -S`, the committed
  pre-landing record, and an independent `git archive` + re-run of the added
  smoke test.
- One verdict per sampled case was filed with `government/audit-accountability.py
  report`. No `--correction` was used: this cycle's cases had no prior verdict.

## Sampled cases (4) — verdicts filed

| Case | Population | Verdict | Short basis |
|---|---|---|---|
| `91e618413c7b7c3826` (issue `8WamKUbxj78aReLPxjoEWY-sustained`) | ignored_work | **finding** | Host-policy only. No `Vitalik` comment and no billy-dev assignment (5 messages), so no Act 9 duty / no neglect. Agent handoff 2026-11-19T08:35Z explicitly works "on authorized marceline-dev"; branch `…/v3-native-web-admin` confirmed at `d697169` (base `6f4cc02`). Not false delivery; work partial, no draft PR. |
| `ddd6b158ae626eb9ca` (issue `dgKBALkpO7M7oKBHrZUzCT-shortly`) | ignored_work | **finding** | Host-policy only. No `Vitalik` comment and no billy-dev assignment (53 messages). 16 comments explicitly place Antonina agent sessions on marceline-dev, e.g. 07:58Z "Live confirmed marceline-dev Antonina sessions (all now select opencode-go/iceman-contributor-free)". Skrynia PR heads independently confirmed; delivery draft/unmerged, owner withdrew v2 parity. Not false delivery. |
| `b0e55ae6181ca8c165` (issue `304`, Antonina) | claimed_delivery | **finding** | Host-policy + unmet acceptance gate on a closed issue. Core removal genuinely merged and verified (PR #113 `8789567`, test-only PR #115 `3d26148`; both ancestors of `origin/main`). But criterion 4 required deploy+live verification on marceline-dev **and** phoebe-dev; only marceline-dev verified, phoebe-dev recorded unreachable, yet issue CLOSED. 21 comments show `HOSTNAME=marceline-dev`. Not false delivery of the main deliverable. |
| `303ead1e0d32621a60` (commit `6ff9aa77…`) | government_decision | **verified** | Lawful, effective, properly gated Act 26 compliance-monitor implementation. Exact-commit pre-landing record (c1a00007, board pin, suite green) and post-landing `suite-status.json` naming exact commit/tree both present. I independently re-ran the added hermetic smoke test: `passed`, EXIT=0. |

Full evidence strings are durable in `state/oversight/random/outcomes/<case>.json`.

## Verified evidence, uncertainty and leading indicators

- **Verified independently:** `git ls-remote` refs for skrynia-tools and Skrynia
  PR heads; antonina merge ancestry via bounded blobless clone; board state,
  author labels and absence of `Vitalik` comments on all three issues; the
  `6ff9aa77` diff, its pre/post-landing gate chain, and the smoke-test result
  (re-run by this office).
- **Uncertainty:** every host finding rests on board author labels and explicit
  self-statements, not independent host telemetry. No project test suite
  (cargo/npm) was re-run locally. Deployment states on marceline-dev/phoebe-dev
  come from board reports, not live production telemetry. skrynia-apps PR #293
  was not confirmed by unauthenticated `ls-remote`.
- **Leading indicators only:** scheduler-turn `state: working` messages, agent
  liveness, PR counts and draft PRs. None counted as delivery or as neglect.

## Sampling and measurement limitations

- Four cases from snapshot `0691b8bf…` (seed after snapshot `ac3aaee0…`) out of
  a universe of 345 claimed-delivery, 40 government-decision and 47
  ignored-work cases. This is not a census; selective or intermittent problems
  can evade it.
- Three `finding` verdicts are **host-policy** findings (two plus one combined
  with a gate issue), not findings that the assigned work was poor or absent.
  Two sampled issues were external Skrynia projects with no billy-dev
  assignment, so no Viche duty to complete them arises under Act 9; the
  reported deliverables were in fact independently confirmed on Git remotes.
  Stating this guards against the false positive of reading a host finding as a
  quality failure.
- The `304` finding is specifically that an acceptance criterion (phoebe-dev
  deployment/verification) has no positive evidence yet the issue is closed;
  absence of that evidence counts against the completion claim, not as proof of
  misconduct or a particular cause.
- False-negative risk on `303ead1e0d`: I confirmed the diff, gate records and
  smoke-test behaviour, not the full `tests/run-all.sh` (the record lists CI as
  `unavailable`). The pre-landing record transparently documents a first full
  suite attempt killed by an OOM (exit=null) and a second green run on the exact
  commit; I did not re-derive that run.
- Missing measurements: host telemetry, reproduced external test suites, live
  deployment verification on the named hosts. All labelled, none filled with
  assertions.

## Judiciary's own operations

- Verdicts were filed once only; no duplicate post, correction, case write,
  cursor movement, merge or dispatch was performed.
- Delivery of this report follows the predecessor's recorded lesson: the
  long-lived seat branch `judiciary/audit-cycle-ec850b40-20261107` has diverged
  from `main` and would carry stale shared records; therefore this additive
  report is proposed from a fresh branch based on current `origin/main`
  containing only this file. This is delivery of a record, not a reform of any
  measurement system or of Judiciary's own operation; no reform is proposed.
- Continuity cases remain `verified_closed`; no new terminal evidence was
  supplied, so no `verified-OFFICE.json` receipt was written or amended. The
  one-time retrospective Founder-withdrawn-amendment review remains complete
  and unchanged; no new substantive evidence required a repeat.
- Verdict records are auditable assertions with evidence strings, not machine
  proofs; the `auditor_report_not_independent_proof` caveat is retained by the
  tool.

No legislative, policy or implementation action was taken by the Judiciary.
