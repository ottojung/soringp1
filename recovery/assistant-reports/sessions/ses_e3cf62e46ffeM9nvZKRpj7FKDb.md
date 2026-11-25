# antonina-5ZeCb0PQT0ht5MRvJP0Zq2-suction

Session: ses_e3cf62e46ffeM9nvZKRpj7FKDb
Workspace: /home/lubko/soring-fronts/prime-excess-vs-antichain-gap
Created: 1794273563149; updated: 1794274189820

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 330 (msg_1c313418b001x0w114t3MFFkgM)

## Finding: the front conjecture is **false**

**Recovery check first.** Host `billy-dev`; worktree clean at `6a96398`; no prior #301 post for this front, so nothing was duplicated. Exactly one board comment was posted at `2026-11-10T01:29:30Z`. No repository, Lean, commit, or PR changes. Scratch is only under `/tmp/opencode/prime_excess_gap`.

### Counterexample

Let  
\[
P=(A_{17}\oplus A_3)\setminus\{(a_0,b_0)\},
\]
i.e. all cross relations \(a_i<b_j\) hold except \(a_0<b_0\). Then \(|P|=20\), \(\operatorname{height}(P)=2\).

**Prime.** The comparability graph is \(K_{17,3}\) minus one edge, hence connected, so \(P\) is not a disjoint union. The incomparability graph is \(K_{17}\sqcup K_3\) plus exactly the edge \(a_0b_0\), hence connected, so \(P\) is not an ordinal sum. Thus \(P\) is series- and parallel-indecomposable.

**Extension count.** Deleting \(a_0<b_0\) adds exactly the extensions
\[
A\setminus\{a_0\}<b_0<a_0<B\setminus\{b_0\},
\]
so
\[
e(P)=17!\,3!+16!\,2!=104\cdot16!
=2{,}175{,}970{,}148{,}352{,}000.
\]
Thus
\[
\lceil\log_2 e(P)\rceil=51,
\]
since \(2^{50}<e(P)<2^{51}\). Two independent extension counters agree.

**Minimax lower bound.** Adding back \(a_0<b_0\) gives
\[
K=A_{17}\oplus A_3,
\]
so
\[
F(K)=S(17)+S(3)=50+3=53.
\]
Because \(L(K)\subseteq L(P)\), \(F(P)\ge F(K)=53\). Therefore
\[
F(P)-\lceil\log_2 e(P)\rceil\ge 53-51=2.
\]

**Global gap.** The information bound gives \(\lceil\log_2 20!\rceil=62\), and the explicit Ford–Johnson bound gives the matching upper bound \(M(20)=62\). Hence \(S(20)=62\) and
\[
E(20)=S(20)-\lceil\log_2 20!\rceil=0.
\]
The claimed bound would be \(E(20)+1=1\), but \(P\) has excess at least \(2\). **The all-\(n\) claim is refuted.**

### Meaning and limits

- This is a genuine prime-state counterexample: local excess at an indecomposable poset can exceed the antichain gap \(E(n)\). Thus \(E(n)\)-based pruning or “prime excess is controlled by \(E\)” heuristics are unsound in general.
- It is **not** an all-\(n\) lower bound, not a statement about \(S(n)\) itself, and not a certificate-completeness theorem. The bound \(\lceil\log_2 e(P)\rceil\) remains a sound lower bound; what fails is the claimed completeness/control by \(E\).
- Exact \(F(P)\) was not computed; only \(53\le F(P)\le S(20)=62\). The lower bound is enough.
- The argument uses the published exact value \(S(17)=50\) (Stober–Weiss, ALENEX 2023, arXiv:2206.05597) and ordinal-sum additivity.
- No complexity-class consequence for `SORT-BOUND-U` follows from this general-poset counterexample.
