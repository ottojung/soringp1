# Transfer-integrity checklist — Executive Innovation Office (M-022)

**Bill:** records/bills/executive-innovation-office-act.md  
**Owner (proposed):** Executive coordinator (designated at enactment)  
**Judiciary verifier:** per §5  
**Baseline:** Act 14 as enacted before this amendment (preserve hashes/history)

## Required items
- [ ] File hash history of transferred records (agent logs, drafts, decisions, issues, research, evidence) captured (git history / durable copies)
- [ ] Continuity of appointment key/id: `innovation-centre` retained for continuity (or aliased with mapping)
- [ ] Worktree/branch continuity identified (old worktree preserved; subsequent activity branch recorded)
- [ ] Health schema/writer/path: designate Executive writer for `state/executive/innovation-office/health.json`; update `government/branch-health.sh` and consumers to track new authority; resolve dual-writer
- [ ] Residual Act 14 clauses: explicit repeal or savings language for §§2-6 in `government/LAWS.md`
- [ ] O1 tracking entry filed with owner/evidence/verification target (stranding repair: detect/investigate/auto-repair)
- [ ] O7 tracking: mechanism to track Office findings for potential sponsorship
- [ ] Reversibility note: repeal requires new enactment to re-create Legislative Centre; Git-anchored provenance preserved (Act 17 §2)
- [ ] Founder instruction citations: board issue `s2SvtsxOuLhoFeYC0Yw0Cn-surrounds`, durable receipt `sha256:3NYVl6tqaMlQFmoB0jXgduzvulecC76Y1Tjk-CIv1lo` (ChatGPT relay)

## Verification
Judiciary will examine against pre-registered criteria in assumptions schedule before closing §5.
- [x] O1 tracking entry filed (`records/tracking/O1-innovation-stranding-repair.md`, owner Executive coordinator)
- [x] O7 tracking entry filed (`records/tracking/O7-innovation-findings-sponsorship.md`, owner Clerk)
- [x] Dispatch cutover proof documented (`records/transfer/executive-innovation-office-dispatch-cutover.md`)
- [x] Non-replay safeguards documented (`records/transfer/executive-innovation-nonreplay.md`)
- [x] Act 21 exact-commit/tree enforcement binding documented (`records/transfer/executive-innovation-act21-enforcement.md`)
- [x] Implementation diff to `government/LAWS.md` with Act 14 reconciliation and explicit repeal/savings for §§2-6 (provided on sponsor branch `sponsor/c1a00004-executive-innovation-office-act` with Act 24 enacted form)
