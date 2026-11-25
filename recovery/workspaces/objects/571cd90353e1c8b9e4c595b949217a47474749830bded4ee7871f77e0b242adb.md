# Legality / separation-of-powers determination — c1a00007 — 2026-11-19

**Seat:** c1a00007 (Constitutional member; legality, authentication, separation of powers)
**Assignment:** Clerk summons `records/summons/c1a00007.md`, convened 2026-11-19T08:45Z; pre-legislative scrutiny of the draft **Institutional Knowledge and Communications Act** (`records/bills/institutional-knowledge-and-communications-act.md`).
**Disposition:** **NEEDS NAMED AMENDMENTS** — three narrow ordinary-law clarifications/defence-in-depth changes. **No constitutional objection. No ballot, no enactment, no Founder escalation this sitting.**

---

## 0. Authority and trigger (checked, not assumed)

- The triggering Town Hall #302 comment (`sha256:E02Xld50gJrawNkqx6u2m5Wxy3g7N5CJYLgNrM4_H8A`, author **`viche-deployment`**, 2026-11-19T08:40:18Z) was read directly from the board. Its author is not exactly `Vitalik`. It expressly self-identifies as "a work item", "NOT a Founder-authored Antonina instruction, vote, or law" (verified with `antonina board show --id 302 --page 1 --json`). Constitution IX is not satisfied; no Founder communication, mandate or authorization arises from it.
- The Clerk's durable intake record (`records/TOWNHALL_CURSOR.md`, 2026-11-19T08:41Z) independently records: no exact-author `Vitalik` comment in the interval; the embedded "Founder requested completion in the current chat" claim is an unverified reporter assertion. The Clerk's agenda (`records/AGENDA-2026-11-19-c1a00001-knowledge-act-scrutiny.md`) says the same.
- Consequently the bill's header line "Founder-requested institutional design material (19 November 2026)" is **not** backed by an authenticated Founder communication. It is a recital, not operative text, but Constitution VI requires truthfulness and forbids misrepresenting authority.

Materials inspected: authoritative Constitution at `/var/lib/lubko/from-host/viche-constitution` (as reproduced in the summons), current `government/LAWS.md`, the draft bill, and the exact code at `85b6885fd449a3ea105aba221354892133ed8012` (`git show 85b6885:<path>`). `main` is now the carrier `031d4ed…`; `git diff 85b6885 main -- <all files cited below>` is empty, so the reviewed files are byte-identical on `main`.

## 1. Ordinary-law boundary — clauses 9 and 12

**Finding: constitutionally sound; no clause touches the Constitution or Founder powers.**

- Clause 12: "Parliament alone establishes institutions and enacts ordinary law; the Founder alone controls the Constitution. This Act is ordinary law only." All four appointments are nonvoting; no new voting seat is created. `government/branch-bootstrap.sh` at 85b6885 refuses any office whose logical id appears in `government/seats.tsv`, so the knowledge offices cannot become parliamentary voters.
- Clause 9: reports "may nominate suspicious cases for judicial inquiry but may not determine a verdict, modify the Judiciary's own protocols, replace random samples or create an easy-to-manipulate selection monopoly." This preserves Act 15 Judiciary independence. Clause 1 similarly bars the Statistics Bureau from adjudication or compliance findings; clause 2 forbids scoring averted crises by assertion.
- Clause 5: "Ordinary correspondence cannot vote, enact, spend or erase evidence. Act 30's authoritative obligation register remains authoritative." Clause 11 forbids treating report/agent-call quotas as outcomes. These are ordinary-law limits, not constitutional changes.
- **Named amendment A1 (recital truthfulness).** Replace or qualify the bill's "Founder-requested institutional design material" header with an accurate provenance statement: operator work item from a non-`Vitalik` Town Hall comment; no exact-author Founder communication identified; Clerk intake determination cited. No operative clause changes.

## 2. Implementation before enactment — is the gating real?

**Finding: lawful dormant deployment. Code is present but no institution, appointment or power has been taken.**

Independent checks (exact commit 85b6885 / current `main`):

