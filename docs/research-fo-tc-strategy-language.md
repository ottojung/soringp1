# FO(TC) strategy language for exact optimal sorting

## Syntax
Program P is a finite sequence of rules over a fixed vocabulary:
- State predicates: Eq(a,b), Lt(a,b), Unk(a,b) (mutable knowledge of comparisons).
- Action: COMPARE(x,y) charges one comparison; observes outcome; updates state.
- Control: IF/branch on outcome; REPEAT (transitive closure over state); OUTPUT permutation.

## Semantics & cost
- Inputs: n distinct keys; unknown total order X.
- Oracle comparisons charged; no free access to X.
- Worst-case comparison budget k; program must sort for all X with <=k comparisons.
- Interpreter: fixed, uniform polynomial time per input (data complexity poly(n)).

## Complexity
- Combined evaluation: program text size s, input size n. Fixed interpreter runs in poly(s,n) (not just data complexity). Verification: exists P (size poly(n+k)) such that for all X, Run(P,X) sorts with <=k comparisons — Sigma_2^P given uniform poly interpreter. FO(TC) source alone does not imply this; combined bound required.

## Completeness (conjecture, all-n)
Optimal S(n)-comparison sorters have polynomial-size programs with polynomial runtime. Not yet proved; fixed-m split schemas suggest no super-polynomial penalty in tested range but are not general programs.

## Findings
- PROVED: soundness/time bound for fixed interpreter (this note).
- CONDITIONAL: Sigma_2^P membership for SORT-BOUND-U for representable subclass.
- OPEN: all-n completeness; fixed-m split penalties bounded.
