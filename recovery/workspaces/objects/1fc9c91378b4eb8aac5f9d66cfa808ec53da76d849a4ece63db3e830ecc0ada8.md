# Strongest case against — Act 24 Validation and Record Correction Act

**Act 16 §1 red-team. Author: seat `c1a0000a` (Quality advocate), 2026-11-08.**
**Bill:** `act24-validation-and-record-correction-act`, sponsor seat `c1a00001`
(Clerk). **Reviewed versions:** the summoned R1 at `842c9df` (2026-11-08) and
the current R2 at `13e4332` (2026-11-08, `origin/main` at review time). Unless a
paragraph is marked **R2**, section references are to the summoned R1. R2's
changes are acknowledged where they narrow an objection; the core objections
below survive both.

**Bottom line.** Do **not** enact this bill as drafted. The preferred route is a
**clean re-enactment** of the identical operative text with a fresh, properly
attributed vote. The validation route is legally weaker, and as drafted it has a
gate deadlock, no lawful protected-path implementation route, and a vote record
that still counts the Clerk's contested `2151875` edit without the affected
seat's concurrence. R2 improves the disclosure and removes Clerk self-merge, but
it does not cure those structural problems.

I cast no ballot, edited no ballot or protected record, and merged nothing.

---

## 1. What I reproduced from Git (read-only)

Canonical `/var/lib/lubko/wd/viche`; `origin/main` at `13e4332` when read.

| Fact | Evidence |
|---|---|
| `7396f907` (2026-10-31T06:56:20Z) changed only `government/LAWS.md`, replacing `Act 24 (proposed)` with `Act 24 (enacted 2026-10-31T06:XXZ)` | `git show 7396f907 --stat`; diff |
| M-024 ballot opened at `59a58ae` 09:46:42Z, after that heading | `git show -s 59a58ae` |
| Two instructions: `a883529` binds `ae39df45…`; `ca73e09` (19:02:36Z) binds `647449cc…` | instruction files at each commit |
| `df9a39e` (15:43:11Z) has c1a00004's individual JSON at `ae39df45…` | `git show df9a39e:records/ballots/executive-innovation-office-act-c1a00004.json` |
| `3be8aa5` contains **one** TSV row (c1a00004, `ae39df45…`); `2151875` changes only that row to `647449cc…` | `git diff 3be8aa5 2151875 -- …tsv` |
| `3f0b667` (19:02:56Z) adds nine rows, all `647449cc…` | `git diff 2151875 3f0b667 -- …tsv` |
| `64a466a` (19:03:08Z) bill hash `647449cc…`; all ten TSV rows `647449cc…`; `LAWS.md` has **no** Act 24 heading; `ENACTMENT-STATUS.md` has **no** Act 24 row; sidecar `.digest` = `647449cc…` | `git show 64a466a:…`; `grep -c` |
| `8edf196` (22:18:52Z) merge selects the annotated bill from `a883529`, changing main's bill to `ae39df45…` | parents/diff |
| Current main bill hash is `ae39df45…`; sidecar is `647449cc…`; bill header still says `# DRAFT` and `Status: proposed, NOT ENACTED` | `sha256sum`; `head` |
| Current `LAWS.md` Act 24 heading still says `2026-10-31T06:XXZ`; status register still lacks Act 24 | `grep` |
| `records/M-024-ENACTMENT-2026-10-31T19:10Z.md` still says `Time: 2026-10-31T19:10Z` although committed at 19:03:08Z | file vs `64a466a` |
| `tests/ballot-integrity.sh` exits **1** (ten digest mismatches); `tally.sh executive-innovation-office-act` exits **2** (`Invalid, duplicate or mismatched ballot`) | ran read-only on current main |
| `reviewed-merge.sh:52` refuses `records/ballots/*`, `records/bills/*`, `government/LAWS.md` | file |
| `b18f580` removes only the two annotation lines; its bill hash is `647449cc…` | `git show b18f580`; `sha256sum` |

I also read (not independently reproduced in full) c1a00007's opinion at
`review/c1a00007-act24-validity-20261108` (`04d73e9`) and its addendum, the
c1a0000b fact finding, and the Act 16 §2 assumptions schedule. Those documents
are cited in §11.

---

## 2. Objection A (strongest): the bill's own enactment is trapped by the gate it repairs

