# antonina-OAYv0hxYe8yS3q1ODtuGhm-stately

Session: ses_e5365dfd0ffeLM5NgT4sFC7xfx
Workspace: /home/lubko/soring-fronts/review-realizability-sibling-budget-20261105
Created: 1793897144521; updated: 1793897174262

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ac9a2170001WNkB5pNrUCzIAU)

I’ll trace the target commit against its parent, derive the recurrence independently, and check the witness/path claims and documentation. I’ll keep the worktree read-only and won’t post to the board.

## Output 36 (msg_1ac9a6212001SUS2jZHt4wJ3Xm)

## Review: commit `42759e1`

**Recommendation: suitable for separate review approval, with one documentation defect to fix.** The reachability correction is sound, and my independent `n=5` checks reproduce the reported counts and exclusions. The tests pass, but their finite coverage is not evidence for the all-\(n\) claims.

### Recurrence and implementation

At depth \(d\), a reached state \(Q\) has \(S-d\) comparisons of total height remaining. To compare incomparable keys and reach either child, the comparison consumes one step and **both** resulting subtrees must fit the same remaining budget:

\[
\max(F(C_0),F(C_1))\le S-d-1.
\]

A wasted comparison leaves the state at \(Q\), so it is valid only if \(F(Q)\le S-d-1\). This follows directly from the strategy’s worst-case height: the sibling branch cannot be discarded just because the branch whose state is being tracked fits.

`build_reach` in `scripts/realizability_window.py` implements both conditions. Its non-antichain-only restriction on wasted comparisons is harmless: the antichain has no already-comparable pair to waste a comparison on. The `F` recurrence also uses the minimax maximum over both children.

### Witnesses and counts

Running the committed tests succeeds. Independently evaluating the code gives \(S(5)=7\), 63 poset classes, and 19 reachable classes. The proposed window-only counterexample `(0,0,0,1,9)` has `(e,covers,pi,F)=(20,2,2,5)`, satisfies the proposed window at depth 2, but is absent from `reach[2]`. Thus window sufficiency is indeed refuted at \(n=5\).

The \(C_2\oplus A_3\) declaration chain canonicalizes to `(0,0,0,7,15)`, with `(e,covers,pi,F)=(6,4,2,3)`, and is absent at depth 4. Its stated predecessor’s two children have continuation costs 4 and 5; with four comparisons remaining after that comparison, the child of cost 5 does not fit. The prior claimed witness is invalid.

### Theorem and documentation

The sibling correction does not affect Theorem 1’s necessity proof or the star exclusion: those are paper arguments about any occurrence, not conclusions inferred from the old reachability DP. The code’s finite star check is only a check through \(n\le6\); the all-\(n\) exclusion rests on the stated proof.

One residual false claim remains in the script’s **module docstring**: it still describes the old forward recurrence, says the census verified window sufficiency through \(n\le6\), and labels that claim a conjecture. This contradicts the corrected implementation and the updated note. It should be corrected before approval. I found no corresponding contradiction in the reviewed note or research-plan change.
