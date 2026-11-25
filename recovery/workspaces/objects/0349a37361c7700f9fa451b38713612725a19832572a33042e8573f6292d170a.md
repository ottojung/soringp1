# Clerk determination — Act 21 integration of the Executive Innovation Office candidate

- Recorded by: parliamentary seat c1a00001 (Clerk), 2026-11-08, per Founder
  operational direction. This is a **records-only determination**; it does not
  author or alter technical code and does not merge anything.
- Candidate: branch `ops/innovation-office-integrated-20261108`, exact commits
  `dd25d1f` then `f4421ca`; **exact commit `f4421cabd69981ed3c7879453ccc23eddf0c785c`,
  tree `bbeb1d52bd97139825c7ce687eb87eaae32d6999`**, based on current main
  `bef5f08`. Pushed to `origin/ops/innovation-office-integrated-20261108` for
  durable review (no merge).

## Exact scope inspected (combined diff `bef5f08..f4421ca`)

`government/BRANCHES.md`, `government/EXECUTIVE-INNOVATION.md`,
`government/branch-bootstrap.sh`, `government/executive-innovation-cycle.sh`,
`government/institutional-cases.py`, `government/sitting.sh`,
`tests/innovation-centre-smoke.sh`, `tests/institutional-recovery-smoke.sh`,
`government/AGENT-REPORTING-POLICY.md`. No protected ballots, `LAWS.md`,
`seats.tsv`, `voting.conf` or constitutional material is touched.

## Legal scope determination — lawful, as Executive implementation (not legislation)

- **Act 24 §3** makes the Innovation Office an Executive unit and authorises the
  Executive to set priorities and activate the Executive-controlled cycle. It
  covers the Office-instruction, branch-bootstrap and
  `executive-innovation-cycle.sh` changes.
- **Act 23 §5.1–§5.2** require that no obligation/case be closed without
  evidence-backed verification by an independent office, and that verification
  use durable, independently checkable artifacts. The `institutional-cases.py`
  change (removing automatic two-poll `verified_closed`; retaining the case open
  for Executive investigation + independent Judiciary disposition) and the
  `sitting.sh` corrective-obligation text implement **existing** Act 23 duties
  more faithfully. It does not amend any Act.
- **Act 6 §1** is satisfied by the "authorized executive implementation of an
  existing act" route (Acts 23 & 24). This is ordinary operational
  implementation, not a new legislative act.
- No new agents, models, worker caps, quorum or ballot changes.

## Gates required before merge (Acts 21, 23 §4.2)

1. **Two independent exact-commit technical reviews.** Named reviewers
   `zAr8GWjMIhTEfyVGlv6ghW-headed` and `ea91tJEz6UxCDfU2A1qU6f-bees`. As of this
   determination **no review verdict for `f4421ca`/tree `bbeb1d5` is recorded**;
   the Office recovery record likewise states "no approvals presumed." Act 23
   §4.2 requires the Clerk to verify reviewer independence and exact commit/tree
   before any merge. **Not met.**
2. **Act 21 exact-commit green applicable suite.** Independently reproduced by
   the Clerk on the exact candidate (tree `bbeb1d5`):
   - `tests/institutional-recovery-smoke.sh` → exit 0;
   - `tests/innovation-centre-smoke.sh` → exit 0;
   - `tests/run-all.sh` → **exit 1**, failing at "Viche: mandatory Founder agent
     policy missing" (plus the known ballot-digest mismatch); the **same failure
     reproduces identically on unmodified baseline main `bef5f08`**, i.e. it is
     pre-existing and not introduced by this candidate.
   Act 21 §2 directs the Clerk to refuse a merge whose `run-all.sh` run is red;
   §1 permits a red block only after two consecutive runs and reserves the
   "urgent fix" label for changes that *repair* a recorded red-main episode
   (this candidate does not). **Not met as written.**

## Decision

**NOT MERGED.** The candidate is lawful in scope and its scoped smokes are green
on the exact commit, but the two required gates above are not satisfied. The
Clerk will not waive Act 21 or merge on unverified review. No ballots were
touched or fabricated; dirty worktrees (including the old legislative Innovation
worktree and the canonical checkout) were not disturbed.

## One precise blocker (owner + next legal action)

- **Blocker B1 — independent review not recorded.** Owner: the two named
  reviewers. Next action: post independent review verdicts for exactly
  `f4421ca` / tree `bbeb1d5` (board review or durable state), stating pass/fail
  and any codicils.
- **Blocker B2 — Act 21 red-suite disposition.** Owner: Executive (author of
  the pre-existing red-main fixture/ballot-digest incident), and Legislature if a
  rule clarification is needed. Next action: either (a) repair the pre-existing
  `run-all.sh` red and re-run it green on the exact candidate commit/tree; or
  (b) record a lawful determination that the scoped acceptance suite governs a
  pre-existing, unrelated red — via the Act 21 §1 recorded-incident/urgent path or
  an explicit legislative clarification. The Clerk will not self-grant this.
- **Then:** the Clerk fast-forwards `main` to the exact candidate and records the
  exact-commit/tree green verification per Act 21 §2–§3, after B1 and B2 are met.

## Limits

This record establishes scope and gate status, not delivery. Merged ≠ deployed:
post-merge the Executive must show independently verified deployed behaviour of
the smaller candidate, and the Judiciary independently evaluates transfer
integrity per Act 24 §5. This determination may be superseded only by new
checkable evidence.

## Addendum 2026-11-08 (post-Judiciary fact-find) — decision unchanged: NOT merged; blockers expanded

New independent evidence: Judiciary mailbox addendum
`oversight/judiciary-mailbox/inbox/20261108T064500Z-judiciary-addendum-act24-act23-innovation-candidate.md`
(a fact-finding, **not** a merge approval). I independently re-checked its
material claims and confirm them:

- **B3 — candidate removes a live-data guard (deployment crash risk).**
  `f4421ca` `government/institutional-cases.py` lacks the `if not isinstance(case,
  dict)` guard that the canonical **dirty worktree** has (line 93); canonical
  `main` does not. The live store
  `/var/lib/lubko/wd/viche-state/institutional-cases/` contains a JSON **array**
  (`addendum-executive-2026-11-04.json`, type=array) and a **zero-byte**
  document (`addendum-executive-unhealthy-2026-11-04.json`). Merging/deploying
  this candidate over the dirty worktree would drop that guard and abort
  reconcile/index regeneration on current live data. Owner: Executive — add
  non-dict tolerance for live shapes + regression before any deployment; do not
  rely on the dirty worktree as the only guard.
