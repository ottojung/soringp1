# FO(TC) combined complexity: a tractable fragment and a compiler barrier

**Status:** paper-level lemma pair, independently auditable, not Lean-checked.
**Model:** adaptive comparison sorting of `n` distinct labelled keys;
`S(n)` is the optimal worst-case comparison count (`docs/problem.md`).
Target: unary `SORT-BOUND-U = {1^n#1^k : S(n) <= k}`.
Coordinates with umbrella Antonina #301 and soringp1 #47 (framed DAGs).

## Sharp question

Is there a *polytime-compilable* logical strategy language in which every
optimal `S(n)`-comparison sorter has a polynomial-size program with
polynomial per-input runtime? A YES with exact budget would put the
representable subclass of `SORT-BOUND-U` in `Sigma_2^P`; a NO for a
proposed restriction rules out that route. Consequence is stated
conditionally throughout: no unconditional lower bound for the sparse
unary language is claimed (cf. `AGENTS.md`).

## Definitions

**[definition]** `FO(TC)_v` is the following globally fixed-variable
syntax. Fix `v >= 2` once for the whole query-program fragment (not separately for
each subformula). Atomic formulas use equality and the input/store
relations; Boolean connectives and first-order quantifiers have their
usual semantics. If `x=(x_1,...,x_m)` and `y=(y_1,...,y_m)` are disjoint
tuples of distinct variable names and `theta` is a formula, then
`[TC_{x,y} theta](s,t)` is allowed when `s,t` are m-tuples and its free
variables other than the endpoint tuples form a context tuple `z` of
length `a`, disjoint from `x,y`, with `a+2m <= v`. The relation tested
for an edge is `theta` with `x,y` assigned to the source and target;
closure is reflexive transitive reachability on the `N^m` endpoint
tuples, separately for each fixed assignment to `z`. All bound and free
variables, including those in nested TC formulas, are drawn from the
same globally fixed set of at most `v` names. This explicit condition
also applies when a formula has additional local bound variables: its
syntax must permit their binding and the TC context without exceeding
that global set. Formula text `|phi|` may grow. Input structures have
domain size `N=Theta(n+k+1)`, a fixed relational vocabulary of arity at
most `v`, and explicitly tabulated input/store relations. In particular,
the vocabulary is not an oracle or a succinctly encoded relation.

**[definition]** A program is a finite byte string `p` interpreted by a
fixed deterministic machine `U`, with a control label, an output buffer,
binary query-history relation `H(i,j)` (meaning `i` was returned as
smaller than `j`), and counter `q`. Repeated queries still increment `q`;
`H` records their logical outcome. At a nonterminal label, its
FO(TC)_v rule over the current store returns exactly one action:
`Ask(i,j)`, `Emit(position,i)`, `Goto(label)`, or `Halt`; malformed or
non-singleton actions reject. `Ask` requires distinct labels, invokes
`QUERY(i,j)`, obtains only the smaller label as answer, appends that
answer to `H`, increments `q`, and branches on that answer. The program
has no other access to the hidden total order `X`. `Emit` fills one
previously unwritten output position. `Halt` is a program action only;
it succeeds at the verifier only if exactly a permutation of `[n]` has
been emitted, `q<=k`, and the output is sorted according to `X`.
In particular, consistency with the queried comparisons alone is not
enough: for `n>=2`, a zero-query constant output fails for some
permutation `X`.

For fixed `c`, let `T=(n+k+|p|+2)^c`. The verifier, given an explicitly
encoded permutation `X` of `[n]`, simulates `U` for at most `T` charged
steps, answering each `QUERY` from `X` and rejecting if there are more
than `k`; after a valid `Halt`, this *outer verifier* checks the full
output is increasing in `X` (as well as being a permutation). The
program sees only charged query answers; only the verifier sees `X`.
The quantified predicate is
`exists p (|p|<=b) . forall X in S_n, Verify(p,X,n,k)`.
For polynomially bounded `b` and the fixed polynomial clock, this
defines a restricted language in `Sigma_2^P`. Its soundness implies
`S(n)<=k`; completeness for all of `SORT-BOUND-U` is not established.
No membership or completeness claim for unrestricted `SORT-BOUND-U`
follows.