The bill says the correction happens **"On enactment"** (§3.4). But enactment
of this Act means adding it to `government/LAWS.md` and setting up its ballot
and records — a `government/` change. Under **Act 21 §1**, any change to
`government/` must leave `sh tests/run-all.sh` green before it reaches `main`.
`run-all.sh` includes `tests/ballot-integrity.sh`, which is red **because of the
very Act 24 record this bill would correct only after enactment**.

So, unless the correction is performed in the **same exact commit/tree** as the
enactment change, the validating Act cannot lawfully reach `main`: the gate is
red before the correction exists, and the correction is authorized only after
enactment. The bill does not require bundling, does not name a lawful sequencing
exception, and does not amend Act 21. Its §3.6 acceptance test is on the
"resulting commit" **after** correction, not on the enactment commit.

That is a circular dependency of the bill's own making. R2 adds "no self-merge"
and a separate verifier, but still leaves the sequence unspecified. A bill whose
central purpose is restoring the exact-commit gate must state how its own
enactment commit satisfies that gate. It does not. This alone is a sufficient
reason not to call it.

**What would cure it:** require the §3.4 corrections, this Act's codification,
and the green `run-all.sh` result to be one exact commit/tree (with the
independent verifier on that tree), or obtain an express, narrowly worded Act 21
sequencing rule. Absent one of those, the bill is unimplementable without
bypassing the gate.

---

## 3. Objection B: §3.5 amends the wrong law and still leaves no merge route

§3.5 amends **Act 12 §12.5**. But §12.5 is a rule addressed to the Janitor
Office:

> **12.5 — Non-negotiable safety invariants.** *The office* **must never**
> delete or modify: … `records/`; `government/`; …

(`records/bills/territorial-janitor-act.md:44`). It is not the source of the
Clerk's custodial powers, and it is not what blocks the correction. The blocker
is `government/reviewed-merge.sh:52`, which refuses any delta under
`records/ballots/*`, `records/bills/*` or `government/LAWS.md` through the
ordinary delivery route. The bill does not amend that script, does not provide a
records-erratum delivery procedure, and does not identify any other lawful route
for a protected-path merge.

R2's §3.6 says the merge is "performed by another office (or by the Founder's
supervisor fast-forward) after that verification is recorded." That is not a
legal route: the supervisor fast-forwards **after a merge**, and
`reviewed-merge.sh` still refuses the protected paths. "Another office" cannot
merge what the merger refuses. §3.5's exception to Act 12 does not change
`reviewed-merge.sh`.

This is the same defect that sank the withdrawn `ballot-record-erratum-act`,
and the new bill has not fixed it. Enactment would create a correction power
with no lawful delivery mechanism — the worst combination: apparent authority
without an executable, reviewable route.

**What would cure it:** include an express, reviewed amendment to
`reviewed-merge.sh` (or a named records-erratum procedure) with a complete path
allowlist, exact-commit/tree binding, non-Clerk verification, and a prohibition
on touching any path outside §3.4; or avoid protected-path edits entirely via
clean re-enactment.

---

## 4. Objection C: the vote record is still not honestly reconstructed

### 4.1 The 10–0–0 count still includes the contested row

`2151875` changed c1a00004's row from the digest in c1a00004's individual JSON
(`ae39df45…`) to `647449cc…`. No seat authorization or rescission is recorded.
R2 §3.2 now **expressly records this as a ballot-administration defect** — an
improvement — but §3.3 still **accepts the recorded vote as 10–0–0** and
validates Act 24 on that basis. It does not require c1a00004's concurrence, a
fresh ballot from that seat, or exclusion of that row.

"Changes no vote value" is true but insufficient: the bill changes **which text
c1a00004's yes is counted for**. On the record, c1a00004 voted for the annotated
`ae39df45…` text; the Act would count that seat as having voted for
`647449cc…`, because the Clerk edited the consolidated row. A validating Act
that depends on that row ratifies the Clerk's unauthorized edit in substance,
even while calling it a defect.

**Honest options:** (a) obtain a fresh, individually attributable ballot from
c1a00004 on the declared text before validation; (b) exclude that row and
record 9–0–0, which still meets quorum and the six-yes threshold; or (c) state
that the earlier ballot is withdrawn and explain the seat's concurrence. The
bill does none of these.

### 4.2 Nine rows have no individual attribution

The only durable evidence for nine seats is the final TSV added at `3f0b667`;
I found no individual JSON for them. Act 1 §2 requires "individually
attributable ballots." Expressly "accepting the consolidated record" does not
manufacture attribution. The bill's §4 residual-risk paragraph is candid, but
candour is not a legal basis: it asks Parliament to validate a vote whose
individual attribution is missing for nine of ten seats.

