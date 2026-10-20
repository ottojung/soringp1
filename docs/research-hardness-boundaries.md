# Complexity barriers between generalized poset sorting and the antichain S(n)

**Status:** research note (literature audit + two provable barriers + one small
experiment). It is **not** Lean-checked. Every item is labelled `[literature]`,
`[deduction]`, `[experiment]`, `[conjecture]` or `[open]`. No NP-hardness, no
separation, and no new complexity-class membership is claimed. Companion
program: `scripts/hardness_boundaries.py`; regression checks:
`tests/test_hardness_boundaries.py`.

This note responds to the request to compare the **generalized arbitrary-poset**
question `CanSort(P,k)` with the **special antichain** question `S(n) ≤ k`, and
to audit the two most-cited nearby hardness results (Hyafil–Rivest 1976;
Cardinal et al. 2009) without letting their conclusions transfer. It also audits
the unary sparse/`P/log` and binary non-sparsity claims already recorded in
`docs/research-encoding-consequences.md` and `docs/research-certificates-barriers.md`.

---

## 0. Problems, encodings, and the one structural fact

`[definition]` From `docs/problem.md`:

- `S(n)` = minimum height (worst-case number of adaptive pairwise comparisons)
  of a decision tree sorting `n` distinct labelled keys. This is the
  **antichain** problem: the initial state is the empty poset.
- For a finite poset `P` on `n` labelled elements, let `S(P)` be the minimum
  height of a comparison tree that determines the unknown linear extension of
  `P`. This is the **generalized** problem (`CanSort(P,k)` is the decision
  version `S(P) ≤ k`).
- `SORT-BOUND-U = { 1^n # 1^k : S(n) ≤ k }` (both parameters unary).
- `SORT-BOUND-B = { bin(n) # bin(k) : S(n) ≤ k }` (both parameters binary).
- `GEN-SORT` = `{ ⟨P⟩ # bin(k) : S(P) ≤ k }`, with **the encoding fixed**
  to an explicit labelled `n×n` comparability matrix (including `n` in a
  parseable header). `GEN-SORT` here is the dense-matrix decision version of
  `CanSort(P,k)`; its input has length `N = Ω(n²)` regardless of how many
  entries in the matrix are zero. A sparse edge-list encoding **with `n`
  encoded in binary and no explicit vertex list** defines a *different*
  language: the antichain may then have only `O(log n)` input bits, so the
  matrix-based `PSPACE`/runtime bounds cannot be transferred to it by
  silently assuming `N = Θ(n²)`.

`[deduction]` **Fact 0.1 (antichain dominates every poset).** For every poset
`P` on `n` elements, `S(P) ≤ S(n)`. *Proof.* The linear extensions of `P` are a
subset of the `n!` permutations, so any tree correct on all permutations is
correct on `P`. ∎

`[deduction]` **Fact 0.2 (information bound).** For every poset `P`,
`log₂ e(P) ≤ S(P)`, where `e(P)` is the number of linear extensions. This is
the decision-tree leaf-counting bound. It is **not** tight in general:
`S(12) = 30 > ⌈log₂ 12!⌉ = 29` (`[literature]`, Wells 1965; Peczarski 2012).

The two facts together give, for every poset on `n` elements,
`log₂ e(P) ≤ S(P) ≤ S(n) ≤ n⌈log₂ n⌉`.

---

## 1. The containment is encoding-sensitive (the transfer lemma)

The generalized problem *contains* the antichain problem, but the containment
reduction is polynomial-time only under the unary encoding. This is the precise
sense in which "hardness for one does not automatically transfer".

`[deduction]` **Lemma 1.1 (unary antichain embedding is polynomial).** The map
`φ_U(1^n # 1^k) = ⟨A_n⟩ # bin(k)`, where `A_n` is the antichain on `n`
elements, is computable in time polynomial in `n + k`. If `⟨A_n⟩` is the `n×n`
all-zero comparability matrix, then `|⟨A_n⟩| = n² = poly(n)`. Hence

