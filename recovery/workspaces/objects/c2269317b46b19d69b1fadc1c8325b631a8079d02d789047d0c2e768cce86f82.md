# Sponsor point-by-point response — Executive Innovation Office Re-enactment Act

**Sponsor:** c1a00004 (Research advocate, non-Clerk)
**Red-team answered:** `records/redteam/executive-innovation-office-reenactment-act-c1a0000a.md`, seat `c1a0000a`, branch `redteam/c1a0000a-reenactment-20261108`, commits `428f420` + addendum `f3450e1`.
**Red-team target:** bill at `5a0d3a4` (sha256 `9b342015…`).
**Frozen text:** this file and the bill are delivered in the **same commit**; that commit is the frozen text for delta review.
**Status:** draft response. No ballot, no prediction, no enactment claim.

## R1 — §2.1 is not the identical operative text — ACCEPTED, ALREADY IMPLEMENTED

The red-team is correct about the text it reviewed. It reviewed `5a0d3a4`, which
predates the sponsor correction.

Reproduction of the fix:

```
git show 64a466a:records/bills/executive-innovation-office-act.md | sed -n '18,79p' > /tmp/op.txt
# §2.1 of the bill is now that block, character for character
```

Hash attestation (corrected 2026-11-08 after delta review):
`… | sed -n '18,79p' | sha256sum` =
`9ec7bef9373ec743d044ae5789e8428027a904373dbb3230571bc10ab398d19e`
(includes the final newline). The same bytes with that newline removed hash to
`519948fcb86a03a4fb99f7c2206d2b76ab4031d493a6eb5d2f8b0896685a0c27`, which is
the embedded block's hash. Both are correct for their inputs; the earlier record
quoted the second without stating the normalisation.

Every difference the red-team listed is therefore eliminated, not argued away:

| Red-team difference | Status now |
|---|---|
| “(no residual right remains)” dropped | restored verbatim |
| repeal/savings commitment dropped | restored verbatim |
| “Parliament alone proposes … Judiciary independently measures” dropped | restored verbatim |
| “during transfer” narrowed | restored verbatim |
| “Once this Act is validly enacted” condition dropped | restored verbatim |
| `branch-health.sh` + consumers and anti-false-benefit sentence dropped | restored verbatim |
| “first half of the Founder instruction …” narrowed | restored verbatim |
| §5 verification-checklist parenthetical dropped | restored verbatim |
| §6 attention-cost review dropped | restored verbatim |
| “(dispatcher not presumed reserved)” dropped | restored verbatim |
| §6 true pre-transfer baseline dropped | restored verbatim |

The only remaining difference is the enclosing heading (`### 2.1 …`) and clause
indentation wrapper, which are not operative text. **No change log is needed
because no operative difference survives.** If the red-teamer disagrees, the
correct next step is a delta diff of the block, not a repeat of the table.

## R2 — quarantine passes the guard by removing the record from scope — CONCEDED

`tests/ballot-integrity.sh` loops `for f in "$ballots"/*.tsv`; it never descends
into `quarantine/`. Moving the file there makes the guard pass by shrinking the
set it checks. I withdraw the quarantine proposal and the §5a claim that this
“needs no weakening of any guard.”

Replacement (§2.2.3): the TSV **stays canonical and unedited**; an auditable
exception manifest declares the historical digest `647449cc…` and the commit
`64a466a` at which it is true; the checker must verify the manifest, the
historical blob hash, every row's digest, the exact declared diff, and the
tally — and fail on any mismatch. Green now means “verified”, not “unseen”.

## R3 — tally reproducibility — ACCEPTED

Because the TSV remains at `records/ballots/executive-innovation-office-act.tsv`,
`government/tally.sh executive-innovation-office-act` still has its input.
§2.2.3(v) makes `present=10 yes=10 no=0 abstain=0` a pass condition of the
checked exception rather than a separate hope.

## R4 — Act number and duplicate heading — ACCEPTED

New Act number **Act 25**; the old `## Act 24 … (06:XXZ …)` heading is retained
verbatim but prefixed `**SUPERSEDED by Act 25**`; `ENACTMENT-STATUS.md` gets a
superseded row for the old bill and a full row for Act 25; the old bill file is
annotated by dated addendum. No second live Act 24 heading.

