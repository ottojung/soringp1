# A small retrograde (backward) DP for exact sorting numbers: toy validation on n ≤ 4

**Status:** research note + finite experiment. This is **not** Lean, **not** a
complexity-class result, and **not** a proof of any asymptotic statement. Every
claim below is labelled `[definition]`, `[literature]`, `[deduction]`,
`[experiment]`, `[conjecture]` or `[open]`.

Companion program: `scripts/retrograde_toy.py`.
Regression test: `tests/test_retrograde_toy.py` (runs in ≈0.05 s).

**Primary source:** F. Stober and A. Weiß, *Lower Bounds for Sorting 16, 17, and
18 Elements*, **ALENEX 2023**, pp. 201–213, DOI `10.1137/1.9781611977561.ch17`,
arXiv:2206.05597. The relevant parts are §4.1 (Lemma 4.1), §4.2 (Lemma 4.2) and
§5.7 (Lemma 5.1, Lemma 5.2, Corollary 5.1). The venue correction to ALENEX 2023
(not SEA) is already recorded in `docs/research-obstruction-next.md` §1.1.

## 0. Model and notation

`[definition]` From `docs/problem.md`. `S(n)` is the minimum height of a
deterministic **adaptive** binary comparison decision tree that sorts every
permutation of `n` distinct labelled keys, in the worst case. A state is a
transitively closed strict partial order `P` on the labelled keys `{0,…,n−1}`.
A legal move compares an **incomparable** pair `{i,j}` and, by the two possible
answers, produces the children `P+i<j` and `P+j<i` (transitive closure). Write

- `P0` for the antichain, `F(P)` for the minimum number of further worst-case
  comparisons that suffices to finish sorting from `P` (so `F(P)=0` iff `P` is a
  chain, and `F(P0)=S(n)`);
- `CanSort(P,d)` for the predicate `F(P) ≤ d`.

Posets are represented as tuples of successor bitmasks, exactly as in
`scripts/state_compression.py` and `scripts/budgeted_dfs.py`.

## 1. The backward layer recurrence

`[definition]` Define the *winning layers*

```
W_0 = { P : P is a chain }
W_d = W_{d-1} ∪ { P : there is a legal comparison whose BOTH children lie in W_{d-1} }.
```

`[deduction]` `W_d = { P : CanSort(P,d) } = { P : F(P) ≤ d }`.

*Proof.* By induction on `d`. For `d=0` both sides are the chains. For `d>0`:
`CanSort(P,d)` holds iff `P` is a chain or some comparison has both children
`CanSort(·, d−1)`; by induction the children condition is "both children in
`W_{d-1}`", giving exactly the definition of `W_d`. ∎

`[deduction]` Hence `S(n)` is the least `d` with `P0 ∈ W_d`, and more generally
`F(P) = min { d : P ∈ W_d }`.

`[experiment]` The program evaluates these layers **bottom-up from the chains**
over the inverted transition graph. Concretely: every legal move of every state
gets a counter initialised to `2`; when a child enters a layer, the counters of
all moves having that child are decremented; a move whose counter reaches `0`
certifies its owner one layer later. One sweep assigns `F(P)` to every state.
This is a *genuine layer-wise backward evaluation*: it never calls the forward
recursion `CanSort`, and it certifies a state by the existence of a comparison
whose two outcomes were certified at budget `−1` (the layer below).

`[deduction]` The forward recursion

```
CanSort(P,d) = (P chain)  if d = 0
             = ∃ legal {i,j}: CanSort(P+i<j,d−1) ∧ CanSort(P+j<i,d−1)   otherwise
```

is implemented **separately** in `make_forward_oracle` and used only as an
independent cross-check. It shares the poset encoding but not the layer
machinery; it is not the algorithm under test.

## 2. What this toy is *not*: the source's predecessor enumeration

`[literature]` The source performs a **backward search** (§4.1): it starts from a
total order (level `C`, sortable in `0` remaining comparisons) and enumerates
predecessors level by level. Its predecessor generation (§5.7) iterates over the
edges of the Hasse diagram of the current poset `P` and calls
`enumeratePredecessors` to list the posets `P'` with `P = P'+u v`. Lemma 5.2 and
Corollary 5.1 characterise that set exactly, and §4.1 states the key subtlety:

> even for one specific comparison `(u,v)` there might be **multiple** potential
> predecessors `P'` such that `P = P'+u v`. Indeed, each combination of
> transitive edges that would be implied by the comparison is a valid option.

`[experiment]` Our toy deliberately does **not** implement that Hasse-edge
enumeration. Instead it:

1. enumerates *all* labelled posets on `n` elements offline by exhaustive
   3-state relation generation (each unordered pair is `<`, `>` or
   incomparable; keep the transitive assignments), obtaining exactly
   `A001035(n)` states;
2. builds *every* legal forward comparison transition and **inverts** the finite
   graph.

This is an honest **offline all-poset graph construction**, valid only because
the state space is tiny (`A001035(4) = 219`). It is not the source's scalable
method and does not claim to be.

