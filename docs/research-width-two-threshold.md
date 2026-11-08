# The width-two Fibonacci threshold

**Status:** paper proof, conditional on one published theorem, plus a small
experiment. Companion test: `tests/test_width_two_threshold.py`. This establishes
the Fibonacci comparison threshold for posets of **width two** only; the global
statement for unrestricted posets remains open, and nothing here changes any
complexity-class bound.

## 0. Definitions

`e(P)` is the number of linear extensions of a finite poset `P`; `m(P)` is the
exact worst-case number of further adaptive comparisons needed to sort every
linear extension. `width(P)` is the size of a largest antichain. Write
`F_1 = F_2 = 1` for the Fibonacci numbers and `T(r) = F_{r+3} - 1` for the class-independent threshold, so
`T(0..8) = 1, 2, 4, 7, 12, 20, 33, 54, 88`; `T_2(r)` denotes the width-two
threshold.

For a class `C` of posets write `T_C(r)` for the largest `E` such that every
`P` in `C` with `e(P) <= E` has `m(P) <= r`.

## 1. Result

**Theorem** `[paper proof, conditional on Peczarski 2006]`. For every finite
poset `P` of width two,

    e(P) >= F_{m(P)+2},

so the width-two threshold satisfies `T_2(r) >= F_{r+3} - 1` for every `r`, with
equality for `r <= 8` (Section 4).

Equivalently: a width-two poset with `e(P) <= F_{r+3} - 1` can always be sorted
in `r` further comparisons, and for `r <= 8` no larger bound is possible.

## 2. The one external dependency

**Gold Partition Conjecture (GPC).** As stated by Peczarski: if `P` is not a
chain, "we can point out two consecutive comparisons such that regardless of the
oracle's answers the following inequality holds: `t_0 >= t_1 + t_2`, where
`t_0, t_1, t_2` denote the number of linear extensions of the poset `P`, the
poset obtained after the first comparison, the poset obtained after both
comparisons, respectively" (Peczarski, *Comments on the Golden Partition
Conjecture*, Contrib. Discrete Math. 12 (2017) 106–109, §1, restating his Order
23 (2006) conjecture; the 2006 paper proves it for width-two posets).

**Consequence used below.** Fix the GPC pair and look at a path on which the
second comparison is made, with first-level child size `t_1` and grandchild size
`t_2`. Since `t_0 - t_1` is the size of the *other* first-level child, the
inequality says every grandchild of that comparison is at most the other
first-level child. Writing the first comparison's children as `a >= b` and the
second comparison as made inside the `a`-child with grandchildren `a_1 + a_2 = a`,
we therefore get

    max(a_1, a_2) <= b,

which is the bound the induction needs. (It is the larger grandchild that must
be controlled: the smaller one is automatically at most `a/2 <= b` only when
`a <= 2b`, which is not known in advance.) I checked this derived form by
exhaustive search against every non-chain poset with `n <= 6`: in all 384 cases
whose larger first child has at least two extensions, such a pair exists; the
other 15 are already total after one comparison.

**Primary source.** M. Peczarski, *The Gold Partition Conjecture*, Order **23**
(2006) 89–95, `doi:10.1007/s11083-006-9033-1`. Its abstract states that the
conjecture is proved "for posets of width two, semiorders and posets containing
at most 11 elements", and that it "immediately implies the 1/3–2/3 Conjecture and
tight upper bound for sorting". So the width-two case is a published theorem.

**Stated limitation.** The 2006 article itself is paywalled; the width-two claim
is verified from its published abstract, and the formal definition above is taken
verbatim from the 2017 paper, which restates it. What is *not* checked here is
Peczarski's proof of the width-two case, only its statement. The induction
arithmetic is checked exactly in the companion test for `r <= 60`.

Width two is closed under adding relations, so every child arising below is again
of width at most two.

## 3. Induction

Fix `r >= 2` and suppose the theorem known for all smaller budgets; let `P` have
width at most two and `e(P) <= T(r) = F_{r+3} - 1`.

If `P` is a chain, `m(P) = 0 <= r`. Otherwise apply GPC: the first comparison
splits `e = a + b` with `a >= b`, and inside the `a`-child the second comparison
splits `a = a_1 + a_2` with `min(a_1, a_2) <= b`. Two cases.

