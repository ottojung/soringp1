# Bidirectional Advice Prototype (Stober–Weiß 2023)

**Date:** 2026-10-18
**Branch:** `research/bidirectional-advice-20261018`
**Script:** `scripts/bidirectional_advice.py`
**Tests:** `tests/test_bidirectional_advice.py`

## Research question

Can a partial backward table of confirmed-YES states (exact minimax cost ≤ B)
reduce forward search cost for proving S(n) ≤ k, while maintaining soundness?
What is the state/memory/runtime tradeoff?

## Model and source

Adaptive comparison decision trees sorting n distinct labelled keys (standard
worst-case model, same as `docs/problem.md`). States are subsets of permutations
consistent with comparisons made so far; equivalently, labelled posets on n
elements.

**Primary source:** Florian Stober and Armin Weiß, *Lower Bounds for Sorting
16, 17, and 18 Elements*, arXiv:2206.05597v2 [cs.DS], 18 Nov 2022.
Sections 3–4, 5.7. Key ideas adapted:

- §3: Forward search via minimax recurrence `S_c(P) = ∨_{(u,v)} (S_{c+1}(P+uv) ∧ S_{c+1}(P+vu))`.
- §4.1: Backward search enumerates predecessors (posets one comparison away
  from sortable). Full backward search is impractical alone (682·10⁶ posets
  for n=13 vs 1.8·10⁶ forward).
- §4.2: Partial backward search — only store states meeting an efficiency
  threshold. Forward search uses results as advice: if a state is in the
  table, it is winning; if marked "unknown", forward must branch.
- §5.7: Predecessor enumeration via Hasse diagram edge removal + transitive
  closure computation.

## Implementation

Tiny Python prototype for n ≤ 5 (≤ 120 permutations, ≤ 4231 labelled posets):

1. **Backward pass:** BFS from root (full antichain) over all reachable states.
   Compute exact minimax cost for each: `cost(s) = 0` if |s|≤1, else
   `1 + min over comparisons of max(cost(left), cost(right))`. Store all
   states with cost ≤ B in advice table.

2. **Forward pass:** DFS from root with remaining budget b. At each state:
   - If |s| ≤ 1: leaf, success.
   - If s in advice and advice[s] ≤ b: prune as YES (sound: exact cost known).
   - Otherwise: **UNKNOWN ≠ FALSE** — must branch and explore children.

3. **Soundness verification:** Every table entry independently recomputed;
   assert exact match.

4. **Comparison:** Plain DFS (no advice, no memoization) at same budget.

## Results

### Full table (B = S(n))

| n | S(n) | Table states | Fwd nodes | Plain DFS nodes | Speedup |
|---|------|-------------|-----------|-----------------|---------|
| 1 | 0 | 1 | 1 | 1 | 1.0x |
| 2 | 1 | 3 | 1 | 3 | 3.0x |
| 3 | 3 | 19 | 1 | 11 | 11.0x |
| 4 | 5 | 219 | 1 | 101 | 101.0x |
| 5 | 7 | 4231 | 1 | 107659 | 107659.0x |

Forward search with full table visits only the root (immediate YES). Table
size = number of labelled posets on n elements (OEIS A001035: 1, 3, 19, 219,
4231 for n=1..5).

### Partial table (B < S(n)) — n=5 example

| Partial budget | Table states | Fwd nodes | Fwd comps | Plain DFS |
|---------------|-------------|-----------|-----------|-----------|
| 5 | 4150 | 82913 | 73273 | 107659 |
| 6 | 4230 | 3 | 1 | 107659 |

With B=5 (one less than S(5)=7), forward still visits 82913 nodes — only
modest improvement. With B=6, forward drops to 3 nodes. The tradeoff is
sharp: the last layer of backward states does most of the pruning work.

## Soundness

All advice table entries verified by independent re-evaluation (test
`TestSoundness`). Partial tables cause no false negatives
(`TestPartialTable_no_false_negative`): forward search always returns True
when S(n) ≤ budget, even with empty advice.

## Limitations and negative assessment

- **No efficiency threshold (§4.2 E_thr):** Our prototype stores all states
  with cost ≤ B, not just those with efficiency ≤ threshold. Stober–Weiß's
  efficiency-based pruning is the key innovation that makes partial tables
  small enough for n=16+. Our prototype does not implement this.
- **No congruence/isomorphism reduction (§5.3–5.4):** We use labelled posets
  directly. Stober–Weiß reduce by congruence (isomorphic or dual-isomorphic),
  cutting state space by ~n! factor. For n=5 this matters (4231 → 63 unlabeled
  posets).
- **No predecessor enumeration (§5.7):** Our backward pass uses forward BFS
  from root, not backward search from leaves. True backward search requires
  the Hasse-diagram-based predecessor enumeration of §5.7, which is more
  complex but necessary for larger n.
- **Exponential state space:** Table size grows as labelled posets
  (A001035): 4231 (n=5), 130023 (n=6), 6129859 (n=7). Full tables are
  infeasible beyond n≈7 without compression.

## Complexity assessment (precise, no exaggeration)

For n ≤ 5, the prototype is a **feasibility demonstration only**. The
bidirectional approach with efficiency thresholds (Stober–Weiß §4.2) is what
enables n=16+ computation. Our contribution is:

1. A verified toy implementation showing the advice mechanism is sound.
2. Quantitative tradeoff data: table size vs forward search reduction.
3. Confirmation that partial tables with UNKNOWN ≠ FALSE preserve correctness.

**No asymptotic claims are made.** The prototype does not scale to n≥6 without
the full Stober–Weiß machinery (efficiency thresholds, congruence reduction,
predecessor enumeration, disk-based storage).

## What would be needed for n≥6

1. Implement efficiency-based partial backward search (§4.2, E_thr bandwidth).
2. Implement congruence reduction via color refinement (§5.3).
3. Implement predecessor enumeration (§5.7) for true backward search.
4. Disk-based storage with SSD caching (§5.1).

This is a significant engineering effort, appropriate only if the research
question demands n≥6 exact computation. For the current objective
(understanding complexity of evaluating S(n)), the toy prototype + tradeoff
data suffices to validate the mechanism.

## Provenance

- Algorithm: Stober & Weiss 2023, arXiv:2206.05597v2, §§3–4, 5.7.
- Model: `docs/problem.md` (adaptive comparison trees, distinct labelled keys).
- Known values: S(1..5) = 0, 1, 3, 5, 7 (standard; see `docs/literature.md`).
- Labelled poset counts: OEIS A001035.