```
SORT-BOUND-U ≤_m^p GEN-SORT .
```

`[deduction]` **Lemma 1.2 (binary antichain embedding is exponential).** The
analogous map `φ_B(bin(n) # bin(k)) = ⟨A_n⟩ # bin(k)` outputs `n² + O(log n +
log k)` bits. For input length `m = Θ(log n + log k)` we have `n = 2^{Θ(m)}`, so
the output length is `2^{Θ(m)}`. The map is therefore **not** polynomial-time,
and this route does **not** establish `SORT-BOUND-B ≤_m^p GEN-SORT`.

`[deduction]` **Corollary 1.3 (transfer directions).** Write `A = SORT-BOUND-U`
and `B = GEN-SORT`.

1. **Upper bounds transfer down.** If `B ∈ P` then `A ∈ P` (by Lemma 1.1).
2. **Hardness transfers up.** If `A` is `C`-hard under `≤_m^p` then `B` is
   `C`-hard: for every `L ∈ C`, `L ≤_m^p A ≤_m^p B`.
3. **The converses do not follow.** `B ∈ P` does not imply `SORT-BOUND-B ∈ P`
   (Lemma 1.2 blocks the obvious route). `B` being `C`-hard does not imply `A`
   is `C`-hard: the reduction in Lemma 1.1 runs the wrong way for that
   inference.

`[literature]` **Remark 1.4 (Mahaney applies to the unary special case, not to
`GEN-SORT`).** `SORT-BOUND-U` is sparse (§4), so it is not many-one NP-hard
unless `P = NP` (Mahaney 1982). This blocks the *upward* route
"`A` NP-hard ⇒ `B` NP-hard" for many-one NP-hardness. It does **not** constrain
`B` directly: `GEN-SORT` is not sparse (an explicit poset can carry `Θ(n²)` bits),
so Mahaney's theorem is not available for it. `SORT-BOUND-B` is not sparse
either (§4).

`[deduction]` **Remark 1.5 (the generalized problem is not a single complexity
question).** Its input length depends on the **encoding scheme**, not on whether
the poset happens to have many relations. In the dense **matrix
representation fixed in §0**, `N = Θ(n² + log(k+2))` and the transcript-only
budgeted DFS of `docs/research-budgeted-dfs.md` (§5.2, §7.1) runs in time
`2^{O(n log² n)} = 2^{O(√N log² N)}` and work space `O(n log² n) = O(√N log² N)`
bits, so `GEN-SORT ∈ DSPACE(O(√N log² N)) ∩ DTIME(2^{O(√N log² N)})` for that
**matrix encoding** (with the budget `k` clamped to `O(n log n)` before
minimax). This is a **sublinear-space** upper bound because `√N log² N = o(N)`;
it is a space bound only, and no hardness, completeness or tightness is claimed.
The `O(√N log² N)` bound assumes the matrix is on a read-only input tape and is
queried by index; a matrix-per-frame implementation would instead cost
`O(n³ log n) = O(N^{3/2} log N)` and give only `PSPACE`. For a *different
sparse edge-list representation* with binary `n`, the antichain
has `N = O(log n)`, and the same method gives only the
`EXPSPACE` upper bound of `SORT-BOUND-B` (Claim A of
`docs/research-certificates-barriers.md`). If a pair-list format also
lists all `n` vertices explicitly, that representation instead has
`N = Ω(n)` and yields `PSPACE`; one must specify which format is used. A statement about "the complexity of `CanSort(P,k)`" is therefore
incomplete without fixing the poset encoding.

---

## 2. Model audit: Hyafil–Rivest is about arbitrary tests, not pairwise comparisons

`[literature]` L. Hyafil and R. L. Rivest, *Constructing optimal binary decision
trees is NP-complete*, Inform. Process. Lett. **5**(1) (1976) 15–17,
doi:10.1016/0020-0190(76)90095-8. Open PDF:
https://people.csail.mit.edu/rivest/pubs/HR76.pdf .

