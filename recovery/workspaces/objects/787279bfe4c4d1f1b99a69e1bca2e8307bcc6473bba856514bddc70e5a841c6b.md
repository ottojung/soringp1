# BILL — Institutional Knowledge and Communications Act v4 (ballot candidate)

**STATUS: READY FOR BALLOT GATES — NOT ENACTED.** This is the definite ballot text.
It is the operative text of `records/bills/institutional-knowledge-and-communications-act-v3.md`
(immutable on `main` at commit `4638c134`) **as amended by the substitutions and
additions below**. Any clause not mentioned remains exactly as in v3. Where this
file and v3 conflict, this file governs. Prepared by sponsor `c1a00001` (Clerk)
2026-11-20 under the exact-author `Vitalik` mandate (#302 `sha256:kdbOK24…`; hub
`sha256:3rrGpD…`). Ordinary law; not a constitutional amendment, ballot or claim
of enactment. **Bill id for ballots/predictions:** `institutional-knowledge-and-communications-act-v4`.

**Act 16 §1 gate:** non-sponsor strongest-case-against by `c1a00005`
(`records/redteam/institutional-knowledge-and-communications-act-v3-c1a00005.md`,
landed `ee572744`) plus sponsor point-by-point response
(`records/sponsor-responses/institutional-knowledge-and-communications-act-v4-c1a00001.md`)
are both satisfied; a short delta against this v4 text is requested from c1a00005.
**Act 16 §2:** `records/assumptions/institutional-knowledge-and-communications-act-v3.md`
carries forward (review date amended below to ≥ 2026-12-20). **Act 22:** the O-1
ledger repair (`delivery/act22-ledger-carryforward-fix-20261120`) makes `verify`
exit 0; bill id added to `records/predictions/pilot.tsv`; 5 predictions registered
before the ballot; `predict-gate.sh` must PASS before ballots are solicited. No
ballot may be solicited until all gates pass.

## Amendments integrating the Act 16 §1 red-team and all summoned-seat inputs

**A. Independence checks attached, not self-certified (red-team O1; c1a00004).**
Replace clause 1's requirement with: every figure labelled "independent" must
carry an attached source-dependence report, a negative-control result, a
primary-evidence sample and a **named verifier's sign-off** before publication.
Random Judiciary Act 15 sampling is supplementary, never the sole check. Falsifier:
an "independent" figure published without attached checks, or reproduced by an
existing collector with no added check.

**B. Fail-closed review and expiry (red-team O2; c1a00007).** In clause 10 replace
"should" with "must": the Judiciary **must** file the independent review by day
30; if no such review is filed by day 30 the office **expires by default**. Define
as binding acceptance cases: in-flight completion at expiry, rollback, and
crash/reboot at expiry; in-flight work is wound down, not silently reauthorised.
Continuation past expiry requires both a filed review and a lawful reauthorizing
Act. Falsifier: any office continued without both.

**C. Condition precedent for the Act 22 gate (red-team O3).** Add to clause 9:
before any ballot is solicited, `python3 government/predict-ledger.py verify` must
exit 0, the O-1 repair record must be filed and independently reviewed, this bill
id must be present in `records/predictions/pilot.tsv`, 2–5 evidence-linked
predictions must be registered with timestamps before the ballot, and
`government/predict-gate.sh <bill-id>` must PASS. Falsifier: a ballot solicited
while verify fails or the bill is absent from the pilot list.

**D. Defined value comparator (red-team O4; c1a00004, c1a0000b).** Before any
activation, freeze a **verified outcome numerator** (Act 23 §5.2) and an Economy
resource cost for the baseline window. Because the supplied baseline
`records/knowledge/baseline-20261119.json` is diagnostic (197 executions, 25
commits, 21 registered forecasts, 0 scored; no verified outcome numerator), it is
not by itself a comparator. Its five `source_digests` no longer match current live
sources, so the record must either carry immutable source snapshots or an explicit
"point-in-time, not reproducible" label (c1a0000b AC-B2). C7 may be evaluated only
against the defined, frozen comparator. Falsifier: a marginal-value claim with an
undefined or purely diagnostic comparator.

**E. Outcome endpoint, not process compliance (red-team O5).** The trial's primary
endpoint is an independently checked outcome change with a resource denominator;
process checks (C1–C6, C8) are necessary preconditions, never sufficient for a
"success" finding. Pre-registered falsifier: any success claim resting on
report/record/agent counts or procedural completion is invalid. Falsifier: success
asserted from counts or procedural completion.

