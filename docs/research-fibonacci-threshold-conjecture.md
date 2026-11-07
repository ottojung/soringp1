# Conjecture: the uniform tightness threshold is Fibonacci

**Status: open conjecture.** The verified values in
`docs/research-core-reduction.md` fit a single closed form. For `r >= 0`, with
`Fib(1) = Fib(2) = 1`,

```
T(r) = Fib(r+3) - 1,
```

i.e. `1, 2, 4, 7, 12, 20, 33, 54, ...` for `r = 0,1,2,3,4,5,6,7,...`.

## Evidence

`T(0..5) = 1, 2, 4, 7, 12, 20` are established (the last two by
`docs/research-core-reduction.md` and, independently, by the Kahn--Saks route in
`docs/research-t4-threshold.md`). Each value is a Fibonacci number minus one, and
the first failing extension counts `2, 3, 5, 8, 13, 21` are consecutive
Fibonacci numbers. Exact depth witnesses:

| `e` | poset | `m` |
|---:|---|---:|
| 2 | 2-antichain | 1 |
| 3 | the 3-element `V` (one element above two incomparable ones) | 2 |
| 5 | `up = (8,12,0,0)` | 3 |
| 8 | `up = (0,0,1,3,7)` (the `W` witness) | 4 |
| 13 | `up = (20,16,0,23,0,22)` | 5 |
| 21 | `up = (0,0,1,3,7,15,31)` | 6 |

## Equivalent form

Let `E_min(k)` be the least `e(P)` over finite posets with `m(P) = k`. Then
`T(r) = E_min(r+1) - 1`, so the conjecture is exactly

```
E_min(k) = Fib(k+2)   for every k >= 1,
```

and it is equivalent to the single inequality

```
e(P) >= Fib(m(P) + 2)   for every finite poset P,
```

together with attainment of `Fib` by an explicit family. The offset is right:
`m = 1` is first achieved by the 2-antichain, `e = 2 = Fib(3)`.

## Why it is not immediate

Induct on `m(P)`. If `P` is not total, take a first comparison splitting `P` into
`P1, P2` with `e(P) = e1 + e2` and `m(P) = 1 + max(m1, m2)`; by induction
`e(P) >= Fib(m1+2) + Fib(m2+2)`. With `m1 = m(P)-1`, this is
`Fib(m+1) + Fib(m2+2)`, which reaches `Fib(m+2)` only when `m2 >= m-2`.

So the obstruction is precisely an **unbalanced optimal split**: a poset whose
best first comparison has child depths differing by at least two. The
conjecture therefore needs either a proof that some optimal comparison is
balanced to within one (at least for `e`-minimal posets at each depth), or a
stronger induction invariant that controls the total extension count across an
unbalanced split.

## Falsifiability

A single explicit poset with `e(P) < Fib(m(P)+2)` refutes the conjecture; the
smallest such poset and its exact `e`, `m` would be the complete answer. The
first genuinely open prediction is `T(6) = 33` (first failing `e = 34`), against
the currently proved range `27 <= T(6) <= 55`. A complete enumeration of cores
with `e <= 33` would establish `T(6) >= 33`; a poset with `e = 34` and `m = 7`
would establish the matching upper bound.

## Scope

This is a conjecture about local extension counts and minimax comparison depth.
It would give a closed form for the whole `T(r)` sequence but would not by
itself improve the complexity of evaluating `S(n)`, prove anything about
`SORT-BOUND-U`, or close issues #47/#48.