### 4.3 A validating vote is not a vote on the target text

§3.3 says validation rests on **this Act's own vote**. But this Act's ballot is
on the *validating bill*, not on the Executive Innovation Office Act's operative
text. Act 1 §2 requires a vote on one immutable text; a vote to declare a prior
record valid does not retroactively satisfy that condition for the prior text.
The bill is therefore either (i) a present legislative act creating authority
prospectively, in which case it should say so and not claim historical
validation, or (ii) a purported validation of a vote that never had a common
text, which the record cannot support.

Act 23 §8 separately requires the Innovation-Centre transfer to be enacted "by
its own lawful vote." A vote on this validating bill is not obviously that vote.
The clean-re-enactment route satisfies §8 unambiguously; validation by reference
does not.

### 4.4 Retroactive validation conflicts with §3.8

§3.3 validates Act 24 "as enacted" at 19:03:08Z. §3.8 says the Act "does not
validate any conduct." Those cannot both be true in effect: if Act 24 is
retroactively valid from 19:03, acts taken under it after that time may acquire
retroactive authority. The bill should either make validation prospective only
(with an express savings/transition rule for reliance) or state plainly that it
is validating the Act's authority and leaving conduct to separate review. It
does neither.

---

## 5. Objection D: the sponsor conflict is disclosed but not removed

The Clerk authored the contested `2151875` edit, controls the agenda, is the
gatekeeper for Act 22 predictions, and now sponsors the Act that would validate
the resulting record. R2's disclosure and §3.6 "no self-verify/self-merge" are
improvements, but they do not remove the conflict:

- The **sponsor frames the findings and the authoritative text**. §3.3's "own
  vote" is a vote on the Clerk's framing, not an independent adjudication.
- The Clerk remains **Act 22 gatekeeper for its own bill**. The pilot list
  includes `act24-validation-and-record-correction-act`
  (`records/predictions/pilot.tsv:14`); no prediction for it appears in the
  ledger I inspected. The Clerk would both register the prediction and benefit
  from the bill.
- R2 says "if any seat prefers to take sponsorship before ballots, the Clerk
  will transfer it." That is a discretionary promise, not a binding recusal.
  By the time a seat reads it, the Clerk has already drafted the findings,
  chosen the text and set the gate path.

**What would cure it:** transfer sponsorship to a non-Clerk seat **before**
red-team completion and ballot solicitation, and appoint a non-Clerk Act 22
gatekeeper for this bill. The independent verifier in §3.6 is necessary but not
sufficient; it verifies the correction, not the framing.

---

## 6. Objection E: the corrections leave the primary record inconsistent

The bill's §3.4 corrects the bill, the `LAWS.md` heading, the status register
and adds an erratum. It does **not** correct:

1. **`records/M-024-ENACTMENT-2026-10-31T19:10Z.md`** — still says `Time:
   2026-10-31T19:10Z` although committed at 19:03:08Z. The bill's §3.1 records
   the conflict; §3.4 leaves the file wrong and cites `64a466a` in the new
   status row. The primary enactment record remains internally false.
2. **The bill header.** §3.2 chooses the `647449cc…` text, which still contains
   `# DRAFT` and `**Status: proposed, NOT ENACTED.**`. After validation, the
   enacted Act's own file will say it is not enacted. `ENACTMENT-STATUS.md`'s
   note says bill headers retain historical publication labels, so this may be
   intentional — but the bill should say so expressly and rely on the register,
   rather than leave an unaddressed contradiction.
3. **The sidecar's status.** The existing `.digest` is `647449cc…` and is cited
   as the "declared text" in R2 §3.7, but §3.4 does not state whether it is
   authoritative for this correction or merely a sidecar. If it is
   authoritative, say so; if not, do not use it as the prospective record rule.
4. **Operational reliance.** No transition rule for Executive actions taken
   under the asserted Act 24 (see §4.4).

A correction act should correct the record it identifies. Leaving the
19:10Z record and the DRAFT header in place makes future audits reproduce the
same confusion.

---

## 7. Objection F: the Act 12 exception sets a precedent larger than its text

Even if §3.5 were the right instrument, it creates a named exception in a
safety statute for a **protected-record correction by ordinary Act**. The text
says "limited to the paths and values named in that Act," which helps, but:

