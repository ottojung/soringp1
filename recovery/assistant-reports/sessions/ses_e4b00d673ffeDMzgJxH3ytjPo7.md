# antonina-lzHvdCxdYtkN8H6R9kFh9n-mahogany

Session: ses_e4b00d673ffeDMzgJxH3ytjPo7
Workspace: /home/lubko/soring-fronts/exec-act19-prepared-provenance-20261107
Created: 1794037983631; updated: 1794038097019

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b4ff29ad00110GEL1CR0XoevJ)

I’ll keep this strictly read-only and capture the requested snapshot identity before inspection and again at the end. I’ll run only the named targeted tests, avoiding broad wildcard sweeps.

## Output 44 (msg_1b4ff6166001LoglMa2Hr6Mj0P)

The guard is asymmetric: bootstrap cleanup checks the recorded PID before removing its own lock; appointment-lock cleanup removes the PID and directory based only on a local “held” flag. I’m checking whether cooperating writers can make that unsafe, and validating the signal test’s actual targeted process and assertions.

## Output 90 (msg_1b50089d1001fvbeNO3404cSWi)

All four targeted tests passed under both `/bin/sh` and `dash`; the office-continuity test emits expected fixture inventory warnings but exits successfully. The signal test sends TERM/HUP to the `setsid` child PID, which execs the appointments shell in place, then asserts lock removal, unchanged registry, expected exit code, and successful retry. I’m recording the ending hashes now.

## Output 99 (msg_1b500a295001l4i4rNH7mqCbav)

## Decision: **No-approve for the exact snapshot**

The snapshot identity changed during the review: HEAD remained constant, but both requested content hashes changed. Per your instruction, I cannot approve this as an exact-snapshot review. I did not edit files or create artifacts.

### Snapshot identity

| | Start | End |
|---|---|---|
| `git rev-parse HEAD` | `756aef4a8267702b030340c52501a578b977048a` | `756aef4a8267702b030340c52501a578b977048a` |
| `git diff --binary \| sha256sum` | `3a8c6542d8ca295a0ab61b1b1c0eb88b8fc7b9178ddb4c825b1b9d5a2f61bef0` | `780b21c9e6d20cc4540138f1bc44e88203dcf1698d0c05a8f94d0b4dc6cf5a83` |
| `sha256sum tests/act19-signal-trap-smoke.sh` | `b30d470c83cdb3213a7a0e646033450f46aa59d3482d43ebe81077e3bde70f8f` | `3913dbd7d5e7694b6a23d210bb06108ba85509259bacf12ec0907481a32ad5bd` |

### Findings

- **Cooperating-writer lock cleanup:** `appointments.sh` removes its lock only when the PID in the lock still equals its own PID. Bootstrap’s `cleanup_locks` does **not** check the appointment-lock PID; it removes the PID file and attempts `rmdir` based on `appointment_lock_held=yes`. Under the cooperating-writer model, the directory cannot be acquired by another writer while the owner holds it, and normal cleanup occurs before another writer can acquire it. Thus this is **not lock theft under cooperating writers**. It is nevertheless a weaker ownership guard than the bootstrap-lock cleanup, and could remove another process’s PID file if the lock were replaced or ownership otherwise changed outside that model.
- **Stale-lock/liveness:** acquisition treats a PID-less/malformed lock as ambiguous, and a dead recorded PID as stale; it refuses takeover rather than stealing the lock. That is a stale-lock/liveness failure mode, distinct from lock theft. PID reuse can make a dead owner appear live and cause a busy timeout; it does not make the contender take the lock.
- **Signal test:** `setsid env … "$sh" appointments.sh … &` is followed by signaling `$!`. The shell script is the launched process (the `env`/shell exec chain does not leave a separate process-group target); the signal is sent to that PID, not the group or gate sleep. The test checks expected TERM/HUP exit status, lock removal, unchanged registry, and a successful retry. Those assertions execute for both shells and both signals.
- **Recovery/transaction:** reviewed registry atomic swap as commit point; prepared intent is written before swap; matching successor/transaction is required for recovery; manifest binds the archive rows to the reset transaction; the marker is removed only after archive/recovery bookkeeping. The integration test exercises pre-swap refusal, post-swap crash recovery, mismatched transaction rejection, archive retry, and lock contention.

### Commands and results

Ran each test under both `/bin/sh` and `dash`; **all passed**:

```text
tests/appointment-recovery-integration-smoke.sh
tests/appointments-smoke.sh
tests/act19-office-continuity-smoke.sh
tests/act19-signal-trap-smoke.sh
```

The office-continuity smoke emitted fixture `delivery-inventory` warnings about the temporary town not being a Git repository, but completed successfully.

Also passed syntax checks for both shells on the two government scripts and four named test scripts, and `git diff --check`. No wildcard sweep or full-suite claim.
