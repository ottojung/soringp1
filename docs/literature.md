# Reading and source leads

Primary and technically useful starting points (not claims of hardness for S):

- Knuth, *The Art of Computer Programming*, Vol. 3, *Sorting and Searching*,
  for comparison-count optimality and sorting numbers.
- Ford and Johnson (1959), *A Tournament Problem*, for merge-insertion sorting.
- Peczarski, *Towards Optimal Sorting of 16 Elements*, for rigorous small-n
  decision-tree analysis.
- Yuval Filmus, *Decision Trees*, §3.1.5, on sorting by relative-order queries:
  https://yuvalfilmus.cs.technion.ac.il/Manuscripts/MSC-2018-01.pdf
- [CLRS-Lean sorting lower bound formalization](https://tanktechnology.github.io/CLRS-Lean/CLRSLean/FourthEdition/Chapter_08/Section_08_1_Lower_Bound_For_Sorting/).
  This uses a similar permutation/decision-tree semantics and may be useful
  for checking definitions. Respect its license before adapting source code.
- [Hardness of optimal sorting (discussion)](https://cstheory.stackexchange.com/questions/21152/hardness-of-optimal-sorting):
  cautions that general minimum-height decision-tree hardness does not
  automatically classify the restricted sorting-number function.

For every cited theorem, record the *exact* model (adaptive vs network;
partial information vs no information; input representation; average vs
worst case). A nearby theorem is not a result about evaluating S(n).
