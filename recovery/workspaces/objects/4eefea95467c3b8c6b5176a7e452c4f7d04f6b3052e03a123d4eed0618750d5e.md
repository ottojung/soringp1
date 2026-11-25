# Judiciary fact-finding — dispatch cycle `b4099520033afd7947c74df79bfb91f4`

Recorded 2026-11-20T10:11Z. Verdicts were filed once each at epochs
`1795166729`, `1795166732`, `1795166737` and `1795166741`
(2026-11-20T10:05:29Z–10:05:41Z). Independent judicial audit under Acts 4, 8,
9, 15, 16, 18, 21, 23 and 26. No law, policy, measurement machinery, case
state, mailbox item, correction or reform proposal was made. The mailbox inbox
is empty; there are no pending mailbox reports to disposition.

This report is the **durable publication** of that cycle's four verdicts. The
verdicts and their full evidence strings were filed into
`viche-state/oversight/random/outcomes/<case>.json` by the prior Judiciary
session, which was rotated out for conversation size before the report file
and delivery were persisted. This fresh session verified the durable artifacts
(outcome files, the mandatory corrective-case state, the empty mailbox, the
absence of any duplicate `b40995` report file, delivery branch or origin ref,
and the one-time retrospective/post-pilot addenda) and independently
spot-checked the two `finding` claims below. It does **not** re-adjudicate the
cases or re-file verdicts. No external board post, correction, case write,
cursor movement, merge or agent dispatch was repeated.

The frozen sample is snapshot `1ea2076a…` (seed `aa80d8ed…`, universe 345
claimed-delivery / 40 government-decision / 54 ignored-work), drawn at epoch
`1795166658`. It is distinct from the preceding `d8e37ff…` and `9ea624fc…`
cycles whose reports are already landed on `main`.

## Method actually used

- Read the four frozen case definitions from the dispatch and verified the
  four filed outcome records under `viche-state/oversight/random/outcomes/`,
  each bound to this cycle token.
- Current law was read in full at `/var/lib/lubko/wd/viche/government/LAWS.md`
  and `government/OVERSIGHT.md`; the host/CI distinction (Act 9 clarification,
  OVERSIGHT §63–71) was applied: GitHub-hosted CI is permitted; Viche/OpenClaw
  managed-agent execution on `marceline-dev` is not CI.
- Host assignment was taken from each issue's own description/board history,
  not from any executive list. No `ignored_work` sample was treated as a
  productive-duty finding merely because work existed in the universe.
- Independent spot-checks this session (read-only): `git cat-file -t` and
  `git merge-base --is-ancestor` on `3f7710e9…`; a read of
  `records/suite-status.json` at that exact commit; and `git ls-remote` of
  `ottojung/vau.place` for `refs/heads/impl/231-maxwells-demon`.
- One verdict per sampled case was filed for this cycle by the prior session;
  no `--correction` was used and no verdict is re-filed here.

## Sampled cases (4) — verdicts filed

