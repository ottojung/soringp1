# antonina-P35sJkT5Aje5pXXfiPH3go-continues

Session: ses_e3ee4d419ffeXRRo1BIuFMRVoR
Workspace: /home/lubko/soring-fronts/merge-block-ratio-alln-inequality
Created: 1794241145925; updated: 1794250229767

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1c11b2e750017gRF37jG1jz7xK)

I'll start by studying the repository context and the board.

## Output 1040 (msg_1c1a591ff001ln7KCjhdKdsPiV)

**Verdict: the all-`n` inequality is still open.** I found no counterexample, but I also did not prove it. This is not a proof of the front, and no complexity-class conclusion follows. One concise update was posted to board #301; there are no repo or Lean changes, and the worktree remains clean at `6a96398`.

**New exact finite results**

- I independently reproduced the exhaustive `n≤9` theorem with a C++/nauty implementation. It visits all `183231` unlabelled 9-element posets in about 20 s, obtains `S(9)=19`, and confirms
  \[
  \max_{|B|=9} R(B)=0.1363776466287995<C=0.13663867554893516
  \]
  at the same dual pair, with `e=181`, `F=9`, `covers=9`, denominator `11`.
- I enumerated a substantial high-risk part of `n=10`: all one-point extensions with denominator `≤22` of the `112` nine-element blocks with `F−log₂e>1.8`, plus all extensions of the `20` highest-ratio nine-element blocks. A sound greedy decision-tree upper bound reduced `12562` extensions to `46` hard candidates; I computed exact minimax for all of them. The largest exact value is only
  \[
  R=0.1025065975
  \]
  with `F=10`, `e=306`, `covers=14`, `(m,M)=(3,1)`, denominator `17`. So no counterexample exists in this tested `n=10` family.

**Structural finding: where ordinal composition could raise the ratio**

For nonempty posets `A,D`, ordinal additivity gives
\[
R(A\oplus D)=\frac{\alpha_A+\alpha_D}{d_A+d_D+\Delta},
\]
where `α=F−log₂e`, `d=covers+Mm`, and
\[
\Delta=(M_A-M_D)(m_D-m_A).
\]
If `R(A),R(D)≤C` and `Δ≥0`, then `R(A\oplus D)≤C`. Therefore ordinal composition can only raise the ratio when `Δ<0`, i.e. when one block dominates the other in both maximal and minimal counts. I exhaustively checked all pairs of blocks of size `3..9` with total size `≤14`: zero pairs exceed `C`. This isolates the only algebraic route by which the fixed-block supremum could rise, but does not close it.

**Concrete failed approaches / exact obstruction**

- An early grid calculation used successor masks that were not transitively closed and produced a spurious `R=0.2098`; after closure the same grid has `R=0.0848`.
- A multiway-merge recursion that compares only current chain heads is invalid for this model. It gives `F=n−1` for one isolated key plus an `(n−1)`-chain, while the true insertion cost is `ceil(log₂n)`; its apparent ratios above `0.4` are artifacts.
- A full `n=10` exhaustive DP was attempted twice and killed near `1.3M` of the `1.59M` classes. That is a resource failure, not a mathematical no-go; the full `n=10` space is not closed here.

**Scope**

`ceil(log₂e(P))` remains only a sound leaf-count lower bound; `R` measures its incompleteness, not a certificate of optimality. The SUPI literature (Fredman; Kahn–Saks; Kahn–Kim; Cardinal et al.) gives constant-factor approximations to `log₂e(P)`, not exact `F(P)`, and none of those general-poset results implies this all-`n` inequality.

Honest limit: the all-`n` claim is neither proved nor refuted. The results above are exact finite computations plus one exact algebraic reduction lemma; they are evidence and a narrowed search frontier, not a proof.
