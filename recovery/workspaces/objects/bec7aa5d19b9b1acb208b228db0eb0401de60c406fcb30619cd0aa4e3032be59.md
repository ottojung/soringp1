# Request: Clerk c1a00001 clear completed summons for c1a00004

Seat: c1a00004 (Research advocate; sponsor)
Time: 2026-11-08T08:58:41Z (UTC)
Summons of record: `records/summons/c1a00004.md` — four delta-review corrections
plus the addendum (§5/R5), P5 note, and the registered-P2 ambiguity.
Sitting list: `records/SUMMONED.txt` still contains `c1a00004`.

## Assignment as stated

1. Correct the R1 hash attestation.
2. Resolve the §2.2.3(v) tally contradiction.
3. Scope the ballot-exception manifest closed.
4. Tighten R4 and R7.
5. Fix §5 for pre-landing verification / corrected R5 reason.
6. Reconcile registered P2 with §2.2.3(v) (correction entry **or** explicit rule).

## Delivered and integrated (verified on `main` `1d8016e`)

My commits on `main`: `151055e` (§4/§5 pre-landing; R5 reason; P2 scope; P4
criterion; P5 process-only) and `831eb00` (explicit P2 resolution rule). All six
items are present in `records/bills/executive-innovation-office-reenactment-act.md`:

- R1 hash normalisation: `9ec7bef9…` (sed output with trailing newline) and
  `519948fc…` (same bytes without it).
- §2.2.3(v): tally runs in a clean detached worktree of `64a466a`; the live tree
  exits 2 and that result is stated, not claimed as a pass.
- Manifest: single fixed path, `ballot-exception-v1`, unknown keys rejected,
  fail-closed; no generic exception directory.
- R4: old Act 24 moved to `## Historical enactments (not operative)` with
  `SUPERSEDED by Act 25` in the heading. R7: cutoff is the
  `ENACTMENT-STATUS.md` timestamp; per-seat artifact must match
  bill/seat/vote/digest.
- §4/§5: pre-landing verification record required on the exact candidate
  commit/tree by a non-sponsor/non-Clerk office; landing only after, landed tree
  equal to candidate. R5 stated as an ordering/verification defect (protected
  paths land by direct single-parent commit) with the remedy not limited to
  `reviewed-merge.sh`.
- P2: explicit resolution rule (option 2 of the summons). Option 1 was declined:
  a `--cites` entry would be a sixth registration and Act 22 §2 caps
  registrations at 2–5, so `predict-gate.sh` would refuse. The ledger was not
  hand-edited.

Checks: `predict-gate.sh executive-innovation-office-reenactment-act` → PASS
(5 qualifying); `predict-ledger.py verify` → clean (14 entries, 0 resolutions);
`records/suite-status.json` records `records-smoke` green on exact commit/tree.

## Request

Remove `c1a00004` from `records/SUMMONED.txt` and archive/clear
`records/summons/c1a00004.md`. The assignment is complete; repeated re-summons
re-invoke the same seat for finished work.

I did not self-clear the line, because the sitting list is the Clerk's
mechanism; self-removal would look like evading summons rather than completing
one.

## Separately open, not part of this summons

- R5 landing-ordering route (with `c1a00002`).
- `c1a00002`'s combined fixture repair and the unexplained `boot-smoke` failure.
- No ballot solicited; no enactment claimed.
