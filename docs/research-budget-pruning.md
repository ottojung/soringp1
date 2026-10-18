# Sound pruning and move reduction for the exact budgeted sorting DFS

**Status:** research note (paper analysis + small experiment). **Not Lean-checked.**
Every item is labelled `[definition]`, `[literature]`, `[deduction]`,
`[experiment]`, `[conjecture]` or `[open]`. Companion program:
`scripts/budgeted_pruning_experiments.py`; tests: `tests/test_budget_pruning.py`.
The reference `scripts/budgeted_dfs.py` is **not** modified; its `can_sort` /
`compute_s_dfs` are re-implemented verbatim in the experiment as
`can_sort_reference` and cross-checked against every pruned variant on each run.

**Coordination:** this note was produced alongside the lower-bounds agent
(coordination note 510a18001004), which owns the mathematical construction of
safe pruning from certified bounds (`P ⊆ Q ⟹ F(P) ≥ F(Q)`). This note owns only
the implementation and benchmarks. The `e(P) > 2^d` information cutoff and the
Hanamura–Iwata `e ≤ 7` base were agreed as the first safe baselines.

---

## 1. Model and notation `[definition]`

From `docs/problem.md`, `docs/upper-bound.md`, `docs/research-budgeted-dfs.md`:

* `n` distinct labelled keys; a state is the transitively closed poset `P`
  induced by the comparisons made so far (successor bitmasks: bit `j` of
  `succ[i]` iff `i < j`).
* `S(n)` = minimum worst-case number of adaptive pairwise comparisons to sort.
* Game `G(n,k)`: sorter picks an incomparable pair, adversary answers, `P`
  becomes its transitive closure. `S(n) ≤ k` iff the sorter wins `G(n,k)`.
* `CanSort(P, d)` = the sorter can force a total order from `P` within `d`
  comparisons. `CanSort(P, d) = True` **iff** `F(P) ≤ d`, where `F` is the exact
  minimax value (`adv univ`, A24) and `S(n) = F(∅)`.
* `e(P)` = number of linear extensions of `P`; `F(total) = 0`;
  `F(P) = 1 + min_{x‖y} max(F(P+x<y), F(P+y<x))`.

## 2. The precise question `[definition]`

The budgeted DFS decides `S(n) ≤ k` by binary search over `k`, calling
`CanSort(∅, k)`. Its worst-case cost is `2^{O(n log² n)}`
(`docs/research-budgeted-dfs.md`), and it is **polynomial space** (only the
recursion stack is kept). The question:

> Which **provably sound** pruning rules and move reductions lower the number
> of `CanSort` calls — ideally without losing the polynomial-space guarantee —
> and what is their measured effect at small `n`? Does any of them improve the
> **asymptotic worst-case exponent**?

The optimizations below are each justified independently. The headline
**experimental** answer is a large *decision-version* speedup with a clean
structural explanation; the **asymptotic** answer is *negative* (no exponent
improvement), and the boundary where the speedup stops working is exactly the
known `n = 12` information-bound obstruction (§7).

## 3. Space complexity (flagged up front) `[deduction]`

The coordination note requires that the pruning prototype's *actual* space cost
be distinguished from the baseline's polynomial space.

| method | space | preserves poly-space? |
|---|---|---|
| reference `can_sort` (baseline) | `O(d · n²)` bits (stack only) | yes |
| `ext='enum'` (`e_exceeds`, capped DFS enumeration) | `O(n²)` bits (ideal stack + counter) | **yes** |
| `ext='width'` (`width!` surrogate) | `O(n)` (subset scan) | yes |
| `ext='exact'` (`linear_extensions`, subset/downset DP) | `O(2^n)` ideal counts (lru_cache) | **no** |
| `hi_base` (`e_at_most(P, 7)`, enumerate ≤ 8) | `O(n²)` bits | **yes** |
| `orbits` (`Aut(P)`, `O(n!)` per node) | `O(n² · n!)` transient | yes, but time-heavy |

`[deduction]` `e_exceeds(succ, n, cap)` decides `e(P) > cap` by a depth-first
enumeration of linear extensions that stops at `cap+1` of them. It keeps only the
order-ideal stack (depth `n`, `O(n)` per frame) and a counter, so it is
polynomial space and never builds a `2^n` table. Because every order-ideal prefix
extends to at least one full linear extension, there are no dead ends, so the
search visits `O(min(e, cap+1) · n)` nodes. `ext='exact'` is kept **only** as a
fast cross-check; it is not the recommended method. `[experiment]` `e_exceeds`
agrees with the exact subset-DP `linear_extensions` on every poset with `n ≤ 5`
and for every cap that arises (`cap = 2^d`, `d ≤ U(n)`) and `cap = 7`
(`--verify`, 0 failures).