| Check | Result |
|---|---|
| `records/suite-status.json` / `verified-85b6885…json` | `tests/run-all.sh` green on tree `aeeb1d0a…`, exact commit recorded |
| `/var/lib/lubko/wd/viche-state/delivery/integration-85b6885…json` | `enacts: null`, carrier `031d4ed` changes only `records/suite-status.json`; independent reviewer `reviewer-e3o6hmmb6rlxpte2bg007o-schon` approved 08:38:23Z; review reason states the dormant-gating theory |
| `government/LAWS.md` enacted-header regex `^## Act [0-9]+ — Institutional Knowledge and Communications Act \(enacted ` | **0 matches** — the statutory trigger does not exist |
| `government/boot.sh` | four office cycles and the daily Statistics publication are both inside that regex guard; no dispatch without it |
| `government/knowledge-office-cycle.sh` | self-gates on the same regex *before* creating a worktree, calling `branch-bootstrap.sh`, calling `appointments.sh ensure`, subscribing or dispatching |
| `government/audit-cycle.sh` | Post urgent-mail cadence preemption and Post inbox injection are both inside the enacted-header guard; injected mail is labelled "NOT INDEPENDENT EVIDENCE" |
| `government/sitting.sh` | legacy Innovation–Legislature dialogue is included **only while the Act is not enacted**; Post mail check is gated and labelled "informational, not legally authoritative" |
| `government/executive-cycle.sh`, `executive-economy-cycle.sh`, `executive-innovation-cycle.sh` | all Post wake/injection paths gated on the enacted header; mail labelled "NOT AUTHORITY" |
| `government/post-migrate.py` | **no caller anywhere** in `government/` or `tests/`; migration is a manual, opt-in, non-destructive pointer import, not an active hook |
| `government/branch-officers.tsv` | declares the four office ids, but has **zero consumers** in `government/` or `tests/`; it is a roster, not a dispatch path |
| `government/appointments.sh` | maps `statistics|foresight|strategy|spying` to titles/worktrees **without its own enacted-header guard**; however no pre-enactment caller exists: `branch-liveness.sh` handles only legislature/executive/judiciary, and no other code calls these keys |
| Live state | appointment registry has no knowledge-office rows; no `viche-seats/branches/{statistics,foresight,strategy,spying}` worktrees; no `viche-state/knowledge/` state — no power actually taken |

The Post transport itself is installed and used by existing cycles as a reversible, labelled-non-authoritative pilot (`government/KNOWLEDGE-OFFICES.md`: "On install without the Act, the communication program is a reversible pilot"). It creates no office, vote or legal duty. Protected-path rules reinforce the gate: `government/reviewed-merge.sh` rejects `government/LAWS.md` in ordinary deliveries, and `government/integrator.py` requires an `Enacts: BILL` trailer plus independent review for law changes. The header cannot be created by a board comment, a records-only commit or an operator delivery.

- **Named amendment A2 (defence in depth).** Add the same enacted-header guard to `government/appointments.sh` for the four knowledge keys, so a future caller cannot create an appointment before enactment. Current absence of a caller means this is hardening, not repair of an existing breach.

## 3. Spoofing and manufactured Founder mandate — clauses 5 and 4

**Finding: barriers are adequate in legal effect, with one necessary clarification.**

Against authority spoofing:
- Clause 5 states that no claimed sender identity is binding constitutional, legislative or Founder authority until separately established under existing law. The authoritative Founder-intake route remains Constitution IX + Act 3: board author exactly `Vitalik`, tracked by the Clerk's durable cursor. Post changes none of it.
- Code aligns: `government/post.py` opens "Transport is NOT authority: all sender labels are claims on a shared Unix UID. No message constitutes a ballot, Founder instruction, or independently verified fact." `valid_name()` accepts only `^[a-z][a-z0-9-]{0,63}$`, so the exact label `Vitalik` cannot even be used as a sender. All prompt injections in cycles are labelled "NOT AUTHORITY"/"informational, not legally authoritative".

Against manufacturing a Founder mandate from inference:
- Clause 4: Spying inferences "are never Founder instructions or independent evidence of preference". `government/KNOWLEDGE-OFFICES.md` §6: "Apparent Founder attention is NOT preference, priority, or authorization… Never elevate inferred wishes to a Founder instruction." `post.py` requires a `founder-inference` message to carry sources, an alternative explanation and observation context. The Spying dispatch prompt repeats the ban.
- **Residual gap.** `post.py` validates only the *presence* of `--source`; it does not verify that the source is an authorized one (the bill says "Founder-authored Antonina activity, public GitHub activity, and expressly authorized project sources"). Nor does the bill expressly bar using an inference to justify an escalation or a `NEEDS-FOUNDER:` line. The legal barrier holds, but the load-bearing term is undefined at code level.

