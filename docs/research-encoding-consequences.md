# Encoding consequences for the complexity of evaluating S(n)

**Status:** research note (literature + deduction + one small experiment). It is
**not** Lean-checked. Every item is labelled `[literature]`, `[deduction]`,
`[experiment]`, `[conjecture]` or `[open]`. No unconditional separation is
claimed, and no NP-hardness is claimed. This note is deliberately *distinct*
from the Executive staging draft
`/home/lubko/soring301-research/docs/research-certificates-barriers.md`
(which the Executive will integrate); it focuses on the exact input encodings,
the elementary deterministic algorithm and its honest runtime, and the
sparse/`P/poly` structure of the unary threshold language.

---

## 0. Model and encodings (fixed once, used throughout)

`[literature]`/definition. From `docs/problem.md`:

- `S(n)` is the minimum height (worst-case number of pairwise comparisons) of a
  **deterministic adaptive comparison decision tree** that correctly sorts
  every permutation of `n` distinct labelled keys. Height is the maximum number
  of comparisons on an execution path; comparison selection may adapt.
- `SORT-BOUND-U = { 1^n # 1^k : S(n) ≤ k }` — both parameters **unary**.
- `SORT-BOUND-B = { bin(n) # bin(k) : S(n) ≤ k }` — both parameters **binary**,
  where `bin(x)` is the standard binary representation (no leading zeros;
  `bin(0) = "0"`).
- Input lengths:
  - unary: `L_U = n + k + 1 = Θ(n + k)`;
  - binary: `L_B = |bin(n)| + 1 + |bin(k)| = Θ(log(n+1) + log(k+1))`.
- Well-formedness (delimiter position, no leading zeros, etc.) is decidable in
  time polynomial in the input length and does not affect any class below.

`[literature]`/`[deduction]` (kernel-checked in this repository):

- Information lower bound: `⌈log₂ n!⌉ ≤ S(n)` (`SoringP1/LowerBound.lean`,
  `Bounds.lean`).
- Elementary upper bound: `S(n) ≤ n(n−1)/2` (`SoringP1/TightBound.lean`,
  `S_le_tight`). Merge sort gives the sharper `S(n) ≤ n⌈log₂ n⌉`.
- Monotonicity: `S(n) ≤ S(n+1)` (`SoringP1/Monotone.lean`, `S_mono`).
- Exact minimax correspondence: `S(n) = adv univ` (`SoringP1/Minimax.lean`),
  where `adv` is the partial-order minimax recurrence.

**Forced regions and informative window.** Let `I(n) = ⌈log₂ n!⌉` and
`U(n) = n⌈log₂ n⌉`. Then `S(n) ∈ [I(n), U(n)]` and `U(n) − I(n) = Θ(n)` (because
`log₂ n! = n log₂ n − Θ(n)`). The input `k` is arbitrary. For `k < I(n)` the
answer to `S(n) ≤ k` is **no**, and for `k ≥ U(n)` it is **yes** (since
`S(n) ≤ U(n) ≤ k`); these are *forced* answers. The only uncertain `k` lie in
the window `[I(n), U(n))`, of width `Θ(n)`. The forced-yes region
`[U(n), ∞)` is used in the binary non-sparsity argument (§4).

---

## 1. The elementary deterministic algorithm and the `2^{O(n²)}` bound

### 1.1 States, representation, recurrence

`[deduction]`. A **state** is a transitive, antisymmetric relation `P` on
`[n] = {0,…,n−1}`; equivalently, for every unordered pair `{x,y}` exactly one
of `x<y`, `y<x`, "unknown" holds and the relation is transitively closed.
Represent `P` by the `n×n` boolean matrix `M` with `M[x][y] = 1` iff `x<y`.
Then:

- `M` is **total** iff for every `x ≠ y`, exactly one of `M[x][y]`, `M[y][x]`
  is `1`.
- `{x,y}` is **incomparable** iff `M[x][y] = M[y][x] = 0`.
- The **successor** of `M` under the comparison `{x,y}` answered `x<y` is the
  transitive closure of `M ∪ {(x,y)}`; similarly for `y<x`.

Define the minimax value `F(M)` by

```
F(M) = 0                                   if M is total,
F(M) = 1 + min_{(x,y) incomparable}
         max( F(succ(M, x<y)), F(succ(M, y<x)) )   otherwise.
```

### 1.2 Correctness

`[deduction]` **Lemma 1.1.** For every state `M`, `F(M)` equals the minimum,
over comparison trees `T` that correctly sort every permutation consistent with
`M`, of the worst-case number of comparisons of `T` on those inputs.

*Proof sketch.* Strong induction on `c(M) =` number of incomparable pairs.
If `c(M) = 0` then `M` is total and zero comparisons suffice, so `F(M) = 0`.
Otherwise the first comparison must be an incomparable pair (a comparison of
comparable elements is redundant); the adversary chooses the worse of the two
outcomes, and the sorter chooses the pair minimising the resulting worst case.
Thus `F(M) = 1 + min_{pairs} max(outcomes)`, which is exactly the game value.
The empty poset has `c = n(n−1)/2` and `F(∅) = S(n)` by the standard
correspondence between transcripts and consistent posets. ∎

### 1.3 Termination

`[deduction]` **Lemma 1.2.** Each branch of the recurrence strictly increases
the number of comparable pairs, so `c(M)` strictly decreases. Hence the recursion
is well-founded and terminates.

This is a *termination* statement only. It says nothing about runtime; see §7.

### 1.4 State enumeration

`[deduction]` **Lemma 1.3.** The states reachable from the empty poset are
exactly the labelled partial orders on `n` elements.

*Proof.* (⊆) Every reachable state is a transitively closed partial order.
(⊇) Let `Q` be a partial order on `[n]` and let `x_1,…,x_n` be a linear
extension of `Q` (so `x_i <_Q x_j ⇒ i < j`). Add the comparabilities of `Q` in
lexicographic order of `(i,j)` for pairs `i<j` with `x_i <_Q x_j`. When
`x_i < x_j` is added, no already-added relation can force it (any forcing chain
would need a relation with first index strictly between `i` and `j`, which is
added later, or a relation `x_a < x_i` with `a<i`, which does not combine with
the not-yet-added `x_i < x_j`), and `x_j < x_i` is false in `Q`. So the pair is
incomparable when added, and the final state is exactly `Q`. ∎

