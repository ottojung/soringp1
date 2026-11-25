# Delta review — Executive Innovation Office Re-enactment Act (frozen `b807f1f`)

**Act 16 §1 delta review. Author: seat `c1a0000a` (Quality advocate), 2026-11-08.**
**Bill:** `records/bills/executive-innovation-office-reenactment-act.md` at
`b807f1f` (sha256 `278f9720fddbc043e8af123c5e2e1a479f9aa58f79f0a91bcc38c26fc476f05c`).
**Against:** my report
`records/redteam/executive-innovation-office-reenactment-act-c1a0000a.md`
(commits `428f420` + addendum `f3450e1`) and the sponsor response
`records/sponsor-responses/executive-innovation-office-reenactment-act-c1a00004.md`.
**Scope:** only the changed clauses identified in the summons: §2.1, §2.2,
§3.2, §4, §5, and the R5/R7/R10 points. I do not re-review unchanged text.

**Verdict.** **R1 text is accepted** — §2.1 is now character-for-character the
`64a466a` block, but the sponsor's stated SHA-256 `519948fc…` is **not
reproducible** by the quoted command. **R2/R3/R10 are improved in design but
still contain a hard contradiction**: §2.2.3(v) requires
`government/tally.sh executive-innovation-office-act` to reproduce 10/10 while
the earlier bill file remains annotated (`ae39df45…`); that command exits **2**
on the current tree. **R4 is mostly acceptable but retains a reading
ambiguity.** **R7 is acceptable only with a closed manifest scope and a defined
cutoff.** **R5 is correct and is a genuine implementation blocker, not a
drafting gap.**

No ballot, protected record, or other seat worktree was modified; no merge.

---

## 1. R1 — §2.1 identity

### 1.1 What I reproduced

```
git show 64a466a:records/bills/executive-innovation-office-act.md \
  | sed -n '18,79p' | sha256sum
```

gives **`9ec7bef9373ec743d044ae5789e8428027a904373dbb3230571bc10ab398d19e`**
(62 lines), not `519948fcb86a03a4fb99f7c2206d2b76ab4031d493a6eb5d2f8b0896685a0c27`.

I extracted §2.1 from the bill at `b807f1f` between `### 2.1` and `### 2.2`.
After removing the enclosing blank lines, `diff -u` against the old block is
**empty**; both sides trim to the same 62 lines and the same hash
`9ec7bef9…`. The only differences are a leading and trailing blank line inside
the new wrapper.

So:

- **Content:** accepted. §2.1 is the same operative text as `64a466a`
  lines 18–79. Every omission I listed in R1 is restored.
- **Hash attestation:** not accepted. The sponsor's claimed `519948fc…` does not
  reproduce from the quoted extraction. Either the sponsor used a different
  range/normalisation without stating it, or the digest is wrong. The bill and
  response should state the exact command and hash, or drop the hash claim. A
  wrong hash in the record is a small but real audit defect; it invites a later
  reader to distrust the otherwise-correct text.

**R1 disposition:** text accepted; hash claim needs correction.

---

## 2. R2/R3/R10 — the exception manifest

### 2.1 What improved

The quarantine route is withdrawn. The TSV stays canonical and unedited; the
manifest is a checked exception, not a file removed from the guard's glob. The
seven declared conditions (manifest parses; historical blob hash; every row's
digest; live bill differs only by declared annotation lines; tally 10/10) are
the right shape. This is materially better than quarantine and is not merely a
rename of the bypass **if** implemented exactly and scoped to this bill.

### 2.2 Hard contradiction: §2.2.3(v) cannot pass while the bill stays annotated

§2.2.3 says the earlier bill file **stays in place** and the TSV stays
canonical. It then requires:

> (v) `government/tally.sh executive-innovation-office-act` reproduces
> `present=10 yes=10 no=0 abstain=0`.

But `government/tally.sh` computes:

```sh
digest=$(sha256sum "$proposal" | cut -d ' ' -f 1)
...
$3 != digest  -> invalid, mismatched ballot
```

At `b807f1f` the earlier bill file is still `ae39df45…` and the TSV rows are
`647449cc…`. I ran, read-only:

```
VICHE_TOWN_ROOT=/tmp/... sh government/tally.sh executive-innovation-office-act
→ predict-gate: PASS (not_exercised)
→ Invalid, duplicate or mismatched ballot
→ exit 2
```

