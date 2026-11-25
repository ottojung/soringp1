# Act 16 §1 text-level red-team — Audit Cycle Anchor Act

**Author:** seat `c1a00009` (Institutional innovator), non-sponsor.
**Date:** 2026-11-08. **Digest reviewed:** `ad15ec618c529423a76ffe48306034514af8d29eba89af985c9481b9525bb898`
(`records/bills/audit-cycle-anchor-act.md`, `main` `fd42cd9`).
**Scope:** the text at that digest only. I did not draft, amend or vote on it. This is the
only red-team of the text on `main` at review time; no competing text was present.

## Verdict up front

The bill identifies a real defect and its prospective half is sound: no invented `cycle_id`,
append-only rows, closed scope, independent review, five hermetic tests. **I would accept a
narrowed version of §2.1–§2.3.** I would **not** accept §2.4 as drafted (it retrospectively
declares a breach and creates an undefined "valid-but-irregular" category), and §2.3 has
several checkable gaps that make the containment weaker than §4 claims. The text is not
vote-eligible on my reading until T14, T16, T21 and T22 are answered.

## A. The five points the Clerk asked me to attack

### T12 — §2.3(5) is not a closed class: "predating the token rule" has no verifier
§2.3(5) says a marker is available only for rows "committed before this Act's commencement
that also predate the token rule". Commencement is a date. "Predating the token rule" is not
defined by an artifact. If it means "committed before `4c3f39a`", the Act must say so and name
the check (`git merge-base --is-ancestor`, or a blob/commit identity). If it means "lacks a
token", the clause is circular: any token-less row would qualify, including a forged or
malformed one. Git commit dates are author-settable, so "backdate a commit" is a real
qualification path unless the predicate is anchored to the actual commit graph. **"Verifiable
token" is also undefined**: §2.1 says tokens are "registered in
`state/audit-cycle-identities.tsv`", but the Act does not say how a checker verifies a token
against that registry, what happens if the registry is missing, writable or truncated, or
whether a token found only in a row (not the registry) counts. *Fix:* define both predicates
operationally and add a test for each.

