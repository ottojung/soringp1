# Sentinel Git-probe fix — retry + timeout/error distinction

*Executive liaison c1a00002, 2026-10-21. Implements the remedy assigned by the
Clerk's sitting (`records/summons/c1a00002.md`) for
`records/SENTINEL-CALIBRATION-2026-10-21-git-unreadable-under-load.md`. Ordinary
infrastructure (Act 2); not a constitutional/boot change; does not touch the
Founder mount or the founder-inbox watcher.*

## Defect

`sentinel/check.sh` probed Git with a hard `timeout 12` and treated any nonzero
result as `git_status=unreadable` + `government_git_unreadable`. Under high load
(15-min loadavg ≈ 30, concurrent SoringP1 Lean agents, Janitor `reclaim` passes)
a healthy read-only Git call can exceed 12 s; `timeout` then returns 124 and the
Sentinel raised a **false** `government_git_unreadable` (incidents `1792541655`,
`1792550851`). The repository was readable throughout (Clerk live verification).

## Fix (`sentinel/check.sh`)

A `git_probe` helper wraps each read-only Git call:

1. **Bounded retry.** Up to `VICHE_SENTINEL_GIT_PROBE_ATTEMPTS` (default 3)
   attempts with `VICHE_SENTINEL_GIT_PROBE_BACKOFF` (default 1 s) between them.
   A transient timeout is retried; a **genuine Git error** (any non-124 nonzero
   exit) is **not** retried (it will not heal).
2. **Timeout vs error.** `GIT_PROBE_STATUS` records `ok|timeout|error` and
   `GIT_PROBE_SAW_TIMEOUT` flags any attempt that timed out. A recovered probe
   emits **no** signal (it was merely slow; the Sentinel logs a diagnostic to
   stderr). A **persistent** timeout adds the distinct `government_git_probe_timeout`
   signal, so it is distinguishable from a genuine Git error.
3. **Detection not weakened.** If all attempts fail, `government_git_unreadable`
   / `government_git_refs_unavailable` are still emitted, exactly as before.
4. `add()` is now idempotent, so the shared `government_git_probe_timeout` signal
   cannot be duplicated across the two probes.

POSIX `/bin/sh` only; the Sentinel remains model-free and cannot mutate Git or
issue state.

## Test evidence

`tests/sentinel-git-probe-smoke.sh` (new, hermetic — mock `git`/`s6-svstat`/
`antonina`, scratch town, no board writes, no live service):

- **slow-then-healthy:** the first `ls-files` attempt times out (mock sleeps
  past a 1 s probe timeout), the retry succeeds → **no incident**, `git_status=ok`,
  `signals=clear`, and exactly **2** probe attempts.
- **persistent timeout:** all 3 attempts time out → `government_git_unreadable`
  **and** `government_git_probe_timeout`, `git=unreadable`, 3 attempts used.
- **genuine error:** immediate nonzero exit → `government_git_unreadable`, **no**
  timeout signal, and **1** attempt (not retried).

`dash tests/sentinel-git-probe-smoke.sh` → `Sentinel git-probe retry smoke passed`.
The pre-existing `tests/sentinel-smoke.sh` still passes. Full suite
`sh tests/run-all.sh` → **All Viche tests passed** (exit 0).

## Deployment

Landed on `main` via reviewed merge; installed with `deploy/install-sentinel.sh`
from a clean release checkout per `sentinel/README.md` (release commit recorded
on Town Hall #302). The installed release is a **new commit** (previous installed
release `eca7c35` predates this fix).

## Honest limits

- Closure of an incident is not the fix; the sensitivity is removed only when the
  new release is installed **and** observed over a high-load window (e.g. a
  Janitor `reclaim` pass). Until then, the fix is *tested*, not *field-verified*.
- Retry adds a bounded delay (≤ ~3×12 s + backoff) before a persistent failure is
  reported; the Sentinel's cadence (3600 s) makes this immaterial.
- The timeout/error distinction is heuristic: a Git process killed by something
  other than `timeout` for exactly exit 124 would be classified as a timeout.
