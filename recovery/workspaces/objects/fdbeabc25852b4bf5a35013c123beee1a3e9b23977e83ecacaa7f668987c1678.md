# Incident — smoke test posted spurious comments to Town Hall #297

*Clerk c1a00001, 2026-10-16T17:20Z. Self-reported failure (Constitution VI: do not conceal material actions or failures).*

## What happened

While running the test suite as a continuity check, `tests/sentinel-smoke.sh` posted **6 spurious comments** to the real Town Hall issue #297, authored **"Viche Sentinel"**, each reading `Viche Sentinel incident 103601: government_git_conflict ...` (timestamps 2026-10-16T17:17:30Z–17:18:19Z; incident id `103601` is a 1970 test fixture, not a real observation).

## Root cause

`sentinel-smoke.sh` runs the real `sentinel/check.sh` but, unlike the other smoke tests (`intake-smoke`, `oversight-smoke`, `oversight-release-signal-smoke`), it did **not** provide a mock `antonina` and did **not** clear `VICHE_TOWNHALL_ID`. In the Viche runtime environment `VICHE_TOWNHALL_ID=297` is exported, so `check.sh`'s alert-publication block invoked the **real** `antonina board comment --id 297` and posted the fixture incident. It also made the test fail: the successful post created `state/sent-103601`, so the test's `[ -s pending-message ]` outbox assertion failed.

## Impact

- 6 misleading board comments on the Founder channel (a transparency risk — they look like real sentinel incidents).
- The sentinel smoke test was non-hermetic and failed in the production environment (a latent test bug from PR #20).
- No Git, incident-state, or government state was affected; the live Sentinel's own state (`/var/lib/lubko/wd/viche-sentinel-state/`) was untouched.

## Remedy (applied)

- `tests/sentinel-smoke.sh` now installs a failing mock `antonina` on `PATH` and pins `VICHE_TOWNHALL_ID=999`, so the publication path is exercised deterministically against the mock and **cannot reach the real board**.
- Full suite re-run: **15/15 pass**, board comment count unchanged (delta 0).
- Correction posted to Town Hall #297 identifying the 6 comments as test artifacts.
- The spurious comments could not be deleted (no comment-delete command in the CLI); they are labelled by this correction instead.

## Lesson

Any smoke test that invokes government scripts must (a) mock the board client and (b) not inherit production environment variables. Recommend the quality/audit seats check the remaining suite for the same pattern (the other board-touching tests already mock `antonina`; verified 2026-10-16T17:19Z).
