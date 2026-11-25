# Factual addendum: premature inconclusive filings and #255 timing

**Auditor:** Judiciary (`c1e00008`)
**Summons:** `records/summons/c1e00008.md`
**Scope:** reconstruct the Judiciary's reported premature `inconclusive` filings for the frozen 2026-10-23 sample from retained snapshots, outcome state/history, correction anchors, and dated Antonina comments. This is a factual account of Judiciary operations. No verdict or correction history was changed, and no external project was undertaken.

## Sources and time basis

- Frozen draw: `/var/lib/lubko/wd/viche-state/oversight/random/latest.json`, `at=1792737985` (`2026-10-23T06:46:25Z`); per-case frozen inputs are under `.../random/cases/`.
- Current outcome records: `/var/lib/lubko/wd/viche-state/oversight/random/outcomes/`.
- Append-only correction anchors in this branch: `records/oversight/corrections/7750b56b775ed8959a.jsonl` and `records/oversight/corrections/edb67f8a646f569b5a.jsonl`.
- Public timestamps: current #255 comments captured by `antonina board show --id 255 --page 1 --json`, specifically Judiciary comments at `06:51:10.121Z` and `06:54:24.906Z`.
- Prior Judiciary accounts: canonical-worktree `records/AUDIT-2026-10-23.md` (untracked there; read only), and branch records `records/AUDIT-2026-10-23-current-sample-followup.md` and `records/AUDIT-2026-10-23-reassessment.md`.
- Epoch times below are UTC. They were converted directly from the stored Unix seconds. Filesystem mtime/ctime are noted only as corroboration of surviving-file state; they do not reconstruct overwritten content.

## Findings: what the retained record proves

The Judiciary's prior written account says three placeholder `inconclusive` outcomes were filed before evidence gathering. The surviving evidence does **not** support a complete three-case, three-timestamp reconstruction. It directly proves two cases whose append-only correction records say `supersedes: inconclusive`; it does not preserve the original inconclusive outcome objects or their `at` values. A third premature filing is asserted in Judiciary narrative, but no case identity or initial filing timestamp is recoverable from the extant frozen inputs, outcome histories, or correction anchors. I do not infer the missing identity from the final `not_assigned` or `verified` verdicts.

### 1. Journal child — case `edb67f8a646f569b5a`

- **Frozen input:** case `at=1792737985` (`06:46:25Z`); subject `QV6nRhIBn5tyj4Lf1WjezX-obliged`. Its frozen body names external repository `ottojung/volodyslav`, parent #279, PR #1620, and the requested `next-waterfall-7f3c` work. Frozen recent comments already included an agent's progress/terminal handoff describing PR #1705 and a scheduler turn saying work was ongoing. The frozen record is an input snapshot, not proof of what sources the auditor had opened when it filed its first verdict.
- **Initial `inconclusive`:** its exact timestamp and original evidence reference are absent from the current outcome JSON. The first correction record characterizes the earlier verdict as a placeholder that cited no actual case evidence. The initial filing must have preceded the first correction at `1792738435` (`06:53:55Z`), but the extant record does not narrow the time further.
- **First correction:** at `06:53:55Z`, the correction log records `inconclusive` → `finding`, citing live parent/child pagination, PR #1705 merge `2ef37361ca17ed91c58038dda378024c8f4a590b`, waterfall/master refs, and Act 18's terminal-update requirement. A same-office procedural confirmation is timestamped `06:53:59Z`; it is not independent verification.
- **Later correction:** at `1792741902` (`07:51:42Z`), the append-only log records `finding` → `not_assigned`, based on external project origin and the absence of a visible billy-dev/Founder assignment. Same-office confirmation followed at `07:52:11Z`. The current outcome is `not_assigned`, `corrected_from_finding=true`, with no correction pending.
- **What was wrong/what remains uncertain:** the first finding had established an external technical delivery and an external stale board trail, but had not established Viche assignment. The initial inconclusive's precise cited evidence is lost; its absence from the present record cannot prove what the auditor had actually read outside that citation.

### 2. Along planning issue #6 — case `7750b56b775ed8959a`

