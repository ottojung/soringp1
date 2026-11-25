# FO(TC) strategy programs for exact optimal sorting

## Model

A strategy program `p` is a finite list of rules over a fixed relational vocabulary for sorting n distinct keys. State is a set of known comparison outcomes (a partial order on key indices) plus an output permutation. At each step the program either (a) selects a comparison `(i,j)` whose outcome is not yet determined, incurring cost 1, branches on `<`/`>`, and adds the fact; (b) outputs a permutation once the order is total; or (c) halts with failure. Worst-case comparison budget `k` bounds the number of (a)-steps along any path.

Syntax (FO(TC)): rules are guarded first-order formulas with transitive closure over the known-order relation; guards select the next comparison pair; TC expresses reachability/order-closure. Mutable state is encoded as an EDB relation updated between rule firings by a fixed uniform interpreter.

Semantics: `Run(p,X)` interprets comparisons against the unknown total order X via an oracle; p never reads X directly. Correctness: for every total X, Run terminates with the sorted permutation and cost <= k.

## Cost accounting

- Program size: number of rules / symbols, must be poly(n+k).
- Runtime: uniform polynomial-time interpreter per input; combined evaluation of FO(TC) over growing program text is NOT guaranteed by data-complexity NL; restrict to bounded-variable/arity fragments or a fixed interpreter with explicit polynomial bounds.

## Soundness/time bound

Given a program p and bound k, verification "forall total X: Run(p,X) sorts with <= k comparisons" is in Sigma_2^P provided the interpreter is uniform polynomial-time. Existential program choice is separate from universal adversarial outcomes; writing FO(TC) source alone does not establish membership.

## Completeness conjecture (all-n, falsifiable)

Conjecture: For every n, there exists an optimal S(n)-comparison sorter representable by a program of size poly(n+S(n)) with polynomial runtime in this language.

A program that exhaustively searches for the optimal tree does NOT satisfy the runtime condition.

## Findings (PROVED / CONDITIONAL / REFUTED)

- PROVED: soundness and Sigma_2^P upper bound under uniform polynomial interpreter (conditional on interpreter).
- CONDITIONAL: completeness for n small (insertion/merge sort programs exist; size poly).
- OPEN: whether fixed-m split-schema programs stay exact beyond computed range (see prior split-schema note).

## Concrete next experiment

Implement an interpreter for the strategy language and encode insertion sort + optimal n<=6 sorters; measure program size and comparison cost; test polynomial combined-evaluation on growing texts.
