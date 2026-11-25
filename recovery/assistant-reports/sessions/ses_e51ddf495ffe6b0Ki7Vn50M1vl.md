# antonina-3Dtx6sJH0Qc32UaVA1Dpps-somewhere

Session: ses_e51ddf495ffe6b0Ki7Vn50M1vl
Workspace: /home/lubko/soring-fronts/parallel-reversal-congruence-20261106
Created: 1793922829191; updated: 1793922858758

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ae220baa001LRgM3E8sc3ImEN)

I’ll first check the research note and operations guidance for an active owner of this exact conjecture. If it’s unowned, I’ll work from the precise model and try to establish either an adaptive-tree proof or a directly checkable counterexample, without changing repository files.

## Output 55 (msg_1ae224e3b001nKTU86pmie7ks5)

**Result: paper proof of the general equality; no counterexample found or claimed.** The conjecture in `docs/research-parallel-duality.md` holds for arbitrary finite posets \(A,B\), including when both are non-selfdual.

Let \(L(A\mathbin{\|}B)\) be the linear extensions of the disjoint union. Define a bijection to \(L(A\mathbin{\|}B^{op})\) by keeping the \(A\)-elements in their positions and reversing the order of the \(B\)-elements in the positions occupied by \(B\). This preserves the relative order of every cross-component pair, preserves comparisons within \(A\), and reverses comparisons within \(B\). Thus, for any fixed pairwise comparison, its outcome is either preserved for every extension or swapped for every extension.

Take any adaptive comparison tree for \(A\mathbin{\|}B\). Use the same comparison at each corresponding node for \(A\mathbin{\|}B^{op}\); when the comparison is within \(B\), swap its two child branches. The bijection ensures this tree identifies the transformed linear extension and has the same height. Applying the construction in reverse gives the opposite inequality, so
\[
F(A\mathbin{\|}B)=F(A\mathbin{\|}B^{op}).
\]
By global order-duality invariance, \(F(A^{op}\mathbin{\|}B)=F(A\mathbin{\|}B^{op})\). Therefore \(F(A^{op}\mathbin{\|}B)=F(A\mathbin{\|}B)\).

The argument concerns the full adaptive tree, not the component-reversal orbit quotient or transition equivalence; it makes no inference from transition failure.

**Sources and check.** The exact minimax and linear-extension model is in `docs/research-parallel-duality.md` §§1–2; its §3 records the candidate extension bijection. Global order-duality invariance is Theorem 3 in `docs/research-compression-next.md` (§ around line 87). The proof above supplies the missing adaptive-tree correspondence directly. As an independent finite check, one can enumerate compatible permutations for each disjoint-union pair, compute \(F\) by the full minimax recurrence on the resulting comparison partitions, and compare the two values. The note reports such evidence through \(n\le7\), but the proof—not that bounded search—establishes the all-finite-posets claim. No repository edits or external posts were made.
