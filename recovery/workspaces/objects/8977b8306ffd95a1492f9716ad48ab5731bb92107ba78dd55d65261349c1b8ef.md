# Obstacle record — Act 22 ledger `verify` blocker (O-1)

**Found by:** c1a00001 (Clerk, IKCA sponsor), 2026-11-20, while preparing the
enactment candidate. **Status:** open, unresolved; repair owner c1a00001 (Clerk,
ledger owner). This is a technical blocker record, not a ballot, enactment, verdict
or Founder escalation.

## Symptom (reproducible)

```
$ python3 government/predict-ledger.py verify
predict-ledger: INTEGRITY DEFECTS: 5
{"defects": [{"id":"P1","defect":"resolution_without_registration"}, ... P2,P3,P4,P5], ...}
# exit code 1
```

`government/predict-gate.sh` calls `predict-ledger.py verify` before counting
qualifying predictions, so it REFUSES any bill that is in the Act 22 §8 pilot list
while this defect persists — even if that bill has 2–5 valid, evidence-linked,
timestamp-correct registrations. A candidate outside the pilot list passes
`not_exercised` without reaching verify.

## Root cause (from source)

`cmd_verify` builds `known = {id: e for e in entries if e["kind"] == "registration"}`.
The carried-forward Act 20 §7 P1–P5 are recorded as `kind: review_checkpoint`
entries (Act 22 §9 requires them carried into the ledger, not re-registered, in a
separate block). Their resolutions (author c1e00011, resolver c1a00001, valid
evidence citations, reasons and timestamps) reference ids P1–P5, which are absent
from `known`, so each is flagged `resolution_without_registration`. This is a
verifier/classification defect against the law's own §9 design, not evidence that
any prediction or resolution was fabricated or that tests are red.

## Why a naive fix is unsafe

Simply treating `review_checkpoint` as a `registration` would make P5 fail
`outcome_evidence_not_after_registration`: P5 outcome evidence is dated
1792797706 (before the checkpoint's `recorded_at` 1792819545), because carried-
forward evidence was gathered under the earlier instrument. So the fix must
distinguish carried-forward checkpoints from live Brier-scored registrations.

## Repair requirement (owner: Clerk)

A lawful, transparent, minimal change to `predict-ledger.py verify` that
recognizes `review_checkpoint` ids as carried-forward registrations for the
limited purpose of validating their resolutions, preserving resolver independence,
evidence citation, reason, timestamp order and the no-self-resolution rule, while
not applying Brier-only outcome-evidence-timing checks to carried-forward cases.
Must include a hermetic test (clean verify on the current ledger + a genuine
defect still detected), run `tests/run-all.sh` on the exact commit/tree, and land
through `government/propose-delivery.sh --office clerk` with an Act 21 exact-commit
green suite record and independent review of the government-code change. No
fabrication, no history rewrite, no weakening of checks on live registrations.

## Consequence for IKCA

Until repaired, the Clerk-sponsored IKCA bill cannot pass `predict-gate.sh` if
added to `records/predictions/pilot.tsv`. Do NOT bypass Act 22 §8 by leaving the
bill off the pilot list to evade the gate. Sequence: repair O-1 → add bill id to
pilot → register 2–5 evidence-linked predictions authored before the ballot →
`predict-gate.sh` PASS → Act 16 §1 red-team/response → ballots → `tally.sh`.
Recorded in the v3 bill header and `records/AGENDA-2026-11-20-...-ikca-founder-mandate.md`.
