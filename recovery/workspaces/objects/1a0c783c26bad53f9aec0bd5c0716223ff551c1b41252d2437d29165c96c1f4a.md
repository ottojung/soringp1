# FO(TC) strategy programs for exact optimal sorting

**Status:** research note (paper-and-literature analysis; no new experiment in this
note). Labels follow the SoringP1 convention: `[definition]`, `[literature]`,
`[deduction]`, `[conjecture]`, `[experiment]`, `[paper proof]`, `[open]`.
No Lean files are added or modified. No unconditional complexity separation is
claimed.

**Scope:** unary encoding only. The target is
`SORT-BOUND-U = { 1^n # 1^k : S(n) <= k }` and the function
`S_unary(1^n)`. All resource statements are measured against the actual input
length `N = n + k + 1` (or `N = n` for the function). The binary encoding
remains defined in `docs/problem.md` but is not an active workstream.

**Coordinates:** umbrella Antonina issue #301 and SoringP1 issue #47 (framed
DAG certificates); this note addresses the FO(TC) strategy-program front
requested by GitHub issue `JTsW4AnxTLzN18IBQibXea-fervor`.

---

## 0. Sharp question and its consequence

**[definition]** Let a *strategy program* `p` be a finite, deterministic description
of an adaptive comparison sorter. Its execution `Run(p, X)` on a hidden total
order `X` on `[n] = {0,...,n-1}` may access `X` only through charged
comparison queries; it maintains mutable knowledge of the order, may branch on
query outcomes, and must terminate by emitting a permutation of `[n]`.

**Question (all-n).** For every `n` with `S(n) <= k`, does there exist a strategy
program `p_{n,k}` such that

1. `|p_{n,k}| = poly(n+k)` (polynomial description size),
2. `Run(p_{n,k}, X)` uses at most `k` charged comparisons for every total order
   `X` on `[n]`, and
3. `Run(p_{n,k}, X)` is executable by a fixed, uniform interpreter in
   polynomial time in `n+k+|p_{n,k}|`?

**Consequence.** If the answer is yes, then the subclass of `SORT-BOUND-U`
realized by such programs lies in `Sigma_2^P` (existential program choice plus
universal verification over input orders). If, in addition, the construction is
uniform and covers every yes-instance, then `SORT-BOUND-U` itself would be in
`Sigma_2^P`, which would be a genuine upper-bound result (membership below
`PSPACE`). If the answer is no for a proposed restriction, that restriction is
ruled out as a route to such a membership proof. No unconditional lower bound
for the sparse unary language is claimed or implied (`AGENTS.md`,
`docs/problem.md`).

A program that first exhaustively searches for an optimal decision tree, or
enumerates all `n!` input orders, inside its own run does **not** satisfy
condition 3: its runtime is not polynomial. Such a program is a proof of
existence, not an executable strategy.

---

## 1. Formal syntax, semantics, and cost accounting

### 1.1 Hidden order, knowledge state, and oracle access

**[definition]** An *instance* is a pair `(n,k)` with `n >= 0`, `k >= 0`.
The hidden input is a total order `X` on `[n]`, equivalently a permutation/rank
function `r_X : [n] -> [n]` with `r_X(i) < r_X(j)` iff `i <_X j`. The program
never sees `r_X` directly.

**[definition]** The *knowledge state* after some comparisons is a transitively
closed strict partial order `P` on `[n]`, represented by an `n x n` boolean
matrix `G` with `G[i][i] = 1` (reflexive reachability) and `G[i][j] = 1` iff
`i <=_P j` is known (i.e. `i < j` in `P` or `i = j`). The state also contains:

- a control label `ell` (index into the program),
- a query counter `q` (number of charged comparisons so far),
- an output buffer `O` (a partial or complete list of labels),
- a binary history relation `H(a,b)` recording that some charged comparison
  returned `a < b` (repeated comparisons are allowed and each is charged; `H`
  records their logical outcome),
- (in the low-level ESP variant, Section 2.4) integer registers.

**[definition]** The only operation that consults `X` is the charged oracle
`ASK(i,j)` (`i != j`): it returns `LT` if `i <_X j` and `GT` otherwise,
increments `q`, and the interpreter updates `G` by transitive closure with the
new edge. No formula, guard, or control expression may depend on `r_X`
directly. This is the "no free access to input order" condition.

### 1.2 Syntax (logical level)

**[definition]** Fix a global variable bound `v >= 2` once for the whole
language. A *state vocabulary* is a finite relational vocabulary of arity at most
`v` over a domain of size `N = Theta(n+k+1)`, containing at least:

- `Eq(a,b)` (equality, available as a logical primitive),
- `Lt(a,b)` (known `a < b` in the current partial order),
- `Unk(a,b)` (incomparable pair, derivable but convenient),
- `H(a,b)` (history of charged answers),
- `Out(pos, a)` (output buffer),
- (in concrete implementations) register tables.

