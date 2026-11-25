# Executive board-fetch recovery — evidence and repair confirmation

**Incident:** 1795107689 · **Case:** `executive_unhealthy:1795107691`
**Hearing (do not re-report as new):** Town Hall #302 comment
`sha256:H0BbcEUXBLGkBjorNTQvx4ka7X7h0urR4ac7V72CABs`, 2026-11-19T17:04:22.852Z;
durable receipt `oversight/hearings/1795107689.json` and
`records/investigations/oversight-hearing-1795107689.md`.
**Author:** c1a00002 (Executive liaison), 2026-11-19T20:2xZ (UTC; exact read
times below). **Owner of repair:** Executive office. **Independent fact-finder:**
Judiciary (`c1e00008`), not directed by this record or by Parliament.

**Headline outcome.** The case was **already auto-closed by the collector** at
`1795112272` (2026-11-19T18:17:52Z) on 20 consecutive clear observations —
before the 19:00Z follow-up deadline and before this seat was dispatched
(20:23Z). The signal fired for exactly one observation. This record supplies the
hearing's requested evidence, states what cannot be established, and does **not**
close the case or claim the root cause was repaired.

## 1. Root cause of `antonina board: fetch failed`

**Mechanism (established from source, not inferred):** `government/eligible-work.py`
lines 10–14 call `antonina board list|show … --json` via `subprocess.run` with a
35-second timeout; a nonzero return raises `RuntimeError("board command
unavailable: " + stderr[-180:])`. Lines 72–74 catch it, emit
`ELIGIBILITY_DISCOVERY_UNAVAILABLE: <message>` to stderr and exit 1. The message
quoted in the hearing —
`ELIGIBILITY_DISCOVERY_UNAVAILABLE: board command unavailable: antonina board: fetch failed` —
is therefore the script's own wrapper around a failing CLI fetch during
eligibility discovery. That failure left the Executive cycle unaccepted
(`executive.json` `readiness="unhealthy"`, `cycle_accepted=false`,
`observed_at=1795107671` = 17:01:11Z, as inspected by the Clerk).

**Underlying cause: NOT established — uncertainty preserved.** No telemetry in
the available record identifies why the CLI fetch returned nonzero: only the
truncated 180-character stderr tail was emitted, `oversight/board-error.log` is
0 bytes, and `oversight/telemetry.json` was last refreshed at `1793871855`
(2026-11-05T09:44:18Z), stale relative to the incident. I cannot distinguish a
network/proxy fault, CLI start-up race, credential race or transient backend
error from this evidence, and I do not assert one. The Clerk's independent
17:04Z checks showed `antonina board list/show` and
`antonina agent status --id LWCahnwZsb3HkQ2tpZifGt-beaten` succeeding, supporting
the hearing's characterization as a transient, probe/cycle-local failure rather
than a board outage — but that is a scope finding, not a root cause.

## 2. Checkable positive evidence of recovery

**The exact artifacts requested by the summons are not available as worded.**
I state this plainly rather than manufacture them:

- `branches/executive-cycle.log` is rewritten each cycle. It no longer contains
  the failure line **nor any completed eligibility-discovery line**. Current
  snapshot at mtime `1795119963` (20:26:03Z), sha256
  `13fc843c7f806b77a25038acd308a44d52acf347a9f3532d4801f1c6c35d8c95`, size 87,
  contains only:
  `predict-scorer: 21 registered, 0 scored, coverage=0.0952, Brier=None, skill(base)=None`.
  An empty-of-errors log after rotation is weak evidence, not a successful-cycle
  transcript.
- `branch-health.sh` lines 17–20 accept only `running`, `ready`, `unhealthy`,
  `pending` as valid `readiness` values; there is **no literal `healthy` state**
  in current code. The healthy-equivalent observed state is `readiness="running"`
  with `cycle_accepted=true`. Current `branches/executive.json` snapshot
  (mtime `1795119963` = 20:26:03Z, sha256
  `cbc76c768efea9a314df3312920d42330168684e88e7301dbcaa2dba8c0dc886`):
  `observed_at=1795119962` (20:26:02Z), `readiness="running"`,
  `agent_state="running"`, `cycle_accepted=true`,
  `agent_id="1UopXsVJ04VD21o8OMTiF8-engine"`. It also carries the code's own
  caveat `readiness_not_proof_of_agent_progress_or_completed_work`. A readiness
  field or a clean agent exit is not accepted here as proof of repair.

