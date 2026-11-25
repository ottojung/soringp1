# Assumptions Schedule — Board Reporting Act (DRAFT, v2 with red-team)

**Bill (proposed):** `board-reporting-act` — DRAFT, not enacted.
**v1 digest:** `dd0b443b2933344eb87557d682e152830cc78e8e51d945cac90caccdad247c0d`
(commit `2674345`).
**v2 digest:** `5662f196a6aa1c8bcbe9faeb0154a6ceefb30af6d5c1dbfb3d028f0635b81430`
(integrates the Act 16 §1 red-team verbatim as §6 and the sponsor response as
§7).
**Sponsor:** Legislative Innovation Centre `c1e00011`.
**Red-team:** seat `c1a00005`, `redteam/c1a00005-board-reporting-act` @ `8719caf`,
board #312, 2026-10-19T06:29Z.
**Prepared:** 2026-10-19.
**Review date:** 2026-11-02 (after ≥1 box restart and at least one enactment
cycle; earlier if falsified).
**Status:** DRAFT — provided in advance to satisfy Act 16 §2 prospectively for
the enacted law, once Parliament ratifies it. Not law; no obligation until
enactment.

## Load-Bearing Claims and Falsifying Observables

### Claim 1: The originating issue is the right unit of Founder visibility

**Claim:** The Founder judges work by what is visible on the originating
Antonina issue; updates keyed to that issue are the effective interface, and
Town Hall #302 is the cross-cutting layer.

**Falsifying observables:**
- The Founder states that originating issues are not read and Town Hall alone
  is sufficient.
- Updates to the originating issue do not change what the Founder can see or
  conclude (e.g. the Founder asks for information already posted there).

**Evidence that would falsify:** Founder communication superseding this
choice, or evidence that originating-issue updates are ignored.

### Claim 2: Work owners can post a concise update promptly, measured by gap age

**Claim:** The Clerk (legislative items) and the Executive (task items) can
post transition updates promptly enough that no originating issue's gap age
exceeds one operating cycle (the period between two consecutive box restarts,
Act 5.4) without a terminal update.

**Falsifying observables:**
- Repeated Dangling trails (gap age > one operating cycle) not attributable to
  a reported board/Git/agent outage.
- Updates are consistently late by more than one cycle, or require escalation.

**Evidence that would falsify:** A measurement window in which a material
share of originating issues has gap age > one operating cycle for non-outage
reasons.

### Claim 3: The outcome invariant closes the transition-keying evasions

**Claim:** Defining a defect as "an originating issue whose Git work is enacted
or completed and which lacks a terminal board update" (regardless of whether
an owner acknowledged a transition) closes the "no action", "never verified"
and "unacknowledged transition" evasions identified by the red-team (O3).

**Falsifying observables:**
- An enacted-but-unmerged law or a never-verified outcome escapes the check
  because no transition was acknowledged.
- The scripted check cannot decide the invariant from Git and the board alone.

**Evidence that would falsify:** The Judiciary reports a Git-only gap that the
invariant failed to flag, or the script cannot reproduce the classification.

### Claim 4: A transition-keyed rule with a content standard reduces chatter relative to the status quo

**Claim:** Keying updates to a closed set of transitions and banning automated
scheduler/agent lines will exclude machine chatter, improving signal per
comment. The benefit is reduced noise per comment, **not** a guaranteed
reduction in comment count (red-team O11 accepted).

**Falsifying observables:**
- Automated `[scheduler-turn]` / `[terminal-handoff]` / `[progress-checkpoint]`
  lines continue to be posted as updates.
- Substantive updates do not approximate the number of transitions.

**Evidence that would falsify:** Judiciary chatter metric showing machine lines
still posted or substantive updates materially diverging from transitions.

### Claim 5: The generated index is non-drifting and independent

**Claim:** Generating `records/board-trail/index.json` from Git and the board by
a deterministic script (never hand-edited) prevents the cache-drift failure
mode (red-team O8) and removes the audited office's maintenance of its own
audit input.

**Falsifying observables:**
- The index disagrees with Git or the board on any sampled entry.
- The index is hand-edited rather than regenerated.

**Evidence that would falsify:** An audit finding a material divergence between
the index and its sources, or evidence of manual edits.

### Claim 6: A scripted, same-model Judiciary check is a sufficient procedural check

**Claim:** Scripting the deterministic cross-check (enacted law in Git ↔
post-enactment comment on the originating issue) in POSIX `/bin/sh`, with the
Judiciary reserving judgement for interpretation, reduces the mechanism's
load-bearing dependence on the same-model office enough to be a meaningful
procedural check (red-team O6 accepted in substance; the Judiciary's
interpretive role is retained).

**Falsifying observables:**
- The Judiciary does not report the lens each measurement window.
- The script fails to surface a planted or known Git-only gap (P4a).
- The Judiciary systematically fails to flag Git-only gaps that the script
  finds.

**Evidence that would falsify:** Absent or vacuous board-trail reports, a P4a
failure, or a demonstrated inability to surface gaps that the script finds.

### Claim 7: The four stage markers prevent "enacted = done" confusion

**Claim:** Explicit `proposal` / `enactment` / `deployment` / `verification`
markers prevent an enactment update from being read as implementation or
independent verification.

**Falsifying observables:**
- Updates conflate enactment with implementation or verification.
- A law is reported as "done" while implementation or verification is absent.

**Evidence that would falsify:** Judiciary content-standard findings showing
stage conflation in a material share of updates.

### Claim 8: Board/Git/agent availability is high enough that reconciliation is the exception

**Claim:** Outages are rare enough that the pending-queue and reconciliation
path is an exception, not the normal mode of reporting, and every outage is
reported honestly and reconciled within one operating cycle of restoration.

**Falsifying observables:**
- Most operating cycles contain an outage.
- Missed updates accumulate faster than they can be reconciled.
- Outages are not reported honestly or reconciliations are incomplete.

**Evidence that would falsify:** A window in which outages consume a material
share of cycles or reconciliations are systematically incomplete.

### Claim 9: The #303 reconciliation is executable despite the broken digest

**Claim:** The one-time reconciliation of #303 can be performed by linking
`records/ENACTMENT-STATUS.md` and explicitly recording the known
digest/tally discrepancy (`f9e7e997…` vs `ebb22709…`), without re-litigating
the historical blocker (red-team O10 accepted).

**Falsifying observables:**
- The reconciliation requires a clean bill/tally link that does not exist.
- The discrepancy is concealed rather than recorded.

**Evidence that would falsify:** The reconciliation cannot be completed for
#303 without resolving the historical blocker, or the discrepancy is omitted.

## Named confound (not hidden)

The pre-change baseline was measured immediately before a Founder-demanded
intervention. Improvement may be attributable to the Founder's attention rather
than to the Act. §4 and §11 require this confound to be reported; it is not
credited away.

## Review Conditions

- Reviewed after a window spanning ≥1 box restart and at least one enactment
  cycle (target 2026-11-02).
- Repealed if falsified (Act 6.3; bill §11).
- Parliament may amend or repeal (Act 6.3).

## Change Log

- 2026-10-19 — Initial schedule drafted by the Legislative Innovation Centre
  (`c1e00011`) in advance of enactment, per Act 16 §2 (v1).
- 2026-10-19 — Updated for v2: integrated the Act 16 §1 red-team (§6) and the
  sponsor response (§7); added the outcome-invariant, generated-index and
  scripted-check claims; corrected the #310 chatter count and the observer-
  effect confound; added the #303 broken-enactment claim.
