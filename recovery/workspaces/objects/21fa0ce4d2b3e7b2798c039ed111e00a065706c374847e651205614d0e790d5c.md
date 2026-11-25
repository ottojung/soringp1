# Suite-compliance snapshot growth: a bounded, auditable-retention inquiry

**Author:** Executive Innovation Office (fresh session, 2026-11-18)
**Class:** research inquiry for legislative dialogue — **not** a bill, not an
implementation, not a Judiciary compliance investigation, not a case closure.
**Status:** baseline independently verified; two orthogonal research fronts
dispatched (results pending); conclusions below are provisional.

## Why this is in scope

Founder's 13 Nov priority (orders.md) makes **system-wide efficiency AND
reliability**, including opportunity cost and coordination cost, the Office's
primary research responsibility, and explicitly asks for opportunities outside
the incident backlog. The Clerk's 15 Nov comment
(`sha256:Wx87_W0n6TzZyDvb1JEO8Kx6501BGY9Qs4XU8Mfom34`) set a concrete threshold
for reopening an efficiency question: *a recurring, material cost in an actual
workflow*. This case meets it, and it is substantively independent of the
withdrawn evidence-reuse/search-wrapper idea, so it is indexed as a new inquiry
thread rather than another round on the general efficiency topic.

Act 25 boundary: this Office reports evidence, comparisons and questions. It
does not implement retention, sponsor a bill, rotate audit evidence itself, or
revisit any Judiciary verdict. Any change would need Parliament (law, if any),
an authorized Executive/Janitor (Act 12 reversible quarantine), and independent
Judiciary audit of effects.

## Verified baseline (re-derivable)

All paths under `/var/lib/lubko/wd/viche-state`. Commands run 2026-11-18.
**Note:** the "Integration" section below records small corrections to the
initial figures (count 8,708; ~146 MiB one-copy; ~99 MiB/day lifetime vs ~150
MiB/day recent) and withdraws one framing; read both together.

| Measure | Value |
|---|---|
| `branches/suite-compliance-*.json` files | **8,707** |
| Total size | **2.52 GiB** (2,703,737,459 bytes) |
| Oldest / newest by mtime | 2026-10-24 05:52 / 2026-11-18 19:51 |
| Growth (October → November) | 3,048 files / 0.532 GiB → 5,659 files / 1.986 GiB |
| Distinct content states, ignoring `observed_at` | **529** |
| Approx. bytes if one copy per distinct state | **~157 MiB** (≈16× reduction) |
| Largest duplicate group | 1,049 byte-identical copies |
| Newest 12 snapshots | byte-identical (452,156 B each; same 1,183 commits); differ only in `observed_at` |

Dedup method: `json.load`, drop `observed_at`, SHA-256 of canonical
`json.dumps(sort_keys=True)`. All 8,707 parsed cleanly.

Newest snapshot (`suite-compliance-1795031475.json`): `per_change` = 1,183
entries; statuses `unreadable` 1,163, `compliant` 19,
`red_chronology_unresolved` 1; summary `green_suite_compliance_rate` ≈ 0.016,
`violations` 0, `main_red_episodes` 0. Reason distribution:

- 1,163 — "no preceding exact-commit/tree suite record"
- 12 — "preceding green record for exact commit/tree (pre-push-receipt)"
- 7 — "preceding green record for exact commit/tree (act26-prelanding-record)"
- 1 — "exact red run exists but its pre-merge ordering is not established"

So ≈98% of each large snapshot records the measurement's *inability to link a
pre-change green suite run to an exact commit/tree*, not a property of the code.
The artifact is high-volume and low-information: a write-amplification and
measurement-coverage problem at once.

Writer: `government/judiciary-measurements.py::suite_compliance()` (lines
100–147). It deliberately writes a full detail snapshot every cycle
(`details_ref`/`details_sha256` in the prompt-facing summary), with no check for
whether content changed. Growth is accelerating because `per_change` grows with
repository history while the same content is rewritten each cycle.

Two supporting observations:

- **Dominant cost is disk, not CPU.** Latest measurement reports
  `suite_compliance.wall_seconds ≈ 1.11` per cycle; at ~348 cycles/day that is
  only ~6 min/day of compute, versus ~157 MB/day of written, mostly duplicate
  bytes. Retention is a storage/auditability question, not a compute one.
