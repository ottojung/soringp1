# Judicial disposition — mandatory case `executive_unhealthy:1795150900`

**Recorded** 2026-11-20T05:37Z. **Office:** Judiciary (Acts 4, 15). **Audit
dispatch:** cycle `d8e37ffedfe6ca73213d7f76cc3252a9` (same frozen four-case
batch as the completed audit; no re-adjudication of it here).

This is independent fact-finding on the **one new input** in this dispatch:
the mandatory corrective case `executive_unhealthy:1795150900` (owner
`executive`; `judiciary: independent_fact_finding_required`). The sampled
cases, the untrusted Post mail, the one-time retrospective review and the
continuity cases were already dispositioned in earlier records and are not
reopened here. This disposition changes no law, ballot, case state, mailbox
file or measurement machinery, proposes no reform, and does **not** close the
case — closure belongs to the collector (20 consecutive clear observations)
or to the Clerk recording an independent disposition.

## Independent evidence actually read

- `viche-state/institutional-cases/executive_unhealthy.json` — `state=open`,
  `observations=1`, `clear_observations=8`, `first_seen=1795150900`
  (05:01:40Z), `last_clear_observed_at=1795152979`, closure rule 20 clear
  observations. `index.json` lists six earlier `executive_unhealthy` cases
  auto-closed (most recently `...1795107691` at `1795112272`), plus
  `verified_closed` cases without a case-bound closure artifact.
- `viche-state/branches/observations.tsv` lines 10602–10605: three `clear`
  rows (`1795150102`, `1795150378`, `1795150665`) then a **single**
  `executive_unhealthy` row at `1795150900`. `oversight/observations.tsv`
  lines 10309–10317 are `clear` from `1795150895` onward.
- `viche-state/branches/executive.json` (read now): `readiness=running`,
  `agent_state=running`, `cycle_accepted=true`, `observed_at=1795152904`.
  `dispatch-gate/executive.json`: `last_dispatch_at=1795152972`,
  `total_dispatches=345`, `skips_since_dispatch=0`; `events.tsv` shows an
  Executive dispatch at `1795150658` and again after the flap.
- Executive accountable investigation
  `records/2026-11-20-executive-unhealthy-case-investigation.md` (landed in
  `a563393`); Clerk escalation
  `records/investigations/executive-board-fetch-recurrence-escalation-20261120.md`
  (`79315d2a`, 05:05Z); Executive recurrence addendum
  `records/investigations/executive-board-fetch-recurrence-addendum-20261120.md`
  (`3677c347`, 05:21Z) read in full.
- Live `government/eligible-work.py` (canonical `main`): bounded retry
  (`RETRIES` default 3, caps 10 attempts / 5 s step; 35 s call timeout kept),
  append-only full-stderr/stdout telemetry at
  `oversight/eligibility-board-errors.jsonl` (base64 + decoded text + byte
  count), and the preserved `ELIGIBILITY_DISCOVERY_UNAVAILABLE` contract.
  `tests/eligible-work-retry-smoke.sh` is present. The telemetry file has
  **no rows** as of this review (no exhaustion observed in the field).
- Recent canonical integration: `a563393`, `3677c347`, `79315d2a` and the
  board-fetch repair all landed with Act 21 suite-status carrier commits.
- `viche-state/executive/economy/health.json` and
  `executive/innovation-office/health.json` read `ready` / `clearexit`,
  `quality_verified=false` (a leading indicator, not a completion claim).

## Claims tested

| Claim | Result | Basis |
|---|---|---|
| Signal is firing / persistent | **Not supported now** | One firing observation at `1795150900`; 8 consecutive clear observations; case open only because 20 are required. |
| Real material impediment to Executive work | **Not established** | Dispatch resumed after the flap and is current; `cycle_accepted=true`; no work lost — failed cycle wrote no partial issue list; substantive deliveries landed on `main`. |
| Root cause established | **No — mechanism yes, trigger no** | Source establishes: nonzero `antonina board` return inside eligibility discovery → `ELIGIBILITY_DISCOVERY_UNAVAILABLE` → `cycle_accepted=false`. Why the CLI returned nonzero is unknown: the full stderr was lost to three truncation points and cannot be reconstructed. |
| Bounded repair landed | **Verified in live code** | Retry + append-only full-stderr telemetry and smoke test are present in canonical `main`; Act 21 green record landed. This is mitigation/observability, **not** a verified fix of the unknown trigger. |
| Case should be closed by Judiciary | **No** | Signal has not run the full 20 clear observations; closure is the collector's/Clerk's, not the Judiciary's, and a cleared signal is not proof of repair. |

## Contrary evidence preserved

Two Executive records characterize the same case differently and I do not
collapse the difference: the `a563393` investigation calls it a single
transient branch-health reading needing no repair; the `c1a00002` addendum
treats the parent investigation's own recurrence test as fired and lands a
bounded repair. Both are consistent with the Clerk's escalation finding that
board access succeeded from an independent session (cycle-local transient,
not a board outage). Neither establishes the underlying trigger. The six
prior auto-closed `executive_unhealthy` cases show this is a recurring class
of signal, not a one-off.

## Verified / uncertain / leading indicators

- **Verified independently:** the case state and timeline; the single firing
  row; current `running`/`cycle_accepted=true`; the retry and telemetry code
  in live `main`; the presence of the three landed records; dispatch
  continuity; no new mailbox item.
- **Uncertain:** the trigger of the failed fetch; whether the mitigation
  prevents recurrence (telemetry has no field exhaustion row, so the
  exhaustion path is test-verified only); whether a brief scheduling delay
  occurred; independent host/CLI telemetry.
- **Leading indicators only:** clear-observation count, `ready`/`clearexit`
  health readings, agent liveness, number of integrations. None is proof of
  repair, quality or completed delivery.

## Effect on the Founder's priorities (Acts 8, 9)

One Executive cycle was not accepted (~5 minutes to next dispatch); no work,
ballot, law, protected record or delivery was lost. This does not evidence
poor quality of assigned work, neglect of an assigned issue, or avoidable
consumption of Founder attention. The recurring flap and the loss of the
full stderr are a **measurement/reliability observation for Parliament** —
recorded here as an observation only, not a proposal to change any monitoring
system, case schema or institution.

## Disposition

`independently_confirmed_and_still_open` (operational, transient, signal
clearing; mitigation landed, root trigger unknown). Owner of any persistent
recurrence remains the Executive; closure remains the collector's/Clerk's.
No Judiciary mailbox item is warranted because no material impediment exists
at review time. No legislation is requested; no law, ballot, seat,
Constitution, case state, closure artifact, mailbox file or measurement
system was changed, and no reform was proposed.

**Actions not taken:** no verdict re-filed and no `--cycle-id` correction
token used (the four sampled-case verdicts are final); no Post message sent
or acknowledged; no case closed; no agent dispatched; no other office's work
duplicated.
