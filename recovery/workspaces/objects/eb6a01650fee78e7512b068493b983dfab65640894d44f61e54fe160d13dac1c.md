# Act 17 audit-cycle finality guard

An **audit cycle** is the frozen randomized sample that the Judiciary
investigates. The ordinary audit dispatch refreshes the sample after its
six-hour cadence. Incident-driven checks can dispatch as frequently as every
30 minutes, but **reuse the current frozen draw** until it is six hours old.
They must NOT mint fresh per-case correction opportunities just because a
second session was launched. The actual draw is identified by its recorded
timestamp, random seed and case IDs; its stable, 32-hex cycle identity is
written to private oversight state.

Before dispatch, `audit-cycle.sh` persists that ID in
`current-audit-cycle` and in the append-only
`audit-cycle-identities.tsv` ledger. The controller accepts a
`--correction --cycle-id ID` only for the current ledger-backed token and
rejects any later correction for the **same case and same frozen sample**
even after its earlier correction has been confirmed. A per-case file lock
serializes reads and append/cache updates between concurrent CLI processes.
A missing, malformed or legacy correction identity fails closed without
backdating or silently assigning an invented cycle. Confirmation is a
procedural second pass, not independent verification. The monitoring check
reads **committed Git HEAD** for each cached correction and never treats an
untracked or modified working-tree correction log as legally effective. If
there is no valid committed confirmed correction, the original verdict stays
effective (where recoverable), and a distinct `correction_not_effective` or
`correction_anchor_invalid` signal exposes the mismatch. Old original evidence
references may be unavailable in legacy cache rows; the signal explicitly
marks them uncertain instead of manufacturing corroboration.

If the detached audit launch returns an error after token preparation, the
dispatch time remains recorded; an immediate retry is refused because the
backend may have started work despite reporting failure. A later dispatch
of the SAME frozen sample uses its original token. This ensures token
visibility before agent execution and preserves evidence of ambiguous
launches. Identity in private state is not independent evidence of delivery.

Tests: `tests/audit-cycle-identity-smoke.sh` checks incident reuse, fresh
samples and ambiguous launches; `tests/audit-correction-smoke.sh` checks
corrected/confirmed verdict semantics, tampered legacy trails and simultaneous
same-cycle correction attempts. The Act 21 full suite must pass on the exact
proposed merge before publication.

**Scope and legal limit:** This is a prospective conservative enforcement
of the existing Act 17 cap, not a legislative amendment and **not** a
retroactive adjudication of the two previously reported corrections from
the October 23 frozen draw. The original and proposed correction histories
remain preserved as non-operative historical evidence. The Legislature and
independent Judiciary must resolve their compliance and the old PR #32
through the separate originating board issue.
