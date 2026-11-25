# antonina-7Sa2lCXTatA27VhWXusS3M-telling

Session: ses_e52dd8cb1ffevS4pS4wsPb37EH
Workspace: /home/lubko/soring301
Created: 1793906078560; updated: 1793906117310

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad227389001h91I0ELX9TzRKx)

I’ll inspect the two research notes and the model/literature pointers, then formulate and falsify a specific potential against the available exact data. I’ll keep this to scratch/paper work and make no repository edits.

## Output 27 (msg_1ad22883c001ssSqtQx4l2306u)

The key constraint is that the witness is a *partial-information state*, while the desired bound is at the antichain root. A potential must therefore be monotone under every adversarial branch and its accumulated per-query cost must telescope; simply transplanting the witness’s one-ply gap would not do that.

## Output 61 (msg_1ad22bf94001Z5P57Ded1Ds1Qt)

**Result: a natural weighted-adversary potential has an exact, simple one-comparison inequality—but it cannot strengthen the root information bound.** Its failure is structural, not a small-instance anomaly. The \(n=12\) witness does not, by itself, yield a root-antichain improvement through this potential.

### Candidate potential and inequality

For any poset \(P\), let \(\mathcal L(P)\) be its linear extensions. Choose nonnegative weights \(w_\pi\) on \(\pi\in\mathcal L(P)\), with total mass \(W(P)=\sum_\pi w_\pi>0\), and define

\[
\Phi_w(P)=\log_2 W(P).
\]

For an incomparable pair \(q=\{i,j\}\), let \(W_0,W_1\) be the weights of extensions placing \(i<j\) and \(j<i\). Then \(W_0+W_1=W(P)\), so

\[
\max(W_0,W_1)\ge W(P)/2,
\qquad
1+\max(\Phi_w(P_0),\Phi_w(P_1))\ge \Phi_w(P).
\]

Thus an adversary choosing the heavier child loses at most one unit of potential per comparison. This is the standard weighted-leaf-counting adversary inequality in distribution form.

But at the antichain root, if the weights are fixed and each permutation is a distinct output, every decision tree’s leaves must distinguish all positive-weight permutations. The potential gives only \(\log_2|\operatorname{supp}(w)|\le\log_2(n!)\); for uniform weights it is exactly the ordinary information bound. Restricting support cannot improve it.

### Concrete falsifier: adaptive reweighting still collapses to leaf counting

A tempting upgrade is to choose a fresh distribution at each state, e.g. maximize \(\Phi(P)=\log_2 e(P)\), or some entropy/weighted analogue. For \(e(P)\), the one-ply recurrence is exactly the note’s \(L_1(P)\). At witness \(W=(26,0,10,0,8)\), its splits are \(5/3,5/3,6/2,6/2\), giving \(L_1(W)=4>L_0(W)=3\).

However, this gain is only **state-local**. To turn state-local gains into a root lower bound, they must be paid along every root-to-leaf path. The standard telescoping potential \(\log e(P)\) pays at most one per comparison and telescopes to \(\log(n!)\); it does not preserve the extra unit seen at \(W\). In particular, the witness is not a root-reachable obstruction that every sorting strategy must encounter: it is just one partial order. A root adversary may follow other branches.

This also explains why the one-ply bound cannot certify the requested infinite-family result: its only global guarantee at the antichain is \(L_1(\bot)\ge\lceil\log_2(n!)\rceil\), and the notes report equality through \(n=11\). At \(n=12\), the known \(+1\) comes from Wells’ exhaustive surviving-frontier argument, not from a scalar potential on extension counts.

### Exact-data test and conclusion

The available exact minimax reference is `scripts/evaluate.py`; it computes \(S(n)\), not the distributional witness statistic. For \(n\le8\), known values are \(S(n)=\lceil\log_2(n!)\rceil\) (with \(S(7)=13,S(8)=16\)). Therefore any proposed **all-\(n\)** root potential claiming a strict improvement already fails on these roots. The fixed-weight potential above passes its one-step inequality but fails the required strict-root test on all \(n\le8\).

**Conclusion (paper deduction):** additive nonnegative extension weights, including the uniform distribution and fixed weighted adversaries, cannot exceed leaf counting at the root. Adaptive reweighting can expose local one-ply gaps such as \(W\), but without a pathwise amortized credit that survives telescoping it does not lift to an antichain-root bound. A successful candidate would need a genuinely nonadditive, strategy-sensitive potential whose credits cannot be reset or escaped on other branches; the material inspected here supplies no such potential or infinite-family theorem. No edits, posts, or Lean work were made.
