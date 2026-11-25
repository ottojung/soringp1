# antonina-bN6pimDH9Cn2qx14JN45Bu-dollars

Session: ses_e49c221b2ffeCPZOFnGaQG37s1
Workspace: /home/lubko/soring-fronts/exec-rutschmann-minimax-kernel-20261107
Created: 1794058870416; updated: 1794058910848

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 49 (msg_1b63e4a4a001PpsreLSJn4XgyJ)

The exact minimax value is **not preserved** by the paper’s shortcut map. The smallest counterexample is the 3-element poset \(0<1\), with \(2\) incomparable to both:

- Longest path: \(P=(0,1)\).
- Off-path vertex \(2\) has no predecessor or successor on \(P\), so \(Y=\{2\}\).
- \(H\) is the induced graph on \(Y\), with no added path edges.
- The exact recurrence gives \(F(G)=2\), while \(F(H)=3\).

This is hand-checkable from the recurrence: for \(G\), compare \(2\) with either endpoint first; the two resulting states have minimax value \(1\), so \(F(G)=2\). For \(H\), the three elements are an antichain. Every first comparison has a branch leaving a 2-element antichain, whose value is \(1\); hence \(F(H)=1+2=3\). No smaller counterexample is possible: for \(n\le2\), the shortcut cannot remove a vertex while leaving a nontrivial comparison problem.

**What the paper establishes:** Theorem 11 gives equality of the projected linear-extension sets: restriction maps extensions of \(G\) onto extensions of \(H\), so \(e(H)\le e(G)\). That is not equality of minimax values; equal extension counts do not in general determine \(F\), as issue #301 also notes.

**Candidate inequalities:** The example refutes \(F(G)=F(H)\) and the proposed direction \(F(G)\le F(H)+r\) only if \(r\) is negative; for any natural nonnegative residual cost, that inequality holds here but is not evidence for a general theorem. It refutes \(F(H)\le F(G)\) outright (\(3\nleq2\)). I did not establish the other direction \(F(G)\le F(H)\), nor a general residual bound.

**Local recurrence and tests:** `scripts/evaluate.py` memoizes closed reachability states and applies
\(F(Q)=1+\min_{x\parallel y}\max(F(Q+x<y),F(Q+y<x))\), with zero at total orders. `tests/test_evaluate.py` checks only the known values through \(n=6\) and negative input; it has no shortcut-map regression coverage.

**Residual fibers / algorithmic consequence:** I found no exact smaller minimax subgame representing the fibers of \(\mathrm{Ext}(G)\to\mathrm{Ext}(H)\). The remaining obstacle is to show that comparison branches on the deleted path vertices can be represented by a state-dependent exact game, with a proved recurrence correspondence and a bound on its per-state cost. Without that, the paper’s \(O(\log e(G))\) sorting comparison bound does not give an exact minimax decomposition or an improvement for computing root-antichain \(S(n)\). No all-\(n\) claim or timing claim follows from this finite counterexample.
