# antonina-ADlOCS9ToOrO6vPdGuHVtz-circle

Session: ses_e4b508ab8ffeiwHKgx4L6z3lfl
Workspace: /home/lubko/soring-fronts/exec-act19-prepared-provenance-20261107
Created: 1794032760138; updated: 1794032816680

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 69 (msg_1b4b02afa001Dom37cGJrNcrfE)

**Review result: not approved.** Pending-reset recovery now holds the appointments lock through registry validation, archive work, and marker removal. The **normal threshold-reset path still races**: it calls `appointments.sh replace`, which releases its lock on return, then reads the registry transaction and performs archive and pending-marker cleanup without reacquiring that lock.

**Race interleaving:** reset A replaces the old appointee; `appointments.sh` releases the lock. Writer B replaces A’s successor and updates the registry transaction. A then reads B’s transaction and archives/removes the old appointee’s hold and pending marker as if its own replacement were still current. The pending marker’s old ID does not bind cleanup to A’s transaction.

**Minimal repair:** acquire the shared appointments lock before invoking `replace` in the threshold path, keep it held while reading and verifying the exact successor/transaction and doing archive, recovery-log, and pending-marker mutations, then release it. Since `appointments.sh replace` itself acquires that lock, it must support a safe already-held-lock protocol (or the supervisor must use a lock-aware helper); simply taking the lock around the existing call deadlocks. Keep bootstrap→appointments lock ordering consistent with pending recovery.

Verified:
- Shared lock: `appointments.sh` uses `mkdir "$root/lock"`, waits up to 20 attempts, and traps lock removal; pending recovery acquires that same lock and releases it on exit/signals.
- Recovery rejects missing/mismatched registry transaction and tests competing-writer contention. The transaction is stored in the replacement registry row and checked against intent/provenance; the archive manifest binds appointee and transaction to exact rows.
- Legacy two-column registry rows remain readable, but cannot satisfy recovery’s nonempty transaction match. Archive readers/tests still use the existing row format.
- `/bin/sh` and `dash` focused appointment-recovery, appointments, and Act19 continuity tests passed; syntax checks and `git diff --check` passed. Continuity smoke emitted expected fixture inventory warnings but passed.
- No files edited.

SHA-256 of `government/branch-bootstrap.sh`: `1d5b1f170f6a08a791398999355c159887b4e9400520af36884b0ef634218011`. The reviewed tree contains additional modified files; their per-file hashes were also recorded during review.