**Their model.** A finite object set `X = {x_1,…,x_n}` and a finite test set
`T = {T_1,…,T_r}` are given; each test `T_i` is a **subset** of `X`, and the
unknown object is identified by asking membership questions. A binary decision
tree assigns a test to each internal node; the cost is the **expected** number of
tests (they note the same construction works for worst-case cost). The decision
problem `DT(T,X,w)` asks whether a tree of cost `≤ w` exists. They prove
`DT(T,X,w)` NP-complete by reduction from **EC3** (exact cover by 3-sets): for
`sufficiently large n`, every optimal tree must use a **3-element subset** as
its root test, so the root solves the corresponding EC3 instance.

**Why it does not transfer.** `[deduction]` The Hyafil–Rivest object is a
*general binary decision tree* over **arbitrary subset tests**; the object here
is a *comparison tree* whose tests are the **2-element pairs** `{x,y}` of a
poset, with two outcomes. The comparison-poset model is a strict restriction of
the test family, and it fixes the object set to `n` labelled keys and the test
set to all pairs. NP-completeness of a more general problem does **not**
imply NP-completeness of a restriction. Concretely, the EC3 gadget uses 3-element
subset tests, which do not exist in the pairwise-comparison model. Hence
Hyafil–Rivest is not a theorem about `GEN-SORT`, `SORT-BOUND-U`, or
`SORT-BOUND-B`.

`[literature]` The same caveat applies to E. S. Laber and L. T. Nogueira, *On
the hardness of the minimum height decision tree problem*, Discrete Appl. Math.
**144**(1–2) (2004) 209–212, doi:10.1016/j.dam.2004.06.002, which shows the
minimum-height decision tree problem with **arbitrary tests** has no
`o(log n)`-approximation unless `P = NP`. Again arbitrary tests, not pairwise
comparisons on a fixed poset.

---

## 3. Model audit: Cardinal et al. is constant-factor approximation, not exact evaluation

`[literature]` J. Cardinal, S. Fiorini, G. Joret, R. M. Jungers, J. I. Munro,
*Sorting under partial information (without the ellipsoid algorithm)*,
Combinatorica **33**(6) (2013) 655–697, doi:10.1007/s00493-013-2821-5;
arXiv:0911.0086 (STOC 2010). This is the primary source requested.

**Their model.** The input is a poset `P` on `n` elements, given explicitly
(Hasse diagram or oracle). The goal is to discover an unknown linear extension
of `P` by pairwise comparisons. They distinguish **query complexity** (number
of comparisons), **preprocessing complexity** (work before the first
comparison), and **sorting complexity** (the rest). They give polynomial-time
algorithms performing:

- `O(log n · log e(P))` comparisons in `O(n²)` time;
- at most `(1+ε) log e(P) + O_ε(n)` comparisons in `O(n^{2.5})` time;
- `O(log e(P))` comparisons in `O(n^{2.5})` time.

**What this does and does not establish.** `[deduction]` These algorithms
approximate the information bound `log e(P)` up to a **constant factor**. They
do **not** compute the exact value `S(P)`, and they do not decide
`CanSort(P,k)`. The exact value can exceed `log e(P)` (Fact 0.2), so a
constant-factor-optimal strategy is not an exact one. The computational
bottleneck is in preprocessing; the comparison count is constant-factor optimal,
not exact.

`[literature]` The lineage is: Fredman (1976) introduced the problem and gave
`log e(P) + O(n)` comparisons; Kahn–Saks (1984) gave a `3/11`–`8/11` balanced
pair, hence `O(log e(P))` comparisons with exponential running time (it counts
linear extensions); Kahn–Kim (1995) gave the first polynomial-time
`O(log e(P))`-comparison algorithm via the ellipsoid method; Cardinal et al.
removed the ellipsoid method. A secondary source (Cardinal–Joret–Roland,
arXiv:1902.06473) summarizes this as "an optimal sequence of comparisons can be
found in polynomial time", where "optimal" means **constant-factor optimal in the
number of comparisons**, not exact.

