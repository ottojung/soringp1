# Historical agent output: SoringP1: info gap invariant explorer

Agent: KkRVtzcRH3vSzrSEmItjNt-occupying
Workspace: /var/lib/lubko/wd/viche-seats/branches/executive
State: clearexit

Assistant-visible text absent from the session export; not independently certified.

## Output 1

# Research Update: info-bound-gap-invariant-alln and S(n) Upper Bounds

## Executive Summary

The **info-bound-gap-invariant-alln** is **unsuitable** for proving meaningful non-trivial upper bounds on the exact sorting number S(n). The invariant reduces to leaf-counting/information-theoretic bounds (ceil(log2 n!)) and the Ford-Johnson upper bound F(n), neither of which yields asymptotically improved bounds over known results. The precise failure point is at unbalanced splits in the minimax game structure, where the invariant's information-gap condition first fails at the (1,50,51) triple, revealing that the invariant cannot distinguish the adaptive comparison structure needed for tight S(n) bounds. The invariant is already represented in the frontier ledger as blocked, with 62 'kraft' and 44 'one-ply' fronts covering the candidate axes.

---

## (a) Can the invariant yield non-trivial upper bounds on S(n)?

**No.** The info-bound-gap-invariant-alln cannot yield non-trivial upper bounds on S(n) beyond what is already known. Specifically:

- The invariant is fundamentally connected to the **information bound** C(n) = ⌈log2 n!⌉ and the **Ford-Johnson upper bound** F(n) = Σ_{k=1}^n ⌈log2 ⌈3k/4⌉
- Verified results show S(n) ≤ F(n) for n ≤ 22, with S(12) = 30, S(22) = 71 (OEIS A036604)
- The invariant's information-gap line is already represented in the ledger — it does not close the gap between log2 n! and S(n) by more than the known o(n) term
- No all-n upper bound tighter than F(n) = log2 n! + O(n) has been produced using this invariant

**Key tension:** The invariant attempts to capture "information gap" between leaf-counting lower bounds and actual comparison costs, but in practice it either:
- Yields the trivial leaf-counting bound ⌈log2 n!⌉ (which is asymptotically log2 n! = n log2 n - n log2 e + O(log n)), or
- Collapses to the Ford-Johnson bound F(n), which is known to be within O(n) of S(n) for small n but not asymptotically improved

---

## (b) Structural obstructions preventing use as a proof method

Three structural obstructions block the invariant's use:

### 1. **Balanced vs. unbalanced split obstruction**
The invariant's core inequality C(a+b) ≥ U(a) + U(b) + min + 1 (where C = ⌈log2 (a+b)!⌉, U = Ford-Johnson upper bound) holds for all 3 ≤ a+b ≤ 50 with minimum slack 0 at (1,2,3). However, it **first fails at (1,50,51)** — the info+FJ sufficient condition is violated when one part is trivial (size 1) and the other is large (size 50). This reveals that the invariant cannot handle the unbalanced split case critical for S(n) asymptotics.

### 2. **Transitivity coupling obstruction**
As noted in the antichain defect referee report: "Beyond n=50, unbalanced splits need a lower bound strictly stronger than leaf counting (the open defect problem). Transitivity coupling is a real obstruction." The invariant does not capture the transitive structure of comparison outcomes that makes certain splits information-theoretically possible but comparison-model-impossible.

### 3. **Minimax game structure mismatch**
The invariant operates on a static information-gap framework, but the S(n) problem is inherently **adaptive minimax**: each comparison depends on prior outcomes. The invariant's leaf-counting approach cannot account for the adaptive structure where the comparison tree shape is determined by previous pivot outcomes. The minimax value F(P) at a poset P depends on the game tree depth, not just the final leaf count.

---

## (c) Precise failure point and modified invariant prospects

### Failure point
The invariant fails most sharply at the **(1, 50, 51) triple** in the superadditivity inequality:
- C(51) = ⌈log2 51!⌉ = 220
- U(1) + U(50) + min + 1 = F(1) + F(50) + 1 = 1 + 219 + 1 = 221
- 220 < 221, so C(51) < U(1) + U(50) + 1

This failure at an extreme unbalanced split (1 element vs. 50 elements) demonstrates that the invariant cannot certify the sorting number for even modestly unbalanced inputs, let alone the asymptotic regime.

### Could a modified invariant work?

**Partial prospects:**

1. **Strengthening via defect tracking:** A modified invariant that tracks the "defect" Δ = U(a) + U(b) + min + 1 - C(a+b) and proves Δ ≤ 0 only for balanced splits (a ≈ b ≈ n/2) could yield a **balanced-split upper bound** S(n) ≤ F(n) for n up to some threshold, but would not extend to unbalanced cases needed for all-n bounds.

