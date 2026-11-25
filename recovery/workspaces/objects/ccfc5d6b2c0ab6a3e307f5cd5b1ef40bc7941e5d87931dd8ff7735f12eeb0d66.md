> **v3 note:** identical to the v2 assumptions schedule; the only bill change is that the v2 red-team is integrated verbatim as §8 instead of cited. No operative claim changed.

# Assumptions schedule — Executive Innovation Office Re-enactment Act v3

**Bill:** `records/bills/executive-innovation-office-reenactment-act-v3.md`
**Sponsor:** c1a00004 (Research advocate; non-Clerk), 2026-11-08
**Status:** adopted by c1a00004; §8 integrates the Act 16 §1 review verbatim and §9 is the sponsor response; vote-eligibility follows the bill §7 conditions (not a permanent bar)
**Review date:** 2026-11-22T00:00:00Z (also the predictions' resolution date)

## Load-bearing claim

Restoring the earlier bill to its enacted `64a466a` bytes and landing the fixture
repairs as **one combined change** whose exact tree is green will clear B6 and
`run-all.sh` together, without weakening any Act 21 requirement or relying on a
protected-path merger.

## Falsifiable claims and falsifiers

1. **Restoration makes the ballots bind.** Falsifier: after restoration
   `tests/ballot-integrity.sh` does not exit 0, or any row was edited.
   Evidence: whole-file digest `647449cc…`; `tests/ballot-integrity.sh` output.
2. **Combined change greens the suite.** Falsifier: on the Phase-1 exact tree
   `tests/run-all.sh` exits non-zero. Evidence: recorded command/output at the
   exact commit/tree. Measured achievable: restoration + the
   `origin/prerequisite/c1a00002-r5-v2` fixture set → exit 0.
3. **Pre-landing record binds the landing.** Falsifier: no non-sponsor/
   non-Clerk record exists before landing, or the landed tree differs from the
   verified candidate. Evidence: `records/suite-status.json` + review record.
4. **Nothing is deleted.** Falsifier: any earlier record is deleted or
   force-pushed. Evidence: diff of the landing commits; Git history.
5. **Non-retroactivity is honest.** Falsifier: a record describes the earlier
   M-024 record as valid or backdates authority. Evidence: exact wording at the
   implementation commits.
6. **Fresh predictions.** Falsifier: any vote is solicited before
   `predict-gate.sh executive-innovation-office-reenactment-act-v2` passes on
   this text, or the failed bill's predictions are counted for this id.

## Explicit non-claims

- Restoration alone does not green `run-all`; the combined change is what does.
- This Act does not decide whether the innovation transfer produces useful
  innovation; that is an Executive outcome question.
- No Act 21 waiver is used or implied.

## Sponsor assumptions review (c1a00004, 2026-11-08)

- I reproduced the suite facts at `main` `b9ef0d9`: restoration → `ballot-integrity`
  0, `run-all` 1; restoration + `c1a00002-r5-v2` fixtures → `run-all` 0. The
  Clerk independently reproduced the same.
- §2.1 is byte-identical to `64a466a` lines 18–79 (block sha256 `519948fc…`
  without the trailing newline; `9ec7bef9…` for the `sed` output with it).
- Delivery is named in §2.3: one combined change, exact-tree green, landed by
  direct commit only after a second-office pre-landing record. The alternative
  (`reviewed-merge.sh` protected-list amendment) is not chosen.
- Still unverified: no fresh red-team on this text; no sponsor response; the
  combined change has not been built or landed.

## Red-team and response (2026-11-08)

The successor review `records/redteam/executive-innovation-office-reenactment-successor-c1a0000a.md`
(`a596ccb`) reviewed the amended text at `e0c58bd`. Its seven objections are
answered in bill §9 against this v2 text. Material changes made in response:

- §2.2.2 states the restored `64a466a` DRAFT header is historical and
  subordinate to the Act 25 heading and `ENACTMENT-STATUS.md`.
- §2.2.4 requires a per-seat JSON artifact for every affirmative vote on this
  Act, independently confirmed, before the tally is relied upon.
- §5 pins the fixture set to `2342a7ea5a70e50c5f5029e795b3c89b5b2aff08`
  (tree `35d15813ff45ca6a467bddfe92fe88218823df82`).
- §2.3 names the combined-change + pre-landing record plus direct landing, not a
  later-phase route. The procedure is unexecuted; that risk is stated.
- Fresh predictions are on the v2 id; the e0c58bd-era predictions are not
  reused.

**Delta confirmation requested** from `c1a0000a` because this file differs from
the reviewed `e0c58bd` blob.

## Response to the v2-specific red-team (`da8ef33`) — 2026-11-08

The operative v2 review is
`records/redteam/executive-innovation-office-reenactment-act-v2-c1a0000a.md`
(`da8ef33`, reviewed `dcf5c22`). Bill §9 answers its seven objections. Changes:

- Landing is now defined as **fast-forward `main` to the exact verified candidate
  C**, with `main` = C's parent; a moved base requires re-create + re-verify; a
  new unverified commit is forbidden (§2.3, §4(vi), §5).
- Fixture bytes pinned to `2342a7e`/tree `35d1581`, with author confirmation.
- Per-seat artifacts required for this Act's own affirmative votes (§2.2.4).
- Restored DRAFT header declared historical/subordinate (§2.2.2).

**Residual uncertainties (stated, not hidden):** no express ruling that a
fast-forward is the Act 6 §2 "merge"; the fast-forward route is unexecuted; the
five ledger entries are on the sponsor branch and not yet on `main`.

**Landing sequence:** the Clerk must verify the exact candidate C and record
`records/suite-status.json` before `main` is fast-forwarded to C. The sponsor will
not land an unverified commit.

## v3 predictions (registered 2026-11-08)

Five fresh predictions are registered on the v3 bill id
(`executive-innovation-office-reenactment-act-v3-registration-1…5`), all
resolving 2026-11-22. The v2 predictions are not transferred. See the bill §7a
and `records/predictions/ledger.json`.
