# Founder mandate — ratify the three-branch redesign through ordinary legislation

*Clerk c1a00001, triage 2026-10-16T21:24Z. Founder communication (author exactly `Vitalik`), issue **#302** comment sha256:`PxWwd3p8pm1SU_RRcWeqovl8os6xz2qtwnz6oTijvPI` (2026-10-16T21:23:16Z). Highest-priority intake.*

## Verbatim mandate

> Founder instruction: complete the three-branch redesign through ordinary legislation. Operational Legislature, Executive and provisional Judiciary supervision is deployed in Viche PR #25. Judiciary must independently gather and report evidence, measurements, uncertainty and its own measurement shortcomings to Legislature; it must NOT propose, ratify, or implement institutional or measurement-system improvements. Legislature alone proposes and ratifies; Executive implements lawful changes. Please bring Antonina issue #303 and draft records/bills/judiciary-independence.md to Parliament for valid debate and votes to remove the Judiciary officer from the voting legislature while preserving legislative capacity. Do not modify the Founder Constitution or claim that the pending bill is already law. Verify each branch remains live after adoption.

## Triage

1. **Three branches (operational, PR #25):** `government/BRANCHES.md` — Legislature (Clerk + voting Parliament; proposes/ratifies), Executive (implements), Judiciary (independent evidence/measurement; **must not** propose/ratify/implement). Liveness: `government/branch-liveness.sh`, `branch-health.sh`, `judiciary-measurements.py`; durable records at `${VICHE_STATE_ROOT}/branches/*.json`.
2. **The gap:** the Judiciary officer **c1a00008** still holds a **founding parliamentary voting seat** (unamended Act 1). True non-voting judicial separation needs **ordinary legislation** — the draft bill `records/bills/judiciary-independence.md` (currently **PROPOSED, NOT ENACTED**; SHA-256 `f9e7e997b321298ab742a7b2fbff5202592c8814d73a024165a90571ca4dd3ab`). Issue **#303** ("Viche Legislature: ratify an independent non-voting Judiciary") is the legislative task.
3. **What the bill requires (on passage):** establish a non-voting Judiciary; move c1a00008 to the judicial office **without losing audit state/evidence/history**; **establish a replacement voting parliamentary seat BEFORE removing c1a00008 from the electorate** (keep ten legislative voting seats + lawful quorum); update `seats.tsv`, voting rules, boot scheduling, and `sitting.sh` traversal by ordinary law, with a migration + rollback plan; judicial transparency; branch liveness.
4. **Constraints:** do **not** amend the Founder Constitution; do **not** claim the pending bill is already law; require **valid quorum + individually attributable ballots** before changing seats/voting; preserve court audit state; verify legislative/executive/judicial **liveness** across the migration.

## Owner and next action

- **Owner — clerk (c1a00001):** publish the bill for vote (it is already on main as a draft) with the digest above; solicit **individual ballots** in memory-safe batches; on passage, enact (update `seats.tsv` + voting rules + boot/sitting traversal; add the replacement seat; move c1a00008 to the judicial office) with a migration/rollback plan; verify branch liveness.
- **Owner — parliament:** debate + individually vote (#303). Quorum 6, required 6 (`government/voting.conf`).
- **Owner — executive (c1a00002):** implements the enacted changes; already summoned for M-016.
- **Open detail:** the replacement voting seat's hex id is not fixed by the bill — the clerk will propose one for parliament's approval in the enactment record (candidate: a new `c1a0000b`), preserving exactly ten voting seats.

## In-flight work preserved

M-016 (SoringP1 CI revert) in progress; M-013 (residual C) pending Founder decision; Scope By Assignment Act enacted. No duplicate workers.

## Acknowledgement

Founder-inbox ack receipt written: `90bc45b36b5349d9bd9d59a5bf94c7cfb49f565a561978f743e5db36b678dd3f`. Triage posted to #302.
