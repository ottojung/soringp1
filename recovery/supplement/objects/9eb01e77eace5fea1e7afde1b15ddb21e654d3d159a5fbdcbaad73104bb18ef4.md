# Exponential-polynomial-time upper bound

This is an informal proof sketch, **not yet a Lean theorem**.

## States

A comparison transcript induces a strict partial order P on the n labelled
items. We keep its transitive closure. Each unordered pair has one of three
relations: x<y, y<x, or unknown. Not every ternary assignment is consistent,
but this gives at most 3^{n(n-1)/2} possible states.

## Minimax recurrence

Let F(P) be the minimum remaining worst-case number of comparisons needed to
determine the unique total order, given prior relations P.

- If P is total, F(P)=0.
- Otherwise, for every incomparable pair x,y, form the two valid successor
  partial orders P+(x<y) and P+(y<x), each transitively closed.
- Set F(P) = 1 + min_{x,y incomparable}
    max(F(P+(x<y)), F(P+(y<x))).

This is a finite acyclic recurrence: each branch strictly decreases the number
of incomparable pairs. Memoize states, start with the empty partial order,
and return F(empty)=S(n).

## Time

There are ≤ 3^{n(n-1)/2} possible ternary relation matrices. For each
reachable state, scan O(n²) incomparable pairs, compute transitive closure,
and combine already-memoized values using polynomial-time arithmetic.
All values are bounded by O(n²), for example by comparing every pair,
so their bit lengths are polynomial in n.

Thus the total deterministic time is bounded by

    poly(n) · 3^{n(n-1)/2} = 2^{O(n²)}.

In terms of unary input length m = Θ(n), this is EXPTIME.
In terms of binary input length m = Θ(log n), this is
2^{2^{O(m)}}, a 2-EXPTIME bound, *not* an EXPTIME result.

## Formalization obligations

To promote this sketch to kernel-checked status, prove:

1. comparison transcripts correspond to consistent partial-order states;
2. F's minimax recurrence is correct for all states;
3. the initial state matches the sorting-tree definition;
4. the recursion terminates and its implementation matches the recurrence;
5. a concrete machine cost bound including state representation, memoization,
   and arithmetic, with the input encoding explicitly accounted for.

The crude ternary-state count establishes an upper bound only. It does not
imply a matching lower bound or exclude a faster closed-form evaluator.