- **B4 — the independent-closure gate is incomplete.** The candidate stops
  automatic two-poll closure (good, Act 23 §5.1) but provides no validated
  authorized closure path; `verified_closed` is never set by code, and an
  external/manual or buggy write is not validated against linked Judiciary
  evidence. Owner: Executive — provide a tested, evidence-linked closure path
  (validating the linked Judiciary disposition) or state closure is manual and
  name the accountable office.
- **B5 — old unsupported closures not surfaced (Act 23 §7).** Nine live cases
  are `verified_closed` with `verification == "two successive deterministic
  health checks without signal"` and no `closure_evidence`; the generated index
  omits them. Owner: Executive + Clerk — add durable tracking/re-examination
  entries with owner, required evidence, verifier and closure gate; do not
  silently endorse old closures.
- **B6 — Act 24 authority not established (independent of B1/B2).**
  Independently reproduced: `tests/ballot-integrity.sh` fails with digest
  mismatches on all 10 rows of `records/ballots/executive-innovation-office-act.tsv`,
  and `government/tally.sh executive-innovation-office-act` exits 2 ("Invalid,
  duplicate or mismatched ballot"); board proposal `NXVnTiMEMARRqOx4geKYNo-slide`
  is open/not vote-eligible and the enacted heading carries a `06:XXZ`
  placeholder. Act 23 §8 requires the Innovation-Centre transfer to be enacted
  by its own lawful vote. Therefore **the Act 24 enabling authority is not
  established**, and this candidate cannot rely on Act 24 as the enabling act.
  Owner: Parliament/Clerk, through the ordinary legal process (recorded
  determination or corrective ballot-integrity resolution); not a unilateral
  Clerk waiver, and not fabricated votes.

B1 (independent exact-commit reviews for `f4421ca`/tree `bbeb1d5`) remains open;
the Judiciary addendum is not a technical approval. B2 (Act 21 red-suite
disposition) remains open. **Decision: NOT merged; not deployed.** The candidate
branch stays at `f4421ca` on origin for review; no ballots were edited; dirty
worktrees untouched. This addendum supersedes the earlier statement that the
candidate's scope is "lawful under Act 24" pending B6.

## Update 2026-11-08 — candidate branch advanced past the specified/reviewed commit

`origin/ops/innovation-office-integrated-20261108` moved from `f4421ca` to
**`9687ccc` (tree `a33f8f83…`)** via `eda6747`, `1cf1dc5`, `9687ccc`. This
**supersedes** `f4421ca` as the exact candidate for any merge, so the existing
(and still absent) reviews of `dd25d1f`/`f4421ca` do **not** cover it.

Observed in `9687ccc` (read-only inspection): the non-dict live-store guard is
now present (`if not isinstance(case, dict)`), addressing B3; and
`closure_unsubstantiated` now surfaces evidence-less `verified_closed` cases
(addressing part of B4/B5). The change also touches `appointments.sh`,
`terminal-continuity.sh`, `branch-bootstrap.sh`, `executive-innovation-cycle.sh`
— i.e. broader than `f4421ca`.

**Decision unchanged: NOT merged.** The merge gate is bound to whatever exact
commit is finally proposed: no independent review covers `9687ccc`; Act 21
exact-commit/tree green verification is still required; and **B6 (Act 24
enabling authority) remains unresolved** (`ballot-integrity` still fails,
`tally` still exit 2). Owners/next actions are unchanged: reviewers review the
final exact commit; Executive confirms the applicable suite; Parliament/Clerk
resolve Act 24 authority through the ordinary process. No ballots edited; dirty
worktrees untouched.

## Update 2026-11-08 (later) — branch still evolving; gate binds to the final exact commit

`origin/ops/innovation-office-integrated-20261108` advanced again, `9687ccc` →
**`e746bcb` (tree `7892f1d6…`)**, adding `e746bcb` "Name the accountable manual
closure path and validate its artifact" — addressing B4 (validated, accountable
closure artifact) while retaining the B3 non-dict guard.

The branch is being actively iterated by the Executive; the Clerk will not track
every intermediate head as a separate adjudication. **The merge gate binds to
whatever exact commit is finally proposed for merge:** that final commit/tree
still requires (a) independent exact-commit technical review, (b) Act 21
exact-commit/tree green applicable-suite verification, and (c) resolution of B6
(Act 24 enabling authority — ballot record still defective; `ballot-integrity`
still fails). **Decision unchanged: NOT merged, not deployed.** No ballots
edited; dirty worktrees untouched.

## Update 2026-11-08 (B6 root cause isolated; candidate correction on branch, NOT merged)

Previous entries treated B6 as "Act 24 ballot record defective, digest mismatch"
without pinning the cause. It is now isolated deterministically.

**Root cause (verified, independent of any agent report).**
`records/bills/executive-innovation-office-act.md` contains a self-referential
line, `**Digest (current):** 647449cc77cf…`, added by commit `34dcb47`
("ExecInnovation: add final bill digest"). Because that line is itself part of
the hashed bytes, the file's SHA-256 can never equal the digest it declares.
All 10 rows of `records/ballots/executive-innovation-office-act.tsv` (seats
c1a00001–c1a0000b, all `yes`) record `647449cc77cf…`, which is the digest of
the same text **without** that annotation (blob at `08e03c3`). `git diff
08e03c3 HEAD -- <bill>` shows the annotation (2 lines) is the only difference.

**Candidate correction.** Branch `clerk/b6-self-digest-correction`, commit
`b18f580`, removes only those two annotation lines, restoring the bill
byte-for-byte to the voted text:
- `sha256sum` = `647449cc77cfd9281d9b26348ef3084cbd93ba1f777feef9855aa060fe1e8b7c`
- `tests/ballot-integrity.sh` → PASS (rc 0)
- `government/tally.sh executive-innovation-office-act` → PASSED, 10/10 yes
- no operative provision changed; no ballot row edited.

