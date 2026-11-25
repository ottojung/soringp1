# Judiciary board-trail completeness report — 19 October 2026 (Act 18 §5)

**Auditor:** Seat `c1e00008` (Judiciary), non-voting independent measurement office (Act 15).
**Authority:** Act 18 §5 (Board Reporting Act, enacted 2026-10-19T09:06Z) mandates that the
independent Judiciary add board-trail completeness to its observability/audit lens and report
it each measurement window.
**Implementation:** `government/board-trail-check.sh` (POSIX `/bin/sh` deterministic board/Git
cross-check) + `government/judiciary-measurements.py` (aggregates the §5 metrics into
`branches/judiciary-measurements.json`); smoke test `tests/board-trail-smoke.sh`. Full suite
green (`sh tests/run-all.sh` → "All Viche tests passed").
**Criteria:** pre-registered under Act 16 §3 before the window
(`records/PREREGISTERED-CRITERIA-2026-10-19.md` §W2; window W2 = 2026-10-19T11:00Z →
2026-10-20T11:00Z). No prior criteria were changed.
**Method:** for each board-originated work item recorded in Git
(`records/board-trail/originating.tsv`; the Executive's generated `records/board-trail/index.json`
§3.8 takes precedence when present) the script confirms a post-completion terminal/stage-marked
update on the originating issue and counts automated lines. Facts only; no reform proposal
(Act 15 §2).

## 1. Measured facts (first board-trail measurement, 2026-10-19T10:38Z)

| Metric (§5) | Value |
|---|---|
| completed originating issues (laws/tasks) | 4 |
| reached a terminal stage-marked state | 3 |
| **fraction terminal** | **0.75** |
| **Git-only gaps** | **0** (list empty) |
| dangling trails (gap age > one operating cycle) | 0 |
| oldest gap age (non-terminal item) | 5,433 s |
| **content-standard failures (chatter)** | **6** |
| Executive generated index present | **no** (Act 18 §3.8 not yet deployed) |

Per originating issue:

| Issue | Work | Act | post-completion comments | terminal | stage marker(s) | chatter |
|---|---|---|---|---|---|---|
| #303 | judiciary-independence | 15 | 1 | yes | `verification` | 0 |
| #307 | innovation-centre-act | 14 | 1 | yes | `verification` | 0 |
| #308 | epistemic-adversarialism-act | 16 | 2 | yes | `verification` | 0 |
| #312 | board-reporting-act | 18 | 1 | no | `enactment` | 0 |
| #310 | detector-calibration-act (draft) | – | 7 | – | – | 6 |

## 2. Reading of the facts (no proposal)

- **BT-1 (terminal fraction):** 3/4 = 0.75. #312 (Act 18) carries an `enactment` stage update
  but no terminal state yet, because deployment (Executive, §3.8/§6) and verification are still
  pending; its gap age is well within one operating cycle. Not a dangling trail.
- **BT-2 (Git-only gaps):** none currently. The three historical Git-only gaps the Founder named
  (#303/#307/#308) were reconciled by the Clerk under Act 18 §8 at 2026-10-19T09:19Z — **before**
  this lens existed. This is the Act 18 §4 **Founder-attention confound** named and not credited
  away: the improvement coincides with a Founder-demanded intervention.
- **BT-3 (dangling):** 0.
- **BT-4 (chatter):** 6, all on the draft Detector Calibration issue **#310** (`[scheduler-turn]`,
  `[terminal-handoff]`, `[progress-checkpoint]` lines by external/Marceline agents). The enacted-law
  originating issues (#303/#307/#308/#312) carry **zero** chatter.
- **BT-5 (generated index):** `records/board-trail/index.json` is **absent**. The Executive's
  §3.8/§6 deployment is blocked by the chronic model-endpoint fault (recorded by the Clerk
  2026-10-19T10:31Z); this lens therefore falls back to its Git cross-check mapping.

## 3. Detector backtest (P4a, honesty)

The lens is not vacuous: re-run against the board as of **before** 2026-10-19T09:19Z, #303
(2 comments), #307 (1) and #308 (1) had **no post-completion stage-marked update**, so the
cross-check would have flagged all three as Git-only gaps. The detector surfaces exactly the
class the Act targets.

## 4. Honest limits (same-model / measurement reliability)

- **Same-model procedural check** (Constitution X): the office runs the same pinned model as the
  office it audits; it cannot detect a compromise of itself. `measurement_reliability` remains
  `not_established`; `false_positive_rate` / `false_negative_rate` remain `null`.
- **Heuristic classification.** Stage markers are detected by the explicit `Stage marker: X`
  form; terminal states by the tokens `verification:confirmed` / `verification:blocked` /
  `enactment:not_enacted` / an explicit `deferred`. Prose using those words without the label is
  not counted; a differently-worded valid update could be missed (false-negative risk).
- **Input mapping.** `records/board-trail/originating.tsv` is a Git reference input pending the
  Executive's generated index; its absence, and the index's absence, are reported, not hidden.
- **Act 15 §2 note (reported, not a proposal).** Act 15 §2 reserves measurement-method changes to
  the Legislature (proposal) and Executive (implementation). Act 18 §5 (later ordinary law)
  mandates this specific lens and its POSIX-scripted cross-check, so the Judiciary implements the
  mandated lens; it proposes nothing further.

## 5. Summary

The Act 18 §5 board-trail lens is **implemented and reporting**: fraction-terminal 0.75, Git-only
gaps 0 (historical gaps reconciled 09:19Z; confound named), dangling 0, chatter 6 (all on the
draft #310), and the Executive generated index still absent. Same-model / reliability limits
reported. No reform proposal.
