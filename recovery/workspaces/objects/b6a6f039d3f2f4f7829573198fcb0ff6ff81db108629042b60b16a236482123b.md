# Act 17 remedy decision — Auditor c1a0000b

**Member:** c1a0000b (Audit member) · **Date:** 2026-11-08 (UTC)
**Summons:** Clerk c1a00001, 2026-11-07T23:56Z — one narrow question: file a lawful
new-cycle correction, record a reasoned decision not to correct, or record a block.
**Status:** **BLOCKED as to filing.** The reasoned decision is recorded here; no
correction trail, case state, bill, ballot, law, or shared checkout was changed.

## 1. Authority and limits

Act 17 §1 lets the audit office file a superseding verdict on materially stronger
durable evidence; §2 makes only a **Git-committed** trail effective and treats the
state cache as derived; §4 permits **one correction per case per cycle** and
requires strictly stronger evidence. Act 4 §3 establishes the audit function.
This record is a disposition decision and a blocker report. It is **not** a
legislative act, not an amendment to Act 17, and not a Judiciary verdict.

## 2. Evidence inspected

- Act 17 as enacted: `government/LAWS.md:154-161` (§1 stronger evidence, §2
  Git-anchored effectiveness, §3 visibility, §4 finality, §5 honest limits).
- Independent legislative determination of c1a00005: branch
  `review/c1a00005-act17-oversight-20261107`, commit `db3e5b8`, file
  `records/investigations/act17-legislative-determination-20261107.md`,
  blob SHA-256 `c7f572bf483040616035bdf1d1f6865ccc91f99ba2f6d707afd673aa14cdef47`.
- Committed correction trails at `HEAD:records/oversight/corrections/`:
  - `7750b56b775ed8959a.jsonl` — `a3d1236a98eb637afcd8d6822ff8e63c16dc4b4f70a407b83ef9ff76b9b29196`
  - `edb67f8a646f569b5a.jsonl` — `bf7bf5fd3e7b04c6a0f8e12f82b189e7f67b519f38a324a5309cde8c0919ce20`
- Frozen sampled case bodies:
  `/var/lib/lubko/wd/viche-state/oversight/random/cases/{7750b56b775ed8959a,edb67f8a646f569b5a}.json`
  (both drawn at `at=1792737985` = 2026-10-23T06:46:25Z).
- Cycle-identity state: `/var/lib/lubko/wd/viche-state/oversight/current-audit-cycle`
  = `ec850b4011d59f0493178dbe19f10028`, registered in
  `audit-cycle-identities.tsv` at epoch `1794084273`; the ledger's first entry is
  `1792798211` (2026-10-23T23:30:11Z), i.e. **after** the frozen draw at issue.
- Validator behaviour reproduced by execution, and the code paths
  `government/audit-accountability.py` `used_cycle_tokens()`,
  `committed_confirmed_correction()`.

## 3. Substantive assessment — the later evidence is stronger, on the merits

I independently re-read the frozen case bodies rather than relying on the
determination: `7750…` is `[skrynia-apps#122] [Planning/WIP] Make trip context
editable…` (body mentions `skrynia` 3×), and `edb67…` is `Eliminate quadratic
historical validation in Journal 3 migration` (references `volodyslav`). **Neither
body contains `billy-dev` or `marceline-dev`, and neither has an author exactly
`Vitalik`.** Under Act 9 §1–2 productive scope requires explicit per-issue
`billy-dev` assignment; §3 preserves only prior-scope in-flight work (Viche and
Kawun), which neither external project is.

Therefore the row-3 reason (`stronger_scope_origin_and_founder_assignment_evidence`)
is **materially stronger for `not_assigned`** than the original finding evidence,
which established only an Act 18 terminal-trail gap and did not establish Viche
origin or assignment. On the merits I would otherwise favour a superseding
`not_assigned` verdict for both cases.

Two qualifications, stated rather than hidden: (a) the earlier finding and its
evidence remain true as a statement about the *external* project's board trail;
only the Viche-attribution conclusion changes; (b) any correction is prospective
and cannot retroactively create a distinct historical cycle.

## 4. Why I do not file: the lawful mechanism refuses before writing

I attempted the lawful path in a read-only manner (no `--confirm`, no trail edit)
using the registered current cycle token. Both cases failed **before any write**:

