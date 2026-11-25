# Second-office factual review: PR #32 (2026-10-23)

**Exact PR head:** `c140eb3d65e66c97846822788291a5dc2bed7155`; **tree:** `54ea0a1d122799bbebaf8bac3ad0c492ed5f9888`. Its GPG signature verifies as good for Otto Jung (local trust unknown). GitHub API reported PR #32 open/unmerged at review time. At that exact detached worktree, `sh tests/records-smoke.sh` exited **0** with:

```text
Viche: records carry no committed merge-conflict markers
```

## Scope and files

The final PR's merge-base change set adds eight audit Markdown reports (`AUDIT-2026-10-20b/c/d`, `AUDIT-2026-10-21a`, and four 2026-10-23 sample/reassessment/watchdog/reconstruction reports), two correction JSONLs, and an `AGENTS.md` refresh. Its merge base with the current main (`f21ab859c2ceecbb839fcf5a3f594c59efda5d01`) is `86627c2f4ee5d8b8afa9771bad76a471faff4c59`; on that change set, no `government/LAWS.md` or ballot path is modified. The AGENTS bytes at PR head match current main. A raw two-tree comparison with later main also shows main-only changes absent from the older PR tree; those are not PR #32 changes and must not be treated as deletions in its merge. Historical report text that refers to `phoebe-dev` is time-bound; current main's assignment scope is `billy-dev`, and this PR does not change it.

## Source preservation and correction rows

Compared the two PR #32 logs with both the current untracked canonical source files and the archived sources plus manifest merged to main by PR #34:

| Case | Canonical and PR #34 archive | PR #32 log | Differences in common rows |
|---|---|---|---|
| `7750b56b775ed8959a` | 4,195 bytes; 3 rows; SHA-256 `a3d1236a98eb637afcd8d6822ff8e63c16dc4b4f70a407b83ef9ff76b9b29196`; exact byte match. | 5,634 bytes; 4 rows; SHA-256 `80d46bc660cf3bc51cf42c7ee469d54ca542b59a5c763da861fc6a6b7b2ad242`. | `evidence_ref` differs at `1792738483` and `1792741896`; `1792738485` matches. |
| `edb67f8a646f569b5a` | 4,441 bytes; 3 rows; SHA-256 `bf7bf5fd3e7b04c6a0f8e12f82b189e7f67b519f38a324a5309cde8c0919ce20`; exact byte match. | 6,183 bytes; 4 rows; SHA-256 `79fa17e3351e215a4e1aa663752225c8cc1600fea09ed462f00061f3d952e28f`. | `why_stronger` differs at all three matching timestamps. |

The PR #34 manifest's hashes, byte counts, row counts and field-difference maps match the sources and PR #32 logs. Each PR #32 file retains the earlier `inconclusive`→`finding` event, its same-office confirmation, the later `finding`→`not_assigned` correction, and another same-office confirmation. The two archived originals preserve the alternative three-row source bytes; neither wording variant is erased. The absent original inconclusive outcome objects/citations remain absent, as the final reconstruction report says.

## Act 17 process and authorization limit

All four confirmation rows name the same Auditor office (`c1e00008`) and are explicitly `second_procedural_pass_not_independent`; they document procedural rechecks, not independent corroboration. The two correction filings per case are:

- #6: `inconclusive`→`finding` at `1792738483`; then `finding`→`not_assigned` at `1792741896`.
- Journal child: `inconclusive`→`finding` at `1792738435`; then `finding`→`not_assigned` at `1792741902`.

Each filing is followed by a same-office pass. The records and reports tie both corrections to the same frozen draw `1792737985`, state no new sample was drawn, and place the two filings about 65 minutes apart. Act 17 §2.6.1 limits corrections to **one per case per audit cycle**; `OVERSIGHT.md` describes an ordinary audit cycle as six hours. No distinct cycle id or intervening draw is documented. On that ordinary reading, each case has two corrections in one cycle, an apparent cap violation. In this tree, `audit-accountability.py` blocks a filing only while `correction_pending` is true; confirmation clears that flag, after which another correction can be accepted. The code does not record a cycle identifier or count prior corrections within a cycle. That implementation behavior does not establish statutory compliance. A different interpretation of “cycle” is possible, but these records do not demonstrate separate cycles. I therefore cannot certify the final correction chains as fully Act 17-compliant or independently proven.

The reasoned second corrections add scope evidence (external repository/body and no visible `billy-dev`/Founder assignment) beyond the first board-gap finding. That supports why the Auditor changed its view, but does not remove the one-per-cycle concern. The first inconclusive submissions and their source references are not in the retained event history; the Auditor's reconstruction accurately leaves the third claimed placeholder unidentified.

## Report accuracy and material caveats

- The retained cases/outcomes match the four verdicts in `AUDIT-2026-10-20b.md` and all eight verdicts in `AUDIT-2026-10-20c.md`; all eight sibling/primary case records share draw `1792509955`, and current outcomes match the report's four `not_assigned` / four `verified` summary. Outcome time `1792530685` is 20,730 seconds after that draw, within six hours. The incident reports 20b, 20d and 21a describe the watchdog signals also retained in `/var/lib/lubko/wd/viche-state/oversight/history.jsonl` and `observations.tsv`.
- I found three timing discrepancies in those incident narratives: (1) 20b states the `1792464244` clear was at `1792464314`, while retained history and observations record `1792464303` (11 seconds earlier); (2) 20d renders epoch `1792536588` as `20:49:48Z`, whereas direct UTC conversion is `22:49:48Z`; (3) 21a renders `1792546733` as `01:52:13Z`, whereas direct UTC conversion is `01:38:53Z`. In 21a, `first_seen=1792546733` to `closed_at=1792548421` is 1,688 seconds (28m08s), so “cleared within one interval” is not established by the cited timestamps absent a stated interval of that length. These affect timestamp precision, not the existence of the retained incident/clear records.
- The Oct 23 reconstruction's #255 563-second interval and 83.094-second public-comment gap are arithmetically correct. It appropriately leaves the conflicting earlier “filed”/health statements unresolved. The Oct 23 reports explicitly distinguish external board gaps from Viche assignment, retain null FP/FN and `measurement_reliability: not_established`, and identify same-substrate limits. They are reports of evidence and assertions, not proofs of underlying truth.
- `AUDIT-2026-10-20c.md` includes eight findings/operations as dated observations and cites source inspection and tests; those tests/board queries are not all embedded as raw outputs in PR #32. This review did not repeat every historic external repository investigation. The audit narratives should therefore be published as attributed, time-bounded evidence with their stated verification limits.

## Verdict

**Qualified yes for publication as historical factual evidence:** the report bundle is signed, exact source variants are preserved, the manifest is accurate, and the scoped records test passes. **Not an unqualified Act 17 compliance endorsement for the operative correction histories:** the apparent two-corrections-per-case/per-six-hour-cycle issue remains unresolved. Publication must not be represented as independent verification of the audits or as adjudication of the cap question. PR #32 changes no law or ballot, and this review neither votes nor enacts law. A future merge still requires Act 21 §1 verification on the exact merge commit/tree by the Clerk or authorized substitute; the test above is for PR head `c140…` only.