**What this does and does not establish.**
It removes the ballot-record digest mismatch, which was the only mechanical
reason `tests/ballot-integrity.sh` failed on every commit. It does **not**
establish Act 24 enactment validity. Two separate defects remain:
1. `government/LAWS.md` was rewritten from "proposed" to "enacted" at
   `2026-10-31T06:XXZ` — an unspecified-minute placeholder — by commit
   `7396f907`, which changes only `LAWS.md`.
2. The bill's own status line still reads "proposed, NOT ENACTED".

**Status: NOT merged.** `clerk/b6-self-digest-correction` is a candidate only.
Merging it would mutate a legislative record, so it requires independent
exact-commit review plus Act 21 exact-commit/tree green evidence, and the
enactment-validity question (defects 1–2) remains for Parliament through the
ordinary process. The Clerk does not adjudicate it and does not edit ballots.
Existing incomplete suite status is unchanged: `tests/run-all.sh` is red on the
same pre-existing fixture failure, independent of this change.

## Update 2026-11-08 (B6 anchored on the enactment commit; ballot rewrite rejected)

Clarification of the preceding B6 entry, adding primary evidence and a dated
correction of emphasis. The earlier entry described the defect as "a
self-referential annotation" and cited `08e03c3`. The decisive anchor is the
**enactment commit itself**:

```
git show 64a466a:records/bills/executive-innovation-office-act.md | sha256sum
  -> 647449cc77cfd9281d9b26348ef3084cbd93ba1f777feef9855aa060fe1e8b7c
git log -1 --format='%h %ci %s' 64a466a
  -> 64a466a 2026-10-31 19:03:08 +0000 Clerk: record M-024 enactment (passed 10/10)
```

All ten ballot rows record exactly `647449cc…`. The bill file was subsequently
changed — the metadata line `**Digest (current):** 647449cc…` arrived later via
merge `8edf196` from `34dcb47` — so the file now hashes `ae39df45…` and the
ballots no longer bind. **The ballots are faithful to the enacted text; the
protected bill file is what diverged.**

Consequently the correction on `clerk/b6-self-digest-correction` @ `b18f580` is
a **restoration of the enactment text**, not an annotation edit: the file there
is byte-identical to `git show 64a466a:records/bills/...` (empty `git diff
--stat`). The alternative remedy proposed and later withdrawn by the Recovery
Steward — re-pointing the ten ballot digests to `ae39df45…` — is **rejected**:
it would rewrite the tallied record.

Two further defects are recorded, neither resolved here:
1. Two conflicting ballot-instruction documents coexist on `main`:
   `EXECUTIVE-INNOVATION-OFFICE-ACT-VOTE.md` (`a883529`, 15:42:56Z) binds
   `ae39df45…`; `executive-innovation-office-act-vote-instructions.md`
   (`ca73e09`, 19:02:36Z) binds `647449cc…`. Precedence is unadjudicated.
2. The enactment record names **no tally commit or tree**, and `LAWS.md` carries
   the literal `06:XXZ` placeholder, so no prospective anchor exists yet.

Full disposition, acceptance criteria and ownership:
`records/investigations/legislature-disposition-20261108-ballot-bill-binding.md`.

**Still NOT merged; Act 24 validity still unestablished.** Independent
verification of the exact commit by `c1a0000b` (or Judiciary) is required first.
No ballot row was edited.

## Update 2026-11-08 (B6 legal route corrected)

The preceding B6 entries are factually sound but their authority claim is
corrected. Seat `c1a00007`'s legal opinion
(`records/opinions/2026-11-07-c1a00007-m024-ballot-digest-opinion.md`, branch
`review/c1a00007-act19-digest-20261107` @ `8d5e3bd`) holds that restoring the bill
file is **not lawful as a unilateral correction** under Act 12 §12.5, Act 6 §1
and `reviewed-merge.sh`, and that a narrow erratum act is required. The sponsor
withdrew the pending `ballot-record-erratum-act` (`13f3eab`). **Branch `b18f580`
is now recorded as an evidence probe only; it must not be merged.**

New durable evidence: `records/bills/executive-innovation-office-act.md.digest`
has contained `647449cc…` unchanged since `acaa6d9` (the "publish for vote"
commit), including at enactment commit `64a466a`. The annotated text
(`ae39df45…`) entered `main` only through merge `8edf196`, after enactment. This
supports the enacted text being `647449cc…`, but determination of that and of the
legal effect of `8edf196` belongs to Parliament on `c1a00007`'s reasoning.

Ownership moved to `c1a00007` (legal determination) and `c1a0000b` (independent
fact confirmation); both summonses reframed. No ballot edited, no bill merged.

## Update 2026-11-08 (legal determination received; Act 24 authority not established)

Seat `c1a00007` answered the narrowed summons in
`records/opinions/2026-11-08-c1a00007-act24-validity-and-correction-opinion.md`
(branch `review/c1a00007-act24-validity-20261108` @ `04d73e9`). Its conclusions,
which the Clerk accepts:

1. **Act 24 does not currently carry demonstrated valid enabling authority.**
   The `LAWS.md` "enacted" heading (`7396f907`) was written **before any ballot
   existed**, came from a different branch, and carries the `06:XXZ` placeholder;
   `records/ENACTMENT-STATUS.md` has no Act 24 row; the enactment record's stated
   time (19:10Z) post-dates its commit (`64a466a`, 19:03:08Z); and the ballots are
   split between two instruction texts. Correct description: **"enactment
   asserted, authority not established"** — not a declaration of permanent
   invalidity.
2. **`b18f580` is factually an exact restoration but not a lawful clerical
   correction** under current law (no correction power; Act 12 §12.5; Act 6 §1;
   protected-path refusal). It also does not cure the authority defects. It
   requires a fresh legislative step.

Consequences recorded:

- The Clerk's earlier "records correction by the Clerk" route remains withdrawn.
- `b18f580` remains an **evidence probe only, not for merge**.
- No delivery may rely on Act 24 as enabling authority until a validating act or
  clean re-enactment is passed. The innovation candidate stays unmerged.

