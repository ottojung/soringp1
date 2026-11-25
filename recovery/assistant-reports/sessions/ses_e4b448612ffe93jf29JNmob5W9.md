# antonina-WlUqXbyNGwBjDnp1L1OiK2-instinct

Session: ses_e4b448612ffe93jf29JNmob5W9
Workspace: /home/lubko/soring-fronts/exec-act19-prepared-provenance-20261107
Created: 1794033547762; updated: 1794033625573

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b4bb7a0d001aXAZHnZQsjBcXX)

I’ll inspect the current diff and relevant lock/recovery code read-only, compute its hash independently, then run the requested focused checks without touching protected records or creating commits.

## Output 43 (msg_1b4bbe820001w7dirHnGr3aYIB)

The focused integration passes, but the lock-token design has a critical shell semantic issue: command substitution runs the script in a subshell, so its `$$` is not a reliable identity for the supervising shell’s lock PID. I’m checking the actual runtime values and broader registry consumers/tests before finalizing the audit.

## Output 73 (msg_1b4bc76ff001EwsRc4MphtxwDD)

**Not approved.** Exact current diff hash (`git diff --binary | sha256sum`): `29d36f6b0c048af1642491ed8b7472aee40c8f7f0c797ec8203a12e0edde0622`.

The focused tests pass, but concrete defects remain:

- **Normal replacement recovery is broken after a crash at the registry commit point.** `appointments.sh` (`government/appointments.sh:208–228`) atomically swaps the registry before writing provenance or printing the new ID. If interrupted after the swap, the supervisor’s command substitution fails at `branch-bootstrap.sh:255`, leaving `reset-pending`; retry enters recovery (`:115–160`), which accepts only a matching prepared/committed intent or provenance. The normal replacement path creates a prepared intent only when it reuses an existing intent (`appointments.sh:155–201`); otherwise it never persists one. Thus the normal generated-successor path can leave a committed registry row with no durable matching transaction evidence, permanently blocking recovery. The recovery fixture supplies provenance manually and does not exercise this normal crash boundary.

- **A mismatched row can pass transaction binding.** Recovery counts rows at `:133`, then independently reads the third field at `:138`; normal validation similarly counts rows, then separately reads successor and transaction (`:256–259`). Neither verifies each selected row has exactly the expected field count. Duplicate-key rows with a matching successor/transaction plus another conflicting row can satisfy these checks. Validate the unique full row, including its field count and all relevant values, atomically.

- **The normal contention test does not prove the competing writer actually waited.** The background subshell writes `writer-started` before starting `appointments.sh` (`tests/appointment-recovery-integration-smoke.sh:405–409`). The test observes the lock and unchanged registry, but not that the writer reached lock acquisition or remained blocked. It also does not assert the writer’s exit status (`:417–424`), so it can pass without proving the intended competing-writer transaction outcome.

- **Stale-lock handling is inconsistent.** Ordinary reset refuses to steal an ambiguous/stale appointment lock (`branch-bootstrap.sh:233–243`), but interrupted recovery waits without inspecting or recovering stale locks (`:124–127`), so a crash while holding that lock can strand recovery indefinitely. `appointments.sh` likewise has no stale-lock policy (`appointments.sh:60–67`). PID-file removal followed by `rmdir` is ordered correctly in the traps, and borrowed-lock cleanup does not release the supervisor lock. However, owner validation (`appointments.sh:50–58`) is only a PID-file/live-PID check, not a race-proof ownership token.

`dash -c` confirmed command-substitution `$$` matched the parent shell in this environment; that point alone is not a demonstrated defect here. **Checks passed:** `/bin/sh` and `dash` syntax, `git diff --check`, appointments smoke, Act 19 continuity, continuity incidents, and recovery integration under both `/bin/sh` and `dash`. No files were edited.