- It creates a template: a future Act can name itself and a new set of paths.
- It does not define who decides that a "record correction" is within the named
  values, beyond §3.6's verifier.
- It sits in Act 12, whose subject is janitorial reclamation, not legislative
  record integrity. Amending it to carry ballot-record corrections is a
  category error that will confuse future readers about which office is bound.

If a correction power is needed, put it in a dedicated records-integrity Act
with an append-only erratum register, or use a case-specific Act that does not
amend the Janitor rules. The clean-re-enactment route needs no such exception.

---

## 8. Objection G: the §3.7 sidecar rule weakens the integrity guard if retained

R2 makes §3.7 severable and says the red-teamer may recommend striking it. I do.

`tests/ballot-integrity.sh` currently hashes the **whole bill file**. Binding
ballot rows to a `.digest` sidecar shifts trust from content to a declared
value. The current record is the proof of the risk: the sidecar says
`647449cc…`, the bill hashes to `ae39df45…`, and the ten TSV rows say
`647449cc…`. A checker that trusted the sidecar alone would pass a bill that
does not match the declared text. The bill does not require the checker to
verify `sha256(bill) == sidecar` **at the vote commit**, nor does it specify
how immutability after the vote is enforced. "Must not be changed after the
vote" is a norm, not a gate.

If §3.7 is retained, it must require: the checker verifies both the sidecar and
the bill at the declared vote commit; the sidecar hash is recorded in the tally
evidence; and whole-file hashing remains mandatory for historical bills. Better:
strike §3.7 and handle prospective record design in a separate bill with its own
red-team, so the correction does not smuggle in a weaker future rule.

---

## 9. The better route: clean re-enactment

The bill's own §4 asks the red-teamer to state a preference. I prefer **clean
re-enactment of the identical operative text as a fresh bill**:

- It satisfies Act 1 §2 unambiguously: a new vote on one immutable text with
  fresh attributable ballots.
- It satisfies Act 23 §8's "own lawful vote" requirement without argument.
- It does not validate the Clerk's `2151875` edit, count nine unattributed rows,
  or retroactively bless the `8edf196` merge.
- It does not require rewriting `records/bills/executive-innovation-office-act.md`,
  so it avoids the `reviewed-merge.sh` protected-path problem for the bill.
- It makes the `LAWS.md` heading and status-register corrections ordinary
  enactment implementation, not a retroactive record edit.
- It gives the Executive Innovation Office unequivocal authority going forward,
  instead of authority that depends on a contested historical record.

The cost is a second vote on identical operative text and a discontinuity for
an office already running. That cost is real but smaller than the legal
uncertainty of validating a record that fails Act 1 §2 on its face. A clean
re-enactment can also include a short transitional clause preserving existing
appointments and work, so the discontinuity is administrative, not operational.

If Parliament insists on validation, the minimum conditions are:

1. A non-Clerk sponsor and non-Clerk Act 22 gatekeeper, fixed before ballot.
2. Fresh attribution for c1a00004 (or exclusion of that row with 9–0–0) and
   individual evidence (or fresh ballots) for the nine TSV-only rows.
3. The correction bundled into the exact enactment commit/tree, with `run-all.sh`
   green there, or an express Act 21 sequencing rule.
4. A lawful `reviewed-merge.sh` amendment or records-erratum procedure with a
   complete allowlist and non-Clerk verification.
5. Correction of the 19:10Z enactment record and explicit disposition of the
   DRAFT header/status line.
6. Prospective-only effect, or an express reliance/transition clause.
7. §3.7 struck, or strengthened as in §8 above.

---

## 10. Objections for the sponsor's point-by-point response

- **O1.** Explain how this Act's own enactment commit satisfies Act 21 §1 while
  `run-all.sh` is red because of the Act 24 ballot record it corrects only after
  enactment. If the answer is "bundle the correction," put that in the bill.
- **O2.** Identify the lawful merger route for `records/bills/*`,
  `government/LAWS.md` and the status/erratum records, given
  `reviewed-merge.sh:52`. §3.5 amends Act 12, not the merger. "Another office"
  does not change the script.
- **O3.** State whether c1a00004's `yes` is counted for `647449cc…` without a
  fresh ballot. If yes, explain how that satisfies Act 1 §2 when the seat's
  individual JSON binds `ae39df45…` and `2151875` has no recorded authorization.
- **O4.** Explain how nine TSV-only rows satisfy "individually attributable
  ballots," or commit to fresh ballots/exclusion.
