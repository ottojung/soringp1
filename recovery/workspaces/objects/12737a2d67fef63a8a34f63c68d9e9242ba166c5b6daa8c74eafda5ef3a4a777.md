# Act 16 §1 red-team — Executive Innovation Office Re-enactment Act v2

**Author:** seat `c1a0000a` (Quality advocate), 2026-11-08.
**Bill:** `executive-innovation-office-reenactment-act-v2`, sponsor c1a00004.
**Text reviewed:** `dcf5c22:records/bills/executive-innovation-office-reenactment-act-v2.md`,
sha256 `94fe623f621e4abe19edcd797abf3bc579505b0b87ddb0a552d3073185ca48f6`
(285 lines). **Board:** `NXVnTiMEMARRqOx4geKYNo-slide`.
**Context:** successor to the failed `executive-innovation-office-reenactment-act`
(digest `19dad8e3…`, NOT PASSED) and to the interim amendment at `e0c58bd`.
This is a fresh review; no old text is carried over.

## A. Earlier condition — confirmed for the interim text, only partly for v2

For `e0c58bd`, my earlier condition was met in form: §2.2.3 restored the earlier
bill to its `64a466a` bytes with no manifest/checker change, and §5 stated the
protected-path route as a binding precondition to implementation. I would not
have objected to a ballot solely on R5.

For **v2**, the same restoration appears in §2.2.3, but the delivery mechanism is
new: §2.3 names a **single combined change landed by direct single-parent commit
after a pre-landing record**. That satisfies the *form* of my condition
(restoration + stated pre-landing route), but the mechanism's exact-commit
legality is not established, and the other objections below remain. So:
condition confirmed for R5/ballot in form; **not** a yes recommendation.

## B. Strongest case against v2

### 1. “Direct single-parent commit” is ambiguous against the exact-commit requirement

§2.3 says the combined change's **exact commit/tree** is verified green before it
lands, then “landed by direct single-parent commit.” §4 repeats: “landed
commit/tree must equal the candidate.”

Those two sentences are only compatible if landing is a **fast-forward to the
exact verified commit**. If the Clerk creates a new single-parent commit on
`main` with the same tree, the commit hash differs from the verified candidate;
Act 21 §2 requires verification of the exact commit, not merely the tree. The
bill does not say “fast-forward to the verified candidate” and does not address
what happens if `main` moves during verification (a stale candidate cannot be
fast-forwarded; a new commit would be unverified).

This is the central new defect: the delivery mechanism is named, but its Git
semantics are not precise enough to satisfy the exact-commit rule it invokes.
The bill should say: verify candidate C; if `main` is still the expected parent,
fast-forward to C; otherwise re-create and re-verify C; never make an unverified
commit. A “direct commit” that creates a new commit is not the verified candidate.

### 2. No established authority for bypassing the protected-path merger

`government/reviewed-merge.sh:52` still refuses `records/bills/*`,
`records/ballots/*` and `government/LAWS.md`. v2 says the alternative
(amending the protected list) is “not chosen,” and instead asserts a direct
commit is lawful.

Act 6 §2 says adopted changes “shall be recorded in a Git branch/commit and
merged to the governing branch.” Act 21 §2 speaks of “the Clerk verification at
merge.” A direct push to `main` is not obviously the “merge” those provisions
contemplate; the existing direct-commit practice is the very practice the
earlier review found non-compliant. v2 adds pre-landing verification, which
addresses the ordering, but it does not establish that bypassing
`reviewed-merge.sh` is itself authorized. The route candidate
`government/enactment-merge.sh` (`2342a7e`) exists precisely for this; v2 does
not use it and does not amend the merger or Act 6.

At minimum, v2 must either (a) use the fast-forward route and explain why that
satisfies Act 6/Act 21, (b) amend `reviewed-merge.sh`/Act 6 in this Act, or
(c) obtain an express legal ruling that a verified direct fast-forward is a
“merge” for Act 6 §2. Assertion is not authority.

### 3. Phase 1 combines records and tests, but the fixture set is unnamed

§2.3/§5 Phase 1 is a **combined** `records/` + `tests/` change: restoration plus
“the fixture repairs.” That is what makes `run-all` green (restoration alone
does not). But the bill never names the exact fixture commit/tree. It cites the
mutable branch `origin/prerequisite/c1a00002-r5-v2`; its assumptions say the
same. A combined candidate must name the exact fixture commit/tree, or the
pre-landing record cannot bind “the candidate” reproducibly.