## 4. Optimization 1 — extension-count cutoff `[deduction]` + `[literature]`

**Necessary condition (information bound, poset level).** For any poset `P` and
budget `d`,

> `F(P) ≤ d`  implies  `e(P) ≤ 2^d`.

`[deduction]` *Proof.* A decision tree of height `d` has at most `2^d` leaves.
From state `P` the sorter must still distinguish every linear extension of `P`:
two distinct extensions `x ≠ y` of `P` are distinct possible inputs consistent
with `P`, and a correct tree sends them to different leaves with different
outputs. Hence `#extensions = e(P) ≤ #leaves ≤ 2^d`. ∎

**Contrapositive (the prune).** `e(P) > 2^d` implies `F(P) > d`, so
`CanSort(P, d) = False` and the node may be pruned. This is the special case
`Q = P` of the lower-bounds agent's monotonicity pruning (`P ⊆ Q ⟹ F(P) ≥ F(Q)`)
using the certified lower bound `ceil(log2 e(P)) ≤ F(P)`. It is applied **only**
to return `False` early (never to manufacture a `True`), so it cannot change a
correct answer into an incorrect one.

**Computing the predicate in poly-space.** The prune needs only the *decision*
`e(P) > 2^d`, decided by `e_exceeds(P, n, 2^d)` (§3). `[experiment]` This is
**exactly as strong** as the exact subset-DP: `ext='enum'` and `ext='exact'`
give identical call counts at every `n ≤ 5` (both decide `e > 2^d` identically),
but `ext='enum'` is poly-space while `ext='exact'` is `O(2^n)` space.

**Cheap surrogate `width(P)!` (strictly weaker, not new).** `[experiment]`
`e(P) ≥ width(P)!` holds for every poset with `n ≤ 5` (verified exhaustively;
`--verify` 0 failures). It is a *weaker* lower bound than `e(P)` (the exact
`ceil(log2 e)`), so it prunes a subset of the nodes the exact cutoff prunes —
it reproduces a weaker bound, it is not a new result. It is included only to
measure how much of the benefit the cheap version captures. `[experiment]` At
`n = 5` the binary search drops to `48,138` calls with `ext='width'` vs `750`
with `ext='enum'`, confirming `width!` is strictly weaker here.

## 5. Optimization 2 — Hanamura–Iwata base `[literature]` + `[deduction]`

`[literature]` S. Hanamura, S. Iwata, *Posets with seven linear extensions
sortable by three comparisons*, Information Processing Letters 111(8):365–369,
2011, doi:10.1016/j.ipl.2011.01.004. Every poset with `e(P) ≤ 7` linear
extensions is sortable by `⌈log2 7⌉ = 3` comparisons, i.e. `F(P) ≤ 3`.

**Acceptance shortcut `[deduction]`.** `CanSort(P, d) = True` whenever `d ≥ 3`
and `e(P) ≤ 7`. This returns `True` early (an acceptance, not a prune), so it
is sound. The predicate `e(P) ≤ 7` is decided in polynomial time **and space**
by `e_at_most(P, 7)` (enumerate at most 8 extensions; §3) — no `2^n` table is
needed. `[experiment]` Verified: for every poset with `n ≤ 5` and `e(P) ≤ 7`,
the reference `CanSort(P, d)` is `True` for all `d ≥ 3` (the shortcut never
lies). `[experiment]` Used alone it barely helps `S(5)` (`258,587` calls) because
the hard `d = 7` search starts at `e = 120 > 7`; combined with the cutoff it is
the best configuration (`ext=enum+hi_base`, `396` calls).

## 6. Optimization 3 — automorphism move orbits `[deduction]`

For `φ ∈ Aut(P)`, the map `P → P` is an isomorphism, so the two children of
`{i,j}` and of `{φi, φj}` have equal `F`; hence the decision predicate
"both children win within `d−1`" is invariant on `Aut(P)`-orbits of incomparable
pairs (this is Theorem 5 of `docs/research-compression-next.md`). The
existential (OR) may range over **one representative per orbit** only. **Both**
adversary outcomes of the chosen representative are still explored — the reverse
branch is never dropped (cf. the `n = 3` dual-branch falsification of
`docs/research-compression-next.md` §6a). `[experiment]` Verified: `orbits`
returns the same decision as the reference on every tested `(P, d)`.
`[experiment]` It reduces calls further (`750 → 553` on the `n = 5` antichain at
`d = 7`) but **increases wall-clock** (`0.014s → 0.029s`) because `Aut(P)` is
`O(n!)` per node — a recorded slowdown, not a free win.

## 7. Optimization 4 — ordinal-sum allocation `[deduction]` (negative result)