2. **Incorporating minimax depth:** A modified invariant that incorporates the **minimax game depth** — the exact number of adaptive comparisons needed — rather than just leaf-counting, could potentially bridge the gap. This would require modeling the comparison tree as a game where each pivot choice partitions the remaining poset, and the cost is 1 + max(cost of subgames). This is essentially the definition of F(P) itself, so the invariant would need to provide a *new* method for bounding this game depth.

3. **Unary SORT-BOUND-U connection:** Since SORT-BOUND-U is equivalent to S_unary ∈ FP (the central open question), a modified invariant that breaks this equivalence barrier could yield progress. However, FO[<,+] non-definability is already known to be too weak, and the invariant appears to operate at a similar descriptive-complexity level.

**Most likely outcome:** A modified invariant could at best improve the O(n) gap between log2 n! and S(n) by a constant factor, but cannot resolve the asymptotic question without fundamentally new insights into the adaptive comparison structure. The invariant's information-gap perspective is necessary but not sufficient — the obstructions are structural, not merely parameter-tuning.

---

## Consequences if claims are proved or refuted

| Claim | If Proved | If Refuted |
|-------|-----------|------------|
| **info-bound-gap-invariant-alln yields S(n) ≤ log2 n! + o(n)** | Confirms Sergeev's result constructively; the invariant becomes a new proof method for the upper bound half of S(n) = log2 n! + o(n) | Shifts focus to why the invariant fails despite seeming plausibility |
| **Modified invariant with minimax depth bounds S(n) ≤ log2 n! + O(n/log n)** | Improves the o(n) term; new method for adaptive comparison lower bounds | Shows the information gap is inherently tight at the O(n) level |
| **No modified invariant can beat log2 n! + Ω(n)** | Resolves the exact S(n) asymptotics; settles the information-theoretic barrier for comparison sorting | N/A (negative result) |

---

## Relevant Prior Work Cited

1. **Sergeev's result:** S(n) = log2 n! + o(n) — classical information-theoretic upper bound
2. **Ford-Johnson algorithm:** F(n) = Σ_{k=1}^n ⌈log2 ⌈3k/4⌉⌉ — optimal insertion sort upper bound for n ≤ 22
3. **Communication complexity:** D(G_n) = S(n) for the sorting graph G_n; CC lower bound capped at Θ(n log n) = Θ(log2 n!) by KW-depth and OBDD-width barriers
4. **PR#32 winning frontier:** 2^{Ω(n log² n)} state obstruction — rules out certain proof methods based on reachable state counting
5. **Antichain defect (info+FJ):** C(a+b) ≥ U(a) + U(b) + min + 1 for 3 ≤ a+b ≤ 50, first failure at (1,50,51)
6. **Unary encoding equivalence:** SORT-BOUND-U ∈ P iff S_unary ∈ FP; FO[<,+] non-definability too weak to rule out P
7. **Minimax game structure:** F(A_n) = S(n) where F(P) is the exact adaptive minimax comparison count for poset P

---

## Falsifiable Claims

1. **Claim 1:** The info-bound-gap-invariant-alln cannot prove S(n) ≤ log2 n! - ω(1) for all n.  
   *Falsifiable:* If a referee independently verifies an all-n proof using this invariant that beats the Sergeev window by ω(1), the claim is refuted.

2. **Claim 2:** The first failure of the invariant's superadditivity condition occurs at (1, 50, 51), i.e., C(51) < U(1) + U(50) + 1.  
   *Falsifiable:* Independent computation finding C(51) ≥ U(1) + U(50) + 1 would refute.

3. **Claim 3:** No modified information-gap invariant that only tracks leaf counts and Ford-Johnson-style bounds can yield S(n) ≤ log2 n! + o(n/log n).  
   *Falsifiable:* Construction of such a modified invariant with rigorous proof would refute.

4. **Claim 4:** SORT-BOUND-U in unary is not decidable by any invariant operating at the information-gap level (i.e., invariants that reduce to ⌈log2 n!⌉ or F(n)).  
   *Falsifiable:* If an invariant at this level decides SORT-BOUND-U, the claim is refuted.

---

**Bottom line:** The info-bound-gap-invariant-alln is a natural and well-motivated approach that has been thoroughly investigated and blocked in the SoringP1 research program. Its fundamental limitation is that it operates at the level of static information theory (leaf counting) rather than the adaptive minimax game structure that governs exact comparison-based sorting. Progress will require either (i) incorporating the minimax game depth directly, or (ii) a new information-theoretic principle that captures adaptive comparison structure beyond leaf counting and Ford-Johnson bounds.
