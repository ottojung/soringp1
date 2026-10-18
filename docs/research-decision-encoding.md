# Decision-language complexity of S(n): binary encoding, upper bounds, and certificate pitfalls

**Status:** research note (literature + deduction). **Not Lean-checked.** Every item
is labelled `[literature]`, `[deduction]`, `[experiment]`, `[conjecture]` or `[open]`.
No NP-hardness, no separation, no unconditional lower bound is claimed. This note
focuses on the **binary-encoded** decision language and the precise distinction
between EXPTIME in input length and double-exponential time.

---

## 0. Model and encodings (fixed)

`[definition]` From `docs/problem.md`:

- `S(n)` = minimum height (worst-case number of pairwise comparisons) of a
  **deterministic adaptive comparison decision tree** that correctly sorts every
  permutation of `n` distinct labelled keys.
- `SORT-BOUND-B = { bin(n) # bin(k) : S(n) ≤ k }` — both parameters **binary**.
- `SORT-BOUND-U = { 1^n # 1^k : S(n) ≤ k }` — both parameters **unary** (for contrast).
- Input lengths: `L_B = |bin(n)| + 1 + |bin(k)| = Θ(log(n+2) + log(k+2))`;
  `L_U = n + k + 1 = Θ(n + k + 1)`.
- For `n≥2`, `S(n) ∈ [⌈log₂ n!⌉, n⌈log₂ n⌉]`; this
  upper/lower-bound window has width `Θ(n)`. For `n=0,1`, `S(n)=0`.

---

## 1. Formal input-size bounds

`[deduction]` **Proposition 1.1 (binary input length).** For `SORT-BOUND-B` with
input `bin(n)#bin(k)`, the input length is

```
L_B = ell(n) + 1 + ell(k) = Θ(log(n+2) + log(k+2)),
```

Here `ell(0)=1` and `ell(t)=floor(log₂ t)+1` for `t≥1`: zero is
encoded by the one-character string `0`.

First, `S(0)=S(1)=0`: accept any nonnegative `k` for `n=0,1`.
For `n≥2` set `U(n)=n⌈log₂ n⌉`; accept immediately when `k≥U(n)`
(merge sort), and reject immediately when `k<⌈log₂(n!)⌉` (information
lower bound). Only the remaining window requires minimax search.
For **nontrivial** instances (`n≥2`, `k<U(n)`), `log(k+2)=O(log n)`, so
`L_B = Θ(log n)`. For **trivially large** `k≥U(n)`, the answer is yes with
`O(L_B)` preprocessing; very small `k` can also yield an immediate no.

`[deduction]` **Proposition 1.2 (numeric parameter vs input length).** Under binary
encoding, `n ≤ 2^{L_B}` and `k ≤ 2^{L_B}`. Hence any runtime expressed as a function
of numeric `n` must be translated using `n ≤ 2^{L_B}`; for nontrivial
instances `L_B=Θ(log n)`, so `n=2^{Θ(L_B)}` in that regime. A runtime `2^{poly(n)}` becomes `2^{2^{poly(L_B)}}`, which is **double
exponential** in `L_B`, not exponential.

---

## 2. Known upper bounds and their encoding sensitivity

`[deduction]` **Proposition 2.1 (memoized DP).** The poset-enumeration DP computes
`S(n)` in time `2^{O(n²)}` and space `2^{O(n²)}` (numeric `n`). Under binary
encoding this yields:

```
time  = 2^{O(n²)} = 2^{2^{O(L_B)}}  →  SORT-BOUND-B ∈ 2-EXPTIME
space = 2^{O(n²)} = 2^{2^{O(L_B)}}  →  not in EXPSPACE via this algorithm
```

`[deduction]` **Proposition 2.2 (budgeted DFS).** The budgeted DFS of
`docs/research-budgeted-dfs.md` decides `S(n) ≤ k` in time `2^{O(n log² n)}` and
space `O(n³ log n)` (numeric `n`). Under binary encoding:

```
time  = 2^{O(n log² n)} = 2^{2^{O(L_B)}}  →  2-EXPTIME
space = O(n³ log n) = 2^{O(L_B)}          →  SORT-BOUND-B ∈ EXPSPACE
```

