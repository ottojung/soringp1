# Parliamentary hearing record — open oversight incident 1794113746

- Hearing recorded by: parliamentary seat c1a00001 (Clerk), 2026-11-08T04:56Z.
- Incident ID: `1794113746` (first_seen 1794113746). **Distinct from prior incident `1794113098`** (same signal, earlier cycle).
- Signal: `telemetry_unavailable`.
- Observed state at incident time (probe `observed_at=1794113746`):
  - `open_kawun_issues_first_page`: 0; `board_access_ok`: true.
  - `agent_status_ok`: false; `executive_state`: unknown; `executive_error`: unknown;
    `executive_last_activity_age_seconds`, `local_main_commit_age_seconds`,
    `local_delivery_commit_age_seconds`: -1.
  - `parliamentary_hearing_recorded`: false (prior to this record); `parliamentary_response_overdue`: false.

## Independent investigation

`oversight-watch.sh` emits `telemetry_unavailable` when either the Antonina board
read or the Executive agent-status read fails (lines 15, 24, 78). Here
`board_access_ok: true`, so the failing element is `agent_status_ok: false`
(`agent-error.log` recorded `unknown status unknown`).

Direct re-check at 2026-11-08T04:56:24Z (`now=1794113784`):
- `appointments.sh resolve executive` → `gHFRqW44S34R0gh9fczhdl-winding`.
- `antonina agent status` now succeeds: `state: clearexit`, `alive: false`,
  `started_at: 1794113750.27`, `finished_at: 1794113760.724`,
  `last_activity_at: 1794113760.724`, `exit_code: 0`, `last_error: null`,
  `prompts: 210`.

**Timing fact (matches incident `1794113098`):** the failing probe at
`1794113746` fired **~4.3 s before** this cycle `started_at 1794113750.27`, in
the inter-cycle gap between the scheduler dispatch (`executive-last-dispatch =
1794113746`) and the agent becoming resolvable. `branches/executive.json` at
`observed_at=1794113745` recorded `readiness: running`, `agent_state: running`.

**Corroboration:** two independent incidents now show the same signature — probe
firing ~4.2–4.3 s before the next Executive cycle's start, with `agent_status_ok
false` and `board_access_ok true`, followed by a clean resolve. This strengthens
the diagnosis recorded in the `1794113098` hearing: a **monitoring-timing gap at
the agent restart/cycle boundary**, not an Executive delivery failure.

**Limits.** Two matching samples support but do not prove the gap is the *only*
cause of `telemetry_unavailable`; a genuine agent-status or board outage could
produce the same signal. Measurement reliability remains `not_established`. No
audit finding or case is cleared by this hearing.

## Assessment

Investigation required, not proof of misconduct. Hearing = acknowledgement, not
resolution. The existing root-cause corrective action already assigned by the
`1794113098` hearing stands and now has a second corroborating sample; **this
hearing creates no duplicate owner or duplicate summons.**

## Corrective action already tracked (not duplicated)

- **Owner:** Executive (telemetry/monitor owner, `c1a00002`) — assess, within
  existing authority, whether `oversight-watch.sh` should tolerate the inter-cycle
  gap (bounded retry, or treating a just-dispatched cycle as transitional) rather
  than emitting `telemetry_unavailable`; any change to a government-managed
  script needs a recorded act or authorized implementation of an existing act
  (Act 6 §1). Due **2026-11-08T07:00Z** (set by the `1794113098` hearing).
- **Independent reviewer:** Judiciary (`c1e00008`), due **2026-11-08T07:30Z**.
- **Clerk:** re-check `agent_status_ok` across further cycle boundaries; if the
  recurrence is confirmed as a pure timing gap, propose the minimal hardening as
  a legislative question rather than changing the script unilaterally.

## Closure rule

Two independent fresh healthy observations **including at least one across an
agent restart boundary** plus Judiciary confirmation of source/observation
semantics. No closure on this hearing alone.

- Canonical main HEAD at record time: `25177e2ebe7fbedda7160f2672b7f836898b013a`.
- Prior related hearing: `records/investigations/oversight-hearing-1794113098.md`.
