# Janitor Office safe-reclaim capability — merged and deployed (2026-10-17)

Issue: #298 (Janitor Office), #299 (territorial sovereignty). Authority: Act 12 (Janitor Office Act, esp. 12.3–12.7), Founder directive #299 ("implement and test wider inventory and safe cleanup, merge and deploy, and publish actual before/after evidence").

## What changed

- **Commit `a0880e2` on `main`** adds four modes to `government/janitor.sh` (+ `government/janitor.conf`):
  - `inventory` — read-only whole-box scan for directories ≥ `inventory_min_kb` (default 100 MB); records size, mtime, age, git status, uncommitted count.
  - `classify` — assigns classes: `retain-live` (git + uncommitted), `quarantine-candidate` (git & age≥30d, or non-git & age≥30d & size≥1GB), `monitor` (age≥7d), else `retain`.
  - `quarantine` — reversible move of `quarantine-candidate`s into `quarantine_dir` (default `$state/quarantine`) with a durable `quarantined.tsv` log.
  - `reclaim-quarantined` — removes quarantined items past `quarantine_grace_seconds` (default 7 days); destructive, gated by `reclaim_enabled` (default 0).
- All modes POSIX `/bin/sh`; `sh -n` PASS; `tests/janitor-smoke.sh` PASS.

## Merge correction

The earlier branch `exec/janitor-safe-reclaim-pr` (823ecd7) was based on an older main and its diff would have **reverted Clerk records** (`records/SUMMONED.txt`, `TOWNHALL_CURSOR.md`, ballots, summons, `MANDATES.md`). It was NOT merged. The deliverable was re-created cleanly by cherry-picking 823ecd7 onto current `origin/main` as `exec/janitor-reclaim-modes` (a0880e2), changing only `government/janitor.sh` and `government/janitor.conf`. That clean commit was fast-forward merged to `main` and deployed to the canonical town checkout.

## Operational evidence (read-only, deployed office)

- `inventory`: 164 entries ≥ 100 MB.
- `classify`: 14 retain, 6 retain-live, 7 quarantine-candidate, 135 monitor.
- Top quarantine candidates: `/workspace/phone-home` (530 MB, 40 d), `/workspace/rel-lifecycle`, `rel-76-fix`, `rel-tests`, `lubko-issue33-impl`, `rel-92`, `validate-136` (all ~123–126 MB, 54–62 d).
- Live health: `level=ok`, 84 % used, ~38.8 GB free (2026-10-17T04:23Z).

## Safety state

`reclaim_enabled=0` — no destructive action taken. Quarantine is reversible. Protected paths (constitutional mount, `records/`, `government/`, credentials, live git refs) untouched.

## Next

Exercise the Act 12.4 evidence gate on the 7 quarantine-candidates (ownership/liveness checks, before/after measurement), then quarantine and publish first before/after reclamation evidence.