`[deduction]` **Proposition 2.3 (game/ATM).** The alternating Turing machine of
`docs/research-certificates-barriers.md` Claim A decides the game `G(n,k)` in time
`O(k·n²)` and space `O(n²)`. Under binary encoding, for informative instances
`k = O(n log n) = 2^{O(L_B)}`:

```
time  = O(k·n²) = 2^{O(L_B)}  →  single exponential in L_B
space = O(n²) = 2^{O(L_B)}    →  SORT-BOUND-B ∈ EXPSPACE
```

By `APTIME = PSPACE` and `AEXPTIME = EXPSPACE` (Chandra–Kozen–Stockmeyer), the
ATM bound gives `SORT-BOUND-B ∈ EXPSPACE`. The ATM runs in time `2^{O(L_B)}`, but
its **deterministic simulation** requires either double-exponential time or
single-exponential space; the tighter deterministic bound is **EXPSPACE**.

`[deduction]` **Proposition 2.4 (strongest upper bound established in this repository).**
The strongest deterministic upper bound established here for `SORT-BOUND-B` is:

```
SORT-BOUND-B ∈ EXPSPACE.
```

This follows from the game/ATM (Proposition 2.3) and is strictly tighter than the
`2-EXPTIME` bound of the memoized DP (Proposition 2.1), since
`EXPSPACE ⊆ 2-EXPTIME`.

---

## 3. The EXPTIME vs double-exponential distinction

`[deduction]` **Proposition 3.1 (EXPTIME in input length).** A language is in
EXPTIME if it is decidable in deterministic time `2^{poly(m)}` where `m` is the
input length. For `SORT-BOUND-B`, `m = L_B = Θ(log n)`, so EXPTIME means time
`2^{poly(log n)}`.

`[deduction]` **Proposition 3.2 (double-exponential time).** A runtime
`2^{O(n log² n)}` in numeric `n`, under binary encoding `n = 2^{Θ(L_B)}`, becomes:

```
2^{O(n log² n)} = 2^{O(2^{L_B} · L_B²)} = 2^{2^{O(L_B)}}.
```

This is **double exponential** in `L_B`, not single exponential. It places the
language in `2-EXPTIME`, not `EXPTIME`.

`[deduction]` **Proposition 3.3 (the gap is real).** By the time hierarchy
theorem, `EXPTIME ⊊ 2-EXPTIME`. Hence a `2^{poly(n)}` bound under binary `n`
does **not** imply EXPTIME membership. The budgeted DFS bound
`2^{O(n log² n)}` is double exponential in the binary input length and does not
establish `SORT-BOUND-B ∈ EXPTIME`.

`[deduction]` **Proposition 3.4 (is EXPTIME achievable?).** Membership of
`SORT-BOUND-B` in `EXPTIME` is **not established by these arguments**. The game `G(n,k)` has `k = 2^{O(L_B)}` rounds
and branching factor `n² = 2^{O(L_B)}`, so the game tree has size
`2^{2^{O(L_B)}}`. No deterministic algorithm running in time `2^{poly(L_B)}` is
provided by this project. This is a research question here, not an
unqualified claim about the worldwide literature; a compact canonical object
for optimal comparison play might help.

---

## 4. Certificate representation pitfalls

`[deduction]` **Proposition 4.1 (explicit tree is not a certificate).** Every
correct comparison tree for `n` keys has at least `n!` reachable leaves and at
least `2n! − 1` nodes. Under binary encoding, `n! = 2^{Θ(n log n)} = 2^{2^{Θ(L_B)}}`,
so an explicit tree is doubly exponential in the input length. Verifying a tree is
polynomial in the **tree size**, not in the input length. Hence the tree witness
yields at most a `N2EXP` verifier, not `NP`.

`[deduction]` **Proposition 4.2 (full DP state space is not a compact certificate).**
The set of all labelled posets has `P_n = 2^{Θ(n²)}` potential entries (Kleitman–Rothschild), each describable with `O(n²)`
bits. Full tabulation under binary encoding would require
`2^{2^{O(L_B)}}` bits — doubly exponential; this does not show every
partial or goal-directed DP must store all of them.
No polynomial-size certificate is known for either `S(n) ≤ k` or `S(n) > k`.