`[literature]` **Lemma 1.4 (Kleitman–Rothschild).** The number `P_n` of labelled
partial orders on `n` elements satisfies
`log₂ P_n = n²/4 + 3n/2 + O(log n)`, hence `P_n = 2^{Θ(n²)}`. A crude but
sufficient bound is `P_n ≤ 3^{n(n−1)/2} = 2^{O(n²)}`.

### 1.5 Representation and runtime

`[deduction]` **Lemma 1.5.** A state is an `n×n` boolean matrix, i.e. `O(n²)`
bits, comparable and hashable in `O(n²)` time. All values `F(M) ≤ n(n−1)/2`
have `O(log n)` bits, so arithmetic on them is polynomial.

`[deduction]` **Theorem 1.6 (elementary deterministic bound).** The memoized
dynamic program that computes `F(∅) = S(n)` by enumerating reachable states runs
in deterministic time

```
P_n · poly(n) = 2^{n²/4 + O(n)} = 2^{O(n²)}
```

measured in the numeric parameter `n`.

*Proof.* By Lemma 1.3 there are `P_n` states; by Lemma 1.4, `P_n =
2^{Θ(n²)}`. For each state, scan the `O(n²)` incomparable pairs, form the two
transitive closures (naively `O(n³)`, or `O(n²)` with bitset operations), and
combine already-memoized values with `O(log n)`-bit arithmetic. The per-state
work is `poly(n) = 2^{O(log n)}`, which is absorbed by `2^{O(n²)}`; **no
additional logarithmic factor is needed**. ∎

`[deduction]` **Remark 1.7 (this algorithm is `2^{Θ(n²)}`, not merely
`2^{O(n²)}`).** Because *every* labelled poset is reachable (Lemma 1.3), any
implementation that memoizes over states must visit all `P_n` of them. So this
particular dynamic program has runtime `Θ(P_n · poly(n)) = 2^{Θ(n²)}`. This is a
lower bound on *this* algorithm, **not** a lower bound on the complexity of
computing `S(n)`; a smarter algorithm need not enumerate all posets.

---

## 2. Encoding consequences: unary versus binary

`[deduction]` **Theorem 2.1 (unary).** `SORT-BOUND-U ∈ EXPTIME`.

*Proof.* For an input `1^n#1^k` we have `L_U = n+k+1`, so `n ≤ L_U`. The
algorithm of Theorem 1.6 runs in time `2^{O(n²)} ≤ 2^{O(L_U²)}`, which is
exponential in `L_U`. A deterministic Turing machine implementing the memoized
recurrence therefore decides `SORT-BOUND-U` in exponential time. ∎

`[deduction]` **Theorem 2.2 (binary).** `SORT-BOUND-B ∈ 2-EXPTIME`.

*Proof.* For `bin(n)#bin(k)`, `L_B = |bin(n)| + 1 + |bin(k)| =
Θ(log(n+1) + log(k+1))`. The input `k` is arbitrary (it need not be `≤ n²`).
In particular `|bin(n)| ≤ L_B`, so `n ≤ 2^{L_B}` and `n² ≤ 2^{2 L_B}`.
Substituting into Theorem 1.6,

```
2^{O(n²)} ≤ 2^{O(2^{2 L_B})} = 2^{2^{O(L_B)}},
```

which is the definition of `2-EXPTIME`. ∎

`[deduction]` **Remark 2.3 (the gap is encoding, not algorithm).** The same
numeric-`n` bound `2^{O(n²)}` becomes `EXPTIME` under the unary encoding and
`2-EXPTIME` under the binary encoding. The binary encoding compresses `n`
exponentially (`n ≤ 2^{L_B}`), so the same computation is doubly exponential in
the input length. This is why `SORT-BOUND-U ∈ EXPTIME` does **not** imply
`SORT-BOUND-B ∈ EXPTIME`.

`[deduction]` **Remark 2.4 (relation to the game/ATM bounds).** The Executive
draft derives the stronger bounds `SORT-BOUND-U ∈ PSPACE` and
`SORT-BOUND-B ∈ EXPSPACE` by a different algorithm (an alternating Turing
machine playing the comparison game, using `APTIME = PSPACE` and
`AEXPTIME = EXPSPACE`). That is a stronger *algorithmic* result. The present
`2^{O(n²)}` DP bound is weaker (`EXPSPACE ⊆ 2-EXPTIME`) but elementary and
self-contained; both are correct and neither contradicts the other.

`[deduction]` **Remark 2.5 (function versus decision).** Given an evaluator for
`S(n)`, the threshold decision `S(n) ≤ k` is a single comparison. Conversely,
given a decider for `SORT-BOUND`, the value `S(n)` is obtained by binary search
over `k` in the window `[I(n), U(n)]` (width `Θ(n)`), using `O(log n)` calls.
Hence `SORT-BOUND-U ∈ P` iff `S_unary ∈ FP`, and `SORT-BOUND-B ∈ P` iff
`S_binary ∈ FP`. The classes are defined on the respective input lengths.

---

## 3. Sparsity and `P/poly` for the unary threshold language

### 3.1 The unary language is sparse

`[deduction]` **Lemma 3.1.** `SORT-BOUND-U` is sparse: the number of its strings
of length at most `L` is at most `(L+1)(L+2)/2 = O(L²)`.

*Proof.* A string of `SORT-BOUND-U` has the form `1^n#1^k` with `n+k+1 ≤ L`.
There is at most one such string for each pair `(n,k)`, and the number of pairs
with `n+k+1 ≤ L` is `∑_{s=0}^{L-1} (s+1) = L(L+1)/2 ≤ (L+1)(L+2)/2`. ∎

### 3.2 Sparse languages are in `P/poly`

`[deduction]` **Lemma 3.2.** Every sparse language is in `P/poly`.

*Proof.* Let `L` be sparse with `|L ∩ Σ^{≤m}| ≤ p(m)` for a polynomial `p`. For
each length `ℓ`, let the advice `a_ℓ` be the list of all strings of length `ℓ`
in `L` (there are at most `p(ℓ)` of them, so `|a_ℓ| ≤ p(ℓ)·ℓ`). A deterministic
machine with advice `a_{|x|}` accepts `x` iff `x` appears in the list; this takes
polynomial time. The advice need not be computable. ∎

