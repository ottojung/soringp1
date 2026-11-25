# antonina-8a59JFfP8tLMw8tuSTEdNm-conqueror

Session: ses_e5291b936ffezbc2EkxNBKmr1G
Workspace: /home/lubko/soring-fronts/average-redundancy-lower-bound-20261024
Created: 1793911047885; updated: 1793911075856

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad6e46ec001zSLUjuCWqYofpn)

I’ll first inspect the project’s model/literature notes and existing n=12 results, then pursue a scratch-only argument or a clearly scoped obstruction. I’ll avoid integrating files or inferring a root bound from a single reached poset.

## Output 38 (msg_1ad6e673d001ByFT30ynHo7Zy0)

**Result: a precise no-go for conserved additive history-sensitive potentials.** This does not give a new lower bound for sorting; it identifies why a broad additive-potential approach cannot certify the known \(n=12\) obstruction.

**Definition — potential family.** At each history \(H\), assign nonnegative weights \(w_H(\pi)\) to the linear extensions \(\pi\) still consistent with that history. Require:

1. At a terminal history, the total weight is at most \(1\).
2. For every comparison, the two sibling histories \(H_0,H_1\) partition the parent’s extensions, and each extension keeps its weight in its corresponding child. Thus
   \[
   \Phi(H)=\sum_\pi w_H(\pi)=\Phi(H_0)+\Phi(H_1).
   \]

Weights may depend on the selected comparison history; they need not be uniform across permutations.

**Theorem — two-sibling bound.** If every leaf of a strategy subtree has remaining depth at most \(r\), then its root potential is at most \(2^r\).

*Proof.* Induct on \(r\). At depth zero the root is terminal, so its potential is at most \(1\). Otherwise, the two children have remaining depth at most \(r-1\). By conservation and the induction hypothesis,
\[
\Phi(H)=\Phi(H_0)+\Phi(H_1)\le 2^{r-1}+2^{r-1}=2^r.
\]
This applies to every strategy, including adaptive strategies and histories that select different queries. ∎

At the antichain, unit weight per permutation gives \(\Phi= n!\), so this family yields only \(n!\le 2^r\), the information bound. In particular, at \(n=12\), \(12!=479{,}001{,}600<2^{29}=536{,}870{,}912\): the potential cannot rule out 29 comparisons. **It does not falsify** \(S(12)=30\); Wells’ exhaustive result, also reported by Peczarski and Stober–Weiß, establishes that obstruction by a different method.

**Scope of the obstruction.** The theorem rules out potentials with sibling-conserved extension weights and terminal capacity at most one. It does not rule out potentials that are nonadditive, change weights across histories, or score a whole strategy subtree. A subtree potential could simply encode the full minimax recurrence, but absent a tractable independently proved invariant that would restate the original problem rather than provide a new certificate.

**Status:** the theorem above is a paper proof for the defined family. No new root lower bound or computational reproduction of the \(n=12\) search is claimed. Scratch-only; no files changed.