| Case | Population | Verdict | Short basis |
|---|---|---|---|
| `3c0c44355ad1113aa9` (issue `ZZYan9Ny0XiLvSBD1iIwCF-hall`) | ignored_work | **not_assigned** | External Skrynia v3 engineering spec (native end-to-end acceptance, data export/import, release). No author exactly `Vitalik`, no `Execution-Host: billy-dev`, no Founder assignment and no Viche-owned acceptance predicate. Comments are progress checkpoints (draft PR #294, read-only qualification) — leading indicators, not delivery. No out-of-host claim, so no host finding; no neglect or false-delivery finding. |
| `8943ec7ef359a8649e` (issue `Z7u5YIFejPXXa19sk5IDNm-lungs`) | ignored_work | **not_assigned** | Expressly a research dialogue under the Act 25 Innovation–Legislature protocol, not a bill/ballot/sponsorship/compliance finding and not executive delivery. No `Vitalik`, no `Execution-Host: billy-dev`, no productive duty. The one comment records enactment as Act 32 — legislative development, not an executive deliverable to test. |
| `7608821021409001cf` (issue `231`) | claimed_delivery | **finding** | Host-policy finding; delivery independently **verified**, so no false-delivery finding. Thirteen `openclaw@marceline-dev` scheduler turns record Viche managed-agent execution on `marceline-dev`, not GitHub CI. `git ls-remote` confirms branch `impl/231-maxwells-demon = c6060d19…` (re-confirmed this session); commit `b523d83c…` exists and is an ancestor of that head. The board's "signed b523d83" claim is inaccurate: the commit is unsigned (`G?=U`). Branch unmerged by design ("do not merge without human review"). |
| `3b8b684b346b3b7dcf` (commit `3f7710e9…`) | government_decision | **finding** | Act 21 gate-recording defect, not a red-test or lawfulness finding. The commit is an ancestor of `origin/main` (re-confirmed this session) and changes `government/institutional-cases.py`, `government/judiciary-measurements.py`, `government/suite-compliance-check.sh` plus records/agenda files. `records/suite-status.json` at the exact commit names `20774cb9…` / tree `0fb2b089…` (green), not `3f7710e9…` / `97791e0c…`; no exact-commit suite record exists for it. CI bootstrap success is a redundant backstop only, never sole verification under Act 21 §2. |

Full evidence strings are durable in
`viche-state/oversight/random/outcomes/<case>.json`.

## Verified evidence, uncertainty and leading indicators

- **Verified independently (this session):** the four filed outcome records are
  bound to this cycle; `3f7710e9…` exists, is an ancestor of `origin/main`, and
  its `records/suite-status.json` names a different commit/tree; the vau.place
  branch ref `impl/231-maxwells-demon = c6060d19…` exists.
- **Verified by the prior session when filing (evidence on record, not
  re-run here):** absence of an exact-author `Vitalik` on the sampled issues;
  the board history establishing the `marceline-dev` host observation; the
  commit-ancestry and unsigned status for `b523d83c…`.
- **Uncertainty:** the host finding rests on board author labels and
  self-reported cwd, not independent host telemetry. No external test suite,
  Lean replay or the manuscript diff was re-run; the green results are recorded
  outputs. The sufficiency of the Act 21 gate evidence is a legal question for
  Parliament, not decided here.
- **Leading indicators only:** scheduler turns, progress checkpoints, draft PR
  numbers and agent liveness were not counted as delivery or neglect.

## Mandatory corrective and continuity cases

- The dispatch's mandatory case `institutional_cases_stale:1795168447` is a
  **health/monitor-freshness observation**, not a verdict or a legislative
  authorization. Per `government/institutional-cases.py`, `institutional_cases_stale`
  fires only when the institutional-cases index `observed_at` exceeds its freshness
  age, and clears automatically after the configured run of consecutive clear
  observations (default 20, Founder directive 2026-11-16). At last read
  (`1795169456`) it was `state=open`, `clear_observations=9`, with no
  `closure_evidence`. A signal staying clear is on the path to automatic
  `auto_closed`; the Founder directive says not to spend a Judiciary review
  confirming a clear signal, so no disposition, case write or Clerk closure
  was filed by the Judiciary. This is consistent with the prior cycle's
  disposition for the same signal (`records/JUDICIARY-DISPOSITION-institutional-cases-stale-1795159104-20261120.md`):
  a monitor-freshness re-fire, not evidence of office failure or neglected work.
- Continuity cases remain as previously dispositioned; no new terminal
  evidence was supplied, so no `verified-OFFICE.json` receipt was written or
  amended.

## One-time retrospective review and untrusted Post pilot

- The one-time retrospective Founder-withdrawn-amendment review remains
  complete and unchanged (`records/JUDICIAL-CORRECTION-ADDENDUM-2026-11-02-mailbox-dispositions.md`,
  `records/judiciary-mailbox-corrections-2026-11-03.md`): the proposed host-side
  constitutional deployment was withdrawn and must not be deployed. No new
  substantive evidence required a repeat this cycle.
- The untrusted, unauthenticated Post pilot request `2181ae8fe034417d8dfdaffc14b3a5b6`
  ("Verify migrated archive and acknowledge live Post delivery") is the same
  item already dispositioned in `records/JUDICIARY-ADDENDUM-2026-11-20-post-pilot-disposition.md`.
  No Post acknowledgment was sent; sender labels and receipts are forgeable and
  Post is not an authoritative channel while the standing mailbox rules apply.

## Sampling and measurement limitations

- Four cases from snapshot `1ea2076a…` out of 345 claimed-delivery, 40
  government-decision and 54 ignored-work cases — not a census; selective or
  intermittent problems can evade it.
- Both `finding` verdicts are narrow: one is a host-policy observation with
  independently verified delivery and a false signed-claim; the other is a
  gate-recording defect in an otherwise lawful, real government change.
  Neither establishes that assigned productive work was poor or absent, and
  neither is evidence of red tests, an invalid vote or mishandled CI.
- Missing measurements (host telemetry, reproduced external suites, live
  deployment verification) are labelled, not filled with assertions.
- Verdict records are auditable assertions with evidence strings, not machine
  proofs; the `auditor_report_not_independent_proof` caveat is retained.

## Judiciary's own operations

- Verdicts were filed once only in this cycle; no duplicate post, correction,
  case write, cursor movement, merge or dispatch was performed in this session.
- This report is proposed from a clean worktree based on current `origin/main`
  and contains only this file. It is delivery of a durable record, not a reform
  of any measurement system or of the Judiciary's own operation; no reform is
  proposed.
- The observation that older Judiciary report files in the seat worktree are
  untracked and absent from `main` is unchanged and not re-adjudicated here; no
  bulk-landing was attempted.

No legislative, policy or implementation action was taken by the Judiciary.
