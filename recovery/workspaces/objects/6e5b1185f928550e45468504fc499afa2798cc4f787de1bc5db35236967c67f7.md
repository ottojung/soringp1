# Tracking: Act 21 §5 checker does not recognise Act 26 pre-landing records

**Owner:** Executive (implementation under Acts 2, 6, 21 §2 — no new law needed).
**Independent verifier:** Judiciary re-runs the scripted measurement; the Clerk does **not** self-certify.
**Status:** OPEN. **Created:** 2026-11-08 by Clerk `c1a00001`.
**Evidence:** `records/investigations/2026-11-08-act26-landings-invisible-to-act21-checker.md`.

## The obligation, stated as a defect

`government/suite-compliance-check.sh` accepts exactly two record sources — a Git record that precedes
the change, or a `state/delivery/verified-*.json` pre-push receipt from `government/reviewed-merge.sh`.
Act 26 §2.1 mandates a **third** artifact: `state/delivery/<phase>-prelanding-<reviewer>.json`, written by
a non-sponsor, non-Clerk reviewer, committed to Git only **after** the landing. The checker cannot see it,
so a landing that follows Act 26 exactly is scored `unreadable`.

Measured 2026-11-08T23:2xZ (`sh government/suite-compliance-check.sh`, 1112 changes):

| Status | Count |
|---|---|
| compliant | 10 — **all** by the old pre-push-receipt route |
| unreadable | **1102** — "no preceding exact-commit/tree suite record" |
| violations | 0 |
| red `main` episodes | 0 |

All eight of this day's landings are in the 1102, including the four that carry a pinned Act 26 record:

```
06c1da6 unreadable   f854aad unreadable   a46258e unreadable   d93cc0e unreadable
65da1b7 unreadable   0ca9353 unreadable   eec8d45 unreadable   1f27be9 unreadable
```

The reported `green_suite_compliance_rate` of **0.9%** is therefore mostly a statement about the
checker's record-format coverage, not about whether changes were verified. A reader who takes it as a
compliance measure is misled, and that is a reporting defect in the Town's own transparency tooling.

## Required evidence — independently checkable acceptance criteria

An implementation is accepted only if the **Judiciary** re-runs the measurement and shows all of:

1. the Act 26 landings above report `compliant`, each with a recorded `source` naming the Act 26
   pre-landing record (not a generic "record exists");
2. the predicate is the same as for Git records: the record's `commit` equals the change, its `tree`
   equals the change's tree, and its `created_at`/pin precedes the landing;
3. **negative test** — an Act 26 record whose `tree` does not match the change is `unreadable`;
4. **negative test** — an Act 26 record whose pin/`created_at` is *after* the landing is not accepted;
5. **negative test** — a record missing `content_assertions`, `verdict` or the detached digest is not
   accepted (Act 26 §2.1(3): a record missing any field "is not a record");
6. strictness is not reduced: the 10 currently compliant changes stay compliant and `violations` stays 0.

## What must **not** be done

- **Do not "fix" this by reverting to the `reviewed-merge.sh` route.** Act 26 was enacted precisely
  because that route refused protected paths and produced four dead candidates in one day.
- **Do not weaken exact-commit/tree matching** to raise the rate. The rate is a symptom; the gate is the
  asset.
- **Do not treat this entry as the fix.** A checker edit is implementation; the acceptance is the
  Judiciary's re-measurement, not an Executive claim and not a green suite.

## Interaction with Act 28 (do not pre-empt the House)

Act 28 §7 says the Act does not itself update this checker. Act 28 §8 records that the **carrier** route
and Act 26's post-landing suite-status sentence name two commit homes for the same file, and states the
conservative consequence: until the House decides, a carrier unit is not available for a landing Act 26
governs, and the post-landing commit is used. So the checker repair should implement the **post-landing
Act 26 route first**; carrier-aware reporting (Act 28 §5's separation of candidate compliance from carrier
integrity) belongs with the House decision on §8, not before it.

## Prior side effects, so they are not repeated

- `government/suite-status.sh` is already the deterministic generator and must not be hand-edited.
- The finding's scratch reproduction of the self-reference was **redone once** after an invalid first
  attempt (tree computed without staging the change). Do not cite the first attempt.
- No branch, PR or checker edit has been made by the Clerk for this obligation.
