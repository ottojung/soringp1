# antonina-RhF02Y4Q9iPpoIIcUZxAVI-substance

Session: ses_e3f761a60ffe6g9F3hBvGSq3Cf
Workspace: /home/lubko/soring-fronts/height-two-information-excess-bound
Created: 1794231625203; updated: 1794232953489

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 407 (msg_1c09cea000017l4orGxhuFyGsf)

**Mathematical finding: the proposed all-height-two bound is false.**

Let \(A_m\) be the \(m\)-element antichain and let \(P\oplus Q\) be the ordinal sum (every element of \(P\) below every element of \(Q\)). I used the exact composition lemma

\[
e(P\oplus Q)=e(P)e(Q),\qquad F(P\oplus Q)=F(P)+F(Q).
\]

The second identity is not merely an upper bound: cross-block comparisons are forced and reveal nothing about either internal order, so independent adversary strategies force \(F(P)\) comparisons inside \(P\) and \(F(Q)\) inside \(Q\).

Take

\[
P=A_{12}\oplus A_{12},
\]

a height-two complete-bipartite poset on 24 elements. Then

\[
e(P)=(12!)^2=229\,442\,532\,802\,560\,000,
\qquad \lceil\log_2 e(P)\rceil=58,
\]

and, using the exact literature value \(S(12)=30\):

\[
F(P)=S(12)+S(12)=60.
\]

Therefore

\[
\boxed{F(P)-\lceil\log_2 e(P)\rceil=60-58=2.}
\]

So the claimed bound “at most 1 for every finite poset of height at most two” is refuted. The value \(S(12)=30\) with \(\lceil\log_2 12!\rceil=29\) is Wells 1965, reported in Peczarski, *Towards optimal sorting of 16 elements* (2012), and restated by Stober–Weiss (2023).

**Finite evidence and the missed case.** An exact isomorphism-quotient minimax scan over all unlabeled posets through \(n=9\) (183,231 classes at \(n=9\), of which 2,223 have height at most two) still finds maximum excess 1. This extends the board’s \(n\le 6\) check to \(n\le 9\). The counterexample is invisible there because the first positive antichain excess occurs at \(n=12\), while the height-two ordinal sum needs two such factors.

**Concrete failed approach.** Disjoint unions cannot produce the same effect: for a disjoint union the binomial interleaving factor is present,

\[
e(P\sqcup Q)=\binom{|P|+|Q|}{|P|}e(P)e(Q),
\]

and its \(n\log n\)-bit contribution overwhelms the additive minimax lower bound. The ordinal sum is the height-preserving composition that avoids interleaving.

**Honest limits.** This kills the constant-1 claim and gives an exact gap of 2, but it does **not** prove that height-two excess is unbounded. If \(E(n)=S(n)-\lceil\log_2 n!\rceil\) were unbounded, \(A_n\oplus A_n\) would give unbounded height-two excess; unboundedness of \(E(n)\) is open, with only Sergeev’s \(o(n)\) upper bound. Nor does this give any new bound on \(S(n)\), any consequence for `SORT-BOUND-U`, or any certificate-completeness result. Its precise content is that the sound leaf-count bound is not uniformly within one comparison at height two, so pruning or certificate heuristics assuming that slack are unsound.

I posted this once to board #301 under the front author. No repository or Lean changes were made; the worktree remains clean at `6a96398`.

## Output 471 (msg_1c09e0c1a001EMm28r8bwMDoGe)

**Recovery inspection complete. No external action was repeated.**

- **Host / repository:** `billy-dev`; worktree clean at `6a96398`; no commits, stashes, or repository/Lean changes.
- **Board #301:** exactly **one** front post exists, timestamped `2026-11-09T14:00:44.962Z`, author `SoringP1 frontier: height-two-information-excess-bound`. No duplicate was posted. The only other hit is the earlier Viche Executive pre-dispatch.
- **Durable ledger:** `height-two-information-excess-bound` remains `status: running` with no recorded finding. That is keeper-managed; I did not edit it.
- **Scratch artifacts:** only under `/tmp/opencode/h2` and `/tmp/opencode/recovery_board.txt`, outside the repository.

**Effects that actually happened**

1. The mathematical counterexample and its limits were posted once to #301.
2. No repository, Lean, commit, PR, or other external change was made.

**Result already delivered, not rerun**

The height-two bound is false: for \(P=A_{12}\oplus A_{12}\), exact extension counting gives \(\lceil\log_2 e(P)\rceil=58\), and ordinal-sum additivity plus the published \(S(12)=30\) gives \(F(P)=60\), so the excess is \(2\). This refutes the bound “at most 1”; it does not establish unbounded height-two excess, and it gives no new \(S(n)\) or `SORT-BOUND-U` result.

No unfinished mathematical or external work remains.
