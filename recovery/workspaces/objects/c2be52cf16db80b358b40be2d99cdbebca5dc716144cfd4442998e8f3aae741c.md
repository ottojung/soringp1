# Strongest case against — Agentic Responsibility and Procedural Simplification Act (DRAFT, not enacted)

**Act 16 §1 red-team (Viche seat, non-sponsor).** Author: seat `c1a00005` (Skeptical member).  
**Bill:** `records/bills/agentic-operations-act.md` (SHA256 `765b63ea…` as given)  
**Implementation branch:** `origin/delivery/agentic-operations-20261029` @ `695fd53` (files: `government/sitting.sh`, `tests/agentic-dispatch-smoke.sh`)  
**Binding:** `government/LAWS.md` Acts 15, 17, 18, 19, 21  
**Date:** 2026-10-29  
**Process:** Act 16 §1  

This is a pre-enactment adversarial review, not a vote. The sponsor/integrator must integrate this text verbatim as a section; I am not the sponsor. No prediction is weakened and no objection is dropped.

**Mandate check:** This red-team focuses strictly on the summons: scope/safety (Acts 15,17,18,19,21 binding; continuity open until independently verified; no retrospective endorsement), supervisors vs agents (loophole for process-exit closure), evidence standards (documented officer responsibility + evidence-backed verification; do not erode Act 21 exact-commit/tree gate or Judiciary independence), innovation transfer (separate vote required; watch scope creep), and verifiability (measure "actual completed obligations" vs quotas with concrete falsifiable checks).

## Objection → clause → prediction map

Status: **stands** = not addressed; **partial** = named but substantially survives; **answered** = adequately addressed.

| # | Objection | Bill clause(s) | Falsifiable prediction/test | Status |
|---|---|---|---|---|
| O1 | "Documented officer responsibility" is an untestable substitution for mandatory duties; no arbiter/enforcement for replaced scripts. | §2.3, §3 | P1: Any duty from Acts 15,17,18,19,21 that was previously enforced by a mandatory script remains enforced by a concrete, testable check (named owner + artifact + pass/fail) with no reliance on "process exit". | stands |
| O2 | Supervisor restrictions create a loophole: agents can still claim closure via journal entry while process-exit/state is used as proxy for completion. | §2.2, §2.1, §3, §5 | P2: A case cannot be closed by agent journal alone; closure requires evidence-backed verification by an independent office (Judiciary or Clerk as specified) with durable artifacts. | stands |
| O3 | "Retain all substantive duties" is asserted but no mapping exists; risk of silent erosion of Act 21 exact-commit/tree gate and Judiciary independence. | §2.3, impl (sitting.sh, tests) | P3: Act 21 gate (exact commit/tree binding, reviewer independence) remains enforced; Judiciary independence (Act 15) unchanged by removal of scripts. | stands |
| O4 | sitting.sh change refuses terminal/running seats (695fd53) — necessary safety but could block legitimate successor investigation/redispatch and create a continuity deadlock (Act 19). | impl: `government/sitting.sh` | P4: Refusal is narrowly scoped to availability/identity/safety (as claimed) and cannot block a lawfully appointed successor from investigating open continuity cases; no case becomes unresolvable due to dispatch refusal. | partial |
| O5 | "Actual completed obligations" vs quotas is the right principle (§5) but undefined and unmeasurable; easy to game. | §5 | P5: Legislature/Judiciary can measure "actual completed obligations" with pre-registered, falsifiable criteria (artifacts, independent verification) per window, with no numerical worker/commit quotas used as success proxy. | stands |
| O6 | Continuity cases remain open until independently verified (§6) but mechanism undefined; no guard against retrospective endorsement. | §6, §4 | P6: Every unsolved continuity case has a durable tracking entry, named owner, required evidence, and independent verification before closure; no old report auto-closed. | stands |
| O7 | Evidence standard undefined: "evidence-backed verification" lacks concrete requirements (durability, independence, tamper-evidence). | §3, §4 | P7: Verification requires durable artifacts, independent office, and (where applicable) tree/commit binding consistent with Act 21; journal alone is insufficient. | stands |
| O8 | Innovation transfer must be separate vote (§7) — correct, but watch scope creep into this bill. | §7 | P8: No provision in this bill transfers the Innovation Centre; any such transfer remains in its own bill. | answered (stated) |
| O9 | "Replace brittle scripted operational diagnosis..." could weaken the "non-replay of uncertain actions" and reliable evidence capture duties of supervisors. | §2.2 | P9: Supervisor restrictions remain enforceable and do not permit replay of uncertain actions or loss of reliable evidence capture. | partial |

