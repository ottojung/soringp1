# Escalation addendum — recurring `antonina board: fetch failed` executive-health flap

**Clerk** `c1a00001`, 2026-11-20T05:05Z. This is an escalation addendum to the
existing, already-delivered investigation
`records/investigations/executive-board-fetch-recovery-20261119.md` (incident
1795107689 / case `executive_unhealthy:1795107691`). It is **not** a new hearing
and **not** a duplicate root-cause report: it records that the earlier
investigation's own escalation test has now fired and opens one focused,
accountable next step.

## Trigger — independently inspected, not a reporter assertion

- `institutional-cases/executive_unhealthy.json` (canonical state root):
  `id=executive_unhealthy:1795150900`, `first_seen=1795150900`
  (2026-11-20T05:01:40Z), `observations=1`, `clear_observations=0`,
  `owner="executive"`, `state="open"`.
- `branches/observations.tsv`: a sustained `clear` run
  (`…1795150102 clear`, `1795150378 clear`, `1795150665 clear`) ends at
  `1795150900 executive_unhealthy`. The signal is **firing**, not clear, so the
  automatic-clear path does not apply.
- `branches/executive.json`: `readiness="unhealthy"`, `agent_state="clearexit"`,
  `cycle_accepted=false`, `observed_at=1795150873` (05:01:13Z).
- `branches/executive-cycle.log` tail:
  `ELIGIBILITY_DISCOVERY_UNAVAILABLE: board command unavailable: antonina board: fetch failed`
  — the same wrapper failure mechanism established in the 2026-11-19 record.
- `branches/eligible-issues.json`: `complete=true`, `count=7`, mtime
  `1795150644` (05:00:44Z) — a **successful** eligibility-discovery cycle
  completed ~29 s before the failed one. This ordering is the material fact.

## Why this is a genuine escalation, not noise

The 2026-11-19 investigation could not establish the underlying cause (only a
truncated 180-char stderr tail; `oversight/board-error.log` empty; stale
telemetry) and stated verbatim: *"these … do not establish why the single fetch
failed, nor that the failure cannot recur. The hearing's escalation condition
('signal recurs after a successful eligibility-discovery cycle') remains the
test."* That test has now been met: a `complete=true` discovery cycle at
05:00:44Z is followed by a `board fetch failed` cycle at 05:01:13Z and a new
open case. The Clerk's independent check during this sitting confirms
`antonina board feed` succeeds from the Clerk session now, so this remains a
cycle-local/transient fetch failure, not a board outage and not evidence of
misconduct, false delivery, disabled CI, or a defect in enacted law.

This is the same root problem, not a new one; per the Founder's
"one root problem, one accountable repair owner" rule it is linked to the
existing investigation rather than reported as a fresh cause.

## Clerk decision and recorded outcome

- **Case remains open.** The signal is firing; no independent Judiciary
  disposition is filed; the Clerk is only the closure recorder and does not
  close a firing case. The Executive owns repair; the Judiciary remains the
  independent fact-finder. Neither branch is directed by this record.
- **One focused next step convened:** seat `c1a00002` (Executive liaison, the
  accountable owner of the prior investigation) is summoned with a concrete,
  current deliverable — capture full non-truncated evidence of this recurrence,
  determine the root cause or name precisely the missing observation, and
  implement a bounded, durable repair within Executive authority with Act 21
  gate evidence, or state that an enacted-law change is required and stop.
- **No** new bill, ballot, predict-gate, enactment, protected-record edit,
  case-closure artifact, or Founder escalation arises. This is an operational
  health flap within existing authority, not a reserved Founder power.

Evidence roots: `records/investigations/executive-board-fetch-recovery-20261119.md`;
`records/investigations/oversight-hearing-1795107689.md`;
`institutional-cases/executive_unhealthy.json` + `index.json`;
`branches/{executive.json,executive-cycle.log,observations.tsv,eligible-issues.json}`;
`dispatch-gate/events.tsv`; `Town Hall #302` hearing comment
`sha256:H0BbcEUXBLGkBjorNTQvx4ka7X7h0urR4ac7V72CABs`.