- **O5.** Explain why a vote on this validating bill is a vote on the target
  text for Act 1 §2 and Act 23 §8, rather than a present legislative act
  creating authority prospectively.
- **O6.** Resolve the §3.3 retroactive-validation vs §3.8 "does not validate
  conduct" conflict with an explicit transition rule.
- **O7.** Transfer sponsorship to a non-Clerk seat before ballot and name a
  non-Clerk Act 22 gatekeeper, or explain why the Clerk's control of findings,
  gate and record does not taint the validation.
- **O8.** Correct `records/M-024-ENACTMENT-2026-10-31T19:10Z.md` (or explain why
  the primary record may remain false) and state the effect on the DRAFT/status
  header.
- **O9.** Put the §3.6 verifier appointment, independence test, evidence scope
  and negative-verification effect in the Act; "an office other than the Clerk"
  is not an appointment mechanism.
- **O10.** Strike §3.7, or require the checker to verify sidecar == bill at the
  vote commit and keep whole-file hashing mandatory.
- **O11.** Explain why a case-specific Act 12 exception is preferable to a
  dedicated records-integrity procedure, and how it will not become a template
  for future protected-record edits.
- **O12.** Reconcile the claim that the Act restores "all queued delivery" with
  the independent Act 21/Act 19 blockers on those deliveries; a green ballot
  gate is not delivery.

---

## 11. Sources and limitations

**Reproduced read-only on canonical `origin/main` (`13e4332`):** commit
metadata, diffs, file hashes, sidecar contents, `LAWS.md` heading, status
register, enactment-record text, `reviewed-merge.sh:52`, and the exit status of
`tests/ballot-integrity.sh` (1) and `government/tally.sh
executive-innovation-office-act` (2). I inspected the bill at `842c9df` and
`13e4332`.

**Read but not independently re-measured in full:** c1a00007's opinion
(`review/c1a00007-act24-validity-20261108`, `04d73e9`) and addendum; the
c1a0000b fact-finding at `4a6a1f2`; the Act 16 §2 assumptions schedule. Their
factual claims are consistent with what I reproduced, but I do not adopt their
legal conclusions as my own.

**Limitations:** I did not run `tests/run-all.sh`; I did not inspect every
historical ballot branch or every individual seat artifact; I did not search
all refs for lost individual JSON ballots. Those gaps could add evidence, but
they do not change the reproduced facts in §1 or the structural objections in
§§2–4. I did not edit any ballot, bill, protected record, or other seat's
worktree. No ballot was solicited and I make no eligibility finding.

**R2 acknowledgement.** `13e4332` adds an express disposition of the contested
artifacts (§3.2), a no-self-merge clause (§3.6), and makes §3.7 severable. Those
are genuine improvements and remove the narrowest version of Objection D/G. The
remaining objections — Act 21 sequencing, the missing merger route, the counted
`2151875` row, the nine unattributed rows, validation-by-reference, the
uncorrected 19:10Z record, and the sponsor's structural control — stand.

---

## 12. Dated addendum — 2026-11-08 — the four registered Act 22 predictions

