# Strategy-program fragment spec (S2, pinned scoped draft)

**Status:** scoped draft pinning one reviewed fragment. Docs-only.
Completeness (every `S(n) ≤ k` realized by a poly-size program at exact
budget) is **OPEN**. No unrestricted `SORT-BOUND-U` membership is claimed.

## Pin

- Fragment: **`FO(TC)_v` + `QWIN_{v,d,c}`** as defined in the reviewed note
  `docs/research-fo-tc-combined.md` at
  `27afe9ef6f0b526c4127381b27b57e91e80f92e0`
  (tree `8c36f049bf6554b489a2297cfd4024ccfd93ff26`).
- This supersedes the unpinned sketch `docs/research-fo-tc-strategy-programs.md`
  (main `f89f6d0`) for any soundness/complexity citation until a re-pin.
- Fixed once per language: variable count `v ≥ 2`, action exponent `d`,
  machine-clock exponent `c`, fixed interpreter implementation `U`.
  None of `v,d,c` may be selected per instance, per program, or per `X`.

## Syntax / store / history (summary; authority is the pinned note)

- **[definition]** `FO(TC)_v`: fixed global variable set (`≤ v` names);
  atomic equality + input/store relations; Boolean connectives; FO quantifiers;
  `TC` rule with endpoint width `m`, context width `a`, `a+2m ≤ v`;
  formula text `|φ|` may grow; domain size `N = Θ(n+k+1)`; fixed relational
  vocabulary of arity `≤ v` with explicitly tabulated relations.
- Program `p`: byte string with control label, output buffer, binary history
  relation `H(i,j)`, counter `q`. One rule application returns exactly one
  action: `Ask(i,j)` | `Emit(position,i)` | `Goto(label)` | `Halt`;
  malformed/non-singleton rejects.
- `Ask` requires distinct labels, invokes `QUERY(i,j)`, records only the
  smaller label in `H`, increments `q`, branches on the answer. **No other
  access to the hidden total order `X`.** Repeated queries re-charge.
- `Emit` fills one unwritten output position; `Halt` succeeds at the verifier
  only if a permutation of `[n]` was emitted, `q ≤ k`, and the output is
  sorted in `X` (consistency with queried pairs alone does not suffice).

## Encoding / clocks / verifier form

- Explicit permutation encoding of `X` (`O(n log n)` bits); well-formedness
  validated by the verifier; `L = n+k+|p|+2`.
- Fixed interpreter `U` runs at most `L^c` ordinary deterministic machine
  steps (table evaluation, parsing, store/history updates, query handling,
  output checking); at most `L^d` rule applications; rejects on `> k`
  comparisons. Each `QUERY` is answered from the explicitly given `X`;
  after `Halt` the verifier checks full sortedness in `X`.
- Quantified predicate: `∃p (|p| ≤ b) . ∀X ∈ S_n, Verify(p,X,n,k)`
  with polynomial bound `b(n+k)`. Program sees only charged answers;
  verifier sees `X`.

## Obligations (what may be cited, with model assumptions)

- **[paper proof]** Soundness: acceptance implies `S(n) ≤ k` (under the
  stated explicit-table / unit-cost-indexing model; multitape overhead
  absorbed per the note).
- **[paper proof]** Combined bound: each `φ ∈ FO(TC)_v` evaluates in
  `O(|φ|·N^(2v))` via memoized bottom-up tables + Floyd–Warshall per `TC`
  node; fixed `v,d` select a fixed `c` dominating simulation + checking.
  `FO(TC)=NL` is **not** used (fixed-formula data complexity only).
- **[conditional]** For fixed `v,d,c` and polynomial `b`, `QWIN_{v,d,c}`
  is in `Σ₂^P` **for the representable subclass only**.
- **[conjecture, falsifiable, OPEN]**: every `S(n) ≤ k` has such a `p`
  with `|p| ≤ poly(n+k)` fitting the fixed `L^d`/`L^c` clocks. A program
  that first exhaustively searches for the optimal tree violates the
  runtime condition and does not count.

## Elementary examples (symbolic; not wall-clock)

**[deduction from standard algorithms, per pinned note]** binary-insertion
sort (`Σ ⌈log₂(i+1)⌉` queries, `O(n log n)` actions) and top-down merge sort
(`O(n log n)` queries/actions) fit the fixed schema; the program observes
only `Ask` answers. A fixed small optimal sorter unfolds to one label per
tree node (`Θ(tree nodes)` text) — a semantics sanity check, **not** a
uniform polynomial compiler (explicit-tree `Ω(n!)` leaf barrier applies).
