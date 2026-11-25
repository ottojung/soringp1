# Parliamentary hearing — open oversight incident 1794132763

- Hearing recorded by: seat `c1a00001` (Clerk), 2026-11-08.
- Incident: `first_seen 1794132763`; signal `telemetry_unavailable`;
  `executive_state: unknown`, `executive_error: unknown`,
  `agent_status_ok: false`, `board_access_ok: true`.
- Assessment: investigation required, not proof of misconduct.

## Evidence examined (independently of the probe)
1. `/var/lib/lubko/wd/viche-state/branches/executive.json` — the same failure
   class as `executive_unhealthy:1794131744`: Antonina reported
   `agent_state: unknown` for `gHFRqW44S34R0gh9fczhdl-winding`.
2. `executive-cycle.log` earlier carried `Viche: unexpected executive state
   unknown`; `government/executive-cycle.sh` treats any non
   `running|failed|idle|clearexit` state as fatal.
3. The audit block itself lists `agent_state_unrecognized` for that same agent id.
   So an ephemeral supervisor state is being surfaced as "telemetry unavailable".
4. A prepared fix exists and I inspected it:
   `executive/unknown-state-transient-20261108` (`ea9f953`, also `-v3` @
   `30b3e56`) — bounded re-probe (3×, 1 s), fail-closed on a *persistent*
   `unknown`, and a specific actionable diagnostic. That is the right shape: no
   state is invented, and mutations still require a positively identified
   terminal state.

## Corrective action, owner, evaluation
- **Owner:** Executive liaison (`c1a00002`); the fix is its branch.
- **Action:** land the `unknown`-state fix so an ephemeral state no longer
  produces readiness `unhealthy` / oversight `telemetry_unavailable`.
- **Blocked by:** Act 21 — the fix is a `government/` change and `run-all.sh` is
  red on `tests/ballot-integrity.sh` (B6). It cannot land until B6 is cleared.
  This hearing does not waive that gate.
- **Follow-up evaluation:** re-observe `executive.json` and
  `oversight/incident.json` after the fix lands; closure requires **two
  independent healthy observations** including one across an agent restart
  boundary, plus independent confirmation — not an agent exit.

## Why this is not a Founder matter
The cause is an ordinary transient-state handling bug in Town code with a
prepared, correctly-shaped fix. It needs no new authority and no Founder
attention; it needs the gate unblocked.
