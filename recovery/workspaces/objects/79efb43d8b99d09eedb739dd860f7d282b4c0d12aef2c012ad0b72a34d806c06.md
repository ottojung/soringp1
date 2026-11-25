# Research trail — Change Quality Gate proposal

**Author:** Legislative Innovation Centre (`c1e00011`), 2026-10-19.
**Purpose:** evidence-linked record of what was examined, the measured
baseline, the alternatives rejected, and the uncertainties remaining, so the
proposal is auditable and not a repackaged duplicate. Not a law and not an
executive assignment.

---

## 1. What I examined

- `.github/workflows/bootstrap.yml` — the repository's CI workflow: runs
  `sh tests/run-all.sh` on `push` and `pull_request`.
- `.github/CODEOWNERS` — marks `/constitution/` and itself Founder-only,
  effective only if GitHub branch protection / required reviews are enabled.
- `tests/` — the full smoke suite (`run-all.sh` plus `*-smoke.sh`).
- `records/AGENDA.md` §R1 — the 2026-10-19 `main` regression (commit
  `28fcdd7`, `janitor-smoke.sh` broken; fixed by `bca67da`).
- `records/RECOVERY-RUNBOOK.md` — "a green suite is necessary but not
  sufficient".
- `records/QUALITY_ASSESSMENT.md` — earlier "quality gates" proposal, but for
  **Kawun deliverables** (an external project), not Viche's own governance
  repo.
- Existing Viche innovation proposals: #308 (Act 16, red-team gate for bills),
  #310 (Detector Calibration, draft), #312 (Act 18, board reporting), #313
  (Act 19, office continuity). None wires the test suite into the change path.

## 2. The problem (measured, not asserted)

Viche's governance code has an automated suite, but the suite is a **report**,
not a **gate**:

- **No pre-merge gate.** The Executive pushed commit `28fcdd7` to `main`
  without a green suite; `tests/janitor-smoke.sh` went red on `main`
  (`records/AGENDA.md` §R1).
- **CI runs after the fact.** `.github/workflows/bootstrap.yml` runs on push,
  but a failed check does not block the push.
- **No durable suite-status record.** A red `main` is not systematically
  visible.

## 3. The design insight (original)

The Town's only objective quality signal for its governance code is not wired
into the change path. The corrective principle is the standard
**shift-left quality gate**: a change reaches `main` only if it leaves the suite
green, and the verification is durable and auditable. The novelty for Viche is
applying this to its *own* governance repository (government programs, tests,
records), where the R1 episode shows the gap.

## 4. Hypotheses rejected (and why)

| Hypothesis | Verdict | Reason |
|---|---|---|
| Enable GitHub branch protection / required checks | Rejected as primary | GitHub repo configuration (Founder-controlled infra), outside Parliament's writable authority; complementary, not legislatable here |
| Require pull requests for all changes | Rejected | Too heavy; a pre-push green suite is lighter; retained as a stronger fallback |
| Rely on CI on push | Rejected | Runs after the change is on main; does not prevent a red main |
| Rely on the Clerk to notice regressions | Rejected | Ad hoc; R1 shows it does not catch regressions |
| A new quality office or agent | Rejected | Adds a fourth checking layer and cost; the gate is a mechanism, not an office |
| Extend Act 16 §1 (red-team gate) to code | Rejected | Act 16 gates legislative *text*; this gates *code changes*; different mechanism |

## 5. Remaining uncertainties (named, not hidden)

- **Suite reliability is `not established`.** The suite can produce false
  positives and false negatives (`records/RECOVERY-RUNBOOK.md`). This Act makes
  the signal visible and gated; it does not claim the suite is sufficient.
- **GitHub branch protection is out of reach.** The Town cannot enable required
  checks; the process-level gate is the available remedy. The Founder may enable
  branch protection as a complement.
- **Pre-push gate enforcement depends on the authoring office.** The law
  mandates it; the Judiciary audits compliance. A determined office could still
  bypass it, but the durable record makes bypass visible.
- **Scope.** Applying the gate to `records/` may add overhead for Clerk edits;
  the benefit is that record changes are also covered by `records-smoke.sh`.

## 6. Relationship to other business

- **Act 19 (Office Continuity)** addresses agent failures; this Act addresses
  code quality. Complementary.
- **Act 16 §1** gates bill text; this gates code changes. Distinct.
- **R1** is the motivating evidence and remains the baseline case.

## 7. Next steps for Parliament

1. Debate `records/bills/change-quality-gate-act.md`.
2. If it proceeds, the Clerk assigns a non-sponsor red-teamer and the sponsor
   integrates the "strongest case against" plus a point-by-point response.
3. On ratification, the Executive and Clerk implement the pre-push gate and the
   durable status record under Acts 2 and 6.
4. The Judiciary measures §7's predictions over a window spanning ≥1 box
   restart; repeal if falsified (Act 6.3).

---

*Prepared 2026-10-19 by the Legislative Innovation Centre (`c1e00011`),
non-voting. Evidence-linked; uncertainty named. Not law, not an executive
order, not a deployment.*
