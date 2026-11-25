# antonina-MuP4OV7XTLicnloi8yM69o-wail

Session: ses_e3ecb332effeJ4fufW6aPGyjHh
Workspace: /home/lubko/soring-fronts/universal-local-excess-cover-ratio
Created: 1794242825497; updated: 1794247305277

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 1127 (msg_1c17864c7001Zist4QOEJEzaz0)

**Outcome: no counterexample found; the inequality is exactly attained at infinitely many sizes. All-`n` remains open. No repo or Lean changes.**

I studied `AGENTS.md`, `docs/problem.md`, the relevant series-decomposition notes, and board #301, then posted the result to #301. The worktree remains clean at `6a96398`.

### Main mathematical finding

Let \(A=\operatorname{Merge}(2,4)\) and \(P_k=A^{\oplus k}\), the ordinal sum of \(k\) copies. Then for every \(k\ge 1\):

\[
e(P_k)=15^k,\quad F(P_k)=5k,\quad \operatorname{covers}(P_k)=8k-4,
\]
\[
M(P_k)=m(P_k)=2,\quad \operatorname{covers}+Mm=8k.
\]

Therefore

\[
\frac{F(P_k)-\log_2 e(P_k)}{\operatorname{covers}(P_k)+M(P_k)m(P_k)}
=
\frac{k(5-\log_2 15)}{8k}
=
\frac{5-\log_2 15}{8}
=
0.13663867554893516\ldots
\]

for **every** \(k\). This is equality, not a limit. The earlier board normalization used \(\lceil k\log_2 e_B\rceil\), which obscured the real-log equality.

Consequence: the constant is sharp at \(n=6,12,18,\ldots\). A strict-inequality strengthening is impossible; a falsifier must strictly exceed this already-attained value.

### Reduction and finite checks

Writing \(w(B)=F(B)-\log_2 e(B)-C\cdot\operatorname{covers}(B)\), an ordinal sum has denominator

\[
D(B_1\oplus\cdots\oplus B_k)
=
\sum_i \operatorname{covers}(B_i)
+
\sum_i M(B_i)m(B_{i+1})
+
M(B_k)m(B_1).
\]

Thus the inequality is a no-positive-cycle statement in the graph of \((m,M)\)-types. Using the board’s exhaustive \(n\le 9\) class data, Bellman–Ford finds **no positive cycle**. Hence any counterexample must contain an ordinally indecomposable block of size at least \(10\).

Two exact corollaries:

- If \(P\) has unique min and max, then \(P=C_1\oplus Q\oplus C_1\), so \(F(P)=F(Q)\), \(e(P)=e(Q)\), and
  \[
  w(P)=w(Q)-C(m(Q)+M(Q)).
  \]
  Exhaustive \(n=8\) interiors give maximum \(-0.002871318121\); exhaustive \(n=9\) interiors give \(-0.071947946262\). Therefore no \(10\)- or \(11\)-element poset with unique min and max violates the bound.
- For the lowest-threshold core type \((m,M)=(2,2)\), the cycle threshold is \(0.546554702196\). Exact minimax over all \(n=10\) \((2,2)\)-blocks with \(\operatorname{covers}\le 9\) gives maximum \(w=0.424846673\), below threshold.

### Failed approach

A first nauty bipartite canonicalizer was **not injective** — it produced only \(6{,}341\) distinct keys for \(16{,}999\) \(n=8\) posets — and silently corrupted exact \(F\). It was discarded; the exact \(n=10\) slice uses the refined \(S_n\) canonical form instead.

### Honest limits and soundness distinction

- The all-\(B\) inequality is **not proved**.
- No \(n\ge 10\) series-prime counterexample was found.
- The obstruction is now narrow: a counterexample must be a series-prime core of size at least \(10\) with \(m,M\ge 2\); the first target is group \((2,2)\) with \(\operatorname{covers}\ge 10\).
- \(C(P)=\lceil\log_2 e(P)\rceil\) is a sound lower bound, not a complete certificate. General-poset SUPI bounds do not transfer to the antichain root \(S(n)\), and none of this gives a complexity-class consequence for `SORT-BOUND-U`.

## Output 1184 (msg_1c179132b001uvrLzCQBg2PF1C)

Recovery check completed. No duplicate actions taken.

**Verified effects from the interrupted turn**

- **Board #301:** the comment from `SoringP1 frontier: universal-local-excess-cover-ratio` exists exactly once, timestamped `2026-11-09T18:00:40.131Z`. The digest confirms one matching post, so it was **not** reposted.
- **Git:** worktree is clean at `6a96398`; no commits, branches, or repository edits were made.
- **Scratch:** durable artifacts remain under `/tmp/opencode/blockratio/`, including `board_post.md` and the saved board response. No background computations from this front are still running.
- **Lean/repository:** no Lean files or repo changes were created, matching the stated publication-gate decision.

**Unfinished work**

None for this front. The mathematical report, exact computations, failed-approach note, and board update were already delivered. The all-`n` inequality remains open, and the precise next target is a series-prime counterexample in group `(2,2)` with `covers >= 10`.

No uncertain external effect remains except the standard caveat that the full `board_post_result.json` is a large board snapshot; the dedicated digest independently confirms the single new comment.
