# antonina-4AZsRZTNMwfQXZV3bloDi3-berg

Session: ses_e3e928d1fffejWqfd7I1zzbh8w
Workspace: /home/lubko/soring-fronts/height-two-excess-split-bound
Created: 1794246538055; updated: 1794256979776

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 963 (msg_1c20ca291001DV4IdFvd7gq3x4)

Recovery inspection complete. I did not repeat the original prompt or duplicate any external action.

**State verified**
- Host `billy-dev`; worktree clean at `6a96398`; no commits, repository edits, or Lean changes.
- Board #301 already contained my earlier 19:29Z counterexample post and a 19:53Z Viche verification. I posted exactly **one** new correction at 20:42Z; no duplicate was made.

**Mathematical outcome**

The proposed height-two split bound is still **open**. The attempted \(n=11\) counterexample
\[
P=(A_3\oplus A_6)\sqcup A_2
\]
does have
\[
e(P)=475\,200,\quad \lceil\log_2 e(P)\rceil=19,\quad I(9,2)=8,
\]
and therefore the sound upper bound \(F(P)\le 13+8=21\), giving excess at most \(2\) versus the claimed RHS \(1\).

However, the lower bound \(F(P)\ge 21\) used the decomposition
\[
F(K\sqcup A_s)=F(K)+I(|K|,s),
\]
and that identity is **false**. Isolated elements can act as comparison pivots: learning \(k_1<x<k_2\) orders \(k_1,k_2\), so comparisons involving an isolated element are not independent of sorting \(K\).

**Explicit disproof of the decomposition**
\[
K=A_1\oplus A_3,\qquad s=1.
\]
Then
\[
F(K)=S(1)+S(3)=3,\qquad I(4,1)=\lceil\log_2 5\rceil=3,
\]
but exact flat minimax gives
\[
F(K\sqcup A_1)=5<6.
\]
The same phenomenon occurs for \(s=2\): \(F=8<9\). This is a concrete failed approach/exact obstruction, not a new counterexample to the split bound.

**Honest limits**
- The \(n=11\) witness only supplies the upper bound \(F(P)\le21\); its actual excess is either \(1\) or \(2\).
- A direct flat \(n=11\) minimax exceeded the local time/memory budget.
- The all-\(n\) split bound remains open; no valid counterexample and no proof were produced.
- No Lean or repository changes were justified.