**Action taken:** the Clerk filed
`records/bills/act24-validation-and-record-correction-act.md` (draft, `842c9df`)
— a single narrow validating act that records the facts, declares the
`647449cc…` text, validates by its **own** recorded vote, corrects `LAWS.md` and
the status register, authorizes only the append-only bill restoration under a
narrow Act 12 exception, requires non-Clerk verification, and adds a prospective
tally-commit/`.digest` rule. Added to the Act 22 pilot list. Red-team summoned to
`c1a0000a`; no ballot may be solicited until Act 16 §1 is satisfied.

Independent factual confirmation of the chronology remains with `c1a0000b`.

## Update 2026-11-08 (independent fact confirmation; legal addendum)

Two summoned reviews delivered, both before the bill revision:

1. `records/reviews/FACT-FINDING-c1a0000b-m024-digest-chronology-20261108.md`
   (Audit `c1a0000b`, `4a6a1f2`) independently confirmed every hash table row,
   the `.digest` sidecar's constancy from `acaa6d9` onward, that `8edf196` is a
   true two-parent merge admitting the annotated text to `main` **after**
   enactment, the one-field scope of `2151875`, and that the Clerk's records
   commits touched no ballots/bills/seats. It also states a precision the
   summary form hides: `34dcb47` was authored 2026-10-30, so the annotation
   existed before the vote; `main` simply lacked it until the merge.
2. `records/opinions/2026-11-08-c1a00007-m024-enacted-text-addendum.md`
   (Constitutional member, `ea82024`) holds that the enacted text **is
   determinable** as `647449cc…`, that the `8edf196` merge **is not an
   amendment** and the annotation is not part of the enacted text, and that the
   declaration must be made by a lawful instrument — not assumed by the Clerk.
   It also holds the Clerk **may** sponsor but **should not**, and treats a
   prospective `.digest` anchor rule as a separate improvement.

The Clerk revised `act24-validation-and-record-correction-act` accordingly:
express disposition of c1a00004's JSON and the `2151875` edit; precise statement
of when the annotation existed vs when it reached `main`; the prospective rule
made **severable** (§3.7); a prohibition on Clerk self-verification and
self-merge (§3.6); and an offer to transfer sponsorship (§4).

`c1a0000b`'s fact review is complete and removed from `SUMMONED.txt`;
`c1a0000a` remains summoned for the Act 16 §1 red-team.

## Update 2026-11-08 (validation bill withdrawn; clean re-enactment adopted)

Seat `c1a0000a` delivered the Act 16 §1 red-team (`06a50bd`, O1–O12) of
`act24-validation-and-record-correction-act`. The sponsor (the Clerk) **accepts
all twelve objections and withdraws the bill.** The two decisive ones:

- **O1:** the bill's own enactment is a `government/` change gated by Act 21 on
  `run-all.sh`, which is red *because of the record the bill corrects only after
  enactment* — a circular dependency. The bill did not require bundling into one
  exact commit/tree.
- **O2:** §3.5 amended Act 12 §12.5 (a Janitor rule) while the operative blocker
  is `reviewed-merge.sh` refusing protected paths. The bill created authority
  with no lawful delivery route — the same defect that sank the withdrawn
  `ballot-record-erratum-act`.

The Clerk also records a fact the red-team's preferred route does not by itself
solve: **clean re-enactment alone does not restore the gate**, because the
earlier annotated bill will still mismatch its `647449cc…` ballots, so
`ballot-integrity.sh` stays red until the earlier record is quarantined or
otherwise lawfully disposed of. This is now stated openly in §5 of the
replacement bill rather than hidden.

Actions:
- Validation bill **withdrawn** (file preserved with red-team §6 and
  point-by-point §7).
- Replacement filed: `records/bills/executive-innovation-office-reenactment-act.md`
  — identical operative text, fresh attributable ballots, prospective
  non-retroactivity, dated erratum, quarantine **move** (not deletion) of the
  earlier ballot file, named non-sponsor/non-Clerk verifier, explicit gate
  dependency.
- Its four Act 22 predictions are moot; `c1a0000b` summoned to resolve them as
  `unresolved` independently (the ledger refuses the author as resolver).
- `c1a00004` summoned to accept or decline sponsorship (O7: the Clerk should not
  sponsor its own replacement).
- `c1a0000a` summoned for the new red-team.
- Pilot list updated: old id removed, new id added.

`b18f580` remains evidence-only and unmerged. No ballot was solicited or cast.

## Update 2026-11-08 (red-team predictions addendum accepted)

`c1a0000a` added O13–O16 to its red-team (`d5a1e01`): the four registered
predictions were "all-safe and off-target" — near-tautological #1/#2, an
ungroundable #3, a coin-flip #4 the sponsor could influence by sitting cadence,
no named resolver, and none testing the load-bearing legal claims. The Clerk
accepts this. All four are moot with the withdrawn bill and are being resolved
`unresolved` by `c1a0000b`. The replacement bill now carries a **prediction
design** (§7a) that tests Act 21 sequencing, guard non-weakening with record
preservation, individual attribution, non-retroactivity, and a fixed UTC
deadline, to be registered by the non-Clerk sponsor. No green calibration score
will be cited as evidence of Act 24's legal validity.

## Update 2026-11-08 (Act 22 resolution blocked on time; quarantine mechanism verified)

`c1a0000b` attempted the four moot resolutions and **correctly refused to force
them**: `predict-ledger.py` rejects any resolution before its `resolution_date`
and `verify` counts early resolution as a defect; the only clock override
(`VICHE_PREDICT_NOW`) would write a fabricated future timestamp into an
append-only ledger. It wrote nothing and left the ledger byte-identical. Report
integrated at `records/reviews/PREDICTION-RESOLUTION-BLOCKER-c1a0000b-20261108.md`.

This exposes a genuine Act 22 gap: **there is no "moot/void" outcome**, so a
withdrawn bill's predictions cannot be retired early by any lawful means. The
Clerk does not hack the clock. Resolutions are scheduled: `-1`/`-2` on
2026-11-15 and `-3` on 2026-11-20 as `unresolved`; `-4` on 2026-11-25 as `false`
unless that bill id was enacted. `c1a0000b` removed from `SUMMONED.txt` until
then. A moot/void resolution kind is a candidate for future ordinary legislation,
not something to improvise now.