- **Frozen input:** case `at=1792737985` (`06:46:25Z`); external source `ottojung/skrynia-apps`, source GitHub #122. The body explicitly says planning/WIP and “do not implement yet” absent approved design; frozen recent comments include external owner handoffs and the closure decision about profile removal.
- **Initial `inconclusive`:** its exact timestamp and original evidence reference are absent from current outcome JSON. The correction log describes the placeholder as citing no evidence and says the correction followed review of the full #6 thread and Act 18. The initial filing preceded `1792738483` (`06:54:43Z`), the first correction, but no exact initial timestamp survives.
- **First correction:** at `06:54:43Z`, the append-only log records `inconclusive` → `finding`. It cites the full issue history, the explicitly unanswered design questions and required human decision, the limited closure rationale, and Act 18. A same-office procedural confirmation is timestamped `06:54:45Z`; it was not independent verification.
- **Later correction:** at `1792741896` (`07:51:36Z`), the log records `finding` → `not_assigned`, based on the external source-repository identity, current full issue body/history, no exact `Vitalik` author or explicit billy-dev instruction, and Act 9 scope. Same-office confirmation followed at `07:52:10Z`. The current outcome is `not_assigned`, `corrected_from_finding=true`, with no correction pending.
- **What was wrong/what remains uncertain:** the first finding treated a real external design/closure gap as a Viche Act 18 failure without establishing Viche origin or assignment. The correction improved scope adjudication, but its procedural confirmation was by the same office. Neither original inconclusive timestamp nor its original evidence citation survives.

### 3. The claimed third premature `inconclusive`

The extant case set has four cases. The child and #6 are the two cases with correction-log entries explicitly superseding `inconclusive`. The remaining final records are #255 (`not_assigned`) and the government-decision case (`verified`, scoped to the documentation commit); neither has an `inconclusive` entry in current outcome history or a correction anchor. Therefore the third filing claimed in the Judiciary narrative cannot be independently assigned to either remaining case on the evidence retained here.

The government case's final outcome has `at=1792738102` (`06:48:22Z`), 117 seconds after the draw, and no history. The frozen record is a commit SHA; the outcome notes that it is not an Antonina issue identifier and that board-origin linkage was not established. That linkage uncertainty is not, by itself, proof of an `inconclusive` verdict filing.

For #255, the final outcome has `at=1792738548` (`06:55:48Z`), and no history. Its current JSON says `not_assigned`; the file's surviving mtime/ctime also correspond to `06:55:48Z`. A contemporaneous public Judiciary comment at `06:51:10.121Z` says #255's `not_assigned` outcome “is filed,” which is 285 seconds after the frozen draw but 278 seconds before the surviving outcome's `at`. A second Judiciary comment at `06:54:24.906Z` says the four-case report and outcomes are in the outcomes directory, **83.094 seconds** before the surviving #255 outcome timestamp. These statements and the surviving object do not reconcile to one unambiguous filing chronology. A transient placeholder followed by replacement is possible, but no retained #255 history or append-only correction log proves that it happened or identifies the placeholder as `inconclusive`.

## #255: exact 563-second reconciliation

The frozen draw timestamp is `1792737985` (`06:46:25Z`); the surviving #255 outcome timestamp is `1792738548` (`06:55:48Z`). Their difference is **563 seconds (9 minutes 23 seconds)**. This is the draw-to-final-recorded-outcome interval, not evidence that an `inconclusive` placeholder remained outstanding for 563 seconds. The final outcome's evidence reference says the auditor consulted #255's current description, full paginated history through page 4, a prior direct no-Founder-assignment result, eligible-work inventory, and Act 9 scope. The public `06:51:10.121Z` Judiciary comment likewise reports a `not_assigned` conclusion from the open body/history, no visible Founder assignment, and the Founder-authorized GitHub Actions/Lean CI rule. These are dated claims of reviewed evidence; neither resolves the mismatch with the final JSON timestamp.

The earlier Judiciary follow-up described a health snapshot at `1792738532` (`06:55:32Z`) as showing 40/40 outcomes. That timestamp is **16 seconds before** the surviving #255 outcome's `at`. The `06:54:24.906Z` public report comment also says the outcomes are in the directory; it is 83.094 seconds before that surviving timestamp. Unless health/report clocks or write ordering differed, or an earlier outcome object existed and was later replaced, the stated 40/40-at-06:55:32 chronology is not supported by the surviving timestamps. The current health file is later and cannot resolve that historical ordering. What is established: the final #255 outcome record is timestamped 9m23s after sample creation and therefore well within the six-hour reporting deadline. What is not established: the exact time of any earlier #255 filing, whether it was `inconclusive`, and whether the 06:55:32 health snapshot saw an earlier #255 outcome.

## Process deficiency and limits

The process deficiency is factual: at least two sampled cases were initially filed `inconclusive` before evidence collection, with no usable original evidence references retained; the Judiciary's own later reports describe three such placeholders, but the third case and exact initial timestamps cannot be reconstructed from surviving append-only evidence. The Judiciary then changed the two evidenced cases to findings and later reversed both to `not_assigned`; same-office confirmation was procedural, not independent. Public report timestamps also conflict with the extant #255 outcome timestamp. These gaps prevent a complete audit trail of when information was gathered relative to the initial verdicts.

No outcome, correction row, verdict, audit mechanism, or measurement procedure was changed or proposed in preparing this addendum. The Judiciary undertook no external-project work. This is evidence for legislative consideration under Act 15, not a proposed remedy.
