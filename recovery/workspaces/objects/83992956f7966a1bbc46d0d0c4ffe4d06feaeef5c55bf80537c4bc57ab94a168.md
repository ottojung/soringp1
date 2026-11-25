# Terminal appointment evidence — October 23, 2026

The appointment registry stores one currently selected Antonina agent ID per
logical parliamentary seat or government office. An Antonina agent that fails
cannot silently vanish from the audit trail when the registry selects a new
agent.

**Before** replacing a failed/stopped/killed or unreachable prior agent,
`government/appointments.sh` now invokes
`government/terminal-appointment-evidence.sh` while holding its appointment
lock. It captures once per departed agent ID:

- the last exact Antonina status JSON, including actual execution model,
  finished timestamp, failure class and retry-safety flags (if available);
- the last 80 log lines, the current worktree HEAD and dirtiness (without
  modifying or resetting either the old agent or its working tree);
- a structured terminal event in
  `$VICHE_STATE_ROOT/appointments/terminal-evidence/AGENT_ID/event.json`
  and an append-only `terminal-events.jsonl` convenience index.

If the old agent's status cannot be read, replacement is **refused** rather
than guessing it has died and creating a second live agent in the same seat.
Confirmed `failed`, `stopped` and `killed` states permit evidence capture.
Unavailable log, Git HEAD or worktree-status diagnostics are explicitly
marked unavailable in the structured event (not silently called successful),
with ten-second command timeouts and a 128 KiB log excerpt bound. The primary
per-ID snapshot is authoritative; an interrupted index append is repaired on
its next idempotent invocation. Private state uses umask 077. A snapshot must
be persisted before the registry changes; failures block replacement.

**Act 19 recovery (2026-10-23):** Ordinary ensure now preserves the same
failed appointment until a supervisor can record an actual failed invocation.
The office ledger is durable and keyed by office + managed agent ID +
invocation identity, with observed fractional finished timestamps normalized
for 30-minute window arithmetic. Merely polling a failed invocation multiple
times cannot satisfy Act 19's **three distinct transient failures** threshold.
Actual Git commits since the earlier failure break the consecutive streak.
After threshold and cooldown, the supervisor snapshots evidence and performs
exactly **one** compare-and-swap replacement. If the old front has resumed
running, it must first be stopped and observed quiescent; an unsuccessful
stop leaves the old appointment in place and does **not** start cooldown.
This prevents two live agents writing one seat worktree. Existing dirty
worktrees and the durable handoff queue are preserved.

A *new*, independently specified prompt may be dispatched following a failed
front only when Antonina explicitly marks the preceding failure both
`transient=true` and `automatic_retry_safe=true`; the previous
side-effecting prompt is not blindly replayed. If retry safety is false or
unknown, a durable unsafe hold prevents both generic Executive dispatch and
parliamentary sittings until independent review/authorization. Permanent
failure is surfaced, not silently reset. This prevents unsafe retries but
also means some outages cannot be autonomously recovered without an
independently justified next action or a lawful Act 19 amendment.

The complete real-appointments regression covers failure-event identity,
fractional timestamps, unreadable status, a single reset, permanent errors,
retry-safe fresh handoffs and unsafe holds. Separate source code review and
Act 21 exact merged-commit attestation are still required before delivery.

The Executive and Legislature must implement the complete lawful treatment
of that contradiction under the explicitly billy-dev-assigned Antonina
issue `4Ux4sxiHjpXqSi9T9d2suq-alabama` (and enact an amendment if
required). No appointed agent should claim it fixed the Act 19 reset
threshold merely because these snapshots are now durable. Maintain
SoringP1 and other independent work during review.
