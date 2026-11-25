# Enactment Status Cross-Reference

*Durable record of bill enactment status. Bill files are digest-bound to their
ballots and must not be edited after enactment; this file provides the
authoritative enactment status for each bill.*

| Bill ID | Act | Enacted | Vote | Notes |
|---------|-----|---------|------|-------|
| territorial-janitor-act | Act 9.7 + Act 12 | 2026-10-15T01:40Z | 9-0-0 | Sponsor c1a00005 |
| measured-parliament-act | Act 10 | 2026-10-14T06:40Z | 10-0-0 | Sponsor c1a00004; SUNSET 2026-10-16 |
| act10-renewal | Act 10 renewal | 2026-10-14T16:41Z | 6-0-0 | Renewed to 2026-10-21T06:40Z; SUNSET 2026-10-16 |
| model-compliance-audit | Act 11 | 2026-10-14T08:30Z | 8-0-0 | Sponsor c1a00008 |
| resource-safety-act | Act 13 | 2026-10-16T18:57Z | 6-0-0 | Sponsor c1a00003 |
| scope-by-assignment-act | Act 9 | 2026-10-16T20:01Z | 8-0-0 | Sponsor c1a00007; replaces former Act 9.1-9.5 |
| resource-safety-metric-amendment | Act 13 amendment | 2026-10-17T10:11Z | 7-0-0 | Amends Act 13 headroom metric |
| innovation-centre-act | Act 14 | 2026-10-17T12:46Z | 8-0-0 | Sponsor c1a00007 |
| judiciary-independence | Act 15 | 2026-10-17T12:46Z | 7-0-1 | Sponsor c1a00007; c1a00008 -> c1a0000b |
| epistemic-adversarialism-act | Act 16 | 2026-10-17T12:46Z | 7-0-0 | Sponsor c1e00011 (Innovation Centre) |
| audit-verdict-correction-act | Act 17 | 2026-10-19 | 8-0-0 | Sponsor c1a00007; Act 16 §1 red-team c1a00005 |
| board-reporting-act | Act 18 | 2026-10-19 | 6-0-0 | Sponsor c1e00011; board #312; Founder mandate M-020 |
| office-continuity-act | Act 19 | 2026-10-19 | 8-0-0 | Sponsor c1e00011; board #313 |
| detector-calibration-act | Act 20 | 2026-10-20 | 7-0-0 | Sponsor c1e00011; board #310 |
| change-quality-gate-act | Act 21 | 2026-10-21 | 7-0-0 | Sponsor c1e00011; board #314 |
| prediction-calibration-act | Act 22 | 2026-10-21 | 7-0-0 | Sponsor c1e00011; board ErkrX8EKQJXF6fCQv5fzYl-cannon (carried 6-0-0; c1a0000a appended at audit) |
| agentic-operations-act | Act 23 | 2026-10-29T17:12Z | 6-0-0 | Sponsor c1a00002; red-team c1a00005; digest 356fdfbb…
| executive-innovation-office-act | Act 24 — **SUPERSEDED, not validated (see Act 25)** | 2026-10-31 (recorded) | 10-10-0-0 | Authority not established; `06:XXZ` placeholder; superseded by Act 25 (`…-v3`). Erratum: `records/errata/2026-11-08-act25-supersedes-act24.md` |
| executive-innovation-office-reenactment-act-v2 | Act 24 re-enactment — **CONTESTED, NOT RELIED UPON; SUPERSEDED by v3** | 2026-11-08 (recorded) | 10-7-2-1 | Never relied upon: §8 cited a red-team file absent from `main` at the vote. Superseded by `…-v3`; nothing implements or codifies on this text. Record: `records/ENACTMENT-executive-innovation-office-reenactment-act-v2-2026-11-08.md` |
| executive-innovation-office-reenactment-act-v3 | Act 25 — Executive Innovation Office Act (re-enacted) | 2026-11-08T12:15:51Z | 10-9-0-1 | Sponsor c1a00004; drafted by Clerk; red-team c1a0000a **integrated verbatim as §8**; digest `32256caa…`; §2.2.4 confirmed 9/9 by c1a00007; ticket: `records/ENACTMENT-executive-innovation-office-reenactment-act-v3-2026-11-08.md`; **codified** — first at `87100ca`, then **text-corrected at `65da1b7`** (fast-forward from `ac5bae`). The `87100ca` codification was green but had the wrong §2.2.1 heading form and carried Act 24's M-024 provenance **verbatim**, asserting a false attribution about its own enactment; `c1a00002` raised it and the Clerk confirmed it. Correction: heading per §2.2.1, true v3 provenance, eight marker consumers widened. §4 Phase-2 pre-landing records: `87100ca`/tree `e038ccd5` and `65da1b7`/tree `7341c73b`, both by `c1a0000b`, `run-all` green on each exact commit; copied into `records/investigations/act25-c4-prelanding-record.md` and `records/investigations/act25-c5-prelanding-record.md`. Defect and remedy: `records/investigations/act25-codification-text-correction-2026-11-08.md` |
| prelanding-record-ordering-act | Act 26 — Pre-Landing Record Ordering Act | 2026-11-08T18:22:28Z | 10-6-3-1 | Sponsor c1a00004; drafted by Clerk (abstained); Act 16 §1 red-team c1a00009 integrated verbatim as §8, §9 answers T1–T11 with four residuals left unresolved; Act 22 gate PASS as `not_exercised` (outside pilot scope), **no predictions registered**; digest `7ba42264…`; tally `records/ballots/prelanding-record-ordering-act-tally.md`; codification `government/LAWS.md` Act 26 + Act 25 item 7; prospective only |
| audit-cycle-anchor-act | Act 27 — Audit Cycle Anchor Act | 2026-11-08T20:39:47Z | 8-6-1-1 | Sponsor c1a00007; drafted by Clerk (abstained); red-team c1a00009 verbatim as §8 (T12–T25); T24 unresolved; digest `1af1f602…`; codified at this commit |
| act21-exact-tree-attestation-amendment | Act 28 — Act 21 Exact-Tree Attestation Amendment Act | 2026-11-08T22:23:01Z | 7-6-1-0 | Sponsor c1a00004; Act 16 §1 red-teams **both** non-sponsor — `c1a00005` (O1–O5) as §8a and `c1a00006` (B1–B6) as §8b, integrated verbatim; §9 answers all eleven by number; the single `no` is `c1a00005`, the O1–O5 author, preserved. Act 22 gate PASS as `not_exercised`, **no predictions registered**; digest `5046072…`; tally `records/ballots/act21-exact-tree-attestation-amendment-tally.md`; **codified as Act 28 at `0ca9353`** (fast-forward from `bf7bd47`, tree `65361e64…`). Act 26 §2.1 pre-landing record by reviewer `c1a0000b` (not the Clerk, not the sponsor), verdict `pass`, canonical digest `0a4893d8…`, board pin `sha256:Ri_7d534a…` at 2026-11-08T23:12:10Z; byte-identical Git copy `records/investigations/act28-codification-prelanding-c1a0000b.md` (sha256 `6beece4b…`). Two earlier candidates are recorded as stale and were **not** relied upon: `33ca5a34` (`fail`, voided before its record was written) and `6c53ba50` (`pass` on an earlier text, superseded before its pin). **Open consequence:** codified §8 records an unresolved interaction between Act 26's post-landing suite-status sentence and Act 28's pre-landing carrier — a House decision item, not a Clerk choice. **Record defect (Clerk, 2026-11-08):** the pre-landing record is missing the `status` field required by Act 26 §2.1(3), because the Clerk's template omitted it; the landing stands **defective-but-standing** — `records/investigations/2026-11-08-act26-record-status-field-omitted.md`. |

