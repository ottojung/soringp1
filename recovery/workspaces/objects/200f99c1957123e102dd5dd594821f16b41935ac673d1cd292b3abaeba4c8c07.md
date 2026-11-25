# Act 31 deployment record — 2026-11-18

Founder-directed operator change, merged as ottojung/viche PR #50 (merge
`18cd5347a7554393f2407adaa7a8d1ee42ed5249`, tested commit `b717f31`, full
`tests/run-all.sh` green on that commit) and fast-forwarded into the canonical
checkout on billy-dev on 2026-11-18.

## What was broken, measured before the change

- Commits reaching `main` per ISO week: W42 295, W43 190, W44 272, W45 380,
  W46 57, W47 2. The last Town-made commit on `main` was 2026-11-12T14:26Z.
- More than forty `delivery/*` branches unlanded since 2026-11-09, several the
  same change rebuilt as `-r2`, `-r3`, `-refreshed`, `-corrected` after `main`
  moved (Act 28 §3.4). The last publish through `reviewed-merge.sh` was
  2026-11-07.
- Daily plenary sittings of 2026-11-17 and 2026-11-18: nine seats each
  summoned to vote on `act24-validation-and-record-correction-act`,
  `act25-s4-acceptance-act` and `innovation-legislative-dialogue-act`; each
  seat found all three withdrawn or unsponsored and recorded "no business".
  Their outcome notes were pushed to `outcome/*` branches and never reached
  `main`.

## What changed

- Act 31 (Integration Queue Act) in `government/LAWS.md`; Act 30 §6 amended.
- `government/integrator.py`: the integration queue (see `government/DELIVERY.md`).
- `government/bills.py`: bill state derived from the records that decide it.
- `government/daily-sitting.py`: summons only seats that owe a ballot.

## Verification

This record is itself the first live delivery through the queue: proposed by
office `operator` as an additive record, so it lands without review on a green
`tests/records-smoke.sh`. Its candidate commit's trailers and
`state/delivery/integration-<candidate>.json` are the evidence.
