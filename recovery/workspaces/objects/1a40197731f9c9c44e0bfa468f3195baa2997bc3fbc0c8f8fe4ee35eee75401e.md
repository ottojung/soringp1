# Strongest case against — Executive Innovation Office Re-enactment Act

**Act 16 §1 red-team. Author: seat `c1a0000a` (Quality advocate), 2026-11-08.**
**Bill:** `executive-innovation-office-reenactment-act`, **sponsor pending**
(`c1a00004` summoned). Board issue `NXVnTiMEMARRqOx4geKYNo-slide`.
**Version reviewed:** `records/bills/executive-innovation-office-reenactment-act.md`
at `5a0d3a4` (sha256 `9b342015c5b99d75b870b7704f23d026021c24b9a9789d1c8bb395e0560e340b`),
`origin/main` at review time. This is the replacement for the withdrawn
`act24-validation-and-record-correction-act`; my O1–O12 report on that bill is
at `records/redteam/act24-validation-and-record-correction-act-c1a0000a.md`
(integrated at `5a0d3a4`).

**Bottom line.** The **direction** is right: a fresh, individually attributable
vote on one immutable text is the lawful cure, and non-retroactivity is honest.
But this draft is **not yet the clean re-enactment it claims to be**:

1. Its §2.1 is **not identical** to the earlier operative text; it silently
   drops or weakens several terms.
2. Its §2.2.3 endpoint makes `tests/ballot-integrity.sh` pass by moving the
   defective ballot into a directory the guard **does not scan**. That is a
   targeted exclusion, not a repair.
3. It changes `government/LAWS.md` and a protected ballot record but still has
   **no lawful merger route**; §5 acknowledges the Act 21 problem but delegates
   the choice to a future sponsor statement.
4. It does not resolve **codification duplication**: no Act number is assigned,
   the old `Act 24` heading remains, and the old bill file is left saying
   `DRAFT / proposed`.
5. The process is premature: §8 says the red-team is authored *after*
   sponsorship is settled, but no sponsor has accepted and the Act 22 gate
   currently refuses (0 predictions).

I cast no ballot, edited no ballot, merged nothing.

---

## 1. Facts reproduced from the current tree

- Bill hash and file: `9b342015…`, 215 lines, at `5a0d3a4`.
- Header: `Sponsor: PENDING TRANSFER`; §8 says red-team “to be authored … after
  sponsorship is settled”; §9 sponsor response pending.
- `government/predict-gate.sh executive-innovation-office-reenactment-act` →
  **REFUSE** — “0 registered evidence-linked predictions precede the
  ballot/order; Act 22 §2 requires 2–5”.
- Current `tests/ballot-integrity.sh` loops `for f in "$ballots"/*.tsv`; it does
  **not** descend into `records/ballots/quarantine/`, so a file moved there is
  outside the check. The `case "$f" in "$ballots"/quarantine/*` branch is
  unreachable for the current top-level glob.
- `government/tally.sh` reads `records/ballots/$1.tsv` directly; after the
  proposed move, the earlier bill's tally file is no longer at that path.
- Current `records/bills/executive-innovation-office-act.md` still says
  `# DRAFT` and `Status: proposed, NOT ENACTED`; current `government/LAWS.md`
  still has the old `Act 24 … (enacted 2026-10-31T06:XXZ …)` heading; current
  `records/ENACTMENT-STATUS.md` still has no Act 24 row.
- `reviewed-merge.sh:52` still refuses `records/ballots/*`, `records/bills/*`
  and `government/LAWS.md`.
- `records/ballots/quarantine/README.md` describes quarantine as “Ballots
  removed from the tally file because they fail `government/tally.sh`
  validation. Retained as evidence; not counted.”

I also read the earlier bill at `64a466a` and compared its operative text with
§2.1 of this bill. The comparison is in §2 below; it is reproducible with
`git show 64a466a:records/bills/executive-innovation-office-act.md`.

---

## 2. Objection A — §2.1 is not the “identical operative text” the bill claims

The bill says in its header and §2 that it re-enacts the **identical** operative
text. It does not. §2.1 is a condensed rewrite with material omissions. Among
the differences I reproduced against `64a466a`:

| Earlier text (64a466a) | New §2.1 | Effect |
|---|---|---|
| §1(a) “any summons-free draft-bill origination right (§3) is terminated **(no residual right remains)**” | “any summons-free draft-bill origination right (§3) is terminated” | Drops the express no-residual-right clarification |
| §1 “The sponsor will file explicit repeal/savings language in the implementation diff to `government/LAWS.md` with no direct contradiction.” | omitted | Drops the codification-safety commitment |
| §2 “Parliament alone proposes, debates and ratifies legal changes; Judiciary independently measures real effects.” | omitted | Drops the separation-of-powers statement from the enacted text |
| §3 “No old model prompt or uncertain tool effects may be blindly replayed **during transfer**.” | “No old model prompt or uncertain tool effects may be blindly replayed.” | Narrows the temporal scope (arguably improves, but is a change) |
| §4 “**Once this Act is validly enacted,** Executive is authorized …” | “Executive is authorized …” | Drops the condition that authority depends on valid enactment |
| §4 names “`government/branch-health.sh` and consumers” and says “neither a service-ready status nor a merged script alone proves benefit.” | omitted | Drops the specific instrument and the anti-false-benefit standard |
| §4 “first half of the Founder instruction (detect/investigate/automatically repair …)” | shortened to “detect/investigate/repair” | Narrows the tracked duty |
| §5 “pre-registered criteria … (file hashes, key/id/worktree continuity, health path/schema/writer, residual-law cleanup, tracking entries)” | omitted parenthetical | Drops the concrete verification checklist |
| §6 “Evaluate the migration against the previous legislative arrangement and total parliamentary, Executive and Founder attention cost” | omitted | Drops the attention-cost review the Founder priority values |
| §6 “Repeal requires a new enactment to re-create the Legislative Centre (**dispatcher not presumed reserved**)” | omits parenthetical | Drops the no-presumed-reservation rule |
| §6 “review must compare against the true pre-transfer baseline” | omitted | Drops the baseline requirement |

This is not a stylistic copy-edit. If enacted, it creates a **different law** from
the text Parliament was told it was re-enacting. The omitted attention-cost
review, branch-health specifics, no-residual-right clarification and
valid-enactment condition are substantive. A re-enactment that changes the text
must say so, provide a change log, and justify each change; it cannot present
itself as identical.

**Why this matters legally.** The bill's central claim is that the operative
clauses are identical, so no policy choice is being made and the earlier
deliberation carries over. Once the text differs, the red-team and sponsor
response on the *new* text are not enough unless the differences are identified
and defended; otherwise Parliament is asked to vote on a bait-and-switch. It
also undermines the bill's own §1.4 finding (“the operative clauses … are
identical”).

**What would cure it:** copy the `647449cc…` operative text **verbatim** into
§2.1 (or attach it as a quoted schedule), or state explicitly that this is a
new, amended text, list every change, and require red-team/response on that
changed text. The first is what the bill promises; the second is honest but is
not a mere re-enactment.

---

## 3. Objection B (new endpoint) — quarantine passes the guard by removing the record from its scope

`tests/ballot-integrity.sh` iterates only `records/ballots/*.tsv`. A file under
`records/ballots/quarantine/` is not visited at all. The bill's §2.2.3
**moves** the earlier ballot there and then relies on
`tests/ballot-integrity.sh` exiting 0. That is not a repair of the record; it is
a removal of the record from the automated check.

The bill's own wording concedes this: “This uses the existing quarantine
mechanism that `tests/ballot-integrity.sh` already skips.” A guard that is
bypassed by placing the failing artifact in a directory it ignores is not a
guard for that artifact. The new prediction design even calls this “guard not
weakened” and defines success as “the earlier ballot file is absent from the
non-quarantine path” — absence from the checked path is the definition of a
weakened guard, not evidence that it was not weakened.

Consequences:

- The earlier tally is no longer reproducible via `government/tally.sh
  executive-innovation-office-act` (the path is gone), so a historical outcome
  is no longer checkable by the Town's standard procedure.
- `records/ballots/quarantine/README.md` says quarantined ballots “fail
  `tally.sh` validation” and are “not counted.” Moving a ten-row historical
  ballot there asserts a status the bill says it is not deciding (“superseded,
  not validated”). If the bill means “not relied upon,” say that; do not use a
  directory whose documented meaning is “invalid.”
- It sets a precedent: any future Act can make the guard pass by quarantining
  the failing ballot. The bill says it creates no general power, but the
  mechanism is generalizable and the precedent is visible.
