# Institutional oversight: detection, inquiry, and correction

## Authority and separation

This implementation executes **existing** Founding Acts 4 (independent audit), 5 (durability), 8 (quality, timeliness, Founder attention) and the latest Founder-authorized productive mandate. It does not amend the Constitution or enact new legislation. Parliament can revise it by ordinary law.

- **Watchdog** (`government/oversight-watch.sh`): deterministic, invoked each ten-minute government reconciliation, independent of the Clerk, executive, Auditor, and model provider. Writes readable, durable observations and a current incident into the host's persistent Viche state. Does not edit Git working trees, close board issues, or judge wrongdoing.
- **Independent Auditor** (`government/audit-cycle.sh`): autonomously dispatched for an open incident or a periodic bounded four-case random sample when the provider permits; retains its own seat and independent Antonina session. Must verify actual outcomes and investigate measurement blind spots, not rely on executive self-reports.
- **Clerk/Parliament** (`government/sitting.sh`): receive active oversight incidents **as mandatory agenda items**, independently of Founder communications. The Clerk coordinates evidence and parliamentary remedies, not executive task selection.
- **Executive**: remains independent, accountable to outcomes, and can correct operational shortcomings under existing law without parliamentary ceremony.

## Measured signs (not performance quotas)

First-page open Kawun issue count is a **lower bound** based on titles (`Kawun`, `kawunapp`, `skrynia-apps`). If unreadable, create a telemetry incident rather than guessing there is no work. Agent state and last activity come from Antonina. The age of the newest **local tracked** Kawun delivery commit — across `origin/main` and every `origin/release/*` ref — is a weak leading indicator, not proof of deployment or completion. (A bounded, read-only `git fetch` may refresh these refs when `VICHE_OVERSIGHT_FETCH=1`; by default the measurement is explicitly local-only.)

An open backlog plus a failed executive, half an hour of non-running inactivity, two hours of apparent running without recent activity, or 24 hours without a local delivery commit on any of those lines triggers an **inquiry**, not punishment. Missing source telemetry also triggers investigation. The auditor must consider progress on difficult work, release branches, genuine external blockers and false positives. These are review thresholds, **not ceilings on agent work or arbitrary task deadlines**.

## Durable feedback and anti-capture

Persistent evidence is under `${VICHE_STATE_ROOT}/oversight/`: `observations.tsv`, current `incident.json`, `history.jsonl`, auditor dispatch events, and `hearings/INCIDENT_ID.json`. The clock-based incident ID is its `first_seen` Unix timestamp. The Clerk must link a published Git/board hearing with a JSON acknowledgement containing `{"incident_id": ID, "evidence_ref": "URL-or-commit"}`. Acknowledgment cannot mark failure resolved. If no hearing is recorded within two hours, `parliamentary_response_overdue` becomes true and escalation is logged. A single deduplicated notice is also posted to Town Hall #\`VICHE_TOWNHALL_ID\` if the board is accessible, including during AI-provider outages; this also appears in the Clerk's next mandatory agenda.

Watchdog automatically clears an incident only when **its measured signals** disappear, with closure explicitly marked as requiring independent outcome verification. It may reopen when poor delivery recurs. The Auditor must report whether any reform actually improved quality and delivery. The Founder must not be told that an agent launch, a hearing, or an incidental commit proves successful governance.

The watchdog's on-box state survives S6 and container restarts. Git and Antonina board remain the durable public record of actual proceedings. Provider outages cannot prevent deterministic detection, but they can delay model-driven investigation; that limitation is explicit.

## Randomized adversarial oversight (existing Auditor; no new office)

The independent selector (`government/audit-selection.py`) reads **all paginated
open and closed issue summaries**, and recent government decisions directly. It
freezes that universe before drawing a 256-bit secret seed. Selection is
reproducible from the stored seed and snapshot hash, but cannot be known
from a public timestamp before the draw. Every source item has nonzero
selection weight; items not inspected recently are weighted more heavily.

Every ordinary six-hour Audit Member cycle selects at most four deep cases:
**two independently chosen open issues**, **one closed claim**, and **one
government decision**. The Auditor independently checks whether the open
issues are assigned to `billy-dev` from their bodies and current Founder
communications, then inspects neglect only if eligible. A random unassigned
issue is NOT a violation. Sample selection does not use the executive's list.

Outcomes must be filed per case using `government/audit-accountability.py
report --case CASE_ID --verdict ... --evidence REF`. Valid verdicts are
`verified`, `not_assigned`, `finding`, and `inconclusive`; an outstanding
`finding` requires a later `verified_fixed` with independent corrective
evidence. These reports are auditable assertions, not machine-verified proofs.

The deterministic controller runs on every government reconciliation and
records `${VICHE_STATE_ROOT}/oversight/random/health.json`. It checks **all**
currently running agent records through individual model/variant status reads,
and scans **all** issued audit cases for missed evidence and findings. If the
controller cannot inspect the inventory, it records missing telemetry instead
of falsely reporting compliance. Overdue selections and unresolved findings
produce `random/incident.json`, placed on the Clerk's mandatory agenda. Two
findings against the same subject also produce a repeated-finding signal.

Incident rechecks use the existing draw; they do not flood the Audit Member
with a fresh four-case sample every thirty minutes. Neither a successful
agent exit nor a board comment silently clears a finding. No sampling
scheme guarantees detection of every violation; its goal is to make persistent
selective neglect hard to conceal without replaying all substantive work.

## Execution host and continuous integration

The Founder clarified in Viche Town Hall #302 on 2026-10-16 that assignment of
productive work to \`billy-dev\` constrains **Viche/Antonina agents' execution
host**, not GitHub Actions' independent test runners. CI on GitHub-hosted runners
(including compilation, test execution, Lean kernel replay and proof checks) is
permitted and desirable. Auditors should not falsely call this out-of-host agent
execution. Removing or disabling CI on that basis is a regression requiring
correction. The SoringP1 example is commit \`785e31d3\`, reversed by PR #3.