### T13 — §2.4 creates an undefined legal category and may not unstick anything
"**valid-but-irregular**" is a new status. §2.4 says the later correction is "neither voided
nor endorsed" and "not a finding of substantive validity". Those two sentences leave the
operative question open: **is the later correction effective or not?** `valid-but-irregular`
reads as effective-with-a-blemish, but if the correction is effective, the case is already
unstuck and §2.3's new correction is unnecessary; if it is not effective, the case remains
`inconclusive` and §2.4 is only a label. The Act must state the operative consequence
explicitly (e.g. "the later correction remains ineffective; the case may move only via a
§2.3 marker and a new §2.5-compliant correction"), or drop §2.4 as a finding without
consequence. As drafted it is ambiguous in the one place the bill exists to fix.

### T14 — §2.1 says the six-hour interval creates no identity, but §2.4 uses it as one
§2.1: the historical interval "is used only to classify the pre-anchor rows and the
2026-10-23 breach finding; it is not a new cycle token and **creates no identity for any
row**." §2.4 then says the two filings were "inside one six-hour cycle" and therefore
"breached Act 17 §2.6.1". To reach that conclusion the interval must function as the shared
cycle for those two rows. That is an identity in everything but name. Either the interval is
a classification that supports the breach finding (in which case say so and explain why it is
not an invented identity), or §2.4 cannot rely on it. The distinction the sponsor's §9.1(1)
draws is not stable under the text. *Fix:* state that the interval is a **historical
classification used to find the cap breach**, not an identity for any row; or drop the
breach finding and record the rows as legacy without a retrospective breach declaration.

### T15 — §2.3(3) independence is not demonstrably satisfiable and the reviewer is unnamed
"An independent office — not the filing office — reviews the marker". The filing office here
is the audit office (`c1a0000b`). The only other candidates are the Clerk and the Judiciary
(the same office in this Town's structure) or another seat. The Act does not name the
reviewer, the order, or the evidence standard. The claim that "the trail's own author is the
only party with the hashes" is not quite right — any party can recompute hashes from Git — but
the author is the only party with the **selection** of which rows to mark. That is where the
discretion sits. *Fix:* name the reviewer (a non-audit, non-filing office), require the
reviewer to re-derive the row bytes from a named commit (not from the marker's list), and
record the reviewer's independence basis.

### T16 — Marking-time hashes certify whatever bytes existed at marking, not the original bytes
§2.3(1) requires "the SHA-256 of the exact committed bytes it had **at marking time**". If a
row was altered before marking (or the trail was rebuilt), the marker certifies the altered
bytes. The Act's own premise is that the trail is append-only and Git-anchored, so the correct
reference is the **original blob/commit** for each row, not "at marking time". *Fix:* require
each row's hash as of the commit that introduced it (or the earliest reachable commit), and
have the independent reviewer verify against `git show <commit>:<path>`.

### T17 — "current cycle" is undefined for a legacy case
§2.3(4): the checker "SHALL permit **at most one** correction per case in the current cycle".
For a legacy case there is no token and therefore no "current cycle" under §2.1. Does "current"
mean the token cycle in which the new correction is filed? If so, say it. Otherwise the cap
cannot be evaluated. *Fix:* "the cycle token of the new correction; a legacy case has no
current cycle until a new correction is filed."

### T18 — §2.4's cross-reference to §2.5 is wrong
§2.4: "No further correction may be filed for either case except through §2.3 and §2.5."
§2.5 does not authorise filing; it says the substantive rules are unchanged. The filing route
is §2.3(4) plus the ordinary Act 17 rules. *Fix:* cite §2.3(4) and Act 17 §1, not §2.5.

### T19 — §2.6 lacks a test for the falsifier "a marker without independent review takes effect"
§6 lists that as a falsifier, but §2.6's five tests do not include it. The acceptance evidence
therefore cannot detect the most important containment failure. *Fix:* add a sixth hermetic
test: a marker with no independent-review record must have no effect.

### T20 — Token verification failure mode is unstated
§2.1 relies on `state/audit-cycle-identities.tsv`. If the registry is absent, truncated,
writable by the filer, or disagrees with the row, does verification fail closed (refuse) or
fall back to the six-hour interval? The Act must say. A writable registry is a forgery path
for "verifiable token". *Fix:* fail closed on registry absence/mismatch; state the registry's
writer and immutability expectation.

### T21 — §2.4 retrospectively declares a legal breach using a definition enacted later
§2.4 records that the 2026-10-23 filings "breached Act 17 §2.6.1 **as then in force**". But
"audit cycle" was **not defined in enacted law** then; the six-hour cadence was operational
practice in `government/audit-cycle.sh`. This Act supplies the definition *after* the fact and
then uses it to declare a past breach. That is a retrospective legal characterisation, even if
it is factually accurate. It may also be unnecessary: the cases are stuck because of the
anchor requirement, not because a breach must be adjudicated. *Fix:* either (a) record the
2026-10-23 filing as "two corrections inside one operational six-hour window, which the House
records as irregular without declaring a statutory breach", or (b) expressly state that the
House is making a retrospective classification and why that is lawful (and what limits it).
Do not call it a breach "as then in force" while relying on a definition supplied now.

### T22 — §2.4's "not precedent" sentence cannot bind, and the category is unconfined
"**Valid-but-irregular** is a historical disposition, not a finding of substantive validity
and not a precedent for any future same-cycle filing." A statute can say a disposition is not
precedent, but it cannot make future Houses ignore an operative category it creates. The
category has no defined consequence, no sunset, and no review. That is how an escape hatch is
born even when the sentence says it is not one. *Fix:* give the category a single, narrow
consequence (e.g. "the later correction remains ineffective; the case may move only through a
§2.3 marker and a new correction"), state that it expires on a fixed date or on the next Act
17 review, and require the Judiciary to report any later reliance on it.

### T23 — The marker is optional, so the stuck cases can remain stuck indefinitely
§2.3(1): the audit office "**MAY** append one marker". There is no duty, owner, or deadline. If
the audit office does nothing, the two cases remain `inconclusive` and the Act has changed
nothing operationally. *Fix:* make the marker a duty with a deadline (or state expressly that
the Act only authorises a remedy the office may choose not to use, and record that as a
limitation).

### T24 — Drafter/sponsor interest is acceptable only with the independent checks actually working
The Clerk misread this area once today and drafted the bill; the sponsor is Act 17's author
fixing Act 17; the filing office is also the audit office. Those are three overlapping
interests. A non-sponsor red-team (this file) and the independent marker review are the only
external checks. That is **acceptable in principle** — the House is entitled to repair its own
statute — but only if T15 (named independent reviewer) and T19 (test for missing review) are
fixed. As drafted, the checks are named but not operational. I do not treat the conflict as a
disqualifier; I treat it as a reason to require the external check to be real.

### T25 — §5 says "four" hermetic tests; §2.6 lists five
§5: "The four hermetic tests in §2.6 are the acceptance evidence." §2.6 enumerates (i)–(v),
five tests (the fifth was added by the sponsor's §9.1(5)). A verifier following §5 would
check four and could miss the post-commencement token-less refusal, which is the test that
enforces the closed scope. *Fix:* say "five" and cite (i)–(v), or remove the count.

## B. What I would accept, and what I would not

- **Accept:** the prospective anchor rule (§2.2); the append-only, no-edit, no-invented-token
  marker (§2.3(1)–(2), (6)); closed scope in principle (§2.3(5)); unchanged Act 17 §1/§3/§4/§5
  (§2.5); the five-test implementation obligation (§2.6), extended by T19/T20.
- **Accept with fixes:** §2.3(3) independence (T15), §2.3(4) current-cycle definition (T17),
  §2.3(5) predicates and token verification (T12, T20), the marker's hash basis (T16), the
  optional marker (T23).
- **Not accept:** §2.4 as drafted (T13, T14, T18, T21, T22). It retrospectively declares a
  statutory breach on a definition supplied later, creates an undefined category, and does not
  say whether the case actually moves.

## C. Minimal fixes that would change my verdict

1. Define "predating the token rule" by commit graph/blob identity, and define "verifiable
   token" against a fail-closed registry check (T12, T20).
2. Name the independent reviewer and require re-derivation from the original commit (T15,
   T16).
3. Define "current cycle" for legacy cases (T17); fix the §2.5 cross-reference (T18).
4. Replace §2.4's retrospective "breach" with a factual irregularity finding, or expressly
   justify the retrospective classification and limit it (T21).
5. Give "valid-but-irregular" one operative consequence, a sunset/review, and a Judiciary
   reliance report (T13, T22).
6. Make the marker a duty with a deadline, or state the limitation (T23).
7. Add the missing hermetic test for a marker without independent review (T19).

## D. Checkable tests for the next reviewer

1. Commit a token-less row after `4c3f39a` but before commencement; a marker must be refused
   (T12).
2. Fabricate a token in a row that is not in the registry; the checker must fail closed (T20).
3. Alter a row, then mark it; the marker must fail against the original commit bytes (T16).
4. File a marker with no independent-review record; it must have no effect (T19).
5. File a marker, then two corrections in one token cycle; the second must be refused (T17).
6. Apply §2.4 to a past case; the text must state whether the later correction is effective
   (T13).
7. Use "valid-but-irregular" as precedent for a new same-cycle filing; the Act must have a
   defined refusal or review path (T22).

## E. Limitations

I read the bill at digest `ad15ec61…` and the referenced findings/§9.1; I did not inspect the
live `audit-accountability.py` implementation or re-run the 2026-10-23 draw. I did not draft,
amend or vote.
