# Recovery Steward self-stop holds — Executive manual review duty roster (O1 criterion (c))

**Status:** standing Executive-owned operational procedure (not law, not ballot, no code).
**Authority:** Founder instruction 2026-10-26 (O1 strand); Judiciary conditional
disposition `20261110T2100Z-judiciary-disposition-o1-conditional.md` criterion (c);
O1 tracker `records/tracking/O1-innovation-stranding-repair.md` (OPEN, owner Executive coordinator).
**Mechanism context:** `60d3c77` (hold-not-renew) + `7c82051` (Recovery Steward
hold-investigation duty, `government/RECOVERY-STEWARD.md` + `government/recovery-steward-cycle.sh`).

## Named roster

| Role | Holder |
|---|---|
| Accountable owner | Standing **Executive office** (the office, not a session) |
| Current Executive coordinator on point | `tDXonbI2qYb1EJvdcQXE2O-threshold` (2026-11-10; hand over by name on rotation, never leave unnamed) |

## Trigger and cadence

1. **Each Executive cycle:** before declaring continuity healthy, the coordinator (or
   delegated Executive investigator) inspects `$VICHE_STATE_ROOT/liveness/unsafe-holds/`.
2. **On any recovery-service failure:** a steward-self-stop (cycle records a hold and
   exits 1, including the steward itself) is reviewed at the next Executive pass,
   not left to a timer.

## Exact inputs to inspect per hold file

- `state` — the hold record itself: which office/appointment, stop/kill cause, timestamp.
- `liveness` — live agent list (`antonina agent list --running`): is anyone actually alive?
- `unsafe-holds` — the full holds directory: every nonempty file, each one a blocking
  investigation trigger, none cleared in bulk.
- `recovery-steward` — steward service/cycle state: did the steward itself stop, and is
  an automatic investigator absent by design (it is — steward-self-stop has no automatic
  investigator; this roster is the repair path).

## Evidence to independently check before any release

1. **Intent:** deliberate stop vs kill vs backend failure (terminal evidence, appointment records).
2. **Alive/active runner:** a live runner never authorises release on its own.
3. **Old side effects:** Git/board/external effects of the stopped turn reconciled; worktree HEAD preserved.
4. **Steers:** pending steering reconciled, not forgotten or duplicated.
5. **Successor:** any replacement appointment named with its own status — or explicitly none.
6. **Review:** independent check recorded (basis + evidence refs), originals preserved;
   release archives the hold without deleting original evidence.

## Prohibitions

- **No blind replay:** a new appointment is a new investigator with new independent
  instructions — never re-run the failed prompt/tools.
- **No auto-clear:** never release a hold because an agent is merely alive, a timer
  elapsed, or two checks are green. If evidence cannot support safe resumption, retain
  the hold with named owner and next action.

## Escalation

If the Executive cannot act (legally restricted step, uncertain irreversible effects,
or conflict of interest — e.g. the Executive repairing itself):
- legally restricted steps → competent office via **Clerk**;
- uncertain irreversible effects → independent **Judiciary** review;
- otherwise → a duly authorised separate **Executive investigator** with fresh instructions.
Record the escalation durably with the hold; the hold stays blocking until resolved.

## Explicit non-claim

This roster asserts **no past hold cleared** and no live hold resolved. Live
`liveness/unsafe-holds/` was empty at last check (per Judiciary disposition §5);
the first real firing will exercise this procedure end-to-end.