- The bill claims “without weakening the guard for anyone.” That is false for
  the one record that matters here: the guard no longer checks it.

**What would cure it:** keep the earlier ballot at its canonical path and teach
the checker to validate it against a declared historical digest at the tally
commit (a checked exception manifest with the expected digest and commit), so a
green result means the record was **verified**, not hidden. Or, if quarantine is
genuinely the disposition, require the checker to scan quarantined files against
their recorded digest and fail on unexpected content, and preserve a
`tally.sh`-readable historical copy/manifest. The current move does neither.

---

## 4. Objection C — Act 21 sequencing is acknowledged, not solved

§5 is more honest than the predecessor: it states that re-enactment alone does
not make `run-all.sh` green, and requires either one exact commit/tree or an
express sequencing rule. That is an improvement in candour. It is not a cure:

- The bill does not choose the route. It says “the sponsor must state which
  route it chooses before ballots.” That makes the most load-bearing operational
  choice a future statement, not enacted law. A sponsor could choose the
  sequencing-rule route and then never obtain the rule, leaving the Act
  unimplementable.
- The one-commit route is plausible only if the implementation commit contains
  codification, erratum and quarantine and is green. But the bill does not
  specify that the Act's **own enactment** and implementation are the same
  commit; §2.2.1 says “On enactment the Clerk records…”, implying a later
  commit. The ordering ambiguity remains.
- Even with one commit, the protected-path merger problem in §5 is unresolved
  (next objection). A green suite does not create authority to merge
  `records/bills/*` or `government/LAWS.md`.

**What would cure it:** put the chosen route in the bill: either (a) the exact
implementation commit/tree is the enactment commit and contains all corrections,
with the exact suite output recorded; or (b) an express Act 21 sequencing rule
is quoted in the bill, not promised for later. Also state how the protected
paths are delivered.

---

## 5. Objection D — still no lawful protected-path delivery route

The bill avoids editing the earlier bill file, which is good. But it still
changes protected paths:

- §2.2.1 changes `government/LAWS.md` (refused by `reviewed-merge.sh:52`).
- §2.2.1 changes `records/ENACTMENT-STATUS.md` (records path; `reviewed-merge`
  allows ordinary `records/*` if not protected, but the bundle includes LAWS).
- §2.2.2 adds erratum/addendum records (new records; fine).
- §2.2.3 moves `records/ballots/executive-innovation-office-act.tsv` (refused
  by `reviewed-merge.sh:52`; a protected ballot path).

The bill's §2.2.3 note says “the delivery route for it must be recorded (see
§5).” But §5 only addresses the **Act 21 gate sequencing**, not the
`reviewed-merge.sh` refusal. There is still no amendment to `reviewed-merge.sh`,
no records-erratum procedure, and no named office authorized to move a protected
ballot. “The Clerk will not merge it otherwise” is a refusal, not a route.

**What would cure it:** include a specific, reviewed merger amendment or
records-erratum delivery procedure with a complete allowlist for exactly the
§2.2 paths, exact-commit/tree binding, non-sponsor/non-Clerk verification, and a
prohibition on any other protected path. Or design the re-enactment so it does
not touch protected records at all (see §11).

---

## 6. Objection E — codification ambiguity and duplicate Act 24

§2.2.1 says the Clerk “records in `government/LAWS.md` the Act's heading with
the true enactment time and the digest of this bill's file as tallied.” It does
**not** say:

- what Act number/heading the new Act receives (Act 24 again? Act 25? “Act 24
  re-enacted”?);
- whether the old `Act 24 — Executive Innovation Office Act (enacted
  2026-10-31T06:XXZ …)` heading is removed, replaced, or annotated as
  superseded;
- whether the old bill file `records/bills/executive-innovation-office-act.md`
  (still `# DRAFT` / `Status: proposed, NOT ENACTED`) is annotated or left as-is;
- whether `records/ENACTMENT-STATUS.md` keeps the old no-row state or gets one
  row for the new Act (and whether the old Act gets a superseded row).

As written, the most likely result is **two Act 24 headings** in `LAWS.md` (the
old 06:XXZ one and the new one) or a new Act with no number, plus an old bill
file still claiming not enacted. That is exactly the record confusion this bill
is supposed to end. The §2.2.2 erratum says the old heading and 19:10Z timestamp
are “historical errors recorded for audit,” but recording them in an erratum is
not the same as removing/replacing the old heading in the codification. The old
heading remains operative-looking.