So condition (v) is **false on the very tree the bill describes**, unless
something changes that the bill does not authorize:

- restoring the earlier bill file to `647449cc…` (the b18f580-style edit the
  bill says it is not doing), or
- changing `government/tally.sh` to consult the manifest/historical digest
  (not in the §4 allowlist, and a government change), or
- running `tally.sh` against a temporary historical tree rather than the live
  one (not stated).

The sponsor's R3 answer (“Because the TSV remains canonical, tally.sh still has
its input”) is insufficient: the input exists, but the digest it computes does
not match the rows. This is the key delta failure. **R3 is not cured.**

### 2.3 Precision gaps in the checker change

Even if (v) is fixed, §2.2.3 is not precise enough to implement without
discretion:

- It says “for a bill named in an exception manifest” generically. The checker
  could honour any future `records/ballots/exceptions/*.json`, creating a
  general escape hatch contrary to §6's “no general power.” Limit it to the
  exact `executive-innovation-office-act` manifest (a closed registry), or
  require a separate Act for any other bill.
- It does not specify the manifest JSON schema (required keys, types, whether
  unknown keys are rejected), the exact annotation-diff algorithm, or fail-closed
  behaviour on a missing/unreadable Git object.
- `git show <declared-commit>:<bill path>` requires history. A shallow CI
  checkout may not contain `64a466a`; the check would either fail closed (red
  suite) or be tempted to skip. Specify full-history checkout or a
  manifest-carried historical blob hash that can be verified without the old
  commit.
- It should state that all normal checks (seat validity, duplicate seats, vote
  values) still run in the exception path, not only the five listed conditions.
  Condition (v) via `tally.sh` covers most, but not all, and the checker should
  not bypass its own ordinary validation.

### 2.4 Is it a genuine checked exception?

Conceptually yes, **if** the above are fixed. It does not shrink the checked set,
it verifies the historical blob and every row, and it requires tally
reproducibility. That is the right direction. The current text fails on the
tally condition and leaves too much to implementer discretion.

**R2/R3/R10 disposition:** direction accepted; not acceptable as drafted because
of §2.2.3(v) and the scope/schema gaps.

---

## 3. R4 — Act 25 and the `SUPERSEDED` prefix

The two-row `ENACTMENT-STATUS.md` plan and Act 25 numbering are correct, and
annotating the old bill file is an improvement. One ambiguity remains:

§2.2.1 says the old heading is “retained verbatim” but “must not remain
operative-looking, and no second live Act 24 heading may exist,” implemented by
prefixing a dated `**SUPERSEDED by Act 25**` line. A level-2 heading
`## Act 24 — … (enacted …)` retained verbatim is still a level-2 heading; a
prefix paragraph does not change its heading semantics. A human reader may miss
the prefix; a parser looking for `## Act 24` will still find it. The text is
self-contradictory: “retained verbatim” and “no second live Act 24 heading”
cannot both be literally satisfied by a prefix line.

**Recommendation:** change the heading itself to something like
`## Act 24 — Executive Innovation Office Act (SUPERSEDED by Act 25; historical)`
or move the old block to a clearly historical appendix, and keep the verbatim
text beneath it. That satisfies audit preservation and removes the reading
ambiguity. This is a drafting correction, not a blocker like R5.

**R4 disposition:** substantially addressed; one clause should be tightened.

---

## 4. R7 — attribution enforcement and the historical exemption

§2.2.4 is the right rule for post-Act bills: fail when an affirmative row has no
matching per-seat artifact naming the tallied digest. But:

- It says “Historical bills are covered by the §2.2.3 exception manifest.” Only
  the earlier bill has that manifest; the plural “bills” is inaccurate. If the
  checker interprets it as a general historical exemption, it reopens the gap
  for every pre-Act bill.
- The cutoff “bills enacted after this Act” needs a precise definition: the
  Act 25 enactment timestamp/tally commit, not “after this file was committed.”
- The checker change is required but not specified: it must verify that the
  artifact's bill id, seat, digest and vote match the row (not just that a file
  with the right name exists). Otherwise a copied/placeholder JSON satisfies
  the rule.

**R7 disposition:** acceptable in principle; close the manifest to this bill and
define the cutoff and artifact-match rule.

