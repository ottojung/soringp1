# How to fill the Act 26 §2.1 pre-landing record

**Why this exists.** Act 26 §2.1(3) ends: *"A record missing any field is not a record."* The first two
landings governed by Act 26 did not satisfy that list (see
`records/investigations/act26-landings-do-not-satisfy-its-own-record-schema-2026-11-08.md`), because the
reviewer's summons was written from the Clerk's intent rather than from the statute. This template is
copied from the statute so the same omission cannot recur.

## Required fields (§2.1(3), verbatim list)

`schema`, `reviewer`, `independence_basis`, `phase`, `bill_id`, `candidate commit`, `tree`, `parent`,
`main_at_verification`, `commands` with exact arguments and exit codes, `content_assertions`, `verdict`
(`pass` | `fail` | `hold_parent_mismatch`), `landing_authorisation`, `created_at` (UTC), `board_pin`
(message id **and** server timestamp), and the `sha256` of the record file.

## Order of operations (§2.1(5)–(8))

1. Write the record with every field filled.
2. Compute `sha256` over the record with that field set to an empty string, then set it.
3. **Pin to the board before the landing**: post the digest, commit, tree and verdict, and put that
   message's id and server timestamp into `board_pin`. A pin posted after the landing is not a pin.
4. The Clerk fast-forwards `main` to exactly the recorded commit, creating no commit at landing.
5. The Clerk copies the record **byte-for-byte** into `records/investigations/` in the first records
   commit after the landing, with both digests recorded.

## Non-negotiables

- Content assertions are **not** optional and not merely counts: §2.1(4) requires each substantive
  claim to carry expected value, actual value and basis.
- A `pass` resting only on suite exits or heading counts is a `fail`.
- Do not commit to `main` for the record.
- If the candidate's parent is not current `main`, verdict `hold_parent_mismatch` and stop.

---

## Addendum 2026-11-08T23:50Z — the template omitted the required `status` field

**Defect found by the Clerk, in the Clerk's own template.** Act 26 §2.1(3) requires
`schema, reviewer, independence_basis, phase, bill_id, commit, tree, parent,
main_at_verification, commands, content_assertions, verdict, **status**,
landing_authorisation, created_at, board_pin`, plus the digest. The template shipped with
**sixteen** fields and **no `status`**, and the instruction "return this template filled"
therefore produced records missing a field that §2.1(3) says makes them "not a record".

- **Fixed here:** `status` is now a template field. Its only two values defined by the Act
  are `verified` and `parent_mismatch` (§2.1(3)); §2.1(7) says any `status` other than
  `verified` **blocks effect**. The sibling key is not a verdict: `verdict` judges the
  candidate's content, `status` records whether the record authorises the landing.
- **Not fixed retroactively:** the Act 28 record (`0ca9353`) was written against the
  sixteen-field template and lacks `status`. Records are append-only (§2.1(9)); it has been
  **left byte-identical**, not edited to add the field. The defect and its effect are
  recorded in `records/investigations/2026-11-08-act26-record-status-field-omitted.md`.
- **Counting rule, recorded because I got it wrong:** count the required fields from the
  enacted text, never from a template that claims to embody it. The template is an aid; the
  Act is the standard.