## Lemma A (PROVED, paper proof): fixed-variable fragment has polynomial combined complexity

**[paper proof]** For the stated syntax and explicit relational encoding,
each formula `phi in FO(TC)_v` evaluates in `O(|phi| N^(2v))` time using
bottom-up truth tables. The tables are memoized by syntax occurrence and
assignment to that subformula's free variables; no subformula is
re-evaluated inside a parent loop. The bound assumes standard unit-cost
table indexing for `O(log N)`-bit tuple indices, or a conventional
deterministic implementation with the resulting polylogarithmic factor
absorbed by a harmless `N^epsilon` exponent adjustment. To retain the
stated exponent literally, count table accesses as unit-cost operations.

*Proof.* A table for a subformula with `f<=v` free variables has at most
`N^f` entries. Atomic tables are filled by scanning their assignments
and looking up explicitly stored relation tuples. Boolean tables are
formed by entrywise operations (including projections for any variable
renaming), and a quantifier table is formed by scanning at most `N`
values per assignment, for `O(N^(f+1)) <= O(N^(v+1)) <= O(N^(2v))`
work. This accounts for each node once, even when a child occurs under
many parent assignments, because its table is reused.

At a TC node with endpoint width `m` and outside context width `a`,
`a+2m<=v`. Its defining subformula's truth table supplies all edge
answers for each context assignment and each source/target pair. For
each of the `N^a` contexts, construct the graph on at most `N^m` nodes
and compute its reflexive transitive closure by Floyd--Warshall, costing
`O(N^(3m))`; edge-table construction/lookups cost at most
`O(N^(a+2m))`. Thus the node costs
`O(N^(a+3m) + N^(a+2m)) = O(N^(a+3m))`. Since
`a+3m <= 2(a+2m) <= 2v`, this is `O(N^(2v))`, including nested TC:
each nested closure has its own memoized table and is charged once in
the same bottom-up sum. With at most `|phi|` syntax nodes this gives
`O(|phi|N^(2v))`. For a fixed vocabulary of arity at most `v`, the
explicit input/store tables and initial history have size and
construction cost `O(N^v)` (plus `O(|p|)` to parse the program); these
are absorbed for `v>=1`. The interpreter per rule evaluation has
polynomial overhead in the syntax/table bound. Choose the fixed clock
exponent `c` large enough to dominate that overhead: across at most `T`
program steps/evaluations, total runtime is bounded by `T` times that
per-evaluation polynomial, plus store updates and input construction,
and hence by a fixed polynomial in `n+k+|p|`. This is a polynomial
verifier clock, not a claim that the whole program costs just one
formula-evaluation bound. The `FO(TC)=NL` capture theorem is not used.
QED.

Corollary: for any fixed polynomial bound `b(n+k)` and fixed verifier
clock exponent as above, the restricted predicate `QWIN_{v,c}` is in
`Sigma_2^P`: guess `p`, universally quantify an `O(n log n)`-bit
permutation encoding, validate it, and run the verifier. Soundness:
acceptance implies `S(n)<=k`. Completeness (every `S(n)<=k` has such a
program) remains OPEN; this does not establish unrestricted
`SORT-BOUND-U` membership in `Sigma_2^P`.

## Lemma B (PROVED, scoped barriers): explicit trees and two specified compiler methods

**[paper proof]** B1 (explicit trees). A correct sorting tree must have
at least `n!` leaves (distinct permutations force distinct answer paths;
two permutations reaching the same leaf would receive the same output
order, wrong for at least one). Hence any compiler emitting the explicit
optimal tree outputs `Omega(n!)` nodes: superpolynomial in `n+k`.