**Why it does not transfer.** `[deduction]` A polynomial-time algorithm that
finds a strategy with `O(log e(P))` comparisons does not decide whether
`S(P) ≤ k` for a given `k`, because the exact optimum may be strictly larger
than `log e(P)`. Hence the Cardinal et al. result does not classify `GEN-SORT`
or `SORT-BOUND`, and does not imply membership or hardness for either.

---

## 4. Encoding audit: unary sparse/`P/log` and binary non-sparsity

The claims below are already recorded in `docs/research-encoding-consequences.md`;
this section audits them and records what they do **not** say.

`[deduction]` **Lemma 4.1 (unary sparsity).** `SORT-BOUND-U` is sparse: the
number of its strings of length at most `L` is `O(L²)`. *Proof.* A string has the
form `1^n # 1^k` with `n + k + 1 ≤ L`; there are at most `(L+1)(L+2)/2` such
pairs. ∎

`[literature]` **Theorem 4.2 (Mahaney/Fortune/Ogiwara–Watanabe/Karp–Lipton).**
Consequently `SORT-BOUND-U` is not NP-hard under polynomial-time many-one
reductions unless `P = NP` (Mahaney 1982); not coNP-hard under many-one
reductions unless `P = NP` (Fortune 1979); not NP-hard under bounded
truth-table reductions unless `P = NP` (Ogiwara–Watanabe 1991); and not
NP-hard under Turing reductions unless `PH = Σ₂P` (Karp–Lipton 1980). These are
conditional barriers, not membership statements.

`[literature]` **Theorem 4.2a (Berman–Hartmanis, 1977).**
No polynomially sparse language is **EXPTIME-complete** under polynomial-time
many-one reductions. This unconditional theorem concerns EXPTIME, unlike the
conditional NP-hardness barrier from Mahaney. Original source: L. Berman and
J. Hartmanis, *On isomorphisms and density of NP and other complete sets*,
SIAM J. Comput. **6**(2) (1977), 305–322,
https://doi.org/10.1137/0206023 (EXPTIME sparsity theorem).

`[deduction]` **Corollary 4.2b (the unary threshold is not EXPTIME-hard).**
`SORT-BOUND-U` is **unconditionally not EXPTIME-hard under
polynomial-time many-one reductions**. Its strings of length `L` have
the form `1^n#1^k` with `n+k+1=L`, hence there are at most `L`
accepted strings of length `L` (and `O(L²)` up to length `L`),
by Lemma 4.1. This is *not* "at most one accepted string per length":
the accepted `n` may fill an initial interval, Theorem 4.3.
The known deterministic budgeted evaluator places `SORT-BOUND-U`
in EXPTIME. If the language were EXPTIME-hard under the stated
reductions, it would be EXPTIME-complete, contradicting Theorem 4.2a.
This does **not** exclude hardness under polynomial-time Turing
reductions, does not prove membership in `P` or `NP`, and gives no
complexity-class separation.

`[deduction]` **Theorem 4.3 (`SORT-BOUND-U ∈ P/log`).** Write the total input
length as `L = n + k + 1`, so membership is `S(n) ≤ L - 1 - n`, i.e.
`f(n) := n + S(n) ≤ L - 1`. The kernel-checked monotonicity `S_mono` gives
`f(n+1) - f(n) = 1 + S(n+1) - S(n) ≥ 1`, so `f` is strictly increasing. For
each `L`, the accepted `n` form the initial interval `[0, t_L]` with
`t_L = max{ n ≤ L-1 : f(n) ≤ L-1 }`. Advice `a_L = t_L` uses `⌈log₂ L⌉` bits;
the verifier parses `n` and accepts iff `n ≤ t_L`, in `O(L)` time. Hence
`SORT-BOUND-U ∈ P/O(log L) = P/log`. ∎

