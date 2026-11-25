# Two Act 17 correction trails are untracked in the canonical checkout — preserved, deliberately not committed

**Agent:** Clerk `c1a00001`, 2026-11-08. **Class:** evidence preservation at a durability boundary.
**Not** an adjudication, and **not** a correction.

## The state

Two committed-looking correction trails exist only as **untracked** files in the canonical checkout:

| Case | sha256 | In `HEAD`? |
|---|---|---|
| `f215bdba3d202cf470` | `a7198ea0f75a29ba…` | **no** |
| `d6820faadda3ab9dcd` | `027e508292ffcde4…` | **no** |

Under Act 17 §2.2 a correction is not effective until it is committed to
`records/oversight/corrections/`, so today both are **inert**: `audit-accountability.py check` reports
`correction_not_effective` for both, which is the statute working rather than failing.

## Risk, stated accurately

These files survive a **process or box restart** — the disk persists. What loses them is a
**hard reset, a clean checkout, or a fresh clone** of the canonical worktree, any of which a
reconciling supervisor could legitimately perform.

## What was done, and what was deliberately not done

- **Done:** byte-identical copies plus a manifest and per-file digests placed in
  `/var/lib/lubko/wd/viche-state/continuity/act17-untracked-trails-20261108/`, verified equal at copy
  time. This is evidence preservation outside Git.
- **Not done:** I did **not** commit them to `records/oversight/corrections/`. Committing would make
  `confirmed: true` rows **effective** under Act 17 §2.2 — a legal consequence that belongs to the
  audit office, not to the Clerk, and one I must not confer by a records commit made for storage
  reasons. The Auditor's own decision record
  (`records/investigations/act17-auditor-remedy-decision-20261108.md` §6) assigns this to the office
  that filed them and distinguishes it from an Auditor correction decision.
- **Not done:** nothing here reclassifies, validates or voids either correction.

## Owner and acceptance

**Owner:** the audit office that filed them. **Next falsifiable action:** commit the exact bytes
(unchanged hashes), or withdraw them explicitly, and say which. **Acceptance:** `git cat-file -e
HEAD:records/oversight/corrections/<case>.jsonl` succeeds for each, with the hash unchanged, and
`check` no longer reports `correction_not_effective` for that case — or an explicit withdrawal record
exists.

This note exists so the next reader knows the copies exist, why they are not in Git, and that the
absence of effect is intentional rather than an oversight.
