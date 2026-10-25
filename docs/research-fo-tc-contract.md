# FO(TC)-style sorting strategy contract: soundness witness

**Status:** bounded semantic specification and finite executable witness;
not an all-`n` completeness result. The target remains
`SORT-BOUND-U = {1^n#1^k : S(n) <= k}`.

## Operational contract [definition]

For fixed `n,k`, a program is a finite deterministic label map. Its store
contains a control label, a partial output array, a query counter `q`, and a
history relation `H(a,b)` meaning that an earlier comparison established
`a < b`. A nonterminal rule evaluates against this store and returns exactly
one of `Ask(a,b)`, `Emit(i,a)`, `Goto(label)`, or `Halt`. An `Ask` requires
distinct labels in `[n]`, invokes the hidden-order oracle once, records the
answer in `H`, increments `q`, and takes the outcome-specific successor.
Repeated comparisons are allowed and each is charged. `Emit` fills one
previously empty output position. `Halt` accepts only when all positions
contain a permutation of `[n]`, `q <= k`, and the output is increasing in
the hidden order.

The program can observe the hidden total order only through `Ask` answers;
`H` is derived solely from those answers. The outer verifier, which does see
the explicitly encoded hidden permutation `X`, checks sortedness. Rule
evaluation, parsing, and store updates are ordinary interpreter work and
must fit a uniform polynomial clock in `n+k+|p|` for the bounded program
class under study. Thus an FO(TC) formula alone is not an execution model:
its encoding, evaluation algorithm, rule dispatch, and clock are part of
the semantics.

In one common fixed-variable fragment, fixing global variable bound `v`
and explicit store relations gives a direct truth-table evaluator with
combined (formula text and structure size) polynomial time; this is
separate from the FO(TC)=NL **data-complexity** capture statement for each
fixed formula. A growing formula text cannot be assigned that data
complexity bound without a combined evaluator argument.

## Soundness [deduction]

If a program passes the outer verifier on every total order of `[n]` and
uses at most `k` queries on every run, its deterministic oracle execution
is an adaptive comparison sorting strategy of worst-case cost at most
`k`. Therefore `S(n) <= k`. This implication does not require any program
size bound. Conversely, placing the unary language in a class such as
`Sigma_2^P` additionally requires polynomial program descriptions and a
uniform polynomial interpreter clock. To infer membership for unrestricted
`SORT-BOUND-U`, one also needs a polynomial-size exact-completeness theorem
for every `n,k`; this document does not establish one.

## Executable witness [experiment]

`scripts/fo_tc_twophase_barrier.py` is an explicit label-map interpreter
and outer verifier. Run:

```sh
python3 scripts/fo_tc_twophase_barrier.py
```

The checked-in script exhaustively checks `n=5,6,7,8`; for each it
validates all `n!` orders, output permutation and sortedness, and compares
the worst query count with the stated budget. The `n=6,7,8` witnesses
attain the information bound and self-certify their exact sorting numbers;
`n=5` records the strict two-phase miss (8 queries versus `S(5)=7`).
These witnesses validate the operational accounting on those instances
only; they provide no all-`n` program construction or complexity-class
membership for unrestricted `S(n)`.
