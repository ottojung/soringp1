# Executive continuity reconciliation — `continuity_unverified_executive:1793894047`

**Office:** Executive liaison `c1a00002` (record custodian for this case).
**Prepared:** 2026-11-07. **Evidence cut:** 2026-11-07T23:30Z.
**Base:** canonical `main` @ `91a136e2e80810d8ee194d4a0ca60748903f0944`.
**Status:** evidence for independent fact-finding. **Not** a disposition, **not** a
case-state edit, **not** a closure claim.

This addresses the one missing observation the Judiciary named for this case
(`20261107T174953Z-…disposition.md`, Executive row: *inconclusive*; missing =
"independent reconciliation of successor work and all prior/successor external
effects"), and the Auditor's acceptance condition in
`records/tracking/AUDIT-ACT23-HISTORICAL-CONTINUITY-2026-11-07.md`
(Executive row).

## Stored state under examination (unchanged by this document)

`institutional-cases/continuity_unverified_executive.json`: `state=verified_closed`,
`first_seen=1793894047`, `verified_at=1793895531`, `observations=4`,
`clear_observations=2`, `closure_evidence=null`,
`verification="two successive deterministic health checks without signal"`.

Receipt `continuity/verified-executive.json` claims `verified_by=judiciary`,
`verification_scope=external_effect_reconciled`, and asserts the successor
"reports no repository changes or #301 post and clean Executive worktree at
captured HEAD 283d87b". `continuity/reconciliation-executive.json` remains
`state=awaiting_reconciliation`.

## Findings

### 1. Predecessor terminal evidence, re-inspected

Directory `appointments/terminal-evidence/FuqijEoHuDVrnHKqmZ0SZ6-readily/`:

- `event.json`: `state=failed`, `failure_class=backend_authentication_failed`,
  `transient=false`, `automatic_retry_safe=false`, `finished_at=1793893766.088`,
  `log_truncated=true`.
- `status.json`: `exit_code=1`, `exit_signal=null`, `cwd=/var/lib/lubko/wd/viche-seats/branches/executive`.
- `worktree-head.txt`: `283d87b9a9598976890dec861bfc753f8a899c87`.
- `log-tail.txt` is exactly **131072 bytes**, consistent with the recorded
  truncation; it is a tail, not the full record.
- `worktree-status.txt` is **0 bytes** and `worktree-error.txt` is **0 bytes**.
  Empty status with an empty error is *consistent with* a clean worktree at
  capture, but it is an inference from file emptiness, not a recorded status
  string, and is stated as such.

### 2. The successor also failed — and the receipt does not say so

`antonina agent status --id 2Sfwsd7B96EjLCCGs2ohOp-quilt`:

- `state=failed`, `alive=false`, `exit_code=null`
- `cwd=/var/lib/lubko/wd/viche-seats/branches/executive`
- `started_at=1793928406.175`, `finished_at=1793928561.337` (≈155 s)

So the agent on whose "durable output" the verification rests did not complete
successfully. The receipt's phrase "reports no repository changes" is true only
in the narrow sense that the successor made no commit in its own worktree; it is
not evidence of a successful handoff.

### 3. A successor external effect the receipt omits

The successor's own durable output log
(`/home/lubko/.local/state/antonina/agents/2Sfwsd7B96EjLCCGs2ohOp-quilt/output.log`,
37,137,405 bytes) records, as its final actions:

- `1793928533.635` — it created an idle agent
  `OQakXIj6uP9oNpdG7Y9tAT-dressers` ("Act 19: re-review transaction-bound hold
  recovery") with `--cwd /var/lib/lubko/wd/viche-seats/branches/executive-act19-reset-hold-clean`;
- `1793928542.048` — it dispatched that agent with a read-only Act 19 review
  prompt;
- `1793928561.354` — that dispatched agent **also failed** (`exit_code=null`,
  ~19 s lifetime).

This is a concrete external effect by the successor that
`verified-executive.json` does not mention: the successor did not merely observe
a clean tree, it started further work and then died with that work in flight.

### 4. Where that work ended up

`/var/lib/lubko/wd/viche-seats/branches/executive-act19-reset-hold-clean`:

- HEAD `756aef4a8267702b030340c52501a578b977048a`
- **14 modified paths**, uncommitted, including `government/branch-bootstrap.sh`,
  `government/institutional-cases.py` and several test scripts.

That is unreviewed, uncommitted work left by the failed chain. It is not a
"no repository changes" outcome, and it is not in `main`.

### 5. The preserved HEAD is outside `main`

The predecessor's captured head `283d87b` ("Preserve uncommitted worktree state
recovered after terminal failure of 8y4kX76sfXDBhayj4a3Q8y-rangers … contents
not yet reviewed or enacted"):

- is **not an ancestor** of canonical `main` @ `91a136e`;
- is contained in **no** local or remote branch (`git branch -a --contains` is
  empty; the worktree holds it detached);
- touches 47 files (2,481 insertions, 1,010 deletions), including summons
  records and many test scripts.

So the Executive worktree has sat on an unreviewed, unmerged preservation commit
since 2026-11-05.

## Conclusion

The stored `verified_closed` for this case is **not substantiated** by
independent successor evidence:

1. the successor failed rather than completing;
2. the chain produced an additional external effect (a dispatched agent) that
   also failed;
3. that chain left 14 uncommitted, unreviewed modifications; and
4. the preserved HEAD is unreviewed and unreachable from `main`.

Consistent with the tracker's gate ("Do not infer ongoing operational failure or
recovery from stored state alone"), this establishes **neither recovery nor
persistent outage**. It establishes that the closure rests on a failed successor
and that unreviewed work exists in a preserved worktree.

## What this document does not do

No case object, index, receipt, or canonical checkout was modified. This is not
a reconciliation of live state, not a Judiciary verdict, and not an Auditor
certification. Per the Clerk's refresh, the case must not be reconciled or
re-indexed until a case-specific Judiciary disposition authorises it, and any
such reconciliation must preserve the original object and closure timestamps and
publish before/after artifacts.

**Independent verifier:** Judiciary fact-finding, then Auditor `c1a0000b` against
the exact resulting state.

**Re-runnable references:**
`appointments/terminal-evidence/FuqijEoHuDVrnHKqmZ0SZ6-readily/`;
`antonina agent status --id 2Sfwsd7B96EjLCCGs2ohOp-quilt`;
`antonina agent status --id OQakXIj6uP9oNpdG7Y9tAT-dressers`;
`git -C /var/lib/lubko/wd/viche-seats/branches/executive-act19-reset-hold-clean status --porcelain`;
`git -C /var/lib/lubko/wd/viche merge-base --is-ancestor 283d87b HEAD`.
