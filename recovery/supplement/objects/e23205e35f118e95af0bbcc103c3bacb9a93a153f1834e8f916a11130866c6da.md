# SoringP1 (#301) research-pool oversight mechanism

Date: 2026-10-19. Issue #301 (assigned to phoebe-dev). Authority: Acts 2 and 6
(executive implementation/oversight). Constitution unchanged.

## Context

origin/main already carries the standing Executive duty for the SoringP1
research pool (`government/executive-agenda.md`, commit `54928ff`): "aim to
maintain **five concurrently active, independent, unary-focused SoringP1
research agents on phoebe-dev ... count the actual live SoringP1 agents through
Antonina, review their distinct research fronts, and commission or replace
useful agents toward the five-agent target ... This takes precedence over prior
ten-agent instructions." Act 19 (office continuity + handoff queue) is likewise
already deployed on main (`5490dbf`, `government/office-continuity.sh`).

## Authority note

A Founder-directed oversight request relayed via the executive dispatch asked
for **TEN** simultaneous agents. That is superseded: the newest SoringP1
AGENTS.md on main (`07596ca`) and the Executive agenda (`54928ff`) both bind
**FIVE**. The request's cited commit `0622741` is stale. This mechanism uses the
operative target (FIVE), overridable via `SORINGP1_TARGET`.

## Delivered

`government/soringp1-oversight.sh` — the measurement/coordination mechanism the
standing duty describes but did not yet mechanise (POSIX /bin/sh):

- **`report`** (read-only, default): counts live SoringP1 agents from
  `antonina agent list --running` (cwd under the SoringP1 worktree base),
  detects **duplicate titles** and **stale agents** (running, no activity
  > 30 min), and records a durable `status.json`. No mutation.
- **`replenish`**: launches **only** operator-curated scopes from
  `government/soringp1-scopes.tsv`, de-duplicated by title and bounded per pass.
  With no registry it does nothing — it never fabricates or duplicates research
  prompts, satisfying the request's own constraints.
- Invoked read-only from `government/boot.sh` each cycle (non-fatal), so it is
  persistent across the 24-hour restart with no host-side service and no
  ChatGPT scheduled task.

Tests: `tests/soringp1-oversight-smoke.sh` (hermetic). Full Viche suite green.

## Live measurement at delivery

`report`: **live = 1**, target = 5, deficit = 4, no duplicate titles, no stale
agents. Replenishment to the target requires operator-supplied scopes and
worktrees; the Executive does not invent mathematical research directions.

## Limitations

Auto-launch is deliberately not enabled without a curated registry. Raising the
target above five is a research-operator / Founder decision, not an Executive
one.
