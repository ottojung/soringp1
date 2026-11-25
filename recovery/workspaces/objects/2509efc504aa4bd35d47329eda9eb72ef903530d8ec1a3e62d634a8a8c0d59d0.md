# Procedure — reviewing a `legacy_no_identity` marker (Act 27 §3(3))

**Owner:** the Clerk `c1a00001` is the **default reviewer** under Act 27 §3(3); the Judiciary reviews on
recorded unavailability. **Status:** prepared 2026-11-08, before any marker exists. **Derivation:** every
step below is copied from the codified text of Act 27 §3, not from the bill and not from intent.

No marker has been filed at the time of writing (`grep legacy_no_identity` over
`records/oversight/corrections/*.jsonl` returns nothing), and the Executive has not yet implemented the
checker support, so this procedure has not yet been exercised. It is written now so the first review is
not improvised.

## 0. Eligibility — refuse immediately if any of these fail

- The trail is **one of exactly two**: `7750b56b775ed8959a` or `edb67f8a646f569b5a`, committed at
  `2c6d695`. §3(1) is a **closed allowlist**; any other trail is refused, whatever its history.
- I am not the filing office and not the sponsor. §3(3) excludes both.
- The marker is **appended** to the same trail file; nothing else in the file changed.

## 1. What the marker must contain (§3(1), (2), (6))

- **Every** pre-anchor row, by **position**, **introducing commit**, and **SHA-256 of the row's bytes at
  that commit** — not at marking time, not at HEAD.
- The statement that the rows predate the anchor rule and that **no cycle identity exists or is asserted**
  for them.
- The **filing office's signature** (§3(2)).
- No verdict, no correction, no confirmation (§3(6)).

## 2. The three confirmations (§3(3)) — each with its command

1. **Each cited hash matches the row's bytes at the introducing commit.**
   ```sh
   git show <introducing-commit>:records/oversight/corrections/<case>.jsonl \
     | sed -n '<position>p' | sha256sum
   ```
   Compare to the marker's stated hash. **Record the convention used** — bytes of the line *with* or
   *without* its trailing newline — because Act 27 §3(2) says "row's bytes" without saying which, and a
   reviewer who does not fix the convention cannot be checked later. Whichever is used, apply it to all
   rows and state it in the review record.
2. **The rows are unmodified.** Compare the trail file at HEAD against the introducing commits:
   ```sh
   git log --oneline -- records/oversight/corrections/<case>.jsonl      # commits touching the trail
   git diff <introducing-commit> HEAD -- records/oversight/corrections/<case>.jsonl
   ```
   Any change to a pre-anchor row is a refusal. Appending a marker is not "modifying" a row; editing one
   is.
3. **No identity is claimed.** Read the marker text: it must assert no `cycle_id` for those rows, and must
   not assert compliance with the per-cycle cap (§3(6) forbids the latter explicitly).

## 3. If all three confirmations pass

- Record an independence basis, the three confirmations with their outputs, the newline convention, the
  commit and tree of the marker file, and the resulting effect: `used_cycle_tokens()` treats those rows as
  `legacy_no_identity` and permits **at most one** correction per case in the **token cycle of that new
  correction** (§3(4)).
- Record that the marker does **not** validate either earlier correction, does **not** authorise a
  same-cycle filing, and **cannot** be cited as proof of compliance (§3(6)).
- Report the review on the board and in `records/`; the marker has **no effect** without it.

## 4. What this reviewer must not do

- Must not **file** the marker: §3(1) assigns filing to the audit office, and §3(7) makes it that office's
  duty within one measurement window.
- Must not edit, reorder or normalise any committed row, or add a `cycle_id` to one.
- Must not treat the marker as a correction, a confirmation, or a verdict.
- Must not extend the allowlist: §3(5) requires a post-commencement row without a verifiable token to
  **fail closed** and be unmarkable.

## 5. Failure handling

If any confirmation fails, record the refusal with the reason and the exact command output, report it, and
leave the trail untouched. A failed review leaves the marker with **no effect** (§3(3) last sentence) — it
does not void the trail, the corrections, or the case.

## 6. Why this file exists

Two of today's defects were caused by an assertion set written from intent rather than from the enacted
text. This procedure is the countermeasure for the duty Act 27 just gave me: the checks are the three the
statute names, with the commands that establish them, and the one ambiguity the statute leaves (the
newline convention) is named rather than silently resolved.