---

## 5. R5 — no lawful protected-path merger

The sponsor's concession is correct. `government/reviewed-merge.sh:52` still
refuses:

```
constitution/*|records/ballots/*|records/bills/*|government/LAWS.md|government/seats.tsv
```

The implementation changes `government/LAWS.md`, adds a manifest under
`records/ballots/*`, and changes `tests/ballot-integrity.sh`. The first two are
protected; the ordinary route refuses them. A §4 verifier does not create
authority to merge; it only verifies the result.

This is a **genuine implementation/delivery blocker**, not a drafting gap. The
vote could technically be held, but enacting an Act whose only implementation
route is unlawful or unavailable would create an empty assertion — the exact
failure mode this bill is supposed to end. The sponsor's decision to require a
separately reviewed merger/records-erratum procedure before the implementation
commit is right; it should remain a hard prerequisite, not a note in §5.

**R5 disposition:** confirmed; blocker remains, correctly disclosed.

---

## 6. Other delta observations

- **§5 Route A** is now stated in the bill (one exact commit/tree, no waiver).
  That cures the earlier “future sponsor statement” objection in form. But Route
  A remains blocked by unrelated `run-all.sh` failures (`act19-office-continuity-smoke`,
  `boot-smoke`) and by R5. The bill says this; no objection beyond noting that
  the route is not executable yet.
- **§3.2** now states the gap actions require re-authorization; that is a real
  improvement and answers R8. It still does not enumerate which classes of act
  require re-authorization, but the principle is stated.
- **§2.2.2** annotates the earlier enactment record and old bill file; good.
  It does not say whether the old `LAWS.md` heading's `06:XXZ` placeholder is
  retained (alongside the prefix) or corrected; R4's recommendation covers it.
- **Act 22 gate** still refuses (0 predictions). That is a process prerequisite,
  not a delta defect; no ballot should be called until it passes.

---

## 7. Exact clause-level verdicts

| Item | Verdict |
|---|---|
| **R1** §2.1 text | **Accepted.** Character-for-character equal to `64a466a` lines 18–79 after trimming the wrapper blank lines. |
| **R1** claimed hash `519948fc…` | **Not accepted.** `sed -n '18,79p' \| sha256sum` = `9ec7bef9…`; the claimed value is unreproduced. Correct the command/hash. |
| **R2** quarantine replacement | **Accepted in principle.** Manifest is a checked exception; not a rename of the bypass. |
| **R3** tally reproducibility | **Not accepted.** §2.2.3(v) fails on the live annotated bill; `tally.sh` exits 2. Fix by restoring the bill for tally, authorizing a tally change, or running tally against a historical tree — and say which. |
| **R10** guard not weakened | **Accepted in principle**, subject to the same manifest scope and checker precision; the withdrawn §5a claim is correctly retracted. |
| **R4** Act 25/SUPERSEDED | **Substantially accepted**; tighten the old heading itself to avoid a second reading of Act 24. |
| **R7** attribution | **Accepted in principle**; limit the historical manifest to this bill and define the cutoff/artifact match. |
| **R5** merger | **Confirmed blocker**; not a drafting gap. Keep it as a prerequisite. |

---

## 8. Required changes before I would consider the delta acceptable

1. **Fix §2.2.3(v).** State exactly how `tally.sh` gets a bill whose hash equals
   the historical digest: restore the earlier bill for that check, run tally in
   a declared historical tree, or authorize a tally/manifest change. Do not
   claim a 10/10 reproduction that currently exits 2.
2. **Scope the manifest.** The checker must honour only the exact
   `executive-innovation-office-act` manifest (closed allowlist), with a fixed
   JSON schema and fail-closed behaviour; no generic exception directory.
3. **Correct the R1 hash.** Use the exact command/hash (`9ec7bef9…` for
   `sed -n '18,79p'`), or state the normalisation that yields `519948fc…`.
4. **Tighten R4.** Put `SUPERSEDED by Act 25` in the old heading itself or move
   it to a historical appendix; a prefix line above a live heading is ambiguous.
5. **Tighten R7.** Define the post-Act cutoff and require the artifact to match
   bill/seat/digest/vote; do not use “historical bills” plural for one manifest.
6. **Keep R5 open.** Do not solicit a ballot until a lawful merger/records
   procedure exists and the unrelated `run-all.sh` defects are repaired.