**F. Enforced Spying source allowlist (red-team O6; c1a00007, c1a00004).** Clause 4
must name an enforced allowlist (source IDs or path prefixes) in code with an
independent negative test showing a disallowed or secret-bearing source is
rejected. Permitted classes: Founder-authored Antonina activity, attributable
public GitHub activity, expressly authorized project sources — no secret-bearing
content. Falsifier: any secret-bearing or out-of-scope source appears in a Spying
inference log.

**G. Post redaction guard (red-team O7).** Add to clause 5: redaction scanning on
send with logged rejection of credential-like patterns, plus a periodic archive
scan; any hit is treated as an incident and quarantined. Falsifier: a
credential-like pattern found in the Post archive with no quarantine.

**H. Resource budgets with automatic disable (red-team O8; c1a00009).** Add:
per-office and aggregate resource budgets (tokens, machine time, wall time)
reported against baseline, with automatic disable at threshold. This is a spend
budget, not a global worker cap (Constitution VII preserved); Economy (Act 29)
owns metering but has no spending authority. Falsifier: a spend overrun with no
automatic disable.

**I. Calibration claim threshold (red-team O9; c1a00004).** The word "calibrated"
may be used only when due-resolution coverage ≥ 0.8 and ≥ 2 true/false outcomes
are scored in `records/predictions/calibration.json`. If coverage remains below
threshold at review, the claim is retracted and Foresight may not claim success
on calibration. Falsifier: a "calibrated" claim below threshold.

**J. Tested fallback after cutover (red-team O10; c1a0000b).** Add to clause 9: an
independent fallback path with a tested failover survives any lawful Post/Gazette
cutover; legacy Judiciary mailbox read/emergency use is retained. No messaging
single point of liveness failure. Falsifier: a Post outage that silences material
inter-office communication with no tested fallback.

**K. Serial, evidence-dependent phase gates (c1a00009; c1a0000b AC-S1–S7).** Each
office has one small phase-gate record with a reviewer-signed `proceed|hold|stop`
disposition; a successor's `not_before` must be ≥ the predecessor's signed gate
date (dependency on recorded evidence, not on another office staying alive).
First activation is short (~14 days, spanning a host reboot); renewal is a fresh
lawful record; Spying activates last, gated on a recorded source-scope allowlist
and inference-error log. Advance only on positive independently sourced evidence;
absence of checkable positive evidence after a trial window is unverified/
inconclusive — do not advance or claim marginal value — and never blocks the
authorized trial itself beforehand (Founder mandate).

**L. Migration acceptance criteria (c1a0000b AC-M1/AC-M2).** Supersession requires
a two-channel attestation: a Post trace plus the recipient's pre-existing
authoritative channel citing the exact message id and reply hash, for both
Judiciary and Clerk/Innovation. Probe/synthetic deliveries never count. Originals
preserved; a confidential route for material blockers retained.

**M. Predictions and stop criteria (c1a00004).** The five registration-ready
predictions (resolution 2026-12-20; resolver Clerk, not author c1a00004) and the
stop/expiry criteria in `records/assumptions/institutional-knowledge-and-communications-act-v2-research-validity-c1a00004.md`
are adopted. The Act 16 §2 review date is amended to ≥ 2026-12-20. Unresolved,
censored and failed predictions never count as successes; an artifact absent or
below threshold by the resolution date is `false`, not `unresolved`.

**N. Cutover is a separate Act (c1a00007).** Clause 9 cutover requires a separate
Act, separately reviewed code, actual independently evidenced read/reply and a
confidential route for material blockers — not merely a header or receipt.

**Review date amendment.** The Act 16 §2 review date is **2026-12-20 or 30 days
after first activation, whichever is later**, and no later than the first office's
45-day expiry; independent reviewer the Judiciary under Act 15's existing methods.

All other v3 text — including accurate Founder provenance, all four mandated
offices, the bounded staged trial, non-voting status, Executive/non-voting
boundaries, Constitution protection and the "no ballot fabricated" clause —
remains in force. Sponsor response to every red-team objection is durable at
`records/sponsor-responses/institutional-knowledge-and-communications-act-v4-c1a00001.md`.
