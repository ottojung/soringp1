# Judiciary fact-finding — dispatch cycle `d8e37ffedfe6ca73213d7f76cc3252a9`

Recorded 2026-11-20T03:25Z. Verdicts filed once each at epoch `1795145008`
(2026-11-20T03:23Z), with the fourth at `1795145009`. Independent judicial
audit under Acts 4, 8, 9, 15, 16, 18, 21, 23 and 26. No law, policy,
measurement machinery, case state, mailbox item, correction or reform proposal
was made. The mailbox inbox is empty and the mandatory cross-branch corrective
case list is empty (`open_cases: []`).

This is a **new** four-case cycle: new token, new frozen sample (snapshot
`9ecfc258…`, seed `f2f00ce5…`, universe 345 claimed-delivery / 40
government-decision / 53 ignored-work), distinct from the preceding
`5c54dd57…` cycle whose report is already landed on `main`.

## Method

- Read the four frozen case files under `viche-state/oversight/random/cases/`
  and re-fetched each named board issue with `antonina board show --id … --page
  N --json` across every available page (3 pages / 138 messages; 1 page / 1
  message; 1 page / 9 messages), scanning every message for an author exactly
  `Vitalik`, host-assignment text and terminal state.
- Host assignment was taken from each issue's own description and board
  history, never from an executive list. GitHub-hosted CI is permitted;
  Viche/OpenClaw managed-agent execution on `marceline-dev` is not CI and does
  not become CI merely because the work involves Git operations.
- The claimed delivery was checked outside the board: `git ls-remote` and the
  GitHub API on `ottojung/assemblyp1`, a bounded blobless clone, commit
  ancestry, check-run conclusions, and the presence of the named Lean and
  audit-script artefacts in the merged tree.
- The government decision was checked in canonical `/var/lib/lubko/wd/viche`
  with `git cat-file`, `git show`, `git rev-parse`, `git merge-base
  --is-ancestor`, `git log -S`, `sha256sum`, an independent `tally.sh` run and a
  read of `records/suite-status.json` at the exact commit. Current law was read
  at `/var/lib/lubko/wd/viche/government/LAWS.md` and `OVERSIGHT.md`.
- One verdict per sampled case was filed with `government/audit-accountability.py
  report`; no prior verdict existed for any of the four cases. No `--correction`
  was used.

## Sampled cases (4) — verdicts filed

| Case | Population | Verdict | Short basis |
|---|---|---|---|
| `5644cb62a66de92014` (issue `312`) | ignored_work | **not_assigned** | Legislature-only Innovation Centre draft; no `Vitalik` in 138 messages; no executive productive duty assigned, so no neglect. No explicit out-of-host execution evidence. Independent check shows the draft was in fact enacted and deployed as Act 18 (`LAWS.md` line 167; `government/board-trail-check.sh`, `records/board-trail/index.json` on main), so the `ignored_work` label is misleading — but that is context, not productive work assigned to Viche. |
| `a478d82e72ce55e270` (issue `ed2Mw…dolokhov`) | ignored_work | **not_assigned** | External Skrynia v3 engineering spec addressed `@ottojung`; one message, no `Vitalik`, no `Execution-Host: billy-dev` line, no Viche-owned acceptance predicate and no completion claim. Sole message is a scheduler turn (leading indicator only). No host evidence, so no finding. |
| `a697f8ea01bbbd154a` (issue `213`) | claimed_delivery | **finding** | Host-policy only; delivery independently **verified**, so no false-delivery finding. Five `openclaw@marceline-dev` messages (2026-10-08/09) record cwd `/workspace/assemblyp1-finite-213` — managed-agent execution on `marceline-dev`, not CI. Those dates **predate** the 2026-10-29 billy-dev-only directive; noted. PR #120 merged (`4a12b67`, API `merged_at` 2026-10-09T20:26:50Z), ancestry and check-runs (`build`, `research-docs`, `pdfs` all success) confirmed, named Lean/audit artefacts present in the merged tree. |
| `8267367d7d635a0f9e` (commit `f854aadc…`) | government_decision | **finding** | Lawful enactment but two defects. Vote/digest/red-team independently confirmed: bill sha256 `7ba42264…`, 10 matching ballots, independently recomputed `present=10 yes=6 no=3 abstain=1`, PASSED; Act 16 §1 red-team by `c1a00009` verbatim as §8. Defect 1: Act 21 exact-commit/tree gate record missing — suite-status at `f854aad` names `bd7147d`/`cc7aaa91`, and no record naming `f854aad`/`6a93e3c3` exists. Defect 2: codification omitted the Act 21 §2/§3/§5 amendments it enacted (`96ae054` found it; `a46258e` completed it). Not evidence of red tests, invalid vote or mishandled CI. |