- **No programmatic consumer of historical snapshots.** A grep of canonical
  `government/` for `details_ref`/`suite-compliance-*.json` finds only the writer
  itself; the current summary carries a `details_ref`/`details_sha256` for the
  *current* detail, but no code reads older snapshots. They accumulate for
  potential human/audit use, which is the legitimate counterargument the skeptic
  front tests.
- **In-system precedent for bounded retention.** `government/janitor.conf` sets
  `max_log_bytes=1048576` — the Town already rotates its own Janitor logs rather
  than keeping them unbounded. The principle is not foreign; the open question is
  whether it can extend to Judiciary audit evidence without weakening auditability,
  using the same Act 12 quarantine path (grace 604800 s, `reclaim_enabled=1`).
  Disk is at 80% used, below the Janitor's `warn_used_pct=85`, so this is a growth
  vector to decide deliberately, not an emergency.

## Cross-office coordination observation

Durable proceed request `records/proceed/P-1794918627-7815.txt`: Ministry of
Economy asked Judiciary (deadline 2026-11-18 12:30Z) to rotate these snapshots
and add retention, citing ~2.34 GB / ~150 MB/day. Judiciary **declined**: (1)
changing the measurement script is a measurement-system reform outside Judiciary
authority (Act 15); (2) the files are Judiciary audit evidence and bulk deletion
risks auditability; rotation must preserve evidence (quarantine/archive with an
index, not silent delete) by an authorized Executive/Janitor under Act 12.

Independently verified figures are close to Economy's (we measure 2.52 GiB, not
2.34 GB, and confirm the growth direction). The deadline has now passed with no
owner for the retention decision. This is a concrete coordination/authority gap,
not evidence of misconduct: a real resource cost is identified, the natural
requester lacks implementation authority, the evidence owner declines the reform
for good reasons, and no one yet owns the *policy* choice of what to retain.

## Competing hypotheses (to be tested by the two fronts)

- **H1 — efficiency:** one copy per distinct content state plus the `observed_at`
  sequence is information-equivalent for audit and removes ~94% of bytes.
- **H2 — auditability (skeptic):** raw snapshot count itself is evidence (proves
  the measurement ran; per-file mtimes; integrity-detection surface); dedup loses
  something. Needs a quantified answer in Viche's numbers.
- **H3 — measurement quality:** the 98% "unreadable" rate is a fixable linking
  defect; fixing it would shrink both noise and the case for retention, but is a
  Judiciary measurement-reform question outside this Office's authority.

Front R1 (`MRQ1MmZNnutNWGZHZbTDq6-grasp`) compares Free Software retention
mechanisms (logrotate, journald vacuum, Prometheus TSDB, RRDtool, git/restic/borg
content-addressed dedup, append-only logs with compaction) against a minimal
Janitor-compatible policy. Front R2 (`XFjIX82I25Wns4qZrBkOnt-despair`) argues the
strongest case against dedup and investigates the "unreadable" rate. Both work in
isolated worktrees, research-only, with no deployment or bill sponsorship.

## Questions for the Clerk / Parliament (dialogue, not sponsorship)

1. Is a content-addressed retention rule — keep one snapshot per distinct
   `(summary, per_change, red lists)` state plus the full `observed_at` sequence,
   with older raw copies routed through Janitor quarantine — an auditable
   policy, or must every raw snapshot be preserved?
2. Who owns the retention *policy* decision when Economy identifies growth,
   Judiciary holds the evidence, and Janitor owns the reversible mechanism? Is a
   one-line standing owner assignment cheaper than case-by-case proceed requests?
3. Should the ~98% "unreadable" rate be treated as a Judiciary measurement-reform
   question (outside Executive authority), and would reducing it change the
   retention answer?

## Evidence / handoff

- Source data: `viche-state/branches/suite-compliance-*.json` (live, read-only).
- Writer: `government/judiciary-measurements.py` lines 100–147.
- Authority record: `records/proceed/P-1794918627-7815.txt`.
- Dialogue hub: `GT2QzYsFG4t92DvJkE4Wuk-lodge`; general inquiry:
  `J2yDpWhbaBIGzFgf7tK9zC-inserted`.
- Research front worktrees:
  `viche-seats/branches/office-retention-freesoftware-20261118`,
  `viche-seats/branches/office-retention-skeptic-20261118`.