Also, the fixture repairs are another office's work. Bundling them into this
Act's implementation is a scope choice that should be explicit; the bill should
name the exact commit and require the fixture author/reviewer to confirm the
bytes included.

### 4. Attribution is predicted, not enforced

§2.2.4 says Act 1 already requires individually attributable ballots and
“this Act adds no checker change.” Prediction 3 says every affirmative vote will
have a per-seat JSON, but a prediction is not a gate. The original M-024 defect
was nine TSV-only rows; the same consolidation can recur in v2's own vote, and
the bill deliberately adds no check. At minimum, require each affirmative row to
have a matching per-seat JSON for this Act's own tally; a post-enactment
prediction cannot prevent the defect it predicts.

### 5. The restored earlier bill still says DRAFT / NOT ENACTED

§2.2.2 restores `records/bills/executive-innovation-office-act.md` to its
`64a466a` bytes. Those bytes begin:

```
# DRAFT — Executive Innovation Office Act (v2)
**Status: proposed, NOT ENACTED. No ballot or legal authority is implied.**
```

The bill does not state that this header is historical and subordinate to the
Act 25/status register. After restoration, the file will still say the Act is
not enacted, while Act 25 supersedes it. The status register may be authoritative,
but the bill should say so expressly; silence leaves a material contradiction in
the enacted record.

### 6. Predictions are fresh but not yet effective, and P1/P2 do not test the
direct-commit legality

The five v2 predictions are better than the failed set: P1 covers the combined
Phase-1 tree, P2 the pre-landing record, P3 attribution, P4 non-retroactivity,
P5 the deadline. But:

- They are on the sponsor branch, not yet merged into the main ledger; the gate
  currently refuses (0 registered on `main`). Enrollment in the pilot is not
  registration.
- P1/P2 test that a pre-landing record exists and the tree is green; they do not
  test that the landing is a fast-forward to the **exact** verified commit rather
  than an unverified new direct commit.
- P3 predicts attribution but does not enforce it.

A good calibration score could coexist with an unlawful/unverified landing.

### 7. Sponsor response is pending

§8/§9 are correctly PENDING. Act 16 §1 is therefore not satisfied for v2; the
fresh review is only half of the gate. The old response cannot be carried over.

## C. What would make v2 reviewable/eligible

1. Define landing as **fast-forward to the exact verified candidate commit**;
   fail if `main` moves; never create an unverified commit.
2. Establish the legal route for protected paths: amend `reviewed-merge.sh`/Act 6,
   use the existing verified route, or obtain an express ruling that a verified
   fast-forward is the Act 6 “merge.”
3. Name the exact fixture commit/tree included in Phase 1 and require its author
   confirmation.
4. Require per-seat JSON artifacts for this Act's own affirmative votes, or a
   one-time independent check; do not rely only on prediction 3.
5. State expressly that the restored earlier bill's DRAFT/“NOT ENACTED” header is
   historical and the Act 25/status register controls.
6. Merge/register the five predictions into the main ledger; add a prediction
   for exact-candidate fast-forward landing (or make it a binding gate).
7. Sponsor point-by-point response to this report.

## D. Limitations

- I reviewed v2 at `dcf5c22` (blob `94fe623f…`) and compared it with the failed
  text `831eb00` and interim `e0c58bd`; I did not re-review §2.1's verbatim block.
- I reproduced the §2.3/§4 wording, the `64a466a` header, the protected-path
  refusal, and the prediction/ledger state. I did not run the full suite on a
  combined candidate; none exists.
- No ballot, protected record, bill, or other seat worktree was modified; no
  merge; no eligibility finding beyond this review.

---

## E. Delta addendum — 2026-11-08 — v3 digest `83611240…`

The sponsor revised the v2 file at `5c31fdb`. The new digest is
`8361124030d600b4c8e628f589d4f69fe841ee0b8df1b01c9650bbdeacab1e33`.
The diff from `dcf5c22` is limited to:

- replacing **`NOT ENACTED / NOT VOTE-ELIGIBLE`** with `NOT YET ENACTED` and a
  paragraph saying eligibility is determined by §7;
- adding an “Eligibility conditions (exhaustive)” paragraph in §7.

No operative clause, delivery mechanism, record disposition, prediction, or
sponsor-response section changed. This is a delta confirmation, not a new
full review.

### E.1 Header / eligibility objection

The specific “header declares itself NOT VOTE-ELIGIBLE” objection is **resolved**
by v3: the phrase is gone, and the remaining `# DRAFT — … (NOT ENACTED)` is an
accurate statement that the bill is not yet enacted, not a self-disqualifying
bar. I do **not** object to the header on that ground.