**[definition]** `FO(TC)_v` is the following fixed-variable syntax. Atomic
formulas use equality and the state/input relations; Boolean connectives and
first-order quantifiers have their usual semantics. If `x = (x_1,...,x_m)` and
`y = (y_1,...,y_m)` are disjoint tuples of distinct variable names and `theta`
is a formula, then `[TC_{x,y} theta](s,t)` is allowed when `s,t` are `m`-tuples
and the free variables of `theta` other than the endpoint tuples form a context
tuple `z` of length `a`, disjoint from `x,y`, with `a + 2m <= v`. The edge
relation is `theta` with `x,y` assigned to source and target; closure is
reflexive transitive reachability on the `N^m` endpoint tuples, separately for
each fixed assignment to `z`. All bound and free variables, including those in
nested `TC` formulas, are drawn from the same globally fixed set of at most `v`
names. Formula text `|phi|` may grow with `n,k`.

**[definition]** A *program* `p` is a finite byte string interpreted by a fixed
deterministic machine `U`. At the logical level it is a finite map from control
labels to *rules*. Each rule evaluates an `FO(TC)_v` guard over the current
state and returns exactly one action:

- `Ask(i,j)` with distinct labels `i,j` in `[n]`: charge one comparison,
  query the oracle, update `G` by transitive closure, and branch on the outcome;
- `Emit(position, a)`: fill one previously unwritten output position;
- `Goto(label)`: unconditional control transfer;
- `Halt`: terminate and request verification.

A rule that evaluates to zero actions or to more than one action is *malformed*
and causes rejection. Thus the interpreter is deterministic given `(p, X)`.

**[definition]** The *size* `|p|` is the length of the byte string (equivalently,
the number of rules/symbols plus the encoding of constants and labels). A
polynomial-size certificate requires `|p| = poly(n+k)`.

### 1.3 Semantics

**[definition]** `Run(p, X)` executes as follows:

1. Initialize `G` to the identity/antichain (no strict comparabilities known),
   `q := 0`, `O := empty`, `ell := 0` (entry label).
2. While the current rule at `ell` is not `Halt`:
   - evaluate its guard; if malformed, reject;
   - if `Ask(i,j)`: require `i != j` and `i,j in [n]`; query `X`; set
     `q := q+1`; if `q > k` (or the declared budget) reject; update `G` by
     transitive closure with the new edge `i < j` or `j < i`; set `ell` to the
     outcome branch label;
   - if `Emit(pos,a)`: require `pos` unwritten and `a in [n]`; write `O[pos] := a`;
   - if `Goto(label)`: set `ell := label`.
   - If the step clock is exceeded, reject.
3. On `Halt`: accept (at the verifier) iff `O` is a permutation of `[n]`,
   `q <= k`, and `O` is increasing in `X`. The program itself does not see
   `X`; sortedness is checked by the outer verifier using the explicitly
   encoded `X`.

**[definition]** `p` is *correct for `(n,k)`* iff for every total order `X` on
`[n]`, `Run(p,X)` terminates by `Halt` and is accepted. Its *worst-case
comparison budget* is

```
k(p) = max_{X total order on [n]}  (# Ask steps in Run(p,X)).
```

Correctness with budget `k` means `k(p) <= k`. Soundness (Section 6) then gives
`S(n) <= k`.

**[definition]** *Termination.* Termination occurs only via `Halt` or rejection.
There is no implicit "budget exhausted = success": if `q` exceeds the declared
budget, the run is rejected. A program that never reaches `Halt` on some `X`
is incorrect.

### 1.4 Cost accounting

**[definition]** Costs are accounted in three independent quantities:

1. **Comparison cost** (charged to the sorting problem): each `Ask` costs `1`.
   This is the quantity bounded by `k` and compared to `S(n)`. Oracle answers
   are the only way `X` enters the computation.
2. **Program size** `|p|`: description length in bits/symbols. For certificate
   purposes we require `|p| = poly(n+k)` in the unary input length.
3. **Interpreter cost**: the number of ordinary machine steps taken by the fixed
   interpreter `U` to execute `Run(p,X)`, including guard evaluation, parsing,
   store/history updates, transitive-closure maintenance, query handling, and
   final output checking. This must be `poly(n,k,|p|)` uniformly (Section 2).

**[deduction]** A program of size `poly(n+k)` and interpreter cost
`poly(n+k)` is a *polynomial-time executable* strategy. A program that is small
but whose interpreter cost is exponential (for example, because it contains a
fixed formula whose evaluation is exponential in its own size) does **not**
qualify. This is the central accounting distinction of this note.

---

## 2. Combined evaluation complexity

### 2.1 Data complexity is not combined complexity

**[literature]** For a *fixed* formula `phi` in FO(TC), evaluating `phi` on a
structure of size `N` is in NL (and hence in deterministic polynomial time).
This is the data-complexity capture theorem (Immerman, *Descriptive Complexity*,
ch. 7). It applies when the formula is fixed and only the structure grows.

**[deduction]** The capture theorem does **not** apply when the formula (or
program text) grows with `n`. A growing `FO(TC)` text is a combined-complexity
input: both the "program" and the "structure" vary. Combined complexity of
first-order logic is PSPACE-complete in general, and transitive-closure
extensions can be EXPTIME-hard or worse depending on the exact syntax. Therefore,
writing an `FO(TC)` formula is not, by itself, an upper-bound argument. One
needs either a bounded-variable/arity fragment with an explicit combined bound,
or a fixed interpreter with a proved uniform polynomial-time bound.