`[experiment]` The multiple-predecessor subtlety is nonetheless *present and
handled* in the inverted graph: `pred[c]` lists every move id whose child is
`c`, and several moves from different owners may share the same comparison pair.
The test `test_one_comparison_can_have_two_predecessors` asserts `≥ 2`, and the
concrete `n = 3` witness is: the chain `0<1<2` is obtained by comparing `(1,2)`
from **two** predecessors, `{0<1}` and `{0<1, 0<2}`. On `n = 4` the program
prints, e.g., the child `succ=(12,0,8,0)` reached by comparison `(0,2)` from
`(0,0,8,0)` and from `(8,0,8,0)`. This is exactly why inverting a single Hasse
edge is insufficient and why the source needs Lemma 5.1/5.2.

`[deduction]` **Storage.** The reverse graph and counters cost
`O(#states · n²)` (≤ `binom(n,2)` moves per state), with `#states = A001035(n) =
1, 1, 3, 19, 219, 4231, …`. `A001035(n)` grows like `2^{n²/4 + o(n²)}`, so this
is **not polynomial space**. The source reduces the state count by congruence
classes, efficiency pruning, hashing and disk storage (§5.1–5.5); the toy does
none of that. No speedup or space improvement over forward search is claimed
here — the source itself reports that for `n = 12` the bidirectional search
*increased* the explored space (their Table 2, footnote ‡).

## 3. Results on n ≤ 4

`[experiment]` Exhaustive 3-state generation reproduces the labelled-poset
counts and the known sorting numbers, and the comparison-reachable set from the
antichain equals the enumerated set (so the "219 states" fixture is correct):

| n | states `A001035(n)` | moves | `S(n)` retrograde | `S(n)` known |
|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 2 | 3 | 1 | 1 | 1 |
| 3 | 19 | 21 | 3 | 3 |
| 4 | 219 | 522 | 5 | 5 |

`[experiment]` **Cross-check.** For *every* poset on `n ≤ 4` and *every*
`d ≤ 5` (1458 `(poset, d)` pairs), the backward layer membership
`F(P) ≤ d` agrees with the independent forward `CanSort(P,d)`. This is the
validation required by the task; it is a finite identity on 243 states.

`[experiment]` **Backward certificate for the `n = 4` antichain at depth
`S(4) = 5`.** The program emits a nested certificate whose root is
`P0 = (0,0,0,0)` with `F = 5`. Its first step is:

```
root succ=(0, 0, 0, 0) F=5   compare (0,1)
  child 0<1: succ=(2,0,0,0) F=4
  child 1<0: succ=(0,1,0,0) F=4
```

Each internal node stores a comparison and references to its two children, and
recurses until chains (`F = 0`). `check_certificate` verifies that every stored
comparison really produces the referenced children and that
`F(parent) = 1 + max(F(children))`; the certificate height is exactly `5`. Thus
the certificate is a complete depth-5 sorting decision tree for `n = 4`,
extracted purely from the backward layers.

## 4. Efficiency-threshold partial completeness (literature only)

`[literature]` The source's §4.2 introduces the *partial backward search*: with a
user threshold `E_thr ∈ [E_tot, 2·E_tot)`, only posets with efficiency
`E(P) = n! / (2^c · e(P))` below the threshold are stored in the lower layers.
Its **Lemma 4.2** states: for a poset `P` obtained by the forward search in `c`
comparisons and sortable in at most `C−c` comparisons,

1. if `c ≥ C_f` then `P ∈ ⋃_{d≥c} B'_d`;
2. if `E(P) ≤ E_thr` then `P ∈ B'_c`.

`[deduction]` The completeness guarantee is **conditional on those hypotheses**.
Absence of a poset from a thresholded backward result does **not** mean it is
unsortable; it may simply have `E(P) > E_thr` or have been pruned. We therefore
do **not** use any absent-implies-`NO` reasoning.

`[experiment]` We did **not** implement the thresholded partial backward search.
The sweep reported in §3 is the *exact, unthresholded* full layer computation
over all `n ≤ 4` states, which is complete for that range; consequently no
threshold-absence question arises in the results above. The threshold variant is
reported here as literature coverage only, not as a verified implementation.

## 5. Scope, evidence labels, limitations

- `[experiment]` All numbers above are exact finite computations on `n ≤ 4`.
  They recompute known literature values (`S(4)=5`) and validate the backward
  algorithm against a forward oracle; they are not new values and prove nothing
  about larger `n`.
- `[deduction]` No asymptotic, `P`/`NP`/`EXPTIME`, or separation claim is made or
  implied. The state space is explicitly non-polynomial (§2).
- `[open]` Whether the reverse-edge/layer machinery can be made competitive with
  the source's bidirectional search at larger `n` is not addressed; the toy
  only isolates the *backward layer evaluation* as a distinct, testable object.
- The forward oracle is the standard memoized minimax recursion; it is a
  reference, not a contribution.

### Reproduction

```
python3 scripts/retrograde_toy.py            # tables + n=4 certificate
python3 -m unittest tests.test_retrograde_toy -v
```

## References

- F. Stober, A. Weiß. *Lower Bounds for Sorting 16, 17, and 18 Elements.*
  ALENEX 2023, 201–213. arXiv:2206.05597. §4.1, §4.2, §5.7.
- M. Peczarski. *Towards optimal sorting of 16 elements.* Acta Univ. Sapientiae
  Informatica 4(2), 2012, 215–224.
- OEIS A001035 (number of labelled partial orders), A036604 (sorting numbers).
