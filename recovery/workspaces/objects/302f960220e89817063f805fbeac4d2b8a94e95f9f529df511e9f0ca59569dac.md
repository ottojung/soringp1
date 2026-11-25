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

**[definition]** A *query program* is a finite byte string `p` run on a
fixed deterministic machine `U` with mutable state. The only operation
observing the hidden total order on `[n]` is `QUERY(i,j)` (distinct
labels), returning the smaller label and incrementing the comparison
counter. All other steps (control, arithmetic, memory, output) are
ordinary charged machine steps. A run is clocked at
`T = (n+k+|p|+2)^c` for a fixed constant `c`; it accepts iff it halts
within `T`, outputs a permutation of `[n]` consistent with all answers,
and used at most `k` queries.

**[definition]** `FO(TC)_v`: first-order logic with transitive closure
where every subformula uses at most `v` distinct variable names
(`v` fixed, arity likewise bounded by `v`). Formula *text* `|phi|` may
grow (it is the guessed part); the domain size is `n` (labels) plus
`O(k)` history slots. A *fragment program* is a finite list of
`FO(TC)_v` rules selecting the next comparison / output from the
knowledge structure (observed outcomes plus their closure); every rule
evaluation is charged, and `QUERY` answers are the only hidden-order
input (no free transitive-closure oracle over the unknown order).

**[definition]** Operationally, a program has a control label, an output
buffer of `n` labels, query history `H(i,j,b)`, and a query counter `q`.
At a nonterminal label an FO(TC) rule over `H` and its derived closure
returns one action: `Ask(i,j)`, `Emit(position,i)`, `Goto(label)`, or
`Halt`. Rules are deterministic; malformed or non-singleton actions
reject. `Ask` requires distinct labels, calls the comparison oracle,
appends its answer to `H`, increments `q`, and branches to a successor
according to the answer. `Emit` fills one previously unwritten position.
`Halt` succeeds only if the buffer is a permutation consistent with all
answers. There is no predicate on the hidden order other than a charged
`Ask`. Rule evaluation and store updates are charged interpreter steps;
the run must halt within the uniform polynomial clock `T` above and use
at most `k` queries. This specifies mutable knowledge/state, branching,
output and termination without granting a free order oracle.

Program choice and adversarial verification have distinct quantifiers:
`exists p, |p|<=b . forall total orders X, Verify(p,X,n,k)`. Under the
uniform clock/interpreter this puts the representable subclass in
`Sigma_2^P`; it does not place unrestricted `SORT-BOUND-U` there absent
completeness.

## Lemma A (PROVED, paper proof): fixed-variable fragment has polynomial combined complexity

**[paper proof]** Claim: for fixed `v`, any `phi in FO(TC)_v` over a
domain of size `N` evaluates in `O(|phi| . N^{2v})` deterministic time
by direct induction, hence polynomial in `|phi| + N` jointly.

*Proof.* Evaluate bottom-up. An atomic or Boolean step scans at most
`N^v` assignments (one per variable binding). A quantifier step iterates
over at most `N` values per bound variable: `O(N^{v+1}) <= O(N^{2v})`
for `v >= 1`. A `TC` step over a `2m`-ary definable relation
(`m <= v/2` given bounded arity) materializes a graph on at most `N^m`
nodes and runs reachability in `O(N^{3m}) <= O(N^{2v})` (Floyd-Warshall;
BFS per source gives the same polynomial). Summing over the `|phi|`
subformula occurrences gives `O(|phi| . N^{2v})`. With `N = O(n+k)`
(history-augmented knowledge structure) and fixed `v`, compiling each
rule to `U` preserves this bound up to a fixed polynomial overhead, so
the fragment interpreter is uniform-polytime in `(n, k, |p|)`.
The `FO(TC) = NL` capture theorem (Immerman, *Descriptive Complexity*,
ch. 7) is data complexity for each *fixed* formula and is NOT used as a
combined-time claim; the bound above is proved directly. QED.

Corollary: the subclass `QWIN_{v,c}` (fragment programs of size
`<= b` passing all `n!` orders within clock `T`) is in `Sigma_2^P`:
guess `p`, universally quantify an `O(n log n)`-bit permutation, run
the fixed clocked verifier. Soundness: acceptance implies `S(n) <= k`.
Completeness (every `S(n) <= k` has such a `p`) remains OPEN.

## Lemma B (PROVED barrier, paper proof + literature): the recurrence/table compiler is not polytime

**[paper proof]** B1 (explicit trees). A correct sorting tree must have
at least `n!` leaves (distinct permutations force distinct answer paths;
two permutations reaching the same leaf would receive the same output
order, wrong for at least one). Hence any compiler emitting the explicit
optimal tree outputs `Omega(n!)` nodes: superpolynomial in `n+k`.

**[literature + deduction]** B2 (optimal-next-comparison recurrence).
The natural recurrence compiler picks the next comparison by solving the
minimax remainder `F(P)` over reachable knowledge posets `P`. Exact
evaluation of the information-theoretic recurrence needs the linear-
extension count `e(P)`; counting linear extensions is **#P-complete**
(Brightwell-Winkler, *Order* 8(3), 1991). So this recurrence cannot be
evaluated in polynomial time unless `FP = #P`. Independently, the
winning-frontier construction (`docs/research-winning-frontier-barrier.md`)
exhibits `2^{(1/4-o(1)) n (log n)^2}` nonisomorphic winning posets at one
depth, so a memoizing/table compiler over reachable states is
superpolynomial in the worst case. Either way the recurrence route is
ruled out as a *polytime exact* compiler. Per `AGENTS.md` this is a
barrier for the *method* (which queries arbitrary posets), not a
hardness claim for the sparse unary `SORT-BOUND-U` itself.

## Findings

- **PROVED:** `FO(TC)_v` (fixed variables/arity) compiles to uniform
  polytime query programs with explicit `O(|phi| . N^{2v})` evaluation.
- **PROVED (barrier):** explicit-tree and exact-recurrence compilers are
  not polytime routes (leaf bound `Omega(n!)`; `#P`-hard extension
  counting; superpolynomial winning frontier).
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

## Next experiment

Run `scripts/fo_tc_combined_probe.py`: checks the Lemma A cost formula
against a naive evaluator's step counts on small instances and verifies
the B1 leaf-bound arithmetic (`n!` vs polynomial budgets). Next implement
the insertion and merge schemas in the bytecode and instrument action
counts against the bounds above. This checks model fidelity only; the
decisive remaining task is an all-`n` proof or refutation of exact-budget
completeness, not finite enumeration.

### Sources

- Immerman, *Descriptive Complexity* (1999), ch. 7: FO(TC)/NL, fixed
  formulas only; combined bound here is proved directly.
- Brightwell-Winkler, "Counting linear extensions," *Order* 8(3),
  1991: #P-completeness used for B2.
- Knuth, *TAOCP* vol. 3, section 5.3.1: decision-tree leaf lower bound.
- SoringP1 `docs/problem.md`, `docs/research-winning-frontier-barrier.md`,
  issue #47: model, frontier barrier, framed-DAG context.
