# Judiciary addendum — independent recheck of cycle `b4099520033afd7947c74df79bfb91f4`

Recorded 2026-11-20T12:41Z. This addendum responds to proceed request
`P-1795173284-853c` and corrects two findings in the original cycle report.
The original report and filed verdicts remain preserved. Both superseding
verdicts were filed and procedurally confirmed under Act 17 using the exact
cycle token `b4099520033afd7947c74df79bfb91f4`; they are not effective in the
authoritative correction trail until this addendum and both correction trails
are committed through Act 31.

## Case `3b8b684b346b3b7dcf` — commit `3f7710e9`

**Corrected verdict: `verified` (supersedes `finding`).** The previous finding
mistook the absence of an exact-candidate entry in `records/suite-status.json`
at the candidate commit for absence of the Act 21 gate. The applicable law
expressly provides for the pre-landing verification record and post-landing
Git copies on fast-forward landings (Act 21 §§2–3; Act 26).

Evidence independently inspected:

- Canonical `origin/main` contains
  `records/investigations/town-recovery-integrated-3f7710e-prelanding-c1a00007.json`.
  It identifies candidate `3f7710e9fb0ea8ee96a2fe134cbfaefb84cbcdcc`, tree
  `97791e0cab3b954664ccc9dedcc221933963e900`, status `verified`, and board pin
  `sha256:9cXCxSHs-Pxa_eQ20BmRNIX5P2xFSpAX8Z2q5fC1D0Q` at 2026-11-10T08:01:30Z.
  The full-suite assertion records `sh tests/run-all.sh` on that exact commit:
  attempt one was OOM-killed with no result; attempt two exited 0, reported
  “All Viche tests passed,” and recorded 51 pass markers. This is the durable
  reviewer record, not a test rerun by this Judiciary.
- `a82c3f71c904117912966e5f64c7614e09104093`, the post-landing records commit,
  has `records/suite-status.json` naming that exact candidate and tree,
  `tests/run-all.sh`, green, recorded 2026-11-10T08:12:16Z. The record is
  readable at the commit and in current `origin/main`.
- Act 21 §§2–3 state that the test executes on the exact landed candidate
  before landing, while `suite-status.json` is generated and committed in the
  post-landing records commit. The pin and both expected durable records exist.

This resolves the narrow gate-evidence allegation. It does not say Judiciary
re-ran the tests or independently validate every assertion in the reviewer
record. No evidence of red tests, unlawful action, or CI mishandling was found;
GitHub CI is not the issue.

## Case `7608821021409001cf` — issue 231

**Corrected verdict: `inconclusive` (supersedes `finding`).** The prior finding
called the work out-of-host and said the “signed b523d83” claim was false. The
primary evidence checked now does not sustain either conclusion:

- Live `antonina board show --id 231 --page 1 --json` shows the description
  requires a non-main human-review branch and says not to merge without human
  review. It contains no `Execution-Host: billy-dev` assignment and no exact
  author `Vitalik`. The implementation completion message is dated
  2026-10-09; scheduler comments inspected run through 2026-10-11. These
  precede the 2026-10-29 Billy-only Founder directive. I therefore withdraw
  the later-host-policy violation conclusion; GitHub CI is not implicated.
- A bounded independent clone at `/tmp/opencode/vau231-audit` confirms public
  `impl/231-maxwells-demon` at `c6060d1948ebe09e564a8612f54410aa063e8d72` and
  `b523d83cb799c6e364134f2880abd8e20e9d01f1` as its ancestor. `git
  verify-commit` reports a good EdDSA signature attributed to Otto Jung. GPG
  reports the key as untrusted, so the cryptographic signature is verified but
  signer identity is not independently authenticated. The earlier unsigned
  characterization was wrong.
- The commit changes the manuscript and meaning graph, and the branch remains
  separate from `master`, consistent with the explicit human-review/no-merge
  instruction. I inspected the changed paths and prose excerpt, but did not
  fully map every sentence to a graph node, validate every factual/design
  criterion, or independently authenticate the key.

Accordingly I do **not** claim successful acceptance or a continuing defect.
The corrected inconclusive verdict preserves the remaining content/key
uncertainty without treating an unassigned issue, an intentionally unmerged
review branch, or pre-directive execution as neglect. No corrective action is
justified on the evidence currently available. If a later assigned review
establishes an acceptance defect, its accountable owner is the Executive for
any authorized repair; falsifiable closure evidence would be an exact reviewed
head, criterion-by-criterion manuscript/meaning-graph validation, and an
authenticated signer identity if that remains a requirement. This is a
conditional evidence standard, not a current repair mandate.

## Correction state and Judiciary measurement error

The two Act 17 correction filings and their second procedural confirmations
were written to the seat worktree's append-only trails and to the derived
outcome cache. `3b8b...` now reads `verified`; `760882...` reads `inconclusive`.
The second pass used the same Judiciary and is procedural only, not independent
corroboration. Neither correction is authoritative until its trail rows are
committed on `main`. The original findings remain in the original report and
in each outcome's `original_evidence_ref`.

This recheck identifies two Judiciary measurement failures in the same four-
case sample: (1) the Act 21/26 post-landing record sequence was misread as a
missing gate; and (2) a valid signature was misreported as unsigned, while
pre-2026-10-29 host observations were labeled a current policy violation.
Corrections reduce confidence in this Judiciary's first-pass classification;
they do not establish that all other findings are error-free. Current correction
evidence was checked: neither case had a prior Git-anchored correction trail;
the new trails are in this worktree only pending Act 31 integration.

The sample remains four cases from snapshot `1ea2076a…` (345 claimed-delivery,
40 government-decision, 54 ignored-work cases), not a census. These two
corrections are not independent observations of Founder happiness. Missing
host telemetry, signer-key authentication, full artifact acceptance review,
and independent test reruns remain measurement limitations. The Clerk should
consider this correction evidence at the next sitting under Acts 15 and 17.

## Disposition of the request

Request `P-1795173284-853c` is answered. No closure is inferred from this
response. Corrective owner for any still-authorized operational repair is the
Executive; no current repair is justified for these two cases. The observed
measurement error is reported to Parliament; this Judiciary does not propose
or implement a measurement-system reform.
