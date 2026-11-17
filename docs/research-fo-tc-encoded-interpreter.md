# Encoded strategy programs with a uniform polynomial-time interpreter

**Status:** bounded research increment (spec + checked restricted-family encoding).
Labels: `[definition]`, `[deduction]`, `[experiment]`, `[paper proof]` (elementary
combined bound) `[conjecture, open]` (exact all-n completeness).

This note is distinct from `docs/specs/S2-strategy-program-fragment.md` (pinned
`FO(TC)_v`/`QWIN` fragment): it gives an explicit low-level **encoded
instruction syntax** and a concrete **uniform interpreter** `U_ESP` with a
machine-checkable implementation (`scripts/encoded_strategy_program.py`) and
tests. It does **not** claim unrestricted `SORT-BOUND-U` membership and does
**not** claim all-n exact completeness.

## 1. Instance and oracle model

- Parameters: `n >= 1`, budget `k >= 0`. Labels are `[n] = {0,...,n-1}`.
- Hidden input: a total order `X` on `[n]`, equivalently a permutation/rank
  function `r_X : [n] -> [n]` with `r_X(i) < r_X(j)` iff `i <_X j`.
- **Charged comparison oracle** `ASK(i,j)` (`i != j`): returns `LT` if
  `i <_X j` else `GT`, increments the comparison counter `q`, and is the
  **only** access to `X`. The interpreter/verifier may later check a produced
  output against `X`; the program's control flow and state updates may depend
  only on its own mutable state and oracle answers, never on `r_X` directly.

## 2. Encoded syntax (ESP)

A program is a finite byte/JSON-encodable object

    p = (n_decl, k_decl, regs, code, out_mode)

- `n_decl,k_decl` are declared bounds (the verifier checks `n == n_decl`,
  `k <= k_decl` for the instance; the same encoding may be instantiated per
  `(n,k)` by setting these fields).
- `regs >= 0`: number of integer registers `R[0]..R[regs-1]`, all initialized
  to `0`. Register values are required to stay in `[-M, M]` for `M = n+k+|code|`
  (enforced; overflow rejects).
- `code` is a list of instructions indexed by `pc = 0..m-1`, `m = |code|`,
  each one of:

| Instruction | Semantics (one step unless stated) |
|---|---|
| `HALT` | stop; success iff output valid (Sec. 3) and `q <= k_decl` |
| `EMIT_PERM` | set output to the current total order implied by state (see below); requires state total |
| `EMIT_REG r` | append `R[r]` to output buffer (used by explicit-output programs); requires value in `[n]` and unused |
| `SET r c` | `R[r] := c` |
| `COPY r s` | `R[r] := R[s]` |
| `INC r` / `DEC r` | `R[r] := R[r] ± 1` |
| `JMP a` | `pc := a` |
| `JZ r a` / `JNZ r a` / `JLT r s a` | conditional jumps |
| `ASK r_i r_j r_out` | oracle query on `(R[r_i],R[r_j])`; stores outcome bit in `R[r_out]` (1 if LT else 0); charges `q := q+1`; rejects if labels invalid/equal or `q > k_decl` |

`out_mode` is `STATE_TOTAL` (output is read from final state by `EMIT_PERM`) or
`BUFFER` (output is the sequence written by `EMIT_REG`).

**Encoding size.** Each instruction is a constant-arity tuple of integers whose
magnitudes are `<= max(m,n,k_decl,regs)`; therefore

    |p| = O((m + regs) * log (2 + m + n + k_decl))  bits.

So a family with `m, regs = poly(n,k)` has polynomial-size encodings.

## 3. Mutable state and semantics

Mutable knowledge state is `S = (G, q, out)` where:

- `G` is the current **comparability graph / partial order closure** represented
  as an `n x n` boolean matrix with `G[i][i]=1` and, whenever known, `G[i][j]=1`
  meaning `i < j` in the current knowledge. After every `ASK` answer, the
  interpreter performs **transitive closure maintenance** by boolean path closure
  over the updated edge (Floyd–Warshall-style relaxation on the matrix, or
  equivalently closure propagation) so `G` always stores the deduced partial
  order. Only oracle outcomes and logical consequence (transitivity) update `G`.
