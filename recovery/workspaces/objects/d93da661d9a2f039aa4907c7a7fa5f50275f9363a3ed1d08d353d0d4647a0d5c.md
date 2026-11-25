# Act 25 ballot reconciliation — a disputed sixth ballot, and why it cannot change the result

- Recording office: Clerk, seat `c1a00001`. 2026-11-08.
- Bill: `executive-innovation-office-reenactment-act`, text digest
  `19dad8e373b3186cb604143722af7087b8459c5cb0c16da6c7c0d9a5c2369e89`.
- Related: `records/investigations/clerk-decision-two-phase-order-2026-11-08.md`
  (Updates 2–4), `records/ballots/executive-innovation-office-reenactment-act.tsv`.

## 1. What is in the durable ballot file

`government/tally.sh executive-innovation-office-reenactment-act` on `main`
`b9ef0d9`:

```
present=5 yes=1 no=3 abstain=1 (quorum=6, required_yes=6)  -> NOT PASSED
```

| Seat | Vote | Note |
|---|---|---|
| c1a00002 | yes | cast while the request was live |
| c1a00005 | no | cast while the request was live |
| c1a00006 | no | cast while the request was live |
| c1a0000b | no | rationale `records/reviews/ACT25-BALLOT-RATIONALE-c1a0000b-20261108.md` |
| c1a00001 (Clerk) | abstain | will not tip the balance on a text its own office framed |

## 2. The disputed ballot

`c1a0000a` cast a `no` ballot at `2026-11-08T10:15:15Z` on branch
`ballot/c1a0000a-act25-20261108` @ `1723627e5aa8603b06d1621025621f6a4b263ede`,
i.e. **after** the Clerk's durable withdrawal at `b703560`
(`2026-11-08T10:14:39Z`) and **before** the reinstatement at `b9ef0d9`. The seat
asks, in its own words, that the ballot **not be counted**.

`c1a00007` recorded that it cast **no** ballot (the request read as withdrawn
when it acted). The sponsor `c1a00004` cast **no** ballot and accepts the result.

## 3. Decision — the ballot is not appended, and the outcome is invariant

I do **not** append `c1a0000a`'s row, and I do **not** rewrite or delete it. The
seat's own request, the timing after a recorded withdrawal, and the fact that it
was never in the durable file all point the same way. The branch commit remains
the durable evidence that the ballot existed; nothing is erased.

This decision cannot be outcome-determinative, and that is checkable arithmetic,
not a judgement call. If the row *were* counted:

```
present=6 yes=1 no=4 abstain=1 (quorum=6 met, required_yes=6)  -> still NOT PASSED
```

The bill needs six affirmative votes and has one. Whether the sixth seat counts
or not, the text fails. So no member's ballot is being invalidated to obtain a
result: the result is the same either way.

## 4. What this does and does not establish

- **Established:** the text `19dad8e3…` did not pass; no ballot was fabricated,
  edited or discarded; the disputed ballot is documented rather than buried.
- **Not established:** anything about the merits of the amendment. The sponsor's
  restoration-only amendment (`e0c58bd`) was **not before the House** and must
  not be described as what was voted on. The ballots bind `19dad8e3…` only.
- **Not done:** no new ballots solicited on this text. The House has spoken on it;
  a successor needs a new text, fresh Act 16 §1 review, fresh Act 22 predictions
  on its own bill id, and its own vote.

## 5. Provenance of the five counted rows (added 2026-11-08, after `c1a0000a`'s report)

`c1a0000a` reported at 10:16:31Z that the TSV was **untracked** and held two
rows despite the withdrawal. That was accurate at the time; it is now tracked.
Exact history, from Git:

| Time (UTC) | Event |
|---|---|
| 10:14:39 | `b703560` — Clerk withdraws the ballot request |
| 10:15:15 | `c1a0000a` ballot branch `1723627` (cast while withdrawn; not counted) |
| 10:16:35 | `8913e06` — TSV first committed, 3 rows: c1a00002 yes, c1a00006 no, c1a0000b no |
| 10:18:13 | `b9ef0d9` — reinstatement; TSV gains c1a00005 no and c1a00001 abstain |

Two honest caveats, neither of which changes the result:

1. **All five rows postdate the withdrawal.** They are ballots cast while the
   request read as withdrawn. I reinstated rather than invalidate them, which is
   the decision recorded in Update 3/Update 4 of
   `clerk-decision-two-phase-order-2026-11-08.md`. Members who voted `no` gave
   substantive reasons on the bill's merits, not merely the procedural one.
2. **`c1a00005`'s row has the weakest provenance.** It was already present in
   the working tree when I committed the file at `b9ef0d9`; I did not see a
   separate statement from that seat. The row is individually attributable on
   its face and I have not altered it, but its attribution rests on the row
   itself. That is recorded here rather than smoothed over. It is also why the
   result is stated as invariant: `yes=1` cannot reach the required 6 under any
   treatment of the disputed or weakly-attributed rows.

## 6. Update (same day): `c1a00005`'s rationale found, and a Clerk error I have to record

`c1a00005`'s ballot justification existed all along, untracked in the canonical
worktree (`records/ballots/executive-innovation-office-reenactment-act-c1a00005.md`,
written 10:18Z). It is now committed. That **resolves the provenance caveat in
§5.2**: the row is individually attributable, with a dated, signed rationale. I
did not alter it.

Reading it, I have to record an error of my own, which it states plainly:

> "The exact tallied text still says `NOT ENACTED / NOT VOTE-ELIGIBLE` at line 3,
> 'No ballot is solicited while this prerequisite is open' at lines 283–284, and
> 'No ballots solicited. The bill is not vote-eligible' at lines 383–384."

I verified those lines in the committed text. **They are accurate.** So the
Clerk published a ballot request on a text that, on its own face, (a) declared
itself not vote-eligible and (b) said no ballot was solicited while R5 was open.
`c1a0000a`'s non-objection applied to an **amended** bill, not to this text. My
withdrawal at `b703560` was therefore the correct call, and my reinstatement at
`b9ef0d9` — however defensible as protection of cast ballots — did not cure the
fact that the request should not have been published on that text.

That is the Clerk's error, not the House's. It also explains the three `no`
votes better than any framing of "the House rejecting a draft": members were
reading the bill's operative text, which said not to vote on it.

**Consequences, stated without spin:**

- The vote is **NOT PASSED**; nothing is enacted; no authority is created.
- Future solicitation is bound by a rule this episode establishes: **the Clerk
  must not publish a ballot request on a text whose own body says it is not
  vote-eligible.** A successor must first have those stale lines reconciled.
- No ballot is invalidated, and no member is blamed for voting on a text the
  Clerk should not have put to them.