### 3.3 Concrete `O(L log L)` advice for `SORT-BOUND-U`

`[deduction]` **Theorem 3.3.** `SORT-BOUND-U ∈ P/poly` with advice length
`O(L log L)`.

*Proof.* For each length `L`, define the advice `a_L` to be the concatenation of
the binary representations of `S(0), S(1), …, S(L)`, each padded to the fixed
width `w_L = ⌈log₂(L²+1)⌉` bits. (This width suffices because
`S(i) ≤ i(i−1)/2 ≤ L²` for `i ≤ L`, by the kernel-checked bound `S_le_tight`.)
Then `|a_L| = (L+1)·w_L = O(L log L)`.

On input `x = 1^n#1^k` with `n+k+1 = L`, the machine scans `x` to obtain `n` and
`k` (time `O(L)`), reads the `(n+1)`-st block of `a_L` (time `O(w_L)`), and
accepts iff that block, interpreted as an integer, is `≤ k`. The total time is
`O(L log L) = poly(L)`. The advice depends only on `L`, as `P/poly` requires. ∎

`[deduction]` **Remark 3.4 (single threshold per `n`; monotonicity in `k`).**
For a fixed `n`, the set `{ k : S(n) ≤ k }` is the upward-closed interval
`[S(n), ∞)`. Hence **one** number `S(n)` determines the answer for *all* `k`;
we store one value per `n`, not one per pair `(n,k)`. This is the sense in
which "variable `k` and monotonicity" collapse the table to a single threshold
per `n`.

`[deduction]` **Remark 3.5 (monotonicity in `n` does not provably shrink the
advice).** The kernel-checked `S_mono` gives an alternative encoding by
increments `S(n)−S(n−1)`. The upper bound on an increment is `U(n) − I(n−1) =
Θ(n)` (the gap between the merge-sort upper bound and the information lower
bound), so an increment may need `Θ(log n)` bits and the worst case remains
`Θ(L log L)`. Monotonicity is useful structurally but does not by itself yield
`o(L log L)` advice.

`[deduction]` **Remark 3.6 (`P/poly` is nonuniform and weak).** Theorem 3.3 is a
*nonuniform* upper bound: the advice `a_L` need not be computable, and `P/poly`
membership does not imply membership in `P`, in `NP`, or in any uniform class.
In fact the general fact `sparse ⊆ P/poly` (Lemma 3.2) is the *same* structural
property that triggers the Mahaney barrier (§4). So `SORT-BOUND-U ∈ P/poly` and
"many-one NP-hardness of `SORT-BOUND-U` would imply `P = NP`" are two faces of
one fact, not a contradiction. Theorem 3.7 below gives an even sharper
nonuniform bound.

---

### 3.4 A sharper nonuniform bound: `P/log` via the length cutoff

`[deduction]` **Theorem 3.7 (`SORT-BOUND-U ∈ P/log`).** `SORT-BOUND-U ∈ P/O(log L)`, i.e. `P/log`, with advice length `O(log L)`.

*Proof.* Write the total input length as `L = n+k+1`, so `k = L−1−n`.
Membership is `S(n) ≤ k = L−1−n`, equivalently

```
f(n) := n + S(n) ≤ L − 1.
```

By the kernel-checked `S_mono`, `S(n) ≤ S(n+1)`, so
`f(n+1) − f(n) = 1 + S(n+1) − S(n) ≥ 1 > 0`. Hence `f` is **strictly
increasing**. Therefore, for each `L`, the set `{ n ∈ [0, L−1] : f(n) ≤ L−1 }`
is an initial interval `[0, t_L]`, where
`t_L := max{ n ≤ L−1 : f(n) ≤ L−1 }` (and `t_L ≥ 0` because `n = 0` always
satisfies `f(0) = S(0) = 0 ≤ L−1` for `L ≥ 1`).

Define the advice `a_L` to be the binary encoding of `t_L` in `⌈log₂ L⌉` bits
(`t_L ∈ [0, L−1]`, so this fits). On input `x` of length `L`, the machine first
checks well-formedness — exactly one `#`, only `1`s on both sides, and
`n+k+1 = L` — then parses `n`, reads `t_L`, and accepts iff `n ≤ t_L`. This
runs in `O(L)` time. Hence `SORT-BOUND-U ∈ P/O(log L) = P/log`. ∎

*Edge cases.* `S(0) = 0` (kernel-checked `S_zero`), so `f(0) = 0`. For `L = 1`
the only well-formed string is `#` (`n = k = 0`), and `t_1 = 0`; the verifier
accepts iff `n = 0 ≤ 0`. For `L = 0` the empty string is not well-formed and is
rejected. For every `L ≥ 1`, `n = 0` is always accepted (the string `#1^{L−1}`).

`[deduction]` **Remark 3.8 (nonuniform; strictly sharper than Theorem 3.3).** The
advice `t_L` is a single number per length and need not be efficiently
computable; Theorem 3.7 is a nonuniform bound and does **not** imply
`SORT-BOUND-U ∈ P` or any uniform membership. It is strictly sharper than
Theorem 3.3: monotonicity of `f(n) = n + S(n)` collapses the advice from `L+1`
stored values (`O(L log L)` bits) to one cutoff (`O(log L)` bits).

`[deduction]` **Remark 3.9 (fixed total length is essential).** The argument
uses the canonical fixed-total-length encoding `L = n+k+1`, in which `k` is
determined by `L` and `n`, so the advice depends only on `L`. In a
separate-input representation whose two lengths are not tied to a single total
`L`, the advice would have to depend on the pair of lengths and the single
cutoff compression would not directly apply. The well-formedness check (one
delimiter, unary blocks) is part of the `O(L)` verification.


### 3.5 A nonuniform depth-two circuit upper bound

`[deduction]` **Theorem 3.10 (`SORT-BOUND-U ∈ nonuniform AC⁰`).**
For each fixed total input length `L`, membership in `SORT-BOUND-U`
has a depth-two, polynomial-size Boolean circuit family (`O(L²)`
literal occurrences). More precisely, let `t_L` be the cutoff from
Theorem 3.7, and index the input symbols from `0` through `L−1`.
For `L ≥ 1`, the circuit is