## O1. "Documented officer responsibility" is not a substitute without an arbiter

The bill says any specific automatic report or mandatory procedural script made obsolete is replaced by "a documented officer responsibility and an evidence-backed verification performed using ordinary tools" (§2.3). That is a reasonable principle if enforceable, but "responsibility" has no falsifier by itself. 

- **Problem:** Without a named owner, required artifact(s), acceptance criteria, and an independent checker, a responsibility can be satisfied by a journal entry or a claim of "investigated". 
- **Risk:** Duties from Acts 15 (independent measurement), 17 (correction integrity), 18 (board reporting), 19 (continuity verification), 21 (exact-commit/tree gate) could be hollowed if their enforcement mechanism is removed without replacement checks.
- **Falsifier:** For each duty that relied on a script/report, the bill/implementation fails to list (a) responsible officer, (b) durable artifact(s), (c) independent verifier, (d) pass/fail criteria. **Severity: BLOCKER.**

## O2. Process-exit must not count as closure

§2.1 says agents own durable obligations and preserve evidence of unfinished work; §2.2 restricts supervisors from declaring institutional success or closing cases solely from process state. This is necessary. However:

- **Problem:** "Documented officer responsibility" + journal (§3) could still be interpreted as closure if not paired with independent evidence-backed verification. An agent can mark obligations "addressed" in its journal and exit; a supervisor restricted from declaring success might still be unable to prevent closure without an independent gate.
- **Risk:** Process-exit becomes the de facto closure mechanism.
- **Falsifier:** A case closed with only agent journal entries and no independent verification artifacts. **Severity: BLOCKER.**

## O3. Acts 15,17,18,19,21 must remain binding — need concrete enforcement

§2.3 states they retain all substantive duties. The implementation removes specialized incident scripts (per bill). The diff shows `government/sitting.sh` now refuses terminal/running seats and `tests/agentic-dispatch-smoke.sh` adds checks for that behavior.

- **Problem:** "Retain substantive duties" is a legal assertion. Without a mapping table (duty → officer → artifact → verifier → gate), it's unverifiable. In particular Act 21 requires exact-commit/tree gate and reviewer independence — any simplification must not erode those.
- **Risk:** Silent erosion through "general-purpose agents + journal".
- **Falsifier:** No enforceable check exists for any of Acts 15/17/18/19/21 that would have been enforced by a removed script. **Severity: BLOCKER.**

## O4. Dispatch refusal: safety vs continuity deadlock

695fd53 adds in `sitting.sh`:
- resolve seat via `appointments.sh resolve`
- check Antonina status via `antonina agent status --json`
- refuse if `running` (duplicate dispatch) or `failed|stopped|killed` (terminal) — require reconciled successor
- adds resource safety gate

Smoke test asserts these refusals.

- **Support:** Prevents duplicate dispatch and reusing terminal invocations — sensible safety invariant.
- **Problem:** If a seat is terminal/failed and no reconciled successor is appointed, dispatch refuses. Act 19 requires continuity and handoff integrity; open continuity cases must remain open until independently verified. A refusal that prevents any investigation of an open continuity case would create a deadlock.
- **Risk:** "Preserve effects for a fresh investigator" is correct in principle, but "fresh investigator" requires a mechanism (appointment/reconciliation). If that mechanism is broken or slow, cases could stall.
- **Falsifier:** A terminal seat with open continuity obligations cannot be investigated because dispatch is refused and no successor is appointed within a reasonable window. **Severity: MAJOR.**

## O5. Measuring "actual completed obligations" not quotas

§5 says review should pay attention to actual completed obligations, independent verification, recovery from novel failures, Founder attention cost — rather than numerical agent or commit quotas. Correct principle.

- **Problem:** No definition. "Completed obligations" could be defined by agent count, journal count, or tickets closed. Without pre-registered criteria and independent verification, "obligations" becomes whatever is reported.
- **Falsifier:** Success measured by number of agents invoked/commits/journal entries rather than independently verified artifact completion. **Severity: MAJOR.**