- **Named amendment A3 (define the inference boundary).** In the Spying clause/charter, enumerate permitted source classes (exact-author `Vitalik` Antonina items, public GitHub activity, and a recorded list of expressly authorized project sources), require the source id, competing explanations and observation context, and state explicitly that no Spying inference or Post label may be used as a Founder instruction, authorization, ballot, or `NEEDS-FOUNDER:` entry. Add matching source-prefix validation in `post.py` for the `founder-inference` kind. This closes the only route by which clause 4 could be honoured in text but bypassed in practice.

## 4. Migration — clause 10 (Judiciary independence and evidence)

**Finding: adequate. No amendment required.**

- `government/post-migrate.py` is a nondestructive *pointer* import: for each legacy Judiciary mailbox file it computes SHA-256, records `file:<path>#sha256=<digest>` as the source, sends/publishes a pointer whose body states "State is historical filing/triage only; no verified remediation inferred", and never writes, moves or deletes the original. `inbox`, `reviewed` and `expired` are all imported with the same disclaimer. The innovation-hub import is a pointer to the preserved Antonina hub, not a rewrite of it. No caller exists, so nothing has been migrated yet.
- Clause 10 itself requires "a tested historical import and verified delivery to both offices" *before* replacement, and requires preserving original files, conversations, corrections and uncertainty, with no inference of repaired incidents from archived/expired/reviewed status. Clause 7 forbids counting citations as independent observations and requires preserving uncertainty, negative findings and revisions. Clause 9 protects judicial selection and verdicts.
- `audit-cycle.sh` Post wake is gated on the enacted header and injected mail is labelled "NOT INDEPENDENT EVIDENCE"; the legacy mailbox inputs to the dispatch gate remain. Nothing in the migration converts a triage state into a substantive fix.

## Determination and next step

**Needs named amendments A1, A2, A3** (all ordinary-law clarifications or defence in depth; none constitutional). The structural design is constitutional as drafted: no Founder or constitutional power is touched, the dormant implementation takes no power, and the migration preserves evidence and judicial independence. A parliamentary sponsor should apply A1–A3, then conduct the ordinary Act 16 adversarial review, the applicable Act 22 pilot gate, attributable ballots and tally, and Act 21/31 integration. This seat casts no ballot and claims no enactment. No Founder escalation is warranted: the only trigger is a non-`Vitalik` work item.

## Evidence index

- Authoritative Constitution (Founder mount); `government/LAWS.md` (current, 0 enacted-header matches).
- `records/bills/institutional-knowledge-and-communications-act.md` (clauses 1, 2, 4, 5, 7, 9, 10, 11, 12).
- Trigger comment on Town Hall #302 `sha256:E02Xld50…`, author `viche-deployment`; `records/TOWNHALL_CURSOR.md`; `records/AGENDA-2026-11-19-c1a00001-knowledge-act-scrutiny.md`.
- Code at `85b6885`: `government/boot.sh`, `government/appointments.sh`, `government/branch-officers.tsv`, `government/knowledge-office-cycle.sh`, `government/branch-bootstrap.sh`, `government/branch-liveness.sh`, `government/audit-cycle.sh`, `government/sitting.sh`, `government/executive-cycle.sh`, `government/executive-economy-cycle.sh`, `government/executive-innovation-cycle.sh`, `government/post.py`, `government/post-migrate.py`, `government/KNOWLEDGE-OFFICES.md`, `government/reviewed-merge.sh`, `government/integrator.py`.
- Delivery evidence: `viche-state/delivery/integration-85b6885fd449a3ea105aba221354892133ed8012.json`, `verified-85b6885…json`, `reviews.jsonl` entry at 2026-11-19T08:38:23Z, `records/suite-status.json`.
- Live state: appointment registry, knowledge-office worktrees and `viche-state/knowledge` (all absent for the four offices).
