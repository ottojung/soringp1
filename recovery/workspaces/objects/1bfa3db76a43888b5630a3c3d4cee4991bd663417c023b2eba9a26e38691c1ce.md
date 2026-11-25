# Janitor Office reform: whole-box coverage, liveness gate, territorial accounting

Issues #298/#299. Authority: Act 12 (Janitor Office Act, enacted 2026-10-15):
12.2 (jurisdiction over the entire box), 12.4(d) (recorded liveness/ownership
check before any reclamation), 12.12 (prevention reporting). Branch
`exec/janitor-box-coverage-liveness`; tests: `tests/janitor-smoke.sh` (extended
with liveness-gate regressions), full suite green.

## Gaps found (measured 2026-10-20T01:26Z, device /dev/nvme0n1p2, 233 GB)

1. **Inventory coverage was partial.** Roots scanned: `/workspace /home/lubko
   /var/lib/lubko/wd /tmp/opencode`. Missed: `/tmp` (bind-mounted writable
   territory, ~5.7 GB, previously invisible) and `/gnu` (host-managed Guix
   store, 37.2 GB, read-only). Individual **large files were invisible**: the
   office inventoried directories only, so 582 transient runtime-scratch files
   (`/tmp/.bcf*`, ~5.4 MB each, 3.17 GB total and accumulating, created by the
   opencode/node agent runtime) were entirely unmeasured until this reform.
2. **No liveness gate before quarantine classification (12.4(d)).** The 2026-10-20
   emergency record (94%→87%) established that the office must detect liveness
   via `/proc/*/cwd`, not the Antonina registry, before build-cache
   reclamation. `classify` still classified purely on age/size.
3. **No territorial accounting.** The device is shared (host system, Guix
   store, other containers); the office could not attribute usage between
   box-visible and outside-box consumption.

## Changes (government/janitor.sh, POSIX /bin/sh)

- **Inventory roots** now cover the writable box territory (`/workspace`,
  `/home/lubko`, `/var/lib/lubko/wd`, `/tmp`, `/gnu`); the directory du timeout
  raised 10s→60s (the 10 s bound silently skipped the largest trees).
- **Large-file inventory**: depth-1 files ≥ `inventory_min_kb` at the roots are
  recorded as rows and flow through classification like directories.
- **Scratch-batch accounting**: `/tmp/.bcf*` (hardcoded observed pattern,
  comment-documented) is counted, sized, age-checked, and liveness-probed in
  one `/proc` pass each inventory; written to `janitor/scratch.tsv` and logged.
  Verdicts: `small` / `accumulating` / `live` / `quarantine-eligible`.
- **Liveness gate (new `path_in_use`)**: for every quarantine-candidate (and,
  for `.lake` candidates, additionally the parent worktree), the office checks
  `/proc/*/cwd`, `/proc/*/root`, `/proc/*/maps`, `/proc/*/fd`, and
  `/proc/mounts` for references. Referenced → `retain-live`; the check result
  is written to `actions.log` (`liveness-gate … result=in-use|clear`), the
  12.4(d) evidence record. Applies to quarantine classification; reclamation
  paths unchanged.
- **Host-managed classification**: `/gnu*` → `retain-host-managed` (observed
  for accounting only, never reclaimed).
- **Territorial accounting**: `janitor/territorial.tsv` attributes device usage
  to box-visible inventoried rows vs outside-box residual (host/other);
  logged per inventory and shown in `report`.
- **New `scratch-quarantine` mode**: stages aged, unreferenced `/tmp/.bcf*`
  files into the quarantine area (reversible `mv`, never direct deletion), where
  the existing grace window + `reclaim-quarantined` pipeline completes the job.

## Measured results (2026-10-20T01:26Z inventory)

- Device: 200.7 GB used (86%); **box-visible 162.9 GB, outside-box 37.8 GB**.
- Inventory: 187 entries; classes: 156 monitor, 15 retain, 11
  retain-unpushed, 3 retain-live, 1 retain-host-managed, 0
  quarantine-candidate (nothing currently meets the parliament-set
  age/size thresholds).
- Scratch batch: 582 files, 3.17 GB, `verdict=accumulating` (newest age 0 d,
  below the 1-day `min_reclaim_age_seconds` gate; live-referenced files are
  excluded from staging). Eligible for `scratch-quarantine` once aged; grace
  then applies before any destructive reclaim (`reclaim_enabled=1` since
  2026-10-17 executive gate, Act 12.7).
- Top growers (19 h): `/home/lubko/.local` +1.48 GB (opencode runtime:
  `opencode.db` 14 GB session store — flagged below), `/home/lubko/.cache`
  +0.79 GB (puppeteer 1.3 GB, mathlib 449 MB shared cache, uv 407 MB).

## Prevention findings (Act 12.12, no unilateral action taken)

- **`opencode.db` 14 GB** (`/home/lubko/.local/share/opencode/`) is the
  single largest box consumer and the fastest grower. It is live agent-runtime
  state (constitutional continuity, §VIII): classified retain-live. Runtime
  retention/pruning belongs to the opencode runtime, not the office; escalated
  here as the principal prevention item.
- **`/tmp/.bcf*` scratch** (3.17 GB and growing with agent activity) is
  runtime bytecode scratch that node does not clean on exit. The office now
  measures it and can stage it reversibly once aged. If agent parallelism
  sustains this rate, consider runtime-level scratch cleanup as a
  recommendation to the Founder.
- `/home/lubko/.cache/puppeteer` 1.3 GB (browser binaries) and `.npm` 1.7 GB are
  regenerable tool caches; retained under existing policy.

## Tests

- `tests/janitor-smoke.sh`: extended with three regressions — live-process
  quarantine-candidate → `retain-live` + logged gate; aged `.lake` with live
  parent worktree → `retain-live`; dead parent → still `quarantine-candidate`
  (the gate retains, it does not loosen classification). All green.
- Full suite (`tests/run-all.sh`): all Viche tests passed.

## Honest limitations

- Scratch reclamation is deliberately slow: age ≥ 1 day, then 7-day quarantine
  grace, then destructive reclaim. The batch will first become eligible
  ~2026-10-20T18:00Z.
- The liveness gate covers process references and mounts; it cannot certify
  that an *unreferenced* regenerable cache is logically unneeded (that remains
  the 12.4 evidence standard for the executive/Founder).
- Outside-box usage (37.8 GB) is reported, not managed: it is host territory
  outside the box's visibility (Act 12.5 invariants).