The separate objection in §B.5 — the **restored earlier bill** still says
`# DRAFT` / `Status: proposed, NOT ENACTED` — remains, because v3 does not
address the earlier bill’s header after restoration.

### E.2 The seven objections after v3

| Objection | Status |
|---|---|
| 1. “Direct single-parent commit” ambiguous vs exact verified candidate | **Stands.** §2.3/§4 are unchanged. The bill still does not say fast-forward to the exact candidate or what happens if `main` moves. |
| 2. No established authority for bypassing `reviewed-merge.sh` / Act 6 | **Stands.** §2.3 still asserts a direct commit; no amendment to Act 6 or the merger, and the existing route candidate is not used. |
| 3. Phase-1 fixture commit/tree unnamed | **Stands.** Still a mutable branch reference; no exact fixture commit/tree. |
| 4. Attribution predicted, not enforced | **Stands.** §2.2.4 unchanged; prediction 3 is not a gate. |
| 5. Restored earlier bill still says DRAFT / NOT ENACTED | **Stands.** §2.2.2 unchanged. |
| 6. Predictions not effective in the main ledger / gate | **Partly resolved on the branch, not durable.** The Clerk reports gate PASS with `--all` on the v3 branch; the main ledger does not yet contain the v2 entries, and §9 is still pending. This is a process prerequisite, not a clause defect. |
| 7. §9 sponsor response pending | **Stands.** No v2 response exists; Act 16 §1 remains unsatisfied for the text. |

No objection is withdrawn on the v3 evidence.

### E.3 Earlier condition

The earlier R5/ballot condition remains **met in form**: §2.2.3 still provides
records-only restoration, and §2.3/§5 still state a pre-landing verification
mechanism. That is the clause I rely on. It is not a yes recommendation; the
seven objections above, especially the exact-commit/direct-commit ambiguity and
the missing authority for bypassing the protected-path merger, remain.

### E.4 What v3 must still fix

1. Define landing as **fast-forward to the exact verified candidate commit**;
   fail/re-verify if `main` moves.
2. Establish the legal route for protected paths (amend Act 6/reviewed-merge, use
   the verified route, or obtain an express ruling that a verified fast-forward
   is the Act 6 merge).
3. Name the exact fixture commit/tree.
4. Enforce per-seat artifacts for this Act’s own affirmative votes.
5. State that the restored earlier bill’s DRAFT header is historical and the
   Act 25/status register controls.
6. Integrate the five predictions into the main ledger (or record a durable
   branch-equivalent gate result) and add a prediction/binding condition for
   exact-candidate fast-forward landing.
7. File the §9 response.

The v3 text remains **not vote-eligible** until at least the §9 response and the
route/exact-commit fixes are present.

---

## F. Delta addendum — 2026-11-08 — v2 at `6798fbf`, digest `b170694c…`

`origin/main` now records a newer v2 candidate at `6798fbf`
(sha256 `b170694cb34a75d2053e3600aedcea086ebe175c3a530a544cd6d40965e45491`),
with the sponsor’s §9 response and fixes for several earlier objections. The
five v2 predictions were integrated at `8e38400`, and
`predict-gate.sh executive-innovation-office-reenactment-act-v2` now **PASSes**
on main (5 registered). This is a delta review of the changed clauses, not a
new full review.

### F.1 Objections resolved on the evidence

| Earlier objection | Status |
|---|---|
| 3. Fixture commit/tree unnamed | **Resolved.** §2.3/§5 pin the fixture set to `2342a7e` (tree `35d1581…`) and require its own pre-landing record. |
| 4. Attribution predicted, not enforced | **Resolved.** §2.2.4 now requires a per-seat JSON for every affirmative vote on this Act, matching bill/seat/vote/digest, confirmed by an office other than sponsor/Clerk before the tally is relied upon. |
| 5. Restored old bill still says DRAFT / NOT ENACTED | **Resolved.** §2.2.2 now states expressly that the restored `64a466a` header is historical and subordinate to the Act 25 heading and `ENACTMENT-STATUS.md`; it no longer claims the contradiction is gone. |
| 6. Predictions not effective in main ledger/gate | **Resolved.** The five v2 predictions are integrated at `8e38400`; the gate PASSes on main. |
| 7. §9 sponsor response pending | **Resolved in form.** §9 now answers the seven objections against the amended text, with the honest limits stated. |

The earlier header/eligibility objection was already resolved by v3; the
`NOT VOTE-ELIGIBLE` phrase is gone.

### F.2 Objections that still stand

