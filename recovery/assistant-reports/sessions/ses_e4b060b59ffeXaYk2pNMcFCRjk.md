# antonina-9viPc81DeAZWzT6BH607XB-taint

Session: ses_e4b060b59ffeXaYk2pNMcFCRjk
Workspace: /home/lubko/soring-fronts/exec-act19-prepared-provenance-20261107
Created: 1794037642409; updated: 1794037673324

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 55 (msg_1b4fa3964001uC6ghaaNsQAh00)

**Finding: the reviewer’s specific signal-window concern is not a lock-theft defect.** In both Act 19 paths, cleanup is gated by `appointment_lock_held=yes`, and that flag is set only immediately after this process’s `mkdir "$appointment_lock"` succeeds. A signal before PID publication therefore triggers cleanup of a lock this process just claimed—not another writer’s lock.

- In recovery, the claim is at [`government/branch-bootstrap.sh:137`](government/branch-bootstrap.sh#L137), the flag at line 146, and PID publication at line 147. In normal reset, they are at lines 251, 263, and 264.
- The EXIT trap invokes `cleanup_locks` ([lines 49–58](government/branch-bootstrap.sh#L49-L58)); HUP/INT/TERM handlers exit, which runs that trap. If interrupted after the flag is set but before or during PID publication, removing the directory is safe: no other writer could have successfully acquired that still-existing directory. If PID publication fails without a signal, `set -e` likewise exits into the trap and cleans up the owned lock.
- There is a distinct tiny window between successful `mkdir` and setting the flag. A signal there can leave a lock without a PID. That is a **fail-closed stale-lock leak**, not early release or theft: competing writers reject ambiguous/missing-PID locks (normal reset: lines 251–260; recovery: lines 137–144). PID publication interrupted after creating a partial/empty file is similarly rejected as ambiguous.

This conclusion assumes the shared state directory is not being maliciously modified to replace the lock path between operations; the code does not defend against an adversary with write access to that directory. Under the normal cooperating-writer model, the reported interleaving does not falsify ownership safety.

**Bootstrap-lock cleanup is a separate ownership concern.** Its claim and PID write are at lines 34–48, but `cleanup_locks` unconditionally removes `$bootstrap_lock/pid` and attempts `rmdir` at lines 55–56—even if this invocation failed to acquire the bootstrap lock or was interrupted before reaching the trap installation at line 58. `rmdir` cannot remove a nonempty live lock, so this does not release the other writer’s lock. But `rm -f` can erase that writer’s PID, turning it into an ambiguous lock that future writers refuse to recover. This is a fail-closed **metadata-damage** risk, not lock theft. The comment at lines 38–42 explicitly intends not to remove another bootstrap lock, so cleanup should be gated on a bootstrap-owned flag set only after successful `mkdir`.

I recommend fixing and testing that bootstrap cleanup ownership issue if it is within the requested review scope. For the appointment-lock signal window itself, no fix is warranted; testing should distinguish the post-`mkdir`/pre-flag leakage case from the post-flag/pre-PID safe cleanup case. I have not independently audited the rest of the candidate or its signal test, and make no blanket approval claim.
