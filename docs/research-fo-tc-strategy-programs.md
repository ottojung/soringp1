# FO(TC) strategy programs for exact optimal sorting

**Status:** research note (paper-and-literature analysis, no experiment yet).
Labels: `[literature]`, `[deduction]`, `[conjecture]`, `[open]`.
No new Lean files. No commits unless separately requested.

## 0. Question (all-n, sharp)

Does there exist, for every n with S(n) <= k, an adaptive comparison
strategy program p in a fixed bounded-arity FO(TC) fragment whose
text size is poly(n+k), whose interpreter runs in uniform poly time, and
whose execution uses <= k charged comparisons on every input order? This is
the completeness half of a Sigma_2^P upper bound for SORT-BOUND-U. The
soundness half is immediate once the interpreter and cost accounting are
fixed. The hard part is completeness: a program that brute-force searches
for an optimal tree is disallowed by the runtime condition.

## 1. Model definition (sketch)

State = transitively closed partial order P on n labelled keys plus a
comparison budget counter. Program text = sequence of FO(TC) rules of form
"if exists incomparable pair (x,y) with property phi(P,x,y) then compare
x,y; update P; decrement budget; branch on outcome; else output P".
Mutable knowledge is the order relation itself; comparisons are the only
charged oracle queries. Termination when P is total or budget exhausted.
Worst-case comparison budget = max over adversarial answers.

## 2. Combined complexity obstacle

FO(TC) is NL in data complexity for each fixed formula, but combined
complexity is exponential in formula size. Growing program texts therefore
need either (a) a fixed interpreter formula with the program encoded as
data, keeping data complexity NL but input length includes program text,
or (b) bounded-variable/arity fragments with polynomial combined checking.
Option (a) preserves expressiveness at the cost of encoding overhead;
option (b) risks losing the ability to express "exists an incomparable pair
satisfying a global property" in poly size. This is the central open
technical point.

## 3. Elementary examples

Insertion sort: O(n^2) comparisons, program size O(n) rules (one per
insertion position), interpreter time O(n^2). Merge sort: O(n log n)
comparisons, program size O(n log n) rules, interpreter time O(n log n).
Small optimal sorters (n <= 7): decision trees of height S(n) can be
unfolded into programs of size O(n!?) in the worst case unless compression
by state rules is used; this is exactly the compression question.

## 4. Conjecture (falsifiable, all-n)

Every optimal S(n)-comparison sorter admits a program of size poly(n) and
runtime poly(n) in the fixed-interpreter FO(TC) fragment. Refutation route:
exhibit a family of n for which any such program either has super-polynomial
size or super-polynomial runtime, e.g. by an information-theoretic or
communication-complexity argument on the universal quantifier over input
orders. A plausible barrier: if the optimal tree has super-polynomial
asymmetry between branches, no polynomial state-rule compression exists.

## 5. Relation to forgetful framed DAGs (issue #47)

Programs subsume DAGs: a framed DAG is a program whose state is the set of
known comparabilities and whose rules are "compare next scheduled pair".
The converse is false in general: programs may compute new comparabilities
from the order (transitive closure queries) and choose comparisons
adaptively based on derived state, which framed DAGs encode only by
explicit nodes. Whether this extra power yields asymptotic compression is
open. Priority: test whether a program can simulate a forgetful framed DAG
with only constant overhead; if yes, programs are at least as succinct.

## 6. Sigma_2^P accounting

Existential program choice (exists p) + universal adversarial input orders
(forall X) + polynomial interpreter verification. The universal step is
polynomial only because the interpreter is uniform polynomial time; writing
FO(TC) source alone does not give this bound (combined complexity). Hence
membership of the subclass is Sigma_2^P; unrestricted S(n) membership is
not claimed without completeness.

## 7. Next experiment

Construct, for n = 4,5,6, an explicit FO(TC) program for an optimal sorter
and measure (a) text size, (b) interpreter steps, (c) comparison count,
against the framed-DAG certificate size from issue #47. Decide whether
state-rule compression beats explicit DAG encoding on these small cases
before attempting an all-n proof.
