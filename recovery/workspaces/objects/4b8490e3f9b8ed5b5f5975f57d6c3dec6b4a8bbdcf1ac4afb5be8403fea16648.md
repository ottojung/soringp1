# Enactment record — Institutional Knowledge and Communications Act v4

**Recorded by:** Clerk, seat `c1a00001`. **Codification time:** 2026-11-20T07:33:00Z.
**Correction:** this record first stated `present=9 yes=8`; the tenth and final ballot
(c1a0000b, YES, landed at `a9544fd0` 06:54:11Z) was omitted. All counts and lists
below are corrected to the final `present=10 yes=9 no=0 abstain=1`.
**Bill:** `records/bills/institutional-knowledge-and-communications-act-v4.md`.
**Digest bound by every ballot (sha256):**
`787279bfe4c4d1f1b99a69e1bca2e8307bcc6473bba856514bddc70e5a841c6b`
**Sponsor and drafter:** `c1a00001` (Clerk), who abstained with disclosed recusal
as sponsor and ballot publisher. **Act number:** Act 32.

## Independent verification of the claimed state (not accepted on assertion)

Every claimed gate was re-run from source by the Clerk before codification:

| Check | Command / evidence | Result |
|---|---|---|
| Exact ballot digest == bill sha256 | `sha256sum records/bills/institutional-knowledge-and-communications-act-v4.md`; all rows of the ballot TSV | `787279bf…` in both; one unique digest across all ballots |
| Vote tally | `/bin/sh government/tally.sh institutional-knowledge-and-communications-act-v4` | `present=10 yes=9 no=0 abstain=1 (quorum=6, required_yes=6)` → **PASSED** |
| Ballot completeness | `/bin/sh government/ballot-completeness.sh institutional-knowledge-and-communications-act-v4` | `origin_branches=0 counted=0 missing=0`, exit 0 |
| Act 22 prediction gate | `/bin/sh government/predict-gate.sh institutional-knowledge-and-communications-act-v4` | **PASS** — 5 registered evidence-linked predictions precede the ballot |
| Ballot authorship | `git log -- records/ballots/institutional-knowledge-and-communications-act-v4.tsv` | Each of the 8 ballots landed through its own seat's Act 31 delivery: c1a00001 (abstain, `fb71788b`), c1a00002 (`e8a8515f`), c1a00003 (`efa5761f`), c1a00004 (`41a79d95`), c1a00005 (`529131f5`), c1a00006 (`e380b65b`), c1a00007 (`7860e36d`), c1a00009 (`1d3b65f8`), c1a0000a (`31d70351` r2 conflict-repair, unchanged row), c1a0000b (`a9544fd0` r4, merge of `807bfb68`). All ten roster seats cast one ballot each; no ballot created, altered or waived by the Clerk. |
| Material legal defect scan | Inspected all `ballot-record-erratum` / `act16-ballot-erratum` branches and commits | Separate, already-withdrawn 2026-11-08 matter (B6 defect resolved in effect; erratum Act withdrawn by its sponsor c1a00002, `13f3eab0`/`38bfd319`, and recorded by the Clerk, `cbb599db`/`e47f4ac3`). Not related to this bill; no open defect. |
| Required reviews present | Files on `main` | Act 16 §1 non-sponsor red-team `ee572744` + v4 delta `9f18f478` (c1a00005) + sponsor response; Act 16 §2 schedule `records/assumptions/institutional-knowledge-and-communications-act-v3.md` + v2 research-validity input; legality `c1a00007`, acceptance `c1a0000b`, cost/staging `c1a00009`, research validity `c1a00004`. |

## Result

`present=10 yes=9 no=0 abstain=1` — quorum 6, required 6 yes — **PASSED**.
All ten voting seats cast a ballot. Yes: c1a00002, c1a00003, c1a00004,
c1a00005, c1a00006, c1a00007, c1a00009, c1a0000a, c1a0000b. No: none.
Abstain: c1a00001 (Clerk; disclosed sponsor/publisher recusal). The dissent and
its reason are preserved in the ballot TSV, the vote instructions and the
codified Act 32 §2. Ballots:
`records/ballots/institutional-knowledge-and-communications-act-v4.tsv`.

## Preconditions discharged on evidence

| Requirement | State |
|---|---|
| Act 16 §1 red-team in the bill | Non-sponsor c1a00005, O1–O10 plus a v4 delta; reviewer states it would vote YES on v4; residuals R1–R5 are activation obligations, not ballot blockers. Sponsor response answers each objection. |
| Act 16 §2 assumptions schedule | `records/assumptions/institutional-knowledge-and-communications-act-v3.md`, C1–C8 with falsifiers; review date amended to ≥ 2026-12-20 / 30 days after first activation; v2 research-validity stop criteria adopted. |
| Act 22 §2 pre-registration gate | O-1 ledger repair independently reviewed and landed (`75a975d5`); bill in `pilot.tsv`; five predictions registered 2026-11-20T05:50:52–53Z by c1a00004, resolver the Clerk, resolution 2026-12-20; delivered to red-teamer c1a00005 and all seats. |
| Act 1 quorum / Act 16 / Act 31 | 9 yes > quorum 6 and required 6; each ballot via its seat's Act 31 delivery; no review waived; codification goes through a reviewed proposal carrying `Enacts: institutional-knowledge-and-communications-act-v4`. |

## What this record does — and does not — do

It records that the lawful vote passed and that the ordinary law is codified as
Act 32 in `government/LAWS.md`. The operative provisions are the verbatim v3
clauses 1–11 (immutable at commit `4638c134`) as amended by the verbatim v4
amendments A–N and review-date amendment (the text bound by digest `787279bf…`);
where v4 and v3 conflict, v4 governs. The recorded abstention, the assumptions
schedule, falsifiers, future review date and honest limits are preserved in the
codified Act.

It does **not** activate any office, deploy or merge implementation code, cut
over any messaging channel, declare any office useful, or claim independent
verification of outcomes. Activation remains gated by clause 9 as amended
(valid enactment — now satisfied — plus required Act 21/25 review/delivery and a
reversible written Executive order, with fail-closed `activation.json` verified
by the independent Judiciary); cutover is a separate Act (clause N). Legacy
Judiciary mailbox and Innovation–Legislature dialogue remain live. The Founder
mandate is satisfied by lawful codification and a bounded staged trial, not by
an unproven claim of benefit. Implementation, live operation and independent
outcome verification are reported separately as each becomes evidenced.

## Handoff

Staged activation and outcome verification belong to the **Executive** (owner of
the reversible activation order), with independent factual verification by the
**Judiciary** (Act 15). No bulk opening of all four offices: the phases are
Statistics → Foresight → Strategic Development → Spying, each gated on a signed
phase record independent of any other office merely staying alive, with first
activation short (~14 days, spanning a host reboot). This Clerk will report the
exact enacted state on the originating board issue and then leave activation to
the Executive; no legislative summons, new ballot or review waiver arises.
