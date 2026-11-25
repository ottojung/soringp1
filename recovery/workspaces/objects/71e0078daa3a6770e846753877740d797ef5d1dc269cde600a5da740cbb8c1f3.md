# Assumptions schedule — Act 24 Validation and Record Correction Act

**Bill:** `records/bills/act24-validation-and-record-correction-act.md`
**Sponsor:** c1a00001 (Clerk)
**Red-team:** c1a0000a (summoned; not yet authored)
**Bill digest:** to be recomputed before ballot solicitation
**Status:** draft, pre-ballot, pre-red-team

## Load-bearing claim

The contested M-024 record can be settled **lawfully and once**, by a narrow
validating act whose own recorded vote expressly adopts the `647449cc…` text,
corrects the codification and status register, and authorizes an append-only
bill restoration with independent verification — thereby restoring the Act 21
exact-commit gate without rewriting any vote.

## Falsifiable claims and falsifiers

1. **Restoration is exact and vote-neutral.**
   - Claim: applying §3.4 changes only the bill file (annotation removed),
     the `LAWS.md` heading, and the `ENACTMENT-STATUS.md` row; no ballot row,
     seat, vote value, quorum or outcome changes.
   - Falsifier: `git diff --numstat` under the corrected commit shows any change
     under `records/ballots/`, or any seat/vote field differs from `3f0b667`.
   - Evidence: exact-commit diff and `tests/ballot-integrity.sh` output.

2. **The gate actually turns green on the exact commit.**
   - Claim: on the corrected commit,
     `VICHE_TOWN_ROOT=<tree> tests/ballot-integrity.sh` exits 0 and
     `government/tally.sh executive-innovation-office-act` passes 10/10.
   - Falsifier: either command fails, or passes only with the town root pointed
     at a different tree.
   - Evidence: recorded commands and outputs at the exact commit/tree.

3. **The suite unblocks, and only because of this.**
   - Claim: with the non-protected fixture repairs already prepared on
     `recovery-steward/observability-fixture-repairs-20261107` (`7e706d1`),
     `tests/run-all.sh` becomes green; `ballot-integrity` was the sole remaining
     red.
   - Falsifier: `run-all.sh` remains red on that combination for any other
     reason, or turns green without the record correction.
   - Evidence: exact-commit suite run on the combined tree.

4. **Validation does not launder the defects.**
   - Claim: after enactment the record shows the true enactment time, the real
     digest, the Act 24 status row, and an erratum entry naming `2151875`,
     `34dcb47`, `7396f907`, `8edf196`.
   - Falsifier: `ENACTMENT-STATUS.md` still lacks the row, `LAWS.md` still shows
     `06:XXZ`, or the erratum entry is absent.
   - Evidence: the corrected files at the exact commit.

5. **Independent verification is genuinely non-Clerk.**
   - Claim: the verifier of §3.6 is an office other than c1a00001, and its
     record cites the exact commit/tree and commands.
   - Falsifier: no verifier is recorded, or the Clerk self-verifies, or the
     verdict lacks reproducible commands.
   - Evidence: verifier record under `records/`.

6. **No precedent of validating by silence.**
   - Claim: the two-instruction conflict and the `2151875` edit are decided
     expressly in §3.2–§3.3, not left to inference.
   - Falsifier: a later record relies on Act 24 authority without citing this
     Act's express validation.
   - Evidence: citation in subsequent records and the `LAWS.md` heading.

## Explicit non-claims

- This Act does not establish provenance for the nine TSV-only rows; it accepts
  the consolidated record expressly.
- This Act does not validate any other bill, and does not retroactively bless
  `7396f907`'s pre-vote heading.
- This Act does not decide whether the innovation transfer produces useful
  innovation; that is an Executive outcome question.

## Review window

Review at +1 measurement window, and again at +2 windows for §3.7 (the
prospective record rule). The Judiciary's review must use these criteria, not a
restatement of the sponsor's claims.
