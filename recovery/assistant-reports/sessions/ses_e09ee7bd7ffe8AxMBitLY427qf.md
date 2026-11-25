# antonina-Un5AMSP4ZaKlZQCJJHz6og-foci

Session: ses_e09ee7bd7ffe8AxMBitLY427qf
Workspace: /home/lubko/soring-fronts/ordered-block-optimal-play-gap-20261120
Created: 1795129705580; updated: 1795129819370

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f6118631001yfEocqvg1YfRPf)

I’ll first map the existing #301 finding against the current research plan, strategy notes, and ledger, then test only the stated ordered-block amplification route. I’ll leave the repository unchanged and won’t post unless there’s a genuinely new result.

## Output 181 (msg_1f612db15001NhH0x38PcHutmI)

## Finding: ordinal-sum additivity does not lift the gap

**Outcome (iii): this route is unsuitable without a new root-prefix lemma.** I found no uniform lifting proof, and the existing facts do not imply one.

The relevant objects are:

- \(L_{\mathrm{loc}}(n)\): states reachable from the \(n\)-antichain by queries locally minimax-optimal at every step:
  \[
  F(P_{i-1})=1+\max\{F(P_i),F(Q_i)\},
  \]
  where \(P_i\) is the chosen child and \(Q_i\) its sibling.
- \(L_{\mathrm{tree}}(n)\): states reachable on *some* sorting tree of height \(S(n)\). A path of depth \(d\) to \(P\), with sibling \(Q_i\) at its \(i\)-th comparison, is feasible exactly when
  \[
  R_h(P)=\max\!\left(d+F(P),\ \max_{1\le i\le d}\{i+F(Q_i)\}\right)\le S(n).
  \]
  Thus endpoint feasibility \(d+F(P)\le S(n)\) alone is insufficient.

The already-checked finite gap is \(|L_{\mathrm{tree}}\setminus L_{\mathrm{loc}}|=1{,}440\) at \(n=6\), and \(274{,}344\) at \(n=7\). These are independently verified on #301; the associated locally-minimax counts are \(65{,}551\) and \(2{,}769{,}663\), respectively. The board also records an \(n=5\) root-prefix obstruction: a \(C_2\oplus A_3\) endpoint has \(d+F(P)=S(5)=7\), yet its best transcript has sibling-inclusive \(R_h(P)=8\).

For a poset endpoint \(P=A\oplus B\), additivity does give \(F(P)=F(A)+F(B)\), and \(e(P)=e(A)e(B)\). In particular, adjoining a chain \(C_m\) gives \(F(A\oplus C_m)=F(A)\) and \(e(A\oplus C_m)=e(A)\). But this is an **endpoint identity**, not an embedding of a root path. The ambient root is the \((n+m)\)-antichain, not \(A\oplus C_m\); reaching that endpoint requires a transcript whose *every sibling* meets the enlarged root budget. Additivity for the endpoint gives no bounds on those sibling costs, nor does it show the original witness path or its locally minimax failure survives.

The attempted generalization also has a concrete warning in the series-decomposition notes: direct-sum additivity is for the full product of independent extension sets. For two 2-element antichains, the full product has value \(2\), while the correlated two-permutation subset \(\{0123,1032\}\) has value \(1\), despite each block projection having value \(1\). This is not itself a root-path counterexample, but it refutes the shortcut of applying product additivity to transcript-conditioned blocks. The ledger’s `root-composition-exact-recurrence` investigation identifies the same missing requirement: preserve root reachability and both sibling branches, not merely the endpoint’s \(F\).

**Uncertainty:** this does not disprove every possible ordered-block embedding. It shows that ordinal-sum additivity and extension-count factorization alone cannot establish one; a successful lift still needs a uniform transcript construction and sibling-budget proof for every \(m\). I made no repository changes and did not post to #301.
