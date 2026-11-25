# Exact sorting numbers are not holonomic

**Status:** paper proof (analytic number theory), independently checkable,
not Lean-checked. **Model:** `S(n)` is the minimum worst-case number of
adaptive pairwise comparisons needed to sort `n` distinct labelled keys.
All asymptotics are in numeric `n`.

## Result

Let `F(z) = sum_{n>=0} S(n) z^n` be the ordinary generating function.

**Theorem.** `F` is not D-finite (holonomic), and therefore `S` is not
P-recursive. In particular, there are no polynomials
`p_0,...,p_r` with `r < infinity`, `p_r != 0`, and

    sum_{i=0}^r p_i(n) S(n+i) = 0    for all sufficiently large n.

The order and the degrees are unrestricted: the theorem excludes every
finite-order linear recurrence with polynomial coefficients, not merely
a bounded-order candidate. The same argument applies to the information
bound `C(n) = ceil(log_2 n!)`.

More generally, no integer sequence asymptotic to `c n log n` with
`c != 0`, up to an additive `O(n)` error, is P-recursive. This is the
form that matters here: the known asymptotic regime
`S(n) = log_2(n!) + o(n)` is far too weak to evade the obstruction, and
the theorem does not need Sergeev's sharper error term.

## Proof

### 1. Radius one

The information lower bound gives

    S(n) >= ceil(log_2 n!) = (1/log 2) n log n - (1/log 2) n + O(log n),

and merge sort gives

    S(n) <= n ceil(log_2 n) = (1/log 2) n log n + O(n).

Hence `S(n) = (1/log 2) n log n + O(n)`, in particular
`S(n) = Theta(n log n)`. Thus `F` has radius of convergence exactly `1`:
the polynomial upper bound gives radius at least `1`, and the unbounded
nonnegative integer coefficients give radius at most `1`.

### 2. D-finite plus integer coefficients plus radius one forces rationality

We use the classical Polya-Carlson theorem: an integer-coefficient power
series with radius of convergence `1` is either rational or has the unit
circle as a natural boundary. (Polya 1916; Carlson 1921; a modern
statement is Remmert 1998, pp. 265--266. See also
Bell--Chen--Nguyen--Zannier 2023, whose D-finite rationality theorem is
a multivariate generalization.)

If `F` were D-finite, it would satisfy a linear ODE

    q_r(z) F^{(r)}(z) + ... + q_0(z) F(z) = 0

with polynomial coefficients and `q_r` not identically zero. A nonzero
polynomial has finitely many zeros, so all finite singularities of `F`
lie in that finite zero set. Therefore the unit circle cannot be a
natural boundary: all but finitely many boundary points are regular and
`F` extends analytically across them. By Polya-Carlson, `F` must be
rational.

Equivalently, one may invoke the D-finite special case directly
(Bell--Chen--Nguyen--Zannier, arXiv:2306.02590): a D-finite power series
with algebraic-integer coefficients and Weil height `o(n)` is rational.
Here `S(n)` is an integer bounded by `n(n-1)/2`, so its height is
`O(log n) = o(n)`.

### 3. No rational power series has these coefficients

Suppose `F = P/Q` is rational with radius `1`. Partial fractions give

    S(n) = sum_alpha P_alpha(n) alpha^{-n},

where `alpha` runs over the poles of `F` and `P_alpha` is a polynomial.
Since the radius is the minimum modulus of a pole, every `|alpha| >= 1`
and at least one `|alpha| = 1`. Put `lambda = alpha^{-1}`. Then every
`|lambda| <= 1`, at least one has modulus `1`, and

    S(n) = sum_lambda P_lambda(n) lambda^n.

Let `d` be the largest degree of a polynomial attached to a term with
`|lambda| = 1`. Separating the unit-modulus terms gives

    S(n) = n^d q(n) + O(n^{d-1}),

where

    q(n) = sum_{|lambda|=1, deg P_lambda=d} c_lambda lambda^n

is a nonzero finite sum of unit-modulus exponentials. Such a `q` is
bounded and does not tend to `0` (its mean square is the sum of the
squared absolute values of the distinct nonzero coefficients).

Now compare with `S(n) = (1/log 2) n log n + O(n)`:

- If `d = 0`, then `S(n) = q(n) + O(1/n)` is bounded, contradiction.
- If `d = 1`, then `S(n)/n = q(n) + O(1/n)` is bounded, while
  `S(n)/n = (1/log 2) log n + O(1)` is unbounded, contradiction.
- If `d >= 2`, then
  `S(n)/n^d = O(n^{1-d} log n) -> 0`, so `q(n) -> 0`, contradiction.

Thus no rational `F` has coefficients asymptotic to `c n log n`,
`c != 0`. Combined with Steps 1--2, `F` is not D-finite. Since a
sequence is P-recursive exactly when its ordinary generating function is
D-finite, `S` is not P-recursive. QED.

## A failed first attempt, kept for the record

A tempting shorter argument is: rational coefficients have polynomial
growth, whereas `S(n)` is `n log n`, which is "super-polynomial". That
is wrong: `n log n = O(n^2)`, and `S(n) <= n(n-1)/2` is itself
polynomial. The growth rate alone does not contradict rationality. What
does contradict rationality is the finer shape of rational coefficients
in Step 3: a finite sum of polynomial-times-exponential terms cannot
carry the logarithmic factor `n log n`.

## Scope and limits

- **What is excluded.** Every fixed-order, fixed-degree holonomic
  recurrence; every algebraic generating function; and every route that
  would evaluate `S(n)` by iterating such a recurrence from finitely many
  initial values. The winning-frontier barrier explicitly left algebraic
  recurrences open; this closes that family.
- **What is not excluded.** Nonlinear recurrences, recurrences whose
  order or degree grows with `n`, divide-and-conquer algorithms,
  algorithms using precomputed advice, and arbitrary polynomial-time
  computations of `S(n)`. Non-holonomy is not a time or space lower
  bound: many non-holonomic integer sequences are trivially computable.
  In particular this proves neither `SORT-BOUND-U ∉ P` nor any
  separation from `NP`.
- **General posets.** No statement is made about minimax values of
  arbitrary partial orders. The theorem uses only the fixed sequence
  `S(n)`, its integrality, and its leading asymptotic term.
- **Certificates.** This says nothing about the soundness or completeness
  of framed sorting certificates. Soundness of a local certificate
  checker and completeness of a polynomial-size certificate system are
  separate questions, untouched here.
- **No exact-value input.** The proof uses no value from OEIS A036604 or
  A003070 and no finite computation. It does not determine `S(23)` or
  any further exact value.

## Sources

- G. Polya, *Uber Potenzreihen mit ganzzahligen Koeffizienten*, Math. Ann.
  77 (1916), 497--513.
- F. Carlson, *Uber Potenzreihen mit ganzzahligen Koeffizienten*, Math. Z.
  9 (1921), 1--13.
- R. Remmert, *Classical Topics in Complex Function Theory*, GTM 172,
  Springer 1998, pp. 265--266 (Polya-Carlson theorem).
- J. P. Bell, S. Chen, K. D. Nguyen, U. Zannier, *D-finiteness,
  rationality, and height III: multivariate Polya-Carlson dichotomy*,
  arXiv:2306.02590 (2023).
- P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge 2009,
  for D-finite series and rational coefficient asymptotics.
- R. P. Stanley, *Differentiably finite power series*, European J.
  Combin. 1 (1980), 175--188; L. Lipshitz, *D-finite power series*,
  J. Algebra 122 (1989), 353--373, for the sequence/function equivalence
  and finiteness of singularities.