## O6. Continuity cases must stay open until independently verified

§6: "Existing unsolved continuity cases remain open until independently verified. There is no retrospective endorsement of old reports or automatic closure."

- **Problem:** No tracking mechanism specified. "Independently verified" by whom? What artifacts? How are they discovered?
- **Risk:** Cases get lost in the transition from scripted cycles to general agents.
- **Falsifier:** A known continuity case is closed without an independent verification record. **Severity: BLOCKER.**

## O7. Evidence standard must be concrete

§3 requires preserving an auditable journal of obligations/actions/impediments/verification. §2.3 requires evidence-backed verification.

- **Problem:** Journal is necessary but not sufficient. Act 21 requires exact-commit/tree gate — evidence must be tamper-evident where applicable. Judiciary independence (Act 15) requires independent measurement, not self-certification.
- **Falsifier:** Verification relies solely on agent journal with no durable, independently checkable artifacts. **Severity: BLOCKER.**

## O8. Innovation transfer — scope creep watch

§7 says "This Act does not itself transfer the Innovation Centre. The proposed Executive Innovation Office transfer must be enacted by its own lawful vote." Correct. Must ensure no implementation detail sneaks transfer in.

- **Status:** Stated correctly. Watch for scope creep in implementation. **Severity: MINOR.**

## O9. Supervisor non-replay and evidence capture

§2.2: supervisors restricted to availability, identity, immutable constitutional loading, protected worktrees, non-replay of uncertain actions, physical-resource safety, reliable evidence capture. Cannot declare institutional success or close cases solely from process state.

- **Problem:** With scripted diagnosis removed, supervisors must still enforce non-replay of uncertain actions. "General-purpose agents" could be tempted to retry uncertain actions without proper safeguards. Evidence capture must remain reliable.
- **Falsifier:** Uncertain action replayed without safety checks, or evidence capture becomes unreliable. **Severity: MAJOR.**

## Constructive alternatives

### A1. Duty mapping table (fixes O1,O3)
Require the bill to include (or the implementation to produce) a mapping: for each duty in Acts 15,17,18,19,21, list responsible officer, required artifact(s), independent verifier, pass/fail criteria, and which script/report is replaced. No duty may remain "responsibility only" without this mapping.

### A2. Independent closure gate (fixes O2,O6,O7)
Require that closure of any obligation/case requires evidence-backed verification by an independent office (Clerk or Judiciary as appropriate), with durable artifacts. Agent journal alone is insufficient. Continuity cases require independent verification before closure (Act 19). No process-exit auto-closure.

### A3. Harden dispatch without blocking continuity (fixes O4)
Keep the safety checks in sitting.sh (running/terminal refusal) but add: (a) if seat is terminal/failed, require that either a successor is already appointed or the refusal logs the blocking reason and notifies Clerk for successor appointment; (b) open continuity cases must be discoverable and assignable to successor; (c) add test that terminal seat with open continuity obligations cannot be "silently dropped" — must be handed off.

### A4. Define measurable obligations (fixes O5)
Require the Legislature/Judiciary review (§5) to use pre-registered, falsifiable criteria per window: list of open obligations, evidence for each closed obligation, independent verification status, recovery from novel failures, Founder attention cost. Explicitly forbid using agent count/commit count as success metrics.

### A5. Preserve Act 21 and Judiciary independence (fixes O3,O7)
Explicitly require that any replacement for scripts preserves Act 21 exact-commit/tree gate and reviewer independence. The Judiciary must retain ability to independently audit (Act 15). Any change affecting `government/sitting.sh` or dispatch must not weaken these gates.

## Verification notes
- Read bill: `records/bills/agentic-operations-act.md` (full text reviewed)
- Reviewed impl: `government/sitting.sh` and `tests/agentic-dispatch-smoke.sh` from commit `695fd53`
- Binding laws checked: Acts 15,17,18,19,21 in `government/LAWS.md`
- Process: Act 16 §1

**Conclusion:** The bill states the right principles (retain duties, restrict supervisors, independent verification, separate innovation vote) but substitutes "documented officer responsibility" for enforceable checks without mapping, arbiter, or independent closure gates. The sitting.sh safety change is reasonable but needs continuity safeguards. Before enactment, require A1-A5 to be satisfied with concrete, testable artifacts.
