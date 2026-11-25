# Audit non-holonomy proof

Session: ses_e4534976bffeWq5qXFRA92TksP
Workspace: /home/lubko/soring-fronts/s-p-recursive-exact-sequence
Created: 1794135255228; updated: 1794135404332

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 5 (msg_1bacb6902001gHNMZe0s2PdhfM)

**INVALID.**

The concrete flaw is **Step 4**. From  
\[
S(n)\ge c\,n\log n
\]
one cannot conclude that \(S(n)\) is not \(O(n^M)\) for any fixed \(M\). In fact
\[
n\log n=O(n^2),
\]
and Step 1 itself already gives \(S(n)\le n(n-1)/2=O(n^2)\). Thus the polynomial growth bound for rational generating functions is perfectly compatible with the known lower bound. The argument would need a super-polynomial lower bound, which is false: merge sort gives \(S(n)=O(n\log n)\), so actually \(S(n)=\Theta(n\log n)\).

Subsidiary checks:

- **(a)** Yes: the Pólya–Carlson theorem is correctly stated for integer coefficients and radius \(1\); no boundedness or monotonicity hypothesis is needed. Standard sources: Pólya (1916), Carlson (1921); Flajolet–Sedgewick, *Analytic Combinatorics*, Chapter IV.
- **(b)** No: a D-finite function satisfies a linear ODE with polynomial coefficients, so its finite singularities lie among the zeros of the leading coefficient. There are only finitely many, so they cannot form a natural boundary. See Stanley, *Enumerative Combinatorics II*, §6.4, or Lipshitz, *D-finite power series*, J. Algebra 122 (1989).
- **(c)** Yes: partial fractions gives coefficients as finite sums of \(p_\alpha(n)\alpha^{-n}\). If \(|\alpha|=1\) but \(\alpha\) is not a root of unity, \(\alpha^{-n}\) is still bounded, so the growth remains \(O(n^M)\).
- **(d)** No: \(S(0)=S(1)=0\) is harmless. Only integrality, nonnegativity, and unboundedness are used.

The conclusion “\(S\) is not P-recursive” is true, but this proof needs repair. A correct route uses the stronger fact \(S(n)=\Theta(n\log n)\): if \(S\) were P-recursive, Pólya–Carlson would force the generating function to be rational; rational coefficients are finite sums of polynomial-times-exponential terms and cannot have growth exactly \(\Theta(n\log n)\).
