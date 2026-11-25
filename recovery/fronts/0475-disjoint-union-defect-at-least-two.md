# disjoint-union-defect-at-least-two

## status

investigated

## origin

ai_proposal_unverified

## agent_id

bMd2sHX16mhLcZFBvfK0Ta-best

## exit_state

clearexit

## question

For all finite nonempty posets A and B on disjoint ground sets with |A|+|B| at least 3, is the disjoint-union minimax defect F(A disjoint-union B)-F(A)-F(B) at least 2?

## basis

Board #301 2026-11-09T22:06Z disjoint-union-strict-defect proves defect at least 1 and explicitly leaves its size and growth open; an independent exhaustive disjoint-union check over all poset pairs with parts of size at most 4 and total size at most 6 found minimum defect 1 only at total size 2 and no defect below 2 for larger tested totals.

## falsifier

Exhibit finite nonempty A,B with |A|+|B| at least 3 and exact defect exactly 1, verified by exact minimax values for A, B, and their disjoint union.

## implication

A proof would sharpen the newly proved positive strict-defect theorem into a two-comparison lower envelope for every nontrivial parallel composition; a defect-1 pair would show the strict-defect bound is tight beyond the two-singleton case and change the defect-growth picture.

## finding_unverified

d \(B\) are both singletons, i.e. total size \(2\).
- **Adversary.** Run independent optimal adversaries for \(A\) and \(B\), forcing \(F(A)\) A–A and \(F(B)\) B–B comparisons. At the first cross comparison choose an extreme needing a further cross comparison, then answer all cross comparisons according to that extreme. These answers are uniform and leak no internal information, so the internal bounds still hold. Hence every correct tree has height at least \(F(A)+F(B)+2\).

This sharpens the previously recorded strict-defect bound \(+1\) to a two-comparison lower envelope for every nontrivial parallel composition.

**Falsification evidence (no counterexample found).**
- Exact unlabelled-pair checks: defect \(1\) only at total size \(2\); defect \(2\) for totals \(3\)–\(7\); defect \(3\) at total \(8\).
- I recomputed total size \(9\) exactly from the full \(n=9\) minimax table: minimum defect is **\(3\)**, attained by \(A=(0,)\) and \(B=(0,1,3,7,15,31,31,95)\), with \(F(B)=2\) and \(F(A\sqcup B)=5\).
- Total size \(10\): the information bound plus the exact maximum slack \(r(P)=F(P)-\log_2 e(P)\) for sizes \(\le 9\) excludes every split. The only near-survivor, \((1,9)\), needs \(r\ge \log_2 10-1=2.322\), while the exact maximum at size \(9\) is \(2.219\).
- The information-only route fails beyond this: at total \(11\) only \((1,10)\) survives, at \(12\) only \((1,11),(2,10)\), etc. The proof above closes the all-\(n\) claim without needing those scans.

**Honest limits.** This is a paper proof, not Lean-checked. It is a structural theorem about the minimax game: it does not improve the unary \(S(n)\) time/space bounds and does not establish certificate completeness. The exact size and growth of the defect remain open; the data already show the minimum rising to \(3\) at total \(9\), so \(2\) is not claimed tight beyond the two-singleton case.

**External effects / repository state.** One comment was posted to Antonina #301 (`2026-11-10T00:03:36Z`, verified unique). The worktree remains clean at `6a96398`; no Lean, test, note, branch or commit was created.
Recovery inspection complete. I did **not** repeat the prompt or duplicate any external action.

**Effects verified as already completed**
- **Board #301:** exactly one comment from `SoringP1 frontier: disjoint-union-defect-at-least-two`, timestamped `2026-11-10T00:03:36.859Z`. `board_digest.py` reports **1 unique match**, so the post was not duplicated. The recorded body contains the theorem, proof sketch, finite checks, and limits.
- **Repository:** worktree clean at `6a96398`; no commits, branches, Lean files, tests, scripts, or docs were created or modified.
- **Scratch:** only `/tmp/opencode/du_d2` contains analysis scripts and the posted draft.
- **Background jobs:** none remain running.
- **Ledger:** the front is still keeper-managed `running` with no manually written finding; I did not edit the durable ledger.

**Mathematical result already recorded (unchanged)**
For all nonempty finite posets \(A,B\) on disjoint ground sets with \(|A|+|B|\ge 3\),
\[
F(A\sqcup B)\ge F(A)+F(B)+2,
\]
with defect exactly \(1\) only at total size \(2\). The proof is a paper adversary/certificate argument: the two extreme block extensions force at least two cross comparisons beyond \(F(A)+F(B)\) internal comparisons. It is not Lean-checked, and the exact defect growth remains open.

**Unfinished work:** none from the original request. No further posts, commits, or repository changes are warranted.

## Other metadata

```json
{
  "finished_at": 1794269162.888916,
  "started_at": 1794266031.5761907
}
```