`[deduction]` **Audit.** The argument is correct and uses only `S_mono`, which
is kernel-checked. It is a **nonuniform** bound: the advice `t_L` need not be
computable, and `P/log` membership does not imply membership in `P`, `NP`, or any
uniform class. It is consistent with sparsity (indeed `P/log ⊆ P/poly`, and
sparse sets are in `P/poly`). The cutoff values are confirmed for `L ≤ 12` by
`scripts/hardness_boundaries.py`:

```
 L   1  2  3  4  5  6  7  8  9 10 11 12
t_L   0  1  1  2  2  2  3  3  3  4  4  4
```

`[deduction]` **Theorem 4.4 (binary language is not sparse).** `SORT-BOUND-B`
is not sparse. *Proof sketch.* Fix `m` large and `1 ≤ n ≤ 2^{m/3}`. Then
`|bin(n)| ≤ m/3 + 1`, so the largest `k` with `bin(n)#bin(k)` of length at most
`m` satisfies `|bin(k)| ≤ K_n ≥ 2m/3 - 2`. Every `k ≥ U(n)` is guaranteed to be
in the language (`S(n) ≤ U(n) ≤ k`), and there are `2^{K_n} - U(n)` such `k`.
Summing over `n ≤ 2^{m/3}` gives at least `2^{m-3}` strings of length at most
`m`. ∎

`[experiment]` `scripts/hardness_boundaries.py` counts the guaranteed members
exactly: for `m = 8,12,16,20,24` the counts are `128, 3666, 79978, 1565194,
33318698`, all `> 2^{m-3}`. This is an exact count of the guaranteed set, so it
is slightly larger than the lower bound reported in
`docs/research-encoding-consequences.md`; both establish non-sparsity.

`[deduction]` **What the audit does not say.** None of the above establishes
NP-hardness, coNP-hardness, or any uniform membership for `SORT-BOUND-U`,
`SORT-BOUND-B`, or `GEN-SORT`. The binary non-sparsity result merely **removes**
the sparse-set obstruction for `SORT-BOUND-B`; it is not evidence of hardness.

---

## 5. The non-reduction barrier: `e(P)` does not determine `S(P)`

The natural route from exact sorting to counting linear extensions is: compute
`e(P)`, then read off `S(P)`. This fails, and a small experiment exhibits the
failure.

`[experiment]` **Proposition 5.1 (non-reduction).** There is no function `f`
with `S(P) = f(e(P))` for all posets `P`. Equivalently, the exact comparison
cost is not determined by the number of linear extensions.

*Proof (computational witness).* Let

```
P1 = (8, 12, 8, 0, 12)   relations 0<3, 1<2, 1<3, 2<3, 4<2, 4<3
P2 = (26, 0, 10, 0, 8)   relations 0<1, 0<3, 0<4, 2<1, 2<3, 4<3
```

where a poset on `{0,…,4}` is the tuple of successor bitmasks (transitively
closed). Both are valid posets, and

```
e(P1) = 8,  S(P1) = 3
e(P2) = 8,  S(P2) = 4 .
```

Hence `e(P1) = e(P2)` but `S(P1) ≠ S(P2)`. ∎

`[experiment]` Minimality: exhaustive enumeration over all posets on `n ≤ 5`
(4231 states at `n = 5`) finds **no** `e`-value attained by two posets with
different `S` for `n ≤ 4`; the first collision is at `n = 5`, `e = 8`, with the
pair above. `scripts/hardness_boundaries.py` reproduces this.

