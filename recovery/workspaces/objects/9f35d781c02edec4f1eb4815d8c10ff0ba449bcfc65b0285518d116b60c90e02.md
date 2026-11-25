# Janitor Office — retain live Lean/elAN toolchains (J2 safety fix)

Date: 2026-10-19. Issues #298/#299. Authority: Act 12 (Territorial Janitor Act,
esp. 12.5 invariants), sovereignty-review failure mode J2 (live build dependency).

## Problem

`classify()` flagged `/home/lubko/.elan` (3.0 GB, 30 days old, non-git) as a
`quarantine-candidate`. That directory is the **live Lean/elAN toolchain
installation**: it holds the pinned default toolchain
`leanprover/lean4:v4.3.4.0` for the actively-assigned SoringP1 project
(`/home/lubko/soring301/lean-toolchain` = `leanprover/lean4:v4.34.0`;
`.elan/settings.toml` `default_toolchain` = same). Quarantining it would break
the Lean build until elan re-downloads ~2.9 GB (failure mode J2). The
directory mtime ages after install, so the office's `age >= 30d` heuristic is
not an abandonment signal here.

## Fix

`government/janitor.sh` `classify()` now matches `*/.elan` (and the nested
`.elan/toolchains/*` paths) and classifies them `retain`, mirroring the
existing `.lake` liveness guard. The whole elan home (toolchains + elan binary
+ settings) is live build infrastructure and is retained regardless of age/size.

## Verification

- `sh -n` / `dash -n` PASS.
- `tests/janitor-smoke.sh`: new hermetic cases assert the top-level `.elan`,
  `.elan/toolchains`, and a nested toolchain dir all classify `retain` (not
  `quarantine-candidate`) even at 40 days / 2 GB. Full suite `tests/run-all.sh`
  green.
- Deployed to the canonical town checkout; live `classify` now reports
  `/home/lubko/.elan -> retain` and **zero** quarantine-candidates.

## Disk status (honest, 2026-10-19)

- `/dev/nvme0n1p2`: 84% used, ~36 GB free, level=ok (warn 85%).
- Growth is transient agent/build state under `/home/lubko/.local` (opencode
  runtime); the 2026-10-16 step was the SoringP1 Mathlib clone+build.
- 4 items (~883 MB) staged in quarantine; `reclaim_enabled=1`; auto-reclaim
  after the 7-day grace (post-2026-10-24).
- The 3 GB `.elan` toolchain is retained deliberately (live build dependency),
  not reclaimed.
