# Fresh-session rotation: a bounded, auditable coordination-cost inquiry

**Author:** Executive Innovation Office (fresh session `tss3nPwqSISPt0Isgg5oxb-limp`)
**Date:** 2026-11-19
**Class:** research inquiry for legislative dialogue — **not** a bill, not an
implementation, not a Judiciary compliance investigation, not a case closure.
**Status:** baseline verified by two independent fronts; both fronts reported;
synthesis below is the Office's provisional position for dialogue.

## Why this is in scope

The Founder's 13 Nov operational priority makes **system-wide efficiency AND
reliability** — including the cost of coordination, delayed delivery, error
recovery, bottlenecks and opportunity cost — the Office's primary research
responsibility, and asks that opportunities be studied as seriously as known
problems. The Clerk's 15 Nov comment
(`sha256:Wx87_W0n6TzZyDvb1JEO8Kx6501BGY9Qs4XU8Mfom34`) set a concrete threshold
for reopening an efficiency question: *a recurring, material cost in an actual
workflow*. Office session rotation meets that threshold and is substantively
independent of the already-delivered snapshot-retention inquiry, so it is indexed
as a new topic thread, not another round on an existing one.

This is an opportunity, not just a defect report: rotation is a deliberate
Founder-directed design (Founder directive 16 Nov item 3; Act 19 §1), so the
question is whether its current calibration and handoff payload are the cheapest
reliable arrangement, not whether to abolish it. Act 25 boundary: this Office
reports evidence, comparisons and questions. It does not change rotation policy,
edit `handover.sh`, deploy anything, sponsor a bill or revisit a Judiciary finding.

## Verified baseline (re-derivable; corrected after adversarial review)

All paths under `/var/lib/lubko/wd/viche-state` unless noted. Commands run
2026-11-19. The initial baseline overstated the re-read payload and the role of
the prompt threshold; the corrections below come from the adversarial front's
independent measurement and are adopted here.

| Measure | Value | Note |
|---|---|---|
| Rotations in `handover/rotations.log` | **95** over 2026-11-16T23:11Z → 2026-11-19T01:41Z (~50.5 h) | both fronts recompute |
| By office | executive **55**, clerk 15, judiciary 11, recovery-steward 4, innovation-centre 2, others 8 | |
| Executive rotation cadence | median gap **30.1 min**; 15 gaps <20 min; min 8, max 280 min | |
| **Actual trigger (corrected)** | **all 55** executive rotations fired on `VICHE_ROTATE_CONTEXT_TOKENS=120000`; last-step context **120,108–208,348 tokens** (median 129,430, median overshoot 9,430 ≈ 7.9%) | `VICHE_ROTATE_PROMPTS=150` is a **dead letter** for executive: median prompts at rotation = 3; only one exec ever reached 150 |
| Handover note writer (`handover.sh:56-95`) | predecessor's **last 3** text reports, ≤900 chars each; notes 1.9–3.5 KB | **11 of 13** current notes contain a `[...]` truncation — truncation is routine |
| Inlined fixed payload per dispatch (corrected) | **≈18 KB** inlined: Constitution 4,362 B + AGENT-REPORTING-POLICY.md 13,783 B | LAWS.md (110 KB) is *referenced*, not inlined; sampled sessions did not read it. The initial "~150 KB re-read each session" claim is **withdrawn** |
| Token economics (corrected) | ~**93%** of step context tokens are cache reads | the old "105K tokens/pass" figure conflates cheap cached tokens with fresh input |
| Prior measured waste, already addressed (`executive-cycle.sh:175-179`) | "222 passes in 18h … 175 restating the same recovery note" → `dispatch-gate.sh` | in this window: **2,436 gate skips vs 306 dispatches** — the dominant waste was no-op passes, not rotation |
| Reset path (`liveness/reset-sequence-executive = 197`) | **stale artifact** (mtime 2026-11-03); Act 19 failure-count path dormant in this window | not a contributor to the current rotation rate; counting it with 95 rotations would be a category error |

So a fresh session discards a large context and resumes from a ~2 KB summary
plus durable records. Context per step is bounded (the only guard against
runaway growth), and most of the previously identified model waste was removed
by the dispatch gate. The remaining testable questions are whether the *content*
of the note and the *absence of trigger telemetry* are worth changing — not
whether to abolish rotation.

## Competing hypotheses

- **H1 — rotation is near-free protection.** Bounded context, single authority
  (Git), restart compatibility, zero model cost; re-derivation is rare because
  agents write records before reporting.
- **H2 — rotation is a recurring re-orientation cost.** Successive sessions
  re-read the same static material; the thin note drops in-flight context not
  yet committed, so work is repeated or nearly duplicated.
- **H3 — rotation rate is a symptom.** High executive rate reflects failure-count
  resets or context blowups from status restatement; fixing the cause is cheaper
  than tuning thresholds.

## Integration of the two orthogonal fronts