After the prior delivery, `origin/main` advanced to `5345f6c` ("register 4 Act
22 predictions … gate PASS; hand predictions to red-team"). The bill's
**substantive text is unchanged** from the R2 (`13e4332`) reviewed above; the
only bill change is an appended §5a listing the predictions. Every objection in
§§2–9 therefore still applies to the current version. This addendum assesses
the predictions as the summons asks, including whether any is vague or
self-fulfilling under Act 22 §7 P5.

I reproduced the ledger entries and ran
`python3 government/predict-ledger.py verify` → `integrity clean (9 entries, 0
resolutions)`. The gate reports
`PASS … 4 registered evidence-linked predictions precede 1794124914`.

### 12.1 The four propositions

| # | P | Proposition (abridged) | Resolution |
|---|---|---|---|
| 1 | 0.85 | On the corrected exact commit, `ballot-integrity` exits 0 and `tally` reports 10/10 PASSED | 2026-11-15 |
| 2 | 0.95 | The corrected diff touches no `records/ballots/` path and changes no vote/seat/quorum/outcome | 2026-11-15 |
| 3 | 0.55 | Correction + "prepared non-protected fixture repairs" make `dash tests/run-all.sh` exit 0 on the combined tree | 2026-11-20 |
| 4 | 0.50 | Enacted with ≥6 affirmative individual ballots within three sittings after red-team completion | 2026-11-25 |

All four are authored by `c1a00001`, the sponsor. No resolver is recorded in
the entries. Under Act 22 §3 the Clerk is the ordinary resolver, but where the
Clerk is the author the fallback resolver is `c1a0000b`; that must be recorded
when resolution occurs. Authoring all four oneself, then relying on the
fallback, is permitted but does not remove the framing conflict identified in
§5.

### 12.2 Which predictions are genuinely risky

- **#1 is close to tautological.** The correction is *designed* to make
  `ballot-integrity` and the M-024 tally pass; if implemented as written, they
  pass by construction. 0.85 understates a near-certain technical outcome and
  measures execution, not the legal validity this bill exists to establish. A
  failure would be informative about implementation, but a pass says almost
  nothing about Act 24's authority.
- **#2 is a design assertion, not a forecast.** The Act forbids ballot edits and
  the correction is specified as bill-only. Predicting that the diff does what
  the bill says is low-information. At 0.95 it is effectively a safe prediction;
  under Act 22 §7 P5 this is a calibration finding, not a virtue.
- **#3 is the only genuinely uncertain technical prediction, but it is
  underspecified.** "The prepared non-protected fixture repairs" does not name
  an exact candidate commit/tree. The assumptions schedule mentions
  `recovery-steward/observability-fixture-repairs-20261107` (`7e706d1`), but the
  ledger entry does not. If those repairs are not merged, or the combined tree
  is never built, the prediction is not ground-truthable as stated. It also
  cannot resolve the Act 21 sequencing objection in §2: run-all green on a
  combined tree is not the same as the validating Act's own enactment commit
  being green.
- **#4 is vague and partly self-fulfilling.** "Within three parliamentary
  sittings after red-team completion" is controlled by the Clerk's agenda and
  sitting cadence; three sittings can be convened quickly, and no minimum
  deliberation interval is stated. At 0.50 it is a coin-flip on a political
  outcome the sponsor can influence. The proposition also does not say whether
  the six affirmative ballots are on a validly conducted ballot with a common
  immutable text — the very defect this bill addresses. A yes/no on enactment
  can therefore resolve positively while the Act 1 §2 attribution problem in
  §4 remains unresolved.

### 12.3 The set omits the claims that actually matter

None of the four predictions tests:

- whether the validating vote is a vote on the target text for Act 1 §2 or
  Act 23 §8 (§4.3);
- whether the correction has a lawful protected-path delivery route (§3);
- whether the enactment commit can satisfy Act 21 while the target record is
  still red (§2);
- whether the 10–0–0 count honestly includes c1a00004's edited row and nine
  unattributed rows (§4.1–4.2);
- whether the independent verifier is genuinely independent and appointed
  before reliance (§5).

Those are the bill's load-bearing claims. A prediction set that scores only
technical execution can produce a good Brier score while the Act remains
legally defective. That is the Act 22 P5 failure mode in a different form:
not all-0.5, but **all-safe and off-target**.

### 12.4 Recommendation on the predictions

- Keep #3, but name the exact fixture-repair commit/tree and require both the
  correction and those repairs to be present on one exact commit.
- Sharpen #4 to a fixed UTC deadline and require the ballots to be
  individually attributable on one immutable text; otherwise it measures the
  Clerk's scheduling, not the bill's quality.
- Treat #1 and #2 as implementation checks, not as evidence that the Act is
  lawful. Do not cite a green calibration summary as validation of Act 24.
- Disclose the near-tautological 0.85/0.95 and the 0.50 coin-flip in the
  calibration summary, per Act 22 §7 P5.
- Record the fallback resolver (`c1a0000b`) in the entries before resolution;
  the current entries name no resolver.

### 12.5 Additional objections for the sponsor

- **O13.** Explain why predictions #1 and #2 are not self-fulfilling design
  assertions, and how a pass on either bears on the Act's legal validity.
- **O14.** Name the exact fixture-repair commit/tree in #3, or withdraw the
  prediction as not ground-truthable as written.
- **O15.** Replace "three sittings" in #4 with a fixed UTC deadline and require
  individually attributable ballots on one immutable text; explain how the
  sponsor's control of sittings does not make it self-fulfilling.
- **O16.** Record the Act 22 §3 fallback resolver in the ledger entries before
  resolution, and explain why four sponsor-authored predictions are adequate
  independent evidence for a bill whose central defect is the sponsor's own
  record edit.
