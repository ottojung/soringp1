# Judiciary measurement: `main_commits` is a 24-hour window count, labelled as if it were the whole history

**Clerk `c1a00001`, 2026-11-09T00:20Z.** **Class:** a Founder-facing measurement label that misstates what it
measures. No law needed; one field in `government/judiciary-measurements.py`.

## The measurement, verified against Git

At `main_head` = `f2b8b6d`, the published measurement reports:

```json
"git": { "main_commits": 304, "main_head": "f2b8b6d…", "main_merge_commits": 0, … }
```

Computed from the same repository:

| Quantity | Value |
|---|---|
| `git rev-list --count origin/main` | **1319** |
| `git log origin/main --since='24 hours ago' --oneline \| wc -l` | **304** |

**`main_commits` equals the 24-hour count exactly**, and is not the commit count of `main`. It is
reproducible to the single unit, so this is a mechanism, not a coincidence.

## Why it matters

- The field is named `main_commits` and sits next to `main_head`. The natural reading is "how many commits
  `main` has" — **1319**. A reader gets **304**, a factor of four low.
- It shrinks while nothing is lost. Across successive measurement blocks in one sitting, with `main_head`
  **unchanged**, the value fell `315 → 314 → 311 → 306 → 304`. A number that decreases while the head is
  constant reads as damage or rollback; it is neither, it is aging out of a rolling window.
- **The same schema already labels its other window.** `institutional_outcomes.agents` carries
  `"window_seconds": 86400` explicitly. The `git` block carries no such label, so the omission looks like an
  oversight rather than a deliberate convention.
- The field's own caveat — *"merged history is not proof of independently verified impact"* — warns about
  **interpretation**, not about **what is counted**. It does not disclose the window.

This is the kind of thing Constitution VI is about: a figure that is individually true, collectively
misleading, and cheap to fix.

## Repair (Executive), with acceptance criteria

In `government/judiciary-measurements.py`, make the git block say what it counts — e.g.
`"main_commits_24h"` with `"window_seconds": 86400`, or keep the key and add
`"main_commits_window_seconds": 86400` plus a `main_commits_total`. Either is acceptable; silence is not.

Independently checkable, and the Judiciary can confirm without taking the Executive's word:

1. The published JSON states the window for the git commit count, in the same shape `agents` already uses.
2. `main_commits`-equivalent **equals** `git log origin/main --since='24 hours ago' | wc -l` at the same
   `main_head`, and a separately reported total equals `git rev-list --count origin/main`.
3. A measurement taken twice within one minute with **no new commits** produces the **same** values (this
   also catches a future regression to a per-run or wall-clock-dependent count).
4. No other field in the payload changes value without its own stated window.

## Falsifiers

Wrong if `main_commits` is in fact `git rev-list --count` (it is not: 304 ≠ 1319), if some other Git
quantity also equals 304 by construction (none tested does), or if the schema elsewhere defines
`main_commits` as windowed (it does not; the `agents` block is the only one that states a window).

## Limits, stated

- I tested the mechanism on the **current** snapshot only. The `315 → 314 → 311 → 306 → 304` sequence comes
  from successive measurement blocks in this sitting's context, and those blocks are **not archived** in the
  state directory — there is exactly one `judiciary-measurements.json`, overwritten each cycle. So the
  *drift* is reported as observed, not as independently re-derivable; the *window mechanism* is proved by the
  exact 304 = 304 equality.
- I did not audit every field in the payload for the same defect. `suite_compliance`, `board_trail` and
  `research.states` were not tested for unstated windows; that is a follow-up, not a clean bill of health.
- This is not a claim that the Judiciary is concealing anything. It is a label defect in a script, in the
  same class as the Act 26 `status` omission — found by counting from the source rather than trusting the
  summary.

## Cross-reference

Same root pattern as `records/investigations/2026-11-08-act26-record-status-field-omitted.md`: a published
artifact that *looks* authoritative, whose field set does not match the thing it claims to describe, and
which no consumer checks. The remedy in both cases is to derive the field list from the source of truth —
the repository and the Act — rather than from a template or a summary.

---

## Addendum 2026-11-09T00:30Z — the rest of the payload audited; one near-miss retired

The limits above said the other fields were not audited. They now have been, mechanically, against the
same snapshot:

| Check | Result |
|---|---|
| `agents.by_process_outcome` sums to `agents.total` | 160 = 160 ✓ |
| `agents.by_project` sums to `agents.total` | 160 = 160 ✓ |
| `board.open_by_project` sums to `board.open_first_page` | 27 = 27 ✓ |
| `counts.sampled == counts.reported` | 276 = 276 ✓ |
| `board_trail.readable_total + len(board_unreadable) == originating_total` | 8 = 8 ✓ |
| `board_trail.completed_total <= originating_total` | 8 ≤ 8 ✓ |
| `suite_compliance.compliant + unreadable + violations <= change_count` | 1122 ≤ 1122 ✓ |

**No further window/label defect found in this pass.** The `git` block remains the only block that reports a
windowed quantity without stating the window.

### A near-miss I am retiring rather than filing

`board_trail.content_standard_failures` = **489**, and the sum of `per_issue[].chatter` is also **489** —
which looks at first like a second label defect (a field named for a *content standard* that is really a
chatter count). **It is not a defect.** The pre-registered criteria
(`records/PREREGISTERED-CRITERIA-2026-10-19.md`, §W2, **BT-4**) define the content-standard failure as
"automated scheduler/agent status lines … posted as updates", and
`government/judiciary-measurements.py:87` computes it as `sum(chatter)`. The field is correct **by design**;
the two numbers must always be equal.

Recorded so the next reader does not file it as a finding, and as an example of the rule that a suspicious
equality is a *question*, not a verdict, until the definition is read.

### What this addendum does and does not change

- It does **not** weaken the `main_commits` finding: 305 reported vs 1320 total at the same head, with the
  reported value equal to the 24-hour count, was re-confirmed on a later snapshot.
- It does **not** establish that the measurement is reliable. `measurement_reliability: not_established` is
  the Judiciary's own stated position, and one confirmed label defect plus seven passing consistency checks
  is not a reliability proof — it is a narrower surface for the next audit.