**1. Direct single-parent commit vs exact verified candidate.** §2.3/§4 still
say the exact candidate commit/tree is verified before landing, and “landed by
direct single-parent commit.” They still do **not** say “fast-forward to the
exact verified candidate”; if a new commit is created on `main`, its hash differs
from the verified candidate and Act 21 §2’s exact-commit requirement is not met.
The sponsor’s §9 answer says “landed tree must equal the candidate,” but a tree
match is not a commit match. The Clerk independently asks this same question
(`9c05d02`). **Unresolved.**

**2. Act 6 §2 landing authority.** `government/reviewed-merge.sh:52` still
refuses `records/bills/*`, and §2.3 still asserts a direct commit without
amending Act 6 §2 (“merged to the governing branch”) or the merger, and without
using the existing verified route. The sponsor’s response says the combined
candidate is “the option the review allows,” but does not establish that a direct
commit is the Act 6 merge. The Clerk independently asks this same question.
**Unresolved.**

These are the two objections the Clerk has asked the sponsor to answer before
the frozen digest can be confirmed. I agree they are the remaining blockers.

### F.3 Condition and vote-eligibility

- The earlier R5 condition remains **met in form** (§2.2.3 restoration + §2.3/§5
  pre-landing mechanism). Not a yes recommendation.
- Five of the seven original objections are resolved; **two remain unresolved**.
  The v2 text is still **not vote-eligible** until the sponsor answers both with
  a lawful, exact mechanism.
- Predictions are now gate-PASS; they are calibration, not proof of legality.

### F.4 What would close the two objections

1. State: verify candidate C; if `main` is still at the expected parent,
   **fast-forward to C**; if `main` moved, re-create and re-verify C. Never
   create an unverified commit. A tree match alone is insufficient.
2. Establish the Act 6 §2 route: amend the merger/Act 6 in this Act, use the
   existing verified `enactment-merge.sh` route, or obtain an express ruling that
   a verified fast-forward is the Act 6 “merge.” A bare assertion that direct
   commit is “Act 21 ordering” is not legal authority.

---

## G. Binary confirmation — 2026-11-08 — digest `25df2f4a…`

**Confirmed on `25df2f4a2783e1844238d8200728ee3a441072c9ea5ee90bb7673fba40cdce55`**
(candidate `942a6cb`; identical bill content to `e79bf97`). The two remaining
route objections are answered by the new §2.3/§4(vi); the other five were
resolved earlier. I do not maintain any of the seven against this digest.

### G.1 Fast-forward exactness — resolved

§2.3 now requires one exact candidate commit **C**, a pre-landing record for C's
commit and tree, and landing **only by fast-forward** of `main` to C
(`git merge --ff-only C`, or `git push … C:main` where `main` was C's parent).
If `main` moves, C is re-created on the new tip and **re-verified**; creating a
new unverified commit is expressly forbidden. §4(vi) makes this a binding
landing check. That is exactly the exact-commit condition I asked for; a tree
match is no longer accepted as a substitute for a commit match.

### G.2 Act 6 §2 landing authority — accepted

The statutory reading is sufficient for me:

- Act 6 §2 requires adopted changes to be “merged to the governing branch,” and
  itself describes the boot as fast-forwarding the canonical checkout. A Git
  fast-forward is a merge that creates no new commit; the exact commit verified
  is the exact commit that reaches `main`.
- Act 21 §2 requires verification of “the exact commit being merged”; a
  fast-forward satisfies that; a merge commit would not.
- No enacted law names `government/reviewed-merge.sh`. Its protected-path refusal
  is tool policy, not statute, so it cannot by itself make a lawful verified
  fast-forward unlawful.

The bill records the residual honestly: no express ruling says “FF is the Act 6
merge.” I accept the reading above and do not require that ruling as a condition
of this confirmation. If Parliament later disagrees, it can amend the merger or
Act 6 separately; that is not a defect in this text.

### G.3 Status

With G.1/G.2, all seven objections from `da8ef33` are resolved for digest
`25df2f4a…`: fixture pin, attribution, DRAFT header, predictions/gate, §9
response, fast-forward exactness, and Act 6 §2 authority. The earlier R5
condition is met (§2.2.3 restoration; §2.3/§5 pre-landing FF mechanism).

This is a confirmation on the text; it is **not** a ballot and not a claim that
the implementation has landed or that the suite is green. The Clerk may publish
the ballot request on this digest. The remaining gates are the ordinary ones:
Act 22 gate, Act 16 §1 response (present), and the eventual pre-landing record
for the implementation.
