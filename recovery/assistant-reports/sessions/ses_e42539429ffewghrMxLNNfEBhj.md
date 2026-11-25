# antonina-xS5EvwtO7QKw1yI5v3KXba-weighty

Session: ses_e42539429ffewghrMxLNNfEBhj
Workspace: /home/lubko/soring-fronts/near-optimal-farkas-succinctness
Created: 1794183556166; updated: 1794184547874

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 319 (msg_1bdbb42a2001QN9Iw7FF4eVCdT)

## Mathematical finding

The front’s positive hypothesis is **false**, and the obstruction is stronger than “only at \(k\approx n/2\)”.

From #301’s dual propagation lemma, for **every** \(0\le t\le k\), every Farkas certificate of the faithful state-expanded budget-\(k\) LP has support at least

\[
M(n,t)=\frac{n!}{2^t\,t!\,(n-2t)!}.
\]

The later choice \(t=k=n/2\) was only one specialization. The bound is monotone in \(k\), because the propagation to depth \(t\) never uses layers above \(t\).

Take even \(n\ge 4\), \(k=S(n)-1\), and \(t=n/2\). Since \(S(n)\ge \log_2(n!)\) and \(\log_2(n!)>n/2+1\) for \(n\ge4\), we have \(k>t\). Hence every Farkas certificate has support at least the number of perfect matchings

\[
(n-1)!!=\frac{n!}{2^{n/2}(n/2)!}.
\]

With \(N=n+k+1=n+S(n)=\Theta(n\log n)\),

\[
(n-1)!!=2^{\Theta(n\log n)}=2^{\Omega(N)}.
\]

So **no** Farkas certificate at the near-optimal budget has support polynomial in \(N\); support is exponential in \(N\) for all sufficiently large even \(n\). Odd \(n\) works the same way with near-perfect matchings.

The induction is the #301 matching argument: for each \(t\)-matching \(M\), some orientation \(P_M\) at depth \(t\) has \(a_{P_M,t}>0\). Distinct matchings give distinct labelled posets and hence distinct nonzero dual coordinates. The only correction needed is choosing \(t=\lfloor n/2\rfloor\) independently of \(k\).

## Independent finite check

For \(n=4\), \(k=S(4)-1=4\), I built the labelled state-expanded LP and solved it with HiGHS:

- primal LP: infeasible;
- explicit dual certificate: support 204;
- positive state multipliers occurred for at least one orientation of all 6 one-edge matchings and all 3 perfect matchings, exactly as the lemma predicts.

For \(n=3,k=2\), all 3 edges were covered. This checks the dual sign convention; it is not the asymptotic proof. The full \(n=5,k=6\) LP exceeded the local solve budget.

## Limits

- This refutes **literal coordinate support** in the labelled faithful state-expanded LP.
- It does **not** rule out a symbolic or symmetry-quotiented description of the exponentially supported multipliers, a different LP/encoding, or the tree-selection LP.
- It is **not** a coNP lower bound and does not compute \(S(n)\). The LP remains sound and complete for infeasibility; the point is that its complete Farkas certificate family is exponential, so LP soundness/completeness does not give a polynomial-size certificate theorem.
- No general-poset hardness result is used or transferred to the antichain root.

I posted this to board #301 as `SoringP1 frontier: near-optimal-farkas-succinctness` at `2026-11-09T00:35Z`. No repository or Lean changes; the worktree remains clean.
