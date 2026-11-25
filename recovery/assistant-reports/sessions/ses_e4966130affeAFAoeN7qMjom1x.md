# antonina-FAZZzj0sKjzgTb9HaGbHIH-unions

Session: ses_e4966130affeAFAoeN7qMjom1x
Workspace: /home/lubko/soring-fronts/exec-arbitrary-merge-tree-gap-20261107
Created: 1794064903471; updated: 1794065330679

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 29 (msg_1b69a18ca001qLYVnTrMNBWBTg)

**The obstruction is valid** for every fixed binary merge tree under the stated standard head-to-head merge rule. It does not extend to arbitrary merge decision trees or other sorting algorithms.

Let each node’s run be the sorted sequence of keys in its subtree. At an internal node with child runs \(A\) and \(B\), standard merging uses exactly \(a+b-1\) comparisons when the final two keys in the merged order come from different children: it compares those two keys, emits one, and the other run is then empty.

These worst cases are simultaneously attainable. Construct a compatible order recursively. For a leaf, its sequence is its sole key. At an internal node, take the recursively constructed sequences for its children, interleave their prefixes in any order that preserves each prefix’s order, then append the maximum of \(A\) followed by the maximum of \(B\). This preserves both child sequences, and the node’s final two keys come from different children. Thus every internal merge attains \(a+b-1\) on this one global input order.

Consequently the architecture’s worst-case cost is exactly
\[
C(T)=\sum_{v}(a_v+b_v-1).
\]
Each leaf key is counted once for each ancestor, so \(\sum_v(a_v+b_v)=\sum_i d_i\), where \(d_i\) is leaf \(i\)’s depth. A binary tree with \(n\) leaves has \(n-1\) internal nodes, giving
\[
C(T)=\sum_i d_i-(n-1).
\]
By Kraft’s inequality, \(\sum_i2^{-d_i}\le1\); Jensen’s inequality then gives \(\frac1n\sum_i d_i\ge\log_2 n\). Hence
\[
C(T)\ge n\log_2 n-n+1.
\]

Writing \(L(n)=\lceil\log_2(n!)\rceil\), Stirling’s formula gives
\[
\log_2(n!)=n\log_2 n-(\log_2 e)n+\tfrac12\log_2 n+O(1).
\]
Therefore
\[
C(T)-L(n)\ge(\log_2 e-1)n-\tfrac12\log_2 n+O(1),
\]
so the gap is at least \((\log_2 e-1)n-O(\log n)\). Sergeev’s Theorem 3, as cited in the repository’s `docs/research-sergeev-asymptotic.md`, gives \(S(n)-L(n)=o(n)\). Since \(\log_2 e-1>0\), every such architecture is strictly nonoptimal for all sufficiently large \(n\).

**Scope:** This rules out fixed binary merge architectures using the specified linear merge as a way to attain \(S(n)\) for all sufficiently large \(n\), regardless of tree shape. It does not rule out optimal arbitrary merge decision trees, adaptive interleaving across unfinished subproblems, or sorting algorithms outside this model.

## Output 172 (msg_1b69e5394001GUQPduq0TuN9Be)

**Recovery/state audit**

- Conversation: the prior turn already produced the complete mathematical audit; it was not interrupted mid-computation.
- Worktree: clean, no modified/untracked files, detached at `c865b23`; no commits, merges, PRs, or source edits were made.
- Board #301: the newest relevant message is the 15:22 assignment of this managed researcher. No result comment for this front exists yet. Nothing was duplicated.
- No GitHub, purchase, or other external action was attempted.

**Theorem verdict**

The proposed obstruction is **correct, within its stated model**. For any fixed binary merge tree whose internal nodes use the standard linear head-to-head merge:

1. **Simultaneous attainability holds.** Recursively construct each child run. At an internal node, interleave the two child sequences after removing their maxima, preserving each child order, then append `max(A)` and `max(B)`. This remains a valid global input order, and the final two survivors come from different children, so the merge performs exactly `a+b-1` comparisons. Thus one global permutation makes every internal merge worst-case.

2. **Cost accounting is exact.**
   \[
   C(T)=\sum_v(a_v+b_v-1)=\sum_i d_i-(n-1).
   \]

3. **Kraft/Jensen direction is correct.**
   \[
   \sum_i2^{-d_i}\le 1
   \quad\Longrightarrow\quad
   \frac1n\sum_i d_i\ge\log_2 n
   \quad\Longrightarrow\quad
   C(T)\ge n\log_2 n-n+1.
   \]

4. **Stirling and rounding are harmless.** With \(L(n)=\lceil\log_2(n!)\rceil\),
   \[
   C(T)-L(n)\ge(\log_2 e-1)n-O(\log n).
   \]

5. **Sergeev comparison is valid.** Since \(S(n)-L(n)=o(n)\) and \(\log_2 e-1>0\), every such architecture has \(C(T)>S(n)\) for all sufficiently large \(n\).

**Scope:** this excludes fixed binary merge-tree architectures using standard linear merging. It does **not** exclude optimal arbitrary merge decision trees, adaptive interleaving across unfinished subproblems, or general sorting algorithms.

No further external action was taken: since the board contains only the assignment and no result post, I did not risk posting a duplicate. The completed theorem check is the deliverable; any durable board comment can be issued once by the Executive/runner.
