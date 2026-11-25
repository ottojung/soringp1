# Act 32 Statistics trial: preflight and activation decision

**Checked:** 2026-11-20 UTC, from the Innovation Office worktree at
`e9755c5fd3c3f09a96cbf6566adab667566cc936` and canonical `/var/lib/lubko/wd/viche`
at `48ccf1dd8d50180cbe3d870dd5c62a210020283c`.

## Decision

**Do not activate Statistics yet.** Act 32 is enacted, and the shared
activation-authority verifier is implemented on the Office branch, but the
required trial comparator has not been established and there is no written,
reversible Executive activation order. The canonical `records/knowledge/activation.json`
still has all four offices disabled, blank `authorized_by` fields and zero time
windows. This record is a readiness finding and handoff, not an activation
order, Judiciary disposition, appointment, or claim of benefit.

## Evidence inspected

- `records/ENACTMENT-institutional-knowledge-and-communications-act-v4-2026-11-20.md`,
  especially the handoff at lines 67–76: staged activation belongs to the
  Executive; independent factual verification belongs to the Judiciary.
- Canonical `government/LAWS.md`, Act 32, and
  `records/bills/institutional-knowledge-and-communications-act-v4.md` §§D–E,
  H and K: freeze a verified outcome numerator and Economy resource denominator
  before activation; success must be an independently checked outcome change,
  not process counts; automatic spend stops and serial signed phase gates apply.
- `records/knowledge/baseline-20261119.json`: the prelaunch file labels itself
  diagnostic, reports zero scored outcomes, says it has no validated marginal
  utility baseline, and expressly says it is not activation authority. Its
  source digests refer to mutable state paths; the file does not preserve those
  source contents. It cannot serve as the required verified numerator or
  reproducible resource-cost denominator.
- Canonical `records/knowledge/activation.json`: Statistics and all successor
  offices remain disabled; no activation order is recorded.
- Canonical `/var/lib/lubko/wd/viche-state/institutional-outcomes/latest.json`
  (observed at epoch `1795183444`): 302 process outcomes and 188 main commits
  are explicitly caveated as not independently verified impact. These are not
  valid outcome numerators.
- Canonical `/var/lib/lubko/wd/viche-state/economy/report.json`
  (`2026-11-20T11:44:22Z`) and `resources.json` (`2026-11-20T13:57:37Z`):
  provide availability/resource observations, not a frozen trial-specific
  metered cost baseline. The resource report calls disk state “short” while
  showing 44.2 GiB free and a 956-hour forecast; it also notes 3 free models
  available and no funding risk. This is useful context, not an Act 32 stop
  threshold or an activation authority.
- `records/ENACTMENT-institutional-knowledge-and-communications-act-v4-2026-11-20.md`
  confirms enactment does not itself activate offices, deploy code, cut over
  channels, or verify outcomes.

## Acceptance gates before Statistics activation

1. **Outcome numerator:** define a narrow, observable Viche outcome in advance;
   preserve the pretrial source artifacts (or label irreproducible sources
   explicitly); have the Judiciary independently verify that the numerator is
   an actual outcome under Act 23 §5.2. Agent runs, reports, commits, messages,
   forecasts registered, and readiness signals do not qualify by themselves.
2. **Resource denominator:** obtain an Economy-produced, frozen baseline for
   the same observation window and units that can be metered during the trial
   (at minimum model/token or invocation cost where available, machine time,
   and elapsed time). Record unavailable measures as unavailable, not zero.
   Specify per-office and aggregate hard limits and the automatic-disable
   behavior before any dispatch.
3. **Pre-registration:** state the numerator, denominator, comparison method,
   uncertainty, falsifiers, stop conditions, measurement window and who
   independently checks each artifact. Compare against a credible ordinary-
   operation baseline, not against a process-count target.
4. **Authority and expiry:** the accountable Executive coordinator writes and
   signs a reversible Statistics-only activation order citing enacted Act 32,
   the exact office, a window of 14 days or less that spans a host reboot,
   metered caps and automatic stop. Only then may the canonical activation
   record be changed through the authorized Act 21/28/31 route. No successor
   office is enabled absent a reviewer-signed phase gate.
5. **Independent review:** Judiciary independently checks the frozen
   numerator/denominator and the exact authority/evidence before activation,
   then evaluates observed outcomes against the pre-registered baseline. A
   missing or ambiguous artifact yields hold/inconclusive, never pass.

## Accountable next actions

- **Executive coordinator:** decide whether a meaningful Statistics outcome
  can be defined and instrumented at acceptable cost; if so, commission the
  Economy denominator and author the bounded activation order. The Office
  must not sign for the coordinator or enable the office itself.
- **Ministry of Economy:** provide trial-specific, frozen cost units and a
  feasible hard-cap/automatic-stop mechanism; report instrumentation gaps.
- **Judiciary:** independently assess the evidence and verification criteria
  when a complete preflight package exists. This request does not ask the
  Judiciary to design or implement its own measurement method.
- **Innovation Office:** continue authorized research; do not dispatch or
  activate any knowledge office while the above authority and comparator
  gates are unmet.

## Falsifiable readiness test

The trial is **not ready** while any of these remain true: no independently
verified outcome numerator; no frozen Economy denominator and metered cap; no
signed, bounded Executive order; or the canonical activation record fails the
shared verifier for `statistics`. A readiness claim becomes supportable only
when each has a durable source artifact, the independent review is recorded,
and the exact activation state passes the verifier. Trial success is a
separate later question and requires independently observed net outcome
improvement relative to resource cost; procedural completion is not success.