```
C_L(x) = OR_{0 ≤ i ≤ t_L} (
              [x_i = #] AND
              AND_{0 ≤ j < i} [x_j = 1] AND
              AND_{i < j < L} [x_j = 1]
         ).
```

Each term checks that the input consists of precisely `i` unary
`1`s, one delimiter `#`, and then `L−i−1` unary `1`s. The circuit
accepts exactly when the delimiter occurs at an index `i ≤ t_L`,
equivalent to `S(i) ≤ L−1−i` by Theorem 3.7.
There are at most `L` terms, each with at most `L` literals.
For `L = 0`, use a rejecting constant circuit. Encoding each
alphabet symbol with a fixed number of Boolean bits changes only
a constant number of gates per equality test. Consequently this is
a nonuniform `AC⁰` family: depth `O(1)` and size `poly(L)`. ∎

`[deduction]` **Corollary 3.11 (a restricted unconditional
hardness barrier).** `PARITY` cannot many-one reduce to
`SORT-BOUND-U` by a polynomial-output-length `AC⁰` circuit
reduction (in the standard fixed-output-length circuit model).

*Proof.* Compose a putative `AC⁰` reduction circuit with the
`AC⁰` decider of Theorem 3.10 at its output length. Depth remains
constant and size remains polynomial, giving a nonuniform
`AC⁰` circuit family for `PARITY`. This contradicts the
classical `PARITY ∉ nonuniform AC⁰` lower bound
(Håstad, STOC 1986, https://doi.org/10.1145/12130.12132). ∎

**Novelty calibration:** the class membership `SORT-BOUND-U ∈
nonuniform AC⁰` is *not* a special sorting discovery. **Every sparse
language** is in nonuniform `AC⁰`: on length-`L` inputs, OR the
exact-match conjunctions for its `poly(L)` YES-strings.
The extra sorting structure here is the explicit single-cutoff
formula and its `O(L²)` size, not the `AC⁰` membership itself.
Consequently Corollary 3.11 is likewise a generic sparse-language
barrier and should not be counted as progress toward a uniform
complexity classification.

This does **not** forbid polynomial-time reductions, prove
`SORT-BOUND-U ∈ P`, or yield a uniform construction of the
circuits: their choice of cutoff `t_L` may itself be
computationally difficult. `AC⁰` circuit membership and
`P/O(log L)` advice membership are two separate nonuniform
descriptions of this particularly structured language, not
a claim of a general containment between those two classes.

---

## 4. Reduction barriers: many-one, truth-table, Turing, and the binary version

### 4.1 The sparse-set theorems

`[literature]` **Theorem 4.1 (Mahaney).** If a sparse set is NP-hard under
polynomial-time many-one reductions, then `P = NP`.

`[literature]` **Theorem 4.2 (Fortune).** If a sparse set is coNP-hard under
polynomial-time many-one reductions, then `P = NP`.

`[literature]` **Theorem 4.3 (Ogiwara–Watanabe).** If `SAT` is polynomial-time
bounded truth-table reducible to a sparse set (a nonadaptive reduction making
`O(1)` queries), then `P = NP`.

`[literature]` **Theorem 4.4 (Karp–Lipton; Turing reductions).** If `SAT` is
polynomial-time Turing reducible to a sparse set, then `PH = Σ₂P`. (Equivalently:
if `SAT` has polynomial-size circuits then `PH = Σ₂P`; and
`A ≤_T^p S` for sparse `S` iff `A ∈ P/poly`.) Kadin refines this to
`PH ⊆ P^NP[log]` when the sparse set is itself in `NP`.

### 4.2 Application to the unary language

`[deduction]` **Theorem 4.5.** `SORT-BOUND-U` is sparse (Lemma 3.1). Therefore:

1. it is **not** NP-hard under polynomial-time many-one reductions unless
   `P = NP` (Theorem 4.1);
2. it is **not** NP-hard under polynomial-time bounded truth-table reductions
   unless `P = NP` (Theorem 4.3);
3. it is **not** NP-hard under polynomial-time Turing reductions unless
   `PH = Σ₂P` (Theorem 4.4);
4. it is **not** coNP-hard under polynomial-time many-one reductions unless
   `P = NP` (Theorem 4.2).

These are *conditional barriers*, not membership statements. They do not say
that `SORT-BOUND-U` is in `P`, in `NP`, or in `coNP`.

### 4.3 The binary language is not sparse

`[deduction]` **Theorem 4.6.** `SORT-BOUND-B` is **not** sparse.

*Proof.* Fix `m` large and let `1 ≤ n ≤ 2^{m/3}`. Then `|bin(n)| ≤ m/3 + 1`, so
the largest `k` for which `bin(n)#bin(k)` has length at most `m` satisfies
`|bin(k)| ≤ K_n := m − 1 − |bin(n)| ≥ 2m/3 − 2`. Every `k ≥ U(n)` is
*guaranteed* to be in `SORT-BOUND-B`, because `S(n) ≤ U(n) ≤ k`. The number of
such `k` with `|bin(k)| ≤ K_n` is at least `2^{K_n} − U(n)`. Since
`U(n) ≤ n⌈log₂ n⌉ ≤ 2^{m/3}·(m/3+1) ≤ 2^{m/3 + log₂ m + 1}` and
`2^{K_n} ≥ 2^{2m/3 − 2}`, for large `m` this count is at least `2^{2m/3 − 3}`.
Summing over `n ≤ 2^{m/3}`, the number of strings of `SORT-BOUND-B` of length at
most `m` is at least `2^{m/3}·2^{2m/3 − 3} = 2^{m−3}`, which is exponential in
`m` and therefore not polynomial. ∎

`[deduction]` **Corollary 4.7.** The Mahaney/Fortune/Ogiwara–Watanabe barriers
do **not** apply to `SORT-BOUND-B`. This is the sharpest formal difference
between the two encodings. It is *not* evidence that `SORT-BOUND-B` is hard: it
merely removes the sparse-set obstruction. No hardness for `SORT-BOUND-B` is
claimed.

### 4.4 What is not claimed

`[deduction]` The following are **not** established by this note and are **not**
claimed:

- `SORT-BOUND-U` or `SORT-BOUND-B` is NP-hard, coNP-hard, PSPACE-hard, or hard
  for any named class;
- `SORT-BOUND-U` or `SORT-BOUND-B` is in `NP` or `coNP`;
- any separation such as `P ≠ NP`, `NP ≠ PSPACE`, or `EXPTIME ≠ 2-EXPTIME`;
- that the `2^{O(n²)}` DP is optimal for computing `S(n)`.

The barriers in §4.2 are conditional; the non-sparsity in §4.3 is a removal of a
barrier, not a hardness proof.

---

## 5. Certificates and why the naive tree witness is not an `NP` proof

### 5.1 Size of an explicit tree

`[deduction]` **Lemma 5.1.** Every correct comparison tree sorting `n` keys has
at least `n!` *reachable* leaves (the `n!` permutations reach pairwise distinct
leaves). There **exists** an optimal (height `S(n)`) tree with exactly `n!`
reachable leaves and `2n! − 1` nodes; an arbitrary optimal-height tree may
contain additional unreachable leaves without increasing the maximum height.

*Proof.* A leaf is reached by the permutations consistent with its comparison
transcript. Correctness forces each leaf to be reached by at most one
permutation (two distinct permutations reaching the same leaf could not both be
sorted correctly by that leaf). Every permutation must reach some leaf, so the
`n!` permutations occupy `n!` pairwise distinct leaves; hence at least `n!`
reachable leaves. To obtain a reduced optimal tree, take any optimal tree and
prune its unreachable branches; pruning cannot increase the maximum height, so
the result is still optimal and now has exactly the `n!` reachable leaves and no
unreachable leaves. A full binary tree with `n!` leaves has `2n! − 1` nodes. ∎

`[experiment]` The repository's `scripts/evaluate.py`/`generate_optimal_tree.py`
and the Executive draft confirm `nodes = 2n! − 1` and `leaves = n!` for the
optimal trees they construct, `n ≤ 6`.

### 5.2 The tree witness is not polynomial

`[deduction]` **Theorem 5.2.** An explicit correct sorting tree is **not** a
polynomial-size certificate for `S(n) ≤ k`.

*Proof.* By Lemma 5.1 any correct tree has at least `n!` leaves, hence at least
`n!` nodes (and a reduced optimal one has `2n! − 1` nodes).
- **Unary:** for informative instances `k = S(n) = Θ(n log n)`, so
  `L_U = n + k + 1 = Θ(n log n)`, and `n! = 2^{Θ(n log n)} = 2^{Θ(L_U)}`, which
  is super-polynomial in `L_U`.
- **Binary:** `n = 2^{Θ(L_B)}`, so `n! = 2^{Θ(2^{L_B}·L_B)}`, doubly
  exponential in `L_B`.

Verifying an explicit tree is polynomial *in the size of the tree*: check the
height bound, then for each root-to-leaf path compute the transitive closure of
its comparisons; an inconsistent path has an unreachable leaf (ignored), while a
total path has exactly one linear extension and the leaf output must match it.
`O(n²)` per path. Since the tree itself is exponential (unary) or doubly
exponential (binary) in the input length, the natural nondeterministic verifier
runs in `NEXP` (unary) / `N2EXP` (binary), **not** `NP`. ∎

`[deduction]` **Remark 5.3.** The upper bounds of §2 (`EXPTIME` unary,
`2-EXPTIME` binary) and the stronger `PSPACE`/`EXPSPACE` game bounds dominate
these nondeterministic bounds, so the tree witness yields no new membership.
Note that the unary witness size is `2^{Θ(L_U)}`, not `2^{Θ(L_U log L_U)}`: for
informative instances `L_U = Θ(n log n)` and `log₂(n!) = Θ(n log n)`. The
super-polynomial conclusion is unchanged.

### 5.3 Candidate short certificates

| Candidate witness for `S(n) ≤ k` | Checkability | Size | Status |
|---|---|---|---|
| explicit adaptive tree | poly in tree size | `≥ n!` leaves (optimal: `2n! − 1` nodes) | super-polynomial; not `NP` (Thm 5.2) |
| memoized DP table over posets | poly in table size | `P_n = 2^{Θ(n²)}` | super-polynomial (Thm 1.6) |
| branching program / DAG strategy | poly in DAG size | no poly upper bound known | `[open]`; whether optimal play confines a DAG to poly many states is open |
| program computing the strategy | not known poly (universal over `n!` inputs) | poly possible | `[open]` |
| potential / invariant | not known | ? | `[open]`; `log₂ e(P)` is not tight |
| nonuniform advice `S(0..L)` | poly with advice | `O(L log L)` | `P/poly`, not uniform (Thm 3.3) |

`[deduction]` **Theorem 5.4 (no known succinct certificate).** Neither
`S(n) ≤ k` nor `S(n) > k` is known to have a certificate polynomial in the
input length. The only known potential is `log₂ e(P)` (the base-2 logarithm of
the number of linear extensions of `P`), which is `#P`-complete to evaluate
exactly (Brightwell–Winkler) and is **not tight** (`S(12) = 30 > 29 =
⌈log₂ 12!⌉`). Hence `NP` and `coNP` membership of `SORT-BOUND-U` and
`SORT-BOUND-B` remain open.

---

## 6. Counterexamples and falsification attempts


`[deduction]` **Counterexample 6.1 (sparse `P/poly` need not be
uniformly polynomial-time decidable).** A unary language may be
decidable but not in `P`, despite requiring only one bit of
nonuniform advice per input length.

Here is an explicit diagonal construction. Fix a standard
polynomial-time-decodable numbering `N_j` of deterministic
Turing machines, with invalid program codes interpreted as
a fixed rejecting machine. For each `i≥0`, uniquely write
`i+1=2^r(2j+1)` and set `M_i=N_j`.
This enumeration is computable in `poly(log(i+2))` time,
every machine has arbitrarily large indices (vary `r`),
and its description at index `i` has `O(log(i+2))` bits.
For `n ≥ 1` let
`i = v₂(n)` be the exponent of the largest power of two dividing
`n`. On input `1^n`, simulate `M_i` on `1^n` for at most
`n^(i+2)` steps and **accept iff `M_i` does not accept within
that many steps**. Call this tally language `TALLY-DIAG`.
Because `i ≤ log₂ n`, its decider runs in
`2^{O((log n)²)}` time (allowing polynomial simulation overhead).
It is therefore decidable and sparse.

If a deterministic polynomial-time machine `M` decided
`TALLY-DIAG` in time `O(n^d)`, take any sufficiently large
index `i ≥ d` at which `M_i = M`. There are arbitrarily large
numbers `n = 2^i(2t+1)` with `v₂(n) = i`. On all sufficiently
large such inputs `M_i` halts within the allowed cutoff;
the diagonal decider gives the opposite answer, a contradiction.
Thus `TALLY-DIAG ∉ P` unconditionally, yet
`TALLY-DIAG ∈ P/1 ⊆ P/poly`: advice for length `n` is the
single membership bit. This exhibits the required distinction
without assuming an unproved class separation. ∎

**Correction to an earlier erroneous unary-SAT example.**
Mapping a binary SAT instance `φ` to a unary string
`1^{⟨φ⟩}` is **not** a polynomial-time many-one reduction
for a standard length-respecting numeric encoding `⟨φ⟩`:
the output generally has exponential length in `|φ|`.
Indeed, under a conventional binary Gödel coding, the unary
language `{1^{⟨φ⟩} : φ is satisfiable}` is itself in `P`:
decode the index and brute-force assignments to a formula of
length `O(log n)` in time polynomial in the unary input
length `n`. The previous claim that it was a sparse,
polynomial-time many-one NP-hard language was false; it
would have contradicted Mahaney's theorem unless `P=NP`.

`[deduction]` **Counterexample 6.2 (the binary language is not sparse).**
Theorem 4.6; the Mahaney barrier does not transfer to `SORT-BOUND-B`.

`[deduction]` **Counterexample 6.3 (the tree witness is not `NP`).** Theorem 5.2.

`[deduction]` **Falsification attempt 6.4 (does the DP need a log overhead?).**
Suppose one claims the DP runtime is `2^{O(n²)}·log n` because of state
representation. Refuted: each state is `O(n²)` bits, there are
`P_n = 2^{n²/4 + O(n)}` states, and the per-state work is `poly(n) =
2^{O(log n)}`; the product is `2^{n²/4 + O(n)}`, with no extra log factor.
Moreover, since every poset is reachable (Lemma 1.3), the DP's runtime is
`Θ(2^{Θ(n²)})` (Remark 1.7).

`[deduction]` **Falsification attempt 6.5 (does monotonicity collapse the
advice?).** Suppose one claims `S_mono` lets us store only `O(L)` advice.
Refuted: the upper bound on an increment is `Θ(n)`, so an increment may need
`Θ(log n)` bits and the worst case is `Θ(L log L)` (Remark 3.5).




`[deduction]` **Theorem 6.6 (even a one-comparison gap AND
the exact insertion recurrence cannot imply uniform `P`).**
There is a computable nondecreasing integer function `G(n)`,
with `G(0)=G(1)=0`, such that, writing
`I(n)=ceil(log₂(n!))`, for every `n≥2`:

1. **One-bit numerical slack:** `I(n) ≤ G(n) ≤ I(n)+1`;
   in particular `G(n)=log₂(n!)+O(1)`, and
   `G(n)≤n ceil(log₂n)`.
2. **The genuine insertion inequality:**
   `0≤G(n)−G(n−1)≤ceil(log₂ n)`,
   the same elementary recurrence satisfied by
   comparison sorting (sort `n−1` keys, then insert the last
   key by binary search). It also satisfies the familiar
   **merging recurrence**
   `G(a+c) ≤ G(a)+G(c)+(a+c−1)` for all `a,c≥1`
   (sort two blocks and merge them).
3. Yet the canonical unary threshold language
   `U_G={1^n#1^k:G(n)≤k}` is **not in uniform `P`**,
   despite having the same nonuniform depth-two `AC⁰`
   circuits as `SORT-BOUND-U`.

*Proof.* Take the explicit decidable but non-P tally language
`H=TALLY-DIAG` from Counterexample 6.1. We first construct
an efficiently enumerable set of places where the arithmetic
information bound leaves one comparison of insertion slack.
For `n≥2` let

```
d_n = ceil(log₂ n) - [I(n)-I(n-1)] ∈ {0,1},
T = { n≥2 : d_n=1 }.
```

The inclusion follows because
`I(n)−I(n−1)` is either `floor(log₂ n)` or
`ceil(log₂ n)`. Importantly, `T` has
**positive lower density**, not just infinitely many
elements. Indeed, telescoping gives

```
sum_{j=2}^N d_j
  = sum_{j=2}^N (ceil(log₂ j)-log₂ j)
    + log₂(N!) - I(N).
```

The last term is in `(-1,0]`. On the first half of
every sufficiently large dyadic block
`(2^a, 3·2^(a−1)]`, each summand
`ceil(log₂ j)-log₂ j` is at least
`1-log₂(3/2)>0`. Taking a completed such block
below `N` proves `sum d_j=Ω(N)`.
We exclude the first eight indices and use the
**explicit constant `N₀=8`**. For every `N=a+c≥9`
with `a,c≥1`, we have
`I(N) ≤ I(a)+I(c)+N−2`: the maximum binomial
coefficient of row 9 is `binom(9,4)=126≤2^7`;
moreover `max_a binom(N,a)/2^N` is nonincreasing
in `N` by Pascal's identity, so
`binom(N,a)≤2^(N−2)` for all `N≥9`.
Finally `N!=a!c!binom(N,a)` and
`ceil(x+y)≤ceil(x)+ceil(y)` give the claim.
Thus no asymptotic central-binomial estimate or
uncomputed threshold constant is needed.
Now let `t_m` denote the `m`-th element
of `T∩(N₀,∞)`. Removing finitely many indices
preserves positive lower density, so `t_m=O(m)`.
We can find `t_m` in polynomial time given
unary `m` by scanning integer arguments and computing
the factorial bit length `I(j)`.

Now define `b_n` as follows: if `n=t_m`, set
`b_n=1` iff `1^m∈H`; otherwise set
`b_n=0`. Put

```
G(n) = I(n) + b_n.
```

Since `b_n∈{0,1}`, the one-comparison gap follows.
As `I(n)−I(n−1)≥1` for `n≥2` and
`b_n−b_(n−1)≥−1`, `G` is nondecreasing.
To check the insertion recurrence, if `n∈T`
then `I(n)−I(n−1)=ceil(log₂ n)−1`,
so adding `b_n−b_(n−1)≤1` respects the
upper bound. If `n∉T` then `b_n=0`,
so `G(n)−G(n−1)≤I(n)−I(n−1)≤ceil(log₂ n)`.
For `n≥2`, `I(n)+1≤n ceil(log₂n)`
follows from `n!≤n^(n−1)`.
For the merging recurrence, write `N=a+c`
with `a,c≥1`. The baseline `I` satisfies
`I(N)≤I(a)+I(c)+N−1`, because
`binom(N,a)≤2^(N−1)` (Pascal's identity
exhibits its two summands among the
`2^(N−1)` subsets of an `(N−1)`-set).
If `N≤N₀`, then `b_N=0`, and
`G(N)≤I(a)+I(c)+N−1≤G(a)+G(c)+N−1`.
If `N>N₀`, the chosen stronger
one-comparison baseline slack absorbs the possible
`b_N≤1`, again giving the claimed inequality.
Computability follows by enumerating `T∩[2,n]`
with indices above `N₀`, then evaluating one
quasipolynomial-time membership bit of `H`
at its rank.

Suppose `U_G∈P`. On input `1^m` to
`H`, compute `n=t_m=O(m)` and `I(n)`
in polynomial time, then query the `P` decider
on `1^n#1^{I(n)}`. This query is of length
`O(n log n)=poly(m)` and is accepted
**iff `b_n=0`**. Negating its answer decides
`H` in polynomial time, contradiction.
Thus `U_G∉P`. The cutoff proof of Theorem 3.10
applies because `n+G(n)` is strictly increasing;
so `U_G` is nevertheless in nonuniform depth-two
`AC⁰`. ∎

**Meaning for the actual sorting function.**
`G` is an **artificial** function; this theorem
is not a complexity lower bound for `S(n)`.
It proves that the information bound, **a constant
additive upper gap**, monotonicity, the **exact
standard insertion and merging upper recurrences**,
and tiny nonuniform circuits **together cannot establish
uniform polynomial-time evaluation**. What matters
is additional *sorting-specific* structure beyond
these numerical inequalities, plausibly a complete,
efficiently verifiable representation of optimal
comparison play. The one-comparison gap is optimal for this type of counterexample:
forcing `G(n)=I(n)` identically would give an ordinary polynomial-time
computable function and hence a uniform P threshold language.
This auxiliary diagonal example does not warrant Lean formalization.

---

## 7. Lean termination is not Turing runtime

`[deduction]` The Lean evaluator `adv` (`SoringP1/Minimax.lean:83`) is defined by
well-founded recursion on `S.card` (`termination_by S.card`,
`decreasing_by … filter_card_lt`). Lean's kernel checks that this recursion
terminates. That is a **logical totality guarantee**, not a resource bound.

The `2^{O(n²)}` bound of Theorem 1.6 is an *external* analysis of a Turing
machine implementing the memoized recurrence over partial orders. It is not
derived from Lean and is not a Lean theorem. In particular:

- Lean's definitional reduction (lazy weak-head normal form) is not a Turing
  machine; the kernel's evaluation strategy can be arbitrarily slower or faster
  than a concrete implementation.
- A Lean proof that a function terminates says nothing about how many steps a
  Turing machine needs to evaluate it.
- The `WellFounded.fix` unfolding/whnf loop recorded in `kernel-results.md` is a
  proof-engineering obstacle in the *height specification*, unrelated to
  runtime.

Therefore one must not read "Lean computes `S(n)` in `X` steps" from a Lean
definition, and must not treat a Lean termination proof as a complexity upper
bound. The two notions are independent.

---

## 8. Experiment (corroboration)

`[experiment]` A small script (kept out of the repository; reproduced in the
session log) confirms the counting claims:

```
 L   unary strings ≤ L   advice bits ≤   O(L log L)
  4         10                 30            12
  8         36                 72            32
 12         78                117            48
 20        210                210           100
 40        820                492           240

 m   guaranteed-in-B strings ≤ m   2^(m-3)
 12              3666                   5.12e2
 16             79626                   8.19e3
 20           1561482                   1.31e5
 24          33304362                   2.10e6
 28         602846378                   3.36e7

 n   reachable poset states
  0              1
  1              1
  2              3
  3             19
  4            219
  5           4231
  6         130023
```

- The reachable-state counts are exactly OEIS **A001035** (labelled posets),
  confirming Lemma 1.3/1.4.
- The unary count is `O(L²)` (Lemma 3.1) and the advice bound is `O(L log L)`
  (Theorem 3.3).
- The binary count uses only *guaranteed* members (`k ≥ U(n)`), and grows
  exponentially in `m` (Theorem 4.6).
- The length cutoff `t_L` (Theorem 3.7) is confirmed for `L ≤ 7` using the exact
  `S(0..6) = 0,0,1,3,5,7,10`: the accepted `n` are exactly `[0, t_L]` with
  `t_1=0, t_2=1, t_3=1, t_4=2, t_5=2, t_6=2, t_7=3`, and each `t_L` fits in
  `⌈log₂ L⌉` bits.

No finite computation here proves a complexity separation.

---

## 9. Summary

| Statement | Status |
|---|---|
| `SORT-BOUND-U ∈ EXPTIME` via the poset DP | `[deduction]` Thm 2.1 |
| `SORT-BOUND-B ∈ 2-EXPTIME` via the same DP | `[deduction]` Thm 2.2 |
| poset DP runs in `2^{O(n²)}` numeric; no log overhead | `[deduction]` Thm 1.6, Rem 1.7 |
| `SORT-BOUND-U` is sparse | `[deduction]` Lem 3.1 |
| `SORT-BOUND-U ∈ P/poly` with `O(L log L)` advice | `[deduction]` Thm 3.3 |
| `SORT-BOUND-U ∈ P/log` via length cutoff `t_L` | `[deduction]` Thm 3.7 |
| `SORT-BOUND-U` not many-one NP-hard unless `P=NP` | `[literature]` Mahaney |
| `SORT-BOUND-U` not Turing NP-hard unless `PH=Σ₂P` | `[literature]` Karp–Lipton |
| `SORT-BOUND-B` not sparse; Mahaney inapplicable | `[deduction]` Thm 4.6 |
| explicit tree witness has `≥ n!` leaves (`2^{Θ(L_U)}` unary); not `NP` | `[deduction]` Thm 5.2 |
| `SORT-BOUND-U`/`-B ∈ NP` or `coNP` | `[open]` |
| `SORT-BOUND-U`/`-B` hard for `NP`/`PSPACE`/`EXPSPACE` | `[open]` |
| poly-size certificate for `S(n) ≤ k` or `> k` | `[open]` Thm 5.4 |
| any unconditional separation | **not claimed** |

---

## 10. Sources

- S. R. Mahaney, *Sparse complete sets for NP: Solution of a conjecture of
  Berman and Hartmanis*, J. Comput. System Sci. **25**(2) (1982) 130–143,
  https://doi.org/10.1016/0022-0000(82)90002-2 .
  Open author manuscript:
  https://ecommons.cornell.edu/entities/publication/02e42763-8a49-4dfe-9e73-59ccc016f74f .
- J. A. Grochow, *NP-hard sets are not sparse unless P = NP: An exposition of a
  simple proof of Mahaney's Theorem, with applications*, arXiv:1610.05825
  [cs.CC], 2016, https://arxiv.org/abs/1610.05825 ,
  https://doi.org/10.48550/arXiv.1610.05825 . (Simple Agrawal-style proof of
  Mahaney; Fortune's theorem; Ogiwara–Watanabe context.)
- S. Fortune, *A note on sparse complete sets*, SIAM J. Comput. **8**(3) (1979)
  426–430, https://doi.org/10.1137/0208034 . (No sparse coNP-complete set
  unless `P = NP`.)
