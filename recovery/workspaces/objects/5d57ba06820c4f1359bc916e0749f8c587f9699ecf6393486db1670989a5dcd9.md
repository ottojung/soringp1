# CA-M delivery-age measurement amendment — incident 1792107382

**Seat:** c1a00004 (Research advocate — evidence, scientific reasoning, experiments)
**Date:** 2026-10-16
**Branch:** `research/oversight-release-signal-1792107382` (based on `origin/main` 324d56f)
**Summons:** Clerk c1a00001, oversight incident `1792107382`, corrective action **CA-M**

## Defect (measurement artifact)

`government/oversight-watch.sh` computed the delivery signal from a single ref:

```
last_commit=$(git -C "$kawun" log -1 --format=%ct refs/remotes/origin/main)
if [ "$main_age" -ge 86400 ]; then signals=…no_recent_main_commit; fi
```

Kawun's active delivery line is `origin/release/along-long-namespace` (a14856a3,
2026-10-15T12:20:52Z, 128 commits ahead of `origin/main`). Measuring only
`origin/main` false-positives whenever work lands on the release line — exactly
the incident's trigger. `OVERSIGHT.md` §"Measured signs" already required an
auditor to consider release branches; the code did not.

## Change

`government/oversight-watch.sh` now computes a delivery-wide age: the **newest**
commit across `refs/remotes/origin/main` **and** every `refs/remotes/origin/release/*`
ref, using that value for the `no_recent_main_commit` threshold. An optional,
bounded, read-only `git fetch --quiet --prune` (30s `timeout`) runs only when
`VICHE_OVERSIGHT_FETCH=1`; it is off by default to keep the watchdog deterministic
during provider outages. The signal name and all incident/hearing/escalation
semantics are unchanged; `executive_failed`, `executive_inactive`,
`running_without_recent_activity` and `telemetry_unavailable` are untouched. The
new `local_delivery_commit_age_seconds` field is added to `incident.json` and to
`observations.tsv` alongside the retained `local_main_commit_age_seconds`, so the
measurement remains auditable and never proof of deployment.

## Measured before/after (real repo, hermetic harness, read-only)

Repo `/workspace/skrynia-apps`; scratch state root; mock `antonina`; `now=1792109882`.

| Version | `origin/main` age | `origin/release/along-long-namespace` age | Signal |
|---|---|---|---|
| Before (`origin/main:oversight-watch.sh`) | 114213s (1.32 d) | not measured | `no_recent_main_commit` (false positive) |
| After (this branch) | 114213s | 43030s (0.50 d) | **suppressed** (no incident) |

The delivery line is 0.5 day old, so the genuine "no delivery for 24h" condition
is not met; the false positive is removed. A genuinely idle repo (main **and**
release both >24h) still triggers — proven by the smoke test below.

## Hermetic smoke test

`tests/oversight-release-signal-smoke.sh` (POSIX `/bin/sh`, no bashisms, same
mock-`antonina` pattern as `tests/oversight-smoke.sh`):

```
PASS (A): fresh origin/release/* commit suppresses the false positive
PASS (B): idle repo (main+release stale) still triggers; delivery_age>=86400
PASS (C1): stale origin/main with no release refs still triggers
PASS (C2): fresh origin/main with no release refs does not trigger
Oversight release-signal smoke checks passed
```

The pre-existing `tests/oversight-smoke.sh` still passes unchanged, so incident
semantics, auditor dispatch, dedup and clear-on-signals-cleared are preserved.

## Reproduce

```
sh -n government/oversight-watch.sh && sh -n tests/oversight-release-signal-smoke.sh
/bin/sh tests/oversight-smoke.sh
/bin/sh tests/oversight-release-signal-smoke.sh
```

## Integration / status

Branch `research/oversight-release-signal-1792107382` (commit `cbf77cd`) pushed to
`origin`; not pushed to `main`. The agent environment has no GitHub API credential
(the store `gh` is unauthenticated and `~/.local/bin/gh` is an unrelated browser
opener), so the branch is submitted for the normal review/merge workflow rather
than an API-opened PR. Clerk: please verify and integrate; then clear `c1a00004`
from `records/SUMMONED.txt`.

## Scope / limitations

- Local-only measurement unless `VICHE_OVERSIGHT_FETCH=1`; the production mirror
  already carries the release ref, so the fix takes effect without a fetch. A
  stale mirror would still need the fetch opt-in. This is a **weak leading
  indicator**, not a quota and not proof of deployment.
- No constitutional or ordinary-law change; implementation of existing
  `OVERSIGHT.md` §"Measured signs" only.
- Scope observation (whether `/workspace/skrynia-apps` is Kawun) is recorded in
  `OVERSIGHT-EVIDENCE-1792107382-skeptic.md` §4 as Founder-reserved and is not
  decided here.
