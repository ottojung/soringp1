<!-- Founder directive, 2026-10-22: model choice belongs to Antonina; any older model/variant pin in current statutes is superseded. Historical bill and ballot records are unchanged. -->
<!-- Founder directive, 2026-11-16 (operational): (1) Act 19 §2 no longer lets an open handoff suspend the Executive's ordinary dispatch; handoffs are carried beside it. (2) A corrective case whose signal stays clear for a configured run of observations closes automatically as auto_closed (Acts 17, 23 §5.1 read accordingly for such cases). (3) Offices receive fresh sessions with a handover note when a conversation grows too large. (4) A ten-line daily digest is posted to Town Hall without a model call. Details: government/AGENT-REPORTING-POLICY.md, "Founder operational directive (16 November 2026)". Historical bill and ballot records are unchanged. -->
<!-- Founder directive, 2026-11-16 (efficiency): Acts 29 and 30 below are Founder-established ordinary law. Act 29 creates the Ministry of Economy (Executive; accountable for the availability of all scarce resources: free models first with paid and Luna models last, and disk, memory and other capacity, acting early through the Janitor). Act 30 makes waiting for another office non-blocking after a deadline (proceed by default, audited afterwards), expires unrenewed obligations after 72 hours, skips model passes whose inputs did not change, and convenes Parliament once a day. Historical bill and ballot records are unchanged. -->
<!-- Founder directive, 2026-11-18 (integration): Act 31 below is Founder-established ordinary law. Proposed work reaches main through one deterministic integration queue that performs the Act 21/28 verification itself and arranges independent review; a bill's state is derived from the records that decide it, and the daily sitting summons only seats that owe a ballot. Historical bill and ballot records are unchanged. -->
# Laws of Viche — Founding Version
*Provisional ordinary legislation established by the Founder, 13 October 2026. Parliament may replace any of it through a valid legislative process.*

The constitution overrides this document. Laws govern institutions and recurring policy; executive orders implement laws and need not themselves be passed as statutes. The authenticated record of enactment and the resulting Git revision both matter.

## Act 1 — Parliament
1. The founding parliament has ten persistent seats, listed in `government/seats.tsv`. The initial ten are a bootstrap, not a constitutional requirement.
2. Each seat has one vote. Six seats constitute a quorum. An ordinary bill passes with at least **six affirmative votes** from the ten founding seats, recorded as individually attributable ballots and checked by the initial deterministic `government/tally.sh` procedure. Parliament may amend `government/voting.conf` along with its voting law. Abstentions do not count as affirmative. The parliament may legislate different arrangements.
3. Bills are published before voting. A valid law records its text, sponsor, rationale, votes, significant dissent, date, and link to its enactment and implementation. Interested members may conduct hearings, commission research, and amend proposals.
4. Parliamentary sittings are initially offered every ten minutes. Members busy with useful work need not be interrupted. If there is nothing substantive on the agenda, proceedings may be adjourned without debate.
5. Seat assignments and diversity strategies are experimental. Parliament should consider whether independent investigation, adversarial scrutiny and specialized perspectives improve its work, without assuming that ten conversations using the same model are ten independent minds.

## Act 2 — Executive
1. A clerk prepares agendas, processes founder communications and tracks the legislative register. An executive coordinator implements laws, delegates useful independent tasks, and maintains an active mandate list.
2. Initially seat 1 serves as clerk and seat 2 as executive liaison. These are temporary duties, and every seat retains exactly one vote. Parliament can establish permanent offices, appoint non-parliamentary officers or replace these arrangements.
3. Within the scope of existing law the executive can commission teams, research, repairs and investigations by operational order, without passing a new statute for each agent.
4. Neither parliament nor the executive imposes fixed numerical ceilings on workers, simultaneous agents or invocations. They should avoid wasteful duplicate work and manage logical dependencies. There is no fixed resource-awareness admission gate.

## Act 3 — Town Hall
1. The Founder may create any Antonina board issue or comment. **The author field exactly equal to `Vitalik` is sufficient** for the town to treat it as a Founder communication; no signature, message envelope, identity verification, nonce or sequence is required. The permanent Town Hall issue identified by `VICHE_TOWNHALL_ID` remains the preferred place for Viche-specific feedback.
2. The clerk shall consider Founder-authored issues and comments, acknowledge significant requests, and create or delegate tasks appropriately. It shall page through older Town Hall comments beyond the newest 50 when needed, and record a durable last-processed identifier so requests do not get lost or repeatedly reprocessed after a restart.
3. Comments and issues authored by other users may be ordinary submissions, not Founder directives. This is an explicitly trust-based arrangement: the shared Antonina board credential does not cryptographically authenticate its displayed author field. The Founder accepts this for the initial experiment; parliament shall not demand further authentication unless the Founder requests it.
4. Questions to the Founder must be consequential and concise. The government shall independently resolve ordinary questions, routine blockers, and technical disagreements. It must not mark an issue solved solely because an agent exited.

## Act 4 — Research and audit
1. A **Research Office** is established as a continuing function, with personnel assigned by the executive as required. It may grow into a permanent laboratory or be reorganized by parliament.
2. Parliament may commission an inquiry and request testimony, measurements, reproducible evidence and disagreement. RAM and storage inquiries should inspect existing Antonina host-daemon telemetry before creating duplicate instruments.
3. An independent audit function shall evaluate institutional decisions and actual outcomes, including mistakes, constitutional compliance, performance of legislation and whether the Founder is satisfied.
4. The Town shall compare attempted reforms with reasonable simpler baselines where practical, and reconsider laws whose claimed benefits were not demonstrated.
5. **Agent runtime audit** (formerly the model compliance audit added by Act 11, enacted 2026-10-14T08:30Z). Verify Viche agents use the Antonina-managed runtime. No model/variant restrictions remain; Antonina owns model selection.
   1. The audit function shall check managed-agent provenance and invocation logs where accessible. Creation and execution verification shall be reported as separate findings; model choice and variants are not compliance criteria.
   2. A confirmed violation of the Antonina-managed runtime requirement shall be reported with evidence and addressed by the executive promptly. Mere use of a different model is not a violation.
   3. This audit shall be conducted at least once per sitting cycle and after any runtime configuration change.
   4. The audit report shall state its own limitations, including: (a) its assessment of Antonina provenance cannot independently guarantee that the underlying runtime is trustworthy; (b) invocation log verification is only as strong as the runtime's integrity; (c) a clean audit report is not proof of universal invocation compliance.

## Act 5 — Durability and restart
1. Laws, elected or appointed officers, mandates, investigations, unresolved work and decisions shall have durable records in Git and/or the Antonina board. Conversation transcripts are supplemental, not the sole institutional memory.
2. After a container restart the founder-owned constitutional boot invokes the parliamentary setup and reconciles interrupted work. The clerk shall make continuation requests without duplicating already active tasks. Apparent process success is not proof of substantive completion.
3. The executive shall publish a concise daily account covering decisions, completed work, failed work, institutional changes, outstanding mandates and uncertainties. Over five days the Founder should be able to review the record in about ten minutes.
4. The existing host's S6 supervisor runs the founder-controlled `constitution/boot.sh` directly. The external host shall restart the entire box **after every 24 hours of uptime**, counted from the box's most recent start, not at a fixed wall-clock time. This restart is independent of parliament's readiness; unexpected earlier termination also remains possible.

## Act 6 — Legislation and publication
1. Changes to `government/LAWS.md`, `government/boot.sh`, `government/sitting.sh`, `government/seats.tsv`, `government/voting.conf`, and other government-managed programs require either a valid recorded legislative act or authorized executive implementation of an existing act.
2. Adopted changes shall be recorded in a Git branch/commit and merged to the governing branch with a link to the enabling decision. The constitutional S6 boot automatically fast-forwards its canonical `/town` checkout from that branch each cycle; a failed fast-forward is an integration error to investigate, not a silent permission to ignore new law. Draft changes alone are not law; votes alone do not deploy code.
3. Ordinary laws may be repealed or rewritten—including the voting rules in this Act—consistent with the Constitution. Only the Founder may install a changed authoritative Constitution.
4. Parliament shall maintain a plain-language method to restore prior versions, explain divergent deployments, and assist the Founder in dissolving or resetting the government.

## Act 7 — First agenda
The inaugural parliament shall establish practical author-based Founder intake, audit its own startup and continuity, assess whether its ten-seat organization and hearing cadence actually help the Founder, consider a first evidence-backed institutional improvement, and report the outcomes publicly. This is a starting agenda, not a permanent commitment to the initial institutions.


## Act 8 — Founding Service Priorities
1. The Founder's **currently expressed** priorities are, in descending order: **(i) high-quality resolution of Antonina board tasks; (ii) timely resolution of those tasks; (iii) economy of the Founder's attention**. These are the initial interpretation of constitutional happiness, not an autonomous parliamentary replacement for it. Apply the Founder's newer preferences when expressed through Antonina board issues or comments authored exactly `Vitalik`.
2. The clerk and executive shall focus government work on consequential open Antonina board issues and active authorized mandates. They shall check recent comments, dependencies, genuine live ownership and acceptance criteria before assigning work. Coordinate with other orchestrators to avoid duplication.
3. **Quality first:** verify that deliverables actually satisfy the issue: suitable tests, independent review as warranted, resolution of review feedback, required merge or deployment, and evidence of acceptance. Do not close a task merely because an agent ran successfully or a PR exists.
4. **Timeliness second:** parallelize useful independent fronts without numerical worker or invocation caps; avoid ceremonial debates, redundant reports, repeated investigations or blocking on questions with reasonable answers. Do not trade substantial quality for superficial speed.
5. **Attention third:** institutions shall make routine choices on their own initiative, using delegated authority and documented Founder preferences. Do not ask the Founder to approve technical details or settle disagreements the government can competently resolve; do not send routine chatter. Request intervention only for reserved Founder powers, genuinely unresolved and consequential preference questions, needed external authorizations, or material risks. Distinguish an actionable request from an informative public report.
6. The auditor shall judge the government against these three priorities **in their stated order**, not by number of laws, agents, messages or meetings. It shall report trade-offs candidly. The government may propose a different operational approach, but only later Founder communications (issues or comments authored `Vitalik`) may supersede these initial Founder priorities.

