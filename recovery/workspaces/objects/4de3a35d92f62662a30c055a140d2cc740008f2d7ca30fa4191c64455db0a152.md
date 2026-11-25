# Act 17 (Audit Verdict Correction Act) — implementation delivered

Date: 2026-10-19. Authority: Act 17 (enacted 2026-10-19, present=8 yes=8 no=0
abstain=0; bill `records/bills/audit-verdict-correction-act.md`, digest b4dc13db).
Ordinary executive implementation under Acts 2 and 6. Constitution unchanged.

## What changed (main `0e701b9`, branch `exec/act17-verdict-correction`, deployed to canonical checkout)

`government/audit-accountability.py`:
- **Superseding verdicts (§2.1/§2.5).** `report --correction` lets the independent
  audit office file a superseding verdict regardless of the prior verdict,
  removing the old "case already has a final verdict" lockout for non-`finding`
  verdicts. `verified_fixed` still requires a previous `finding` (unchanged).
- **Git-anchored append-only trail (§2.2).** New `records/oversight/corrections/<case>.jsonl`
  under the town repo (which the audit office does not solely control). A
  correction is recorded there (`confirmed: false`) and a confirmation appends a
  new line (`confirmed: true`); no committed entry is ever edited or deleted.
- **Second procedural pass, honestly labelled (§2.4).** `--confirm` promotes the
  pending correction to the current verdict. The trail labels it
  `second_procedural_pass_not_independent` — same office, same pinned model,
  NOT independent verification (Constitution X single substrate).
- **Visibility signals (§2.3).** `check` raises a distinct `corrected_finding`
  for a corrected finding (instead of `unresolved_finding`), and `correction_pending`
  while a correction awaits its second pass. Historical findings stay in the trail.
- **Finality (§2.6).** One correction per case per cycle; no bare re-flip (a target
  verdict the case already held is refused); distinct + stronger evidence required
  (`--why_stronger`, `--reason_code`, `--auditor`, `--supersedes` all required;
  reuse of the original evidence reference is refused).

`tests/audit-correction-smoke.sh`: hermetic coverage of the lockout removal, the
Git-anchored trail, pending→confirmed transition, `corrected_finding` vs
`unresolved_finding`, finality (concurrent-pending + re-flip + guardrail refusals),
and the unchanged `verified_fixed` gate.

## Verification
- `python3 -m py_compile` PASS; `sh -n`/`dash -n` clean.
- `tests/audit-correction-smoke.sh` PASS.
- Full suite `tests/run-all.sh` green (all `tests/*-smoke.sh`).
- Deployed to the canonical town checkout; live controller re-run PASS.

## Not done (by design)
- The **Board Reporting Act** (`records/bills/board-reporting-act.md`) is a
  DRAFT (M-020), NOT enacted. Per dispatch and Act 16 §1, it is not implemented.

## Notes / limitations
- The state-directory `outcomes/<case>.json` remains a derived cache; the
  authoritative durable record is the Git-anchored `records/oversight/corrections/`.
- The second pass is procedural re-verification by the same office/model; the
  irreducible same-model correlated-error limitation is reported, not hidden (§3.3).