`[deduction]` **Proposition 4.3 (no known succinct certificate).** Neither
`SORT-BOUND-U` nor `SORT-BOUND-B` is known to have a certificate polynomial in the
input length. The only known potential is `log₂ e(P)` (the base-2 logarithm of the
number of linear extensions of `P`), which is `#P`-complete to evaluate exactly
(Brightwell–Winkler) and is **not tight** (`S(12) = 30 > 29 = ⌈log₂ 12!⌉`).
Hence `NP` and `coNP` membership remain open.

---

## 5. Reduction barriers

`[literature]` **Proposition 5.1 (Mahaney).** If a sparse set is NP-hard under
polynomial-time many-one reductions, then `P = NP`.

`[deduction]` **Proposition 5.2 (unary barrier).** `SORT-BOUND-U` is sparse (at most
`O(L²)` strings of length `≤ L`). By Mahaney's theorem, it is not NP-hard under
many-one reductions unless `P = NP`. Under Turing reductions, NP-hardness would
collapse `PH` to `Σ₂P` (Karp–Lipton; Ogiwara–Watanabe).

`[deduction]` **Proposition 5.3 (binary non-sparsity).** `SORT-BOUND-B` is **not**
sparse: for `m≥4`, fix `n=1` and vary the positive integer `k` among
binary strings of length at most `m−2`. Since `S(1)=0`, every one of these
`2^{m−2}−1 ≥ 2^{m−3}` distinct length-`≤m` strings is a yes-instance.
Thus the Mahaney sparse-set barrier does **not** apply as stated to this
binary language. This particular density witness uses **trivial** large-`k`
instances, so its density alone conveys no hardness information. A separate
analysis would be required for the promise/restricted *informative* sublanguage.

---

## 6. State representation is not a space lower bound

`[deduction]` **Observation 6.1 (no lower bound follows from explicit state
size).** The current minimax algorithms store an `n`-element partial order as
an `n×n` relation, requiring `O(n²)` bits. This is an **upper bound for a
particular representation**, not a lower bound on the space needed to decide
the special binary language `SORT-BOUND-B`. A different algorithm might not
construct a poset at all. Therefore no `Ω(n²)` space lower bound or
`SORT-BOUND-B ∉ PSPACE` conclusion is justified. Establishing a space
lower bound would require an independent complexity-theoretic argument.

---

## 7. Summary of exact propositions

| Proposition | Statement | Status |
|---|---|---|
| 1.1 | `L_B = Θ(log(n+2) + log(k+2))`; nontrivial: `Θ(log n)` | `[deduction]` |
| 1.2 | `n ≤ 2^{L_B}`; `2^{poly(n)} = 2^{2^{poly(L_B)}}` | `[deduction]` |
| 2.1 | DP: `2^{O(n²)}` → `2-EXPTIME` binary | `[deduction]` |
| 2.2 | DFS: `2^{O(n log² n)}` time, `2^{O(L_B)}` space → `EXPSPACE` binary | `[deduction]` |
| 2.3 | ATM: `O(k·n²)` time, `O(n²)` space → `EXPSPACE` binary | `[deduction]` |
| 2.4 | Repository upper bound: `SORT-BOUND-B ∈ EXPSPACE` | `[deduction]` |
| 3.1 | EXPTIME = `2^{poly(L_B)}` | `[definition]` |
| 3.2 | `2^{O(n log² n)} = 2^{2^{O(L_B)}}` double exponential | `[deduction]` |
| 3.3 | `EXPTIME ⊊ 2-EXPTIME`; DFS bound ≠ EXPTIME | `[deduction]` |
| 3.4 | `SORT-BOUND-B ∈ EXPTIME` not established here | `[open]` |
| 4.1 | Tree witness: `≥ n!` leaves, `2^{2^{Θ(L_B)}}` binary; not `NP` | `[deduction]` |
| 4.2 | Full DP state space: `2^{Θ(n²)}` potential entries, doubly exponential binary | `[deduction]` |
| 4.3 | No known succinct certificate for either direction | `[open]` |
| 5.1 | Mahaney: sparse NP-hard ⇒ `P = NP` | `[literature]` |
| 5.2 | `SORT-BOUND-U` sparse; Mahaney barrier applies | `[deduction]` |
| 5.3 | `SORT-BOUND-B` not sparse; barrier inapplicable | `[deduction]` |
| 6.1 | Explicit poset encoding size does **not** prove a space lower bound | `[deduction]` |