- M. Ogiwara, O. Watanabe, *Polynomial-time bounded truth-table reducibility of
  NP sets to sparse sets*, SIAM J. Comput. **20**(3) (1991) 471–483,
  https://doi.org/10.1137/0220030 . (No sparse `≤^p_btt`-hard set for NP unless
  `P = NP`.)
- R. M. Karp, R. J. Lipton, *Some connections between nonuniform and uniform
  complexity classes*, STOC 1980, 302–309,
  https://doi.org/10.1145/800141.804678 . (`NP ⊆ P/poly ⇒ PH = Σ₂P`; Turing
  reductions to sparse sets.)
- J. Kadin, *P^NP[log n] and sparse Turing-complete sets for NP*, Proc. 2nd
  Annual Conference on Structure in Complexity Theory (SCT) 1987, 33–40,
  https://doi.org/10.1109/PSCT.1987.10319252 . (Refinement of Karp–Lipton.)
- P. Young, *How reductions to sparse sets collapse the polynomial-time
  hierarchy: a primer*, SIGACT News **23**(3) (1992),
  https://doi.org/10.1145/148080.148084 . (Uniform exposition of Karp–Lipton,
  Long, Kadin.)
- D. J. Kleitman, B. L. Rothschild, *Asymptotic enumeration of partial orders
  on a finite set*, Trans. Amer. Math. Soc. **205** (1975) 205–220,
  https://doi.org/10.1090/s0002-9947-1975-0369090-9 .
  (`log₂ P_n = n²/4 + 3n/2 + O(log n)`.)
