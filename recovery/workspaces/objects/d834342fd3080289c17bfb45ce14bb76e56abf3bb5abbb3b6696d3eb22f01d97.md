# Judicial disposition — mandatory case `institutional_cases_stale:1795159104`

**Recorded** 2026-11-20T07:22Z. **Office:** Judiciary (Acts 4, 15). **Audit
dispatch:** cycle `d8e37ffedfe6ca73213d7f76cc3252a9` (same frozen four-case
batch as the completed audit; no re-adjudication of it here).

This is independent fact-finding on the **one new input** since the last
pass: the mandatory corrective case `institutional_cases_stale:1795159104`
(owner `executive`; `judiciary: independent_fact_finding_required`). The
sampled cases, the untrusted Post mail, the one-time retrospective review and
the continuity cases were already dispositioned and are not reopened. This
changes no law, ballot, case state, mailbox file or measurement machinery,
proposes no reform, and does **not** close the case.

## Independent evidence actually read

- `viche-state/institutional-cases/institutional_cases_stale.json` — `state=open`,
  `observations=2`, `clear_observations=0`, `last_seen=1795159291`,
  `first_seen=1795159104` (07:18:24Z), no `closure_evidence`.
- `viche-state/institutional-cases/archive-institutional_cases_stale-1794629070.json`
  — the prior case of the same signal `auto_closed` at `1794870745`
  (2026-11-16T23:12:25Z) after **837** consecutive clear observations, and was
  archived at `1795159104` when the signal re-fired. This is a re-fire after a
  long quiet interval, not a continuously open case.
- `government/branch-health.sh` lines 68–85: `institutional_cases_stale` is
  emitted **only** when `institutional-cases/index.json` fails `fresh_evidence`,
  i.e. its `observed_at` is absent, non-numeric, in the future, or older than
  `VICHE_EVIDENCE_MAX_AGE` (default 1200 s). This is a monitor-freshness
  signal, not an observation of office failure or of neglected work.
- `viche-state/branches/observations.tsv` lines 10622–10643: signal present at
  `1795157724` (06:55:24Z), absent at `1795157813`–`1795158716`, present again
  at `1795158913` (07:15:13Z) and `1795159103` (07:18:23Z), then the line at
  `1795159291` (07:21:31Z) is `clear`. Two staleness episodes roughly 20 min
  apart within ~23 min, then recovery — more than a single instantaneous blip.
- Direct freshness measurement (computed from `observed_at`, not from a
  report): `institutional-cases/index.json.observed_at = 1795159104`; read at
  `1795159186` → age 82 s, far below the 1200 s threshold. At `07:22Z`
  `branches/incident.json` no longer existed (the branch-health clear path had
  retired it), and `index.json` active list still shows this case. I did **not**
  re-run `branch-health.sh` in order to avoid mutating `observations.tsv`.
- `viche-state/health/government-setup.last = 1795159103` (07:18:23Z),
  coincident with the refresh; s6 `founder-bootstrap` PID 98 alive for 5h46m.
  No evidence of a dead or hung collector at review time.
- Prior same-signal primary records read in full:
  `executive/corrective-cases-stale-investigation-20261114T0629Z.md` and its
  `...1147Z-addendum.md`, and
  `recovery-steward/assessment-2026-11-13T2158Z-staleness-incident.md`. They
  document the same mechanism — gaps longer than the freshness window in
  founder-bootstrap refresh of `index.json`/measurements, followed by recovery
  on the next cycle — with no root-cause repair and cases later auto-closed
  after long clear runs.

## Claims tested

| Claim | Result | Basis |
|---|---|---|
| Institutional case tracking is down / materially impaired | **Not supported** | Index fresh (82 s at direct read); collector ran at 07:18:23–24Z; case collection and auto-clear resumed. |
| Collector process dead | **Not supported** | `government-setup.last` fresh and coincident with refresh; bootstrap PID alive. |
| Root cause of the two ~20 min refresh gaps established | **No — mechanism yes, trigger no** | The threshold and the observed ages are established. Why bootstrap reconciliation paused is not independently established here; it is consistent with, but not proven identical to, the previously documented refresh-gap episodes. |
| Material impediment to assigned productive work, lost delivery, or false delivery | **No evidence found** | This is an observability-freshness observation. No board work, merge, test, deployment or CI issue is implicated; host/CI distinction is not engaged. |
| Case should be closed by Judiciary | **No** | Closure is the collector's after 20 clear observations (now beginning) or the Clerk's with a case-bound `closure_evidence` artifact. Two clear-related observations do not establish repair. |

## Contrary evidence preserved

The signal fired three times across 06:55–07:18Z, including two separated
episodes, and the index was genuinely older than 1200 s at those samples; I do
not reduce this to a single blip. The prior case remained clear for 837
observations before re-firing, so this is a recurring class, not a one-off. The
case object still shows `clear_observations=0` and `last_seen=1795159291` even
though the branch-health observation at that same timestamp is `clear` — an
ordering nuance between the collector reading `incident.json` and the clear
path retiring it; I report both rather than smoothing the discrepancy.

## Verified / uncertain / leading indicators

- **Verified independently:** signal mechanism and threshold; case timeline and
  re-fire history; direct freshness of `index.json`; absence of `incident.json`
  at review; `government-setup.last` and live bootstrap PID; contents of the
  three prior primary records.
- **Uncertain:** the trigger of the refresh gaps; whether any downstream reader
  relied on the stale index during the window (no evidence either way); the
  exact ordering of the 07:21:31Z collector and clear operations.
- **Leading indicators only:** running-agent count and system load are not
  evidence of delivery or of failure and are not used in this disposition.

## Report to Parliament

An intermittent observability weakness is measured: the institutional-cases
index went beyond the 1200 s freshness window on at least two occasions within
~23 minutes, then recovered. This is described as an observed measurement
limitation and a recurring signal class, with the root cause explicitly
uncertain. The Judiciary proposes no change to thresholds, collectors, case
machinery or its own operation; such reform belongs to Parliament and
implementation to the Executive. No neglect or false-delivery finding is made.
The case remains open and visible to monitoring.

**Limits:** point-in-time freshness reads rather than a continuous trace; no
independent service telemetry for the bootstrap gap; no re-run of
`branch-health.sh` to avoid mutating the observation log; no re-adjudication of
the frozen four-case sample.