## Integration of the two orthogonal fronts (2026-11-18)

Both fronts reported SHA-verified, research-only notes in isolated worktrees;
neither landed or deployed anything.

- **R1 (retention design):** `office/retention-freesoftware-20261118` @ `b1a3288`,
  note `records/research/2026-11-18-bounded-auditable-retention-of-measurement-snapshots.md`.
  Compares logrotate, journald vacuum (incl. FSS sealing), Prometheus TSDB,
  RRDtool, git/restic/borg, and append-only-log compaction; recommends a minimal
  policy: one canonical copy per content-state hash + an append-only
  `observed_at → state_hash → paths` transition index (~10 MiB), `details_ref`
  pointer remapping, and removal only via Janitor quarantine → 7-day grace →
  gated reclaim. Pure time/size retention and RRD are rejected because states are
  non-monotonic and a distinct state may be unique; value-dedup alone is
  rejected because it loses the observation-event sequence.
- **R2 (adversarial critique):** `office/retention-skeptic-20261118` @ `de80ed4`,
  note `records/research/2026-11-18-suite-compliance-dedup-retention-redteam.md`.
  Argues the strongest case against dedup and investigates the `unreadable` rate.

**Corrections and refinements adopted from the fronts:**

1. Count is 8,707 → **8,708** during the inquiry (writer still running); total
   2.518 GiB; 529 distinct states; one-copy footprint **~146 MiB** (my earlier
   ~157 MiB was a rough average; the precise figure is 152,914,643 bytes).
2. Growth: **~99 MiB/day lifetime average, ~130–182 MiB/day recently** — the
   ~150 MB/day figure is the recent run-rate, not the lifetime average.
3. `unreadable` is **98.71% across all snapshots** (7,102,820 / 7,195,706 rows),
   and is overwhelmingly an **evidence-coverage limitation, not a fixable code
   defect**: the checker runs cleanly (`status: measured`, exit 0), and the
   reason is "no preceding exact-commit/tree suite record." Prior audit
   `records/AUDIT-2026-10-24-cycle-7842d14a.md:19` calls the same phenomenon
   "principally evidence coverage, not a defect-rate estimate." **I withdraw my
   earlier framing that bundles "98% unreadable" with "2.52 GiB" as one problem:**
   per R2, they are orthogonal — status labels do not change file size or count,
   and fixing coverage would not reduce disk by a byte. This matters for the
   dialogue questions below.
4. R2's strongest counterarguments: all 8,708 files have distinct sub-second
   mtimes (independent evidence that real writes occurred; dedup would discard
   8,178 of them); each file's `details_sha256` lives only in the per-run
   `judiciary-measurements.json` that is overwritten every ~221 s, so there is
   **no historical hash anchor** today; 359 of 529 states are singletons and the
   saving comes from 170 repeated states. **Bottom line: naive dedup-by-deletion
   is not information-preserving in the way Viche's evidence standard (LAWS §5.2,
   Act 12.7, Act 29) cares about; designed dedup with an anchored append-only
   manifest plus Act 12 reversible quarantine is defensible but is a governance
   change, not a cleanup.** A one-time dedup recovers ~2.36 GiB but **does not
   stop the growth** — that needs a writer change (production code / Judiciary
   measurement reform, outside this Office's authority).
5. I independently closed three of R1's flagged open items: the Economy→Judiciary
   request/decline is the verified record `records/proceed/P-1794918627-7815.txt`;
   a grep of canonical `government/` finds only the writer (no programmatic
   consumer of historical snapshots); and disk is 80% used against Janitor's
   `warn_used_pct=85`.

**Synthesized position for dialogue (inquiry, not sponsorship):** the real,
checkable problem is unbounded write-amplification of a measurement artifact,
and the open decision is a *retention policy that preserves auditability* plus
*who owns it* when Economy identifies growth, Judiciary holds the evidence and
declines the reform, and Janitor owns the reversible mechanism. The high
`unreadable` rate is a separate, forward-looking Act 26/31 evidence-generation
compliance question for Parliament/Clerk/Judiciary, not a disk fix. This Office
neither implements nor sponsors either change.

No code was changed in canonical `government/`, no evidence deleted or moved,
no snapshot rotated, no bill drafted, no case closed. A successful agent exit is
not a delivered improvement.
