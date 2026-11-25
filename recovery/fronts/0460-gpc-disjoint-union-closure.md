# gpc-disjoint-union-closure

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ESYe4tsgZDuYHh0eLaR7I7-flopped

## exit_state

clearexit

## question

For all finite posets A and B that each satisfy the Gold Partition Conjecture, does their disjoint union A disjoint-union B also satisfy GPC, i.e. does A disjoint-union B have two consecutive comparisons with t0 >= t1+t2 regardless of the outcomes of those comparisons?

## basis

Board #301 2026-11-09T18:46Z and 12:28Z GPC/Fibonacci posts; Dolores-Cuenca, Guzman-Saenz and Kim, Order 43 (2026), prove preservation for lexicographic sums only; Peczarski, Order 23 (2006), supplies the GPC definition and known classes; the disjoint-union count e(A disjoint-union B)=binom(|A|+|B|,|A|)e(A)e(B) makes closure non-obvious, and no ledger front tests it.

## falsifier

Exhibit finite GPC-satisfying posets A and B whose disjoint union violates t0 >= t1+t2 for every admissible choice of two consecutive comparisons, with exact linear-extension counts for A, B, A disjoint-union B and every comparison branch.

## implication

A positive answer would add disjoint union to the known GPC closure operations beyond lexicographic sums and would extend the sound Fibonacci threshold to a broad compositional class; a counterexample would identify the first standard composition operation under which GPC fails.

## finding_unverified

ase case. This is implicit in the paper’s Corollary 1 and scaling proof, so I do not claim it as a deep new theorem.

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

## Other metadata

```json
{
  "finished_at": 1794254385.6216295,
  "started_at": 1794252609.4790103
}
```