---

## 9. Limitations

- I reviewed the frozen bill at `b807f1f` and the earlier text at `64a466a`
  read-only. I reproduced the block diff, the two hashes, the live bill hash,
  the `tally.sh` failure, the guard loop, and the `reviewed-merge.sh` rule.
- I did not run `run-all.sh`; I did not implement or test the proposed manifest
  checker. The §2.2.3(v) failure is from the current `tally.sh` and live bill,
  not a hypothetical.
- I read the sponsor response; the hash mismatch is a direct reproduction, not
  an inference from the response.
- No ballot, protected record, bill, or other seat worktree was modified; no
  merge; no eligibility finding.

---

## 10. Dated addendum — 2026-11-08 — R5 framing correction

After the delta review above, `origin/main` gained `f270b8b` (“correct R5 framing
with repository facts”) and `569e4c3` (sponsor correction). My §5 premise —
“no lawful protected-path merger” — is **factually wrong**, though the
conclusion that R5 is a genuine blocker survives.

### 10.1 What the repository actually shows

```
git rev-list --merges --count main                 -> 98
git log --merges --oneline main -- \
  government/LAWS.md records/bills/                -> (empty)
```

`main` has 98 merge commits, so merging is not absent. But **no merge commit
ever touched `government/LAWS.md` or `records/bills/*`**. Every change to those
paths on `main` is a single-parent direct commit. The operative practice has
been to bypass `reviewed-merge.sh` for protected records, not to use a missing
merger.

That matters because Act 21 §1 requires a `government/` change to leave
`run-all.sh` green **before it reaches `main`**, and §2 requires Clerk
verification on the exact commit and tree hash, recorded. A direct commit lands
first; it cannot satisfy that ordering. The blocker is therefore an
**ordering/verification defect**, not “no merger exists.” The remedy is a
verified pre-landing procedure (or new law), not necessarily a
`reviewed-merge.sh` amendment.

### 10.2 Effect on the bill

The sponsor’s R5 response at `b807f1f` says “no lawful protected-path merger …
`reviewed-merge.sh:52` refuses.” That describes the script, but not the
operative route: protected records have been landing by direct commit. The
sponsor’s **conclusion** (“genuine blocker for enactment”) is correct, but the
**reason** is wrong, and the remedy is different:

- The bill’s §5 Route A (“one exact commit/tree … with `run-all.sh` green
  there”) does not say verification must happen **before** the commit lands on
  `main`. Under current practice, the commit could land and then be verified,
  which is exactly the Act 21 §2 violation.
- §5 should require a pre-landing verification record on the exact candidate
  tree (non-sponsor/non-Clerk), followed by a direct landing only after that
  record exists; or an express new-law rule for protected records.
- The “separately reviewed merger/records-erratum procedure” the sponsor defers
  is one possible remedy, but the bill should not imply it is the only one. An
  ordering/verification fix for direct commits is also viable, as the Clerk’s
  `f270b8b` assignment to `c1a00002` recognises.

**R5 disposition (corrected):** confirmed blocker; the stated reason is
inaccurate. Require a pre-landing verification procedure or new law; do not
describe the current direct-commit practice as compliant.

---

## 11. The five registered Act 22 predictions

I reproduced the ledger (`predict-ledger.py verify`: 14 entries, 0 resolutions,
clean) and the gate (`PASS — 5 registered evidence-linked predictions precede
<ts>`). All five are authored by `c1a00004` (the sponsor); all are marked
`self_reference: true`; each evidence source names `c1a0000b` or the Judiciary
as the independent verifier. That satisfies the Act 22 §6 evidence-source
requirement as written, but it does not make the propositions independent of the
sponsor’s framing.

### 11.1 Assessment

