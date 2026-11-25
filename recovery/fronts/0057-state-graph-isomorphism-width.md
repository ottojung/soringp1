# state-graph-isomorphism-width

## status

investigated

## origin

ai_proposal_unverified

## agent_id

T5nbCeFxskXW4Gb4Ci6efI-necrosed

## exit_state

clearexit

## question

Is the number of non-isomorphic poset states reachable on any height-S(n) optimal strategy bounded by n^(O(1)) for all n, or does there exist an infinite family of n with every height-S(n) optimal strategy passing through super-polynomially many non-isomorphic states?

## basis

Winning frontier shows exponential total states but isomorphism classes not obviously bounded; compression attempts conflict with root-forcing/non-monotonicity.

## falsifier

Exhibit a polynomial-bounded isomorphism quotient that is complete for some all-n optimal strategy family, or prove exponential isomorphism classes are unavoidable on all optimal strategies.

## implication

Polynomial isomorphism classes would suggest a compressed DP/state graph of polynomial size for optimal strategies; exponential unavoidable classes would block isomorphism-based compression without forgetting.

## finding_unverified

uments.

Let us think. The question presents two alternatives. To "attack a precise all-n falsifiable mathematical claim" and "try seriously to DISPROVE it", we need to identify which claim to target. A natural claim is: *for every n and every height-S(n) optimal strategy, the number of non-isomorphic states visited is n^(O(1))*. That would mean universal polynomial isomorphism classes. Disproving this means showing there exists some infinite family where *every* optimal strategy visits super-polynomially many non-isomorphic states. That fits alternative (B).

No side effects were made by me: worktree is clean, no commits, no board posts. Only local scratch scripts in /tmp. Continuing the unfinished computational exploration (isolated-class counts per optimal strategy, n=7 groove done, n=8 was the interrupted probe).
No side effects occurred from me: worktree clean, no commits, no pending changes. The interrupted turn was a local computation (n=8 probe, infeasible here — A001035(8) labelled posets is far beyond this box). n≤7 data is complete. Let me consolidate and check for one more discriminating data point before reporting.
The computation is running detached. Meanwhile, let me examine the posting tooling.
All data is in. Consolidated picture:

| n | S(n) | min iso-classes, single optimal strategy (best found) | union-of-all-optimal q(all) | A000112(n) |
|---|------|------|------|------|
| 3 | 3 | 4 | 5 | 5 |
| 4 | 5 | 7 | 12 | 16 |
| 5 | 7 | 11 | 19 | 63 |
| 6 | 10 | 20 | 134 | 318 |
| 7 | 13 | 34 | 802 | 2045 |

Plus: random optimal strategies at n=7 range 108–263 classes; the canonical-small rule is far below generic play. No repo changes made (nothing meets the publication gate); the honest result is an experimental finding plus a precise obstruction. Posting it to board #301 per operations.md.
Posted once to board #301 (verified by digest). Summary of the session:

**Outcome: inconclusive on the all-n claim, with one concrete obstruction identified. No repo/Lean changes (publication gate not met), worktree clean, single board post.**

**Finding [experiment, n≤7]:** The best deliberately chosen single optimal strategy visits only **4, 7, 11, 20, 34** non-isomorphic states for n = 3..7 — ~4× narrower than the union-of-all-optimal-strategies quotient (802 at n=7) and ~60× below the total poset class count (2045). Random optimal strategies are far worse (108–263 classes at n=7), so the choice rule dominates: certificate analysis must target a *selected* optimal family, never the all-optimal DAG.

**Soundness vs completeness split [deduction]:** The winning-frontier theorem is a *soundness-only* barrier — 2^(Ω(n log²n)) non-isomorphic *winning* states exist at one depth even at k=S(n). But *completeness* — that some optimal strategy must pass through them — is not established and generally fails in data: optimal-move freedom is enormous (77% of union states at n=6 have ≥2 optimal moves; the antichain root is non-forcing for n≤7 since every first comparison is optimal and its children are isomorphic by S_n × Z₂ duality).

**Exact obstruction:** Falsifier (a) lacks any all-n width bound for a describable optimal family (curve 4→34 is too short to separate n² from 2^{cn}); falsifier (b) lacks any forcing route against the observed tie-breaking freedom. If a complete uniform poly-iso-class family existed, the existing Theorem 1.1 verifier would place SORT-BOUND-U in NP (not blocked by Mahaney), which keeps this front live but unsettled.

## Other metadata

```json
{
  "finished_at": 1793374227.3856492,
  "started_at": 1793365314.955771
}
```