**[literature + deduction, scoped]** B2 concerns two narrower methods.
First, the greedy child-`e` selector chooses a comparison `{x,y}` by
minimizing `max(e(P+xy),e(P+yx))`. Computing this selector by explicitly
counting linear extensions uses the function `e(P)`, whose exact counting
is #P-complete (Brightwell-Winkler, *Order* 8(3), 1991). This is a
barrier to that particular implementation of the greedy selector; it
does not show that the exact minimax recurrence
`F(P)=1+min_{x,y} max(F(P+xy),F(P+yx))` needs `e(P)`, nor that exact
minimax evaluation or optimal comparison selection is #P-hard.
Second, the winning-frontier construction
(`docs/research-winning-frontier-barrier.md`) exhibits
`2^{(1/4-o(1)) n (log n)^2}` nonisomorphic winning posets at one depth.
It therefore rules out methods whose work requires explicitly listing
the entire frontier at that depth (even modulo isomorphism). It does not
force every memoizing algorithm or compiler to enumerate those states.
In particular, neither result rules out a polynomial exact recurrence
evaluator, a selective compiler, state compression, or another method
that avoids these specified steps. These are scoped method barriers,
not a hardness claim about computing `S(n)` or about the sparse unary
`SORT-BOUND-U`.

## Findings

- **PROVED:** `FO(TC)_v` (fixed variables/arity) compiles to uniform
  polytime query programs with explicit `O(|phi| . N^{2v})` evaluation.
- **PROVED (scoped barriers):** an explicit optimal sorting tree has
  `Omega(n!)` leaves; explicitly counting `e(P)` for the greedy
  child-`e` selector invokes a #P-complete function; and explicit full
  winning-frontier enumeration has superpolynomial size for the stated
  family. None rules out polynomial exact minimax evaluation or
  selective compilation.
- **CONDITIONAL:** all-`n` exact completeness of the fragment (every
  `S(n) <= k` realized by a poly-size fragment program at exact budget)
  would place that subclass of `SORT-BOUND-U` in `Sigma_2^P`.
- **NOT CLAIMED:** unrestricted-FO(TC) polytime evaluation; `NP` or
  `Sigma_2^P` membership of unrestricted `SORT-BOUND-U`; hardness of
  computing `S(n)`.
- **OPEN:** prove or refute fragment completeness at exact optimal depth;
  or separate fragment-expressible strategies from general optimal trees.

## Elementary strategy examples

**[deduction from standard algorithms]** The interpreter can implement
binary-insertion sort using midpoint `Ask` operations over each sorted
prefix. It makes at most
`sum_{i=1}^{n-1} ceil(log2(i+1))` queries and `O(n log n)` rule actions;
the loop schema is fixed, with `O(log n)` bits for binary-encoded indices
and `n` when passed as a parameter. Top-down merge sort uses `O(n log n)`
queries and control actions, with a fixed recursive schema and logarithmic
recursion depth; it observes only results of explicit `Ask` operations.
For a fixed small optimal sorter, encode its finite decision tree as one
control label per node: text size `Theta(tree nodes)`, with worst-case
query count exactly its height. That representation is useful for
sanity-checking semantics but is not a uniform polynomial compiler for
all `n` (the leaf bound above applies). These are symbolic program-size
and comparison/action counts, not wall-clock measurements; exact byte
constants depend on bytecode encoding.

**[conjecture, falsifiable]** For every `n`, some optimal adaptive sorter
of depth `S(n)` has an FO(TC) strategy program of size polynomial in
`n+S(n)` and the stipulated uniform polynomial clock. A proof would give
exact completeness for this representation and the corresponding
`Sigma_2^P` upper bound for `SORT-BOUND-U`; a refuting family would be
optimal trees for which every program in the specified fragment exceeds
every fixed polynomial size or clock. No completeness claim is proved.

## Next step

No computational probe is claimed for the paper argument. The decisive
remaining task is an all-`n` proof or refutation of exact-budget
completeness for the specified syntax, not finite enumeration.

### Sources

- Immerman, *Descriptive Complexity* (1999), ch. 7: FO(TC)/NL, fixed
  formulas only; combined bound here is proved directly.
- Brightwell-Winkler, "Counting linear extensions," *Order* 8(3),
  1991: #P-completeness used only for the explicitly-counting greedy
  child-`e` selector in B2.
- Knuth, *TAOCP* vol. 3, section 5.3.1: decision-tree leaf lower bound.
- SoringP1 `docs/problem.md`, `docs/research-winning-frontier-barrier.md`,
  issue #47: model, frontier barrier, framed-DAG context.
