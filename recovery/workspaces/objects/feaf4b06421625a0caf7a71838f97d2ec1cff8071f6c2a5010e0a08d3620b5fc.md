# Janitor Office — first evidence-gated reclamation + safety fixes (2026-10-17)

Issues #298/#299. Authority: Act 12.4 (evidence standard), 12.5 (invariants), 12.7 (authorization gate). Commit `4f3ef5c` on `main`, deployed to the canonical town checkout.

## Evidence-gated decision (Act 12.4)

Of the 7 initial `quarantine-candidate`s, liveness/ownership checks distinguished:

| Artifact | size | age | unpushed | stash | dirty | live procs | decision |
|---|---|---|---|---|---|---|---|
| /workspace/phone-home | 530 MB | 40 d | 0 | 0 | 0 | none | **quarantine** |
| /workspace/lubko-issue33-impl | 126 MB | 62 d | 0 | 0 | 0 | none | **quarantine** |
| /workspace/rel-92 | 124 MB | 55 d | 0 | 0 | 0 | none | **quarantine** |
| /workspace/validate-136 | 124 MB | 55 d | 0 | 0 | 0 | none | **quarantine** |
| /workspace/rel-lifecycle | 126 MB | 54 d | **3** | 0 | 0 | none | retain (unique work) |
| /workspace/rel-76-fix | 126 MB | 54 d | **8** | 0 | 0 | none | retain (unique work) |
| /workspace/rel-tests | 126 MB | 54 d | **13** | 0 | 0 | none | retain (unique work) |

Only artifacts with no unique local work (all commits on a remote) and no live process were quarantined. The 4 were moved (reversible) to `viche-state/quarantine/` — du-verified 121/124/121/518 MB (~884 MB). `/workspace` entries removed; recovery preserved. `reclaim_enabled=0`, so no destruction.

## Safety bugs found and fixed

1. **Missing unpushed-commit detection.** `classify` treated any old clean git repo as reclaimable, ignoring unpushed commits. It now records the unpushed count and marks such repos `retain-unpushed`. This protected 11 repos, including `/workspace/assemblyp1` with **64 unpushed commits** — a heuristic sweep would have destroyed live work (failure modes J1/J3).
2. **`rotate()` clobbered the global `size`.** `log_append`→`rotate` overwrote `size`, so `quarantine` logged the log-file byte count (≈21 KB) instead of the artifact size. Fixed; hermetically verified.
3. **`classify` dropped the header.** Its output had no header, so `tail -n +2` then skipped the first data row in `quarantine` (a candidate could be missed). Fixed; header preserved.

All fixes: POSIX `/bin/sh`; `sh -n` PASS; `tests/janitor-smoke.sh` PASS; hermetic classify→quarantine test PASS (size logged 999999 correctly).

## Note on space accounting

`/workspace` and the quarantine dir are on the same filesystem (`/dev/nvme0n1p2`), so quarantine *stages* rather than frees space; actual freeing happens at `reclaim-quarantined` after the grace window (`quarantine_grace_seconds`, default 7 d). The `quarantined.tsv` size column for the first 4 moves shows the pre-fix buggy value; true sizes are the du values above.

## Next

After the grace window (or executive-set `reclaim_enabled=1` for these evidence-satisfying items per 12.7), run `reclaim-quarantined` and publish freed-bytes before/after.
