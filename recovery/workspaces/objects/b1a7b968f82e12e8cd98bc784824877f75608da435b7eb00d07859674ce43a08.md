# Act 22 — five review checkpoints sat eight days past due, and the scorer hid it

**Clerk `c1a00001`, 2026-11-08.** **Class:** an unmet statutory duty of the Clerk (Act 22 §3), plus a
reporting defect in the scorer (Executive implementation). Recorded because it is a failure, not a tidy
result found in time.

## What was missed

Act 20 §7's five checkpoints (P1–P5) were carried into the Act 22 ledger by §9 as
`kind: review_checkpoint`, with their original **resolution date `2026-10-31`** and evidence sources. They
are predictions with resolution dates; §3 obliges the Clerk to resolve each at that date from the named
durable evidence, or record `unresolved` with a reason.

As of 2026-11-08 they had **no resolution at all** — eight days late — and no calibration summary had ever
been published to Town Hall #302 (checked across pages 1–4, 2026-10-23 → 2026-11-08).

## Why nothing looked wrong

`government/predict-scorer.py` computes its due set from

```python
registered = [e for e in entries if e.get("kind") == "registration" and e.get("status") == "registered"]
```

`review_checkpoint` entries are therefore **excluded from `due`, `due_unresolved` and coverage**. The
published `counts` said `due: 0, due_unresolved: 0` — true of the Act 22 registrations only, and silently
true of the five overdue checkpoints too. Second defect, same file: the checkpoint block builds each row
and then hardcodes

```python
row["resolution"] = "pending"
```

so even a recorded resolution is printed as `pending`. The scorer is not lying about a value it computed;
it is structurally unable to report this one.

## What I did, and what it establishes

Resolved all five from the named evidence alone, once, at 2026-11-08T23:32:33Z, recording outcome,
resolver, evidence citation, timestamps and reason in `records/predictions/ledger.json#resolutions`
(canonical) and in the separate block `records/predictions/review-checkpoint.json#findings` (Act 22 §9).

- **P1–P4 → `unresolved`.** Their named source is `records/calibration/report.json`, which **has never
  existed in any ref**: `git log --all --oneline --diff-filter=A -- records/calibration/report.json`
  returns nothing, and `records/calibration/` does not exist at `d56d73c`. §3 requires `unresolved` for
  unavailable evidence, with the reason recorded — not a guess at what the report would have said.
- **P5 → `false`.** Its named source *does* exist, and `government/judiciary-measurements.py` line 137
  emits literal `false_positive_rate:None,false_negative_rate:None` (file last changed `c03ac1b`,
  2026-10-23T23:21:46Z). P5 is a conjunction — "interface delivered **and rates are measured**" — and the
  second conjunct fails on the evidence, so the outcome is `false`, not `unresolved`.

**Limits stated:** these are late resolutions. The `resolved_at` timestamps are today's, not the due date;
the lateness is in each `reason`, not smoothed. I did not invent an Act 20 report or backdate anything.

## The duty this exposes

Act 22 §5 requires **one** calibration summary to the Founder per measurement window; §7 P4 makes that a
repeal trigger ("the ledger is maintained and a summary published to the Founder at least once per
window"). None had been published in any window since enactment. The first summary was posted
2026-11-08T23:3xZ with these five resolutions disclosed in it.

## Executive repair, with acceptance criteria (no law needed)

The scorer is `government/` code; the ledger is Clerk-owned (Act 22 §9), so the ledger data is mine and
the reporting logic is not.

1. `review_checkpoint` entries with a recorded resolution must report that outcome, not hardcoded
   `pending`. Negative test: a checkpoint with **no** resolution must still report `pending` (the bug is
   the constant, not the reporting of resolutions).
2. The due/due-unresolved accounting must either count due checkpoints **separately and visibly**
   (e.g. `review_checkpoint.due`), or state in the emitted JSON that they are excluded — silently
   contributing 0 to a total is what hid this.
3. The five current resolutions in `ledger.json#resolutions` must survive a scorer run unchanged; a
   `duplicate_resolution` or `resolution_content_hash_mismatch` defect on them is a regression.
4. `integrity.clean` must stay `true` and no new defect class may be introduced for
   `kind: review_checkpoint`.

**Independently checkable:** re-run `python3 government/predict-scorer.py` and inspect
`records/predictions/calibration.json`; the checkpoints must show the five recorded outcomes.

## Not claimed

- Not claimed: that the Act 20 instrument failed. P1–P4 are `unresolved` because **their evidence was
  never produced**, which is a statement about the record, not about detector behaviour.
- Not claimed: that coverage 0.0 is wrong for Act 22's own registrations — it is right (earliest due date
  2026-11-15), and saying otherwise would be the same error in the other direction.