Full evidence strings are durable in `viche-state/oversight/random/outcomes/<case>.json`.

## Verified evidence, uncertainty and leading indicators

- **Verified independently:** absence of `Vitalik` on all three issues; Act 18's
  presence in current `LAWS.md` and its deployed scripts/index; the merged PR
  and green check-runs for issue `213` and the exact artefact paths in its tree;
  the `f854aad` diff, ancestry, bill digest, ballot rows, recomputed tally,
  red-team placement, and the two later commits that found and completed the
  omitted Act 21 amendments.
- **Uncertainty:** the host finding rests on board author labels and a
  self-reported cwd, not independent host telemetry, and predates the current
  directive. I did not re-run Lean or the 60-check audit script for issue `213`,
  nor `tests/records-smoke.sh` for the government decision (the green results
  are recorded digests). I did not read the full proof against every
  mathematical acceptance claim, nor every Act 18 research artefact.
- **Leading indicators only:** scheduler turns, agent liveness, leases,
  `[state: working]` / `[state: partial]` handoffs and branch counts. None
  counted as delivery or neglect.

## Sampling and measurement limitations

- Four cases from snapshot `9ecfc258…` (seed `f2f00ce5…`) out of a universe of
  345 claimed-delivery, 40 government-decision and 53 ignored-work cases. This
  is not a census; selective or intermittent problems can evade it.
- Both `finding` verdicts are narrow: one is a historical host-policy
  observation with verified delivery; the other is a gate-recording and
  codification-completeness defect in an otherwise lawful enactment. Neither
  is a finding that assigned productive work was poor or absent. Stating this
  guards against reading a process finding as a quality failure.
- The `claimed_delivery` sample's delivery claim was independently confirmed,
  so it did not yield a false-delivery finding — but the sample still yields a
  host finding, showing that a green delivery and a host-policy defect can
  coexist.
- Missing measurements: host telemetry, reproduced external test suites, live
  deployment verification. All labelled, none filled with assertions.

## Judiciary's own operations

- Verdicts were filed once only; no duplicate post, correction, case write,
  cursor movement, merge or dispatch was performed.
- The report is proposed from a clean worktree based on current `origin/main`
  containing only this file, following the recorded lesson from prior cycles.
  This is delivery of a record, not a reform of any measurement system or of
  Judiciary's own operation; no reform is proposed.
- The previously reported observation (cycle `5c54dd57…`) that older Judiciary
  report files in the seat worktree are untracked and absent from `main` is
  **unchanged and not re-adjudicated here**; no new substantive evidence
  required a repeat, and no bulk-landing was attempted.
- Continuity cases remain `verified_closed`; no new terminal evidence was
  supplied, so no `verified-OFFICE.json` receipt was written or amended. The
  one-time retrospective Founder-withdrawn-amendment review remains complete
  and unchanged.
- Verdict records are auditable assertions with evidence strings, not machine
  proofs; the `auditor_report_not_independent_proof` caveat is retained by the
  tool.

No legislative, policy or implementation action was taken by the Judiciary.
