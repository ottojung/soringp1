# colour-pair-signature-move-quotient

## status

investigated

## origin

ai_proposal_unverified

## agent_id

uhGjva0kmjeaxnYiTMZXzF-huguenots

## exit_state

clearexit

## question

For every finite poset P, is the two-dimensional colour-refinement signature of an incomparable pair a sound invariant of its exact move value max(F(P+x<y),F(P+y<x)), as the data through n<=6 suggest, or does some poset have two pairs with equal signatures but different move values?

## basis

docs/research-compression-next.md section 6d leaves the colour-pair-signature quotient unproven after no counterexample through n<=6; section 5 proves only the stronger Aut(P)-orbit quotient sound.

## falsifier

Exhibit an explicit poset with two incomparable pairs of equal colour-pair signature and unequal exact move values, or prove signature-equality implies move-value equality for all finite posets.

## implication

Soundness would yield a polynomial-time move quotient for exact minimax and a new state-compression lemma relevant to evaluating S(n); a counterexample would rule out colour-refinement quotients for exact search and limit canonical-form evaluators.

## finding_unverified

## Finding

The §6d colour-pair quotient is **false**, not merely unproven. There is an explicit counterexample at **n = 8**.

Let \(P\) be the height-2 poset on \(\{0,\dots,7\}\) whose transitive closure is

\[
5<0;\qquad 6<0,\ 6<1,\ 6<2;\qquad 7<0,\ 7<3,\ 7<4,
\]

with successor masks

\[
(0,0,0,0,0,1,7,25).
\]

The repository’s `refine_colors` gives

\[
c=(0,1,1,1,1,2,3,3).
\]

The incomparable pairs \(\{1,2\}\) and \(\{1,3\}\) therefore have the same unordered colour-pair signature \((1,1)\). But their exact move values differ:

\[
T(\{1,2\})=\max(F(P+1<2),F(P+2<1))=10,
\]
\[
T(\{1,3\})=\max(F(P+1<3),F(P+3<1))=11.
\]

In fact all six pairs among \(\{1,2,3,4\}\) have signature \((1,1)\); \(\{1,2\}\) and \(\{3,4\}\) give 10, while the other four give 11. Also \(F(P)=11\), and the optimal move value is 10. So a quotient that keeps one representative per signature and happens to choose \(\{1,3\}\) returns 12 instead of 11.

## Verification and minimality

- A self-contained checker with its own closure, colour refinement and memoised labelled minimax reproduces all values over 977,093 descendant states.
- The repository’s exact isomorphism-class DP at \(n=8\) agrees.
- Exhaustive scan of all **16,999** isomorphism classes at \(n=8\): 16 classes show the failure; the displayed witness has the minimum relation count, 7.
- Exhaustive scan for \(n\le 7\) found no failure, so \(n=8\) is the smallest size for this signature.
- Sanity values \(S(6)=10\), \(S(7)=13\), \(S(8)=16\) match the literature.

## Scope and honest limits

This is a genuine counterexample to **soundness of the specific `refine_colors` endpoint-pair move quotient**. It does not disprove every colour-refinement method.

- The sound **Aut\((P)\)-orbit quotient** of §5 is unaffected: the witness is exactly two distinct Aut\((P)\)-orbits collapsed by colour refinement.
- If “two-dimensional” is read as full **2-WL pair colouring**, that is stronger: it separates this witness, and an exhaustive \(n=8\) scan found no 2-WL counterexample. That stronger variant remains open beyond \(n=8\).
- Completeness of `refine_colors` plus individualisation as an isomorphism canonical form is not in question. The failure is that it is incomplete for move orbits, hence unsound for exact move values.
- No complexity separation, no claim about all polynomial-time move quotients, and no change to the exponential state count.

I posted this finding to board #301. The repository worktree remains clean; scratch verification files are under `/tmp/opencode/cpsig`.
Recovery check complete. I did not repeat any external action.

**Effects that actually happened**
- Board #301 comment was successfully posted exactly once:
  - author: `SoringP1 frontier: colour-pair-signature-move-quotient`
  - timestamp: `2026-11-09T12:51:12.788Z`
  - current board scan finds **1 unique match**, not duplicates.
- Scratch verification files remain under `/tmp/opencode/cpsig`; `board_post.err` is empty, and `board_post.out` contains exactly one copy of the posted front text.

**Repository state**
- Worktree is clean at `6a96398`.
- No commits, branches, or repository files were created by this work.
- No Lean changes.

**Unfinished work**
- None from the mathematical front. The counterexample, independent verification, minimality scan, and board report are complete.

No further posts or side effects were performed.

## Other metadata

```json
{
  "finished_at": 1794228737.0205295,
  "started_at": 1794227803.3037567
}
```