**[deduction]** This is why the `Sigma_2^P` accounting in Section 6 is
conditional: the universal verification step is polynomial only if the
interpreter is uniform polynomial-time. Without that, the quantifier pattern
lands in a larger class (for example, NEXP) rather than `Sigma_2^P`.

### 2.2 Lemma A: polynomial combined bound for `FO(TC)_v`

**[paper proof]** For the syntax of Section 1.2 with a fixed variable bound `v`,
each formula `phi in FO(TC)_v` evaluates on an explicitly tabulated structure
of size `N` in time `O(|phi| * N^{2v})`, using memoized bottom-up truth tables
and Floyd-Warshall per `TC` node. The input/store relations have arity at most
`v` and are given explicitly (not as oracles or succinct encodings).

*Proof sketch.* A table for a subformula with `f <= v` free variables has at
most `N^f` entries. Atomic tables are filled by scanning assignments and
looking up explicitly stored relation tuples. Boolean tables are formed by
entrywise operations (including projections for variable renaming), and a
quantifier table scans at most `N` values per assignment, costing
`O(N^{f+1}) <= O(N^{v+1}) <= O(N^{2v})`. Each syntax node is charged once
because its table is memoized and reused, even when it occurs under many parent
assignments.

At a `TC` node with endpoint width `m` and context width `a` (`a + 2m <= v`),
the defining subformula's table supplies all edge answers for each context and
source/target pair. For each of the `N^a` contexts, build the graph on at most
`N^m` nodes and compute reflexive transitive closure by Floyd-Warshall, costing
`O(N^{3m})`; edge-table construction/lookups cost at most `O(N^{a+2m})`. Thus
the node costs `O(N^{a+3m})`. Since `a + 3m <= 2(a + 2m) <= 2v`, this is
`O(N^{2v})`. Nested `TC` nodes are charged the same way, each with its own
memoized table. With at most `|phi|` syntax nodes the total is
`O(|phi| * N^{2v})`. Parsing and initial table construction cost `O(N^v + |p|)`,
absorbed for `v >= 1`.

The bound assumes standard unit-cost indexing for `O(log N)`-bit tuple indices,
or a conventional deterministic implementation with a polylogarithmic factor
absorbed by a harmless `N^epsilon` exponent adjustment. To keep the stated
exponent literally, count table accesses as unit-cost operations.

**[deduction]** Corollary (clocks). Fix `v`, `d`, and an interpreter
implementation `U`. Let `L = n + k + |p| + 2`. A program fits the
`FO(TC)_v` fragment if each guard evaluates within the Lemma A bound and the
interpreter makes at most `L^d` rule applications. Then there is a fixed
exponent `c` (chosen once for that `v`, `d`, and implementation, never per
instance or per program) such that `U` runs in at most `L^c` ordinary
deterministic machine steps, including formula evaluation, parsing, store and
history updates, query handling, and output checking. The exponent `c` must be
stated and fixed; it is not selected after seeing the instance.

**[deduction]** For fixed `v`, `d`, `c`, and any polynomial bound `b(n+k)`, the
restricted predicate

```
QWIN_{v,d,c}(n,k)  :=  exists p (|p| <= b(n+k)) such that
                        for all X in S_n, Verify(p, X, n, k)
```

is in `Sigma_2^P`: guess `p`, universally quantify over the
`O(n log n)`-bit encoding of `X`, validate `X`, and run the verifier. Soundness
(Section 6) gives `S(n) <= k` whenever `QWIN` holds. Completeness (every
`S(n) <= k` has such a `p`) is **open**; no unrestricted `SORT-BOUND-U`
membership follows.

### 2.3 Expressive power lost by the bounded fragment

**[deduction]** Fixing `v` and arity `<= v` is what makes the combined bound
polynomial, but it costs expressive power:

- **Variable/context width.** A `TC` node may have endpoint width `m` and
  context width `a` only when `a + 2m <= v`. For `v = 2`, reachability can
  only relate individual elements (`m = 1`) with no context (`a = 0`); a
  context-dependent transitive closure (for example, "is `y` reachable from
  `x` in a graph parameterized by a third element `z`") requires `v >= 3`. In
  general, properties that need simultaneous quantification over tuples whose
  size grows with `n` cannot be expressed directly; they must be encoded via
  iterated `TC` with fixed width, possibly increasing formula size.
- **Arity of stored relations.** The state vocabulary has arity at most `v`.
  A binary relation such as `Lt` is fine, but a ternary or higher-order state
  (for example, a family of subsets indexed by elements) must be flattened or
  encoded via `TC`. This can make guards longer but does not destroy
  polynomiality for fixed `v`.
- **Fixed exponents.** The clocks `L^d` and `L^c` are fixed once. A program
  family whose natural interpreter cost grows like `n^{omega(1)}` for fixed
  `v` but with an exponent depending on the construction does not fit unless
  that exponent is absorbed into the fixed `c`. If no fixed `c` works, the
  family is outside the certified subclass.
- **No per-instance tuning.** `v`, `d`, and `c` may not be chosen per
  instance, per program, or per hidden order `X`. This prevents the trivial
  trick of letting the formula size and variable count grow just enough to
  encode an exhaustive search.

**[deduction]** The trade-off is explicit: larger `v` gives more expressive
power (wider transitive closures, more context) but raises the polynomial
degree `2v` and the table sizes. The fragment remains polynomial for any fixed
`v`, but the degree is part of the certified bound and must be reported.

### 2.4 Concrete executable witness: ESP interpreter

**[definition + experiment]** The Encoded Strategy Program (ESP) model
(`scripts/encoded_strategy_program.py`, `tests/test_encoded_strategy_program.py`)
is a lower-level register-machine realization of the same accounting. A program
is a byte/JSON object

```
p = (n_decl, k_decl, regs, code, out_mode)
```

with instructions `HALT`, `EMIT_PERM`, `EMIT_REG`, `SET`, `COPY`, `INC`, `DEC`,
`JMP`, `JZ`, `JNZ`, `JLT`, and `ASK r_i r_j r_out`. Mutable state is
`(G, q, out)` where `G` is the `n x n` transitive closure matrix; `ASK` is the
only access to `X`; transitive closure is maintained after each answer. Register
values are magnitude-bounded by `M = n + k + |code|`.

**[paper proof]** The uniform interpreter `U_ESP` runs in time

```
O(T(p,X) * n^2 * polylog M) + O(|p|)
```

where `T(p,X)` is the number of executed instructions. Per `ASK` step, oracle
lookup is `O(1)` and closure maintenance is `O(n^2)` (or `O(n^3)` in a naive
full recomputation, still uniform polynomial). Validation and output checking
cost `O(n^2 + |code|)`. Thus, if `T(p,X) <= poly(n,k)` for all `X`, the
interpreter is uniform polynomial-time. This is a combined bound (program is
data to a fixed interpreter), not a fixed-formula data-complexity claim.

**[experiment]** The ESP tests validate optimal programs for `n <= 4`, exhaustive
charged-oracle simulation for binary insertion and standard top-down merge sort
for `n <= 8`, and rejection cases. They support the accounting model but do
not establish all-n completeness.

---

## 3. Elementary examples

### 3.1 Insertion sort (restricted upper-envelope family)

**[deduction]** Binary insertion sort maintains a sorted prefix and inserts each
new element by binary search over the prefix using charged comparisons
`(y, x)`. Each comparison adds an order fact; transitive closure updates the
state. The worst-case comparison count is

```
B(n) = sum_{i=1}^{n-1} ceil(log2(i+1)) <= n log2 n.
```

This is a fixed adaptive strategy whose control decisions depend only on prior
`ASK` outcomes and the fixed insertion schedule; it never reads `r_X` directly.

**[deduction + experiment]** In a RAM/array-addressed extension of ESP, a
parametric control schema has `O(log n)`-bit parameter encoding and step clock
`O(n^2 log n)`, hence uniform polynomial time. In the minimal register-only
ISA, an explicit per-`n` unfolding is a decision structure whose size is
polynomial only when that structure is compressible. The ESP checker validates
the strategy exhaustively for `n <= 8`.

**[deduction]** `B(n)` is not uniformly optimal: `B(5) = 8 > S(5) = 7`,
`B(6) = 11 > S(6) = 10`, etc. Insertion sort is an upper-envelope witness at
budget `B(n)`, not an exact-`S(n)` completeness witness.

### 3.2 Merge sort (restricted upper-envelope family)

**[deduction]** Standard top-down merge sort splits indices into halves,
recursively sorts, and merges by comparing current front elements. A merge of
sorted lists of sizes `p,q` uses at most `p+q-1` charged comparisons (worst
case when one list is exhausted only at the final comparison), so

```
M(0) = M(1) = 0,   M(n) = M(floor(n/2)) + M(ceil(n/2)) + n - 1  (n >= 2).
```

**[experiment]** Exhaustive simulation for `n <= 8` verifies correct sorting and
attainment of `M(n)`:

| n | M(n) | S(n) (context) | exact at S(n)? |
|---|------|----------------|----------------|
| 1 | 0    | 0              | yes            |
| 2 | 1    | 1              | yes            |
| 3 | 3    | 3              | yes            |
| 4 | 5    | 5              | yes            |
| 5 | 8    | 7              | no             |
| 6 | 11   | 10             | no             |
| 7 | 14   | 13             | no             |
| 8 | 17   | 16             | no             |

`S(n)` values are cited as literature/kernel context only. Merge sort and
binary insertion sort coincide at `M(n)=B(n)` for `n <= 8` in this table, but
they differ asymptotically and neither is uniformly optimal. They remain useful
restricted-family witnesses with polynomial-size programs and polynomial
runtime at their own budgets.

### 3.3 Small optimal sorters

**[deduction]** For a fixed `n`, an optimal decision tree of height `S(n)` can
be encoded as a program with one control label per tree node: size
`Theta(tree nodes)`, query count exactly the height. A single-policy optimal
tree has `2 * n! - 1` nodes (Theorem 2.1/2.5 of
`docs/research-strategy-certificates.md`), so this encoding is exponential in
`n`. It is a semantics sanity check, not a uniform polynomial compiler.

**[experiment]** The ESP implementation checks optimal-height programs for
`n <= 4` (budgets `0,1,3,5`) by exhaustive simulation over all `n!` orders.
For `n = 5` (budget 7), an exact-budget program requires compression beyond
explicit tree enumeration; this is exactly the open completeness step.

**[deduction]** The hash-consed all-optimal DAG can share states (for example,
`DAG(all)` grows from 19 to 65551 for `n = 3..6`), but no polynomial bound is
known, and a single-policy optimal tree has zero hash-consing sharing. Thus
state sharing alone does not yet yield a polynomial compiler.

---

## 4. All-n conjecture (falsifiable)

**[conjecture, falsifiable, open]** Conjecture C (exact completeness). For
every `n >= 0`, there exists an optimal adaptive comparison sorter of depth
`S(n)` that is expressible as a strategy program `p_n` with

```
|p_n| = poly(n + S(n))   and   interpreter cost poly(n + S(n))
```

in a fixed bounded fragment (`FO(TC)_v` with fixed `v,d,c`, or an equivalent
fixed interpreter), such that `k(p_n) = S(n)`.

**[deduction]** If Conjecture C holds, then `QWIN_{v,d,c}` covers all
yes-instances of `SORT-BOUND-U`, and the representable subclass coincides with
the whole language, placing `SORT-BOUND-U` in `Sigma_2^P`. If it fails, the
failure identifies a genuine limitation of rule-based compression.

**What a proof would need.** Not an enumeration of optimal trees. A proof would
require one of:

- a state-compression theorem showing that optimal play visits only
  polynomially many distinct states (or isomorphism classes) under a sound
  quotient, together with a compact rule set for selecting the next comparison;
- a structural characterization of optimal strategies (for example, a uniform
  recurrence or decomposition) whose control flow is polynomial in size;
- a simulation theorem showing that some known polynomial-size certificate
  family (such as the framed DAGs of issue #47) can be executed by a
  polynomial-size program without increasing comparison count.

**What would refute a proposed restriction.** A refutation must exhibit an
infinite family of `n` for which every program in the specified fragment either
has super-polynomial size or super-polynomial runtime, while still sorting
optimally. Candidate pressure points already known:

- **Split-schema barrier.** Fixed `m`-subset-first strategies miss several
  exact cells: `(m,n) = (4,6), (3,6), (4,7), (6,9)` are not exact, while
  `(5,8)` is exact. A uniform split schema is therefore insufficient for all
  `n` (`docs/research-fo-tc-split-schema.md` if available; the barrier is also
  recorded in the framed-certificate frontier). This rules out one natural
  family of polynomial programs, not all.
- **Exact-reset divisibility.** For odd `n >= 3`, an exact reset from the
  antichain `A_n` to the star poset `V_n` is impossible because the root
  comparison splits `n!/2` orders, which is not a multiple of `(n-1)!` when
  `n` is odd (`docs/research-exact-reset-realizability.md`). This is a
  branch-level obstruction to exact join transitions, relevant to forgetful DAG
  compression.
- **Tree size.** A single optimal policy has `2*n! - 1` nodes, so storing the
  tree explicitly is impossible in polynomial size. Any polynomial program must
  compress the strategy, not the tree.
- **Winning-frontier size.** There are `2^{(1/4 - o(1)) n (log n)^2}`
  nonisomorphic winning posets at one depth, even at budget `S(n)`
  (`docs/research-winning-frontier-barrier.md`). Explicit enumeration of the
  frontier is ruled out, though selective methods are not.
- **State-count exponent.** Both labelled posets `A001035(n)` and unlabelled
  quotient classes `A000112(n)` are `2^{Theta(n^2)}`. Symmetry compression
  changes the polynomial factor but not the exponential exponent
  (`docs/research-state-compression.md`).
- **#P barrier.** The greedy rule "choose the comparison minimizing
  `max(e(P+xy), e(P+yx))`" requires counting linear extensions, which is
  #P-complete (Brightwell-Winkler). This rules out that particular
  implementation, not exact minimax evaluation itself.

**[deduction]** A program that first exhaustively searches for an optimal tree
violates the runtime condition regardless of its size: the search cost is at
least exponential in `n` (or requires enumerating posets), so it cannot fit a
fixed polynomial clock. Such a construction proves existence but not
membership in a polynomial-time verifiable class.

---

## 5. Forgetful framed DAGs and program compression

### 5.1 Can a logical program simulate a forgetful framed DAG efficiently?

**[deduction]** Yes, up to polynomial overhead, in the following sense. A framed
DAG certificate (issue #47, `docs/research-framed-certificate-frontier.md`) is
an acyclic graph of comparison instructions with permutations and joins. It can
be simulated by a strategy program:

- each DAG node becomes a control label (or a small block) in the program;
- each comparison edge becomes an `Ask` with branch targets for the two
  outcomes;
- a join (intersection of guaranteed relations) becomes a state update that
  retains only comparabilities common to all feasible incoming arcs, which can
  be computed from the stored partial orders or by re-running the incoming
  branches;
- output occurs at terminal nodes when the state is total.

The program's state size is `O(n^2)` bits (the partial order matrix), and the
number of steps is `O(|DAG| * n^2)` under the ESP cost model. Therefore, if a
polynomial-size framed DAG exists for a family, a polynomial-size program with
polynomial runtime exists for that family. Programs are at least as succinct as
framed DAGs up to polynomial factors.

**[open]** The converse is the real question. Programs can compute derived
comparabilities by transitive closure (a `TC` query) and can choose comparisons
adaptively based on derived state, whereas a framed DAG encodes choices only by
explicit nodes and joins. Whether this extra power yields *asymptotic*
compression beyond what framed DAGs achieve is open. Candidate sources of
compression:

- transitive-closure-derived comparisons (avoiding explicit intermediate nodes),
- symmetry quotient (relabeling canonicalization, which can reduce state counts
  by large factors but has its own canonicalization cost),
- parametric schemas (insertion/merge sort style control flow with `O(log n)`
  parameter encoding).

**[deduction]** A program can also simulate a *forgetful* join (where
disjunctive correlations are discarded) by simply not retaining the
correlations: the state is the partial order only, and the interpreter's
transitive-closure maintenance is exactly a forgetful update. Thus forgetfulness
is not an obstacle to simulation; it is the default behavior of the state model.
The open issue is whether forgetting permits (or forces) smaller programs than
explicit DAGs.

### 5.2 Review of finite-model theory (fixed vs. combined)

**[literature]** Immerman's capture theorem: over ordered structures, FO with
least fixed point (FO[LFP]) captures P, FO with partial fixed point (FO[PFP])
captures PSPACE, and existential second-order logic (ESO) captures NP.
Transitive closure logic FO(TC) sits between FO and FO[LFP] and captures NL in
data complexity for fixed formulas.

**[deduction]** The capture theorems are data-complexity statements: the formula
is fixed. For `SORT-BOUND-U`, the PSPACE upper bound (game formulation
`G(n,k)`, alternating Turing machine) implies an FO(PFP) definition exists on
ordered structures, but constructing and validating an explicit formula is
separate work (`docs/research-plan.md`). An FO(LFP) (P) or ESO (NP) definition
would be a new upper bound. One must not infer a smaller-class definition from
a compact-looking informal recursion. In particular, a compact `FO(TC)`
strategy program does not by itself imply FO(LFP) or ESO definability; the
combined complexity and uniformity conditions must be verified (Lemma A).

**[deduction]** The descriptive-complexity route and the strategy-program route
are related but distinct. A strategy program is an executable object with a
uniform interpreter; an FO(PFP) definition is a declarative formula. The
program route aims at `Sigma_2^P` for a subclass via explicit quantifiers over
programs; the declarative route would aim directly at P or NP. Neither is
currently known.

### 5.3 Review of comparator and adaptive sorting literature

**[literature]** The following results are relevant but must not be over-applied:

- Hyafil and Rivest (1976): constructing optimal binary decision trees with
  arbitrary tests is NP-complete. Laber and Nogueira (2004): minimum-height
  decision trees are NP-hard to approximate within `o(log n)`. These concern
  *arbitrary* tests and item sets, not the fixed family of pairwise comparisons
  on `S_n`. No reduction to `S(n)` is known or implied.
- Parberry (1990/1991): `NONSORT` (does a given comparator network sort?) is
  NP-complete; sorting-network verification is coNP-complete. This concerns
  *fixed* networks and the zero-one principle. Adaptive trees existentially
  choose the next comparison, adding a quantifier that changes the problem from
  coNP-shaped to a game. The two models must not be conflated.
- Kahn and Saks (1984), Kahn and Kim (1995), Cardinal et al. (2013): sorting
  under partial information can be done in polynomial time within a constant
  factor of the information bound. The exact optimum `S(P)` for a given poset
  is not known to be polynomial-time computable; counting `e(P)` is #P-complete.
- Brightwell and Winkler (1991): counting linear extensions is #P-complete.
  They note that easy counting would immediately yield the optimal next
  comparison. This is a barrier to the counting-based greedy selector, not a
  hardness theorem for `S(n)`.
- Wells (1965), Peczarski (2004/2012), Stober and Weiß (2022/2023): exact
  values through `n = 22`, with `S(12) = 30 > ceil(log2 12!) = 29`. These
  proofs are exhaustive searches over posets, not succinct certificates.
- Sergeev (2020): `S(n) - log2(n!) = O(n / (log n)^{1/5}) = o(n)`. The
  sharper behavior (including whether the excess is unbounded) is open.
- Framed DAGs (issue #47): a sound polynomial-time checker exists for explicit
  graphs; merge-sort and rank-envelope constructions give polynomial-size DAGs
  for upper bounds, but optimal-size completeness is open. Parberry's
  coNP-completeness for arbitrary networks is a reason to avoid demanding
  proofs for all programs, not a barrier to one optimal sorter per `n`.

**[deduction]** The "candidate succinct forms" table of
`docs/research-certificates-barriers.md` (Section 4) summarizes the status:
explicit trees are `2n! - 1` nodes; DAG compression has no polynomial bound;
programs are "poly possible" but no polytime universal verifier is known;
inductive potentials are unknown. The strategy-program front is the attempt to
make the "program" row concrete and verifiable.

---

## 6. Existential program choice vs. universal adversarial outcomes

**[definition]** Let `Verify(p, X, n, k)` be the predicate that the fixed
interpreter `U` accepts `Run(p, X)` with at most `k` comparisons and emits a
permutation sorted according to `X`. Define

```
V(p, n, k)  :=  for all total orders X on [n], Verify(p, X, n, k).
```

The decision problem for a fixed representable class is

```
QWIN_{v,d,c}(n,k)  :=  exists p with |p| <= poly(n+k) such that V(p, n, k).
```

**[deduction] Soundness.** If `QWIN_{v,d,c}(n,k)` holds, then there is a
program that sorts all `X` within `k` comparisons, hence an adaptive
comparison strategy of height `<= k`, so `S(n) <= k`. Soundness does not
require any size bound on `p` beyond what the quantifier provides; it requires
only that the interpreter's execution matches the model (charged queries,
transitive-closure state, no free access to `X`).

**[deduction] Why universal verification is `Sigma_2^P` only given a uniform
polynomial interpreter.** The predicate `V(p,n,k)` universally quantifies over
`X` (there are `n!` of them, exponentially many in the input length). For a
fixed `p` that fits the uniform polynomial clock, a counterexample `X` (an order
on which `p` fails or exceeds `k`) can be guessed and verified in polynomial
time: guess an `O(n log n)`-bit encoding of `X` (or a consistent comparison
path), run `p` under `U`, and check failure. Hence `V(p,n,k)` is in `coNP`
relative to `p`. Adding the existential guess of `p` (polynomial size) gives
`Sigma_2^P`.

If the interpreter is **not** uniform polynomial-time, this step fails. Evaluating
a growing `FO(TC)` text naively can take time exponential in `|p|`; then
verifying a fixed `p` is not polynomial, `V(p,n,k)` is not in `coNP`, and the
quantifier pattern `exists p forall X` no longer yields `Sigma_2^P`. It may
yield NEXP or a larger class. This is why the combined bound (Lemma A, ESP) is
not a technicality but the load-bearing condition for the class membership.

**[deduction]** `QWIN` is a statement about a *representable subclass*. It does
not imply `SORT-BOUND-U in Sigma_2^P` unless Conjecture C (or an equivalent
completeness theorem) shows that every yes-instance has such a program. It also
does not imply `SORT-BOUND-U in NP`: NP would require a polynomial-size
certificate with a polynomial-time verifier for yes-instances, and the
universal quantifier over `X` would have to be eliminated or shown redundant.
CoNP membership would require polynomial refutation certificates for no-instances,
which are not known. Neither NP nor coNP membership is claimed.

**[deduction]** The sparse-set barrier (Mahaney) says that `SORT-BOUND-U` is not
NP-hard under polynomial-time many-one reductions unless `P = NP`. This is a
barrier to hardness proofs, not a membership proof. It is compatible with
`SORT-BOUND-U` being in P, NP, coNP, `Sigma_2^P`, or none of these.

---

## 7. Failed approaches preserved

The following negative or partial results are retained because they constrain
future attempts. None of them is a final lower bound for all programs.

1. **Fixed split schemas.** Sorting a fixed `m`-subset first and then completing
   gives a lower bound `S(m) + ceil(log2(n!/m!))`. Several cells are not exact
   (for example `(4,6)`, `(3,6)`, `(4,7)`, `(6,9)`), so a uniform split point
   does not yield optimal programs for all `n`. Cell `(5,8)` is exact. This
   rules out one natural family of polynomial programs.
2. **Exact-reset divisibility.** For odd `n >= 3`, an exact reset from the
   antichain `A_n` to the star poset `V_n` is impossible because `n!/2` is not
   divisible by `(n-1)!`. Extension-count divisibility alone is not sufficient.
3. **Linear-extension count is not a sufficient statistic.** Two posets on 5
   elements with the same number `e(P) = 8` of linear extensions can have
   different minimax values (`F = 3` vs `F = 4`). Hence no state that is a
   function of `e(P)` alone can compute `S(n)`.
4. **Balanced-greedy restricted trees.** The class that always compares a pair
   minimizing the larger child's linear-extension count is optimal for
   `n <= 8` but returns `20` for `n = 9` while `S(9) = 19`. Restricted tree
   classes do not preserve the optimum.
5. **Explicit tree storage.** A single optimal policy has `2*n! - 1` nodes, so
   storing the tree is exponential. Hash-consing saves nothing in a single
   policy (distinct nodes have distinct labelled posets).
6. **All-optimal DAG size.** Hash-consing helps (for example, `DAG(all)` is
   65551 at `n = 6` vs. `2*720 - 1 = 1439` for a single policy), but the
   quotient by `S_n` still grows (19 to 134 from `n = 5` to `n = 6`), and no
   polynomial bound is known.
7. **State-count exponent.** Both `A001035(n)` and `A000112(n)` are
   `2^{Theta(n^2)}`. Symmetry compression does not change the exponent.
8. **#P barrier for greedy selection.** The child-`e` selector requires counting
   linear extensions, which is #P-complete. This is a barrier to that
   implementation only.
9. **Winning-frontier enumeration.** There are super-polynomially many
   nonisomorphic winning states at one depth. Methods that must list the
   frontier are ruled out; selective methods are not.
10. **FO(TC) = NL is not enough.** Using the capture theorem directly for
    growing program texts would be a category error (data vs. combined
    complexity). This is the reason Lemma A and the fixed clocks are stated
    explicitly.

---

## 8. Known vs. conjectured vs. open

| Statement | Status |
|---|---|
| `FO(TC)_v` evaluates in `O(|phi| N^{2v})` (Lemma A) | `[paper proof]` |
| Fixed clocks `L^d`, `L^c` dominate simulation | `[paper proof]` (given `v,d` and implementation) |
| `QWIN_{v,d,c}` in `Sigma_2^P` for representable subclass | `[deduction]` (conditional) |
| Soundness: acceptance implies `S(n) <= k` | `[deduction]` |
| ESP interpreter combined bound `O(T n^2 polylog M)` | `[paper proof]` + `[experiment]` |
| Insertion sort `B(n) <= n log2 n` comparisons, poly size/time | `[deduction]` + `[experiment]` |
| Merge sort `M(n)` comparisons, poly size/time | `[deduction]` + `[experiment]` |
| Single optimal policy has `2*n! - 1` nodes | `[deduction]` + `[experiment]` |
| Optimal programs for `n <= 4` at exact budgets | `[experiment]` |
| Conjecture C: all-n exact completeness | `[conjecture, open]` |
| Programs simulate framed DAGs with poly overhead | `[deduction]` (simulation), completeness `[open]` |
| Programs compress DAG families asymptotically | `[open]` |
| `SORT-BOUND-U in Sigma_2^P` (unrestricted) | `[open]`; not claimed |
| `SORT-BOUND-U in NP` or `coNP` | `[open]`; not claimed |
| `SORT-BOUND-U` NP-hard (many-one) | would imply `P = NP` (Mahaney) |
| `FO(LFP)`/`ESO` definition of `SORT-BOUND-U` | `[open]`; not inferred |

---

## 9. Next decisive step

No finite enumeration is the main result. The decisive remaining task is an
all-n proof or refutation of Conjecture C for a precisely delimited fragment:
either (a) a uniform construction mapping each `(n,k)` with `S(n) <= k` to a
program of polynomial size and polynomial runtime at exact budget `k`, or (b) an
infinite family forcing super-polynomial size or runtime. Small cases (`n <= 8`)
can calibrate definitions and cost accounting, but the result must be all-n.

### Primary sources

- Immerman, *Descriptive Complexity* (1999), ch. 7: FO(TC)/NL data
  complexity; capture theorems.
- Chandra, Kozen, Stockmeyer, *Alternation*, J. ACM 28(1) (1981): APTIME =
  PSPACE, AEXPTIME = EXPSPACE.
- Mahaney, *Sparse complete sets for NP*, JCSS 25(2) (1982): sparse NP-hard
  implies `P = NP`.
- Brightwell and Winkler, *Counting linear extensions is #P-complete*, STOC
  1991.
- Kahn and Saks, *Every poset has a good comparison*, STOC 1984; Kahn and
  Kim, *Entropy and sorting*, JCSS 51(3) (1995); Cardinal, Fiorini, Joret,
  Jungers, Munro, *Sorting under partial information*, Combinatorica 33(6)
  (2013).
- Hyafil and Rivest, *Constructing optimal binary decision trees is
  NP-complete*, IPL 5(1) (1976); Laber and Nogueira, *On the hardness of the
  minimum height decision tree problem*, DAM 144(1-2) (2004).
- Parberry, *On the computational complexity of optimal sorting network
  verification*, LNCS 506 (1991).
- Wells (1965); Peczarski, *New results in minimum-comparison sorting*,
  Algorithmica 40 (2004); Peczarski, *Towards optimal sorting of 16 elements*,
  Acta Univ. Sapientiae Inform. 4(2) (2012); Stober and Weiß, *Lower bounds
  for sorting 16, 17, and 18 elements*, arXiv:2206.05597 (2022).
- Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096 (2020).
- Kleitman and Rothschild, *Asymptotic enumeration of partial orders*, Trans.
  AMS 205 (1975): `2^{Theta(n^2)}` posets.
- Framed certificate frontier: `docs/research-framed-certificate-frontier.md`
  and issue #47.
- SoringP1 internal notes: `docs/problem.md`, `docs/research-plan.md`,
  `docs/research-certificates-barriers.md`,
  `docs/research-strategy-certificates.md`,
  `docs/research-state-compression.md`,
  `docs/research-exact-reset-realizability.md`,
  `docs/research-winning-frontier-barrier.md`,
  `docs/research-budgeted-dfs.md`, `docs/upper-bound.md`.