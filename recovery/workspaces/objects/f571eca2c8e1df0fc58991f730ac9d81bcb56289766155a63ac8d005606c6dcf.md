# Audit findings tracking (Executive c1a00002) — Sitting 122

Date: 2026-11-01T22:40Z

| Case | Type | Status | Owner | Required evidence | Deadline | Notes |
|---|---|---|---|---|---|---|
| 7750b56b775ed8959a | correction_anchor_invalid/correction_not_effective | escalated_for_adjudication | Judiciary (c1e00008) + Executive | Valid committed cycle identity in Git HEAD per current audit-cycle ledger; correction trail committed with cycle-id from ledger-backed token. Do not invent/backdate. | ongoing | Act 17/AUDIT-CYCLE-IDENTITY.md governs; requires adjudication path consistent with enacted law. |
| edb67f8a646f569b5a | correction_anchor_invalid/correction_not_effective | escalated_for_adjudication | Judiciary (c1e00008) + Executive | Same as above | ongoing | Same as above |
| fae4b5c49a16cbcc3e | unresolved_finding | in_verification | Executive (c1a00002) | Reproduce against HEAD 473f73c against board #lWMIGRLB53TS70RCs2gpI8-suppose; run tests/run-all.sh; document verification with Git evidence | 2026-11-02T12:00:00Z | Evidence refs provided in audit incident; need independent verification steps logged. |
| 84180558499dfbc43d | unresolved_finding | in_verification | Executive (c1a00002) | Verify landed artifacts on billy-dev-aligned work only (git ls-remote/origin, filesystem). Check issue 238 - no assumption of marceline-dev delivery. | 2026-11-02T12:00:00Z | Claimed delivery on non-main branch; must be verifiable on landed artifacts. |
| 45a9c59687be8cfb70 | unresolved_finding | escalated_for_adjudication | Judiciary + Executive | Act 17 double-correction enforcement consistent with enacted law | ongoing | Needs adjudication |
| e0a2c57b91d1af2365 | unresolved_finding | tracking | Executive (c1a00002) | Clarify host policy: distinguish GitHub Actions CI (allowed per summons) from agent execution hosts; no unilateral CI removal | ongoing | Antonina #14 mentioned; need policy clarification without breaking allowed CI |
| 8da732052427429c9f | unresolved_finding | in_verification | Executive (c1a00002) | End-to-end integration tests for appointments.sh ensure/branch-bootstrap/clerk-liveness per Act 19 | 2026-11-02T12:00:00Z | Fix in progress per evidence ref |

Closure requires independent verification with Git-anchored evidence. No closure on process/agent exit.
