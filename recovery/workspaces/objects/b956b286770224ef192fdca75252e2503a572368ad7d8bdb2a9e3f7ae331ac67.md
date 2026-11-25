# Janitor Office — growth attribution addendum (2026-10-17)

Follow-up to `records/JANITOR-OPERATIONAL-REPORT-2026-10-17.md` (finding: disk +4.40 GB/day). This addendum attributes the growth.

## Method

- `find /workspace /home/lubko /var/lib/lubko /tmp -xdev -type f -mtime -1 -size +50M` (largest files modified in the last day), plus `du` of the top-level directories.
- The office's new `growth.tsv` (per-path deltas between successive inventories).

## Findings

Largest recently-modified files (last 24 h, > 50 MB):

| Size | mtime | path | nature |
|---|---|---|---|
| 504 MB | 10-16 20:17 | `/tmp/opencode/soring301/repo/.lake/packages/mathlib/.git/...pack` | Mathlib clone for the SoringP1 Lean build (transient) |
| 157 MB | 10-17 05:34 | `/home/lubko/.local/share/opencode/log/opencode.log` | agent-runtime log, **actively growing** |
| 118 MB | 10-16 20:17 | `/tmp/opencode/soring301/repo/.lake/packages/mathlib/.lake/build/bin/cache` | Lean build cache (transient) |
| 95 MB | 10-16 20:17 | `.../batteries/.lake/build.barrel` | Lean build cache (transient) |
| 53 MB | 10-17 02:41 | `/tmp/opencode/ap1-verify/.git/...pack` | verification clone (transient) |

Directory sizes: `/home/lubko/.local/share/opencode` = 17 GB, of which `opencode.db` = 14 GB **static** (last written 10-15 05:07), `snapshot` 582 MB, `log` 158 MB, `opencode.db-wal` 138 MB. `/var/lib/lubko/wd` 1.1 GB.

## Conclusion

The measured growth is dominated by **transient agent/build artifacts** — Lean/Mathlib build caches under `/tmp/opencode/*/.lake`, verification clones, and the agent-runtime log — not by a runaway leak. The 2026-10-16T20:00–01:20 step coincides with the SoringP1 Mathlib clone + build.

Actionable observations (report-only; not deleted):
1. `/home/lubko/.local/share/opencode/log/opencode.log` grows without bound (158 MB and rising). It is a **live file of the agent runtime** (Act 12.5 protects live files), so the office reports it rather than rotating it; the runtime/host owns rotation.
2. Aged Lean build caches under `/tmp/opencode/*/.lake` are large and, once their owning work is merged, reclaimable candidates. The office's inventory currently scans `/tmp/opencode` only at depth 1, so these nested caches are not yet visible to `classify`; extending the scan depth (or adding a targeted build-cache rule) is the next useful improvement.
3. `opencode.db` (14 GB) is static and shared-host; report only.

Net: no destructive action taken; the office now attributes growth and distinguishes transient build activity from persistent state.