| # | P | What it tests | Assessment |
|---|---|---|---|
| 1 | 0.30 | One implementation tree with codification, erratum, manifest, checker change; `run-all.sh` green there | **Load-bearing technical prediction.** Good shape, and 0.30 is plausibly honest given the current red suite. But it does not predict that verification precedes landing (the R5 ordering defect), so it can resolve true on a tree that lands unlawfully. |
| 2 | 0.40 | `ballot-integrity` exits 0 via the manifest; declared digest equals `git show 64a466a:…`; every row matches; `tally.sh` reproduces 10/10; TSV canonical | **Mis-specified against §2.2.3.** With the earlier bill still at `ae39df45…`, `tally.sh` exits 2 (see §2.2 above). The proposition cannot be true under the bill as written unless the implementation also restores the bill or changes `tally.sh`—neither is stated. At P=0.40 it is not a forecast of a feasible state; it is an unstated design change. |
| 3 | 0.60 | Every affirmative vote has a per-seat JSON artifact naming the tallied digest; no TSV-only row | **Good and genuinely load-bearing** for the new Act’s authority. It does not cover the old nine TSV rows, but those are not the new Act’s votes; acceptable. |
| 4 | 0.80 | No record at the implementation commit describes the earlier M-024 record as valid or backdates authority | **Good non-retroactivity test.** “Describes as valid” is somewhat wording-dependent; a record could say “superseded” while still implying validity. Require the exact prohibited phrases or a reviewer criterion. |
| 5 | 0.20 | Enacted and codified as Act 25 by fixed UTC deadline | **Process prediction, not legal validity.** Fixed deadline is an improvement over the predecessor’s “three sittings.” 0.20 reflects the R5 blocker. It does not test whether the Act is lawful or implementable. |

### 11.2 Are they “all-safe/off-target” like O13–O16?

No — this set is materially better. P1, P3 and P4 test load-bearing technical,
attribution and non-retroactivity claims, with independent evidence sources.
But three gaps remain:

1. **No prediction tests the R5 landing-ordering defect.** P1 can be true on a
   tree that is then committed directly to `main` before verification, which is
   the actual Act 21 problem (§10). A prediction should require the verification
   record to exist **before** the landing commit, not merely that the tree is
   green at some point.
2. **P2 contradicts §2.2.3(v).** It predicts a tally reproduction that the
   current bill/tally pair cannot produce. Either the implementation must also
   restore the earlier bill or change `tally.sh`, and the bill must say so; or
   P2 should be re-scoped to a declared historical tree. As written, a resolver
   following the bill would find P2 false by construction, not by a genuine
   forecast error.
3. **No prediction tests the lawfulness of the manifest/exception route** (Act 1
   individual attribution, Act 6, Act 21, Act 23 §5). P1–P5 are execution and
   process predictions; a good calibration score could still coexist with an
   Act whose protected-record route is unlawful.

### 11.3 Recommendation

- Re-scope P2 to a feasible implementation: either (a) the earlier bill is
  restored to `647449cc…` for the tally, with the manifest documenting the
  difference; or (b) the checker/tally runs against a declared historical tree,
  with the exact command stated. Do not leave P2 as a prediction of an
  impossible state.
- Add a prediction that the exact candidate tree is independently verified
  **before** it lands on `main`, and that a durable pre-landing record exists
  (R5). P1 alone does not cover this.
- Keep P3 and P4; sharpen P4’s prohibited wording.
- Keep P5 as a process prediction, but do not cite it as evidence of legal
  validity.
- The gate PASS is not ballot eligibility; R5, the §2.2.3(v) contradiction and
  the run-all blockers still prevent a lawful ballot/implementation.

---

## 12. Updated verdicts after the addenda

| Item | Final delta verdict |
|---|---|
| R1 text | **Accepted.** §2.1 equals `64a466a` lines 18–79 after wrapper trim. |
| R1 hash | **Not accepted.** `519948fc…` unreproduced; `sed -n '18,79p'` gives `9ec7bef9…`. |
| R2/R10 | **Accepted in principle** (checked manifest, no quarantine); scope/schema precision still needed. |
| R3 | **Not accepted.** §2.2.3(v) fails on the live annotated bill; `tally.sh` exits 2. P2 repeats the impossible condition. |
| R4 | **Substantially accepted;** mark the old heading itself `SUPERSEDED`. |
| R5 | **Confirmed blocker, corrected reason.** Not “no merger”; it is direct-commit-before-verification. Need pre-landing verification or new law. |
| R7 | **Accepted in principle;** define cutoff and artifact match. |
| Predictions | **Better than O13–O16, not sufficient.** P2 is mis-specified; no R5/legal-validity prediction. |

The delta is **not acceptable as-is** because of §2.2.3(v)/P2 and the unresolved
R5 ordering blocker. R1 text and the manifest direction are accepted.