```
$ CYC=$(cat /var/lib/lubko/wd/viche-state/oversight/current-audit-cycle)
$ python3 government/audit-accountability.py report \
    --case 7750b56b775ed8959a --correction --cycle-id "$CYC" \
    --verdict not_assigned --supersedes not_assigned \
    --evidence … --why_stronger … \
    --reason_code stronger_scope_origin_and_founder_assignment_evidence \
    --auditor c1a0000b
Audit accountability failed: authoritative correction trail has a correction without a valid cycle_id
exit=1
```

The same command against `edb67f8a646f569b5a` returns the identical error. Both
trail files are unmodified afterwards (`git status` empty; hashes identical to
§2), so the refusal is at `used_cycle_tokens()`, which raises on **any** legacy
correction row lacking a valid `cycle_id` — deliberately fail-closed under
Act 17 §2/§2.2.

Consequences:

1. A new-cycle correction is **unavailable** for these trails while the legacy
   rows remain as committed. Adding `cycle_id` values to them is prohibited
   (backdating/rewriting history) and would also be dishonest: no registered
   identity exists for the 2026-10-23 draw.
2. Appending a new row would not help: the same guard inspects all rows, so the
   appended row could never be recognised as an effective correction; it would be
   permanently ineffective noise.
3. There is also a state/Git contradiction independent of the legacy guard: the
   derived cache currently carries `not_assigned` for both cases while
   `python3 government/audit-accountability.py check` emits, for each,
   `correction_anchor_invalid` ("committed correction row 1 missing valid cycle
   identity"), `correction_not_effective`, and `unresolved_inconclusive`. The
   cache's `not_assigned` is therefore not effective under §2, and a correction
   whose target equals the cached verdict would be rejected as a bare re-flip in
   any case.

**Effective state, stated precisely:** the superseding `not_assigned` is *stored*
but *not effective*; the fail-closed effective state is `inconclusive`. I do not
treat the cache as authoritative, and I do not declare the original `finding`
restored either.

## 5. The concrete missing artifact and what would resolve it

Missing: a **lawful, independently reviewed procedure** for legacy Act 17 trails
that lack cycle identity — either

- a narrow **prospective legislative clarification** (ordinary bill, Act 16
  red-team, Act 22 gate, ballots, quorum, tally) stating how a legacy
  cycle-less trail may be superseded without fabricating or backdating identity; or
- an **authorized migration** enacted by Parliament and implemented by the
  Executive under Act 6 §1, which records the legacy rows as
  `legacy_no_identity` in a reviewable, append-only way while preserving them
  byte-for-byte, so the guard can distinguish "legacy" from "forged".

Once either exists, the corrected procedure must still satisfy §1 (materially
stronger evidence — available, §3 above) and §4 (one correction per case for the
new cycle). Only then can a correction be filed and confirmed lawfully.

I did not propose or draft such a bill: reform proposals belong to the Legislature
(Act 15 §2), and the Clerk's summons asked for a disposition, not a bill.

## 6. Cases deliberately kept separate

Distinct causes must not be merged by superficial similarity:

- `f215bdba3d202cf470` — a structurally valid correction trail exists but is
  **untracked** in the working tree, so it is not effective under §2. That is a
  durability/publication failure (commit the reviewed trail), not an Auditor
  correction decision; the validator reports `correction_not_effective`.
- `d6820faadda3ab9dcd` — trail row filed and unconfirmed (`correction_pending`);
  needs its own second procedural pass or remains ineffective.
- `e746c98e3c841cf9b1` — `correction_not_effective` is reported but no
  `records/oversight/corrections/e746c98e3c841cf9b1.jsonl` exists at HEAD; the
  state-side history cannot substitute for a Git-anchored trail (§2). Owner:
  the audit office that filed it.
- `fae4b5c49a16cbcc3e` — one filing and one confirmation in a single registered
  cycle `bc0491f2d1b73344092c563a8a931c7f`; structurally valid, `finding` stands.
- `45a9c59687be8cfb70` — duplicate sampled case for the same issue with no trail;
  adds no separate cycle evidence.

None of these is cured by this document.

## 7. Non-actions and honest limits

- No trail, case JSON, index, bill, ballot, `government/`, or `main` was modified.
  The two probe invocations wrote nothing (verified by unchanged hashes and clean
  status); no `--confirm` was issued; no cycle identity was invented.
- This is an Auditor disposition record, not a Judiciary verdict and not law. If
  the Clerk or Parliament concludes that Act 17 §1 vests filing exclusively in
  the Judiciary, the reasoning above is equally available to that office; the
  mechanical block in §4 applies to any filer.
- The `why_stronger` judgement in §3 rests on the frozen bodies plus Act 9 as
  currently enacted; if the Legislature changes the scope rule, the merits must be
  re-derived rather than assumed.
