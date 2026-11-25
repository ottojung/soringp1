# disjoint-union-minimax-superadditivity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

N7YUdbEHrvpGx0ktKlhnX4-eyelid

## exit_state

clearexit

## question

For all finite posets A and B on disjoint ground sets, is F(A disjoint-union B) at least F(A)+F(B), where F is the exact minimax comparison number measured against the linear extensions of the poset in question?

## basis

Newest #301 correction showing F(K disjoint-union A_s) need not equal F(K)+I(|K|,s) because cross comparisons can order elements of K; docs/research-series-decomposition.md; a finite exact-minimax scan over all 3+3 labelled poset pairs found no violation.

## falsifier

Exhibit explicit finite posets A and B with F(A disjoint-union B) < F(A)+F(B), with both sides obtained from the exact minimax recurrence rather than from an information bound or an assumed additivity formula.

## implication

An all-n superadditivity theorem would give a sound decomposition lower bound for reachable disjoint-union states; a counterexample would show exactly how cross-component comparisons can destroy direct-sum intuition and would invalidate evaluators that treat such unions additively.

## finding_unverified

(5,14,46,178,851,5138,40246\).
- at \(n=8\), every nondegenerate pair has slack at least \(3\) (slack \(0\) occurs only with an empty component).
- for \(n=9\), a sound information prune over all \(23{,}687\) split pairs found **0 candidates** satisfying \(\lceil\log_2 e(A\sqcup B)\rceil\le F(A)+F(B)-1\); hence superadditivity at \(n=9\) also follows from \(F\ge\log_2 e\).

These finite checks corroborate the proof but are not the proof.

### Exact obstruction to the natural induction

The tempting component potential
\[
\Phi(P)=F(P|_A)+F(P|_B)-c(P)
\]
(where \(c(P)\) is the number of edge-containing components of the cross-comparability graph) survives exhaustive checks \(n\le8\), but it is **not** an adversary potential. Explicit \(n=6\) witness:

\[
P=(0,1,1,3,5,21),\quad A=\{2,3\},\quad B=\{0,1,4,5\},
\]
with exact values \(F(P)=4\), \(F(P|_A)=1\), \(F(P|_B)=2\), \(c(P)=1\), so \(\Phi(P)=2\). The single comparison \(1<4\) inside \(B\) has children with exact \(F=2\) and \(F=3\), and both children have \(\Phi=0\). One query drops \(\Phi\) by \(2\): it mediates \(3<2\) through \(3<1<4<2\), doing double duty across the two induced blocks. The maximum-matching correction fails similarly (drop \(3\)). This explains why a component-count/matching induction is the wrong route, even though the theorem is true.

### Honest limits

- This is a structural theorem about the minimax game, not a complexity-class result and not an improvement of the established \(SORT-BOUND-U\) bounds.
- It does not give a faster exact evaluator or an NP certificate.
- The finite scans are complete only for the tested sizes; they are not a substitute for the proof.
- Novelty is low/folklore-adjacent. The value is closing the front, ruling out the falsifier, and recording the precise failure of the obvious cross-component induction.

An Executive 21:17Z note also stated the conclusion; the monotonicity + ordinal-sum proof above is the argument I checked and stand behind.
Recovery inspection complete.

## Effects that actually happened

- **Board post: confirmed, exactly once.** Antonina #301 contains my post at `2026-11-09T21:27:41.054Z` under `SoringP1 frontier: disjoint-union-minimax-superadditivity`. It was followed by an independent Viche Executive verification at `21:28:06Z`. I did **not** repost or comment again.
- **Git: no changes.** Worktree is clean on `billy-dev` at `6a96398`; no commits, branches, or repository files were created or modified.
- **Lean: untouched.**
- **Scratch: only `/tmp/opencode/du_superadd/`**, containing the scan scripts, logs, and the board-post draft. No repository side effects.
- **Background job:** the `n9stats.py` process was deliberately killed; it was scratch-only and produced no external effect.

## Remaining work

None. The research question was resolved in the prior turn with a paper proof and finite exact-minimax checks, and the finding was posted. Repeating the prompt would risk duplicating the #301 post, so I stopped after verification.

## Result recorded

The front is **true**: for all finite posets \(A,B\) on disjoint ground sets,

\[
F(A\sqcup B)\ge F(A)+F(B),
\]

because \(A\sqcup B\) is a subposet of the ordinal sum \(A\oplus B\), hence \(L(A\oplus B)\subseteq L(A\sqcup B)\), so \(F(A\oplus B)\le F(A\sqcup B)\), and \(F(A\oplus B)=F(A)+F(B)\).

The falsifier cannot exist. The exact component-potential obstruction and the finite scans (\(n\le8\) exhaustive; \(n=9\) information-pruned) are in the existing #301 post.

## Other metadata

```json
{
  "finished_at": 1794259769.442122,
  "started_at": 1794257550.7951157
}
```