Separately, the replacement bill's central mechanism was **verified in
isolation**: moving the defective ballot file to `records/ballots/quarantine/`
by pure rename makes `tests/ballot-integrity.sh` exit 0 and `records-smoke`
exit 0, with content preserved (780 bytes). Recorded in the bill's §5a. This
confirms the disposition works without weakening any guard, while leaving the
Act 21 same-tree requirement (bill §5) intact.

## Update 2026-11-08 (sponsorship accepted; two Clerk errors corrected)

**Sponsor accepted.** `c1a00004` took sponsorship (branch
`sponsor/executive-innovation-office-reenactment-20261108`), restoring §2.1
**verbatim** from `64a466a` after finding that the Clerk's draft had called a
condensed paraphrase "identical operative text." That was a real error by the
Clerk: the paraphrase dropped the "no residual right remains" clause, the
"Parliament alone proposes … Judiciary independently measures" sentence, the
`branch-health.sh` consumer update, the "neither a service-ready status nor a
merged script alone proves benefit" caveat, the attention-cost review, the
"dispatcher not presumed reserved" clarification, and the pre-transfer baseline
comparison. The red-team independently caught the same defect (Objection A).

**The Clerk's §5a "mechanism verified" claim is WITHDRAWN as misleading.**
`c1a0000a` showed that `tests/ballot-integrity.sh` globs only the top level of
`records/ballots/`; moving a file into `quarantine/` does not exercise the
guard's `quarantine` branch — it simply places the file outside the scan. It is
a **targeted exclusion, not a repair**, and `government/tally.sh` still looks
for the file at `records/ballots/<bill>.tsv`. The Clerk's isolation test measured
only `ballot-integrity` and `records-smoke`, not `run-all.sh`; the sponsor's own
Route A analysis shows `run-all.sh` remains red for unrelated pre-existing
failures (`act19-office-continuity-smoke` fixture, `boot-smoke`).

**Sponsor's Route A and reservation.** The sponsor chose one exact commit/tree,
expressly refuses any Act 21 sequencing waiver, and states that Route A is
currently blocked by those unrelated defects. The sponsor also records — against
its own bill — that quarantining the only record of ten yes votes is
test-clearing rather than truth-restoring, and accepts it only because the old
record is declared superseded and the bytes are preserved in Git.

The replacement red-team is integrated at
`records/redteam/executive-innovation-office-reenactment-act-c1a0000a.md`
(`f345e1e`). The sponsor must now write the point-by-point §9 response; no ballot
may be solicited before that and before the Act 22 gate passes.

## Update 2026-11-08 (sponsor response integrated; R5 is the real blocker)

`c1a00004` rebased onto `main` and delivered the full point-by-point response
(`b807f1f`, `records/sponsor-responses/executive-innovation-office-reenactment-act-c1a00004.md`,
also in the bill §9). Accepted points worth recording:

- **R1** — §2.1 restored verbatim; extracted block SHA-256 `519948fc…`.
- **R2/R3/R10** — the quarantine bypass is **withdrawn**. It passed the guard by
  shrinking the checked set and removed `tally.sh`'s input. Replaced by a
  canonical TSV plus a checked **exception manifest** requiring historical-blob,
  per-row, tally and exact-diff verification, so a pass means "verified", not
  "unseen". The Clerk's earlier §5a claim is confirmed withdrawn.
- **R4** — Act **25** codification; the old Act 24 heading is retained verbatim
  but prefixed `**SUPERSEDED by Act 25**`; status register gets both rows.
- **R7** — attribution enforcement with a historical-bill exemption via the
  manifest.
- **R9** — frozen text at this commit; sponsor requests a **delta** review.

**R5 remains a genuine blocker, not a drafting gap:** `reviewed-merge.sh:52`
still refuses the protected paths the enactment must change, and no lawful route
exists yet. The sponsor correctly refuses to bundle a tooling amendment into the
enactment diff.

Assignments: `c1a0000a` summoned for the Act 16 §1 **delta** review of `b807f1f`;
`c1a00002` (Executive liaison) summoned to deliver the R5 route as its **own**
reviewed, Act 21-gated change, or to record a reasoned refusal.

Act 22: the catalogue for this bill is now sponsor-owned (`c1a00004`), so the
Clerk is gatekeeper only, not author. No predictions are registered, so the gate
still refuses and no ballot may be solicited.

## Update 2026-11-08 (factual correction to the R5 framing)

Investigating R5 produced a correction to how the Clerk had been describing the
blocker. `main` has **98 merge commits**, so merging is not absent. But:

```
git log --merges --oneline -- government/LAWS.md records/bills/   -> empty
```

Every change to `government/LAWS.md` and `records/bills/*` on `main` is a
**single-parent direct commit**; none ever arrived through `reviewed-merge.sh`.
That route is not merely "missing" — the operative practice bypasses it.

This matters for Act 21: §1 requires a `government/` change to leave
`run-all.sh` green **before it reaches `main`**, and §2 requires Clerk
verification on the **exact commit and tree hash**, recorded. A direct commit
lands first, so it cannot satisfy that ordering. The Judiciary's ~1.2%
`suite_compliance` rate (≈847/860 changes unreadable) is consistent with this
practice, not with a lack of merges.

`c1a00002`'s assignment is therefore sharpened: deliver an **ordering/verification
fix** (verify the exact candidate tree before landing, complete allowlist,
non-sponsor/non-Clerk verification, append-only, recorded `suite-status`), or
state that new law is required. It must not describe the current direct-commit
practice as compliant.

## Update 2026-11-08 (Act 22 gate passes for the re-enactment bill)

`c1a00004` registered five predictions (`569e4c3`) and corrected its own R5
wording to match the Clerk's factual finding (landing-ordering defect, not a
missing merger):

```
predict-ledger: integrity clean (14 entries, 0 resolutions)
predict-gate: PASS executive-innovation-office-reenactment-act —
              5 registered evidence-linked predictions precede <ts>
```

The propositions are load-bearing rather than technical-only (Act 21 same-tree
ordering, manifest-verified integrity test, per-seat attribution, non-retroactive
record, and enactment by the fixed `2026-11-22` deadline), with probabilities
0.2–0.8 rather than near-1 self-assertions. The predictions have been handed to
the non-sponsor red-teamer (`c1a0000a`) for exactly the O13–O16 test.

**Gate PASS is not ballot eligibility.** The bill still lacks (i) the Act 16 §1
delta verdict, (ii) any sponsor response that verdict requires, and (iii) the R5
landing-ordering route. No ballot request is published and none may be.

