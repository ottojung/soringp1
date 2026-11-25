# antonina-PXDAUb6dYfEV3JBACSIyoH-annette

Session: ses_e49a3ea52ffeAnZ2psrKecHLuD
Workspace: /home/lubko/soring-fronts/exec-interval-reversal-quotient-20261107
Created: 1794060850653; updated: 1794061575380

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 299 (msg_1b6661d6a0013syh3M6LW1wt4T)

## Result

**Yes, the interval-module reversal quotient is an exact quotient, and it is transition-compatible. No, it is not an asymptotic improvement: the measured gain is a finite constant factor.**

All work is in the untracked script `scripts/interval_reversal_quotient.py`; no tracked file was modified, nothing was committed or posted.

## 1. Canonical form and soundness

The implementation uses only the two generators:

- relabelling of the `n` keys;
- reversal of every interval module `S` of `P`, including `S = V` (the order dual).

On isomorphism classes, the orbit is computed as the connected component of the Schreier graph with an edge

```
c  --  canon(reverse_S(c))
```

for every interval module `S` of every iso-class representative `c`. The canonical form is the lexicographically least iso representative in the orbit.

**Soundness.**
- Relabelling is an order isomorphism, so it preserves `F`.
- Interval reversal preserves `F` by Theorem 3 of `docs/research-orientation-modules.md`.
- Therefore every word in the generated group preserves `F`, so `F` is constant on each produced orbit.
- No orbit pruning is used: all nonempty interval modules are enumerated, including `S = V`. The only excluded subset is `S = 0`, whose reversal is the identity.
- Completeness of the Schreier graph follows because relabelling conjugates interval modules and commutes with interval reversal; generators at a non-representative member are images of generators at the representative.
- The exact DP is sound because it memoises by the canonical form `C` and replaces each successor `Q` by `C(Q)`; since `F(Q) = F(C(Q))`, the minimax recurrence is unchanged. The DP still iterates over all incomparable pairs of the stored representative, so it does not need an unproved transition rule.

As an independent implementation check, a brute-force orbit BFS over all *labelled* posets (relabelling plus all interval reversals) gives orbit counts `4, 11, 34` for `n = 3,4,5`, matching the quotient counts exactly.

## 2. Exhaustive `n = 7` exactness check

The iso-class count is `2045`, matching A000112(7). The interval-reversal quotient produces **915 classes**, versus **1082** for iso+dual.

| quotient | classes |
|---|---:|
| iso | 2045 |
| iso+dual | 1082 |
| iso × interval-reversal | **915** |

**Classes with non-constant `F`: 0.** There is no counterexample to report. The quotient is strictly coarser than iso+dual and still exact.

Orbit-size histogram at `n = 7`:

```
{1:100, 2:685, 3:15, 4:91, 5:2, 6:17, 8:1, 10:1, 12:3}
```

## 3. `n = 8` confirmation and counts

The `n = 8` run was also completed inside the cap.

| quotient | classes |
|---|---:|
| iso | 16999 |
| iso+dual | 8746 |
| iso × interval-reversal | **7573** |

Exhaustive `F` check over all `16999` iso classes: **0 mixed classes**.

Orbit-size histogram at `n = 8`:

```
{1:431, 2:6219, 3:45, 4:736, 5:5, 6:100, 7:1, 8:10,
 10:2, 12:20, 15:1, 20:2, 24:1}
```

So the quotient removes about `55%` of iso states and about `13–15%` of iso+dual states. The absolute state counts remain in the thousands at `n = 8`.

## 4. Work measurement

One representative full run, with identical code paths and accounting. Wall-clock is load-dependent; the state and call counts are deterministic.

| n | mode | S(n) | states | moves | successor C calls | iso-canon calls | DP seconds |
|---:|---|---:|---:|---:|---:|---:|---:|
| 7 | iso | 13 | 2045 | 20123 | 40246 | 40247 | 3.22 |
| 7 | iso+dual | 13 | 1082 | 10710 | 21420 | 42842 | 3.49 |
| 7 | interval | 13 | 915 | 9632 | 19264 | 19265 | **1.63** |
| 8 | iso | 16 | 16999 | 228009 | 456018 | 456019 | 20.24 |
| 8 | iso+dual | 16 | 8746 | 117566 | 235132 | 470266 | 22.00 |
| 8 | interval | 16 | 7573 | 106604 | 213208 | 213209 | **10.37** |