---

## 8. What is not claimed

`[deduction]` The following are **not** established:

- `SORT-BOUND-B ∈ EXPTIME` (open, Proposition 3.4);
- `SORT-BOUND-B ∈ NP` or `coNP` (open, Proposition 4.3);
- `SORT-BOUND-B` hard for any class above `P` (open);
- any unconditional separation (`P ≠ NP`, `EXPTIME ≠ 2-EXPTIME`, etc.);
- any `Ω(n²)` space lower bound or `PSPACE` nonmembership (Observation 6.1);
- optimality of the `2^{O(n log² n)}` DFS bound.

---

## 9. Literature primary sources

- S. R. Mahaney, *Sparse complete sets for NP: Solution of a conjecture of
  Berman and Hartmanis*, J. Comput. System Sci. **25**(2) (1982) 130–143,
  https://doi.org/10.1016/0022-0000(82)90002-2 .
- A. K. Chandra, D. C. Kozen, L. Stockmeyer, *Alternation*, J. ACM **28**(1)
  (1981) 114–133, https://doi.org/10.1145/322234.322243 .
  (`APTIME = PSPACE`, `AEXPTIME = EXPSPACE`.)
- D. J. Kleitman, B. L. Rothschild, *Asymptotic enumeration of partial orders
  on a finite set*, Trans. Amer. Math. Soc. **205** (1975) 205–220,
  https://doi.org/10.1090/s0002-9947-1975-0369090-9 .
  (`log₂ P_n = n²/4 + 3n/2 + O(log n)`.)
- G. Brightwell, P. Winkler, *Counting linear extensions is #P-complete*,
  STOC 1991, https://doi.org/10.1145/103418.103441 .
- R. M. Karp, R. J. Lipton, *Some connections between nonuniform and uniform
  complexity classes*, STOC 1980, 302–309,
  https://doi.org/10.1145/800141.804678 .
- M. Ogiwara, O. Watanabe, *Polynomial-time bounded truth-table reducibility of
  NP sets to sparse sets*, SIAM J. Comput. **20**(3) (1991) 471–483,
  https://doi.org/10.1137/0220030 .
- S. Fortune, *A note on sparse complete sets*, SIAM J. Comput. **8**(3) (1979)
  426–430, https://doi.org/10.1137/0208034 .
- L. Hyafil, R. L. Rivest, *Constructing optimal binary decision trees is
  NP-complete*, Inform. Process. Lett. **5**(1) (1976) 15–17,
  https://doi.org/10.1016/0020-0190(76)90095-8 .
  (Arbitrary tests; does **not** transfer to `S(n)`.)
- E. S. Laber, L. T. Nogueira, *On the hardness of the minimum height decision
  tree problem*, Discrete Appl. Math. **144**(1–2) (2004) 209–212,
  https://doi.org/10.1016/j.dam.2004.06.002 .
  (Arbitrary tests; does **not** transfer.)
- I. Parberry, *On the computational complexity of optimal sorting network
  verification*, LNCS **506** (1991) 252–269.
  (Fixed networks; does **not** transfer.)
- M. Peczarski, *Towards optimal sorting of 16 elements*, Acta Univ. Sapientiae
  Inform. **4**(2) (2012) 215–224, https://real-j.mtak.hu/23036/2/Acta%20Info%202012_4_2.pdf .
- F. Stober, A. Weiß, *Lower bounds for sorting 16, 17, and 18 elements*,
  arXiv:2206.05597 (2022).
- OEIS **A001035** (labelled posets), **A036604** (sorting numbers); indexes, not proofs.

---

## 10. Next obstacle

The central obstruction is the **absence of a compact canonical object** describing
optimal comparison play. The game `G(n,k)` has `2^{O(L_B)}` rounds and branching
factor `2^{O(L_B)}`, giving a game tree of size `2^{2^{O(L_B)}}`. The strongest deterministic bound **established here** is `EXPSPACE`
(via ATM simulation). Whether `SORT-BOUND-B ∈ EXPTIME` is unresolved
**within this project** and would require either a fundamentally new algorithm or a breakthrough in
lower-bound technique. The most informative next experiment is to measure the number
of distinct poset states on *some* height-`S(n)` optimal play for `n = 7…10` and
compare with `n!`, A001035, and `poly(n)`.