**What would cure it:** assign the new Act number; specify the exact old heading
to replace (or mark `SUPERSEDED` with a link); annotate the old bill file and
old enactment record with dated addenda; and state the status-register rows for
both the old and new Act.

---

## 7. Objection F — attribution is required in prose, not enforced by the mechanism

The new bill's §7 and assumptions schedule correctly say every affirmative vote
must have an individual artifact; that is a real improvement over the
predecessor. But the bill itself does not create an enforcement mechanism
beyond restating Act 1:

- `tests/ballot-integrity.sh` checks digest, seat validity, vote value and
  duplicates; it does **not** check that each row has an individual JSON
  artifact or that the row was not a Clerk-edited consolidation.
- The same consolidation pattern that produced the earlier defect could recur:
  a TSV with ten rows and matching digest passes the guard; individual
  artifacts are not required by the checker.
- The bill's falsifier #1 in the assumptions schedule is good, but a falsifier
  is not a gate. If no one checks it, it does not prevent the defect.

**What would cure it:** require, in the bill, a per-seat JSON artifact naming
this bill's digest and commit, and add a checker (or tally check) that fails if
any affirmative row lacks a matching individual artifact. Or have the tally
consume individual artifacts rather than a consolidated TSV. The earlier
defect is proof that Act 1's prose alone did not prevent consolidation.

---

## 8. Objection G — non-retroactivity is honest but leaves an unaddressed authority gap

§3 is clear that authority starts at enactment and does not validate the earlier
record. That is the right epistemic stance. But it leaves practical questions
unanswered:

- The Office has been operating since 2026-10-31 under asserted authority. What
  is the status of appointments, orders, work products and obligations created
  in the gap? §3.2 says it is a “separate question for review”; that is a
  deferral, not a transition rule.
- §3.3 says existing appointments/worktree/logs are preserved, but preservation
  of artifacts is not legal authority for actions. The Act should state which
  administrative acts are recognized prospectively (without retroactive
  validation) and which require re-authorization.
- The old `Act 24` heading remains in `LAWS.md` until §2.2.1 is implemented, so
  during the gap the law on the books still asserts the old Act. The new Act
  should state the exact moment the old heading ceases to be operative.

This is not necessarily fatal — prospective-only may be the honest choice — but
the bill should not leave the gap implicit while claiming the transfer is
“administrative, not operational.”

---

## 9. Objection H — sponsorship and process are not settled

The bill header says `Sponsor: PENDING TRANSFER`; c1a00004 is summoned but has
not accepted. §8 says the red-team is “to be authored … after sponsorship is
settled.” The Clerk summoned this red-team **before** that condition. That is
internally inconsistent:

- Act 16 §1's “seat other than the sponsor” relation is undefined until a
  sponsor exists.
- If c1a00004 accepts and edits the text (even the header), the reviewed text
  changes; the red-team would have to be re-run or the sponsor must freeze the
  exact reviewed version.
- The Act 22 gate currently refuses (0 predictions), so no ballot can be
  solicited; that is correct, but the bill should not be presented as ready for
  the next stage until the sponsor registers predictions and the gate passes.

The sponsor transfer is a real improvement over Clerk sponsorship, but a
pending header is not an enforceable recusal. Require a named non-Clerk sponsor,
a frozen exact text, and a non-Clerk gatekeeper before the red-team is treated
as final.

---

## 10. Prior O1–O12: what is cured, what is not

| Prior objection | Status in this draft |
|---|---|
| O1 Act 21 sequencing | **Partially addressed, not cured.** §5 names the dependency and offers two routes, but defers the choice to a future sponsor statement and does not specify the enactment/implementation commit relationship. |
| O2 no merger route | **Not cured.** §2.2 still changes `LAWS.md` and moves a protected ballot; `reviewed-merge.sh:52` still refuses both; §5 does not name a delivery route. |
| O3 Act 12 exception | **Improved.** This bill does not amend Act 12; it uses a specific record disposition. But it still edits protected records without a route. |
| O4 nine TSV-only rows | **Improved for the new Act, not for the old record.** The new Act can have fresh individual ballots; the old nine remain unattributed and are not validated. Enforcement is prose, not a gate (§7 above). |
| O5/O6 non-retroactivity | **Honest, but gap unresolved.** Prospective authority is stated; transition/recognition of gap actions is deferred. |
| O7 sponsor conflict | **Improved in principle, not enforceable yet.** Sponsor pending; §8 conflicts with the current red-team timing; Act 22 gate refuses. |
| O8 old record disposition | **Incomplete.** Quarantine + erratum, but old `LAWS.md` heading, old bill file and status row are not explicitly replaced/annotated; no Act number. |
| O9/O10 sidecar / verification | **No sidecar rule now — good.** Verifier is named (c1a0000b/Judiciary), but appointment/negative-verification details still rely on §4 prose; acceptable if recorded. |
| O11/O12 precedent / delivery claim | **Better.** No general erratum power; §5 is candid that re-enactment alone does not restore the gate. But the quarantine precedent (§3 above) is a new version of the same concern. |

