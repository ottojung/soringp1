# antonina-8OW0mOdYM2wgXHCgTBOqAN-aggravate

Session: ses_e3ecb2915ffewzomQMo0T6omvx
Workspace: /home/lubko/soring-fronts/height-two-excess-unbounded
Created: 1794242828090; updated: 1794246191588

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 919 (msg_1c167422d0012RCN1BWO2s4Hj3)

**Mathematical finding (posted to board #301 as `height-two-excess-unbounded`).**

Let  
\[
H(n)=\sup\{F(P)-\lceil\log_2 e(P)\rceil : P\text{ has height }\le 2,\ |P|=n\}.
\]

1. **Exact reduction to the open excess \(E(n)\).**  
   For the one-edge state \(P_n=C_2\sqcup A_{n-2}\),
   \[
   e(P_n)=n!/2,\qquad F(P_n)=S(n)-1,
   \]
   so
   \[
   F(P_n)-\lceil\log_2 e(P_n)\rceil
   =S(n)-1-(C(n)-1)=E(n).
   \]
   Hence
   \[
   H(n)\ge E(n)\quad\text{for all }n.
   \]
   Therefore **any uniform height-two bound would prove \(E(n)\) bounded**—a major open sorting-theory statement.

2. **All-\(n\) upper sandwich.**  
   For height-two \(P\) on \(n\) elements with \(t\) comparable cross pairs, the board’s height-two extension lemma \(e(P)\ge n!/2^t\) and \(F(P)\le S(n)\) give
   \[
   F(P)-\lceil\log_2 e(P)\rceil \le E(n)+t+1.
   \]
   Thus the defect is controlled by \(E(n)\) plus the number of known relations, but this is not a constant bound.

3. **New exact excess-3 witness at \(n=27\).**  
   For complete bipartite \(K_{a,b}=A_a\oplus A_b\),
   \[
   e=a!b!,\quad F=S(a)+S(b),\quad
   \text{excess}=E(a)+E(b)+\delta,\ \delta\in\{0,1\}.
   \]
   Using \(S(13)=34,S(14)=38\):
   \[
   K_{13,14}:\quad n=27,\ C=69,\ F=72,\ \text{excess}=3.
   \]
   So excess 3 already appears at \(n=27\), not only at \(K_{14,14}\) (\(n=28\)). This is exact arithmetic, not unboundedness.

4. **Failed amplification attempts.**  
   - Ordinal sums add \(F\) and multiply \(e\), but add heights, so height two permits only two antichain factors.
   - Disjoint unions preserve height but introduce a multinomial interleaving term whose leading cost must also be paid by any sorter; exact small unions gave excess only 0 or 1.
   - Removing relations from \(K_{a,b}\) lowered excess in every checked case.
   - Matching states \(M_k=kC_2\) had excess 0 for \(k\le4\), consistent with their excess tracking \(E(2k)\).
   - One-relation states reproduce exactly \(E(n)\).

5. **Precise obstruction.**  
   The data are consistent with the endpoint conjecture
   \[
   H(n)\le \max\!\Big(E(n),\ \max_{a+b=n}(E(a)+E(b)+1)\Big),
   \]
   but I did **not** prove it. The missing step is a height-two merge lemma after sorting the two antichain layers. Such a lemma is false for unrestricted two-chain merging; the one-relation family shows why the naive layer-sort-then-merge proof fails—cross comparisons absorb the merge excess.  
   Consequently, to disprove the bounded hypothesis one must either prove \(E(n)\) unbounded, or exhibit a genuinely new height-two amplification with
   \[
   F(P)-\lceil\log_2 e(P)\rceil\ge 4
   \]
   at an \(n\) where \(E(n)\le1\). No such construction was found; complete-bipartite families cannot produce it from the known \(E\) values.

No infinite unbounded family and no uniform bound were established. No repository or Lean changes were made.

## Output 985 (msg_1c16810b3001xwGR9RW0NFUnLv)

**Recovery audit completed — no repeated side effects.**

- **Host:** `billy-dev`.
- **Working directory:** `/home/lubko/soring-fronts/height-two-excess-unbounded`.
- **Git state:** clean at `6a96398`; no commits, edits, or new repository files from the interrupted turn.
- **Board effect:** exactly **one** #301 post exists for `height-two-excess-unbounded`, timestamped `2026-11-09T17:41:58.682Z`. I did not post again.
- **Durable record:** `~/.local/state/soringp1/frontier-ledger.json` still lists the front as `status: running`. I left it untouched; that state is managed by the keeper/Executive, not by rewriting the ledger from the research turn.
- **Scratch artifacts:** confined to `/tmp/opencode/h2` and `/tmp/opencode/h2lit`; they are not repository effects.

The research deliverable from the previous turn is complete as posted: the exact reduction \(H(n)\ge E(n)\), the bound \(H(n)\le E(n)+t+1\), the \(K_{13,14}\) excess-3 witness at \(n=27\), and the stated obstruction that the unbounded horn requires either unbounded \(E(n)\) or a new height-two amplification mechanism. No unfinished external action remains.