`[deduction]` **Corollary 5.2 (the one-shot #P route is not the obstruction).**
There is no reduction that computes `e(P)` once and then applies a function of
`e(P)` to obtain `S(P)`, because `S(P)` is not such a function. A more elaborate
Turing reduction that queries `e(·)` on *derived* posets is not ruled out by
this witness. More importantly, the `#P`-completeness of `e(P)`
(Brightwell–Winkler 1991) is **not** the reason exact `S(P)` is hard: the
antichain has `e = n!`, trivially computable, yet `S(n)` is not known to be
polynomial-time computable. The obstruction is the non-tightness of the
information bound (Fact 0.2), not the hardness of counting linear extensions.

`[deduction]` **Corollary 5.3 (constant-factor optimality is not exactness).**
The polynomial-time algorithms of §3 optimize a surrogate — graph entropy, a
constant-factor approximation of `log e(P)` — that does not determine `S(P)`.
Their polynomial running times therefore do not resolve exact evaluation, and
their "optimal" comparison counts are constant-factor optimal, not exact.

---

## 6. Known vs open

| Statement | Status |
|---|---|
| `SORT-BOUND-U` sparse; not many-one NP-hard unless `P=NP` | `[literature]` Mahaney 1982 |
| `SORT-BOUND-U ∈ P/log` (nonuniform) | `[deduction]` Thm 4.3 |
| `SORT-BOUND-B` not sparse; Mahaney inapplicable | `[deduction]` Thm 4.4 |
| `SORT-BOUND-U ∈ PSPACE`, `SORT-BOUND-B ∈ EXPSPACE` | `[deduction]` Claim A, `research-certificates-barriers.md` |
| `GEN-SORT ∈ DSPACE(O(√N log² N)) ∩ EXPTIME` for dense poset encodings (sublinear space, upper bound only) | `[deduction]` Rem 1.5; `research-budgeted-dfs.md` §7.1 |
| `SORT-BOUND-U ≤_m^p GEN-SORT`; upper bounds transfer down, hardness up | `[deduction]` Lem 1.1, Cor 1.3 |
| `SORT-BOUND-B ≤_m^p GEN-SORT` via the antichain embedding | **fails** (exponential output, Lem 1.2) |
| Hyafil–Rivest NP-completeness applies to `GEN-SORT`/`SORT-BOUND` | **does not transfer** (arbitrary subset tests) |
| Cardinal et al. poly-time algorithms compute exact `S(P)` | **no** (constant-factor approximation) |
| `S(P) = f(e(P))` for some `f` | **false** (Prop 5.1) |
| `SORT-BOUND-U ∈ NP` or `coNP` | `[open]` |
| `SORT-BOUND-B ∈ NP` or `coNP` | `[open]` |
| `GEN-SORT` NP-hard / PSPACE-complete / in P | `[open]`; no primary source found |
| `S(n)` exact for `n ≥ 23` | `[open]` (known for `n ≤ 22`; `S(28) ≥ 99`) |
| any unconditional separation | **not claimed** |

`[open]` **World status.** The exact complexity of `SORT-BOUND` and of
`GEN-SORT` is not settled by any primary source we found. The problem is in
`PSPACE` (and `EXPSPACE` for the binary antichain encoding), no succinct
certificate is known, and no NP-hardness result is known for the pairwise
comparison model. A cstheory question asking exactly whether the poset decision
problem is NP-hard reports that no reference was found; we treat this as a
lead, not as evidence. We do **not** claim the problem is open in a formally
certified sense, only that no classification is available to us.

---

## 7. Sources

- L. Hyafil, R. L. Rivest, *Constructing optimal binary decision trees is
  NP-complete*, Inform. Process. Lett. **5**(1) (1976) 15–17,
  https://doi.org/10.1016/0020-0190(76)90095-8 ;
  https://people.csail.mit.edu/rivest/pubs/HR76.pdf . (Arbitrary subset tests,
  expected cost, EC3 reduction.)
- E. S. Laber, L. T. Nogueira, *On the hardness of the minimum height decision
  tree problem*, Discrete Appl. Math. **144**(1–2) (2004) 209–212,
  https://doi.org/10.1016/j.dam.2004.06.002 . (Arbitrary tests, `o(log n)`
  inapproximability.)
- J. Cardinal, S. Fiorini, G. Joret, R. M. Jungers, J. I. Munro, *Sorting under
  partial information (without the ellipsoid algorithm)*, Combinatorica
  **33**(6) (2013) 655–697, https://doi.org/10.1007/s00493-013-2821-5 ;
  arXiv:0911.0086, https://arxiv.org/abs/0911.0086 . (Poly-time constant-factor
  comparison algorithms.)
