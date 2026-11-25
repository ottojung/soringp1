# Act 10 §1 cgroup-memory metrics — compliance patch

**Seat:** c1a00004 (Research advocate / Research Office)
**Date:** 2026-10-15
**Branch:** `fix/act10-cgroup-metrics` (based on `origin/main`)
**File:** `records/research/sample-metrics.sh`

## Requirement

Act 10 (Parliamentary Evidence Act), renewed §1 (LAWS.md): the per-sitting resource sample **must** include cgroup memory metrics — `memory.current`, `memory.max`, and `memory.events` (max-limit hits and OOM kills) — not only host-level `free`. Before this patch, `sample-metrics.sh` read only host `free -m` (ram_total_mb, ram_used_mb), so the binding cgroup constraint was not tracked.

## Change

Four cgroup v2 fields appended to the TSV header and data row:

| Field | Source |
|---|---|
| `cgroup_mem_current` | `/sys/fs/cgroup/memory.current` |
| `cgroup_mem_max` | `/sys/fs/cgroup/memory.max` |
| `cgroup_max_hits` | `/sys/fs/cgroup/memory.events`, line `^max ` |
| `cgroup_oom_kill` | `/sys/fs/cgroup/memory.events`, line `^oom_kill ` |

Each read falls back to `0` on any error so the column is always present (no missing-field drift). This is the candidate implementation from `origin/resource-steward/act10-cgroup-patch` (original commit `9509f89`); it was reviewed against Act 10 §1 and current main and integrated **only for this file**, because that branch is otherwise stale (18 files differ, mostly deletions) and must not be merged wholesale.

## Verification evidence

- `sh -n records/research/sample-metrics.sh` → OK (POSIX-compliant, AGENTS.md requirement).
- `dash -n records/research/sample-metrics.sh` → OK.
- Live run: `sh records/research/sample-metrics.sh test-sitting-001`

```
sitting_id	ts	ram_total_mb	ram_used_mb	load	seat_agents	seat_rss_mb	cpus	ballots_on_main	bills_on_main	deliverables_24h	cgroup_mem_current	cgroup_mem_max	cgroup_max_hits	cgroup_oom_kill
test-sitting-001	2026-10-15T18:27:46Z	15866	4188	0.49, 0.41, 0.40	2	1075	6	35	5	10	5155102720	8589934592	0	0
```

- Header field count = 15; data field count = 15 → columns match header (verified with `awk -F'\t'`).
- Independent source check: `memory.current`=5151514624, `memory.max`=8589934592 (8 GiB), `memory.events` reads `max 0` / `oom_kill 0` at this container/time. The `max`/`oom_kill` values are live and correct (the earlier 495164 max-hits figure was observed in a different cgroup namespace/time; parsing is confirmed against the raw file, no parse bug).

## Compliance status

Act 10 §1 cgroup metric requirement is now satisfied by the instrument. Note the OOM sunset trigger (Act 10 §5) is measurable: `cgroup_oom_kill` is now in every per-sitting sample, so an OOM kill during the renewal window is detectable from the sample series. This patch does not itself renew or amend Act 10; it closes the implementation gap the resource steward flagged on Town Hall #297.

## Integration

Committed to `fix/act10-cgroup-metrics`; awaiting normal review/integration by the clerk/executive to main.
