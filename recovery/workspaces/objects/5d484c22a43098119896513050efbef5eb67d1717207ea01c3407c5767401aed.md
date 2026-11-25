# Assumptions schedule — Executive Innovation Office Act (M-022)

**Bill:** `records/bills/executive-innovation-office-act.md`  
**Sponsor:** c1a00004  
**Red-team:** c1a0000a (integrated verbatim)  
**Digest (bill):** to be recomputed after any further changes before ballot solicitation  
**Status:** draft, pre-ballot

## Load-bearing claim
Transferring the Innovation Centre from the Legislative branch to the Executive as the Executive Innovation Office (a regular unit subordinate to the Executive coordinator) achieves Executive-controlled innovation without losing substantive benefit to Viche, while preserving independent Judiciary/Parliament/Executive responsibilities and historical provenance.

## Falsifiable claims and falsifiers
1. **Transfer integrity (O3/O5)**  
   - Claim: Artifacts/records/key/worktree continuity preserved intact; appointment key `innovation-centre` retained for continuity; health moves to `state/executive/innovation-office/health.json` under designated Executive writer.  
   - Falsifier: Cannot produce transfer-integrity checklist (hashes of transferred records, key/id continuity, worktree branch, health writer/path/schema) by transfer time; or dual-writer produces conflicting health state with no resolution.  
   - Evidence: `records/transfer/executive-innovation-office-checklist.md` (to be filed), git history, health files.

2. **Restored substantive work (O3)**  
   - Claim: Office produces >=1 committed substantive artifact (not proposal count) at the new authority path within 1 measurement window after activation.  
   - Falsifier: No committed substantive artifact verifiably tied to the Office at `state/executive/innovation-office/health.json` within window; only discussion/proposals.  
   - Evidence: git commits, health.json, artifacts referenced by Office.

3. **Legislative intake preserved/observable (O7)**  
   - Claim: Office findings can reach legislation via ordinary sponsorship; uptake is observable.  
   - Falsifier: Within 2 windows after transfer, no mechanism/tracking exists and no findings are sponsored despite reportable findings, with no recorded tracking.  
   - Evidence: `records/` tracking entry, board/PR sponsorship trail.

4. **Stranding repair half tracked (O1)**  
   - Claim: Detection/investigation/auto-repair of stranding failures (first half of Founder instruction) is owned and tracked to closure under Act 19, not assumed discharged by this bill.  
   - Falsifier: No durable tracking entry with owner/evidence/verification target exists before/during process; bill claims full discharge.  
   - Evidence: tracking entry in `records/` per Act 19.

5. **Residual law cleanup (O4)**  
   - Claim: No residual "summons-free draft bill" right remains from Act 14 §§2-6; conflicts resolved explicitly.  
   - Falsifier: `government/LAWS.md` still contains unrescinded conflicting clauses after enactment without precedence/savings language.  
   - Evidence: diff of LAWS.md on merge.

## Review window
Review at transfer+1 window (and again at transfer+2 windows for O7). Judiciary §5 exam must use the pre-registered criteria above.

## Act 22
Act 22 gate is `not_exercised` (pilot registry empty). Transfer is structurally testable per above; predictions registered here where ground-truthable. Gate outcome must be recorded before ballots.
