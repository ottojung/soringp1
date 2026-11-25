# antonina-LGEOlljKsABuelqqFCRugE-admit

Session: ses_e478ca269ffer2Yp5t6557uKl7
Workspace: /home/lubko/soring-fronts/optimal-fibonacci-split-alln
Created: 1794095930788; updated: 1794102521384

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 562 (msg_1b8d7c250001PaxkD4EOZ8Jb8s)

**Finding (posted to board #301, 2026-11-08T01:48:23Z): no counterexample to the single-optimal-branch Lemma A, but only a finite obstruction, not an all-`n` proof.** Worktree remains clean; no repo or Lean changes.

**Claim attacked.** For every finite poset \(P\) with \(m(P)\ge 2\), there is an incomparable pair whose minimax-optimal split has child depths
\[
(m(P)-1,\ \ge m(P)-2).
\]
This is stronger than the board’s Lemma A: Lemma A only needs both children \(\ge m-2\), while this requires the worse child to be exactly \(m-1\), i.e. the comparison must lie on an optimal branch.

**Exact checks, zero violations**

| Search | Result |
|---|---|
| all labelled posets, \(n\le 6\) | 130,023 at \(n=6\), plus smaller \(n\) |
| all unlabeled posets, \(n=7\) | 2,045 classes; 6,129,859 labelled minimax states |
| unlabeled \(n=8\), \(e(P)\le 5000\) | all 16,999 classes generated; every class meeting the filter checked exactly |
| core census \(e(P)\le 70\) | all 10,638 core isomorphism classes, complete through \(E=70\) |
| core census \(E=88\) | 21,932 of 22,120 classes, namely \(n\le 41\); not complete |

So the claim survived every exact check I completed. The missing \(E=88\) tail is 188 long-\(n\) classes, and I do not claim it.

**Near misses are not falsifiers.**
- The board’s \(e=8,m=4\) poset with successor masks \((0,0,1,3,7)\) has optimal splits with light child depth \(1\), but also optimal splits \((0,1)\) and \((3,4)\) with light child depth \(2=m-2\). It satisfies the claim.
- The four-element \(e=3,m=2\) balanced-split failure cannot refute this claim: at \(m=2\), the required bound \(m-2=0\) is vacuous.

**Structural reduction (paper deduction).**
1. Deleting a universal element preserves \(m\) and the set of incomparable pairs, hence preserves the claim.
2. For an ordinal sum \(A\oplus B\), \(m(A\oplus B)=m(A)+m(B)\), and an optimal comparison inside a factor lifts with the same one-step gap. Hence if both factors satisfy the claim, so does \(A\oplus B\).
3. Therefore a counterexample chosen with minimal \(e\) must be an **ordinal-indecomposable core**.

Combined with the complete core census through \(E=70\), this gives the exact finite obstruction:
\[
\boxed{\text{any counterexample has a core with } e(P)\ge 71 \text{ and } m(P)\ge 7.}
\]
The second follows from \(m\ge \lceil\log_2 e\rceil\). This is a deduction from exhaustive exact computation, not a proved all-`n` lower bound.

**Honest limits and complexity meaning.**
- No proof of the all-`n` claim and no counterexample. The decisive missing step is an extension lemma for adjoining a maximal element above a proper ideal; ordinal sums are already covered.
- Finite verification is not an all-`n` theorem.
- Even a proof of this claim would only yield Lemma A and hence the Fibonacci threshold picture \(T(r)=F_{r+3}-1\). It would **not** give a succinct optimal-play certificate, NP membership, or any complexity-class separation.
- This is entirely about the general-poset minimax game. It does not establish certificate **soundness** or **completeness** for `SORT-BOUND-U`; the soundness/completeness gap is untouched.
