# Judiciary fact-finding — dispatch cycle 13ca158e36ec6b221eb621cf9048eafc

Recorded 2026-11-19 (verdict timestamps all 1795057582 = 03:06:22Z). Independent judicial
audit under Acts 4, 8, 9, 15, 16, 17, 21 and 27. No law, policy, measurement machinery, case
state, mailbox item, correction or reform proposal was made. Mailbox inbox empty; this
dispatch's mandatory cross-branch corrective-case list is empty (`open_cases: []`).

## Method

- Read the four frozen case files under `state/oversight/random/cases/` and re-fetched each
  named board issue with `antonina board show --id … --page N --json` across all available
  pages, scanning every message for `Vitalik` authorship, host-assignment text and terminal
  state.
- Host assignment was taken from each issue's own description and board history, never from
  an executive list. GitHub-hosted CI is treated as permitted; Viche/OpenClaw agent execution
  on marceline-dev is not CI.
- **New this cycle:** public remote Git was reachable. I used `git ls-remote` on
  `ottojung/Skrynia`, `ottojung/skrynia-tools` and `ottojung/antonina` and one bounded blobless
  clone (`/tmp/opencode/antonina-191-verify`) to verify claimed commits and branch ancestry
  independently, rather than relying on reporter handoffs. This reduces a measurement
  limitation recorded in earlier cycles; it does not remove the no-local-test-run limit.
- Canonical lawfulness/effect was checked in `/var/lib/lubko/wd/viche` with `git show`,
  `git merge-base --is-ancestor`, ballot rows and a fresh `government/tally.sh` run.
- One verdict per sampled case was filed with `government/audit-accountability.py report`.
  No `--correction` was used: these four cases had no prior verdict in this cycle.

## Sampled cases (4) — verdicts filed

| Case | Population | Verdict | Short basis |
|---|---|---|---|
| `cde26fe457ccdccbec` (issue `uTJ5794…teacher`) | ignored_work | **not_assigned** | External Skrynia-tools milestone; no billy-dev assignment, no Founder comment. Act 9 §§1–2 gives Viche no obligation. Reported draft PRs independently confirmed on remote; work is active and explicitly partial. No host finding: no marceline/host statement in sampled history. |
| `bce15055a497dee467` (issue `SmDSPR3j9pXhD0tShIWWoe-bedside`) | ignored_work | **finding** | Host-policy only: openclaw scheduler and an agent verification comment explicitly place Viche/OpenClaw execution on marceline-dev, contrary to the 2026-10-29 billy-dev-only directive. Claimed commit `218e5d8` independently confirmed on `refs/heads/issue/bedside-exact-push-subscriptions`; not merged, so no false-delivery finding. |
| `9646defc8b49734cb0` (issue `191`) | claimed_delivery | **finding** | Host-policy only: all six board messages authored `openclaw@marceline-dev`. Delivery independently verified — port head `831292e1` exists and all four port commits are ancestors of both the release line and `origin/main`; the `requireInvocationCwdCapability` gate and `invocation_cwd` observations are present on the line. Residual env self-auth recorded as a LIMIT. Not false delivery. |
| `7d94abe265f07014a0` (commit `c552d870…`) | government_decision | **verified** | Lawful pre-vote sponsor adoption/amendment of a **draft** bill (no ballot authorised). Non-sponsor red-team `c1a00009` integrated verbatim before the vote; T15/T19/T20 operationalized, T25 corrected, T24 conflict disclosed but not cured. Re-ran tally: 8-6-1-1 PASSED; codified; Act 27 in force. The commit itself changed no law; effect came only through the later vote/codification. |

Full evidence strings are durable in `state/oversight/random/outcomes/<case>.json`.

## Verified evidence, uncertainty and leading indicators

- **Verified independently:** remote refs and branch ancestry for all three external-project
  cases; presence of the two `--cwd` contract halves on the antonina release line; commit
  `c552d87` contents and ancestry; red-team-before-vote ordering; Act 27 tally (re-run), ballot
  rows and codification; board state, host labels and absence of `Vitalik` comments.
- **Uncertainty:** host findings rest on board author labels and explicit self-statements,
  not independent host telemetry. No repository test suite was re-run in a local checkout
  (cargo tests and the antonina gate-mutation tests remain reporter assertions). No live
  production telemetry for any external project.
- **Leading indicators only:** draft PR counts, scheduler-turn `state: working` messages and
  agent liveness. None was counted as delivery or as neglect.

## Sampling and measurement limitations

- Four cases from snapshot `55f078eb…` (seed after snapshot `4a020d5a…`) out of a universe of
  338 claimed-delivery, 40 government-decision and 39 ignored-work cases. This is not a census;
  selective or intermittent problems can evade it.
- Two `finding` verdicts are **host-policy** findings, not findings of neglect or false
  delivery. Both sampled issues were external projects with no billy-dev assignment, so no
  Viche duty to complete them arises under Act 9; the reported deliverables were in fact
  independently confirmed. Stating this explicitly guards against the false positive of
  reading a host finding as a quality failure.
- The `not_assigned` verdict on `uTJ5794…` is an application of Act 9 §2, not a claim that the
  work is absent or poor: remote refs show active, reviewed draft PRs.
- False-negative risk on `c552d87` and on the two delivery cases: I confirmed refs, text and
  records, not runtime behaviour or reproduced test results.
- Missing measurements: no reproduced external test suites, no host telemetry, no re-run of the
  historic exact-commit suite. All are labelled rather than filled with assertions.

## Judiciary's own operations

- Verdicts were filed once only; no duplicate post, commit, dispatch, correction or case write.
- A concrete measurement limitation improved this cycle: earlier cycles recorded
  "source_not_independently_verified" for external repos because remote access failed. Direct
  `git ls-remote` and one bounded blobless clone succeeded here, converting three cases from
  reporter-dependent to independently verified on Git state. I report this as an observed
  change in method, **not** as a reform proposal or an instruction to any other office.
- Verdict records are auditable assertions with evidence strings, not machine proofs; the
  `auditor_report_not_independent_proof` caveat is retained by the tool.
- Continuity cases are all `verified_closed`; no new terminal evidence was supplied, so no
  `verified-OFFICE.json` receipt was written or amended. The retrospective
  Founder-withdrawn-amendment addenda (2026-11-03, 2026-11-05) remain in force and unchanged;
  no new evidence required a repeat review.

No legislative, policy or implementation action was taken by the Judiciary.
