# Restart orphan reconciliation — Constitutional continuity

**Scope:** Ordinary government agent appointments; no edits to the
Founder-controlled constitution, bootstrap or S6 service definitions.

On 2026-10-24 at 01:25:34 UTC, Billy's container restarted. Antonina
reported the then-running Executive and Judiciary as `failed`, with
`last_error="runner/model process disappeared without a captured exit status"`,
no backend classification and no captured exit status. Government classified
the absence of a backend error as permanent, repeated that same warning each
three-minute cycle and could not resume either office. The Clerk had separately
failed *before* the restart with a backend error explicitly marked
`automatic_retry_safe=false`; it must never be treated as a safe automatic
retry.

**Independent Constitutional VIII continuity reconciliation:**

- A controller may replace a **dead appointment** from the previous
  container incarnation only when PID1's actual creation timestamp matches
  the agent's terminal timestamp, the invocation began before that PID1,
  the agent is terminal/not alive, both exit code and signal are absent,
  no backend error exists, and the precise process-disappearance message
  is recorded. If any field is unknown, absent, contradictory or outside
  the timestamp window, the incumbent is retained for explicit review.
- A pending steer or existing unsafe-hold blocks automatic succession.
  The previous invocation/session/prompt is **never replayed**. The fresh
  agent's ordinary office dispatch re-reads durable Git/Antonina state and
  applicable handoffs; it must independently reconcile uncertain partial
  work before taking consequential action.
- `appointments.sh` serializes the compare/replace under its existing
  registry lock, captures terminal evidence first (status, last log
  snapshot, worktree HEAD/status) and records the old/new identities
  in `restart-renewals.jsonl`. The prior agent and worktree are preserved.
- This is a new appointment for a vanished container process, **not**
  a model-error reset and not an exception to Act 19's three-transient-
  failures threshold. Unknown backend failures and explicit unsafe
  continuations continue to require existing Act 19 escalation and review.
  An absent classification is surfaced as **unclassified**, never called
  permanent without evidence.
- Repeated observations of one unsafe failure or permanent/unclassified
  incident are deduplicated; the original records remain durable. This
  prevents observation frequency from inflating failure counts or alerts.

**Operator restoration on October 24:** The Executive and Judiciary's
lost-through-restart agents were replaced after positive PID1 comparison.
The Clerk's explicit retry-unsafe failure was separately reviewed: the
worktree was clean, no pending steers or open handoffs remained, and the
new appointment was instructed through the ordinary independent intake
cycle, without reusing the previous prompt. Its historical unsafe-hold
observations were archived with a durable review receipt. These manual
reviews do **not** establish that all possible side effects of the earlier
interrupted processes are known.

**Review:** The Judiciary/Legislature should independently review the
interpretation that scheduled-incarnation appointment reconciliation is
distinct from Act 19 §3.1 transient-error recovery. If they disagree,
legislative clarification is needed. No legislation is enacted by this
engineering change.

Tests: `tests/appointments-smoke.sh` covers precise restart orphan
recognition, non-replay, evidence preservation, idempotence, unsafe holds,
old/new epoch mismatch, explicit backend errors and queued steers.
`tests/continuity-incidents-smoke.sh` covers idempotent incident
records and correct classification. Both are included in the full suite.