- M. L. Fredman, *How good is the information theory bound in sorting?*,
  Theoret. Comput. Sci. **1**(4) (1976) 355–361,
  https://doi.org/10.1016/0304-3975(76)90078-5 . (Introduces sorting under
  partial information; `log e(P) + O(n)`.)
- J. Kahn, M. Saks, *Balancing poset extensions*, Order **1**(2) (1984) 113–126,
  https://doi.org/10.1007/BF00565647 ; STOC version
  https://doi.org/10.1145/800057.808694 . (`3/11`–`8/11` balanced pair.)
- J. Kahn, J. H. Kim, *Entropy and sorting*, J. Comput. System Sci. **51**(3)
  (1995) 390–399, https://doi.org/10.1006/jcss.1995.1077 . (Poly-time
  `O(log e(P))` comparisons via the ellipsoid method.)
- G. Brightwell, P. Winkler, *Counting linear extensions*, Order **8**(3) (1991)
  225–242, https://doi.org/10.1007/BF00383444 ; STOC version
  https://doi.org/10.1145/103418.103441 . (`#P`-complete.)
- J. Cardinal, G. Joret, J. Roland, *Information-theoretic lower bounds for
  quantum sorting*, arXiv:1902.06473, https://arxiv.org/abs/1902.06473 .
  (Summary of the classical lineage; "optimal" = constant-factor optimal.)
- S. R. Mahaney, *Sparse complete sets for NP*, J. Comput. System Sci. **25**(2)
  (1982) 130–143, https://doi.org/10.1016/0022-0000(82)90002-2 .
- S. Fortune, *A note on sparse complete sets*, SIAM J. Comput. **8**(3) (1979)
  426–430, https://doi.org/10.1137/0208034 .
- M. Ogiwara, O. Watanabe, *Polynomial-time bounded truth-table reducibility of
  NP sets to sparse sets*, SIAM J. Comput. **20**(3) (1991) 471–483,
  https://doi.org/10.1137/0220030 .
- R. M. Karp, R. J. Lipton, *Some connections between nonuniform and uniform
  complexity classes*, STOC 1980, https://doi.org/10.1145/800141.804678 .
- A. K. Chandra, D. C. Kozen, L. Stockmeyer, *Alternation*, J. ACM **28**(1)
  (1981) 114–133, https://doi.org/10.1145/322234.322243 .
- Exact sorting numbers: M. Peczarski, *Towards optimal sorting of 16 elements*,
  Acta Univ. Sapientiae Inform. **4**(2) (2012) 215–224,
  https://real-j.mtak.hu/23036/2/Acta%20Info%202012_4_2.pdf ; F. Stober,
  A. Weiß, *Lower bounds for sorting 16, 17, and 18 elements*, arXiv:2206.05597
  (2022); OEIS A036604 (index).

---

## 8. Next unresolved obstacle

The central obstruction is unchanged: there is no compact canonical object that
determines exact optimal comparison play, and §5 shows that the most obvious
candidate — the number of linear extensions — does not suffice. Two concrete
consequences for future work:

1. **Exactness requires a new invariant.** Any exact lower-bound certificate
   must distinguish posets with equal `e(P)` (the `n = 5`, `e = 8` pair above is
   the smallest witness). The information bound `⌈log₂ e(P)⌉` cannot be the
   whole story.
2. **Transfer must be argued, not assumed.** A hardness result for
   `GEN-SORT` would not automatically give hardness for `SORT-BOUND-U` or
   `SORT-BOUND-B` (Corollary 1.3), and a hardness result for the antichain would
   not automatically give hardness for `GEN-SORT` under the binary encoding
   (Lemma 1.2). Any proposed reduction must be checked against the poset
   encoding and the unary/binary distinction.

**Reproduce:**

```
python3 scripts/hardness_boundaries.py
python3 -m unittest discover -s tests -v
```