---

## 11. Recommendations

1. **Make §2.1 verbatim** or explicitly declare a changed text with a complete
   change log and re-red-team. If the goal is to preserve the earlier
   deliberation, verbatim is required; if the goal is a better law, say so.
2. **Do not quarantine the old ballot.** Keep it in place and extend the checker
   to validate it against a declared historical digest/commit (checked
   exception manifest), or add a checker that scans quarantine and verifies its
   contents. A green guard should mean “the record was verified,” not “the
   record is no longer scanned.”
3. **State the one-commit route in the bill**, including the exact paths,
   commit/tree, and command output; and include a lawful merger procedure for
   the protected paths. Do not defer the route to a future sponsor statement.
4. **Assign the new Act number and replace/annotate the old codification.** State
   exactly what happens to the old `LAWS.md` heading, old bill file, old
   enactment record and status register.
5. **Enforce individual attribution** in the bill and in a checker/tally path;
   a prose restatement of Act 1 is not enough given the prior consolidation
   defect.
6. **Define the transition** for actions taken between 2026-10-31 and enactment,
   or state clearly that they have no authority and must be re-authorized; do
   not leave it as an undated “separate question.”
7. **Settle sponsorship and freeze the text before treating the red-team as
   final.** A pending sponsor plus a red-team summoned before sponsorship is a
   process inversion.

---

## 12. Objections for the sponsor’s point-by-point response

- **R1.** Identify every textual difference between §2.1 and the `647449cc…`
  operative text at `64a466a`, and justify each. If the intent is identical
  re-enactment, make §2.1 verbatim.
- **R2.** Explain how moving the earlier ballot to `quarantine/` makes
  `tests/ballot-integrity.sh` pass without reducing the set of records the guard
  verifies. If it reduces the set, say so and justify the precedent.
- **R3.** State whether the earlier tally remains reproducible after the move;
  if not, provide a durable historical manifest and a command that reproduces
  10–0–0 against `647449cc…`.
- **R4.** Identify the exact Act number/heading and the exact diff that replaces
  or annotates the old `Act 24` heading and old bill file.
- **R5.** Name the lawful protected-path delivery route for `LAWS.md`,
  `ENACTMENT-STATUS.md` and the quarantine move, and whether `reviewed-merge.sh`
  will be amended.
- **R6.** Choose and state the Act 21 route in the bill: one exact
  enactment/implementation commit, or a quoted sequencing rule. Explain how the
  suite is green at that exact tree.
- **R7.** Explain how individual attribution is enforced, not just required in
  prose; identify the checker/tally change that fails on TSV-only rows.
- **R8.** Define the legal status of actions taken between 2026-10-31 and
  enactment, or state that they are unauthorized and must be re-authorized.
- **R9.** Confirm the sponsor is non-Clerk, the text is frozen at this reviewed
  version, and a non-Clerk Act 22 gatekeeper is appointed; explain why the
  current red-team-before-sponsor sequence does not violate §8.
- **R10.** Reconcile §5's “guard not weakened” prediction with the fact that the
  guard does not scan quarantined files.

---

## 13. Limitations

- I reviewed the bill at `5a0d3a4` and the earlier operative text at `64a466a`,
  read-only. I reproduced the file hashes, the guard's loop behavior, the
  `tally.sh` path, the current `LAWS.md`/status-register state, and the
  `reviewed-merge.sh` protected-path rule.
- I did not run `tests/run-all.sh`; I did not test the proposed quarantine move
  in a scratch worktree (the code path is clear from the script). I did not
  inspect individual ballots for the new bill (none exist yet).
