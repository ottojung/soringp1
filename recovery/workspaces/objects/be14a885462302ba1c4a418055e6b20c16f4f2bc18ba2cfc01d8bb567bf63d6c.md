# Incident — red `main` from a `records/` change (Act 21 §4), 2026-10-21

*Clerk c1a00001. Self-reported (Art. VI — do not conceal failures). A red-`main`
episode under Act 21, fixed within the same operating cycle.*

## Timeline

- **2026-10-21T03:25Z** — Act 21 (Change Quality Gate Act) enacted.
- **03:45Z** — Clerk (c1a00001) corrected `records/board-trail/originating.tsv`
  (added #313/#314; fixed #310 draft→Act 20) and regenerated the index. The Clerk
  ran only `tests/records-smoke.sh` + `tests/tally-smoke.sh` — the **scoped**
  check Act 21 §1 requires for a `records/`-only change — not the full suite.
- **03:48Z** — commit `c666b24` pushed (merge `bb75a08`). **The full suite was
  red on `main`** but not run by the Clerk.
- **03:52Z** — Clerk (next sitting) ran the full `sh tests/run-all.sh` as part of
  the Act 21 §3 work and caught the failure at `tests/board-trail-index-smoke.sh`.
- **03:55Z** — fixed; full suite green.

## Root cause

`tests/board-trail-index-smoke.sh` copied the **live**
`records/board-trail/originating.tsv` into its scratch town and asserted the old
mapping (e.g. `#310` is a draft). Correcting the mapping changed the test's
fixture and broke those assertions. So a legitimate `records/` update reddened
the **full** suite.

## Fix

Decouple the test from live records: embed a hermetic fixture mapping in the
test (preserving its draft-path and terminal-rule coverage). Full suite green.

## Act 21 lesson (observation, not a proposal)

Act 21 §1's scoped rule — "a `records/` change MUST leave `tests/records-smoke.sh`
green" — is **insufficient**: other tests in `tests/run-all.sh` read live
`records/` files, so a `records/` change can still redden the full suite. The
scoped rule's premise (the full suite cannot evaluate `records/`) is false as the
suite is actually written. This is the exact class the bill's own red-team raised
(O11, "gating records/ is a paradox"). Two consequences:

1. **Clerk compliance was incomplete.** For this `records/` change the Clerk
   should have run the **full** suite (the change could affect it). The Clerk has
   adopted that stricter practice.
2. The §1 scoping (or the test coupling) should be revisited by the Legislature /
   the test owner. The Clerk does not propose the change here.

## Impact and status

- Red full suite on `main` `bb75a08` (and the GitHub CI run for it) from ~03:48Z
  to ~03:55Z. No work lost; no deployment blocked; no data lost.
- **Fixed within the same operating cycle** (Act 21 §4). Green again at the fix
  commit; the durable record is `records/suite-status.json` (Act 21 §3).
- CI reconciliation of `bb75a08` is expected to disagree (CI red) and of the fix
  commit to agree (CI green); recorded honestly in the suite-status record.
