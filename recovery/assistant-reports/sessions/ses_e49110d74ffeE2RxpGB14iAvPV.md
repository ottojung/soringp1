# antonina-iRi3hI5ZVGnhesoG3G564W-peroxide

Session: ses_e49110d74ffeE2RxpGB14iAvPV
Workspace: /home/lubko/soring-fronts/exec-merge-tree-rounding-gap-20261107
Created: 1794070475465; updated: 1794070510089

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 77 (msg_1b6ef547c001fSS41boOVL6GNA)

**Evidence points to a negative answer:** there is an explicit all-\(n\) family with \(R(T)=o(n)\).

Take \(T_n\) to be the recursively defined *binomial merge tree*: a subtree of size \(m\) splits into subtrees of sizes \(m-1\) and \(1\). At the root of a size-\(m\) subtree, the rounding contribution is
\[
\delta_m=\lceil\log_2 m\rceil-\log_2 m.
\]
Thus
\[
R(T_n)=\sum_{m=2}^{n}\delta_m.
\]
For \(m=2^j+r\), \(0\le r<2^j\), the contribution is \(\log_2(1+r/2^j)\). Using \(\log_2(1+x)\le x/\ln 2\), each complete block \(2^j\le m<2^{j+1}\) contributes at most \(1/\ln 2\). There are \(O(\log n)\) blocks, so
\[
R(T_n)\le \frac{\lfloor\log_2(n-1)\rfloor+1}{\ln 2}=O(\log n)=o(n).
\]
This directly refutes any universal linear lower bound for the **rounding-only** quantity.

As a small exact-DP falsification check, minimizing \(R\) over all binary tree shapes gives \(R_{\min}(24)\approx2.9625\), while the explicit family has \(R(T_{24})=\sum_{m=2}^{24}\delta_m\). The DP is only a finite check; the block argument establishes the all-\(n\) claim.

This does **not** imply sublinear actual merge surplus: the local cost may exceed \(\lceil\log_2\binom{a+b}{a}\rceil\), and that additional \(M(a,b)\)-slack is absent from \(R(T)\). Nor does this establish a bound for general adaptive sorting trees. No repository files were changed.