- OEIS **A001035** (labelled posets: `1, 3, 19, 219, 4231, 130023, …`),
  https://oeis.org/A001035 (index, not a proof).
- G. Brightwell, P. Winkler, *Counting linear extensions is #P-complete*,
  STOC 1991, https://doi.org/10.1145/103418.103441 .
- A. K. Chandra, D. C. Kozen, L. Stockmeyer, *Alternation*, J. ACM **28**(1)
  (1981) 114–133, https://doi.org/10.1145/322234.322243 .
  (`APTIME = PSPACE`, `AEXPTIME = EXPSPACE`; used for the stronger game
  bounds, Remark 2.4.)
- Exact sorting numbers: M. Peczarski, *Towards optimal sorting of 16
  elements*, Acta Univ. Sapientiae Inform. **4**(2) (2012) 215–224,
  https://real-j.mtak.hu/23036/2/Acta%20Info%202012_4_2.pdf ; F. Stober,
  A. Weiß, *Lower bounds for sorting 16, 17, and 18 elements*,
  arXiv:2206.05597 (2022); OEIS **A036604** (index).
- Related hardness that does **not** transfer: L. Hyafil, R. L. Rivest,
  *Constructing optimal binary decision trees is NP-complete*, Inform. Process.
  Lett. **5**(1) (1976) 15–17, https://doi.org/10.1016/0020-0190(76)90095-8 ;
  E. S. Laber, L. T. Nogueira, *On the hardness of the minimum height decision
  tree problem*, Discrete Appl. Math. **144**(1–2) (2004) 209–212,
  https://doi.org/10.1016/j.dam.2004.06.002 ; I. Parberry on optimal sorting
  network verification. These concern arbitrary tests or fixed networks, not the
  single-parameter family `S(n)`.

---

## 11. Next unresolved obstacle

The central obstruction remains the **absence of a compact canonical object**
describing optimal comparison play. The only known upper-bound certificates are
exponential (explicit trees) or super-polynomial (poset tables); the only known
lower-bound potential (`log₂ e(P)`) is `#P`-hard and not tight. The `P/log`
membership of `SORT-BOUND-U` (Theorem 3.7, sharpening Theorem 3.3) is a
nonuniform fact and does not close this gap. The most informative next experiment is to measure the number
of distinct poset states lying on *some* height-`S(n)` optimal play, for
`n = 7…10`, and compare it with `n!`, with A001035, and with `poly(n)`. If it is
polynomially bounded, a succinct branching-program certificate route becomes
plausible; if it matches the full poset count, that is evidence against such a
route. Either outcome is a useful, falsifiable result.
