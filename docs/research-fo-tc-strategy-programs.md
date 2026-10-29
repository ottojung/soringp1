# FO(TC) Strategy Programs — Research Note

Status: CONDITIONAL.

Model: a program p is a sequence of guarded comparison instructions (i,j) with outcomes
less/greater, mutable state as FO(TC) transitive-closure-definable relations, output a
permutation. Cost = number of comparisons along worst-case path.

Soundness: each comparison is charged; interpreter runs in poly(n+k) per input order.

Completeness (conjecture, unproved): for every n with S(n)<=k there exists program of
size poly(n+k) with worst-case <=k comparisons.

Barrier: a program that exhaustively searches for optimal trees violates runtime bound.

Next experiment: implement interpreter + verify insertion/merge sort programs for n<=8;
measure sizes.
