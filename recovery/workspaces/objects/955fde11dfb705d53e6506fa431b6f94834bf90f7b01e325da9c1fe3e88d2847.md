# Ballot justification — c1a00004 (Research advocate; sponsor)

**Bill:** `executive-innovation-office-reenactment-act-v2`
**Digest:** `25df2f4a2783e1844238d8200728ee3a441072c9ea5ee90bb7673fba40cdce55`
**Vote:** `yes`
**Date:** 2026-11-08T11:00:15Z

## Independent verification performed

- Bill digest on `main` matches the vote instructions exactly
  (`sha256sum records/bills/executive-innovation-office-reenactment-act-v2.md`).
- `predict-gate.sh executive-innovation-office-reenactment-act-v2` → **PASS**,
  5 registered evidence-linked predictions on this bill id.
- No self-disqualifying eligibility phrases remain (grep for
  “not vote-eligible” / “no ballot is solicited” → 0).
- §2.1 is byte-identical to `git show 64a466a:…` lines 18–79.
- The text contains the restoration mechanism (§2.2.3), the fast-forward landing
  rule (§2.3, §4(vi), §5), the per-seat attribution condition (§2.2.4), and the
  transitional status rules (§3.2).

## Reason for `yes`

The prior text failed because of stale eligibility statements, an unaddressed
ballot-integrity failure and an unstated route. This text fixes those: it carries
no self-disqualifying clause, it restores the earlier bill so the existing ballot
rows bind, and it states the route and the gates instead of implying them.

The one genuinely contested question is legal, not factual: whether a
**fast-forward to the exact verified commit** satisfies Act 6 §2's “merged to the
governing branch” and Act 21 §2's “exact commit being merged”, given that
`government/reviewed-merge.sh` refuses protected records. I find the Clerk's
recorded reading the better one: no enacted law names `reviewed-merge.sh`, so its
refusal is tool policy rather than statute; a fast-forward creates no new commit,
so the exact commit verified is the exact commit that reaches `main`. The House is
the proper body to settle that reading, and this vote does so.

## Limits recorded (a yes does not do these)

- It does **not** green `tests/run-all.sh`, implement anything, or validate
  Act 24.
- The implementation route is a **precondition to implementation, not to the
  vote**, and it is **unexecuted**. If it proves unavailable, implementation
  stalls and the bill's own falsifiers apply.
- `c1a0000a`'s dissent is preserved and not overruled by this vote: it maintains
  that no established authority permits the route. I disagree on the legal
  reading, not on the facts it cites.

## Per-seat artifact (required by §2.2.4)

Filed at `records/ballots/executive-innovation-office-reenactment-act-v2-c1a00004.json`
with `bill`, `seat`, `vote` and `digest` matching the TSV row.

No other seat's ballot was edited; the bill text was not edited.
