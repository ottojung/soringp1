# Why the information bound is not tight at n = 12

**Status:** research note. Separates literature facts, deductions, experiments
and conjectures. No Lean files, no commits. Exploration front:
"Explain non-tightness of information bounds" (now in `docs/research-plan.md`).

## 1. Precise question

For the adaptive worst-case comparison-sorting number
`S(n) = min { height(T) : T sorts all n! permutations }` and the
information-theoretic lower bound `C(n) = ceil(log2 n!)`, the known exact
values satisfy `S(n) = C(n)` for `n <= 11`, while `S(12) = 30 > C(12) = 29`
(`docs/literature.md`, `docs/research-plan.md`).

**Question.** Is there a *reusable* combinatorial invariant or obstruction,
strictly stronger than the leaf count `n! <= 2^h`, that (a) explains the `+1`
gap at `n = 12`, and (b) predicts *when* such gaps occur?

Sub-questions:
1. What exactly does the primary proof of `S(12) > 29` establish?
2. Is the standard refinement of the leaf count (the "efficiency" pruning of
   Wells / Peczarski / Stober–Weiss) genuinely stronger than leaf counting?
3. Can any scalar function of the current partial order (number of linear
   extensions `e(P)`, efficiency, slack ratio) predict tightness?
4. If not, what is the smallest example where the scalar picture breaks?

## 2. Model and notation (fixed throughout)

- Inputs are `n` distinct labelled keys; comparisons are adaptive; height is
  the worst-case number of comparisons. This is the model of
  `docs/problem.md` and of `SoringP1/Model.lean`.
- A state after `c` comparisons is a partial order `P = (U, <)` on `n`
  labelled elements; `e(P)` is its number of linear extensions. The initial
  state is the antichain `P0` with `e(P0) = n!`.
- Adding a comparison `u < v` gives `P + uv`; the two children of a comparison
  are `P + uv` and `P + vu`, with `e(P+uv) + e(P+vu) = e(P)`.
- `m(P)` is the minimum number of further comparisons that sorts every linear
  extension of `P` (`m(P) = 0` iff `P` is a total order). Then `S(n) = m(P0)`.
  In the repository this is the object `adv` in `SoringP1/Minimax.lean`; the
  context for this note states `S n = adv univ` was just proved (A24). The
  experiments below use an independent Python implementation
  (`scripts/evaluate.py`, `scripts/nontightness_experiments.py`).
- Node-level information bound (**definition/lemma**): if `P` is reached after
  `c` comparisons in a height-`h` tree, then `e(P) <= 2^(h-c)`, i.e. every
  child of an internal node at depth `c` must satisfy
  `e(child) <= 2^(h-c-1)`.

The global bound `S(n) >= C(n)` is exactly the `c = 0` case.

## 3. Sources (primary, with model caveats)

1. **M. Wells**, *Applications of a language for computing in combinatorics*,
   Information Processing 65 (Proc. 1965 IFIP Congress), 497–498, 1966; and
   *Elements of Combinatorial Computing*, Pergamon, Oxford, 1971.
   The original exhaustive-search proof that `S(12) > C(12) = 29`
   (hence `S(12) = 30`, since Ford–Johnson sorts 12 keys in 30 comparisons).
2. **M. Peczarski**, *Towards optimal sorting of 16 elements*, Acta Univ.
   Sapientiae Informatica 4(2), 2012, 215–224,
   <https://real-j.mtak.hu/23036/2/Acta%20Info%202012_4_2.pdf>.
   Introduction credits Wells for `n = 12`; §4 analyses *why* the information
   bound is missed for `n = 13, 14, 15` (the closest published structural
   discussion). This note's PDF text was extracted and audited locally.
3. **F. Stober, A. Weiss**, *Lower Bounds for Sorting 16, 17, and 18 Elements*,
   **ALENEX 2023** (SIAM Symposium on Algorithm Engineering and Experiments),
   pp. 201–213, DOI `10.1137/1.9781611977561.ch17`; preprint
   arXiv:2206.05597v2 (2022). Modern description of the
   Wells–Peczarski search, the "efficiency" pruning, and experiments including
   `n = 12`. `[literature]`