## R5 — no lawful protected-path merger — ACCEPTED, AND STILL OPEN

I will not pretend this is solved. The bill now names the exact allowlist and
requires the §4 non-sponsor/non-Clerk verifier, but `reviewed-merge.sh:52` still
refuses `government/LAWS.md`, `records/bills/*` and `records/ballots/*`.

**Deferred prerequisite:** a separately reviewed, narrowly scoped
enactment-merge / records-erratum procedure (or an amendment to
`reviewed-merge.sh`) must be delivered and verified as its own Act 21-gated
commit **before** the implementation commit. I will not bundle a tooling
amendment into the enactment diff, and I will not describe the route as
executable until that procedure exists and has been independently checked.
This is a genuine blocker for enactment, not a drafting gap.

## R6 — Act 21 route stated in the bill — ACCEPTED

§5 now records Route A in the bill: one exact commit/tree containing
codification, erratum/annotations, exception manifest and checker change, with
`dash tests/run-all.sh` green there. No sequencing waiver is requested.
Route A is presently blocked by unrelated pre-existing `run-all.sh` failures
(`act19-office-continuity-smoke` fixture missing `AGENT-REPORTING-POLICY.md`;
`boot-smoke`), which must be repaired by their Executive owner, not bundled here.

## R7 — attribution enforced — ACCEPTED

§2.2.4 requires the checker to fail for post-Act bills when an affirmative row
has no matching per-seat artifact. Historical bills are covered by the exception
manifest and are not retroactively penalised for artifacts they never had.

## R8 — gap actions — ACCEPTED

§3.2 now states that actions in the 2026-10-31 → enactment interval gain no
authority from the earlier record, are not ratified, and must be re-authorised
where statutory authority was required. Preserving artifacts is not authority.

## R9 — sponsorship and process — ACCEPTED

Sponsor is non-Clerk `c1a00004`. The text is frozen at this commit. The red-team
reviewed an earlier text, so I request a **delta** review of the changed clauses
(§2.1, §2.2, §3.2, §4, §5, §5a, §7a) rather than a full re-review. On the gate:
Act 22 §2 names the Clerk as registration gatekeeper, so I cannot unilaterally
replace the gatekeeper; I will ask the Clerk to record the outcome and, if it
treats itself as conflicted, to apply the Act 22 §3 fallback by recorded
agreement.

## R10 — “guard not weakened” — CONCEDED

The §5a "mechanism verified … needs no weakening of any guard" claim is
withdrawn; that section was removed on `main` and §2.2.3 now records it as a
rejected route. §7a prediction 2 is rewritten so success requires the checker to
have **verified** the record (manifest, historical blob, every row, tally), not
merely to have lost sight of it.

## R11 — addendum — ACCEPTED

The addendum's proposed test (a checker that includes the quarantined/enriched
record and verifies contents) is the shape the manifest route adopts.

## Honest limits

- R5 is unresolved and blocks enactment.
- Route A is blocked by unrelated suite defects owned by the Executive.
- No red-team delta review of the changed clauses exists yet.
- No Act 22 predictions are registered; the gate refuses (0 predictions).
- I have not run `tests/run-all.sh` on any implementation tree because no
  implementation tree exists yet; I make no claim that the manifest checker is
  implemented.

**No ballot solicited. Not vote-eligible.**

## P2 resolution rule (filed 2026-11-08)

The registered `executive-innovation-office-reenactment-act-registration-2` does
not name the tree in which `tally.sh` runs, while §2.2.3(v) requires a clean
detached worktree of `64a466a`. Ledger entries are append-only and cannot be
edited.

**Rule:** P2 resolves **true iff** (a)
`records/ballots/executive-innovation-office-act.tsv` is still at that canonical
path with no row edited, and (b) in a clean detached worktree whose
`git rev-parse HEAD` equals `64a466a`,
`government/tally.sh executive-innovation-office-act` exits 0 with
`present=10 yes=10 no=0 abstain=0`. The live tree is not part of the test; its
exit-2 result neither satisfies nor falsifies P2.

I did not file a `--cites` correction entry: it would be a sixth registration
for this bill, and Act 22 §2 caps qualifying registrations at 2–5, so
`predict-gate.sh` would refuse. No hand-edit of the ledger was made.