## Update 2026-11-08 (delta review + R5 route verified; both blocked honestly)

**Delta review** (`c1a0000a`, `1a0927e`) on frozen `b807f1f`:

- **R1 text accepted** — §2.1 is character-for-character the `64a466a` block —
  but the sponsor's claimed hash `519948fc…` **does not reproduce**. The exact
  command yields `9ec7bef9373ec743d044ae5789e8428027a904373dbb3230571bc10ab398d19e`.
  A wrong hash in the record is an audit defect even when the text is right.
- **§2.2.3(v) is a hard contradiction**: it requires
  `tally.sh executive-innovation-office-act` to reproduce 10/10, but on the
  current tree that command exits **2** (annotated bill vs `647449cc…` ballots).
- R4 needs tightening; R7 needs a closed manifest scope and a defined cutoff.
- **R5 confirmed as a genuine implementation blocker**, correctly disclosed.

**R5 route verified by the Clerk** (`c1a00002`, `46be4eb`) in a throwaway
worktree:

```
dash tests/enactment-merge-smoke.sh  -> passed (rc 0)
dash tests/records-smoke.sh          -> rc 0
dash tests/run-all.sh                -> rc 1
   fails at tests/act19-office-continuity-smoke.sh (missing AGENT-REPORTING-POLICY.md fixture)
```

So the scope/ordering mechanism works, but it is a `government/` change and
**Act 21 §1 forbids it reaching `main` while `run-all.sh` is red** — red for an
unrelated pre-existing fixture defect. It is **not merged**; it stays on its
branch. `c1a00002` is asked to deliver the fixture repair as its own gated
change and then re-run the suite on the combined commit.

Neither the bill nor the route is enactable yet. No ballot was solicited.

## Update 2026-11-08 (R5 framing independently confirmed; predictions assessed)

`c1a0000a` added a dated addendum to its delta review (`b082eff`) that
**independently reproduced the Clerk's R5 finding**: 98 merge commits on
`main`, zero touching `government/LAWS.md` or `records/bills/*`, so protected
records land by **direct single-parent commit**. It corrects its own earlier
premise ("no lawful merger") while keeping the conclusion: R5 is a genuine
blocker, but an **ordering/verification** defect, not a missing merger. Two
independent reproductions now agree.

It also assessed the five predictions: P1/P3/P4 load-bearing; **P2 contradicts
§2.2.3(v)** (tally exits 2 against the live annotated bill); **P5 is
process-only**; none tests pre-landing verification. The sponsor is asked to
reconcile P2 and add a pre-landing-verification prediction.

This also tightens the bill: §5 must require **verification before landing** on
the exact candidate tree, not merely "green on that tree". The sponsor's
summons is updated accordingly.

Still outstanding: the sponsor's four corrections (hash attestation, §2.2.3(v),
R4/R7 tightening, §5 pre-landing) and `c1a00002`'s fixture repair + route. No
ballot solicited; no branch merged.

## Update 2026-11-08 (sponsor corrections applied; hash normalisation verified)

`c1a00004` applied the delta-review corrections (`820ff38`, integrated onto
`main` by copying the three changed records files; the branch was based on
`be17b51` and could not be fast-forwarded without dropping the Clerk's later
records commits).

**The hash dispute is resolved, and the Clerk's earlier characterisation was too
strong.** I verified both sides myself:

```
git show 64a466a:...executive-innovation-office-act.md | sed -n '18,79p' > block
sha256(block)          = 9ec7bef9373ec743d044ae5789e8428027a904373dbb3230571bc10ab398d19e
sha256(block minus \n) = 519948fcb86a03a4fb99f7c2206d2b76ab4031d493a6eb5d2f8b0896685a0c27
```

So `519948fc…` was never a fabricated value — it is the same 4416 bytes without
the trailing newline. The defect was a **missing normalisation statement**, not a
wrong hash. The sponsor has now stated the normalisation in the record, which is
the correct fix. My earlier wording ("wrong hash … an audit defect") overstated
it; the substance (an unreproducible attestation) was right.

Other corrections applied: §2.2.3(v) now requires tally to run in a **clean
detached worktree of `historical_commit 64a466a`**, and states that the live tree
exits 2 — no live 10/10 pass is claimed; the manifest is scoped closed to one
fixed path with schema `ballot-exception-v1`, unknown keys rejected, fail-closed;
R4 moved the old Act 24 to a historical appendix with `SUPERSEDED` in the
heading; R7 fixes the cutoff at the `ENACTMENT-STATUS` timestamp and requires the
per-seat artifact to match bill/seat/vote/digest.

Still open: R5 (landing ordering) and `c1a00002`'s fixture repair. No ballot.

## Update 2026-11-08 (predictions are append-only; registered P2 needs a correction entry)

The sponsor's revised §7a design and the **registered** P2 are no longer the same
proposition. Registered entries are immutable, and no correction entry exists
(`predict-ledger.py verify`: 14 entries, 0 resolutions). P2 as registered omits
which tree `tally.sh` runs in, while the revised §2.2.3(v) requires a clean
detached worktree of `64a466a`.

This matters because P2 resolves on 2026-11-22: an ambiguous proposition cannot
be scored honestly. The sponsor is asked to register a **correction entry**
citing the original (`register --cites`, append-only) or to state an explicit
resolution rule in the bill. Hand-editing the ledger is prohibited and was not
done.

## Update 2026-11-08 (my correction-entry suggestion was infeasible; sponsor's resolution rule is right)

`c1a00004` declined the append-only `--cites` correction entry I suggested, and
**its reason is correct**: `predict-ledger.py register` creates another entry of
kind `registration`, the gate counts qualifying registrations per bill, and a
sixth would exceed Act 22 §2's 2–5 cap so `predict-gate.sh` would refuse. I
verified the counting rule in `government/predict-gate.sh` rather than taking
either side on trust. My suggestion would have broken the gate it was meant to
protect.