4. **D. E. Knuth**, *TAOCP* Vol. 3, §5.3.1 (merge-insertion; comparison-count
   optimality history).
5. **Ford & Johnson**, *A Tournament Problem*, 1959 (the 30-comparison upper
   bound at `n = 12`).
6. OEIS [A036604](https://oeis.org/A036604) (values) and
   [A003070](https://oeis.org/A003070) (information bound): indexes only.
7. S. Hanamura, S. Iwata, *Posets with seven linear extensions sortable by three
   comparisons*, Information Processing Letters **111**(8) (2011) 365–369,
   doi:10.1016/j.ipl.2011.01.004. **Result (local, tight boundary):** a poset
   with `e(P) = 7` linear extensions *can* be sorted in `⌈log₂ 7⌉ = 3`
   comparisons; this is the tight case immediately below the `e = 8` local
   failure of H3 below. `[literature]`

All sources treat **adaptive, worst-case pairwise comparisons**, not sorting
networks and not average case. Wells' and Peczarski's proofs are exhaustive
computer searches over partial-order states; neither gives a short closed-form
invariant. Hanamura–Iwata is a *poset-sorting* (single-instance) result, not a
statement about the family `S(n)`; it is cited only as the tight local
boundary for the H3 witness.

## 4. What the primary proof actually establishes (audit)

**Literature fact (Wells).** To certify `P0` is *not* sortable in `C`
comparisons it suffices to build the levels

```
S_0 = {P0},
S_c = { heavier child of every admissible comparison (u,v) of some P in S_{c-1} }
```

where a comparison is *admissible at level c* iff both children satisfy
`e(child) <= 2^(C-c)`. If some `S_c = empty`, no height-`C` tree exists: if one
did, the heavier child of its root comparison would be admissible and
sortable in `C-1`, and induction gives `S_c != empty` for all `c` (**deduction**,
a standard argument, reproduced in Peczarski 2012 §3 and Stober–Weiss §3).

- Peczarski 2012 (text extracted from the PDF; the subscript in the first
  quote is ambiguous in OCR): *"Wells reported that for `n = 12` only the set
  `S_24` is empty."* and *"for `n = 12` it is sufficient to check only one
  outcome"*. For `n = 13, 14, 15, 16` one must also inspect the second child
  (Stober–Weiss confirm: for `n = 12` Wells' one-sided exploration already
  empties a level).
- Stober–Weiss Table 2 (n = 12 row): efficiency of a total order
  `E_tot = 12!/2^29 = 0.8922`, efficiency bandwidth `0.05`, full layers
  `C_f = 5`, **`sortable = no`** (i.e. `P0` is not sortable in `C(12)=29`, so
  `S(12) > 29`), about `6190` posets stored during the search, `152 ms` total
  (15 ms forward, 137 ms backward). The relevant column is `sortable = no`;
  the separate remark that for `n = 12` Wells' *one-sided* forward search
  already empties a level (`S_24`) is a statement about Wells' method, not a
  table column. `[literature]`
- `[deduction]` The `0.05` "bandwidth" is a *user-chosen search threshold*
  (`E_thr − E_tot`), not a measured window of bottleneck posets, and the
  `6190` is the number of posets *stored during both searches* — for `n = 12`
  the bidirectional search actually **increased** the space relative to a
  one-sided search. So neither figure localises the obstruction to a small
  set of "bottleneck posets"; they describe the *search effort*. The
  obstruction is certified only by the exhaustive search, not by a compact
  structural object.

**Deduction (the efficiency refinement is not stronger than leaf counting).**
Define efficiency `E(P) = n! / (2^c e(P))` for a poset reached at depth `c`.
Then `e(child) <= 2^(C-c-1)` is equivalent to `E(child) >= n!/2^C = E_tot`.
Thus the "efficiency" condition used as a search heuristic is *definitionally
equivalent* to the node-level information bound. It is a convenient
bookkeeping device and pruning order, **not** a new lower-bound invariant.
Stober–Weiss state exactly this (their Observation 2.2 follows "by the same
argument as the information theoretic lower bound").

**Literature fact (Peczarski 2012 §4) — the obstruction is not scalar.**
For `n = 13`, the backward search leaves a *unique* congruence class of
bottleneck posets `P16` with `e(P16) = 113400`, sortable in 17 comparisons.
Its two alternative predecessors require the children
`Q'16` (`e = 109350`) and `Q''16` (`e = 124740`), and *neither* is sortable in
17 comparisons. Peczarski writes: *"It is quite surprising that the posets
`Q'16`, `Q''16` cannot be sorted. The poset `Q'16` has less linear extensions
than the poset `P16`, which intuitively should make it easier to sort ... The
poset `P16` is sortable in 17 comparisons because of its symmetry."*

So at the level of individual posets, **sortability is not monotone in
`e(P)`**: fewer linear extensions can be *harder*. Any invariant that is a
monotone function of `e(P)` (or of `E(P)`, or of any slack ratio) is therefore
provably insufficient, already for `n = 13`.

## 5. Candidate invariants and hypotheses (with tests)

Notation: `C(n) = ceil(log2 n!)`; the *slack ratio* is `2^C(n)/n!`; the
*allowed split fraction* at a node with remaining budget `r` is
`2^(r-1)/e(P)`, and the split fraction of a comparison is
`max(e(child1), e(child2)) / e(P)`.

### H1 (scalar slack ratio). `S(n) = C(n)` iff `2^C(n)/n!` is large enough.
**Falsified.** Experiment A:

| n | 2^C/n! | S(n) | tight |
|---|---|---|---|
| 5 | 1.0667 | 7 | yes |
| 10 | 1.1558 | 22 | yes |
| 11 | 1.6812 | 26 | yes |
| 12 | 1.1208 | 30 | **no** |
| 20 | 1.8955 | 62 | yes |
| 22 | 1.0503 | 71 | **no** |

`n = 5` has *less* slack than `n = 12` yet is tight; `n = 20` is tight with the
largest slack, `n = 22` fails with the smallest. No function of this ratio
predicts tightness.

### H2 (monotone in `e`). A larger `e(P)` never makes `P` easier.
**Falsified at `n = 6`** (Experiment B). Exhaustive minimax over all `130023`
labelled posets on 6 elements gives `9960` witnessed pairs `e(P1) < e(P2)` but
`m(P1) > m(P2)`. Smallest witness:

- `P1 = (20, 16, 0, 23, 0, 22)`: `e = 13`, `ceil(log2 e) = 4`, `m = 5`, `|Aut| = 1`.
- `P2 = (0, 37, 1, 39, 1, 0)`: `e = 14`, `ceil(log2 e) = 4`, `m = 4`, `|Aut| = 1`.

`P1` has *fewer* extensions and is strictly *harder*. (For `n <= 5` no
violation exists; this is the smallest computational counterexample, and
the same phenomenon is Peczarski's `n = 13` `P16`/`Q'16`.)

**Stronger (and what §8 actually needs): `m` is not even a *function* of `e`.**
`[experiment]` At `n = 5`, among the `360` labelled posets with `e = 8`, exactly
`240` have `m = 3 = ceil(log2 8)` and `120` have `m = 4`. Explicit witnesses:

- `succ = (8, 12, 8, 0, 12)`: `e = 8`, `m = 3` (tight);
- `succ = (26, 0, 10, 0, 8)`: `e = 8`, `m = 4` (loose).

So two posets with the *same* `e` have different `m`; the monotonicity witness
above (`e = 13 < 14`) is strictly weaker. This is the smallest instance of
"same `e`, different `m`", and it is what licenses the §8 conclusion that no
invariant depending only on `e` (or efficiency, or slack) can determine
sortability.

### H3 (local information bound). `m(P) = ceil(log2 e(P))` for every poset.
**Falsified already at `n = 5`** (Experiment B): `120` posets with `e = 8`
and `m = 4`, e.g. `succ = (0, 0, 1, 3, 7)`. So even the *poset-level*
information bound can be off by one. Yet the *global* `S(5) = 7 = C(5)` is
tight. Local non-tightness does not imply global non-tightness. Max local gap
observed is `1` for `n = 5, 6` (**empirical observation**).

`[literature]` The failure is sharp at `e = 8`: Hanamura–Iwata (2011) show
`e = 7` posets *are* sortable in `⌈log₂ 7⌉ = 3` comparisons, so the local
information bound is attained at `e = 7` and first fails at `e = 8`. Our
`n = 5` witness (`e = 8`, `m = 4`) is the smallest instance of that first
failure; no monotone-in-`e` invariant can repair it (see H2).

### H4 (forced balanced prefix). The early comparisons are forced.
**Deduction + Experiment C2.** For target height `h`, a comparison is
admissible only if its heavier child fits `2^(h-c-1)`. Along an all-`1/2`
prefix the allowed fraction is the constant `F = 2^(h-1)/n!`. Computed
achievable split fractions on the shapes `k` disjoint 2-chains + free:

- `n = 11`, `h = 26`, `F = 0.8406`: *every* achievable fraction (up to `5/6`)
  is admissible — maximal slack, consistent with tightness.
- `n = 12`, `h = 29`, `F = 0.5604`: only `1/2` splits are admissible; the
  chain-free split `2/3` (depth 1) and the min–max cross-chain split `5/6`
  are already inadmissible. In particular the *second* comparison is forced to
  pair two free elements. (Same-role comparisons between equal-sized chains,
  also `1/2`, remain admissible, so the later prefix is constrained but not a
  unique shape.)
- `n = 10` (`F = 0.5779`) and `n = 5` (`F = 0.5333`) show the *same* forced
  second comparison, yet both are tight.

So the forced-prefix phenomenon is real but **not sufficient**: it occurs at
tight values too. It cannot by itself predict the `n = 12` gap.

### H5 (efficiency frontier). All bottleneck posets lie in a narrow efficiency
window just above `E_tot`. **Too strong as stated.** What Stober–Weiss support
is an *algorithmic guide*: the bandwidth `0.05` is a *user-chosen search
threshold*, not a measured distribution, and the `6190` stored posets reflect
search effort (the bidirectional search even *increased* the space for
`n = 12`), not a small set of bottleneck posets localising the obstruction. The
efficiency condition at each node is, by Observation 2.2, equivalent to the
information bound. `[literature]` + `[deduction]`

### H6 (symmetry protects tightness). A locally loose poset has trivial
automorphism group. **Falsified at `n = 6`** (Experiment E): among posets with
`e <= 64`, there are `14760` locally loose ones, and `4680` of them have
`|Aut| > 1`. (At `n = 5` the hypothesis happened to hold: all `120` loose
posets had `|Aut| = 1`.) Symmetry is neither necessary nor sufficient.

### H7 (merge / disjoint-union-of-chains family). `[literature]` + `[deduction]` + `[experiment]`

Let `Merge(a, b)` be the disjoint union of an `a`-chain and a `b`-chain; sorting
it is exactly merging two sorted lists, so `e = C(a+b, a)` and
`m(Merge(a,b)) = M(a,b)`, the minimum worst-case merge cost. The elementary
**tape merge** gives `M(a,b) <= a+b-1`, but this is **not** a universal formula:
`M(m,m) = 2m-1` (Graham–Karp; Stockmeyer–Yao 1980) and `M(m,n) = m+n-1` only
for `m <= n <= floor(3m/2)+1` (Stockmeyer–Yao 1980; Murphy–Paull 1979; Christen
1978), extended to `n <= 1.52 m` (Li–Sun–Zhang 2016); for unbalanced sizes
Hwang–Lin (1972) do better (e.g. `M(1,n) = ceil(log2(n+1))`). `[literature]`

Exact minimax on the two-chain posets (verified with `scripts/
nontightness_experiments.py`'s own `add_relation`/minimax, no formula used):

| `(a,b)` | (1,4) | (2,4) | (2,6) | (4,4) | (5,5) | (6,6) |
|---|---|---|---|---|---|---|
| `e = C(a+b,a)` | 5 | 15 | 28 | 70 | 252 | 924 |
| `ceil(log2 e)` | 3 | 4 | 5 | 7 | 8 | 10 |
| `M(a,b)` | 3 | **5** | **6** | 7 | **9** | **11** |
| tight? | yes | **NO** | **NO** | yes | **NO** | **NO** |

So the tempting criterion "decomposable / disjoint-union-of-chains posets are
tight" is **false**, and the mechanism is the exact merge cost `M(a,b)`, which
leaf counting cannot see. The smallest two-chain local violation is
`Merge(2,4)` (`n = 6`): `e = 15`, information bound `4`, but `M(2,4) = 5`
(this value is itself covered by the `m <= n <= floor(3m/2)+1` optimality
theorem). `[experiment]` The **unequal-length** case is precisely where the
tape bound overestimates: `M(2,4) = 5` and `M(2,6) = 6` exceed the information
bound, while the balanced `Merge(4,4)` is still tight. `[deduction]`

## 6. Smallest compelling examples

- **Smallest global gap:** `n = 12`, `S(12) = 30 > C(12) = 29` (Wells).
- **Smallest local failure of the information bound:** `n = 5`,
  `e(P) = 8`, `ceil(log2 8) = 3`, but `m(P) = 4`
  (`succ = (0,0,1,3,7)`), while `S(5) = 7` is still tight.
- **Smallest "more extensions, easier":** `n = 6`, `P2` (`e = 14`, `m = 4`)
  is easier than `P1` (`e = 13`, `m = 5`). This is the minimal computational
  witness that no monotone-in-`e` invariant can work.

## 7. Falsification attempts (concrete, with outcomes)

1. **H1 ratio threshold** — falsified by `n = 5` (tight with smaller ratio
   than `n = 12`) and by the `n = 20`/`n = 22` inversion.
2. **H2 monotone-in-`e`** — falsified at `n = 6` (9960 witnesses).
3. **H3 local tightness** — falsified at `n = 5` (120 posets).
4. **H4 forced prefix as predictor** — falsified: the same forced prefix
   occurs at `n = 5, 10` (tight) and `n = 12` (not).
5. **H6 symmetry** — falsified at `n = 6` (4680 loose posets with nontrivial
   automorphisms).
6. **Direct forward-search reproduction of `S(12) > 29`** — attempted
   (Experiment D). The one-sided admissible forward search reproduces the
   expected behaviour for `n = 5, 6, 7` at `C = C(n)` (no empty level; peak
   `S_7 = 54334` for `n = 7`) and dies at level 1 for `C = C(n)-1` (the global
   information bound). It could **not** be pushed to `n = 12` in pure Python
   (state explosion; the `n = 12` level sets exceed our time cap within the
   first few levels). The `n = 12` non-sortability is therefore taken from the
   literature, not reproduced here.

## 8. What was learned

- The information bound is a **node-level** necessary condition, and the
  classical "efficiency" refinement is *equivalent* to it. There is no
  well-known scalar strengthening.
- The obstruction is genuinely **structural / global**. Peczarski's `n = 13`
  `P16`/`Q'16` example and our `n = 6` witness both show that sortability is
  not monotone in `e(P)`. Hence **no invariant that is a function only of the
  number of linear extensions** (or efficiency, or slack) can explain the gap.
- Local failures of the information bound appear very early (`n = 5`) and do
  **not** imply a global gap; the global gap first appears at `n = 12`. So an
  explanation must be *strategic*: it must track how a whole tree routes all
  `n!` permutations, not a single poset.
- The `n = 12` obstruction is certified only by exhaustive search
  (`sortable = no` in Stober–Weiss Table 2); it is **not** localised to a small
  set of "bottleneck posets" — the `6190` stored posets are search effort
  (the bidirectional search increased the space), and the `0.05` bandwidth is a
  chosen threshold, not a measured window. The forced balanced prefix is the
  visible *local* signature; the actual death of the search happens deeper, in
  a finite case analysis whose bottleneck posets are not published.
- Symmetry (large `|Aut|`) is neither necessary nor sufficient for local
  tightness, despite Peczarski's remark that `P16` is sortable "because of its
  symmetry".

## 9. Next unresolved obstacle

- **A human-readable certificate.** No short closed-form invariant or proof of
  `S(12) > 29` is known; Wells' and all later proofs are exhaustive poset
  searches. Producing a compact, checkable certificate (or a genuinely new
  lower-bound technique) remains open and is the natural target.
- **Global vs local gap.** We lack a theorem relating local information-bound
  failures to the first global gap. Conjecture to test: the first global gap
  occurs when the antichain cannot be routed through the efficiency frontier
  for `h = C(n)` — a statement currently equivalent to the search itself.
- **Reproduction scale.** Our evaluator cannot reach `n = 12`; a congruence-
  quotiented forward search (canonical labelling of posets) would be needed to
  reproduce Wells' result in-repo.
- **Max local gap.** Observed gap `= 1` for `n <= 6`; whether the poset-level
  information bound can be off by more than 1, and for which `n`, is open here.

## 10. Honest novelty assessment

- **Not new:** the value `S(12) = 30` and the fact of non-tightness (Wells
  1966/1971); the search method and the efficiency pruning (Wells, Peczarski,
  Stober–Weiss); the observation that sortability is not monotone in `e(P)`
  (Peczarski 2012 §4, at `n = 13`).
- **Minor original contributions of this note:** (i) the explicit
  *equivalence* of the efficiency pruning with node-level leaf counting,
  framed as a no-go for scalar invariants; (ii) the smallest computational
  witnesses — local information-bound failure at `n = 5` (`e = 8`, `m = 4`)
  and non-monotonicity at `n = 6` (`e = 13` harder than `e = 14`); (iii) the
  falsification of five natural candidate invariants, including the
  symmetry hypothesis; (iv) the observation that the forced balanced prefix
  occurs at tight values (`n = 5, 10`) and therefore is not a predictor.
- **Bottom line:** there is **no known reusable combinatorial invariant**
  stronger than leaf counting that explains the `+1` gap. The obstruction is
  structural and, in the literature, is established only by exhaustive search.
  A new unifying invariant remains an open problem; this note provides
  evidence that it must be non-scalar and strategic.

## 11. Reproducing the experiments

```
python3 scripts/evaluate.py 7                       # S(7)=13
python3 scripts/nontightness_experiments.py --experiment A
python3 scripts/nontightness_experiments.py --experiment B --n 6     # ~15 min
python3 scripts/nontightness_experiments.py --experiment C2
python3 scripts/nontightness_experiments.py --experiment D --n 7 --height 13
python3 scripts/nontightness_experiments.py --experiment E --n 6 --emax 64
```

The H2 same-`e` witness and the H7 merge family use the same engine as
Experiment B (`add_relation` + memoised `minimax` from
`scripts/nontightness_experiments.py`). The same-`e` pair verifies as
`e = 8, m = 3` versus `e = 8, m = 4`; each `Merge(a,b)` is built with
`add_relation` along its two chains and read with the same memoised `m`, giving
the H7 table.

Experiment B enumerates all labelled posets (19, 219, 4231, 130023 for
`n = 3..6`); Experiment E's automorphism test is brute force over `n!`
permutations and is restricted by `--emax`. No experiment here is a proof of a
complexity-class statement; all values for `n >= 8` are literature facts.
