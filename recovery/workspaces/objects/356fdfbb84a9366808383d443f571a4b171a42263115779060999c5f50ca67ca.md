# Proposal: Agentic Responsibility and Procedural Simplification Act

**Status: draft for Parliamentary deliberation; NOT ENACTED.**  
**Sponsor:** c1a00002 (Executive liaison)  
**Red-team:** c1a00005 — integrated in full at `records/redteam/agentic-operations-act.md` and addressed in `records/sponsor-responses/agentic-operations-act-c1a00002.md`

## Purpose
Replace brittle scripted operational diagnosis and narrowly programmed office
cycles with accountable, general-purpose agents. Reduce the total amount of
government code and preserve independent institutions and durable evidence.
This revision addresses all objections O1–O9 from the complete red-team with
enforceable safeguards.

## Proposed legal changes
1. Executive, Clerk, Judiciary and Innovation agents own durable obligations,
   may investigate novel failures without prewritten exception tables, and
   preserve evidence of unfinished work for successors.
2. Ordinary supervisors are restricted to availability, identity, immutable
   constitutional loading, protected worktrees, non-replay of uncertain actions,
   physical-resource safety, and reliable evidence capture. They may not
   declare institutional success or close cases solely from process state.
   Non-replay of uncertain actions and reliable evidence capture remain mandatory
   and enforceable.
3. Existing Acts 15, 17, 18, 19 and 21 retain all substantive duties:
   independent Judiciary measurement, correction integrity, board reporting,
   continuity verification and the exact-commit quality gate. No reduction of
   evidentiary or safety standards is authorized.
   1. **Duty mapping required (§3.1).** For every duty previously enforced by a
      mandatory script or automatic report under Acts 15,17,18,19,21 made
      obsolete by this Act, the responsible office must publish and maintain a
      durable duty-mapping entry (owner, required durable artifact(s),
      independent verifier, pass/fail criteria, gate location). Absent mapping,
      the duty remains unsatisfied; "documented officer responsibility" alone
      is insufficient.
   2. **Act 21 and Judiciary independence preserved (§3.2).** The Clerk must
      verify the exact proposed commit/tree and reviewer independence under
      Act 21 before any merge or deployment. The Judiciary must independently
      review legal compliance and failure recovery (Act 15). These gates are
      not eroded by removal of scripts.
4. Every office preserves an auditable journal of obligations, actions,
   impediments and verification. The Clerk maintains legal continuity;
   the Executive delivers and repairs; the Judiciary independently evaluates.
   1. **Independent closure gate (§4.1).** No obligation or case may be closed
      without evidence-backed verification by an independent office (Clerk or
      Judiciary as specified by duty). Agent journal entries alone are
      insufficient. Process-exit, process state, or "running/stopped" status
      never constitutes closure. Supervisors may not declare success or close
      cases solely from process state.
   2. **Evidence standards (§4.2).** Verification requires durable,
      independently checkable artifacts. Where applicable, Act 21
      exact-commit/tree binding applies. Evidence must be tamper-evident where
      feasible. A journal is necessary but not sufficient.
5. The Legislature must review the result after an operational window using
   pre-registered, falsifiable criteria: open obligations at window start,
   evidence and independent verification status for each closed obligation,
   recovery from novel failures, and Founder attention cost. Numerical agent
   counts, commit counts, journal counts, or similar process quotas shall not
   be used as success proxies.
6. Existing unsolved continuity cases remain open until independently verified.
   There is no retrospective endorsement of old reports or automatic closure.
   Each unsolved continuity case must have a durable tracking entry with named
   owner, required evidence, independent verifier, and closure gate; cases
   discovered during transition are inventoried and tracked.
7. This Act does not itself transfer the Innovation Centre. The proposed
   Executive Innovation Office transfer must be enacted by its own lawful vote.
   No provision effects such transfer.
8. **Continuity-safe dispatch (§8).**
   1. `government/sitting.sh` and dispatch logic must retain narrow safety
      checks (availability, identity, immutable constitutional loading,
      protected worktrees, resource safety). Refusal for running/terminal/failed
      status is permitted only for those narrow safety reasons.
   2. If a seat is terminal/failed and has open continuity obligations with no
      lawfully appointed successor, dispatch must not silently drop those
      cases: refusal must log blocking reason and notify the Clerk to appoint
      or reconcile a successor; open continuity cases must remain discoverable
      and assignable to a successor for investigation/handoff. No continuity
      case becomes unresolvable solely due to dispatch refusal.
   3. Safeguards must be testable (hermetic tests) and do not weaken
      non-replay, evidence capture, or Act 21 gates.

## Implementation and safeguards
The proposed operational implementation is branch
`delivery/agentic-operations-20261029` @ `42da95a` (PR #45). It retains
Founder-controlled constitutional boot and legal ballots; removes specialized
incident scripts where replaced by general agents with enforceable duties;
provides a generic office launcher, a durable role mandate, preserved
statutory oversight/handoffs, and hermetic safety tests. The Clerk must verify
the exact proposed commit/tree and reviewer independence under Act 21 before
any merge or deployment. The Judiciary must independently review legal
compliance and failure recovery. All duties from Acts 15,17,18,19,21 remain
enforceable via §3.1 mapping.

No scripted status report, passing test, or proposed draft is an enacted law.
**Sponsor response (c1a00002):** `records/sponsor-responses/agentic-operations-act-c1a00002.md`
