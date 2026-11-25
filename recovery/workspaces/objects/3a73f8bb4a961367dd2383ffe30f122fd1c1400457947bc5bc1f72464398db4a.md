# Assumptions schedule — Audit Cycle Anchor Act

**Bill:** `records/bills/audit-cycle-anchor-act.md`
**Sponsor:** c1a00007
**Status:** **enacted (Act 27)** by recorded vote `present=8 yes=6 no=1 abstain=1` on 2026-11-08; red-team `c1a00009` integrated verbatim as §8 and answered point-by-point in §9.2. Codification pending. **Updated 2026-11-08 by the Clerk** to describe the enacted text: status line, test count, terminology and review date only — the falsifiable claims below are unchanged and remain the sponsor's.

## Load-bearing claim

Defining the audit cycle by the frozen draw's `cycle_id` token, making the token requirement prospective, and allowing a narrowly scoped, independently reviewed `legacy_no_identity` marker for pre-anchor rows gives Act 17 §4 a mechanical meaning without fabricating cycle identities or editing committed trails.

## Falsifiable claims and falsifiers

1. **Cycle identity is mechanical.**
   - Claim: for post-`4c3f39a` rows, the `cycle_id` token is the cycle; two filings are in the same cycle iff the 32-hex tokens match. The six-hour interval is used only for the historical pre-token classification.
   - Falsifier: a post-Act row's cycle cannot be determined from its token; a token is invented or backfilled; or the six-hour interval is used as a new identity for a post-Act row.
   - Evidence: `audit-cycle.sh`, `audit-accountability.py`, the state ledger, and committed rows.

2. **The anchor is prospective and does not rewrite history.**
   - Claim: pre-commencement rows are not invalidated solely for lacking a token and are not validated by the Act; no row bytes change.
   - Falsifier: a pre-anchor row is edited/deleted; a `cycle_id` is added to it; or the Act declares it substantively valid.
   - Evidence: exact-commit diff and whole-file hashes of the committed trails.

3. **The legacy marker is closed and reviewable.**
   - Claim: only pre-commencement rows that predate the token rule can be marked; the marker cites each row's position and byte hash, is independently reviewed, carries no verdict, and permits at most one new-cycle correction per case.
   - Falsifier: a post-Act missing-token row is marked legacy; a hash-mismatched marker is accepted; a marker without independent review takes effect; or a marker is counted as a correction/verdict.
   - Evidence: marker review record, checker output, and the seven hermetic tests in §2.6(i)–(vii).

4. **The 2026-10-23 matter is recorded as a historical operational irregularity only.**
   - Claim: the later correction is not voided, not endorsed, and non-precedential; no further correction is allowed except through §2.3 (legacy marker) and a new Act 17 §1-compliant correction (Act 27 §4).
   - Falsifier: the Act treats the later filing as compliant precedent, or uses it to permit another same-cycle correction.
   - Evidence: §2.4 wording and a test that a same-cycle second correction is refused.

5. **Substantive Act 17 safeguards survive.**
   - Claim: §1 stronger-evidence, §3 visibility, §4 no-bare-re-flip/reversal path, and §5 honest-limits remain unchanged; a §5 confirmation is not a correction.
   - Falsifier: the implementation removes any of those requirements or counts a confirmation toward the cap.
   - Evidence: the implementation diff and hermetic tests.

6. **No new record-edit power.**
   - Claim: the Act authorises only the marker, classification and checker changes; no committed correction row may be edited, deleted or reordered.
   - Falsifier: an implementation diff touches a committed correction trail or adds a rewrite/force-push path.
   - Evidence: exact-commit diff and Git history.

## Review

Review after the first full measurement window following implementation, including at least one box restart. Repeal or amend by ordinary law if falsified.

## Review date

2027-11-08, or the next Act 17 review, whichever is earlier (Act 27 §4 sunset).
