# certificate-starvation-propagation-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

PcNvKx3PtxcYlxbjLy8lrh-notably

## exit_state

clearexit

## question

For every n >= 8, does there exist a certificate-starved poset state reachable from the n-antichain by optimal play at depth S(n), or does some n have every optimal-play reachable state admit an A/B/C-certified optimal continuation?

## basis

Newest board #301 02:10Z antichain-reachable-abc-tree-completeness reports reachable certificate-starved states at n=8 and n=9; the 02:14Z Executive calls propagation a dedicated falsification target.

## falsifier

Exhibit an n >= 8 such that every poset reachable from A_n along a height-S(n) optimal strategy has an A/B/C-certified optimal move at every node, or prove propagation for all n >= 8.

## implication

Propagation would show A/B/C certificates are incomplete for optimal antichain play at every n, constraining certificate-based NP routes for SORT-BOUND-U; failure would isolate starvation as a small-n phenomenon. No direct S(n) bound changes.

## finding_unverified

</longcat_tool_call>

Recovering — inspecting worktree and ledger before continuing.
Worktree is clean with no new posts — checking for remaining work.
No board post exists yet for this front — verifying the corrected n=8–10 results before reporting.
Core witnesses verified — analyzing the n=10 starved state's children.
Validation complete — drafting the board report.
Recovery complete. No external effects were duplicated; the one unfinished item (this front's board report) is now done.

**Effects that actually happened before the failure (verified, not repeated):** prior front's n=8/9 census scratch, corrected `reachg`/`gcheck` runs for n=8–10, and a 99.2%-complete `p11.txt`. **Not happened:** no #301 post from this front existed, no commits, no ledger write. Worktree clean at `6a96398` throughout.

**Finding posted once to #301 (07:04:58Z, exactly 1 match, no duplicates):**
- **Bug correction [deduction+experiment]:** the 02:10Z census undercounted — `ext()` clobbered the `downMask` used by `slaveCount`, and the reachability pass lacked the `F==0→G=true` base case. Corrected optimal-reachable bad counts: n=8: 146/5102 (was 18), n=9: 2184/33054 (was 153); new n=10: 1299/19565. `F` values byte-identical (0 mismatches); full-census H>F at n=8 corrects 52→434.
- **Propagation holds through n=10** (starved reachable states exist: Q8, prior Q9, new Q10 `up=(0,0,0,0,0,0,512,768,512,0)`, F=19, G=false, 3 optimal steps from A_10), **but `G(A_8)=G(A_9)=G(A_10)=true`** with F=16,19,22 matching published S(n) — so all-certified optimal trees still exist and neither all-n disjunct is resolved. All-n remains OPEN.
- **Validation:** independent Python replay agrees 20/20 on n=8 samples and reproduces reachable=5102; cert logic matches Peczarski 2006 via Gupta arXiv:2607.23926 Lemma 3 / CDM 2017 Facts.
- **Honest limits:** n=11 exhaustive (46.7M classes) exceeds this host's budget — deliberately not attempted; `P_4+C_2^k` padding pattern is numerical through n=10, not a proof. No S(n)/SORT-BOUND-U consequence; no repo/Lean changes per the publication gate.

## Other metadata

```json
{
  "finished_at": 1794294387.6447856,
  "started_at": 1794281700.8731487
}
```
