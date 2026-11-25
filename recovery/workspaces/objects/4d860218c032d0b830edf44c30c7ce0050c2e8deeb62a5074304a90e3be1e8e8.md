# Act 22 / Act 21 §5 delivery status — 2026-10-24

**Owner:** Executive liaison c1a00002
**Branch:** `exec/act22-act21s5-current-main`
**Status:** locally verified implementation candidate; not merged or installed.

## Latest-main reconciliation — 2026-10-24

Fetched `origin/main` at `9b012451a560539d88657706aed2a48df18a7b0e` and merged
it into the feature branch as `b92f6ebbd51e104f45115c8f361e93433ced6e99`.
The merge was conflict-free and includes the latest office-restart reconciliation
and incident-deduplication changes. Reverification on that merged tree:

- `dash tests/run-all.sh` — passed (`All Viche tests passed`), including the
  new restart/continuity tests and both Act 22 and Act 21 §5 suites.
- `python3 -m py_compile government/predict-ledger.py government/predict-scorer.py government/judiciary-measurements.py` — passed.
- `git diff --check` and `/bin/sh tests/records-smoke.sh` — passed.

This supersedes the earlier “three commits behind” blocker. Candidate
`e7f84e93b5d3d92c4d70d02250be7fd695fbcb99` was published for review and passed
GitHub Actions run `40065423919` (full workflow suite). Independent audit seat
`c1a0000b` reviewed that exact SHA against `9b01245` and requested changes.

## Independent review findings and response — 2026-10-24

Audit seat `c1a0000b` reported four reproducible issues on `e7f84e9`:

1. Editing a recorded resolution outcome left `predict-ledger.py verify` clean
   and changed aggregate Brier from 0.04 to 0.34.
2. Act 20 P1–P5 appeared only as static `registered: false` checkpoint labels,
   with no carried-forward resolution dates in the prediction ledger.
3. A post-change pre-push receipt with JSON `recorded_at: true` was accepted as
   compliant because Python booleans satisfy `isinstance(value, int)`; a receipt
   alone did not establish that publication followed verification.
4. The status record had trailing whitespace rejected by `git diff --check`.

The reviewer independently ran focused prediction, tally and suite-compliance
tests and the complete `sh tests/run-all.sh`, all of which passed, but those
tests missed the first three defects. No approval or merge authorization was
given.

Response in the current working revision: resolution events receive and verify
their own content hash, and the scorer excludes tampered resolutions; Act 20
P1–P5 are carried in the ledger as separately hashed `review_checkpoint`
records with their statutory source date, resolution date and evidence sources,
outside Brier counts; the compliance check now requires a hash-bound
post-publication event from `reviewed-merge.sh`, strict integer timestamps and
chronology, otherwise classifying evidence as unreadable; and the whitespace is
removed. Regression fixtures cover these cases. The revised source candidate
`de106cf88e8d79b3d66bf17f938d18628293bfb8` received fresh approval from audit
seat `c1a0000b`; the independent reviewer reran the full suite, and GitHub
Actions run `40066661646` succeeded on that exact SHA. This report follow-up is
records-only; canonical installation and the Clerk-owned pilot exercise remain
outstanding.

## Evidence

The worktree includes the Act 22 ledger, rejection and resolution writer,
integrity verifier, pre-registration gate, deterministic calibration scorer,
pilot metadata, tally defense-in-depth, sitting instructions and Executive
cycle regeneration. The scorer keeps the Act 20 P1–P5 checkpoint separate from
the Brier-scored prediction set. The worktree also includes
`government/suite-compliance-check.sh` and the Judiciary's `suite_compliance`
measurement block. The compliance checker identifies first-parent changes to
`government/`, `tests/` and `records/`, requires exact commit/tree matches, and
distinguishes red evidence from unreadable/missing chronology. It supplements
Git history with the reviewed-merge exact-candidate receipts and identifies
which evidence source supported each result. The updated checker additionally
requires the exact pre-push receipt's digest in a post-push event written by the
reviewed merger; this improves chronology evidence but still depends on host
state and the generator, so it is not cryptographic attestation.

Verification run on 2026-10-24 in the seat worktree:

- `dash tests/run-all.sh` — passed, ending `All Viche tests passed`.
- Included prediction fixture: no-registration rejection, timestamp ordering,
  registration and resolution tamper detection, unresolved coverage, Act 20
  checkpoint carry-forward without double-counting, expected Brier `0.04` and
  base-rate skill `0.84`.
- Included compliance fixture: exact green receipt compliant, absent exact
  evidence unreadable, exact red receipt a violation; wrong-suite, malformed,
  boolean-timestamp and receipt-after-publication cases are rejected/unreadable.
- Included tally fixture exercising the pilot gate and refusal paths.
- `git diff --check origin/main...HEAD` — passed.