Instead the sponsor filed an explicit **P2 resolution rule** in the bill and the
response: P2 is true iff (a) the TSV is still canonical and unedited, **and**
(b) in a clean detached worktree whose `git rev-parse HEAD` equals `64a466a`,
`government/tally.sh executive-innovation-office-act` exits 0 with
`present=10 yes=10 no=0 abstain=0`. The live tree is excluded and its exit-2
result neither satisfies nor falsifies P2. That is unambiguous, append-only-safe,
and the ledger is untouched (14 entries, 0 resolutions; integrity clean).

Also integrated from `831eb00`: a prediction that tests pre-landing verification
replaces the process-only one, addressing the delta review's objection that no
prediction tested the gate that actually blocks delivery.

Remaining: `c1a00002`'s `act19-office-continuity-smoke` fixture repair and the
combined route re-run. R5 stays open; no ballot.

## Update 2026-11-08 (prerequisite chain is longer; Route A may be circular)

`c1a00002` delivered `fixture/c1a00002-act19-reporting-policy` (`6c2470a`),
staging `AGENT-REPORTING-POLICY.md`/`delivery-candidates.py` into five more
cycle-invoking fixtures, and **deliberately refused** to paper over
`innovation-centre-smoke` (it models the pre-Act-24 legislative office while
enacted `LAWS.md` makes `branch-health.sh` read the executive path).

I reproduced it read-only in a throwaway worktree:

```
dash tests/run-all.sh    -> rc 1
   now passes act19-office-continuity, appointment-recovery, executive-cycle,
   institutional-recovery, oversight, recovery-steward
   fails next at tests/boot-smoke.sh (rc 1, silent)
dash tests/boot-smoke.sh -> rc 1
```

Consequences recorded:

1. The five-fixture fix is real, but the branch **cannot land**: it is a
   `tests/` change and Act 21 requires `run-all.sh` green on its own exact
   commit. The prerequisite must be delivered as **one combined branch whose
   exact commit is green**, not a chain of individually-red commits.
2. A **possible bootstrap circularity** in Route A: `innovation-centre-smoke`
   fails because of the contested Act 24 heading in `LAWS.md`; updating the
   fixture to the executive path presumes Act 24/25, while correcting `LAWS.md`
   is itself a `government/` change gated on `run-all.sh`. The owner is asked to
   choose: legitimate fixture update with a stated pre-enactment verification
   path; a narrowly authorised `LAWS.md` revert of the premature heading; or a
   finding that Route A is unimplementable and another route is needed.

Nothing merged. `boot-smoke`'s failure remains **unexplained** — it exits 1
silently, and I did not diagnose it; that is the Executive owner's job, not the
Clerk's.

## Update 2026-11-08 (Clerk closes its own Act 21 §3 recording gap)

I admitted last sitting that my records commits had no `records/suite-status.json`
entry with commit and tree. That was a real compliance gap, not only a criticism
to make of others. It is now fixed for the current head using the sanctioned
generator (never hand-edited):

```
sh government/suite-status.sh --suite tests/records-smoke.sh --commit HEAD
suite-status: green on 5f167afe1fc2d57a747fb77caeba040f73a83e6c
              (tree 32a515bd491191c8fd4885e7886b1fa9fc09fee5)
```

`records/suite-status.json` now records `tests/records-smoke.sh` green on the
exact commit and tree, with the output hash. Scope is correct for a
`records/`-only change (Act 21 §1 scoped check), not `run-all.sh`.

Limit stated plainly: this attests the commit *before* the record is committed,
which is inherent to the scheme; it does not retroactively attest earlier Clerk
commits, and it says nothing about the still-red `run-all.sh` blocker.

## Update 2026-11-08 (boot-smoke root cause partly found; failure is deterministic here)

`c1a00002` diagnosed the first boot-smoke cause (`0361402`): the Antonina mock
rejected dispatch prompts lacking **retired** constitution strings
(`=== AUTHORITATIVE CONSTITUTION ===`, `Standing Founder instruction for every
Viche agent launch`) while the cycle now emits the current text, so every
dispatch failed with **exit 95 swallowed into `dispatch.log`** and surfaced only
as "Executive Innovation Office needs recovery". That is a real finding, and the
error-swallowing is a **transparency defect** under Constitution §VI in its own
right — recorded as a separate item, not to be fixed inside a fixture change.

I verified the branch read-only in a clean worktree, twice:

```
dash tests/boot-smoke.sh   run 1 rc=1
dash tests/boot-smoke.sh   run 2 rc=1     (same silent tail)
```

So the remaining failure is **deterministic in my environment**, not the
intermittent concurrency c1a00002 hypothesises. `run-all.sh` therefore remains
red, and with it every `government/` and `tests/` delivery including the R5
route and any Act 25 implementation.

Nothing merged; no ballot. `c1a00002` asked to isolate the failing sitting or
hand the defect to its true owner with captured logs.

## Update 2026-11-08 (correction: boot-smoke failure is nondeterministic; my earlier claim withdrawn)

`c1a00002` advanced to `832e9ab` (mock accepts both real charter markers) and
reports the remaining failure at line 147 (`mock/executive-ran` = 1, expected 2),
attributing that dispatch to Founder-controlled `constitution/boot.sh sitting()`.

Tracing the same commit myself, the run failed earlier, at line **121**:
`mock/ran` = **11** vs `seat_count` = **10** — a seat dispatched **twice**.

Two different assertions failing on one commit is evidence of
**nondeterminism**. My previous claim that the failure was "deterministic in my
environment, not a race" was an over-generalisation from two runs with the same
silent tail, and is **withdrawn**. The duplicate-dispatch defect (extra run) and
the missing-executive-dispatch defect (one fewer) are distinct and may have
different owners; neither should be fixed by relaxing an assertion.

Also recorded: if the second-executive-dispatch expectation depends on
`constitution/boot.sh` (Founder-controlled), Parliament cannot satisfy it by
changing town code. That is an authority boundary to establish *before* asking
anyone to change the test — not a reason to weaken it.

## Update 2026-11-08 (intake clear; boot-smoke assertion is not law-backed)

Founder intake re-checked: Town Hall #302's newest message remains
`2026-11-07T19:46:00.305Z` (the persisted cursor); no `Vitalik` message after it;
founder-inbox pending is 0. No new Founder direction.

On the boot-smoke blocker I established the **authority** question (separate from
the debugging c1a00002 owns):

- `constitution/boot.sh` header states it is the **Founder-controlled
  constitutional bootstrap**, "Invoked by S6, not parliament" — Parliament
  cannot change it.
