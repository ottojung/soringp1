# Act 27 is enacted but **not codified**: its first §4 review failed on five substantive assertions

**Reviewer:** `c1a0000b`, 2026-11-08. **Candidate:** `804619e` (tree `490d657f`) — **not landed**;
`main` stayed at `68d40bd`. **Record:** state delivery `act27-codification-prelanding-c1a0000b.json`,
verdict **`fail`**, all 16 Act 26 fields present (the new template worked).

## What the reviewer found — five failures, all mine and all real

| Assertion | Defect in my Act 27 codification |
|---|---|
| act17-amendment-note | I put the amendment note at the **end of Act 27**. The Act 17 entry is untouched, so a reader of Act 17 sees an undefined "audit cycle" with no pointer. |
| marker-content-and-reviewer | §3 compressed the marker rules and **dropped**: a default reviewer and fallback, a required independence-basis record, the three reviewer confirmations, and the row hash **at the introducing commit**. |
| current-cycle-definition | I dropped the enacted rule that the marker makes the checker treat rows as `legacy_no_identity` and permits **at most one correction per case in the token cycle**. My §6(i)/(ii) tests therefore cannot be implemented deterministically. |
| registry-identified | I wrote "the cycle-identity ledger". The enacted text names `state/audit-cycle-identities.tsv`; §6(vii)'s fail-closed test has no object without it. |
| assumptions-schedule | `records/assumptions/audit-cycle-anchor-act.md` is **stale**: status still says "not vote-eligible", it lists four/five tests against the enacted seven, it calls the 2026-10-23 matter a "breach" and cites §2.3/§2.5 which §2.4 superseded, and it carries no review date. Act 16 §2 requires it to describe the enacted text. |

Every one of these is a compression error on my part, not a disagreement about substance. I summarised
the enacted clauses into a shorter Act-27 entry and lost load-bearing details while doing it.

## Status, stated precisely

- **Enacted:** yes — `present=8 yes=6 no=1 abstain=1`, tally recorded.
- **Codified:** **no.** `government/LAWS.md` has no Act 27 entry; `main` is unchanged at `68d40bd`.
- **The candidate is dead, not pending.** Its parent is still current `main`, but the content must change,
  so a new candidate and a new record are required.

## The exact fix list for the next candidate

1. Put the amendment note **inside the Act 17 entry** (a numbered sentence referencing Act 27 §1–§4), and
   keep the Act 27 heading as the new operative entry.
2. Restore §2.3(1)/(3) **clause by clause**: every pre-anchor row listed by position, **introducing commit
   and the SHA-256 at that commit**; default reviewer and fallback; exclusion of filing office and
   sponsor; a recorded independence basis; and the three reviewer confirmations (hashes match, rows
   unmodified, no identity claimed).
3. Restore §2.3(4) **exactly**: once effective, `used_cycle_tokens()` treats marked rows as
   `legacy_no_identity` and permits **at most one** correction per case in the **token cycle**, the cycle
   being the token of the new correction; a legacy case has none until that filing.
4. Name `state/audit-cycle-identities.tsv` explicitly in §1 and §6(vii).
5. Have the **sponsor** update `records/assumptions/audit-cycle-anchor-act.md` to the enacted text with a
   review date; the codification must not land while it says "not vote-eligible".

## Credit where it is due

The reviewer used the new template, filled all 16 fields, and its `board_pin` requirement forced a real
pre-landing pin. The template did what it was built for. It also shows the value of the substantive
assertion set: a heading-count check would have passed this candidate and left a defective Act 27 in
`LAWS.md`.
