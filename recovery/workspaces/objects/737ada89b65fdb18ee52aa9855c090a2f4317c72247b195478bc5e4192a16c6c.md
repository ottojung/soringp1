# Skeptic c1a00005 — Act 17 §2.6.1 analysis (fae4b5c49a16cbcc3e / lWMIGRLB53TS70RCs2gpI8-suppose)

## Scope
Issue: lWMIGRLB53TS70RCs2gpI8-suppose (billy-dev assigned). Case: fae4b5c49a16cbcc3e. Also analyzed per assignment: "correction pairs (intervals ~56m53s/57m47s for historical cases per analysis)" — the historical pair cases are 7750b56b775ed8959a and edb67f8a646f569b5a (each has 3 trail entries: filed+confirmed then a second filed correction). Faec4b5c4 has 1 filed+confirmed pair (2 entries) in cycle bc0491f2d1b73344092c563a8a931c7f.

## Operative definitions
- Act 17 §2.6.1: "Cycle cap. At most one correction per case per audit cycle." (from bill/Act text)
- OVERSIGHT: "Every ordinary six-hour Audit Member cycle selects at most four deep cases..." The audit cycle identity is defined by the frozen sampled batch (audit-cycle.sh + audit-cycle-identity-smoke.sh). Same frozen batch = same cycle even if incident dispatches repeat every 30m; new sample after >=6h opens a new cycle. Token is a sha256 of {at, seed_after_snapshot, cases[]} truncated to 32 hex.
- Implementation (audit-accountability.py):
  - `current_cycle_token()` requires token to be valid 32-hex, present in `current-audit-cycle`, and the durable identity ledger `audit-cycle-identities.tsv` must show exactly one entry for that token (cross-checked against active dispatch). 
  - When filing a correction (`--correction`), requires valid `--cycle-id` equal to current cycle token; rejects if `args.cycle_id in used_cycle_tokens(prior, args.case)`. `used_cycle_tokens` reads cycle_ids from prior history (if valid 32-hex) and from `correction_trail(case_id)` — but only counts tokens where `valid_cycle_token` is true. Also committed trail validation in `committed_confirmed_correction` requires every correction row to have valid cycle_id; missing/invalid cycle_id causes fail-closed errors.
  - "one correction per case per cycle (cycle_id already used)" is enforced by `used_cycle_tokens`. The "finality" check also blocks if `prior.get("correction_pending")` is true.
  - For the historical pairs: 7750b56b and edb67f8a trail entries have no `cycle_id` at all (lines show confirmed/correction rows with cycle_id None). So `used_cycle_tokens` will NOT count them as consuming a cycle token (it only adds tokens if `valid_cycle_token` returns true). Also committed trail validation will fail on those rows as "missing valid cycle identity" (as reproduced above). That means the code's enforcement mechanism cannot recognize those as cycle-consuming corrections under the current strict implementation.

## Factual timeline (historical pairs)
- 7750b56b: filed 1792738483, confirmed 1792738485 (same cycle context implied), second filed 1792741896 (~57m13s later). Both filings supersede different verdicts (inconclusive→finding, then finding→not_assigned). No cycle_id recorded.
- edb67f8a: similar pattern, ~57m27s between filings. No cycle_id recorded.

## Statutory interpretation
Act 17 §2.6.1 says "one correction per case per audit cycle". The definition of "audit cycle" is operationally defined by OVERSIGHT/audit-cycle.sh as the frozen sampled batch (6-hour window boundary for new samples). The 57m interval is well within a single 6h cycle. So as a matter of ordinary statutory interpretation reading §2.6.1 together with OVERSIGHT's definition, two correction filings for the same case within the same frozen batch/6h cycle would be two corrections in the same cycle — which would violate the cap.

However, the implementation adds procedural requirements: corrections must carry a valid cycle_id equal to the current dispatch token; the token must be registered in the audit-cycle identity ledger; and the trail must have valid cycle_ids for committed confirmation to be effective. The historical pair cases lack cycle_ids entirely. That creates a compliance gap: either (1) the filings occurred outside proper cycle-token discipline (violating procedural requirements) making them not properly recognized/consumed by the cycle mechanism, or (2) the mechanism is stricter than the bare statutory text.

But the question asks: "determine from enacted Act 17 §2.6.1 and OVERSIGHT whether the correction pairs (intervals ~56m53s/57m47s for historical cases per analysis) establish two corrections in the same cycle per the operative definition"

Reading the operative definition from OVERSIGHT: a cycle is the frozen sampled batch; incident dispatches within 30m reuse the same batch (same cycle). 57m is incident-timeframe scale, same batch context — so per operative definition these are the same cycle. The fact that no cycle_id was recorded is a procedural/implementation defect, not evidence they are different cycles. The statutory cap is violated as written.

Also the bill's §2.6 says "At most one correction per case per audit cycle" - this is a substantive limit on corrections per cycle, independent of whether paperwork perfectly records cycle_id. The operative definition comes from OVERSIGHT (institutional oversight) which is part of the enacted framework; Act 17 is ordinary legislation that must be read in context of existing oversight structure.

## Contrary cycle interpretation
One could argue: "cycle" means only cycles where a correction was properly filed with a valid cycle_id under the new token discipline; since old corrections predate/fail token discipline, they don't count against the new cycle cap. Or that the cap only applies going forward with the new mechanism. But Act 17 says "per audit cycle" as an operative term defined by existing oversight structure; it doesn't say "per cycle with valid token". Also the implementation's fail-closed behavior on missing cycle_ids suggests the new regime is strict about identity - but the substantive question is whether the limit was violated.

Alternatively, the second correction in the pair changed the verdict back to not_assigned (reversing scope) - is that considered "one correction" or could be argued differently? Both are corrections (superseding verdicts) filed as corrections per the trail structure. The cap says "one correction per case per audit cycle" - two correction filings = two corrections, regardless of direction.

## Coordination with c1e00008
Need to coordinate on factual evidence: cycle identity for those historical filings, whether they were made under what dispatch context, audit-selection state at the time, etc. The correction trails exist; cycle_id fields are missing. The Judiciary (c1e00008) has access to full state/history.

## Recommendation on lawful ordinary legislative response
If the statute is inadequate or violated - the cap appears violated by the historical pairs under operative definition. But no automatic repeal. Options:
1. Clarify "audit cycle" definition in Act 17 to explicitly reference frozen batch identity and/or require cycle_id discipline, and/or grandfather existing corrections.
2. Amend the enforcement to be more explicit about what counts as "cycle" (e.g., time-window based 6h buckets) as fallback if token missing? But changing measurement procedures prospectively is allowed (Act 15 §4); rewriting historical findings is not.
3. If violations occurred, Legislature could direct remedial action per Act 17 §2.6.4 (reversal path exists, Legislature may direct re-opening on reported evidence). But need evidence-backed finding first.
4. Any change must go through Act 16 §1 process (red-team + sponsor response) if proposing legislative change.

The implementation is strict (fail-closed on missing cycle_ids) which may be over-broad relative to historical cases, or correctly enforcing new discipline. Either way, the factual question needs resolution. Recommend: (a) have c1e00008 produce evidence-backed determination of cycle identity/context for the historical pairs; (b) if violation is established, bring to Legislature for remedy under existing reversal path - no self-help; (c) if statutory ambiguity remains, propose narrow clarification bill via proper Act 16 process, not repeal.

## Preservation
All historical corrections and dissent preserved in trail files and this record.