*Case 1: `a <= e/phi`*, where `phi = (1+sqrt5)/2`. Then
`a <= T(r)/phi < F_{r+2}` — the strict inequality is the Binet identity
`phi F_{r+2} = F_{r+3} + (-1)^{r+1} phi^{-(r+2)} > F_{r+3} - 1`. As `a` is an
integer, `a <= F_{r+2} - 1 = T(r-1)`. Both first children have at most
`T(r-1)` extensions, so by induction each sorts in `r-1` more comparisons and
`P` sorts in `1 + (r-1) = r`.

*Case 2: `a > e/phi`.* Then `b = e - a < e(1 - 1/phi) = e/phi^2 <= T(r)/phi^2`.
Using `phi^2 F_{r+1} = F_{r+3} + (-1)^r phi^{-(r+1)} > F_{r+3} - 1`, we get
`b <= F_{r+1} - 1 = T(r-2)`, and by the GPC consequence above both grandchildren
satisfy `a_1, a_2 <= b <= T(r-2)`. After the two GPC comparisons all three
surviving states have at most `T(r-2)` extensions, so by induction each sorts in
`r-2` more comparisons and `P` sorts in `2 + (r-2) = r`.

The bases `r = 0, 1` are immediate: `e <= 1` forces a chain, and `e <= 2` leaves
at most one comparison. Hence `e(P) <= T(r)` implies `m(P) <= r` for width-two
`P`, i.e. `T_{width<=2}(r) >= F_{r+3} - 1`.

## 4. Tightness

Let `W_n` be the staircase poset of `docs/research-core-threshold.md`: elements
`0..n-1` with `i` above `j` exactly when `j <= i - 2`. It has width two.

*Extension count, all `n`.* The two maximal elements of `W_n` are `0` and `1`.
Extensions ending in `0` are exactly the extensions of `W_{n-1}` (the induced
subposet on `1..n-1`), and extensions ending in `1` have `0` first and are
extensions of `W_{n-2}` (on `2..n-1`). Hence `e(W_n) = e(W_{n-1}) + e(W_{n-2})`
with `e(W_1) = 1, e(W_2) = 2`, i.e. `e(W_n) = F_{n+1}` for every `n >= 1`.

*Depth.* `m(W_n) = n - 1` is verified by exact minimax for `n <= 10`; this note
does **not** prove it for all `n`. Consequently, taking `n = r + 2` gives
`e(W_{r+2}) = F_{r+3}` and `m(W_{r+2}) = r + 1` for `r <= 8`, so
`T_{width<=2}(r) <= F_{r+3} - 1` there, and with Section 3 the width-two
threshold is exactly `F_{r+3} - 1` for `r <= 8`. For `r > 8` the inequality of
Section 1 still holds (it is unconditional in `r` given GPC), but the matching
equality is conditional on `m(W_n) = n - 1` for the relevant `n`.

## 5. Experiment

`tests/test_width_two_threshold.py` enumerates all core isomorphism classes with
`e <= 20`, keeps those of width at most two with at most nine elements (146 of
them), computes `m` exactly by bounded minimax, and asserts
`e(P) >= F_{m(P)+2}`; it also checks that `W_n` has width two and the stated
`e` for `n <= 10`, and checks the four Binet inequalities used above. This is a
consistency check on small cases, not evidence for the theorem.

## 6. Scope: what this does not give

- **Not the global threshold.** Posets of width three or more are untouched. The
  full statement `T(r) = F_{r+3} - 1` is open; the verified class-independent
  finite cases are `T(6)=33`, `T(7)=54`, `T(8)=88` (see
  `docs/research-core-threshold.md`), and `T(9)=143` is predicted, not verified.
- **No complexity consequence.** The antichain root of `S(n)` has width `n`, not
  two, so this yields no new bound for `S(n)` or `SORT-BOUND-U`. Counting linear
  extensions of bounded-width posets is polynomial, so the width-two threshold
  predicate is easy on its own class; that does not transfer to the unary
  language.
- **Conditional, not unconditional.** The theorem rests on GPC for width two as
  published; the proof here is not formalised in Lean.

## 7. Reproduce

```sh
python3 -m unittest tests.test_width_two_threshold -v
```
