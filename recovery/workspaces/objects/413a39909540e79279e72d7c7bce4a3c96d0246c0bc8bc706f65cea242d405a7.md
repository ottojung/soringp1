# Literature baseline and source leads

Before investing in another proof or evaluator, check what is already known
about the **minimum worst-case number of adaptive pairwise comparisons**.

## Exact values and non-tight lower bounds

- Marcin Peczarski, *Towards optimal sorting of 16 elements*, Acta Univ.
  Sapientiae Informatica 4(2) (2012), 215–224:
  https://real-j.mtak.hu/23036/2/Acta%20Info%202012_4_2.pdf .
  Its introduction reports equality of optimal comparison counts with the
  information bound through n=11 and discusses the known S(12)=30 versus
  ceil(log₂(12!))=29, credited to Wells.
- L. R. Ford Jr. and Selmer M. Johnson, *A Tournament Problem* (1959):
  merge-insertion sorting; check bounds and optimality against the model.
- Knuth, *The Art of Computer Programming*, Volume 3, §5.3.1:
  comparison-count optimality and the historic sorting-number results.
- OEIS [A036604](https://oeis.org/A036604) indexes exact optimal
  comparison counts, and [A003070](https://oeis.org/A003070) indexes the
  ceiling-logarithm information bound. These are **indexes**, not
  substitutes for primary proofs.

## Complexity barriers

- Stephen R. Mahaney, *Sparse complete sets for NP: Solution of a conjecture
  of Berman and Hartmanis*, Journal of Computer and System Sciences 25(2)
  (1982), 130–143, DOI
  https://doi.org/10.1016/0022-0000(82)90002-2 .
  [Author manuscript](https://ecommons.cornell.edu/entities/publication/02e42763-8a49-4dfe-9e73-59ccc016f74f).
  A sparse NP-hard language under polynomial-time many-one reductions would
  imply P=NP. The fixed unary threshold language in `problem.md` is sparse;
  see `exploration-agenda.md` for the elementary counting argument.
  This is a barrier to a routine proposed reduction, **not** a proof that
  the sorting-number evaluation problem belongs to P or NP.

## Related models — use with care

- Yuval Filmus, *Decision Trees*, §3.1.5, on sorting by relative-order
  queries: https://yuvalfilmus.cs.technion.ac.il/Manuscripts/MSC-2018-01.pdf .
- [CLRS-Lean sorting lower-bound formalization](https://tanktechnology.github.io/CLRS-Lean/CLRSLean/FourthEdition/Chapter_08/Section_08_1_Lower_Bound_For_Sorting/):
  relevant for auditing definitions; respect its license before adapting code.
- [Discussion of hardness of optimal sorting](https://cstheory.stackexchange.com/questions/21152/hardness-of-optimal-sorting):
  background lead, *not* primary evidence of a reduction for S(n).

For each cited theorem, record the precise model (adaptive tree vs network,
partial information vs no information, uniform evaluation vs one-off
sorting, average vs worst case) and input encoding. A claim about a related
optimization problem is not automatically a claim about evaluating S(n).