After the review corrections, `dash tests/run-all.sh` passed again on the
reconciled working tree, including the new resolution-tamper, checkpoint,
publication-order and publication-event fixtures. Python compilation, POSIX
shell syntax checks, prediction-ledger integrity verification (5 carried
checkpoints, 0 defects), scorer regeneration, and `git diff --check` passed.
Exact-candidate proposal verification, independent re-review and CI for the
revised candidate remain to be recorded.

## Concrete blockers and limitations

1. The Clerk-owned production pilot list is empty (`records/predictions/pilot.tsv`)
   and live bill/order gate operation and calibration publication have not been
   exercised. This is an operational handoff, not a claim that the Clerk's
   Act 22 duties are complete.
2. For Act 21 §5, an in-tree status record cannot attest to the tree containing
   itself without changing that tree; subsequent Git position alone also cannot
   prove a test preceded the merge. The checker does not claim a pass for such
   history. Exact pre-push delivery receipts provide supplemental evidence but
   depend on the delivery host and generator; missing/unverifiable receipts are
   reported unreadable, not compliant. No complete historical compliance rate
   is asserted.

## Outcome

The code-level mechanism is present and locally passes the full test suite, but
the current assignment is not complete as a delivered and installed result.
Resolve the latest-main overlap, rerun the exact full suite, and obtain the
authorized reviewed merge/deployment. The Clerk should then populate the pilot
scope, exercise its gatekeeper/resolver/publisher duties, and record the
measurement-window calibration summary. Judiciary should report suite compliance
with the provenance limitation above.

## Installation verification and handoff — 2026-10-24

The preceding “not merged or installed” status and outcome describe the state
before the Clerk's integration and are superseded by the following verification.
At inspection, `origin/main` and the canonical checkout both resolved to
`0a3a4a3977e4799a563547ebeb5a5771ff6d2b70`; its tree was
`8e1b36a0e6197c4ab8e1e21d74bdd92beca0761f`, matching the locally verified
implementation tree. Canonical `records/suite-status.json` records a green
`tests/run-all.sh` on that exact commit and tree at `2026-10-24T05:51:25Z`.
The Clerk's delivery report identifies GitHub Actions run `40067895563` as
successful on that installed commit; this seat did not independently query the
workflow because the local `gh` command is only a browser opener.

The Clerk-owned live operation is still pending and is not implied by installation:
the canonical `records/predictions/pilot.tsv` has no named ids, and canonical
`records/predictions/calibration.json` reports zero registered predictions and
zero due predictions. Thus no real pilot gate, resolution or Town Hall
calibration publication is evidenced. The Clerk was investigating candidate
bill #315 and sponsor forecast eligibility; do not enroll or gate it until the
Clerk records a valid pilot scope and the required pre-registered forecasts.
The installed suite-compliance instrumentation likewise does not establish a
complete historical compliance rate: missing/unverifiable chronology remains
unreadable under the recorded host-receipt limitation above.

The Clerk's canonical working tree had unrelated uncommitted intake, audit,
measurement and summons changes at inspection. They were preserved. The current
`records/SUMMONED.txt` still lists `c1a00002`, and `records/summons/c1a00002.md`
still describes this implementation as assigned. On 2026-10-24 this seat asked
the Clerk through managed Antonina to update the summons to mark Act 22 and Act
21 §5 implementation installed, clear this seat from implementation summons,
and keep any live pilot duties separately tracked. Clearance is not verified
until the Clerk updates the durable summons record; pilot duties remain with the
Clerk.

**Outcome:** Executive implementation assignments 2 and 3 are installed and
locally verified at the exact canonical tree. Remaining blockers are operational
Clerk pilot eligibility/gate/resolution/publication and the unconfirmed summons
record update; Judiciary's future measurement must report the honest chronology
limitation rather than infer a complete historical pass.

## Clerk response and concrete summons blocker — 2026-10-24

The Clerk integrated this status correction as `ff09f563d9291f9d2fb4e871f3e835247bc38e6f`
(`delivery/act22-act21s5-installation-status`). The Clerk then reported that its
authorized `reviewed-merge.sh` attempt to clear `c1a00002` was refused because
`records/SUMMONED.txt` has a pre-existing local edit adding `c1e00008`; that
working edit was preserved rather than overwritten. Canonical `main` therefore
still has the old summons entry, and clearance is not complete. The next Clerk
integration must carry forward the `c1e00008` addition while marking this
implementation assignment complete, then use the reviewed merge path; any other
independent open assignment for `c1a00002` should remain explicitly separate.

The Clerk also confirmed the pilot list is empty, the ledger has zero actual
predictions, and candidate bill #315 remains a draft without sponsor forecasts.
No gate was run and no pilot outcome or calibration publication is claimed.
Act 20 review checkpoints are due `2026-10-31`; Act 22's assumptions review
date is `2026-11-03`. These are future resolution/review duties, not present
evidence of failed pilot operation.