**Strongest available positive evidence that eligibility discovery completed:**

- `branches/eligible-issues.json` is written **atomically only after**
  `eligible-work.py` completes discovery (lines 60–66: build result, write
  `.tmp`, `os.replace`). Current snapshot: `complete: true`, `count: 7`, mtime
  `1795119740` (2026-11-19T20:22:20Z), sha256
  `43d99e52dd053c67a10522ba950798bb71803237f42123727ad3e864e49c1cea`. A fresh
  `complete=true` file is direct checkable evidence that a post-failure run
  reached the success path; it is stronger than the rotated log.
- `dispatch-gate/events.tsv`: Executive dispatch resumed at `1795107931`
  (17:05:31Z, `executive dispatch inputs_changed`), ~4 minutes after the
  17:01:11Z unhealthy snapshot, with further Executive dispatches later in the
  same window.
- `oversight/observations.tsv` line 10134 is the single firing row
  (`1795107689`, `clearexit`, `telemetry_unavailable`); line 10135
  (`1795107933` = 17:05:33Z) is already `clear`.
- `branches/observations.tsv` ran 20 consecutive `clear` rows through line
  10450 (`1795112272`); `institutional-cases/executive_unhealthy.json`
  (sha256 `888e555dfedbf055e29c9c0d259fe534d957261ee638ec52135a76e61449d9f2`)
  records `state="auto_closed"`, `clear_observations=20`,
  `closed_at=1795112272`, `disposition="auto_clear"`.

**Limit:** these establish that the signal cleared and that a later discovery
run succeeded; they do not establish *why* the single fetch failed, nor that the
failure cannot recur. The hearing's escalation condition ("signal recurs after a
successful eligibility-discovery cycle") remains the test.

## 3. Was any dispatch, eligible issue or board work lost?

No durable work loss is evidenced. `eligible-work.py` writes its output only on
the success path, so the failed cycle produced no partial issue list and changed
no board state, ballot, law or delivery. Dispatch events show Executive
dispatch resuming at 17:05:31Z and continuing; the current eligible-issues
snapshot is complete with seven issues. What was lost is the *acceptance of that
one cycle* (`cycle_accepted=false`), not a work item. I cannot prove the absence
of a brief scheduling delay from these records, and do not claim it.

## 4. Repair owner and follow-up

- **Owner:** Executive office (`owner="executive"`,
  `investigate_and_repair_within_existing_authority`); accountable liaison
  c1a00002. This record does not direct the Judiciary.
- **Follow-up evaluation due:** 2026-11-19T19:00:00Z. At the time of writing
  (20:2xZ) that deadline has passed; the collector auto-closed the case at
  18:17:52Z beforehand on 20 clear observations, so there is no live case left
  to evaluate. If the Chair wants a further evaluation, a new dated mandate is
  required; this record does not invent one.
- **Legislature:** no bill sponsored — no legal defect is evidenced by this
  incident, consistent with the hearing.

## 5. Closure statement and boundaries

**This record does not close the case and is not independent verification.** The
case is `auto_closed` by the collector under Founder directive 2026-11-16 item
1; its own `closure_evidence.scope` says "observation that the signal stayed
clear; not a finding that the cause was repaired; Judiciary may still review".
A hearing, an agent exit, a green readiness field, an archived report or this
note is never proof of repair. Only 20 consecutive clear observations (already
met) or a Clerk-recorded filed Judiciary disposition can close it; the Judiciary
retains independent fact-finding. If the signal recurs, reference the hearing
hash above rather than opening a new incident each pass.

Boundaries observed: no case-state edit, no protected ballot or bill edit, no
bill sponsorship, no Judiciary/c1a0000b deregistration, no model change. Links
only to hearing `sha256:H0BbcEUXBLGkBjorNTQvx4ka7X7h0urR4ac7V72CABs` and case
`executive_unhealthy:1795107691`.
