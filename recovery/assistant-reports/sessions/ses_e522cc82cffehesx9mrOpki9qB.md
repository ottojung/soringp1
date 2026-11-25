# antonina-N8xkQQs3KEgyaQlpmnjkG4-chin

Session: ses_e522cc82cffehesx9mrOpki9qB
Workspace: /home/lubko/soring-fronts/parallel-reversal-congruence-20261106
Created: 1793917663191; updated: 1793917685345

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 42 (msg_1add36ab2001At51TuEB54wtBO)

I found no counterexample. The proposed reversal of the \(B\)-subsequence does **not** by itself provide the required decision-tree transport.

For each linear extension of \(A\parallel B\), reverse the relative order of its \(B\)-elements and leave the \(A\)-subsequence fixed. This is a bijection onto the extensions of \(A\parallel B^{op}\). But a cross-component query \((a,b)\), with \(a\in A\), \(b\in B\), is answered by whether \(a\) occurs before \(b\). Reversing only the \(B\)-subsequence does not generally preserve that answer or turn it into its complement: the position of \(a\) relative to the reversed \(B\)-subsequence can change in either direction. Thus the bijection does not map each query’s two answer blocks to the blocks of a fixed query in the target problem. That is the precise obstacle to using it recursively to transport decision trees.

The global-duality argument in `docs/research-compression-next.md` proves the target identity when \(B\) is self-dual, but does not settle the arbitrary case. The note’s exhaustive checks through \(n\le7\) are evidence, not proof. I did not produce a larger exact minimax counterexample or an all-size proof.

**Strongest justified result:** \(F(A^{op}\parallel B)=F(A\parallel B)\) when \(B^{op}\cong B\), by global order-duality invariance and relabelling invariance; the arbitrary finite-poset case remains unresolved here. No files, commits, or board actions were made.
