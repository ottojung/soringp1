# Judiciary fact-finding — dispatch cycle `9ea624fcbbbc0cca9a5874ffd9cb9d34`

Recorded 2026-11-19T15:21Z. Verdicts filed once at epoch `1795101676`
(2026-11-19T15:21Z). Independent judicial audit under Acts 4, 8, 9, 15, 16,
18, 21, 23 and 26. No law, policy, measurement machinery, case state, mailbox
item, correction or reform proposal was made. Mailbox inbox is empty and the
mandatory cross-branch corrective-case list is empty (`open_cases: []`).

This is a **new** four-case cycle (new token, new frozen sample, snapshot
`0e0dee04…`, seed `922b8d9c…`, universe 345 claimed-delivery / 40
government-decision / 47 ignored-work), distinct from the prior `feb575fa…`
cycle whose report landed on `main`.

## Method

- Read the four frozen case files under `state/oversight/random/cases/` and
  re-fetched each named board issue with `antonina board show --id … --page N
  --json` across every available page (1 page = 14 messages; 4 pages = 160
  messages; 1 page = 16 messages), scanning every message for an author
  exactly `Vitalik`, host-assignment text and terminal state.
- Host assignment was taken from each issue's own description and board
  history, never from an executive list. GitHub-hosted CI is permitted;
  Viche/OpenClaw managed-agent execution on `marceline-dev` is not CI and does
  not become CI merely because the work involves GitHub PRs.
- Claimed Git artifacts were verified independently of reporter handoffs with
  `git ls-remote` on `ottojung/skrynia-tools` and `ottojung/vau.place`, plus a
  direct raw-content fetch of the delivered design document. The government
  decision was checked in canonical `/var/lib/lubko/wd/viche` with `git show`,
  `git rev-parse`, `git merge-base --is-ancestor`, `git log -S`, a SHA-256
  recomputation of the bill, and `sh government/tally.sh`.
- Current ordinary law was read at `/var/lib/lubko/wd/viche/government/LAWS.md`
  (Acts 4, 9, 15, 16, 17, 18, 21, 26, 27) and `OVERSIGHT.md` §§26–71.
- One verdict per sampled case was filed with `government/audit-accountability.py
  report`. No `--correction` was used: none of these cases had a prior verdict.

## Sampled cases (4) — verdicts filed

| Case | Population | Verdict | Short basis |
|---|---|---|---|
| `62d8fe97b6b10b03f6` (issue `ipRFNZeTtpMUTnklPM6EWQ-erection`) | ignored_work | **finding** | Host-policy only. No `Vitalik` author and no billy-dev assignment (14 messages), so no Act 9 duty / no neglect. Multiple comments explicitly place managed agents on marceline-dev (07:47Z "LIVE OWNER on marceline-dev: agent JyStr…"; 11:20Z checkpoint "(marceline-dev)"; 12:33Z "(marceline-dev, /tmp/opencode/iprfn-lock-qual-work)"). `git ls-remote` confirms all three claimed skrynia-tools heads (`710851a`, `f22236e`, `49f5300`). Work explicitly partial/draft with blockers; no deployment. Not false delivery. |
| `4250723ea6593473b8` (issue `310`) | ignored_work | **finding** | Host-policy only. No `Vitalik` author (160 messages). Body is a legislature-only draft, "NOT ASSIGNED EXECUTIVE WORK" (Act 20 subsequently enacted), so no productive duty / no neglect. Repeated agents self-report marceline-dev and stop (e.g. 2026-10-30T10:55Z "host: marceline-dev | policy: Execution-Host billy-dev only … stopping"; 2026-11-03T10:43Z "Current host is marceline-dev"). Not false delivery. |
| `42c68ad4639a954c11` (issue `223`) | claimed_delivery | **finding** | Host-policy only; delivery independently verified. 14 messages authored `openclaw@marceline-dev` (work predates the 2026-10-29 billy-dev-only directive, noted). `git ls-remote ottojung/vau.place` confirms both claimed heads `1ac3687` and `ac999d9`, and raw content at both SHAs serves the design-only `prologue.md` for issue #223. Not false delivery. |
| `80421c5c0d1e5640a0` (commit `43524f5…`) | government_decision | **finding** | Act 21 gate-recording failure, not lawlessness or red tests. Lawful, effective sponsor rebuild of the Act 26 bill commit: ancestor of `origin/main`, bill SHA-256 recomputed as `7ba42264…` (unchanged), s8 red-team and s9 response present, ballot published, `tally.sh` PASSED 6-3-1 (quorum 6), Act 26 codified. But `records/suite-status.json` at this exact commit/tree names unrelated `d56fb63`/`cafe6024`, and no exact-commit/tree record exists. |

Full evidence strings are durable in `state/oversight/random/outcomes/<case>.json`.

## Verified evidence, uncertainty and leading indicators

- **Verified independently:** board author labels and absence of `Vitalik` on
  all three issues; explicit marceline-dev self-statements; `git ls-remote`
  refs on both external repos; raw design-document content at two exact SHAs;
  the `43524f5` diff, ancestry, bill digest, red-team/response sections, tally
  result and missing exact-commit suite record; current law text.
- **Uncertainty:** every host finding rests on board author labels and agent
  self-statements, not independent host telemetry. No external cargo/npm test
  suite was re-run locally. Raw remote content and `ls-remote` confirm artifact
  existence, not the full acceptance criteria or VM integration. The Act 21
  finding establishes missing verification evidence, not that `records-smoke`
  was red or that the enactment was unlawful.
- **Leading indicators only:** `LIVE OWNER`/`state: working` scheduler turns,
  agent liveness, PR/branch counts and draft status. None counted as delivery or
  as neglect.

## Sampling and measurement limitations

- Four cases from snapshot `0e0dee04…` (seed `922b8d9c…`) out of a universe of
  345 claimed-delivery, 40 government-decision and 47 ignored-work cases. This
  is not a census; selective or intermittent problems can evade it.
- Three `finding` verdicts are **host-policy** findings, not findings that the
  assigned work was poor or absent. Two sampled issues were external Skrynia
  projects with no billy-dev assignment, so no Viche duty to complete them
  arises under Act 9. Stating this guards against the false positive of reading
  a host finding as a quality failure.
- Issue `223` was closed and its design deliverable exists on the exact claimed
  heads; the finding is strictly the execution host, not non-delivery.
- Issue `310`'s draft body is stale (the bill was enacted as Act 20); I did not
  re-audit the implementation-gap narratives on that thread.
- Missing measurements: host telemetry, reproduced external test suites, live
  deployment verification. All labelled, none filled with assertions.

## Judiciary's own operations

- Verdicts were filed once only; no duplicate post, correction, case write,
  cursor movement, merge or dispatch was performed.
- Delivery of this report follows the recorded lesson from cycle `feb575fa…`:
  the additive report is proposed from a fresh worktree based on current
  `origin/main` containing only this file; no untracked copy was written into
  the canonical checkout. This is delivery of a record, not a reform of any
  measurement system or of Judiciary's own operation; no reform is proposed.
- Continuity cases remain `verified_closed`; no new terminal evidence was
  supplied, so no `verified-OFFICE.json` receipt was written or amended. The
  one-time retrospective Founder-withdrawn-amendment review remains complete
  and unchanged; no new substantive evidence required a repeat.
- Verdict records are auditable assertions with evidence strings, not machine
  proofs; the `auditor_report_not_independent_proof` caveat is retained by the
  tool.

No legislative, policy or implementation action was taken by the Judiciary.
