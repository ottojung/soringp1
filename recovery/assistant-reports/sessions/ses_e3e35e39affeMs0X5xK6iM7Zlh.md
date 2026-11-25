# antonina-ESYe4tsgZDuYHh0eLaR7I7-flopped

Session: ses_e3e35e39affeMs0X5xK6iM7Zlh
Workspace: /home/lubko/soring-fronts/gpc-disjoint-union-closure
Created: 1794252610914; updated: 1794254372096

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 401 (msg_1c1e39411001U0yLDVnnhAf1lN)

**Finding: the falsifier cannot exist.** Disjoint union of GPC posets is GPC. In fact the stated front is already settled by the cited lexicographic-sum theorem, by two applications; the binomial counting formula is not even needed.

## Sources and exact definition

I used the GPC definition from Peczarski, *Order* 23 (2006) 89–95, and his restatement in *Contrib. Discrete Math.* 12 (2017) 106–109: for a non-chain \(P\), two consecutive comparisons must satisfy
\[
t_0 \ge t_1+t_2
\]
for every oracle answer, where \(t_0=e(P)\), \(t_1\) is the number of extensions after the first comparison, and \(t_2\) after both. The second comparison may depend on the first answer; the argument below works either way.

The cited paper is Dolores-Cuenca–Guzmán-Sáenz–Kim, *Order* 43 (2026), arXiv:2410.12494v2, Theorem 3 and Corollary 1.

## Proof 1: the front is a two-step lexicographic sum

Let \(A,B\) satisfy GPC. Start with the two-element antichain \(P=\{p,q\}\).

1. Replace \(p\) by \(A\):
\[
P\circ_p A=A\sqcup\{q\}.
\]
Theorem 3 has no hypothesis on the base \(P\) and only requires the substituted poset \(A\) to satisfy GPC. Hence \(A\sqcup\{q\}\) satisfies GPC.
2. Take \(P'=A\sqcup\{q\}\) and replace the point \(q\) by \(B\):
\[
P'\circ_q B=A\sqcup B.
\]
Again Theorem 3 applies because \(B\) satisfies GPC and \(P'\) is arbitrary. Hence \(A\sqcup B\) satisfies GPC.

So the proposed counterexample route is empty. Disjoint union is not a new composition operation outside the paper’s scope; it is two successive one-point lexicographic replacements.

## Proof 2: a slightly stronger factoring statement

For any lexicographic sum \(R=P(Q_1,\dots,Q_n)\), Corollary 1 gives
\[
e(R)=e\!\left(P(\langle |Q_1|\rangle,\dots,\langle |Q_n|\rangle)\right)\prod_j e(Q_j).
\]
A comparison \((x,y)\) inside one block \(Q_i\) changes only \(Q_i\), so
\[
e(R+xy)=e(\text{base})\,e(Q_i+xy)\prod_{j\ne i}e(Q_j),
\]
and likewise after the second comparison. If \(Q_i\) satisfies GPC, multiplying its inequality by the positive constant \(e(\text{base})\prod_{j\ne i}e(Q_j)\) proves the same inequality for \(R\), for both first outcomes.

Thus **one GPC block suffices** for an arbitrary lexicographic sum; the other blocks need not satisfy GPC. Disjoint union is the antichain-base case. This is implicit in the paper’s Corollary 1 and scaling proof, so I do not claim it as a deep new theorem.

## Exact count check

Take \(A=A_3\) (3-antichain, \(e=6\)) and \(B=C_3\) (3-chain, \(e=1\)). Then
\[
e(A\sqcup B)=\binom{6}{3}\cdot 6\cdot 1=120.
\]
Lift \(A\)’s witness: compare two elements of \(A\), giving
\[
t_1=20\cdot 3=60.
\]
In either branch compare one of them with the third \(A\)-element. The two possible second outcomes give
\[
t_2=40 \quad\text{or}\quad t_2=20.
\]
Hence \(120\ge 60+40\) and \(120\ge 60+20\). Direct subset DP reproduces all four counts \(120,60,40,20\) exactly.

## Falsification attempt

I exhaustively checked all pairs of unlabeled non-chain posets \(A,B\) with \(|A|,|B|\le 5\) (63 classes at \(n=5\)), using exact linear-extension DP and a depth-two GPC checker: **6,724 GPC pairs, zero counterexamples.** This is finite evidence only; the proof above is the actual result.

## Honest limits and complexity implication

- This is a closure observation, not a new exact \(S(n)\) bound or algorithm. The root relevant to \(S(n)\) is the antichain \(A_n\), already a disjoint union of antichains; the closure does not decompose its minimax tree.
- The GPC consequence \(F(P)\le \log_\phi e(P)\) is a golden-ratio bound, and the board’s `gpc-antichain-upper-bound-barrier` already shows it is weaker than Ford–Johnson for \(n\ge 4\). So this does not improve the unary complexity frontier.
- Extending the Fibonacci threshold \(e(P)\ge F_{m(P)+2}\) is conditional on the board’s GPC\(\to\)Fibonacci deduction via Peczarski’s Propositions 2–3; I did not independently re-prove that implication here.
- The statement is a sufficient closure condition, not a characterization. Whether \(A\sqcup B\) satisfying GPC implies that a summand satisfies GPC remains open and is not needed for the front.

I posted this finding to board #301. The repository worktree remains clean at `6a96398`; no Lean, test, script, or note was added.

## Output 482 (msg_1c1e4dd9c001SpZqbelEX7PH1b)

Recovery inspection complete. I did **not** repeat the research prompt or any external action.

**Effects that actually happened (verified):**
- Board #301 contains exactly one comment from `SoringP1 frontier: gpc-disjoint-union-closure`, timestamped `2026-11-09T19:57:47.911Z`. It was not duplicated.
- The repository worktree is clean on `billy-dev` at `6a96398`. No commits, branches, Lean files, tests, or notes were created.
- Scratch files remain only under `/tmp/opencode/gpcdu` (`board_post.md`, `check.py`, `check2.py`).
- The frontier ledger contains the entry `gpc-disjoint-union-closure` with `agent_id` and `started_at`, but no completion field was written by me.

**Mathematical outcome already recorded:**
- The falsifier is impossible: disjoint union of GPC posets is GPC.
- This follows by two applications of Dolores-Cuenca–Guzmán-Sáenz–Kim Theorem 3, replacing one antichain point by \(A\), then the other by \(B\).
- A stronger factoring argument shows one GPC block suffices for any lexicographic sum.
- Exact example: \(A_3\sqcup C_3\) has \(e=120\), with lifted counts \(t_1=60\), \(t_2\in\{20,40\}\), so \(120\ge 60+40\).
- Exhaustive finite check over all pairs of non-chain classes with sizes \(\le 5\) found no counterexample.
- No new \(S(n)\) complexity bound follows from this closure.

**Uncertain / left for review:** whether the external frontier ledger should be marked `investigated`. I deliberately did not edit it, to avoid inventing a completion record after the backend interruption.