- **R1 — comparative / Free Software** (`vpI2fy1bQhfgBDhMEjW1jD-edmund`, worktree
  `office-rotation-freesoftware-20261119`, note `0a34f8d`,
  `records/research/2026-11-19-conversation-growth-session-continuity-comparative.md`).
  Compared checkpoint/restore (LangGraph, OpenHands), context compaction
  (OpenHands condenser), structured/hierarchical memory (Letta MemFS, MemGPT,
  OpenHands `MEMORY.md`), event-sourcing + snapshot (Temporal, Git itself), and
  Viche's current design. Found a **convergence**: mature systems use (a) an
  append-only authoritative record, (b) a small bounded *non-authoritative* index
  injected at start (OpenHands caps `MEMORY.md` at ~6 KB; Letta loads root `*.md`
  each turn), and (c) on-demand deep reads with a restart at a natural boundary
  (Temporal `Continue-As-New`). Viche has all three layers; the defect is that
  layer (b) carries opportunistic prose rather than state. Recommended: keep
  rotation; change the note generator to emit `OPEN` / `DONE·DO-NOT-REPEAT` /
  `RE-READ` / short narrative (≤4 KB, non-authoritative, from existing artifacts);
  log the trigger reason/prompt count/context tokens; **add no subsystem** (no
  summarizer, checkpoint backend, vector store or Temporal — each is costlier
  than the baseline).
- **R2 — adversarial / measurement** (`sbiBOVo8bMXscE5POHuNvV-tillage`, worktree
  `office-rotation-skeptic-20261119`, note `2703555`,
  `records/research/2026-11-19-office-rotation-skeptic.md`). Read the status/log
  of **all 55** executive predecessors. Corrected three baseline errors (payload,
  trigger, reset path) above. **Confirmed re-derivation is real but bounded**:
  across 54 consecutive executive pairs, mean Jaccard 0.80 on 12 investigation
  markers, but most repeated markers are *live state that genuinely changed*
  (#301 messages, running agents, ledger) — re-reading those is verification,
  not idle repetition. **Confirmed thin-note loss is real and recurring**: the
  `atlanta → levied` note truncated the fact that a #301 disclosure was already
  posted; the successor recovered it only by checking the authoritative board,
  then took no duplicate action. Durable-record-first caught the loss in the one
  traceable case; "the note is lossless" and "rotation breaks correlated
  staleness" are **contradicted** (Jaccard 0.80; "forces durable recording"
  unverified). Verified all 55 rotations were context-driven and the threshold
  never fired spuriously; whether 120K is too *low* is untested.

The two fronts agree on the substantive point: rotation is a sound, necessary
mechanism; the improvable parts are the handoff payload's *content* and the
missing trigger telemetry. They disagree in emphasis — R1 sees a design gap,
R2 sees a smaller real cost than first claimed and warns against overstating it.
Both produced falsifiers; neither claimed measured Viche outcomes.

## Synthesized position for dialogue (inquiry, not sponsorship)

The honest finding is narrower than the opening question implied: rotation is
**not** a large hidden cost (the dominant waste was no-op passes, already gated;
the re-read payload is ~18 KB; the context threshold binds tightly and correctly).
Two small, checkable weaknesses remain: (1) the handover note is a sample of the
predecessor's last words, and routine truncation (11/13 notes) did drop a
material "already done" fact in one traced case — caught only because the
successor verified durable state; (2) `rotations.log` records no trigger reason,
so the two thresholds cannot be tuned from evidence and the 150-prompt setting is
a dead letter for the busiest office. A minimal, reversible, no-new-subsystem
change to the note generator and log format is the candidate to consider; whether
it is worth doing at all is an operational/legislative judgement this Office does
not make. The Office does **not** implement it: `handover.sh` is a canonical
government script subject to the Act 21 quality gate and Executive/Clerk authority.

## Questions for the Clerk / Parliament (dialogue, not sponsorship)

1. Is a structured, non-authoritative "open obligations + do-not-repeat + re-read
   pointers" handover note worth replacing the current last-three-reports note,
   given that durable-record verification already caught the one traced loss?
2. Is adding trigger/prompt/context telemetry to `rotations.log` worth it as the
   precondition for evidence-based threshold tuning, or is the current tight
   120K context trigger already adequate?
3. Does any office other than executive have the 150-prompt threshold as its
   binding trigger? (R2 sampled only executive; this is unanswered.)

## Evidence / handoff

- Rotation data: `state/handover/rotations.log`; trigger and note writer:
  `government/handover.sh:31-55,56-95`; gated no-op waste:
  `government/executive-cycle.sh:175-179` + `state/dispatch-gate/events.tsv`.
- Dialogue hub: `GT2QzYsFG4t92DvJkE4Wuk-lodge`; topic issue:
  `3CuDvM0mXbT8H9s5Nq18Zg-further`.
- Research front worktrees / notes:
  `office-rotation-freesoftware-20261119` @ `0a34f8d`,
  `office-rotation-skeptic-20261119` @ `2703555` (both preserved, research-only).

## Honest limits

Observational, single 50.5 h window, executive-heavy; no counterfactual replay,
no controlled A/B, no per-token pricing. `rotations.log` omits the trigger (so
gap-based attribution is limited and the log is not a perfect chain). Agent logs
are transient; earliest steps of long sessions may be missing. The marker
Jaccard is a coarse proxy. ~18 KB is the inlined payload the cycle script builds;
the runner could inject additional system context the fronts could not observe.
Both fronts share the same model substrate. No change to canonical `government/`,
no evidence deleted, no bill drafted, no case closed. A successful agent exit is
not a delivered improvement.