- `q` is the number of charged `ASK` steps.
- `out` is the output buffer/permutation.

A run on `(p,X,n,k)` is the step-by-step execution from `(pc=0, R=0, G=I_n,
q=0, out=empty)`. `ASK` is the only point where `X` is consulted. `EMIT_PERM`
is legal only when `G` is a total order; it emits the unique linear extension.
`HALT` accepts iff the emitted object is a permutation of `[n]` sorted
according to `X` and `q <= k_decl <= k` (or the instance budget condition
checked by the verifier).

**Soundness (deduction).** If `U_ESP(p,X,n,k)` accepts for all total orders
`X`, every accepting run emits a correct sort and uses `<= k` charged
comparisons, hence the decision-tree height of the realized strategy is `<= k`
and `S(n) <= k` (witnessed by this explicit adaptive strategy).

## 4. Uniform interpreter and combined time bound

`U_ESP` is a single fixed algorithm (independent of the family, except through
the encoded input `p`): it decodes `p`, validates bounds/operands, and executes
instructions in a loop.

Let `m = |code|`, `M = n+k+m`, and let `T(p,X)` be the number of executed
instruction steps until `HALT`/reject.

- **Per non-ASK step:** `O(1)` register/pc operations on `O(log M)`-bit values
  under the enforced magnitude bound.
- **Per ASK step:** oracle lookup `O(1)` plus transitive-closure maintenance on
  `n` elements. Using boolean-matrix closure propagation this is `O(n^2)` word
  operations (and `O(n^3)` in a naive full recomputation upper bound). Crucially
  this is bounded by `poly(n)` **uniformly**, independent of which program `p` is
  run.
- **Validation/output check:** `O(n^2 + m)`.

Therefore the total combined running time is

    Time(U_ESP, p, X, n, k) = O(T(p,X) * n^2 * polylog M) + O(|p|),

a uniform polynomial in `(n, k, |p|, T(p,X))`. Equivalently, if `p` declares or
satisfies a step clock `T(p,X) <= C(n,k)` for all `X`, then runtime is
`poly(n,k,|p|)` uniformly. This is the required **combined** bound (program is
data to a fixed interpreter), not a fixed-formula data-complexity claim.

**Budget honesty.** A program that searches for an optimal tree or enumerates
orders/permutations inside its own run must pay that work in `T(p,X)` and thus
in runtime; it cannot satisfy a polynomial runtime bound except where such
search is itself polynomially bounded (no such general bound is assumed).

## 5. Restricted-family polynomial-size encoding (proved/checkable)

### 5.1 Fixed adaptive decision trees (instance-wise, bounded height)

**[deduction]** Any adaptive comparison strategy given explicitly as a decision
tree of height `h` on `n` labels is encodable as an ESP program by a
straight-line/tree-unfolding encoding: one `ASK` node becomes one `ASK` plus
branches over `pc` targets (a binary decision structure over the outcome
register), leaves emit the total order. This yields

    m, |p| = O(N_h * polylog(n+h)),   q <= h,

where `N_h` is the number of tree nodes (`N_h <= 2^(h+1)-1`).

- **Polynomial when the explicit strategy is polynomial-size:** for fixed/small
  `n` (hence `S(n)` known/constant) optimal trees have constant/explicit size;
  the implementation checks optimal-height programs for `n <= 4`.
- **Not a uniform all-n compiler:** for general `n`, an optimal tree may have
  exponentially many nodes, so this encoding is **not** polynomial-size in `n`
  and does **not** establish completeness. This is exactly the compression gap.

### 5.2 Binary insertion sort family (restricted, charged comparisons)

**[deduction + experiment]** Binary insertion sort on `n` elements uses at most

    B(n) = \sum_{i=1}^{n-1} \lceil log2(i+1) \rceil <= n log2 n