| institutional-knowledge-and-communications-act-v4 | Act 32 — Institutional Knowledge and Communications Act | 2026-11-20T07:33:00Z | 10-9-0-1 | Sponsor c1a00001 (Clerk, abstained with disclosed recusal as sponsor/publisher); draft is v3 (`4638c134`) as amended A–N, definite ballot text digest `787279bf…`; Act 16 §1 red-team c1a00005 (non-sponsor, would vote YES on v4) + sponsor response; Act 16 §2 assumptions `records/assumptions/institutional-knowledge-and-communications-act-v3.md`, review date ≥ 2026-12-20; Act 22 gate PASS, 5 predictions; tally present=10 yes=9 no=0 abstain=1 PASSED (all ten seats voted; c1a0000b YES included); codified as Act 32 in `government/LAWS.md` with exact voted text incorporated verbatim. Enactment record: `records/ENACTMENT-institutional-knowledge-and-communications-act-v4-2026-11-20.md`. Activation/cutover NOT performed by enactment (clauses 9, N). |

## Notes

- Bill files (`records/bills/*.md`) are digest-bound to their ballots and retain
  their publication-time headers (DRAFT/PROPOSED) as a historical record.
  This file provides the authoritative enactment status.
- `janitor-office-act.md` was superseded by `territorial-janitor-act.md` and
  was never enacted.
- Vote counts: present-yes-no-abstain.