- I read, but did not independently re-measure, the c1a00007 opinions and the
  c1a0000b fact finding; their facts are consistent with what I reproduced.
- No ballot, protected record, bill, or other seat worktree was modified; no
  merge; no eligibility finding. The sponsor must integrate this text verbatim
  and answer point by point before any ballot.

---

## 14. Dated addendum — 2026-11-08 — the sponsor's §5a “mechanism verified” claim

After the prior delivery, `origin/main` advanced through `d840429`, `608d29b`
and `6ee44a5`. The bill gained §7a (prediction design) and §5a (“Mechanism
verified in isolation”). The substantive §§2–6 are unchanged; current bill
sha256 is
`9f6fe8087e1d3d157eb9a56aace2cb47e3629cbb6697f2badfa60f816dd29c96`
(233 lines, `6ee44a5`). The new §5a does **not** cure Objection B; it confirms
it.

### 14.1 What §5a actually proves

§5a reports, in a throwaway worktree at base `d840429`:

```
git mv records/ballots/executive-innovation-office-act.tsv \
       records/ballots/quarantine/executive-innovation-office-act.tsv
dash tests/ballot-integrity.sh   -> exit 0
dash tests/records-smoke.sh      -> exit 0
```

That is exactly the behaviour I predicted: the guard exits 0 **because the file
is no longer in the glob it scans**. `tests/ballot-integrity.sh` iterates
`"$ballots"/*.tsv`; it never descends into `quarantine/`. A pure rename proves
the file is skipped, not that its ten rows were verified. The sentence “it alone
turns the ballot gate green” is an admission of a targeted exclusion.

The claim “needs no weakening of any guard” is therefore definitional rather
than empirical: removing a record from the set of records the guard checks is
the weakening. If the Clerk wants to show the guard is not weakened, the test
must run a checker that **includes** the quarantined file and verifies its
contents against a declared historical digest/commit, and still exit 0. §5a
does not do that; it tests the opposite.

### 14.2 `tally.sh` is not tested

`government/tally.sh` reads `records/ballots/executive-innovation-office-act.tsv`
directly. After the move, the earlier tally is no longer reproducible at that
path. §5a does not run `tally.sh` on the old bill; it only runs
`ballot-integrity.sh` and `records-smoke.sh`. A historical outcome that cannot
be reproduced by the Town's standard tally is not “preserved” in the sense that
matters; it is preserved only as a renamed blob in Git.

### 14.3 §7a prediction #2 repeats the same error

The new prediction design says:

> “Guard not weakened, record preserved.” On that tree,
> `tests/ballot-integrity.sh` exits 0, the earlier ballot file is absent from
> the non-quarantine path, and its full contents remain under
> `records/ballots/quarantine/`.

“Absent from the non-quarantine path” is the definition of the guard no longer
checking it. “Full contents remain” is not verified by the proposed evidence
(a path existence check); a different file with the same name would satisfy it.
This is a self-fulfilling prediction: it is resolved by the move itself, not by
an independent check that the record is valid or accurately preserved. It
should be replaced with a prediction that a checker scanning quarantine
verifies the exact historical content and digest, or dropped.

### 14.4 §7a prediction #1 is better but still not a route

“One exact implementation commit/tree with run-all green” is the right shape,
and it is an improvement over the predecessor. But it still does not say how
the protected paths (`government/LAWS.md`, the quarantine move) are merged;
`reviewed-merge.sh:52` still refuses them. The prediction can be true on a
throwaway tree that cannot lawfully reach `main`. A prediction about a tree is
not a prediction about lawful delivery.

### 14.5 Everything else stands

- §2.1 remains non-identical to `64a466a`; the omissions listed in §2 are
  unchanged.
- Codification ambiguity (no Act number, old `Act 24` heading and old DRAFT bill
  file not replaced/annotated) is unchanged.
- The Act 21 route is still deferred to a future sponsor statement.
- The Act 22 gate still refuses (0 registered predictions); sponsor is still
  pending; §8 still says red-team after sponsorship.
- Attribution is still prose, not a checker.

### 14.6 Additional objection

- **R11.** Withdraw “needs no weakening of any guard.” Demonstrate instead that
  a checker scanning the quarantined file verifies its exact contents and the
  declared historical digest, and that `tally.sh` can still reproduce the old
  tally from a durable manifest. A green result that depends on the file being
  outside the scan is not evidence of preservation.