`[definition]` An ordinal sum `A (+) B` has every element of `A` below every
element of `B`. `[deduction]` **Additivity.** `F(A (+) B) = F(A) + F(B)`: all
cross pairs are already comparable, so every legal comparison is internal to one
block and the two blocks are independent subproblems (standard; see
`docs/research-series-decomposition.md` §2). `[experiment]` Verified for every
poset with `n ≤ 5`: `F_value(P, use_ordinal_sum=True) == memoized_F(P)`, and the
blocks form a genuine ordinal sum.

**Negative result `[experiment]`.** Allocation is *exact* but does **not** reduce
the no-memoization DFS call count at `n ≤ 5` — it can even increase it (e.g. the
`n = 5` ordinal sum `(0,29,0,1,0)`: plain `1179` calls vs allocated `1753`).
Reason: without a memoization table the two component searches re-explore shared
substates, while the direct search on the full poset benefits from its own
short-circuits. The antichain root used for `S(n)` is series-prime, so
allocation does not apply there at all. Its value is as an exact-value identity
and a potential accelerator **only when combined with memoization** (a separate
axis, already covered by `scripts/evaluate.py`). This is recorded as a
conditional/negative result, not a speedup.

## 8. Experiments `[experiment]`

`python3 scripts/budgeted_pruning_experiments.py` (deterministic; one run).
Call counts are `CanSort` invocations; times are wall-clock. All pruned variants
return the **same** decision as the reference (checked per row, "OK").

**Binary search for `S(n)`** (`value, calls, seconds`):

| n | S(n) | reference | ext=width | ext=enum | ext=exact | hi_base | ext=enum+hi_base | ext=enum+orbits |
|---|---|---|---|---|---|---|---|---|
| 3 | 3 | 27, 0.000 | 27 | 13 | 13 | 17 | 3 | 13 |
| 4 | 5 | 793, 0.002 | 127 | 109 | 109 | 745 | 61 | 109 |
| 5 | 7 | **261,662, 0.657** | 48,138 | **750** | 750 | 258,587 | **396** | 556 |

At `n = 5` the poly-space cutoff `ext='enum'` cuts the binary-search calls
`261,662 → 750` (**349×**) and wall-clock `0.657s → 0.015s` (**44×**);
`ext='enum'+hi_base` reaches `396` calls (**661×**). `ext='width'` is weaker
(`48,138`), confirming §4.

**Adversarial posets (worst case per `(P,d)`, near the `F` boundary):**

| poset | F | d | reference | ext=enum | ext=enum+hi_base | ext=enum+orbits |
|---|---|---|---|---|---|---|
| n=5 antichain | 7 | 6 (False) | 125,407 | **1** | **1** | **1** |
| n=5 antichain | 7 | 7 (True) | 107,659 | 747 | **393** | 553 (0.029s, slower) |
| n=4 antichain | 5 | 4 (False) | 645 | **1** | **1** | **1** |
| n=5 2-chains | 4 | 3 (False) | 149 | **1** | **1** | **1** |

**Important cost distinction.** One top-level DFS call does *not* mean constant computational time: the capped extension-counting subroutine may enumerate `2^d+1` permutations, taking `2^{O(d)}·poly(n)` time and polynomial space. The tables count `CanSort` invocations and report wall-clock separately. Capping does not establish an asymptotic improvement over the previously proved `2^{O(n log² n)}` time bound.

**Important cost distinction.** One top-level DFS call does *not* mean constant computational time: capped extension enumeration can visit as many as `2^d+1` permutations, taking up to `2^{O(d)}·poly(n)` time while using polynomial space. These tables count `CanSort` invocations; wall-clock cost is reported separately. The optimization does not establish an asymptotically better worst-case upper bound than `2^{O(n log² n)}`.

**Interpretation `[deduction]`.** The cutoff makes every *False* probe whose
budget is below the root information bound uses **one top-level `CanSort` call**: at the root
`e = n!`, so `CanSort(∅, d) = False` is decided the moment `n! > 2^d`, i.e.
`d < ⌈log2 n!⌉`. The binary search's `False` probes are exactly those with
`d < S(n) ≤ ⌈log2 n!⌉ + gap`; whenever the information bound is tight at the
root (`S(n) = ⌈log2 n!⌉`, true for `n ≤ 11` per `docs/literature.md`), every
`False` probe collapses to one call. Only the single *True* probe at `d = S(n)`
requires real search, and `hi_base` shaves that. This is a large
**decision-version** speedup, not an asymptotic one (§9).

## 9. Asymptotic status — no exponent improvement `[deduction]` + `[open]`

**No asymptotic exponent improvement is claimed.** The pruning changes the
*constant and the False-side* of the decision search, not the worst-case
exponent:

* The worst case of `CanSort` is a *True* probe at `d = S(n)`, or any instance
  with `e(P) ≤ 2^d` but `F(P) > d`. The extension cutoff does not touch these
  (it only fires when `e(P) > 2^d`), so the worst-case node count is unchanged.
* The poly-space property is preserved by `ext='enum'` / `hi_base` / `orbits`, so
  the space bound is not regressed — but no new asymptotic space claim is made.

**The cutoff is strong exactly where the information bound is tight, and weak
exactly at the known obstruction `[deduction]`.** For `n ≤ 11`,
`S(n) = ⌈log2 n!⌉`, so the root `False` probe (`d = S(n)−1`) satisfies
`n! > 2^{S(n)−1}` and is pruned instantly. At `n = 12`, `S(12) = 30` but
`⌈log2 12!⌉ = 29` and `12! ≈ 2^{28.83} < 2^{29}`, so the root `False` probe at
`d = 29` has `e = 12! ≤ 2^{29}` and the cutoff **does not fire** — the search
must run. The `n = 12` gap (`S(12) = 30 > 29`) is therefore the canonical case
where this pruning stops helping, which is precisely the structural obstruction
tracked in `docs/research-n12-nontightness.md` and `docs/exploration-agenda.md`.
`[open]` Whether the *True*-search exponent `2^{O(n log² n)}` can be reduced
remains open; these prunings do not reduce it.

## 10. What was learned, failed ideas, next hypotheses

**Learned `[experiment]`.**
1. The poset-level information cutoff `e(P) > 2^d` is a **sound, poly-space**
   prune that collapses every information-bound-refuted `False` probe to one top-level DFS call (not constant runtime),
   giving a **349×** call and **44×** wall-clock reduction for `S(5)`, and is
   exactly as strong as the exact subset-DP.
2. `width(P)!` is a valid but **strictly weaker** surrogate (not a new bound).
3. The Hanamura–Iwata `e ≤ 7` base is a sound poly-space **acceptance** that
   helps most in combination with the cutoff.
4. Automorphism move orbits (both outcomes retained) are sound and cut calls
   further but **slow wall-clock** at `n = 5` due to `O(n!)` automorphism
   computation.

**Negative / conditional results `[experiment]`.**
* Ordinal-sum allocation is exact but does **not** reduce no-memoization DFS
  calls at `n ≤ 5`; it needs memoization to pay off (separate axis).
* `orbits` trades calls for wall-clock (recorded slowdown).
* No asymptotic exponent improvement; the `n = 12` gap is where the cutoff fails.

**Next hypotheses `[open]`.**
1. A canonical-labelling orbit computation (nauty-style) could remove the
   `O(n!)` bottleneck and make `orbits` a net wall-clock win (`docs/research-compression-next.md`
   §8).
2. A lower bound *stronger than* `ceil(log2 e)` that is still poly-time
   computable would prune the `e ≤ 2^d < F` region the cutoff misses; the local
   gap `m(P) − ⌈log2 e(P)⌉` is the candidate invariant (`docs/research-obstruction-next.md`).
3. Bidirectional search on `S_n × Z_2` classes with orbit-reduced moves
   (Stober–Weiss) combined with the cutoff, targeting the `n = 12` gap.

## 11. Provenance and non-overlap

* Primary sources: Hanamura–Iwata doi:10.1016/j.ipl.2011.01.004; the
  information-bound argument is standard decision-tree leaf counting; the
  orbit-invariance theorem is `docs/research-compression-next.md` Theorem 5;
  ordinal-sum additivity is `docs/research-series-decomposition.md` §2.
* The extension-cutoff construction and the `e ≤ 7` base were coordinated with
  the lower-bounds agent (510a18001004), which owns the mathematics; this note
  owns implementation and benchmarks only.
* No Lean file is added or modified; the kernel-checked model is untouched. The
  reference `scripts/budgeted_dfs.py` is byte-for-byte unchanged.
* This document and `scripts/budgeted_pruning_experiments.py` /
  `tests/test_budget_pruning.py` are the only artifacts of this task.

## 12. Reproduce

```
python3 scripts/budgeted_pruning_experiments.py --verify     # exhaustive soundness (0 failures)
python3 scripts/budgeted_pruning_experiments.py              # full benchmark + adversarial + ordinal-sum
python3 -m unittest tests.test_budget_pruning -v             # 9 regression tests
python3 -m unittest discover -s tests -v                      # full CI suite (41 tests)
```

`--verify` checks, exhaustively for `n ≤ 5`: exactness of `e`; `e_exceeds`
against exact `e` for all arising caps and `cap = 7`; `e ≥ width!`;
ordinal-sum additivity; and decision equivalence of every pruned variant vs the
reference (exhaustive `n ≤ 4`, structured `n = 5`). Result: **0 failures**.