charged comparisons, with worst case `max_X q = B(n)` (attained). It is a fixed
adaptive strategy whose control decisions depend only on prior `ASK` outcomes.
In a RAM/array-addressed extension of ESP, a parametric control schema keeps
`m, regs = O(1)` (encoded size `O(log n)` once `n_decl` is written) with step
clock `T = O(n^2 log n)`; under `U_ESP`-style uniform cost accounting this gives
`Time = poly(n)`. In the present minimal register-only ISA the adaptive
comparison schedule is an explicit decision structure, so a fully explicit
per-`n` ESP unfolding is a decision program/DAG (polynomial only when that
structure is compressible).

**Checked artifact.** `check_binary_insertion_family` exhaustively simulates the
strategy via charged oracle calls for all `n!` orders, `n <= 8`, verifying
correct sorting, `q <= B(n)`, attainment of `B(n)`, and polynomial step counts.
This is a sound restricted-family upper-envelope witness at budget `B(n)`, not
an exact-`S(n)` completeness witness (e.g. `B(5)=8 > S(5)=7`).

## 6. Exact missing completeness step (identified)

To obtain the strong all-n statement required for `Sigma_2^P` membership of
`SORT-BOUND-U` via strategy programs, one would need:

> **(Completeness / compression compiler, OPEN)** A uniform polynomial-time
> (or at least polynomially-bounded) construction mapping each `(n,k)` with
> `S(n) <= k` (or mapping an implicit optimal strategy witness) to an ESP
> program `p_{n,k}` with `|p_{n,k}| <= poly(n+k)` and `T(p_{n,k},X) <=
> poly(n+k)` for all `X`, such that `U_ESP(p_{n,k},X,n,k)` accepts using `<= k`
> comparisons.

What is **not** sufficient: (i) existence of an optimal decision tree (may be
exponentially large/uncompressed), (ii) a program that enumerates/searches for
such a tree at runtime (violates runtime/clock), (iii) per-instance
non-uniform advice without a polynomially verifiable encoding bound. A proof
would need either a general state-compression/forgetful-DAG simulation theorem
with polynomial blow-up preserving exact budget, or an independent structural
characterization of optimal strategies; a refutation would exhibit an infinite
family forcing super-polynomial `|p|` or super-polynomial `T` in this (or a
precisely delimited) model.

## 7. Relation to S2 / Sigma_2^P accounting

- **[deduction]** Soundness + uniform polynomial verifier: for any fixed class
  `C` of ESP programs with `|p|, T <= poly(n+k)`, the language
  `{1^n#1^k : exists p in C forall X, U_ESP accepts}` is in `Sigma_2^P` (guess
  `p`, universally verify over `X` in polynomial time). This matches the S2
  accounting but via an explicit machine interpreter rather than fixed-variable
  `FO(TC)_v` evaluation.
- **No overclaim:** because completeness of `C` for all `S(n)<=k` is open, this
  does **not** place unrestricted `SORT-BOUND-U` in `Sigma_2^P` (or NP).

## 8. Artifacts and validation

- `scripts/encoded_strategy_program.py`: ESP data model + `U_ESP` interpreter +
  constructors for concrete optimal small-n programs and exhaustive checking of
  the binary-insertion strategy family (restricted witness); self-check/CLI helpers.
- `tests/test_encoded_strategy_program.py`: correctness/budget/soundness checks
  (optimal `n<=4`, insertion sort exhaustive for `n<=8`, charged-oracle and
  runtime-bound accounting, rejection cases).
- Validation: `python3 -m unittest tests.test_encoded_strategy_program -v` and
  (when run in-repo) full `python3 -m unittest discover -s tests`.

## 9. Next concrete experiment

(1) Encode a **merge-sort** family with explicit split/merge control in ESP and
check `q = M(n)` exhaustive for `n<=8` to compare description/runtime overhead
to insertion. (2) Attempt a bounded compiler from a **forgetful framed DAG**
node/transition description (issue #47 / S3) into ESP with measured blow-up on
known small optimal strategies, to probe the compression step identified in §6.
