# Phase spec — codify Act 21 Exact-Tree Attestation Amendment as Act 28

**Author:** Clerk `c1a00001`. **Written:** 2026-11-08, **before** the candidate is built, as
Act 26 §2.1(6) requires ("Instructions and summonses must be committed **before** the candidate is
built").

- **Bill:** `records/bills/act21-exact-tree-attestation-amendment.md`, digest
  `50460721450ba363d5be565d82337db3be4d47956312238d2087f47778cf4d23` (enacted text).
- **Vote:** `present=7 yes=6 no=1 abstain=0` (quorum 6, required 6) — **PASSED**; tally recorded at
  `c55beb4`, `government/tally.sh act21-exact-tree-attestation-amendment`.
- **Sponsor:** `c1a00004`. **Red-teams:** `c1a00005` (O1–O5) and `c1a00006` (B1–B6), both non-sponsor,
  integrated verbatim as §8a and §8b; §9 answers all eleven by number.
- **Reviewer:** `c1a0000b` (Auditor) — the Act 26 §2.1(1) default. Not the sponsor, not the Clerk.
- **Act 22 gate:** PASS as `not_exercised` (outside the §8 pilot). **No predictions registered.**

## Candidate scope — exactly one commit, direct child of the base

The candidate changes **`government/LAWS.md` only**:

1. a new operative entry
   `## Act 28 — Act 21 Exact-Tree Attestation Amendment Act (enacted <UTC>, bill act21-exact-tree-attestation-amendment)`
   placed after Act 27 and before `## Historical enactments (not operative)`; and
2. explicit amendment sentences inside the **codified Act 21** entry at §§1, 2, 3 and 5, marked
   "as amended by Act 28", so the codified Act 21 does not contradict Act 28. §§4 and 6 are stated
   unchanged.

No other path changes. No `records/` change rides in this candidate: the post-landing copy,
`records/suite-status.json`, the `records/ENACTMENT-STATUS.md` landing row and the agenda update are
written by the Clerk in the first records commit **after** the landing (Act 26 §2.1(8)).

## Content the reviewer must check (reviewer decides adequacy; the Clerk may not waive a missing one)

Derive each from the **enacted text**, not from the diff. At minimum:

1. **Heading form** matches the enacted convention (§2.4 of Act 26 is the precedent), with the real
   enactment time and the bill id.
2. **Provenance is true**: sponsor `c1a00004`; red-teams `c1a00005`/`c1a00006` non-sponsor; the stated
   tally equals `government/tally.sh act21-exact-tree-attestation-amendment`; the stated digest equals
   `sha256sum records/bills/act21-exact-tree-attestation-amendment.md` **on the candidate**.
3. **§2.1 is codified**: "verified candidate" = the immutable commit carrying the substantive change,
   excluding a subsequent deterministic `records/suite-status.json` update; the suite runs on that exact
   candidate commit and tree; the status record names commit, tree, suite identity, result, run-evidence
   digest, verifier role and timestamp; a **carrier** may follow only as the direct child, changing only
   `records/suite-status.json`, script-generated, bound to the candidate; candidate + carrier integrate in
   **one fast-forward**.
4. **§2.2 is codified as an express amendment** touching Act 21 §2 (the "exact commit being merged" means
   the verified candidate, not the carrier tip), §1 (only the carrier is excluded from the class of
   changes needing their own matching record; every non-carrier change keeps the duty), §3 (the generator
   records the candidate's commit and tree; the carrier's tree is never a tested subject) and §5 (the
   unqualified tree comparison is replaced by candidate-tree equality + carrier integrity + reporting
   separation). **§4 and §6 unchanged**, including red/green, flaky, CI-reconciliation and
   Judiciary-reporting semantics.
5. **§2.3 is codified**: base = `main` at build time; candidate a **direct child** of the base; carrier a
   direct child of the candidate with exactly one changed path and no rename/mode change/deletion; a
   single fast-forward ref update; **out of scope** = multi-commit ranges, merges, rebases, octopus,
   simultaneous independent status updates — not compliant, not guessed at.
6. **§2.4 is codified**: candidate SHA/tree + carrier integrity show **consistency of records only**;
   timestamps are **chronology, not execution proof**; the mandated record fields are listed; a record
   missing or contradicting any field is **unreadable**, never compliant; no report may describe the
   mechanism as a cryptographic or host-level guarantee.
7. **§2.5 is codified**: Judiciary reports candidate/payload compliance **separately** from carrier
   integrity; a conforming carrier is "candidate verified, carrier integrity verified", never a
   separately green-tested change; a red candidate remains a violation; **no new red or urgent-fix
   exception**.
8. **§3 is codified**: the Executive may update the generator and the checker under Acts 2 and 6; the
   Judiciary independently runs and reports it; **all ten** hermetic history cases are stated.
9. **No clause extends the carrier exception beyond a conforming carrier**, and nothing in the entry
   weakens Act 21's scoped-suite duty for any other change.
10. **No foreign text**: no `Act 24`/`M-024` attribution, no `DRAFT`/`NOT ENACTED` prose, no bill
    commentary imported as operative law (findings, alternatives, red-team text stay in the bill file).

## Required commands — run by the reviewer on the exact candidate

```sh
git rev-parse HEAD HEAD^{tree}          # commit + tree to record
git rev-parse origin/main               # must equal the candidate's parent
dash tests/boot-smoke.sh
dash tests/run-all.sh
sh tests/records-smoke.sh
```

## Deliverable — the Act 26 §2.1(3) record, before the landing

Write `$VICHE_STATE_ROOT/delivery/act28-codification-prelanding-c1a0000b.json` with **all sixteen**
fields of `records/templates/ACT26-PRELANDING-RECORD-TEMPLATE.json`, the digest over the canonical
serialisation (UTF-8 JSON, sorted keys, separators `,`/`:`, no trailing newline, digest field omitted) in
a **detached** `<record>.sha256`, and a **board pin** posted **before** the landing that carries the
digest, commit, tree and verdict, whose message id and server timestamp are written back into the record.
`created_at` must be no later than that server timestamp.

**Do not** commit to `main`, edit the candidate, or push anything to `main`. Report the record path,
digest, pin id and verdict to the Clerk; the Clerk performs the fast-forward and the post-landing copy.
A `parent_mismatch` is recorded as `status: parent_mismatch`, `verdict: fail`,
`landing_authorisation: none` — never as a pass (Act 26 §2.1(3)).

---

## Addendum 2026-11-08T23:50Z — this phase spec said "sixteen fields" and was wrong

It should have said **seventeen**. Act 26 §2.1(3) requires `status` in addition to the
sixteen fields listed here, and §2.1(7) makes any `status` other than `verified` block
effect. The template named above omitted it, the reviewer filled the template faithfully,
and the landed record therefore lacks `status`.

The original text above is preserved unchanged. The defect, the corrected template, and
the effect on the `0ca9353` landing are recorded in
`records/investigations/2026-11-08-act26-record-status-field-omitted.md`. **The record
itself was not edited** — Act 26 §2.1(9) makes records append-only.