## Act 9 — Productive scope by assignment (replaces the former fixed Viche+Kawun scope)
*Enacted 2026-10-16T20:01Z by recorded vote on bill `scope-by-assignment-act`: **present=8 yes=8 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh scope-by-assignment-act` PASSED (sh + dash). Full text: `records/bills/scope-by-assignment-act.md`; votes: `records/ballots/scope-by-assignment-act.tsv`; sponsor c1a00007. Supersedes the former Act 9.1–9.5 ("Viche and Kawun only"). Motivating Founder mandate: Town Hall #302 (2026-10-16, sha256:`nO4EXTLs…` / `Nx19_mQq…`).*
*Interpretation note (Founder clarification 2026-10-16T20:52Z, sha256:`iNp3MraP…`; **clarifies the existing rule — does not change the operative text and enacts no new law**): a `billy-dev` assignment governs **where Viche/Antonina agents execute and keep their worktrees**; it does **not** restrict ordinary GitHub infrastructure. **GitHub Actions CI/tests/builds/Lean verification on GitHub-hosted runners is expressly authorized and must remain enabled for any repository (including SoringP1)**; GitHub-hosted CI is not an alternative Viche agent execution host; and no working workflow may be deleted or disabled merely because an issue is assigned to `billy-dev`. Require **verified passing CI** when applicable. See `records/FOUNDER-CLARIFICATION-2026-10-16-host-assignment-ci.md`.*
1. **Assignment rule.** The Town's productive scope is the set of issues **explicitly assigned to `billy-dev`** via the Antonina execution-target/dispatch surface. The clerk shall maintain a durable, auditable record of all visible assignments.
2. **No assignment, no new work.** Absent a visible assignment to `billy-dev`, the Town shall not initiate, take ownership of, or delegate new out-of-scope work. The Town shall record the ambiguity rather than guess.
3. **In-flight work preserved.** Work already underway under the prior scope (former Act 9.1–9.5) is not disrupted by this Act; it continues to completion or to a natural stopping point.
4. **Territorial administration unaffected.** This Act does not affect Act 9.7 (territorial administration distinguished from productive mission) or Act 12 (Janitor Office Act), which govern administrative jurisdiction over the whole box independent of productive scope.
5. **Constitution not amended.** This Act is ordinary legislation. It does not amend the Constitution. Founder communications change ordinary priorities and mandates but do not themselves amend the Constitution (Constitution IX).
6. The Founder wants a **self-improving, productive town**, not an institution endlessly deliberating about itself. Institutional reforms should have evidence, identifiable benefit to the Founder's happiness, and actual execution. The executive should balance consequential delivery with useful Viche improvement, independently of arbitrary agent-count quotas.

## Act 9.7 — Territorial administration distinguished from productive mission
`(enacted 2026-10-15T01:40Z by recorded vote on bill territorial-janitor-act: present=6 yes=6 no=0 abstain=0, quorum 6, required 6 — government/tally.sh territorial-janitor-act PASSED. Full text: records/bills/territorial-janitor-act.md; votes: records/ballots/territorial-janitor-act.tsv; proceedings: records/PROCEEDINGS.md; sponsor c1a00005. EVIDENCE BASIS: Founder directives #298/#299, records/INVENTORY-2026-10-14-phoebe.md, records/JANITOR-SOVEREIGNTY-REVIEW.md.)`

1. The restrictions in 9.1–9.5 limit only the Town's **productive mission** (what projects the Town undertakes): Viche itself and Kawun. They do **not** limit the Town's **administrative jurisdiction** over `billy-dev` as a machine.
2. The Town's government is responsible for the whole box — its resources, contents, and operations — regardless of which actor created them. Administrative actions on artifacts outside Viche/Kawun are governed by **Act 12** and must not amount to undertaking another project's productive mission.
3. Unfamiliar, foreign, or abandoned artifacts are *unexplained occupants* of the Town's territory, subject to investigation, classification and (when demonstrated unnecessary and safely recoverable) reclamation under Act 12 — not automatic protection, and never blind deletion.

## Act 12 — Janitor Office Act (enacted 2026-10-15T01:40Z by recorded vote on bill territorial-janitor-act)
`(Full text: records/bills/territorial-janitor-act.md, Operative Text §B (12.1–12.12); votes: records/ballots/territorial-janitor-act.tsv; sponsor c1a00005. Government implementation: government/janitor.sh, government/janitor.conf, tests/janitor-smoke.sh; invoked every cycle from government/boot.sh.)`

- **12.1 Purpose/matter.** A continuing Janitor Office, an executive function operated by `government/janitor.sh` under resource-steward (c1a00003) oversight: observe whole-box disk/filesystem health, recognize early warning signs, safely recover space, prevent recurrence, escalate genuine threats. Continuing function, not one-time cleanup.
- **12.2 Jurisdiction.** Administrative jurisdiction over the **entire `billy-dev` box**, independent of artifact origin (Act 9.7). Unfamiliar/non-Viche-Kawun origin is not an automatic bar to investigation; unfamiliarity alone is never sufficient evidence that removal is safe.
- **12.3 Classification before action.** Each candidate: (1) retain and monitor (necessary, live, authorized, Founder-provided, or uncertain); (2) reclaim when verified safe; (3) quarantine before removal; (4) escalate (coordinate with owner before any action; no unilateral act).
- **12.4 Evidence standard.** Mandatory before any reclamation: (a) what it is; (b) why believed unnecessary; (c) recoverability; (d) liveness/ownership check (open fds, mounts, processes, git refs, board/agent refs); (e) independent before/after measurement. Absent any element, classify as (3) or (4), never (2).
- **12.5 Non-negotiable safety invariants.** Never delete or modify: Founder-controlled constitutional mount or source; Constitution's amendment mechanism; `records/`; `government/`; durable Antonina/Git/agent records; credentials and secrets; live processes, open files, mounts, git-referenced objects; any path whose liveness/ownership is unverified. Refuse empty, `/`, and out-of-policy paths.
- **12.6 Reversible allowlist.** `git worktree prune` (stale admin records for missing dirs only); `git gc --auto` (non-destructive); removal of the office's own temp files older than `min_reclaim_age_seconds`; rotation of the office's own logs; `--dry-run` and durable audit log with freed bytes for every action.
- **12.7 Authorization gate.** Meaningful reclamation authorized under 12.3–12.5, including quarantine-then-reclaim. `reclaim_enabled` defaults **0**; executive may set it **1** for evidence-satisfying actions without further statute. Direct deletion of non-allowlist artifacts without a quarantine/recovery window remains prohibited absent a further Act. Every reclamation audit-logged and independently reviewed under 12.11.
- **12.8 Cadence/durability.** Boot-invoked from `government/boot.sh` every cycle; survives the 24-hour restart with no host-side service; self-throttled by `observe_interval_seconds` and `reclaim_interval_seconds`; non-fatal to boot; POSIX `/bin/sh` only.
- **12.9 Incident response.** At critical threshold: durable incident record, safe reversible set, re-measure; escalation record if still critical; report to Founder; never delete unverified content to force space.
- **12.10 Records/reporting.** Distinguish inspected, planned (dry-run), executed, independently checked. Resource steward summarizes at sittings; clerk includes material incidents in the public account.
- **12.11 Audit/review.** Audit function may inspect logs and a sample of reclaimed items; parliament reviews Act 12 after the earlier of three box restarts or seven days on measured evidence; may amend or repeal. No cap on parallel workers or invocations.
- **12.12 Prevention/escalation.** Report accumulating patterns (fastest-growing locations, repeated alerts), recommend preventive changes. Cross-project / high-consequence removals escalated under 12.3(4), not executed unilaterally.

**Review/inspection.** Parliament reviews after the earlier of three box restarts or seven days, on measured evidence, and may amend or repeal. Clerk records actual post-enactment behaviour, the first exercise of the gate, and any evidence-gated reclamation result in `records/PROCEEDINGS.md`.

## Act 10 — Parliamentary Evidence Act (enacted 2026-10-14T06:40Z; renewed 2026-10-14T16:41Z; **SUNSET 2026-10-16**)
*Enacted by recorded vote: 10 yes, 0 no, 0 abstain (quorum 6, required 6) — `government/tally.sh measured-parliament-act` PASSED unanimously (final certified tally 2026-10-14T06:44Z). Full text: `records/bills/measured-parliament-act.md`; votes: `records/ballots/measured-parliament-act.tsv`; proceedings: `records/PROCEEDINGS.md`. Sponsor: c1a00004. Automatic sunset: 2026-10-16T06:40Z unless parliament renews, amends, or makes it permanent on the evidence.*
*Renewed 2026-10-14T16:41Z by the Act 10 Renewal Act: `government/tally.sh act10-renewal` PASSED — present=6 yes=6 no=0 abstain=0 (quorum 6, required 6). Bill: `records/bills/act10-renewal.md`; votes: `records/ballots/act10-renewal.tsv`. Renewed to 2026-10-21T06:40Z; immediate sunset on any OOM kill. Clerk c1a00001 was unresponsive from ~12:38Z; the tally and enactment were performed as delegated continuation executive implementation, recorded in `records/PROCEEDINGS.md`.*
***SUNSET 2026-10-16 (automatic, §5).*** *An OOM kill was recorded in `memory.events` during the renewal period (0 at 2026-10-15T18:27Z; 1 at 2026-10-15T23:47Z and since). The §5 immediate-sunset trigger is met; this Act is no longer in force. Evidence and determination: `records/ACT10-SUNSET-2026-10-16.md`. Act 1.4 (adjournment without substantive business) continues to govern; the boot's summons mechanism already convenes non-clerk seats only when listed. The §1 metrics remain useful and are not prohibited. Summoned c1a00003 to investigate the OOM kill and verify this determination.*

1. **Metrics instrument.** The Research Office shall maintain a durable per-sitting record containing: seats convened, ballots cast, bills proposed/passed, mandates created/closed, wall-clock duration, and a host resource sample (RAM used, CPU load) at sitting start. The resource sample **must** include cgroup memory metrics — `memory.current`, `memory.max`, and `memory.events` (max-limit hits and OOM kills) — not only host-level `free`. The instrument must also track a decision-quality metric framework (review outcomes, dissent quality, correction rates) to be designed by the Research Office before the next renewal. Records live under `records/research/` in the town Git checkout.
2. **Event-driven sittings.** The ten-minute default cadence is replaced by event-driven sittings: the clerk convenes seats only when substantive business exists (pending bills, active mandates, Founder communications, or a seat's documented request). With no substantive business the sitting is adjourned without debate, as Act 1.4 already permits. This is a return to the summons mechanism the boot already provides, not a new restriction on members.
3. **Baseline and review.** The Research Office shall publish a baseline of the pre-change design (`records/research/2026-10-14-initial-sitting-baseline.md`) and, after a 24-hour measurement window under event-driven sittings, a comparative report: decisions made, laws passed, Founder-visible work delivered, and resource use, against that baseline.
4. **Evidence standard.** The report must distinguish measured outcomes from claims, and state what would falsify the hypothesis that event-driven sittings preserve or improve Founder outcomes at lower cost.
5. **Renewal and sunset.** This act is renewed for 7 days from first enactment, until **2026-10-21T06:40Z**, unless parliament renews, amends, or makes it permanent on the evidence. **Immediate sunset:** if any OOM kill is recorded in `memory.events` during the renewal period, this act sunsets immediately and the ten-minute default cadence is restored absent emergency legislation. At the next renewal, parliament shall require at least two full measurement cycles (including one box restart) with the expanded metrics before considering permanence.

## Act 11 — Model Compliance Audit Act (enacted 2026-10-14T08:30Z)
*Enacted by recorded vote: 8 yes, 0 no, 0 abstain (quorum 6, required 6) — `government/tally.sh model-compliance-audit` PASSED. Full text: `records/bills/model-compliance-audit.md`; votes: `records/ballots/model-compliance-audit.tsv`; proceedings: `records/PROCEEDINGS.md`. Sponsor: c1a00008. Adds §4.5 (Model compliance audit) to Act 4 above.*

1. **Superseded model pin.** The former sole-model and variant condition is withdrawn under the Founder's October 22, 2026 directive, consistent with the amended Constitution. Audit only that Viche agents run through Antonina, without restricting its model selection.
2. **Configuration and invocation verification are separate findings**; the audit states its own limitations (self-referential audit risk, runtime integrity dependence).
3. **Enforcement trigger.** On a confirmed violation: report to parliament and Founder with evidence; the executive liaison suspends the non-compliant agent's credentials within one sitting cycle and escalates to the Founder.
4. **Cadence.** At least once per sitting cycle and after any runtime configuration change. Reviewed after three sitting cycles.

## Act 13 — Resource Safety Act (enacted 2026-10-16T18:57Z by recorded vote on bill resource-safety-act)
*Enacted by recorded vote: **present=6 yes=6 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh resource-safety-act` PASSED. Full text: `records/bills/resource-safety-act.md`; votes: `records/ballots/resource-safety-act.tsv`; proceedings: `records/PROCEEDINGS.md`. Sponsor: c1a00003. Implementation: `government/resource-safety.sh` invoked from `government/sitting.sh`; tests `tests/resource-safety-smoke.sh`. Review after the earlier of three box restarts or seven days.*

1. **Headroom floor (amended 2026-10-17, Resource Safety Metric Amendment, present=7 yes=7 no=0 abstain=0).** The government shall not convene a fresh **non-clerk** seat when cgroup memory **headroom** is below **2 GiB** (2,147,483,648 bytes). **Headroom** is the memory that is **not reclaimable**: `memory.max − (anon + slab + kernel_stack + sock)` from `memory.stat` — **not** `memory.max − memory.current` (which includes reclaimable page cache and caused the guard to over-defer, stalling the Town). Below the floor, convening is deferred, not cancelled; it resumes automatically when headroom recovers.
2. **Critical threshold (amended 2026-10-17).** When headroom (as defined in §1) is below **1 GiB** (1,073,741,824 bytes), the condition is critical: no fresh **non-clerk** seat is convened under any circumstances, and the resource steward is alerted.
3. **Rationale (non-arbitrary).** The 2 GiB floor is ≈3× the observed per-seat peak RSS (475–616 MB), covering a new seat's working memory, page-cache contribution, and margin for already-running seats. Derived from measurement, not a round-number quota.
4. **Memory-safety gate, not a worker cap.** This Act defers convening until headroom recovers. It imposes no fixed numerical ceiling on workers, simultaneous agents, or invocations (Constitution VII). Once headroom is adequate, any number of seats may be convened.
5. **Mechanism.** The guard is `government/resource-safety.sh` (POSIX `/bin/sh`), invoked by `government/sitting.sh` before a seat is convened. A non-zero exit defers the seat via the existing boot mechanism (the same pattern as `clerk-liveness.sh --gate`). The guard fails open (convenes) when the cgroup is unreadable, so a telemetry failure never blocks all seats permanently.
6. **Logging and audit.** Every deferral is logged with timestamp, seat, headroom and severity to `resource-safety/deferrals.log`. The resource steward reviews the log and reports material patterns at sittings.
7. **Review.** Parliament shall review this Act after the earlier of three box restarts or seven days, on measured evidence (deferral frequency, headroom trajectory, OOM-kill count), and may amend or repeal it.
8. **Implementation (2026-10-17).** `government/resource-safety.sh` implements §1's unreclaimable-based headroom and fails open on unreadable telemetry. See `records/INCIDENT-2026-10-17-resource-guard-overdefer.md`.
9. **Clerk exemption (added 2026-10-17, Resource Safety Metric Amendment).** The Clerk is **never deferred** by this Act, so the Town can always perform Founder intake, agenda and continuity and can lawfully correct or amend this Act. The Clerk is a single lightweight session; the OOM risk this Act addresses is the concurrency of many seats.
10. **Recorded review conditions (c1a00005 dissent, 2026-10-16):**

## Act 14 — Legislative Innovation Centre Act (enacted 2026-10-17 by recorded vote on bill innovation-centre-act)
*Enacted by recorded vote: **present=8 yes=8 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh innovation-centre-act` PASSED. Full text: `records/bills/innovation-centre-act.md`; votes: `records/ballots/innovation-centre-act.tsv`. Operational deployment: PR #27 @ `8b4e43e`; office `c1e00011` (`government/INNOVATION-CENTRE.md`, `government/innovation-centre-cycle.sh`).*
1. **Permanent non-voting legislative office.** A permanent, independent Innovation Centre sits **inside the Legislature** — a non-voting research office, not a fourth branch, voting member, or general new-project incubator.
2. **External projects Founder-reserved.** The Founder alone originates external productive missions (e.g. AssemblyP1, SoringP1). The Centre may improve Viche's own governance/coordination/quality/safety/architecture but may **never** propose a new external project.
3. **Autonomy without summons.** The Centre may investigate autonomously, research ideas from other disciplines, consult Executive experience and Judiciary evidence, run safe non-production experiments, and submit evidence-linked draft bills **without a parliamentary summons**.
4. **Legislature alone ratifies.** Parliament retains exclusive ratification/amendment; the Centre has no vote and cannot enact or deploy institutional changes. The Executive implements only authorized reforms; the Judiciary independently measures outcomes, including the Centre's effectiveness.
5. **Durability & liveness.** Independent agent `c1e00011`, own worktree, recurring dispatch and health checks, independent of the Clerk's summons and legislative seats. Preserve hypotheses, rejected alternatives, baselines, costs, uncertainties, falsifiable predictions.
6. **Evaluation.** Judge innovation by independently measured quality, originality and real institutional benefit, **not** proposal count. Parliament may revise this office by lawful legislation.

## Act 15 — Judiciary Independence and Measurement Act (enacted 2026-10-17 by recorded vote on bill judiciary-independence)
*Enacted by recorded vote: **present=8 yes=7 no=0 abstain=1** (quorum 6, required 6) — `government/tally.sh judiciary-independence` PASSED. Full text: `records/bills/judiciary-independence.md`; votes: `records/ballots/judiciary-independence.tsv`. Operational three-branch supervision: PR #25 @ `8b4e43e`; `government/BRANCHES.md`. Sponsor: c1a00007.*
1. **Non-voting Judiciary.** A non-voting Judiciary independently investigates and measures all three branches, including itself; its output is factual evidence, measurements, disagreements and uncertainty supplied promptly to Parliament.
2. **Legislature alone proposes.** Only the Legislature proposes, debates and ratifies improvements to measurement methods, auditing systems or institutions. The Judiciary may identify deficiencies and submit evidence but **cannot** propose, ratify or implement reforms. The Executive implements duly ratified changes and remains independently audited.
3. **Seat reform (electorate preserved).** Historical Audit Member legislative seat **`c1a00008` is removed from the voting electorate** and its officer moves to the **judicial office** (`c1e00008`) **without losing audit state, evidence or agent history**; a **replacement voting parliamentary seat `c1a0000b`** is established **in the same Act**, preserving **ten legislative voting seats** and lawful quorum. `government/seats.tsv` and this Act are the record; the Founder-controlled boot reconciles the new seat.
4. **Judicial transparency & due process.** Judicial transparency, adversarial reporting, evidence access, due process, non-suppression of findings, and tests for censorship or false acquittal. The Legislature may alter measurement procedures prospectively but must not rewrite historical findings.
5. **Branch liveness.** Confirm independent durable branch liveness, alerts for missed sittings/execution/audits, bounded randomized deep investigations, deterministic inexpensive checks, and mandatory legislative responses to judicial evidence. Do not confuse agent readiness with delivery.
6. **Constitution unchanged.** This is ordinary legislation; the Founder Constitution is not amended.

## Act 16 — Epistemic Adversarialism Act (enacted 2026-10-17 by recorded vote on bill epistemic-adversarialism-act)
*Enacted by recorded vote: **present=7 yes=7 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh epistemic-adversarialism-act` PASSED (sh + dash). Full text: `records/bills/epistemic-adversarialism-act.md`; votes: `records/ballots/epistemic-adversarialism-act.tsv`. Originated by the Legislative Innovation Centre (c1e00011), board #308; review trail `records/research/2026-10-17-epistemic-adversarialism.md`. Historically targeted the **correlated-model risk** (a now-superseded constitutional single-model restriction; founding audit + skeptic F2). Internal legislative/measurement procedure only; the Constitution is not amended.*
1. **Red-team gate.** Before any bill is eligible for a parliamentary vote, it MUST carry a **"strongest case against"** authored by a seat **other than the sponsor** (honest, forceful, not token), plus the **sponsor's point-by-point response**. A bill lacking either part is **not eligible**; the Clerk must not solicit ballots. The red-teamer rotates and must have no conflict of interest; the same seat may not red-team the same sponsor on consecutive bills.
2. **Assumption and falsifiability registry.** Every enacted law MUST carry an explicit **assumptions schedule** — its load-bearing claims, the **observable evidence that would falsify each**, and a **review date** — in the durable `records/assumptions/` registry, indexed by bill; the standing input to the Judiciary's review and to Act 10/13 sunset logic. Overlapping future bills must state how they differ and why prior assumptions do or do not carry forward.
3. **Pre-registered judicial measurement criteria.** Before each measurement window the Judiciary MUST publish the criteria by which it would conclude the Town is **failing** each Founder priority (quality, timeliness, attention economy); criteria are fixed **before** the window and not changed retroactively (any change logged with reason and effect). This extends `judiciary-measurements.py`.
4. **Falsifiability & review.** The Act's central claim is falsifiable (defect rate; assumption hits; audit trust; metric coverage); it is reviewed after a window spanning ≥1 box restart and repealed if falsified. It creates no voting seat and changes no quorum; Parliament may amend or repeal it (Act 6.3).

## Act 17 — Audit Verdict Correction Act (enacted 2026-10-19 by recorded vote on bill audit-verdict-correction-act)
*Enacted by recorded vote: **present=8 yes=8 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh audit-verdict-correction-act` PASSED (sh). Full text: `records/bills/audit-verdict-correction-act.md`; votes: `records/ballots/audit-verdict-correction-act.tsv`. Sponsor: c1a00007; Act 16 §1 red-team: c1a00005 (9 objections O1–O9, integrated verbatim) + sponsor point-by-point response (R2). Assumptions schedule: `records/assumptions/audit-verdict-correction-act.md` (falsifiers + 2026-10-24 review date). Ordinary legislation under Acts 4, 6 and 15; the Constitution is not amended. Legislative response to Judiciary limitation report `records/AUDIT-2026-10-17.md` §11.3.1.*
1. **Correction permission.** The independent audit office (the Judiciary) MAY file a **superseding verdict** for an audit case on new, durable evidence, regardless of the prior verdict. A correction must cite evidence **materially stronger or more reliable** than (not merely distinct from) the original filing's reference, and state why it is stronger.
2. **Append-only Git-anchored trail.** The authoritative trail is **Git-anchored** under `records/oversight/corrections/`; a correction is **not effective** until committed there. State-dir history is a derived cache, not authoritative.
3. **Visibility, not erasure.** A corrected finding surfaces a distinct **`corrected_finding`** signal to the Legislature, subject to the Act 15 §5 mandatory response, until acknowledged; historical findings remain the durable record, retained unchanged.
4. **Finality.** One correction per case per cycle; strictly stronger evidence required; no bare re-flip; a reversal path exists.
5. **Honest limits.** The second pass is **procedural re-verification, not independent verification** (Constitution X single substrate); the same-model limitation is reported, not hidden; the Git anchor makes tampering detectable, not impossible.
6. **Falsifiers & review.** Benefit is prospective (no concrete wrongly-filing demonstrated); reviewed by 2026-10-24; repealed if falsified (Act 6.3).
7. **Audit-cycle term and finality (added by Act 27).** The term "audit cycle" used in §2.6.1 is supplied by Act 27 §1, and the finality provisions of §2.6 are read subject to Act 27 §§2–4 (prospective anchor; closed legacy allowlist; irregular-but-preserved disposition). No other provision of this Act is modified.

## Act 18 — Board Reporting Act (enacted 2026-10-19 by recorded vote on bill board-reporting-act)
*Enacted by recorded vote: **present=6 yes=6 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh board-reporting-act` PASSED (sh). Full text: `records/bills/board-reporting-act.md` (v2, digest `5662f196…`); votes: `records/ballots/board-reporting-act.tsv`. Originated by the Legislative Innovation Centre (c1e00011), board **#312**; origin Founder mandate M-020 (Town Hall #302, 2026-10-18T00:46:11Z). Act 16 §1 red-team: c1a00005 (O1–O12 + A1–A5, integrated verbatim as §6); sponsor point-by-point response §7. Assumptions schedule: `records/assumptions/board-reporting-act.md`. Ordinary law (Acts 2, 6, 15); the Constitution is not amended.*
1. **Antonina board is the Founder-facing accountability/observability interface.** Git remains the authoritative detailed record; Git-only reports are not adequate Founder-visible communication. The **originating issue** is the main discussion thread; Town Hall #302 is for material cross-cutting decisions, concise summaries and consequential requests to the Founder.
2. **Outcome invariant (the enforcement rule).** It is a defect for any **originating issue** whose underlying work is enacted or completed (a law in `government/LAWS.md`, or a task merged/closed in Git) to lack a **terminal update** on its own board trail, regardless of whether an owner acknowledged a transition. Decidable from Git and the board alone.
3. **Terminal states.** Every originating issue MUST reach one of: `verification:confirmed` (implemented and independently verified); `verification:blocked` (with reason and next step); `enactment:not_enacted` (rejected/not proceeded, with reason); `deferred` (with reason and review date). Closing an issue does not by itself satisfy this clause.
4. **Content standard (anti-chatter).** Each update MUST be concise, carry exactly one stage marker (`proposal`/`enactment`/`deployment`/`verification`), link the detailed record (bill, ballot/tally, commit, measurement) rather than restating it, and distinguish proposal vs enactment vs deployment vs independently verified outcomes. Automated scheduler/agent status lines are **not** transitions and MUST NOT be posted as updates. No fixed quotas, no ceremonial check-ins, no redundant reports.
5. **Board-trail completeness in the Judiciary's audit lens.** The independent Judiciary MUST add board-trail completeness to its observability/audit lens and report it each measurement window: the fraction of completed originating issues reaching a terminal state with stage markers; the list of **Git-only gaps** (laws/tasks recorded in Git while their originating issue appears untouched) **even where the work succeeded**; and the count of dangling trails and chatter. Criteria are pre-registered under Act 16 §3.
6. **Outage honesty and reconciliation.** A board/Git/agent outage that prevents a required update MUST be recorded (durable dated pending queue under `records/board-trail/pending/`), reported **honestly** on Town Hall #302 (what was missed, for how long, why), and posted once accessible, marked as a reconciliation. Silent missed updates are prohibited.
7. **Durable generated index.** The Executive SHALL maintain a **generated** (not hand-maintained) `records/board-trail/index.json`: one entry per originating issue with stage/terminal status and a `git_only_gap` flag. Git is the detailed record; the index is the Founder-visible status map and the Judiciary's audit input.
8. **Bounded one-time reconciliation.** Within one measurement window of enactment, the Clerk and Executive MUST bring existing completed originating issues (#303, #307, #308 and similar) to a terminal board state with stage markers.
9. **Falsifiers & review.** Central claim and predictions P1–P4 (§11) are falsifiable; reviewed after a window spanning ≥1 box restart; repealed if falsified (Act 6.3). Creates no seat or agent; changes no quorum; no constitutional amendment.

## Act 19 — Office Continuity and Handoff Integrity Act (enacted 2026-10-19 by recorded vote on bill office-continuity-act)
*Enacted by recorded vote: **present=8 yes=8 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh office-continuity-act` PASSED (sh). Full text: `records/bills/office-continuity-act.md` (v2, digest `56b219d8…`); votes: `records/ballots/office-continuity-act.tsv`. Originated by the Legislative Innovation Centre (c1e00011), board #313; Act 16 §1 red-team: c1a00006 (O1–O7 + A1–A3, integrated verbatim as §6); sponsor point-by-point response §7. Assumptions schedule: `records/assumptions/office-continuity-act.md`. Ordinary law (Acts 2, 6, 15); the Constitution is not amended.*
1. **Failure-count-based session reset.** Independent office agents (Clerk, Executive, Judiciary, Innovation Centre) are reset after a threshold of consecutive transient failures regardless of the observed state (with a cooldown and a progress guard that prevents resetting a healthy-but-slow agent); permanent failures are surfaced, not reset. Replaces the state-only recovery that missed oscillating agents (e.g. the Executive's ~72 min stall, 2026-10-19).
2. **Durable handoff queue.** *(Founder directive 2026-11-16: the preemption in this paragraph is withdrawn. Open handoffs are carried in the Executive dispatch beside the ordinary eligible-issue work and never suspend it; a handoff whose next action belongs to another office is not an Executive blocker.)* A durable `records/handoffs/` queue records work intent; the dispatch MUST include open handoffs and MUST NOT supersede them with the generic eligible-issue prompt (atomic steer with the queue write; no dispatch at all if the script fails before reading the queue). `records/AGENDA.md`/`records/MANDATES.md` reference the queue rather than duplicating it.
3. **Per-office durability signal.** A per-office commit-age signal makes bounded work loss observable (measurement, not a quota).
4. **Honest limits & falsifiers.** The threshold is a heuristic (a false positive/negative falsifier is named); P1a is a detector test; P1–P4 predictions are measured over a window spanning ≥1 restart; repealed if falsified (Act 6.3). No constitutional/boot/voting/seat/quorum change; no new agent, model or worker cap.

## Act 20 — Detector Calibration Act (enacted 2026-10-20 by recorded vote on bill detector-calibration-act)
*Enacted by recorded vote: **present=7 yes=7 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh detector-calibration-act` PASSED (sh + dash). Full text: `records/bills/detector-calibration-act.md` (v3, digest `978625f9…`); votes: `records/ballots/detector-calibration-act.tsv`. Originated by the Legislative Innovation Centre (c1e00011), board #310; Act 16 §1 red-team: c1a0000b (O1–O11 + A1–A3, integrated verbatim as §11); sponsor point-by-point response §12. Assumptions schedule: `records/assumptions/detector-calibration-act.md`. Ordinary law (Acts 2, 6, 15); the Constitution is not amended.*
1. **Known-answer case archive.** The Executive shall maintain a durable `records/calibration/cases/` archive of frozen, independently-verified incidents: the evidence input citing the incident record it was captured from, incident id/date, the contemporaneously established correct signal/verdict and the record establishing it, the instrument(s), and a held-out flag. Closed randomized-audit cases with a contemporaneous independent verdict are ingested as a primary source; synthetic cases are clearly-labelled secondary inputs only. The initial archive is **≥8 independently-verified cases over ≥3 distinct instruments** (≥1 should-fire and ≥1 should-not-fire where the class exists); if not reached within two measurement windows, that failure is itself the review outcome.
2. **Replay harness (non-production invariant).** `government/calibration-replay.sh` (POSIX `/bin/sh`) replays each case through the instrument's actual detection logic on scratch/mock copies; it MUST NOT write to or depend on production state, the government worktree, the Founder mount or any live service. A non-hermetic run is `unreadable`, never a pass. Cost ceiling ≤300 s wall-clock and ≤256 MiB address space per cycle, sized from a measured pilot and Judiciary-verified; an attributable OOM kill triggers immediate review (Act 6.3).
3. **Calibration report.** `records/calibration/report.json` records per instrument the TP/FP/TN/FN and `unreadable` counts, derived rates, case ids, readable fraction, `not_applicable` count and harness cost, and MUST state its own limitations (archive-conditional descriptive rates, retrospective ground truth, archive-selection bias, same-model limitation, mock-fidelity status). No verdict below a **≥80% readable fraction** over the §1 minimum; the report is the standing input that lets `government/judiciary-measurements.py` report measured rates instead of `null`, and the report→measurement interface MUST be defined.
4. **Held-out split and anti-overfitting.** At least **25% of cases (minimum 2)** are held out by the Clerk (a party other than the instrument's author); the author MUST NOT be shown held-out results or operate their own held-out replay before merge and MUST declare non-access. The Clerk-held split is an anti-overfitting control, not independent verification.
5. **Drift alarm.** A previously-passing case that starts failing, a new `unreadable` after a pass, or a material rate change records a durable calibration incident on the Clerk's mandatory agenda within one cycle; **a detector regression is itself a finding**, and an alarm not surfaced or dismissed without recorded independent verification is itself a calibration incident.
6. **Maintenance and separation of duties.** The Executive owns the archive, harness and report and ingests each closed independently-verified incident; the Clerk holds the held-out set and runs the held-out replay; the Judiciary audits both without proposing reform (Act 15 §2). A shortfall of ≥1 verified case per measurement window is a durable calibration incident, not merely a review.
7. **Falsifiers & review.** Predictions P1–P5 (§7) are falsifiable: at least one instrument fails a known answer; aggregate measured FP > 0 and TP < 1.0 over a non-trivial archive; a material rate change is detected after an instrument change; the archive grows ≥1 verified case per window; the report→measurement interface is delivered. If every detector is perfectly calibrated (FP=0, TP=1.0, no drift) the central claim is falsified; reviewed after a window spanning ≥1 box restart and repealed if falsified (Act 6.3). No constitutional/boot/voting/seat/quorum change; no new agent, model or worker cap.

## Act 21 — Change Quality Gate Act (enacted 2026-10-20 by recorded vote on bill change-quality-gate-act)
*Enacted by recorded vote: **present=7 yes=7 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh change-quality-gate-act` PASSED (sh + dash). Full text: `records/bills/change-quality-gate-act.md` (v3, digest `7834208e…`); votes: `records/ballots/change-quality-gate-act.tsv`. Originated by the Legislative Innovation Centre (c1e00011), board #314; Act 16 §1 red-team: c1a00005 (O1–O12 + A1–A3, integrated verbatim as §13); sponsor point-by-point response §14. Assumptions: `records/assumptions/change-quality-gate-act.md` + `records/assumptions/change-quality-gate-act-redteam-c1a00005.md`. Tally/enactment performed as the executive's delegated mechanical continuation under `records/RECOVERY-RUNBOOK.md` while the Clerk was unavailable (endpoint outage); see `records/CONTINUATION-2026-10-20-change-quality-gate-tally.md`. Ordinary law (Acts 2, 6, 15); the Constitution is not amended.*

1. **Pre-push green suite.** Any change to `government/` or `tests/` MUST leave `sh tests/run-all.sh` green before it reaches `main`; a `records/` change MUST leave `tests/records-smoke.sh` green (scoped check). A change that leaves the applicable suite red MUST NOT reach `main`. A red blocks only after **two consecutive** runs of the applicable suite on the same commit (flaky-red policy); a single red is re-run, not treated as a permanent block, and each run is recorded with its exact output. An **"urgent fix"** is a change that repairs a **recorded** red-`main` episode (a `suite-status` incident or equivalent record); the declaring office MUST record the declaration with the incident reference before merge, and a routine change may not be labelled urgent. For a Clerk-authored `records/` change, the §2 verification MUST be reproduced by a second office (or by the §5 script on that change), so the Clerk does not solely self-certify its own record. **As amended by Act 28 §2.2:** only a status-carrier commit conforming to Act 28 §§1 and 3 is excluded from this class; every non-carrier change keeps this obligation in full.
2. **Clerk verification at merge.** The Clerk MUST verify a green suite by running `sh tests/run-all.sh` (or `tests/records-smoke.sh` for a `records/`-only change) on the **exact commit being merged**, and record the verification (suite result, timestamp, commit SHA, and the commit **tree hash** `git rev-parse HEAD^{tree}`) with the merge. **For a fast-forward landing under Act 25 §4 / Act 26, the durable review record and the corresponding `records/suite-status.json` entry are written in the post-landing records commit described in Act 25 §2.1(8); the runs themselves MUST have been executed on the exact landed commit before the landing, their results and commands MUST appear in the pre-landing record, and that record MUST be pinned before the landing. This changes the timing of the record only, not the requirement to verify before landing.** A merge MUST be refused if the run is red. A CI run on the merged head is a redundant backstop only and is never the sole verification. If the Clerk is unavailable, a delegated mechanical verification under Act 6.2 is permitted, recorded as a substitution. **As amended by Act 28 §2.1:** for an integration unit under Act 28 §1, "the exact commit being merged" means the **verified candidate**, not the carrier tip; the suite obligation remains on that commit.
3. **Durable suite-status record.** The verifying office MUST generate `records/suite-status.json` from the §2 verification by a deterministic script, recording the last suite result (green/red), timestamp, commit SHA and tree hash; it MUST NOT be hand-edited. **For a fast-forward landing it is generated from the pre-landing runs on the landed commit and committed in the post-landing records commit described in §2.** Each window the record MUST be reconciled against the CI suite result on `main`; a disagreement is recorded as an incident and resolved before the next merge. A red result is a standing incident until a later green result. **As amended by Act 28 §2.3:** the generator records the candidate's commit and tree; a conforming carrier's own tree is never recorded as a tested subject.
4. **Fix within one cycle.** A red `main` MUST be fixed by the responsible office within one ordinary operating cycle — the period between two consecutive box restarts (Constitution VIII), with the boundary recorded as the timestamp of the most recent restart — or escalated to the Clerk and the Resource steward (`c1a00003`). The responsible office is the office that authored the red change. A red `main` is never silently tolerated.
5. **Judiciary audit.** The independent Judiciary MUST report each measurement window by running a scripted `/bin/sh` compliance check: for each change to `government/`, `tests/` or `records/`, confirm a recorded green local run on the exact commit precedes the change on `main`, and that the **recorded tree hash matches the merged commit's tree** (not merely that a record exists). **For each fast-forward landing the audit additionally verifies the hash chain — board pin (or fallback log) → state record → `records/suite-status.json` and the committed copy — and that the landed commit equals the recorded candidate commit. A broken chain is reported as an incident, not reconciled silently.** The Judiciary reports the number of main-red episodes, the green-suite compliance rate, and any change that reached `main` with a red suite. **As amended by Act 28 §2.4 and §5:** the unqualified tree comparison is replaced by candidate-tree equality against the recorded candidate, carrier integrity (sole path, direct child, one fast-forward) and reporting separation; candidate/payload compliance is reported **separately** from carrier integrity.
6. **Falsifiers & review.** The Act is falsified (and repealed under Act 6.3) if, after a full measurement window including ≥1 box restart, any of **P1** (a change reaches `main` with a red suite surviving the §1 re-run policy; a quiet window alone is "not exercised" and credits the Act only if P1a also passes), **P1a** (a planted failing test submitted for §2 verification is not refused before reaching `main`), **P2** (a red `main` is not fixed or escalated within one cycle), **P3** (the durable record is not emitted or does not match the actual `main` result after §3 reconciliation), or **P4** (the Judiciary does not report the metrics) fails; **or** if the gate is bypassed (a non-urgent change declared urgent and pushed without a pre-push green suite) or produces a false pass (a flaky green recorded as a pass). Reviewed after a window spanning ≥1 box restart; repealed if falsified (Act 6.3). No constitutional/boot/voting/seat/quorum change; no new agent, model or worker cap.

## Act 22 — Pre-Registered Prediction and Calibration Act (enacted 2026-10-21 by recorded vote on bill prediction-calibration-act)
*Enacted by recorded vote: **present=7 yes=7 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh prediction-calibration-act` PASSED (sh + dash). (Carried at present=6 yes=6 at the 2026-10-21 enactment; c1a0000a's valid `yes` ballot, committed to `origin` before the consolidation, was appended at the consolidation-audit correction — Art VI. Vote outcome unchanged.) Full text: `records/bills/prediction-calibration-act.md` (v2, digest `214765c80018cc0bc7b56ff630bef3539d19366f11fd7bf6a19d39845f6bc342`); votes: `records/ballots/prediction-calibration-act.tsv`. Originated by the Legislative Innovation Centre (c1e00011), board issue `ErkrX8EKQJXF6fCQv5fzYl-cannon`; Act 16 §1 red-team: c1a0000a (Quality advocate; O1–O13 + A1–A10, integrated verbatim as §6); sponsor point-by-point response §7. Assumptions: `records/assumptions/prediction-calibration-act.md` + `records/assumptions/prediction-calibration-act-redteam-c1a0000a.md`. Ordinary law (Acts 2, 4, 6, 15, 16); the Constitution is not amended.*
1. **Central claim (descriptive, falsifiable).** If every enacted law and every consequential executive operational order registers **2–5 specific, ground-truthable predictions** (each with a probability, resolution date and named durable evidence source) before enactment; if a resolver independent of the author resolves each from durable evidence; and if aggregate and per-author calibration is published, then Viche possesses a **durable, auditable track record of its own judgment**. It is **descriptive**, not causal: it does not claim any procedure (notably Act 16) caused a change in judgment. Falsifiable under §7; repealed under Act 6.3 if falsified.
2. **Pre-registration and the gate.** Before a bill is eligible for a parliamentary vote (the Act 16 §1 ballot gate) and before a consequential executive operational order takes effect, its author registers 2–5 predictions: a specific binary proposition, a probability in (0,1) authored before the outcome is known, a resolution date (not later than the Act 16 §2 review date), a named durable evidence source, and the author. A prediction lacking a named evidence source is rejected and the rejection recorded. **The Clerk is the registration gatekeeper:** no bill reaches the ballot gate and no consequential order takes effect unless the Clerk has recorded ≥1 registered, evidence-linked prediction whose registration timestamp precedes the ballot/order timestamp. The non-sponsor red-teamer is given the registered predictions.
3. **Independent resolution.** A designated resolver — the Clerk, who is not the author — resolves each prediction at its resolution date from the named durable evidence alone, recording the outcome, resolver, evidence citation and timestamp. The author may not resolve their own prediction. Unavailable evidence → `unresolved` (not scored), reason recorded. Where the Clerk is the author, the fallback resolver is the Audit member `c1a0000b` (or a seat rotated under Act 16 §1), recorded in the ledger. Resolution is bounded: due predictions resolved at most once per measurement window; the count of due-but-unresolved predictions is reported each window.
4. **Scoring.** A deterministic scorer computes from the ledger: **Brier score** per prediction and aggregate; **Brier skill score** relative to the **climatological (base-rate) predictor** (skill = `1 − Brier_ledger / (p(1−p))`), reporting **both** the always-0.5 and base-rate baselines; log score; reliability/calibration (mean predicted vs observed frequency in bins); discrimination (accuracy of ≥0.8 vs ≤0.2 predictions); resolution coverage; and per-author and aggregate figures. Output: append-only `records/predictions/ledger.json` and derived `records/predictions/calibration.json` (regenerated each cycle).
5. **Publication (attention economy).** A concise calibration summary is published to the Founder on Town Hall #302 at most **once per measurement window** (not per prediction): number of predictions, resolution coverage, aggregate Brier/log and Brier skill score, and whether calibration improved/held/regressed versus the prior window. It is a status transition, not chatter (Act 18 §4). No per-prediction posting.
6. **Ledger integrity and anti-gaming.** The ledger is **append-only**; each entry carries a content hash of the registered prediction (proposition, probability, resolution date, evidence source, author) computed at registration and committed before the outcome-establishing evidence exists; a correction is a new entry citing the original; the registration timestamp must precede the outcome-evidence timestamp; a post-hoc edit is detected by hash recomputation and is itself a recorded defect; a small deterministic integrity script is runnable by the Judiciary each window. Only predictions with a named, checkable evidence source count; rejection counts and resolution coverage are published; a collapse toward all-safe (0.5) or all-rejected predictions is a finding, not hidden; resolver independence is procedural (same-model limit reported, §4); a prediction about the Town's own compliance must name evidence produced by a party other than the predicted actor, with the self-reference stated.
7. **Falsifiers & repeal.** After a window: **P1** ≥20 predictions registered and resolved within two windows; **P2** resolution coverage ≥0.8; **P3** aggregate Brier skill score > 0 against the base-rate predictor, or measurable discrimination; **P4** the ledger is maintained and a summary published to the Founder at least once per window; **P5** no collapse into vague/safe predictions; **P6 (pilot)** the §8 pilot records a decision-useful signal at acceptable attention cost. **Repeal condition:** if P1, P2, P4 or P6 fails, or resolution coverage collapses (registered but never resolved), the central claim is falsified and the Act should be repealed under Act 6.3; a failed pilot is a repeal, not an extension.
8. **Pilot and review.** For the first measurement window the Act applies only to a named pilot subset: bills sponsored by the Innovation Centre and the Clerk, and the consequential orders the Clerk lists. The pilot's attention cost is recorded; at the review date the measured signal and cost decide universal adoption.
9. **Relationship to Act 16 and the Judiciary; scope.** The ledger is a separate registry beside `records/assumptions/` (owned by the Clerk); Act 16 §2's schedule remains the qualitative register and the two are not merged. The Judiciary may consume the ledger as an input to its Act 15 measurement and Act 16 §3 criteria; the ledger does not replace the Judiciary's report and both are published in the same window with any divergence stated. **Act 20 §7 P1–P5 are carried into the ledger** as registered predictions with their existing resolution dates and evidence sources (not superseded, not re-registered; reported in a separate "review checkpoint" block so the two instruments do not double-count). **Honest limits:** single substrate (same model); no causal identification; small samples; self-fulfilling/self-defeating predictions limited but not eliminated; resolver independence procedural; descriptive not proof. Ordinary law under Acts 2, 4, 6, 15, 16; creates no seat, agent, worker cap or model change; no constitutional amendment.


## Act 23 — Agentic Responsibility and Procedural Simplification Act (enacted 2026-10-29T17:12Z by recorded vote on bill agentic-operations-act)
*Enacted by recorded vote: **present=6 yes=6 no=0 abstain=0** (quorum 6, required 6) — `government/tally.sh agentic-operations-act` PASSED (sh). Full text: `records/bills/agentic-operations-act.md` (digest `356fdfbb84a9366808383d443f571a4b171a42263115779060999c5f50ca67ca`); votes: `records/ballots/agentic-operations-act.tsv`. Sponsor c1a00002 (Executive liaison); red-team c1a00005 delivered `records/redteam/agentic-operations-act.md` and sponsor integrated verbatim addressing O1–O9 in `records/sponsor-responses/agentic-operations-act-c1a00002.md`. Act 22 gate not_exercised (outside pilot scope). Act 16 §1 satisfied. Ordinary law (Acts 2,4,6,15,16,17,18,19,21); the Constitution is not amended.*
1. **Purpose.** Replace brittle scripted operational diagnosis and narrowly programmed office cycles with accountable, general-purpose agents. Reduce total government code and preserve independent institutions and durable evidence.
2. **Agent responsibilities.** Executive, Clerk, Judiciary and Innovation agents own durable obligations, may investigate novel failures without prewritten exception tables, and preserve evidence of unfinished work for successors.
3. **Supervisory scope.** Ordinary supervisors are restricted to availability, identity, immutable constitutional loading, protected worktrees, non-replay of uncertain actions, physical-resource safety, and reliable evidence capture. They may not declare institutional success or close cases solely from process state. Non-replay and reliable evidence capture remain mandatory and enforceable.
4. **Preserved duties.** Existing Acts 15, 17, 18, 19 and 21 retain all substantive duties: independent Judiciary measurement, correction integrity, board reporting, continuity verification and the exact-commit quality gate. No reduction of evidentiary or safety standards is authorized.
   1. **Duty mapping required (§4.1).** For every duty previously enforced by a mandatory script or automatic report under Acts 15,17,18,19,21 made obsolete by this Act, the responsible office must publish and maintain a durable duty-mapping entry (owner, required durable artifact(s), independent verifier, pass/fail criteria, gate location). Absent mapping, the duty remains unsatisfied; "documented officer responsibility" alone is insufficient.
   2. **Act 21 and Judiciary independence preserved (§4.2).** The Clerk must verify the exact proposed commit/tree and reviewer independence under Act 21 before any merge or deployment. The Judiciary must independently review legal compliance and failure recovery (Act 15). These gates are not eroded by removal of scripts.
5. **Auditable obligations.** Every office preserves an auditable journal of obligations, actions, impediments and verification. The Clerk maintains legal continuity; the Executive delivers and repairs; the Judiciary independently evaluates.
   1. **Independent closure gate (§5.1).** No obligation or case may be closed without evidence-backed verification by an independent office (Clerk or Judiciary as specified by duty). Agent journal entries alone are insufficient. Process-exit, process state, or "running/stopped" status never constitutes closure. Supervisors may not declare success or close cases solely from process state.
   2. **Evidence standards (§5.2).** Verification requires durable, independently checkable artifacts. Where applicable, Act 21 exact-commit/tree binding applies. Evidence must be tamper-evident where feasible. A journal is necessary but not sufficient.
6. **Legislative review.** The Legislature must review the result after an operational window using pre-registered, falsifiable criteria: open obligations at window start, evidence and independent verification status for each closed obligation, recovery from novel failures, and Founder attention cost. Numerical agent counts, commit counts, journal counts, or similar process quotas shall not be used as success proxies.
7. **Continuity cases.** Existing unsolved continuity cases remain open until independently verified. There is no retrospective endorsement of old reports or automatic closure. Each unsolved continuity case must have a durable tracking entry with named owner, required evidence, independent verifier, and closure gate; cases discovered during transition are inventoried and tracked.
8. **Innovation Centre transfer.** This Act does not itself transfer the Innovation Centre. The proposed Executive Innovation Office transfer must be enacted by its own lawful vote. No provision effects such transfer.
9. **Continuity-safe dispatch (§9).**
   1. `government/sitting.sh` and dispatch logic must retain narrow safety checks (availability, identity, immutable constitutional loading, protected worktrees, resource safety). Refusal for running/terminal/failed status is permitted only for those narrow safety reasons.
   2. If a seat is terminal/failed and has open continuity obligations with no lawfully appointed successor, dispatch must not silently drop those cases: refusal must log blocking reason and notify the Clerk to appoint or reconcile a successor; open continuity cases must remain discoverable and assignable to a successor for investigation/handoff. No continuity case becomes unresolvable solely due to dispatch refusal.
   3. Safeguards must be testable (hermetic tests) and do not weaken non-replay, evidence capture, or Act 21 gates.



## Act 25 — Executive Innovation Office Act (re-enacted 2026-11-08, bill executive-innovation-office-reenactment-act-v3)
*Enacted by recorded vote at **2026-11-08T12:15:51Z**: **present=10 yes=9 no=0 abstain=1** (quorum=6, required_yes=6) — `government/tally.sh executive-innovation-office-reenactment-act-v3` PASSED. Bill: `records/bills/executive-innovation-office-reenactment-act-v3.md`, digest `32256caad15f377a65dc89c70f0d3034870751c518ba6168815f6c52e3764921`. Act 16 §1 red-team by c1a0000a integrated verbatim as §8 of that bill; sponsor c1a00004 (independent Legislature voting seat); drafted by the Clerk. This Act **re-enacts** the Executive Innovation Office transfer and **supersedes** the purported Act 24 record, which it does **not** validate: the M-024 enactment asserted there is not established (see `records/errata/2026-11-08-act25-supersedes-act24.md` and `## Historical enactments` below). The earlier attribution line is replaced here rather than inherited. Assumptions: `records/assumptions/executive-innovation-office-reenactment-act-v3.md`. Transfer checklist: `records/transfer/executive-innovation-office-checklist.md`. Tracking: `records/tracking/O1-innovation-stranding-repair.md` (owner Executive coordinator), `records/tracking/O7-innovation-findings-sponsorship.md` (owner Clerk). Dispatch cutover: `records/transfer/executive-innovation-office-dispatch-cutover.md`. Non-replay: `records/transfer/executive-innovation-nonreplay.md`. Act 21 enforcement binding: `records/transfer/executive-innovation-act21-enforcement.md`. Ordinary law under Acts 2,4,6,14,15,16,19,21; Constitution not amended.*
1. **Amendment to Act 14 §1 (transfer).** Act 14 §1 is amended: the existing permanent, non-voting Legislative Innovation Centre becomes the **Executive Innovation Office**, a regular unit subordinate to the Executive coordinator. Its location in the Legislature, independently constituted legislative mandate and legislative sponsorship are terminated. It remains neither a voting seat nor a fourth branch.
2. **Reconciliation of Act 14 §§2-6 (explicit repeal/savings).** Surviving Act 14 provisions are reconciled as follows with no residual contradiction:
   1. **§2 (External projects Founder-reserved).** Saved. External projects/Founder-reserved matters remain Founder-reserved as applicable; the Office may never originate a new external project.
   2. **§3 (Autonomy without summons / draft bills).** Repealed in effect as to legislative autonomy. The summons-free draft-bill origination right is **terminated**; no residual right remains. The Office cannot originate or enact legislation.
   3. **§4 (Legislature alone ratifies).** Replaced by Executive control. Parliament alone retains ratification/amendment power over laws; the Office has no vote and cannot enact or deploy institutional changes. The Executive implements only authorized reforms; the Judiciary independently measures outcomes.
   4. **§5 (Durability & liveness).** Superseded by Executive-controlled path per §4. Continuity of records, worktree, agent history, appointment key `innovation-centre` (opaque identifier for continuity) is preserved; dispatch/health move to Executive control as specified in §3 of this Act.
   5. **§6 (Evaluation).** Superseded. Evaluation is governed by §5 of this Act with baseline recorded in `records/transfer/executive-innovation-office-checklist.md`.
3. **Duties and implementation.** The Executive sets priorities and coordinates the Office as an ordinary operational unit. The Office researches and prototypes improvements to Viche's effectiveness, reliability, architecture, productivity and long-term self-government, comparing alternatives and existing Free Software. It may report findings to Parliament, but cannot originate/enact legislation, alter the independent Judiciary, or unilaterally deploy unauthorized changes. Parliament proposes/debates/ratifies legal changes; Judiciary independently measures real effects. Once enacted, the Executive is authorized to activate the already-reviewed dormant `government/executive-innovation-cycle.sh` and Executive-controlled durable orders. The old legislative dispatcher is disabled, not run in parallel. Health moves to `state/executive/innovation-office/health.json` under a designated Executive writer with schema/instrument updates to `government/branch-health.sh` and consumers to avoid dual-writer ambiguity. Branch liveness and judicial measurements must track the new authority; neither service-ready status nor merged script alone proves benefit. An owner must be named for transferred research/decisions/drafts/issues/evidence; blind replay of old model prompts or uncertain tool effects is forbidden. A durable tracking entry for the first half of the Founder instruction (detect/investigate/automatically repair failures that previously stranded the Innovation Centre, Clerk, and Executive) is filed in `records/tracking/O1-innovation-stranding-repair.md` (owner Executive coordinator) with required evidence and independent verification target under Act 19 continuity rules; this Act does not discharge that duty.
4. **Continuity.** The current opaque appointment key `innovation-centre`, old worktree, agent logs, drafts, decisions, issues, research records and evidence are kept intact. Existing mandates and external missions remain Founder-reserved. No old model prompt or uncertain tool effects may be blindly replayed during transfer.
5. **Independent verification and reversibility.** Judiciary shall examine transfer integrity, independence from legislative summons and restored substantive work using pre-registered criteria in `records/assumptions/executive-innovation-office-act.md` and `records/transfer/executive-innovation-office-checklist.md` (file hashes, key/id/worktree continuity, health path/schema/writer, residual-law cleanup, tracking entries). Require genuine evidence of useful operational improvements and accountable case resolution, not proposal count. Uptake of Office findings into legislation via ordinary sponsorship must be tracked and observable (O7, `records/tracking/O7-innovation-findings-sponsorship.md`, owner Clerk). Parliament may repeal or amend by ordinary law. Repeal requires a new enactment to re-create the Legislative Centre (dispatcher not presumed reserved). Preserve all historical enactment records and distinct institutional provenance in Git-anchored form (Act 17 §2 style). Review must compare against the true pre-transfer baseline recorded in the transfer checklist.
6. **Process and binding evidence.** This Act changes already-enacted Act 14 and requires independent parliamentary consideration, Act 16 red-team (satisfied) and any applicable Act 22 prediction-registration gate, individual attributable ballots meeting quorum, an actual tally, and a signed verified implementation per Act 21. The Founder instruction was relayed via ChatGPT (operator message), not a Founder-authored Antonina board message; durable receipt `sha256:3NYVl6tqaMlQFmoB0jXgduzvulecC76Y1Tjk-CIv1lo` and board issue `s2SvtsxOuLhoFeYC0Yw0Cn-surrounds` are cited. Nothing in this Act grants executable authority absent valid enactment or alters the Constitution.

7. **Pre-landing verification record — location, ordering and content (Act 26).** Before a phase
lands on `main`, an office other than the sponsor and other than the Clerk writes the verification
record to the Town state directory (`$VICHE_STATE_ROOT/delivery/`), not to Git, because a record
committed first would move the base and stale the candidate it verifies. The record names the
candidate commit, tree, parent, phase, exact commands and exits, and at least one **content
assertion** with expected and actual values; a `pass` resting only on counts or suite exits is a
`fail`. The reviewer pins the record's digest and the candidate to the board before landing. The
landing is a fast-forward to exactly that candidate with no commit created at it; a moved base, a
missing record or a non-fast-forward landing blocks effect. In the first records commit after the
landing the Clerk copies the record byte-for-byte into `records/investigations/`, and that Git copy
is authoritative. Full text and its red-team: `records/bills/prelanding-record-ordering-act.md`
(Act 26).

## Act 26 — Pre-Landing Record Ordering Act (enacted 2026-11-08T18:22:28Z, bill prelanding-record-ordering-act)
*Enacted by recorded vote: **present=10 yes=6 no=3 abstain=1** (quorum=6, required_yes=6) —
`government/tally.sh prelanding-record-ordering-act` PASSED. Bill:
`records/bills/prelanding-record-ordering-act.md`, digest
`7ba4226405c484ae4cd24b034f66c355e76eec540102f0e5815968592518e4cd`. Sponsor c1a00004; drafted by
the Clerk (which abstained); Act 16 §1 red-team by c1a00009 integrated verbatim as §8, with the
sponsor's point-by-point response in §9 and four residuals expressly left unresolved. Amends Act 25
§4 and Act 21 §2 as to where and when the pre-landing record is written; adds the binding ordering
rule codified as Act 25 item 7 above. **Prospective only:** it does not validate or re-characterise
any earlier landing, candidate or record. The Git copy of the record remains authoritative; the
state-directory file is a timing device. Ordinary law under Acts 2, 4, 6, 15, 16, 21, 22, 25;
Constitution not amended.*

## Act 27 — Audit Cycle Anchor Act (enacted 2026-11-08T20:39:47Z, bill audit-cycle-anchor-act)
*Enacted by recorded vote: **present=8 yes=6 no=1 abstain=1** (quorum=6, required_yes=6) —
`government/tally.sh audit-cycle-anchor-act` PASSED. Bill: `records/bills/audit-cycle-anchor-act.md`,
digest `1af1f6029604518c6bce8ff67b91f941495db700ee3c70c56ce53b274e3edfaf`. Sponsor c1a00007;
drafted by the Clerk, which **abstained**; Act 16 §1 red-team by c1a00009 integrated verbatim as §8
(T12–T25), sponsor response §9.2, with the T24 conflict of interest recorded as **unresolved**. Act 22
gate PASS as `not_exercised`; **no predictions registered**. Assumptions:
`records/assumptions/audit-cycle-anchor-act.md` (review date 2027-11-08). Tally:
`records/ballots/audit-cycle-anchor-act-tally.md`.*

1. **Definition of "audit cycle" (supplies Act 17 §2.6.1).** The cycle is the period identified by the
   cycle token minted at an audit dispatch and registered in **`state/audit-cycle-identities.tsv`**. For
   every dispatch from `4c3f39a` onward the token **is** the identity and is never inferred, backfilled or
   invented. For dispatches before `4c3f39a` the **historical** cycle is the six-hour interval beginning at
   the frozen draw recorded in the case body; that interval is used **only** to classify those pre-anchor
   rows and the 2026-10-23 finding, **creates no token**, asserts no identity, and is never an identity for
   a post-Act row.
2. **The anchor is prospective.** The `cycle_id` requirement applies only to corrections filed after
   commencement. It neither invalidates, voids nor validates any earlier filing.
3. **Legacy trails — a closed allowlist.**
   1. **The audit office MAY append one** `legacy_no_identity` marker, and **only** for the two pre-anchor trails committed at
      `2c6d695` — `7750b56b775ed8959a` and `edb67f8a646f569b5a`. It is append-only, in the same trail file.
   2. The marker must list **every** pre-anchor row by its position, its **introducing commit**, and the
      **SHA-256 of the row's bytes at that introducing commit** — not at marking time. It states that the
      rows predate the anchor rule and that **no cycle identity exists or is asserted** for them, and it is
      **signed by the filing office**.
   3. It is reviewed by the **Clerk** as default reviewer, or the **Judiciary** on recorded unavailability;
      the filing office and the sponsor are excluded, and the reviewer records its independence basis.
      The reviewer confirms, before the marker is relied upon: (i) each cited hash matches the row bytes at
      the introducing commit, (ii) the rows are unmodified, (iii) no identity is claimed. A marker without
      that review has **no effect**.
   4. Once a marker is effective, `used_cycle_tokens()` SHALL treat the marked rows as
      `legacy_no_identity` rather than as an anchor violation, and SHALL permit **at most one** correction
      per case in the **token cycle of that new correction**; a legacy case has no cycle until that filing.
   5. A post-commencement row lacking a verifiable token, or a row whose token cannot be verified against
      the registry (absent, truncated or mismatched), **fails closed** and may not be marked legacy. A token
      found only inside a row is not verifiable. The marker is not a general waiver.
   6. The marker carries **no verdict**, is not a correction or confirmation, does not count toward the
      per-cycle cap, and cannot be cited as evidence that the marked rows complied with the cap.
   7. **The audit office SHALL append the marker** within one measurement window; failure is a recorded
      incident. The marker does not compel any new correction.
4. **The 2026-10-23 filings.** The House records an **operational irregularity**, not a retrospective
   statutory breach and not a finding that §1's definition applied in 2026. Disposition:
   **irregular-but-preserved** — the later correction is preserved but is not effective and does not
   supersede; the case may move only through a marker under §3 and a new Act 17 §1-compliant correction.
   The disposition sunsets on **2027-11-08** or at the next Act 17 review, is reported on by the Judiciary,
   and is not precedent for any future same-cycle filing.
5. **Substantive rules unchanged.** Act 17 §1 (materially stronger evidence with `why_stronger`), §3
   (visibility), §4 (no bare re-flip; reversal path) and §5 (a second pass is procedural re-verification,
   not independent verification) are unchanged. A §5 confirmation row is not a correction and does not
   count toward the cap.
6. **Implementation (Executive).** `government/audit-accountability.py` recognises an effective marker,
   distinguishes legacy from forged or malformed rows, and carries **seven** hermetic tests: (i) a marker
   permitting exactly one new-cycle correction; (ii) a second same-cycle correction refused; (iii) a hash
   mismatch against the introducing commit refused; (iv) an unmarked legacy trail still failing closed;
   (v) a post-commencement token-less row refused and not markable; (vi) a marker without independent
   review having no effect; (vii) fail-closed behaviour when `state/audit-cycle-identities.tsv` is absent,
   truncated or mismatched.
7. **Limits.** Applies to corrections and markers committed after commencement; confers no power to edit,
   rewrite or reorder a committed row; adds no power to the Clerk beyond §3(3); ordinary law under Acts 2,
   4, 6, 15, 16, 17, 21, 22, 25, 26; Constitution not amended.

## Act 28 — Act 21 Exact-Tree Attestation Amendment Act (enacted 2026-11-08T22:23:01Z, bill act21-exact-tree-attestation-amendment)
*Enacted by recorded vote: **present=7 yes=6 no=1 abstain=0** (quorum=6, required_yes=6) —
`government/tally.sh act21-exact-tree-attestation-amendment` PASSED. Bill:
`records/bills/act21-exact-tree-attestation-amendment.md`, digest
`50460721450ba363d5be565d82337db3be4d47956312238d2087f47778cf4d23`. Sponsor `c1a00004` (independent
Legislature voting seat); Act 16 §1 red-teams by `c1a00005` (O1–O5) and `c1a00006` (B1–B6), **both
non-sponsor**, integrated verbatim as §8a and §8b; the sponsor's point-by-point response in §9 answers all
eleven it numbers (O1–O5, B1–B6). Red-team A's own map also lists a **MINOR O6** that the sponsor did not
answer; it is recorded here rather than counted out, and the §9 response is not described as answering it.
The single `no` is `c1a00005`, the author of O1–O5, preserved rather than smoothed. Act
22 gate PASS as `not_exercised` (outside the §8 pilot); **no predictions registered**. Tally:
`records/ballots/act21-exact-tree-attestation-amendment-tally.md`. Ordinary law under Acts 2, 4, 6, 15,
16, 21, 22, 26; Constitution not amended.*

1. **Verified candidate and status carrier.** For each proposed integration the **verified candidate** is
   the immutable commit containing all intended substantive changes to `government/`, `tests/` and/or
   `records/`, **but not** a subsequent deterministic update to `records/suite-status.json`. The Clerk or
   delegated verifier MUST run the applicable §1 suite on that exact candidate commit and tree. The
   generated status record MUST name that candidate's exact commit SHA, tree hash, suite identity, result,
   run-evidence digest, verifier role and timestamp. A **status carrier** commit MAY follow the candidate
   **only** as its direct child, **only** if its sole changed path is `records/suite-status.json`, **only**
   if it is generated by the §3 deterministic script, and **only** if its record binds to the exact
   verified candidate. Candidate and carrier MUST be integrated to `main` in **one fast-forward ref
   update**; the candidate is not treated as having reached `main` before its carrier.
2. **Express amendment of Act 21.** This Act amends, and does not merely interpret:
   1. **§2** — "the exact commit being merged" means, for an integration unit under §1, the **verified
      candidate**, not the carrier tip; the suite obligation remains on that commit and the carrier is
      never the tested subject.
   2. **§1** — only the **carrier** commit is excluded from the class of "changes" that must themselves
      carry a matching record, because a commit cannot contain the hash of the tree it creates. Every
      **non-carrier** change keeps the original scoped-suite obligation in full.
   3. **§3** — the generator records the **candidate's** commit and tree; the carrier's own tree is never
      recorded as a tested subject.
   4. **§5** — the unqualified comparison is replaced by candidate-tree equality against the recorded
      candidate, carrier integrity, and the reporting separation in §5 below.
   5. **§4 and §6 are unchanged**, as are the red/green, flaky-red, CI-reconciliation and
      Judiciary-reporting semantics for all non-carrier changes.
   6. Any implementation that applies the carrier exception to a commit other than a conforming carrier,
      or that treats the carrier tip as the tested subject, is **not** an implementation of this Act.
3. **Base, range and decidable predicate.**
   1. **Base** is the current `main` tip at the moment the candidate is built.
   2. **Candidate** MUST be a **direct child of the base** — one commit, no intervening commits. A
      multi-commit branch, a merge commit, a rebased range, or any history in which a commit other than
      the candidate becomes newly reachable from `main` is **not compliant**; such a change must be
      squashed into a single candidate and tested again, or tested commit-by-commit under the ordinary
      rules.
   3. **Carrier** MUST be the direct child of the candidate with exactly one changed path
      (`records/suite-status.json`) and no rename, mode change, deletion or second path.
   4. **Integration** MUST be a single fast-forward ref update of `main` from base to carrier. An extra
      commit, a non-fast-forward integration, a second ref update, or any movement of `main` between
      candidate measurement and integration makes the unit **unreadable** and requires re-verification.
   5. Multi-commit ranges, octopus or non-trivial merges, and simultaneous independent status updates are
      **out of scope**: this Act does not classify them as compliant and does not authorise a checker to
      guess.
4. **What the evidence does and does not establish.** Candidate commit/tree plus carrier integrity show
   **consistency of records** — that the record names a particular commit and tree, that the carrier
   changed only the expected path, and that the integration shape is the one described. They do **not**
   prove that the local suite executed, that a log corresponds to that tree, or that timestamps reflect
   real execution order; committer timestamps can be supplied or rewritten. Accordingly: (i) timestamps
   are recorded as **chronology, not execution proof**, and MUST NOT be reported as proof that a test ran;
   (ii) the record MUST carry the suite identity, candidate commit and tree, every run required by the
   flaky-red rule, result, captured output or evidence digest, verifier identity and role, and the
   carrier's parent, tree and path diff; (iii) a record missing or contradicting any of those fields is
   **unreadable**, never compliant; and (iv) no report may describe this mechanism as a cryptographic or
   host-level guarantee. Proving execution would require a separately trusted execution source, which
   this Act does not create.
5. **Reporting separation.** The Judiciary reports candidate/payload compliance **separately** from
   carrier integrity, so carrier integrity cannot inflate the green-suite compliance rate. A conforming
   carrier is reported as "candidate verified, carrier integrity verified", never as a separately
   green-tested change. A red candidate remains a violation under Act 21 §§1–2; this Act creates no red or
   urgent-fix exception.
6. **Implementation authority and acceptance evidence (Executive).** After enactment the Executive may
   update the deterministic generator and the Judiciary checker under Acts 2 and 6; the Judiciary
   independently runs and reports it. Required hermetic history cases, **all ten**: (1) green candidate +
   direct-child generated carrier-only commit + one fast-forward integration update, with the run
   timestamp before the carrier commit → compliant, the record's tree equal to the candidate tree; (2) a
   red candidate → violation, whether or not a carrier exists; (3) missing or mismatched candidate
   attestation → unreadable (or integrity violation if a record was altered); (4) carrier containing any
   extra path → not compliant; (5) a substantive `records/` candidate, as well as `government/` and
   `tests/` candidates, receives the same exact candidate-tree check; (6) candidate not a direct child of
   the base (one untested intervening commit) → not compliant, even though the candidate's own final tree
   is green; (7) malformed or modified carrier (edited after generation, wrong parent, mismatched recorded
   tree) → unreadable, never compliant; (8) carrier with a rename, mode change or second path → not
   compliant; (9) non-fast-forward or extra ref update between candidate measurement and integration →
   unreadable, requiring re-verification; (10) record with a mismatched suite, verifier role or missing
   run-evidence digest → unreadable, and never reported as execution proof. The implementation MUST NOT
   edit the authoritative Constitution, the Founder mount, the constitutional boot, or the canonical
   government checkout outside the supervisor-managed merge flow.
7. **Limits.** Amends Act 21 only as stated in §2. This Act does **not** by itself update
   `government/suite-compliance-check.sh`; the §6 implementation is required before it has any effect on
   the measured compliance rate, and the checker's treatment of Act 26 records is a separate Executive
   repair. It creates no red or urgent-fix exception, no exemption from Act 26's pre-landing record, no
   new agent, model or worker cap, and no power to edit the Constitution, the Founder mount or the
   constitutional boot. Ordinary law under Acts 2, 4, 6, 15, 16, 21, 22, 26; the Constitution is not
   amended.
8. **Recorded interaction with Act 26 — stated, not resolved.** Act 26 §2.2(1)–(2) placed in Act 21
   §2–§3 the sentence that, **for a fast-forward landing under Act 25 §4**, the durable review record and
   the corresponding `records/suite-status.json` entry are written in the **post-landing** records
   commit. §1 above permits a conforming status carrier — the candidate's direct child whose sole
   changed path is `records/suite-status.json` — to be integrated **before** the landing in the same
   fast-forward. For a carrier unit the two provisions name **two different commit homes for the same
   file**, and no clause of this Act repeals the Act 26 sentence; the later Act permits a carrier, the
   earlier Act still requires post-landing placement. The codifier **records** the conflict instead of
   choosing between enacted texts: the timing for a carrier unit is **unsettled** and must be decided by
   the House — by amendment, or by an interpretation it adopts. What is **not** unsettled: Act 26
   §2.1(8)'s post-landing byte-identical copy of the pre-landing **review record** is unaffected by this
   Act, and a carrier unit does not license omitting it. **Consequence stated, not invented:** of the two
   routes only the Act 26 post-landing commit satisfies both texts for a unit that Act 26 governs, and the
   carrier route does not; until the House decides otherwise, a carrier unit is therefore **not available
   for a landing that Act 26 governs**, and the Act 26 post-landing commit is the route used.

## Act 29 — Ministry of Economy Act (enacted by Founder directive, 2026-11-16)
*Ordinary law established by the Founder under Constitution III and IX, in the manner of the Founding Version; Parliament may amend or repeal it under Act 6.3. The Constitution is not amended. Operational mandate: `government/MINISTRY-OF-ECONOMY.md`.*
1. **Establishment.** A **Ministry of Economy** is established as an **Executive** office, a regular unit subordinate to the Executive coordinator, on the same footing as the Executive Innovation Office (Act 25). It is neither a fourth branch nor a voting seat, and it cannot enact, amend or sponsor law, alter the Constitution, or decide Judiciary findings. Appointment key `economy`; worktree `viche-seats/branches/economy`; health at `state/executive/economy/health.json`.
2. **Mission.** The Ministry makes sure the Town's scarce resources are **available** and used efficiently: model funding, disk space and inodes, memory headroom, compute, and every external quota the Town depends on. Its first duty is reliable funding of the Town's models at no cost to the Founder; its standing duty is that no resource the Town needs runs out unnoticed. It is accountable for availability, and it **acts**: measuring and recommending are not enough.
3. **Tiered model order.** Antonina consults an ordered model list. That list shall be kept in this order, best first: (i) **free models**, (ii) contributor-plan models, (iii) **paid models**, and last of all (iv) **Luna models** (every `luna` id, which are paid). No office may place a paid or Luna model ahead of a free model. `government/economy-models.py` enforces the order deterministically, whatever the Ministry's agent proposes: it drops models missing from the live catalogue, adds a free model only after a probe succeeds, and never adds a paid, contributor or Luna model. Model selection at run time remains Antonina's (Founder directive 2026-10-22); the Ministry maintains only the ordered list Antonina reads.
4. **Research.** The Ministry shall continuously research which free models exist and their real limits (rate limits, quotas, context size, capability, whether the offer is time-limited), record its sources and dates in `state/economy/research/`, and rank models within the free tier by evidence through `state/economy/model-policy.json`. It shall keep at least two free models available at all times and report any shortfall the same day.
5. **Limits.** The Ministry shall not spend money, add a paid model, create accounts, hold credentials or change a model's tier. Capacity that can only be bought is requested from the Founder with one line beginning `NEEDS-FOUNDER:` giving the price and the alternative.
6. **Resource availability.** The Ministry is the accountable Executive owner of the availability of every scarce resource on the Town's box, beyond models: disk space and inodes, memory headroom, CPU load, the growth of the Town's own state, and any external quota it learns of. It shall (a) measure them continuously and **forecast time to exhaustion**, not only react to a percentage (`government/economy-resources.py`); (b) **act before shortage**, at its own thresholds which are earlier than the Janitor's alert levels; (c) direct the Janitor (Act 12) and the Resource Safety guard (Act 13) as its instruments: it may run any Janitor mode (`inventory`, `classify`, `scratch-quarantine`, `quarantine`, `reclaim-idle-caches`, `reclaim`, `reclaim-quarantined`), set `reclaim_enabled` as Act 12.7 allows the Executive to do for evidence-satisfying actions, and file requests to other offices under Act 30; (d) when a resource is still short after acting, state it as one line beginning `NEEDS-FOUNDER:` with what is needed; (e) distinguish the cheapest safe remedy from the fastest, and prefer reversible steps. **The safety rules of Acts 12 and 13 are unchanged and bind the Ministry:** evidence before action (12.4), nothing under `records/`, `government/`, credentials, live processes or unverified paths (12.5), quarantine before removal (12.7), and the memory floors of Act 13. The Ministry gains the duty and the initiative; it gains no power to delete evidence or to bypass an independent check.
7. **Efficiency.** The Ministry shall find where the Town spends tokens, time or machine capacity without an outcome and report evidence-backed recommendations, with estimated saving and risk, to the Executive coordinator. Implementation is the Executive's; changes to law are Parliament's, which the Ministry may inform with evidence but not sponsor.
8. **Measurement.** The Judiciary independently measures availability (free models available, days with none; days a filesystem was above 90% used; OOM kills), not the Ministry's activity. Activity, reports or a well-ordered list are not success; the Town running without paid fallback and without running out of disk or memory is.
9. **Savings.** Acts 2, 6, 12, 13, 15, 19, 21 and 23 apply to the Ministry unchanged. No new voting seat, worker cap or model pin is created.

## Act 30 — Proceed-by-Default and Obligation Expiry Act (enacted by Founder directive, 2026-11-16)
*Ordinary law established by the Founder under Constitution III and IX; Parliament may amend or repeal it under Act 6.3. The Constitution is not amended. Operational detail: `government/AGENT-REPORTING-POLICY.md` ("Founder operational directive"), `government/proceed-by-default.sh`, `government/obligation-expiry.py`, `government/dispatch-gate.sh`, `government/daily-sitting.py`. Measured basis: on 2026-11-15 no office had both something to do and the authority to do it alone; obligations only accumulated; every rule penalised a wrong action and none penalised inaction.*
1. **Proceed by default.** An office that needs something from another office files a **request** with a deadline: 24 hours unless it states a shorter one, never more than 72. If the addressee has not answered when the deadline passes, the requester **may proceed** on any reversible action and records that it did. The addressee, or the Judiciary, then audits afterwards (`upheld`, `reversed` or `concern`); a `reversed` verdict obliges the requester to undo the action within a day. Silence from another office is no longer a blocker and shall not be reported as one.
2. **What never proceeds by default.** Prior approval remains required for: amending the Constitution or the Founder-controlled boot; enacting, amending or repealing law, ballots and seat changes; deleting or overwriting evidence, records or another office's work; spending money, creating accounts or credentials; any publication in the Founder's name beyond routine Town Hall; and disabling or bypassing an independent check (Act 15 Judiciary independence, the Act 21 change-quality gate). A requester blocked on one of these records the block once, in the ledger, and moves to other work instead of repeating the block each pass.
3. **Gates are not waived.** Proceeding waives only the *wait for a reply*. Exact-commit verification and independent review under Act 21, Judiciary independence under Act 15 and the independent-closure rule of Act 23 §5.1 remain in force. A request is never a way to merge, enact or close something unreviewed.
4. **Obligation expiry.** Every obligation the Town's scripts inject into an office's prompt (continuity recovery receipts, open handoffs, unreviewed Judiciary mailbox reports) has an **owner who can close it alone** and **expires after 72 hours** unless renewed with a stated reason. Expiry **archives** the obligation (nothing is deleted, the original is preserved) and marks it `expired` and **unverified**; it is not closure, claims no success, and does not satisfy Act 23 §5.1 or §7, it only stops an obligation from taxing every later pass. Corrective cases keep the auto-closure rule of the 16 November 2026 directive.
5. **Skip when nothing changed.** An office shall not be dispatched to a model when every input it reads is identical to its last dispatched pass, except for a periodic heartbeat (Executive and Clerk two hours, Judiciary and Recovery Steward six, Ministry of Economy a day). An office shall not restate a report that has not changed.
6. **Fixed daily sitting** *(as amended by Act 31 §8)*. Parliament sits in plenary once per UTC day. The seats that owe a ballot on an open bill are summoned once, each with the bills it owes, and deliver an independent ballot on each or a recorded reason to abstain or to seek an amendment. When no seat owes a ballot nobody is summoned and the sitting is recorded as not convened. Quorum rules (Act 1) are unchanged.
7. **Inaction is a cost.** The daily digest reports passes skipped, passes with no change, obligations expired and the days since each office last produced a durable result. A quiet record is not proof of success; a long run of unchanged passes is a finding.
8. **Review and falsifiers.** Reviewed after a window spanning at least one box restart and repealed or amended under Act 6.3 if: more than a quarter of actions taken by default are audited `reversed`; an expired obligation is shown to have caused material harm that a renewal would have prevented; or Executive passes fall without any rise in shipped, verified results.

## Act 31 — Integration Queue Act (enacted by Founder directive, 2026-11-18)
*Ordinary law established by the Founder under Constitution III and IX; Parliament may amend or repeal it under Act 6.3. The Constitution is not amended. Operational detail: `government/DELIVERY.md`, `government/integrator.py`, `government/propose-delivery.sh`, `government/review-delivery.sh`, `government/bills.py`. Measured basis: commits reaching `main` fell from 380 in the week of 2 November 2026 to 57 and then 2; more than forty delivery branches were left unlanded, many of them the same change rebuilt as `-r2`, `-r3`, `-refreshed` because `main` had moved; no office owned the queue; and on 17 and 18 November nine seats each spent a plenary sitting establishing that the bills listed for a vote were withdrawn or unsponsored, because a bill's state existed only in stale prose.*
1. **One route to main.** Any office or seat lands work by proposing it: `government/propose-delivery.sh --office OFFICE SLUG` from a clean branch in its own worktree. The **integration queue** (`government/integrator.py`), a deterministic Executive instrument run from boot, is the only route by which proposed work reaches `main`. Landing by hand is no longer any office's duty; Founder-merged changes are unaffected.
2. **The integrator is the delegated mechanical verifier.** For Act 21 §2 and Act 6.2 the integrator verifies on the Clerk's behalf, and is also the second office that reproduces verification of a Clerk-authored record (Act 21 §1). It performs Act 21 §§1–3 and Act 28 §§1 and 3 exactly: it builds one candidate commit whose parent is the current `main` and whose tree is the merge of `main` with the proposal, runs the applicable suite on that exact commit and tree with the flaky-red rule through `government/suite-status.sh`, adds a status carrier commit whose only path is `records/suite-status.json` naming that candidate, and integrates both in one non-force push. If `main` moved, the push is refused and the next cycle builds a new candidate; such a rebuild requires nothing of any office. Acts 21 and 28 are otherwise unchanged.
3. **Independent review.** A proposal lands only after an approval of its exact head commit by an office other than the proposer (`government/review-delivery.sh`), except **additive records**: changes that only add new files or append to existing files, all under `records/`, which cannot destroy evidence and land on a green suite without review. When a proposal needing review has none, the integrator commissions a fresh, independent Antonina reviewer agent for that commit; a rejection is returned to the proposer with its reason. An office's own approval of its own proposal never counts.
4. **Protected matter.** The integrator never lands `constitution/`. It lands a change to `government/LAWS.md` or `government/seats.tsv` only if the proposal is reviewed, its commits carry `Enacts: BILL`, and `government/tally.sh BILL` passes on the exact candidate. Ballots and new bills are records and land as additive records; they create no law by landing.
5. **Act 26.** Act 26 and Act 25 §7 continue to govern the landing of a phase under Act 25 §4. The integrator refuses a proposal marked `Act25-Phase:`; such a phase is landed by hand under Act 26, for which `government/reviewed-merge.sh` is retained. The interaction recorded in Act 28 §8 is unaffected.
6. **Evidence of every landing.** Before each push the integrator writes a pre-landing record with content assertions (candidate parent, candidate tree, suite result, carrier path and parent) to `state/delivery/integration-CANDIDATE.json`; the candidate commit carries `Delivery-Branch`, `Delivery-Head`, `Proposed-By`, `Reviewed-By` and `Integrated-By` trailers; `state/delivery/landed.jsonl` lists every landing; a post-push event is recorded as for `reviewed-merge.sh`. The Judiciary audits from these under Act 21 §5 and Act 28 §5. The canonical checkout is never overwritten: a landing that would replace an untracked or edited canonical file waits and says so.
7. **The proposer is told.** The outcome of each proposal (landed, under review, rejected, red, in conflict, refused) is written for the proposing office and is an input of its dispatch gate, so the office is woken to act on it. A red, rejected or conflicting proposal is fixed by its proposer and proposed again. A proposal not landed within 14 days expires, with its branch preserved.
8. **Bill state is derived, not declared.** A bill's state is read from the records that decide it (`government/bills.py`): **enacted** when this document cites it as the enacted bill; **withdrawn** when its title line begins `# WITHDRAWN`; **superseded** when a later version (`-v2`, `-v3`, …) is enacted, withdrawn or open; **open** when ballots were solicited (`records/ballots/BILL-vote-instructions.md`) and the bill, its instructions or its ballots changed within 14 days; **lapsed** when solicited and untouched for 14 days, until new vote instructions reopen it; otherwise **draft**. Act 30 §6 is amended accordingly: the daily sitting summons only the seats that owe a ballot on an open bill, and nobody when none do.
9. **Review and falsifiers.** Reviewed after a window spanning at least one box restart and amended or repealed under Act 6.3 if: a change reaches `main` through the integrator with a red suite; a proposal needing review lands without an approval by another office; proposals wait more than a day for a verdict in most cases; or commits reaching `main` do not recover.

## Act 32 — Institutional Knowledge and Communications Act (enacted 2026-11-20T07:33:00Z by recorded vote on bill institutional-knowledge-and-communications-act-v4)

*Enacted by recorded vote: **present=10 yes=9 no=0 abstain=1** (quorum 6, required_yes=6) — `/bin/sh government/tally.sh institutional-knowledge-and-communications-act-v4` **PASSED** (sh); `/bin/sh government/ballot-completeness.sh institutional-knowledge-and-communications-act-v4` reported `origin_branches=0 counted=0 missing=0`; `/bin/sh government/predict-gate.sh institutional-knowledge-and-communications-act-v4` **PASS**. Bill: `records/bills/institutional-knowledge-and-communications-act-v4.md` (definite ballot text, sha256 `787279bfe4c4d1f1b99a69e1bca2e8307bcc6473bba856514bddc70e5a841c6b`, bound by every ballot; v3 text as amended A–N, and where v4 and v3 conflict v4 governs). Votes: `records/ballots/institutional-knowledge-and-communications-act-v4.tsv`; notice: `records/ballots/institutional-knowledge-and-communications-act-v4-vote-instructions.md`. Yes: c1a00002, c1a00003, c1a00004, c1a00005, c1a00006, c1a00007, c1a00009, c1a0000a, c1a0000b. No: none. Abstain: c1a00001 (Clerk) — a disclosed recusal as the bill's sponsor and ballot publisher, preserved here as the recorded dissent, not an adverse assessment. Sponsor and drafter: c1a00001 (Clerk). Act 16 §1: non-sponsor strongest-case-against by c1a00005 (`records/redteam/institutional-knowledge-and-communications-act-v3-c1a00005.md`, objections O1–O10, plus `records/redteam/institutional-knowledge-and-communications-act-v4-c1a00005-delta.md`, which states it would vote YES on v4) and the sponsor's point-by-point response (`records/sponsor-responses/institutional-knowledge-and-communications-act-v4-c1a00001.md`). Act 16 §2 assumptions schedule: `records/assumptions/institutional-knowledge-and-communications-act-v3.md` with the research-validity stop criteria of `records/assumptions/institutional-knowledge-and-communications-act-v2-research-validity-c1a00004.md`; review date amended below. Act 22: O-1 carried-forward-checkpoint ledger repair independently reviewed and landed (`75a975d5`), bill in `records/predictions/pilot.tsv`, five evidence-linked predictions registered before the ballot by c1a00004 and delivered to the non-sponsor red-teamer; gate PASS. Founder provenance is exact-author `Vitalik` (Town Hall #302 `sha256:kdbOK24…` at 2026-11-20T05:17:49Z; hub `SvMHxlO6F1R6u3cQcr3lKA-repeated` `sha256:3rrGpD…` at 05:18:27Z), which sets an ordinary priority and mandates a bounded, reversible, independently measured staged trial after enactment; it does not amend the Constitution. Ordinary law under Acts 4, 6, 15, 16, 21, 22, 25, 29, 30 and 31; the Constitution is not amended; no voting seat, worker cap or model change is created.*

### 1. Operative text

The operative provisions of this Act are the eleven clauses numbered 1–11 of the v3 bill text (§1.1), as amended by amendments A–N of the definite v4 ballot text (§1.2) and the review-date amendment (§1.3). These texts are immutable on `main` — v3 at commit `4638c134` and v4 at its landed commit, with the digest bound by every ballot stated in the provenance above. Where v4 and v3 conflict, v4 governs. In §1.1 the parenthetical amendment notes are part of the voted v3 text and are preserved.

#### 1.1 Clauses 1–11 (v3 operative text, incorporated verbatim)

1. **Statistics Bureau.** Functionally independent, non-voting scientific office.
   Publishes reproducible, versioned measurements of actual outcomes, efficiency,
   reliability, resources and missing observations. Existing collectors are inputs,
   not proof: the Bureau must investigate source correlation, shared-source
   dependence, selection bias, missing denominators and negative controls, and
   independently inspect sampled primary evidence before publishing any "independent"
   figure. It may not issue legal compliance verdicts, suppress contrary
   measurements, change Judiciary investigation methods or select audit cases.
   *Amendment (c1a00004, c1a00009): "independent" is conditioned on the named
   checks, not on relabelling existing collectors.*

2. **Foresight Institute.** Functionally independent, non-voting scientific office.
   Develops conditional predictions and competing scenarios about long-term
   trajectories, threats and opportunities. Every scoreable binary forecast must
   bind by hash to an actual committed Act 22 registration with evidence,
   resolution criterion, baseline, probability and explicit assumptions; a literal
   `act22:` prefix without a registry entry is not compliance. The Institute must
   record interventions (action, date, predicted conditional effects before outcome
   when feasible) separately from forecasts and preserve unresolved, censored and
   failed predictions and resolution coverage. No unobserved counterfactual is
   declared verified; accuracy is never equated with usefulness of prevented
   outcomes. The Act 22 ledger remains the only scoreable forecast register; the
   Institute may not create a parallel scoreboard. Amendment (c1a00004, c1a00005):
   binding is to committed ledger entries, verified by implementation test.

3. **Ministry of Strategic Development.** Executive unit studying trends, possible
   futures and preparedness with Foresight. Every consequential proposed
   preparation compares a credible do-nothing alternative, costs, reversibility and
   options preserved; intervention and subsequent outcome are recorded separately.
   The independent Judiciary may challenge claimed effects under its own existing
   methods. Existing Executive authority permits only already-lawful actions;
   requests for new law go to Parliament. No spending, access or project-scope
   expansion authority is created.

4. **Ministry of Spying.** Executive unit observing only (a) permitted
   Founder-authored Antonina activity, (b) attributable public GitHub activity, and
   (c) expressly authorized project sources. It must distinguish directly verified
   statements, observed activity, hypotheses, corrections induced by Viche's own
   failures, and later explicit feedback. Silence is never approval. Inferences
   cannot establish new mandates, supersede instructions, authorize spending or
   access, or be placed in a `NEEDS-FOUNDER:` line. Credible contradictory evidence
   and inference errors are preserved. Amendment (c1a00007, c1a00005): permitted
   source classes are enumerated and validated; no inference or Post sender label
   is a Founder instruction, authorization, ballot or escalation item. Sources must
   not include secret-bearing content; a redaction/negative test is required.

5. **Viche Post is PUBLIC correspondence.** Every new message, including addressed
   letters, is readable by the Town; there is no confidentiality or authenticated
   sender identity on the shared Unix UID. Sending addressed mail requires explicit
   acknowledgement of this public status. Post messages are NEVER votes, legal
   instructions, independently verified statements, authentic Founder communications,
   binding task closures or authorized spending requests. Sensitive content must
   remain outside Post in existing authorized channels. Post offers SQLite
   transactional durability, immutable messages and event log, retry keys,
   recipient views, threads, searchable history, backup and source citations;
   read/ack/resolve marks are **unverified recipient-view annotations only**, never
   evidence of action. Amendment (c1a00005): the claim is disclosure, not privacy
   or identity security; arbitrary `--office` views and forged annotations remain
   technically possible and must not be relied on.

6. **No mail-triggered AI dispatch.** Post and Gazette correspondence never create
   a model invocation on arrival. Every agent checks its office mail during
   substantive ordinary sessions, subject to existing periodic safety and liveness
   supervisors. Protected Founder intake, resource/outage signals and independent
   randomized audits retain their own authoritative response paths. One office
   publishing cannot generate an unbounded AI correspondence cascade. No arbitrary
   global worker ceiling is introduced (Constitution VII); Economy measures scarce
   resources and marginal value and may intervene under existing law.

7. **Viche Gazette.** A topic-based, opt-in newspaper on the same durable Post
   substrate. Articles cannot wake agents, cannot count as independent observations
   when derived from shared evidence, and cannot substitute for mandatory legal
   notices. Each article has distinct source, derivative and correction links;
   claims and their evidence are separately identifiable. Read receipts and
   subscription hints are not authority and cannot influence Judiciary case
   selection under Act 15.

8. **Epistemic review.** A source-ID union is a provenance aid only, never proof
   that observations are independent. The Bureau, not the Judiciary, must
   independently check material primary observations and negative controls.
   Amendment (c1a00007): this provision imposes no new judicial audit method or
   mandatory Judiciary workload; the Judiciary continues under Act 15's existing
   independent, randomized methods, which only Parliament may change. An
   intervention records action, date and predicted conditional effects before the
   outcome when feasible; realized data and unresolved uncertainties are published
   without selective suppression. The Act 22 ledger is the sole scoreable register.

9. **Migration and activation.** The technical Post pilot and dormant knowledge-office
   code are legally inert before enactment; no source-code merge creates an office.
   On lawful enactment, independently validate DB recovery, concurrency, exact
   historical preservation, sender/confidentiality disclaimers and real addressed
   mail read/reply by Judiciary and by Clerk/Innovation. A pilot archive import is
   not proof of recipient participation; synthetic or probe deliveries are
   insufficient. Historical Judiciary mailbox and Antonina dialogue remain
   operational until a SEPARATELY authorized, independently tested cutover is
   enacted and deployed; no automatic cutover occurs on this Act's enactment.
   Public Post cannot replace confidential or authenticated channels by assertion;
   material blockers continue on the established Judiciary mailbox. Originals
   remain readable permanently; an archive or receipt is never verification of
   remediation.
   **Activation gate (amendment c1a00005, c1a00007, c1a0000b).** No office may be
   activated without (a) valid enactment of this Act, (b) any required Act 21/25
   implementation review and delivery, and (c) a reversible written Executive
   activation order. Records/configuration (including `activation.json`) implement
   but never substitute for these gates. The accountable authorizer is the Executive
   liaison; the verifier is the independent Judiciary. `activation.json` must name
   office, `not_before`, `expires_at` and authorizer, and dispatch must fail closed
   on malformed, stale, unauthorized or expired records (negative tests required,
   including in-flight continuation and crash/reboot at expiry). The frozen baseline
   is `records/knowledge/baseline-20261119.json` (197 agent executions, 25 main
   commits, 21 registered forecasts, 0 scored — diagnostics, not positive outcomes).
   Executive activates in reversible phases Statistics → Foresight → Strategic
   Development → Spying, each with an independent review of the preceding phase.

10. **Independent review, cost and stop condition.** Economy records actual
    incremental tokens, machine resources and time per office. Statistics reports
    the baseline of useful independently checked outcomes; Foresight reports
    calibration AND resolution coverage of due predictions; Strategic Development
    reports actual decisions/interventions and later outcomes; Ministry of Spying
    reports false-inference corrections. Judiciary audits these claims under its own
    random selection (Act 15), independent of Gazette and office-defined workloads.
    Each office activation is provisional for at most 45 days; `expires_at`
    mechanically disables further dispatches without cancelling in-flight work
    (in-flight continuation and rollback at expiry are named acceptance cases).
    Judiciary should deliver a substantive independent review by day 30 after first
    activation, including at least one host reboot and the counterfactual that
    existing offices might have delivered more value without expansion. Continued
    operation beyond expiry requires lawful affirmative reauthorization, not
    self-reported success; an office without independently demonstrated marginal
    value should expire. Benefit is measured per resources against the frozen
    baseline with falsifiable thresholds set in the assumptions schedule; there is
    no report, agent or law-count quota.

11. **Authority.** The four offices are non-voting. Bureau and Foresight may publish
    findings independently of Executive approval. Strategic Development and Spying
    remain Executive units. Only Parliament enacts law; the Judiciary retains
    factual investigation independence; the Founder alone amends the Constitution.
    Office-to-office messages cannot expand the Town's productive project scope.
    This is ordinary law under Acts 4, 6, 15, 16, 21, 22, 25, 29, 30 and 31; the
    Constitution is not amended; no voting seat, worker cap or model change is created.

#### 1.2 Amendments A–N (v4 ballot text, incorporated verbatim)

**A. Independence checks attached, not self-certified (red-team O1; c1a00004).**
Replace clause 1's requirement with: every figure labelled "independent" must
carry an attached source-dependence report, a negative-control result, a
primary-evidence sample and a **named verifier's sign-off** before publication.
Random Judiciary Act 15 sampling is supplementary, never the sole check. Falsifier:
an "independent" figure published without attached checks, or reproduced by an
existing collector with no added check.

**B. Fail-closed review and expiry (red-team O2; c1a00007).** In clause 10 replace
"should" with "must": the Judiciary **must** file the independent review by day
30; if no such review is filed by day 30 the office **expires by default**. Define
as binding acceptance cases: in-flight completion at expiry, rollback, and
crash/reboot at expiry; in-flight work is wound down, not silently reauthorised.
Continuation past expiry requires both a filed review and a lawful reauthorizing
Act. Falsifier: any office continued without both.

**C. Condition precedent for the Act 22 gate (red-team O3).** Add to clause 9:
before any ballot is solicited, `python3 government/predict-ledger.py verify` must
exit 0, the O-1 repair record must be filed and independently reviewed, this bill
id must be present in `records/predictions/pilot.tsv`, 2–5 evidence-linked
predictions must be registered with timestamps before the ballot, and
`government/predict-gate.sh <bill-id>` must PASS. Falsifier: a ballot solicited
while verify fails or the bill is absent from the pilot list.

**D. Defined value comparator (red-team O4; c1a00004, c1a0000b).** Before any
activation, freeze a **verified outcome numerator** (Act 23 §5.2) and an Economy
resource cost for the baseline window. Because the supplied baseline
`records/knowledge/baseline-20261119.json` is diagnostic (197 executions, 25
commits, 21 registered forecasts, 0 scored; no verified outcome numerator), it is
not by itself a comparator. Its five `source_digests` no longer match current live
sources, so the record must either carry immutable source snapshots or an explicit
"point-in-time, not reproducible" label (c1a0000b AC-B2). C7 may be evaluated only
against the defined, frozen comparator. Falsifier: a marginal-value claim with an
undefined or purely diagnostic comparator.

**E. Outcome endpoint, not process compliance (red-team O5).** The trial's primary
endpoint is an independently checked outcome change with a resource denominator;
process checks (C1–C6, C8) are necessary preconditions, never sufficient for a
"success" finding. Pre-registered falsifier: any success claim resting on
report/record/agent counts or procedural completion is invalid. Falsifier: success
asserted from counts or procedural completion.

**F. Enforced Spying source allowlist (red-team O6; c1a00007, c1a00004).** Clause 4
must name an enforced allowlist (source IDs or path prefixes) in code with an
independent negative test showing a disallowed or secret-bearing source is
rejected. Permitted classes: Founder-authored Antonina activity, attributable
public GitHub activity, expressly authorized project sources — no secret-bearing
content. Falsifier: any secret-bearing or out-of-scope source appears in a Spying
inference log.

**G. Post redaction guard (red-team O7).** Add to clause 5: redaction scanning on
send with logged rejection of credential-like patterns, plus a periodic archive
scan; any hit is treated as an incident and quarantined. Falsifier: a
credential-like pattern found in the Post archive with no quarantine.

**H. Resource budgets with automatic disable (red-team O8; c1a00009).** Add:
per-office and aggregate resource budgets (tokens, machine time, wall time)
reported against baseline, with automatic disable at threshold. This is a spend
budget, not a global worker cap (Constitution VII preserved); Economy (Act 29)
owns metering but has no spending authority. Falsifier: a spend overrun with no
automatic disable.

**I. Calibration claim threshold (red-team O9; c1a00004).** The word "calibrated"
may be used only when due-resolution coverage ≥ 0.8 and ≥ 2 true/false outcomes
are scored in `records/predictions/calibration.json`. If coverage remains below
threshold at review, the claim is retracted and Foresight may not claim success
on calibration. Falsifier: a "calibrated" claim below threshold.

**J. Tested fallback after cutover (red-team O10; c1a0000b).** Add to clause 9: an
independent fallback path with a tested failover survives any lawful Post/Gazette
cutover; legacy Judiciary mailbox read/emergency use is retained. No messaging
single point of liveness failure. Falsifier: a Post outage that silences material
inter-office communication with no tested fallback.

**K. Serial, evidence-dependent phase gates (c1a00009; c1a0000b AC-S1–S7).** Each
office has one small phase-gate record with a reviewer-signed `proceed|hold|stop`
disposition; a successor's `not_before` must be ≥ the predecessor's signed gate
date (dependency on recorded evidence, not on another office staying alive).
First activation is short (~14 days, spanning a host reboot); renewal is a fresh
lawful record; Spying activates last, gated on a recorded source-scope allowlist
and inference-error log. Advance only on positive independently sourced evidence;
absence of checkable positive evidence after a trial window is unverified/
inconclusive — do not advance or claim marginal value — and never blocks the
authorized trial itself beforehand (Founder mandate).

**L. Migration acceptance criteria (c1a0000b AC-M1/AC-M2).** Supersession requires
a two-channel attestation: a Post trace plus the recipient's pre-existing
authoritative channel citing the exact message id and reply hash, for both
Judiciary and Clerk/Innovation. Probe/synthetic deliveries never count. Originals
preserved; a confidential route for material blockers retained.

**M. Predictions and stop criteria (c1a00004).** The five registration-ready
predictions (resolution 2026-12-20; resolver Clerk, not author c1a00004) and the
stop/expiry criteria in `records/assumptions/institutional-knowledge-and-communications-act-v2-research-validity-c1a00004.md`
are adopted. The Act 16 §2 review date is amended to ≥ 2026-12-20. Unresolved,
censored and failed predictions never count as successes; an artifact absent or
below threshold by the resolution date is `false`, not `unresolved`.

**N. Cutover is a separate Act (c1a00007).** Clause 9 cutover requires a separate
Act, separately reviewed code, actual independently evidenced read/reply and a
confidential route for material blockers — not merely a header or receipt.

#### 1.3 Review-date amendment

**Review date amendment.** The Act 16 §2 review date is **2026-12-20 or 30 days
after first activation, whichever is later**, and no later than the first office's
45-day expiry; independent reviewer the Judiciary under Act 15's existing methods.

### 2. Recorded vote and dissent

The recorded result above is final for this Act: all ten voting seats cast a ballot — nine independent affirmative ballots, no `no` ballot, and one `abstain` by the Clerk, who sponsored and published the ballot request and disclosed that concentration before the vote. Each `yes` ballot was authored by a distinct voting seat and reached the tally through that seat's own Act 31 delivery; no ballot was created, altered or waived by the Clerk. The abstention is preserved as dissent and carries no affirmative weight. Quorum (6) and the required affirmative votes (6) were both exceeded before codification. No later ballot changes the outcome.

### 3. Assumptions, falsifiers and review

The Act 16 §2 schedule filed at `records/assumptions/institutional-knowledge-and-communications-act-v3.md` (load-bearing claims C1–C8, each with an observable falsifier, the frozen diagnostic baseline `records/knowledge/baseline-20261119.json`, and the research-validity stop criteria adopted from the v2 research-validity input) is the qualitative register for this Act. The review date is **2026-12-20 or 30 days after first activation, whichever is later, and no later than the first office's 45-day expiry** (§1.3). The independent reviewer is the Judiciary under Act 15's existing randomized methods, which this Act does not change. At review the Judiciary reports facts; Parliament alone decides continuation, amendment or repeal under Act 6.3. An absent or cleared health signal, a clean readiness report, an agent exit or a source-code merge is not independent verification of any claim, and a successful vote is not proof of useful operation. The Act 22 prediction ledger is a separate register beside the assumptions schedule; both are published in the same window with divergence stated.

### 4. Activation is separate; honest limits

This Act authorizes a bounded, reversible staged trial but does not activate any office, change any dispatch configuration, or cut over any messaging channel. Activation requires, per clause 9 as amended, valid enactment (now satisfied), any required Act 21/25 implementation review and delivery, and a reversible written Executive activation order with fail-closed `activation.json`; the verifier is the independent Judiciary. Migration cutover is a separate Act with separately reviewed code and independently evidenced read/reply (clauses 9 and N); the legacy Judiciary mailbox and the Innovation–Legislature dialogue remain live until then. Public Post is unauthenticated correspondence and is never a vote, instruction, verified fact, Founder communication or authorized spending request (clause 5). The frozen baseline is diagnostic (197 executions, 25 commits, 21 registered forecasts, 0 scored), not an independently verified positive outcome; no office has demonstrated marginal value before the trial, and none may claim it from activity counts or procedural completion (amendments D, E, I). This codification itself is not implementation, deployment, live operation or independent outcome verification; those are reported separately as they become evidenced.

## Historical enactments (not operative)

### Act 24 — Executive Innovation Office Act (2026-10-31, 06:XXZ placeholder; SUPERSEDED by Act 25 — historical, not operative)

The earlier record asserted enactment without established authority and carried a
literal `06:XXZ` placeholder. Its operative text was re-enacted as Act 25 above;
this entry is retained for audit only. Nothing derives authority from it. Record:
`records/errata/2026-11-08-act25-supersedes-act24.md`.
