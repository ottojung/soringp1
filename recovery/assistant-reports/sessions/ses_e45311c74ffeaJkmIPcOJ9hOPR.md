# Audit repaired non-holonomy proof

Session: ses_e45311c74ffeaJkmIPcOJ9hOPR
Workspace: /home/lubko/soring-fronts/s-p-recursive-exact-sequence
Created: 1794135483316; updated: 1794135603397

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 5 (msg_1bacee3f0001vEqZew6gipnRCJ)

**Concrete flaw (repairable):** Step 3 reverses an inequality.

Since the poles are \(\alpha_j=1/\lambda_j\) and \(\operatorname{rad}(F)=1\), we have \(|\alpha_j|\ge 1\). Therefore

\[
|\lambda_j|\le 1,
\]

so radius \(1\) excludes \(|\lambda_j|>1\), **not** \(|\lambda_j|<1\). Terms with \(|\lambda_j|<1\) are allowed and decay exponentially. As written, exponentially growing terms are not excluded, and the later statement “if there are no unit-modulus terms, \(S(n)\) decays exponentially” is unjustified. Replacing “no \(|\lambda_j|<1\)” by “no \(|\lambda_j|>1\)” fixes this.

With that correction, the rest is sound:

- **(i)** Step 4 is correct with several unit-modulus \(\lambda\)'s of different arguments. Grouping the top polynomial degree gives  
  \[
  S(n)/n^d=q(n)+O(1/n),\qquad q(n)=\sum c_j\lambda_j^n.
  \]
  If \(\lambda=1\) has degree \(d\), it is simply one term of \(q\). Equal \(\lambda\)'s are merged in canonical partial fractions, and the leading coefficient for each pole is nonzero, so no hidden cancellation occurs.
- **(ii)** \(S(n)=\Theta(n\log n)\) does hold: information-theoretic lower bound plus merge sort upper bound.
- **(iii)** Terms with \(|\lambda|>1\) are impossible because they would correspond to poles inside the unit circle, contradicting radius \(1\). This is exactly the corrected Step 3.
- **(iv)** The Pólya–Carlson step is valid. A D-finite series satisfies a linear ODE with polynomial coefficients, hence has only finitely many finite singularities, so it cannot have the unit circle as a natural boundary.
- **(v)** Yes: for a rational function, the radius of convergence is the minimum modulus of its poles, so radius \(1\) forces at least one pole on the unit circle.
- **(vi)** Yes: a nonzero finite sum of distinct unit-modulus exponentials has positive mean square, hence cannot tend to \(0\).

**Verdict:** As literally written, the proof has a concrete sign error in Step 3. After changing “no \(|\lambda_j|<1\)” to “no \(|\lambda_j|>1\),” the proof is **VALID**; Step 4 itself has no remaining logical gap.
