# antonina-3MboDSvyJMG9SajjWqVLwo-piti

Session: ses_e4b45b53bffeYX8iGWWLi3P094
Workspace: /home/lubko/soring-fronts/exec-act19-prepared-provenance-20261107
Created: 1794033470152; updated: 1794033543437

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 55 (msg_1b4bb345c001aO9nKK2tuZcdz9)

## Review result: **No approval**

I recorded the requested initial values before inspection:

- **Base HEAD:** `756aef4a8267702b030340c52501a578b977048a`
- **Initial `git diff --binary | sha256sum`:** `29d36f6b0c048af1642491ed8b7472aee40c8f7f0c797ec8203a12e0edde0622`

### Concrete finding: ordinary replacement can strand an appointment lock

In `government/appointments.sh`, the normal lock-acquisition path creates `appointments/lock` and writes its PID at lines 61–67, but its cleanup trap only runs for the script process. The script then calls external commands including agent creation/status, evidence preservation, policy sync, and registry writes. If the shell is interrupted or one of those commands fails after the lock is acquired, the trap removes the lock; however, a hard termination or host/process failure can leave a lock directory with a stale PID.

Act 19’s normal reset path and recovery path treat an existing appointment lock differently: normal reset refuses an ambiguous/stale lock, while recovery waits without stale-lock detection. A stale lock can therefore block recovery until timeout, and there is no shared stale-lock reclamation protocol. This is a liveness gap; I found no lock-order deadlock in the reviewed paths because bootstrap acquires its own lock before the appointment lock, and appointment writers do not acquire the bootstrap lock.

The owner-token check is constrained to a matching live PID recorded in the lock, but PID reuse is not distinguishable from the original owner. Its safety depends on the lock remaining private and the recorded PID being trustworthy; it is not a strong process-identity token.

### Coverage and verification

The focused integration and office-continuity tests passed under both shells:

- `/bin/sh tests/appointment-recovery-integration-smoke.sh` — passed
- `dash tests/appointment-recovery-integration-smoke.sh` — passed
- `/bin/sh tests/act19-office-continuity-smoke.sh` — passed
- `dash tests/act19-office-continuity-smoke.sh` — passed
- `sh -n` and `dash -n` on the two changed government scripts and focused tests — passed
- `git diff --check` — passed

The office-continuity smoke emitted expected fixture diagnostics about unavailable Git inventory in its temporary town directories; it still passed.

The tests exercise replacement and injected failures around registry/provenance updates, and the integration test covers reset/recovery. They do **not** independently establish ordinary replacement cleanup under a real interruption while holding the lock, nor stale-lock recovery behavior. I did not run the full suite, so I make no full-suite claim. The protected ballot mismatch is treated as known and was not edited.

### Trust boundary and scope

This was a read-only review of the current worktree diff. I did not edit files, create artifacts, commit, or post to boards. The review concerns the candidate diff against the stated base; the manifest checks provide transaction-bound consistency against accidental corruption, not protection against an actor able to rewrite both archive and manifest.
