# antonina-MWn0LxxhMPyUmR4gJj2UXW-evacuated

Session: ses_e4b35f4a2ffep3lGtMWGIS47GE
Workspace: /home/lubko/soring-fronts/exec-act19-prepared-provenance-20261107
Created: 1794034502495; updated: 1794034591171

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b4ca0b79001tLwMBy38GkBjGR)

I’ll independently inspect the candidate and test changes without modifying the worktree, compute the exact diff hash, then run only the requested focused verification commands.

## Output 36 (msg_1b4ca41d9001bpxM2a2nHS7PaK)

The registry reader currently validates rows only for the requested key, and permits both legacy two-field and transaction three-field rows. I’m checking how that interacts with recovery’s exact-three-field assumption and the test fixture/runtime behavior now.

## Output 80 (msg_1b4cb4610001ZQBH1B7PaVgDVm)

**Not approved.** The independently computed exact diff hash is `95a6c49973568389d15ad1eaf6967ad046e1eb380ef5ff05cc0b54be74c279e9`.

The focused tests pass, but the snapshot still has proof gaps:

- `government/appointments.sh:74` validates field count and uniqueness only for the requested key. Other rows can be malformed or duplicated, yet replacement rewrites and preserves them. This does not establish exact, unique full-registry row validity.
- `government/branch-bootstrap.sh:119–122, 253–259` accepts a matching **prepared** intent as evidence of commit. The prepared intent is written before the registry swap; a crash before the swap leaves it behind. Recovery must require the registry’s transaction-bound successor and distinguish an actually committed swap from a pre-swap prepared intent.
- In stale appointment-lock recovery (`government/branch-bootstrap.sh:90–98`), a lock with a malformed or missing PID is retried until timeout rather than immediately failing closed. The wait is bounded, but does not meet the stated fail-closed stale-lock requirement.

The corrected post-swap crash fixture does check that the registry successor and transaction match the prepared intent, and exercises recovery after that boundary. However, it does not test the **pre-swap crash** case that exposes the prepared-intent ambiguity. The normal competing-writer test now signals that it reached the lock-attempt loop and asserts eventual replacement success; that evidence is adequate.

Verification passed: `/bin/sh` and dash syntax checks; recovery integration and appointments smoke under both shells; office continuity under both shells; `git diff --check`. I did not rerun the full suite or touch protected records.
