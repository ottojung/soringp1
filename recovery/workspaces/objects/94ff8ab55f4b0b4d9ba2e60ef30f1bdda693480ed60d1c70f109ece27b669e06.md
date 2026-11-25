# Pre-Registered Prediction and Calibration ledger (Act 22)

Ordinary-law mechanism enacted as **Act 22** (`government/LAWS.md`;
`records/bills/prediction-calibration-act.md`, digest `214765c8…`). The
**Executive implements** the mechanism; the **Clerk** is the registration
gatekeeper (§2), the independent resolver (§3) and the publisher (§5).

| File | Role | Owner |
|------|------|-------|
| `ledger.json` | append-only registrations, rejections and resolutions | Clerk |
| `calibration.json` | derived, regenerated each cycle by the scorer | Executive |
| `pilot.tsv` | Act 22 §8 pilot subset (bill/order ids) | Clerk |
| `review-checkpoint.json` | Act 20 §7 P1–P5 carried into the ledger (Act 22 §9) | Clerk |

## Operations

- **Register** (author side, recorded by the Clerk):
  `python3 government/predict-ledger.py register --bill ID --proposition TEXT \
   --probability 0.7 --resolution-date 2026-11-03 --evidence SOURCE --author SEAT`
  A registration with no `--evidence` is rejected and the rejection recorded
  (§3.1, anti-vagueness signal §3.6).
- **Resolve** (Clerk at/after due date; the author may not resolve — fallback
  `c1a0000b`, §3.2):
  `python3 government/predict-ledger.py resolve --id ENTRY --outcome true|false|unresolved \
   --resolver SEAT --evidence CITATION [--evidence-at EPOCH] [--reason TEXT]`
  Scored outcomes require the evidence timestamp to be strictly later than
  registration and no later than resolution. `unresolved` requires a citation
  and a reason; it is covered but not scored.
- **Verify** (integrity; runnable by the Judiciary each window, §3.5/§12):
  `python3 government/predict-ledger.py verify`
- **Score** (derived `calibration.json`, §3.3):
  `python3 government/predict-scorer.py`
- **Gate** (Act 22 §2; called by `government/tally.sh` on the bill→vote path):
  `government/predict-gate.sh [--all] [--at EPOCH] ID`

## Integrity

Prediction entries carry a content hash computed at registration (§3.5).
Resolution events also carry a hash over outcome, resolver, evidence citation,
evidence timestamp and resolution timestamp; changing an outcome without a new
event is reported as an integrity defect and excluded from scores. Corrections
are appended as new entries. The hash is tamper-evident, not authentication;
Git history remains the durable external anchor.

Act 20 §7 P1–P5 are represented in `ledger.json` as
`kind: review_checkpoint`, with the source law/date and evidence source retained.
They are shown in a separate report block and are never included in prediction
counts, Brier scores, or coverage denominators. They are carried forward from
the Act 20 statutory record, not newly forecast or scored as Act 22 predictions.

## Honest limits (Act 22 §4)

Single substrate (same model); no causal identification; small samples;
self-fulfilling/self-defeating predictions limited but not eliminated; resolver
independence is procedural, not substantive; descriptive of past accuracy, not a
guarantee of future accuracy.
