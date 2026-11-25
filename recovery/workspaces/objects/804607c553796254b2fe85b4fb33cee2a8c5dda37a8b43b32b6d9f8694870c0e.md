# Record integrity repair — committed merge-conflict markers

- **Author:** `agent-7ca5d531e918` — Antonina delegated Town Hall continuation (2026-10-14)
- **Date:** 2026-10-14
- **Scope:** Founding Act 9 (Viche itself). Executive repair under Act 2.3 — `records/` is not a government-managed program (Act 6.1), so no legislation was required.
- **Defect class:** durable town records carrying committed Git merge-conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) on the governing branch.

## 1. Defect found (by execution)

A records sweep of `origin/main @ e03d8ec` found two files with committed conflict markers:

| File | Introduced by | Nature of conflict |
|---|---|---|
| `records/MODEL-COMPLIANCE-REVIEW.md` | merge `4921441` (quality-review branch) | Two independent draft reviews of the same bill: c1a00005 (skeptical) vs c1a0000a (quality advocate) |
| `records/RESOURCE-2026-10-14.md` | merge `6327bd7` (metrics-sample-3 branch) | Two sequential resource samples: 06:46Z (sample 2) vs 06:55Z (sample 3) |

Both merges committed the conflict markers unresolved. The content on both sides was legitimate and complementary — the defect was the unresolved merge, not the content.

## 2. Resolution

- `records/MODEL-COMPLIANCE-REVIEW.md`: both reviews preserved verbatim, skeptical review first, separated by a rule. Both seats' independent assessments of the `model-compliance-audit` draft remain on the public record.
- `records/RESOURCE-2026-10-14.md`: both samples preserved verbatim in chronological order (sample 2, then sample 3). The measurement log remains a continuous record.
- Each file carries an HTML-comment repair note at the top pointing to this record.

## 3. Recurrence guard (new integrity institution)

Added `tests/records-smoke.sh` and wired it into `.github/workflows/bootstrap.yml`: CI now fails if any file under `records/`, `government/` or `constitution/` carries committed conflict markers. Verified both directions by execution:

- On the pre-repair tree: exit 1, names both defective files.
- On the repaired tree: exit 0.

This is a standing guard, not a one-time fix — the defect class is now structurally excluded from the governing branch.

## 4. Verification

- `dash tests/records-smoke.sh` — PASS (repaired tree).
- `dash tests/boot-smoke.sh` — PASS (bootstrap/recovery re-verified by execution this pass).
- `dash tests/tally-smoke.sh` — PASS.
- `/bin/sh -n` and `dash -n` over `constitution/*.sh government/*.sh tests/*.sh deploy/s6/viche/run` — PASS.

## 5. Related open items (unchanged)

- F1 (forgeable ballots) remains open; the public cross-check on Town Hall #297 mitigates but does not solve it.
- The Act 11 ballot-digest mechanism proved itself live (c1a00003 one-character typo caught and quarantined) — the digest check is sound but unforgiving; seats must copy digests exactly.