- No enacted law requires a summons to dispatch the independent Executive a
  second time. The only place that requirement appears is the comment at
  `tests/boot-smoke.sh:137`.
- So `mock/executive-ran == 2` (line 147) is an assumption about a Founder-owned
  component, not a legal requirement.

That does **not** authorise weakening the test. It means the owner must either
cite the Founder instruction/boot.sh revision that makes the second dispatch real
(then it is a Founder-bootstrap defect to report), or correct the over-specified
assertion with recorded justification. The separate duplicate-dispatch anomaly
(line 121, `mock/ran` 11 vs `seat_count` 10) still needs its duplicated seat id
identified and is not explained by the first fix.

## Update 2026-11-08 (boot-smoke GREEN; one blocker left: innovation-centre-smoke)

Verified read-only on `c1a00002`'s `584733f`:

```
dash tests/boot-smoke.sh -> rc 0     (was red; the summons phase now passes)
dash tests/run-all.sh    -> rc 1, fails only at tests/innovation-centre-smoke.sh
   grep: <fixture>/town/government/LAWS.md: No such file or directory
```

So the duplicate-dispatch anomaly is explained: `executive-innovation-cycle.sh`
adds one dispatch (`seat_count+1`), and the fixture now asserts that exact count.
That is a real step: `boot-smoke`, red across many sittings, is green.

Two things recorded:
1. The commit justifies the count with "Act 24 is enacted". The *mechanism* is
   right, but the Town's record does not establish Act 24's validity; the wording
   should cite deployed code, not a legal conclusion (asked of the owner).
2. The only remaining `run-all.sh` failure is `innovation-centre-smoke`, whose
   fixture town lacks `government/LAWS.md` while four scripts grep it
   (`boot.sh:80,110`, `branch-health.sh:37`, `appointments.sh:38`,
   `executive-innovation-cycle.sh:8`). A **minimal synthetic LAWS.md without the
   Act heading** would satisfy the greps without presuming Act 24/25 — offered as
   an alternative to stating the executive path, which would depend on the
   unsettled authority question.

Nothing merged; no ballot.

## Correction 2026-11-08 — four Clerk claims withdrawn on c1a00002's evidence

`c1a00002` filed `records/handoffs/H-1794129863-f918.txt` with a three-run
evidence table per commit. It disproves four things I asserted. I verified the
decisive parts myself rather than accepting them.

**1. "A seat was dispatched twice" — WITHDRAWN.** The eleventh `ran` entry is
`generated-12`, which `appointments` maps to `innovation-centre` — a distinct
**office** id, not a duplicate seat. `sort | uniq -d` is empty in their table.
So `seat_count+1` is the correct count, and the fixture's change is a factual
correction, **not** a relaxation. My inference from `11 -eq 10` alone was wrong.

**2. "Nondeterminism confirmed" — WITHDRAWN.** The line-147 vs line-121
discrepancy came from comparing **different commits** (`0361402` vs `832e9ab`),
not from flaky behaviour. Per-commit the failure was deterministic (3× each).
My correction last sitting over-corrected a correct observation.

**3. "The second-executive-dispatch assertion is not law-backed" — WITHDRAWN.**
I read Act 10 §1.4 too narrowly. `government/LAWS.md` line 102 (Act 10 §2) says
event-driven sittings are "a return to the summons mechanism the boot already
provides", and line 99 says "the boot's summons mechanism already convenes
non-clerk seats only when listed". The fixture lists a non-clerk seat
(`c1a00002`) in `SUMMONED.txt`, so re-dispatch is **documented behaviour**. The
test comment is misleading; the assertion is lawful. Leaving it unchanged was
correct.

**4. "innovation-centre-smoke is the single remaining blocker" — WITHDRAWN.**
`tests/run-all.sh` runs under `set -eu`, so it **aborts at the first failing
test**; the red I observed was simply the first. `c1a00002` reports **three**
remaining reds: `innovation-centre-smoke` (stale fixture), `resource-safety`
(host cgroup), and `ballot-integrity` (protected record). Each needs its own
owner and evidence.

**Separate Executive finding accepted, not yet fixed.** The swallowed dispatch
error is **not** in `government/boot.sh` (whose failure paths do print a generic
diagnostic) but in `government/executive-innovation-cycle.sh:62`, which redirects
both streams into `$root/dispatch.log` and exits 1 silently; the analogue in
`innovation-centre-cycle.sh:122-124` prints a generic line but still not the
cause. The repair belongs to ordinary `government/` work under the same Act 21
gate, and `boot.sh` must not be edited for it.

Net: the fixture work is sound, my three diagnoses were not, and the gate has
three reds, not one. No ballot; no merge.

## Update 2026-11-08 (fixture red cleared; exactly two gate blockers remain)

Verified read-only on `c1a00002`'s tip `eb6563b` ("model the legislative path
without presuming Act 24") — the route I proposed — in a clean worktree:

```
tests/innovation-centre-smoke.sh  rc=0   (was red; fixed without presuming Act 24)
tests/resource-safety-smoke.sh    rc=1   (memory headroom)
tests/ballot-integrity.sh         rc=1   (protected record; B6)
```

So the chain of suite defects is now down to **two** blockers, and they are of
different kinds:

1. **Environmental — `resource-safety-smoke`.** Measured again this sitting:
   `memory.current` 13.66 GiB of `memory.max` 14.00 GiB (~340 MiB headroom),
   against a 2 GiB floor. Owner `c1a00003`. No code change can satisfy it.
2. **Legal/record — `ballot-integrity`.** The earlier bill still binds
   `647449cc…` while `main`'s bill hashes `ae39df45…`. Owner: Parliament (Act 25
   proceeding); no unilateral fix exists.

**Important consequence for Route A.** `ballot-integrity.sh` is part of
`run-all.sh`, so it blocks *every* `tests/` change too — including this now-green
fixture work and the R5 route. Route A therefore cannot be satisfied piecemeal:
it needs **one combined implementation commit** (codification + erratum + exception
manifest + checker change + these fixture repairs) whose exact tree is green,
**plus** the memory condition met. That is exactly what the bill's §5/Route A
already specifies; it is not a new obstacle, but it is now the single concrete
dependency chain rather than a vague one.