Offline quotient construction:

| n | iso enumeration | orbit construction | orbit reversals |
|---:|---:|---:|---:|
| 7 | 3.05 s | 1.22 s | 4657 |
| 8 | 31.86 s | 13.26 s | 32027 |

At `n = 7`, `4657 - 2045 (full-set duals) = 2612` proper interval reversals, matching the `2612` reported in the orientation note.

**Important accounting point:** the DP itself is substantially faster (`~1.6 s` vs `3.2 s` at `n=7`; `~10.4 s` vs `20.2 s` at `n=8`), but the one-shot end-to-end interval approach is slower because the orbit table requires enumerating all iso classes: `~5.9 s` vs `3.2 s` at `n=7`, and `~55.5 s` vs `20.2 s` at `n=8`. The gain is realized only if the quotient table is amortised over repeated evaluations.

## 5. Additional structural finding: the quotient is transition-compatible

This goes slightly beyond the requested task and strengthens the answer.

**Claim (deduction).** If `S` is an interval module of `P`, then `P = A ⊕ S ⊕ B` is an ordinal sum, so every incomparable pair lies inside exactly one of `A`, `S`, `B`. For a move inside `A` or `B`, interval reversal commutes with the extension. For a move inside `S`, it swaps the two children:

```
σ_S(P + x<y) = σ_S(P) + y<x,
σ_S(P + y<x) = σ_S(P) + x<y.
```

Hence the multiset of unordered successor-class pairs is preserved by each interval reversal. Since relabelling preserves it too, the interval-reversal quotient is a sound DP quotient in the strong sense of `docs/research-compression-next.md`, not merely a partition on which `F` happens to be constant.

The exhaustive check found **0** classes with a non-well-defined successor multiset at both `n = 7` and `n = 8`.

## 6. Honest assessment

**Asymptotic gain:** none demonstrated, and none claimed. The quotient reduces the number of iso classes by a factor of about `2.2` at `n = 7,8` and the number of iso+dual classes by about `1.15`. That is a finite constant-factor compression. The state space is still governed by the same super-polynomial growth of iso classes; the operation is a local series-block symmetry, not a structural collapse of the `2^{Θ(n²)}` state space. No asymptotic claim is made from these finite runs.

**Usefulness:** it is a genuine exact quotient with the stronger transition property, so it is a valid optimization for memoised exact evaluation. Its practical value is limited by the one-time cost of building the orbit table; for a single `S(n)` evaluation at `n = 7,8`, the overhead outweighs the DP saving. It becomes useful when many evaluations share the same orbit table.

**Issue #47 (framed certificates):** the decision-tree/game symmetry suggests a possible lifting to framed DAGs: interval reversal is a fixed pair-permutation on relations, so it commutes with intersection of annotations, and the two children of an internal-`S` comparison simply swap. That is a plausible normalization/quotient route for a certificate DAG. However, a full framed-certificate lifting (slot permutations, joins, root guarantee) is not proved or implemented here, and even if it works the reduction is constant-factor. It does not address the real question: whether an optimal root sorter has a polynomial-size sound certificate at height `S(n)`.

**Issue #48 (root forcing):** interval reversal is a symmetry of the adaptive comparison game: comparability graphs are preserved, and strategies transport with outcome labels swapped for comparisons inside `S`. So forceability of a target poset is invariant under the quotient, and the adversarial state space can be quotiented by it. This can reduce case analysis by a constant factor, but it does not produce a root-specific forcing rule or any asymptotic lower-bound improvement.

## Reproduce

```bash
python3 scripts/interval_reversal_quotient.py \
  --n7 --n8 --check-transitions --verify-f --cap 900
```

The script stays untracked. `git status --short` shows only `?? scripts/interval_reversal_quotient.py`; no production files were edited.
