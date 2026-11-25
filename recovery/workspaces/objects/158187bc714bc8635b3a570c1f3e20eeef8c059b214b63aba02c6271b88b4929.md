# Structural compression of the minimax state space

**Status:** research note (2026-10-17). Everything below is a **deduction**,
**experiment**, or **conjecture** unless explicitly marked *literature*. No
Lean file and no complexity-class separation is claimed. The companion program
is `scripts/state_compression.py`; it reproduces every number in this note.

## Precise question

`docs/problem.md` fixes `S(n)` as the minimum worst-case number of adaptive
pairwise comparisons needed to sort `n` distinct labelled keys. The exact
partial-order minimax recurrence of `docs/upper-bound.md` (the value called
`adv univ` in the Lean model, proved equal to `S n` by A24) evaluates `S(n)`
over information states. The naive count of information states is
`2^{n!}` (arbitrary subsets of the `n!` permutations), and a crude count gives
`2^{O(n²)}` states. The question is:

> Which identifications of information states are **sound** for the minimax
> recurrence (preserve the optimum), how much do they shrink the reachable
> state space, and does the shrinkage change the `2^{Θ(n²)}` asymptotics?

This note answers the soundness question exactly for permutation symmetry,
measures the gain, and falsifies two stronger compression hopes.

## Source and model

*Literature/index:* the exact values used as checks are
`S(0..6)=0,0,1,3,5,7,10`, `S(7)=13`, `S(8)=16`, `S(9)=19`, `S(12)=30`, with
`S(12) > ⌈log₂ 12!⌉ = 29`; see `docs/literature.md` and `docs/research-plan.md`
(Peczarski 2012; OEIS A036604 is only an index). The state-count sequences
below are OEIS [A001035](https://oeis.org/A001035) (posets on `n` labelled
points) and OEIS [A000112](https://oeis.org/A000112) (posets on `n` unlabelled
points); they are used as **references**, and independently reproduced by our
program for `n ≤ 7` (labelled) and `n ≤ 9` (unlabelled quotient).

*Model:* a state is the strict partial order `P` (transitive closure) induced
by the comparisons made so far; `F(P)` is the minimum remaining worst-case
comparison count,

    F(P) = 0                                       if P is total,
    F(P) = 1 + min_{x,y incomparable} max( F(P+x<y), F(P+y<x) )   otherwise,

and `F(∅) = S(n)`. This is exactly `adv univ` in `SoringP1/Minimax.lean`.

## Finding 1 (deduction + experiment): reachable states are *labelled posets*

Every reachable state is a strict partial order on the labelled keys, and
**every** labelled poset is reachable: enumerate the pairs `x ≺ y` of a target
poset `P` and add them one at a time; a pair that is not already implied is
incomparable in the current sub-poset, so the comparison is legal, and the
process ends at `P`. Hence the reachable state space is exactly the set of
labelled posets, with `A001035(n)` elements — not `2^{n!}`.

This is a deduction, and it matches the existing evaluator: `scripts/evaluate.py`
memoizes exactly `A001035(n)` states. Measured by `scripts/state_compression.py`
(labelled DP), `S(n)` and state counts are:

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| S(n) | 0 | 0 | 1 | 3 | 5 | 7 | 10 | 13 |
| states | 1 | 1 | 3 | 19 | 219 | 4231 | 130023 | 6129859 |
| A001035(n) | 1 | 1 | 3 | 19 | 219 | 4231 | 130023 | 6129859 |

`2^{n!}` for comparison: `2`, `2`, `4`, `2^6`, `2^24 ≈ 1.7·10^7`,
`2^120 ≈ 1.3·10^36`, `2^720 ≈ 5.5·10^216`. So the first compression,
`2^{n!} → A001035(n)`, is already built into any correct partial-order DP.

## Finding 2 (deduction): the `S_n` symmetry quotient is exact

Let `S_n` act on labelled posets by relabelling keys: `(π·P)` has
`π(x) ≺' π(y) ⟺ x ≺ y`.

**Claim.** `F(π·P) = F(P)` for every permutation `π`.

*Proof sketch.* Relabelling keys by `π` is a bijection of the comparison
model: it maps comparisons, decision trees and correctness to themselves, so
an optimal tree for `P` transports to one for `π·P`, and conversely. ∎

Consequently `F` is well defined on isomorphism classes `[P]`, and with
`G([P]) := F(P)` for any representative,

    G([P]) = 0                                    if P is total,
    G([P]) = 1 + min_{x,y incomparable in P} max( G([P+x<y]), G([P+y<x]) ).

**Exactness (when it preserves the optimum).** For any representative `P' = π·P`
the successor set satisfies `P'+x'<y' = π·(P+x<y)` with `x'=π(x), y'=π(y)`, so
the multiset of successor classes and their `G` values is representative-
independent; the inner `min`/`max` is unchanged. Hence `G([∅]) = F(∅) = S(n)`.
The quotient is sound **for the full relabelling group `S_n`**.

*Generalization (deduction).* The same equivariance argument shows that
quotienting by **any** subgroup `H ≤ S_n` is sound (successors are
`H`-equivariant, `F` is `H`-invariant). This gives a trade-off: smaller `H`
means more classes but cheaper canonicalization. `H = S_n` minimizes the state
count.

## Finding 3 (experiment): measured state counts and time

`scripts/state_compression.py` implements the quotient recurrence with a
complete isomorphism invariant (2-dimensional colour refinement followed by
brute force inside colour classes). Measured values agree with `S(n)` and with
`A000112(n)`:

| n | quotient S(n) | classes (=A000112) | time | labelled time |
|---|---|---|---|---|
| 3 | 3 | 5 | 0.001 s | 0.000 s |
| 4 | 5 | 16 | 0.002 s | 0.001 s |
| 5 | 7 | 63 | 0.015 s | 0.048 s |
| 6 | 10 | 318 | 0.14 s | 2.4 s |
| 7 | 13 | 2045 | 1.5 s | 185 s |
| 8 | 16 | 16999 | 19 s | (≈4.3·10⁸ states, not run) |
| 9 | 19 | 183231 | 305 s | (≈4.5·10¹⁰ states, not run) |

The quotient reproduces the literature value `S(8)=16` and independently
recomputes `S(9)=19`, both far outside the labelled DP's practical range here.
For reference, a brute-force canonical form (minimum over all `n!` relabellings)
took 11.6 s at `n=6`, versus 0.14 s for the colour-refinement invariant.

| n | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|
| A001035(n)/A000112(n) | 67 | 409 | 2998 | 25397 | 242923 |
| n! | 120 | 720 | 5040 | 40320 | 362880 |

The saving is a factor between `A000112(n)` and `n!·A000112(n)` (exactly
`A001035(n) = Σ_classes n!/|Aut(P)|`), i.e. a factor `2^{Θ(n log n)}`.

## Smallest compelling example

The quotient does real work already at `n=3`: the labelled DP stores 19 states;
the quotient stores 5. At `n=4`, 219 → 16; at `n=5`, 4231 → 63. The first case
where the quotient's *practical* value is dramatic is `n=7`: 6,129,859 labelled
states (185 s) collapse to 2045 classes (1.5 s), and the answer `S(7)=13` is
unchanged.

## Falsification attempts

### (a) A coarser invariant (linear-extension count) does **not** preserve `F`

A natural hope is to compress a state to its information content, e.g. the
number `L(P)` of linear extensions. **Falsified at `n=5`.** Two non-isomorphic
posets on 5 elements, each with `L = 8`, have different remaining costs:

* `P` with relations `4<3, 4<2, 3<0, 3<1` (Hasse: bottom `4`; `4` covers `2`
  and `3`; `3` covers `0` and `1`): `F(P) = 3`.
* `Q` with relations `2<0, 4<2, 3<0, 3<1, 4<1` (Hasse: minimal `3,4`; `4`
  covers `2,1`; `2` covers `0`; `3` covers `0,1`): `F(Q) = 4`.

Both have 8 linear extensions (so the same information bound `⌈log₂ 8⌉ = 3`),
but `F` differs. Therefore no state that is a function of `L(P)` alone — in
particular no "entropy/leaf-count" state — can compute `S(n)` exactly. This is
a concrete, small instance of the phenomenon behind `S(12) > ⌈log₂ 12!⌉`:
leaf counting is not a sufficient statistic for the minimax cost.

### (b) A restricted class of decision trees does **not** preserve the optimum

Another hope is to restrict the trees searched over. Consider the deterministic
**balanced-greedy** class: at every state compare a pair minimizing the larger
child's linear-extension count. This class is optimal for small `n` — it
returns `S(3..8) = 3,5,7,10,13,16` — but **fails at `n=9`**: it returns `20`
while `S(9)=19`. Hence this restricted class does not preserve the optimum, and
cannot replace full minimax search. (Computed on the quotient, so the value is
well defined; note `20` is a genuine upper bound for `S(9)` from an explicit
tree, while `19` is `S(9)`.)

## What was learned

1. **Sound and useful.** Quotienting the partial-order minimax recurrence by
   key relabelling is *exact* (Finding 2), cuts the state count by a factor
   `2^{Θ(n log n)}` (Finding 3), and extends practical exact computation from
   `n=7` (labelled, 6.1M states) to `n=9` (183k classes) in pure Python.
   Quotienting by any subgroup `H ≤ S_n` is also exact, giving a
   canonicalization-cost vs state-count trade-off.
2. **Not asymptotic.** Both `A001035(n)` and `A000112(n)` are `2^{Θ(n²)}`
   (measured `log₂ A001035` tracks `n²` closely: 12,17,22.5,28.7,35.4 for
   `n=4..8`). Symmetry compression changes only the polynomial factor, **not**
   the `2^{Θ(n²)}` exponent of the crude bound. It is a constant-factor
   (superpolynomial-in-`n`, but sub-exponential) improvement.
3. **Two compression hopes are false.** Neither the linear-extension count nor
   the balanced-greedy restricted tree class preserves the optimum. The state
   genuinely needs the poset's structure, and the tree search genuinely needs
   the minimax `min` over all incomparable pairs.

## Next unresolved obstacle

**Canonicalization cost, not state count, is the bottleneck.** The measured
quotient state count at `n=9` is only 183,231, yet the run takes 305 s because
the complete invariant still brute-forces permutations inside colour classes
(worst case `n!` for highly symmetric posets such as the antichain). A proper
canonical labelling / orderly generation (e.g. nauty-style, or Poset
canonicalization) should make the quotient DP reach `n=10`–`n=12`, where the
known obstruction `S(12)=30` lives. The open structural questions are then:

* Does a canonical-form DP over `A000112(n)` classes have a *provable* time
  bound better than `poly(n)·2^{Θ(n²)}`? The class count is still
  `2^{Θ(n²)}`, so a better bound would need either a much smaller *reachable*
  quotient (are all `A000112(n)` classes actually reachable? experiment says
  yes for `n ≤ 9`) or a decomposition theorem.
* **Decomposition.** Posets that are disjoint unions / series-parallel
  compositions admit a merge structure, but the minimax value of a disjoint
  union is *not* additive (comparisons across components may be interleaved);
  making this a sound, smaller recurrence is unresolved.
* The `n=5` witness shows the obstruction is already present at tiny `n`; a
  reusable invariant stronger than leaf counting, and weaker than the full
  poset, is not known.

## Reproduce

    python3 scripts/state_compression.py --max-n 6 --falsify-n 5

and, for the quotient beyond the labelled range (each is a separate run):

    python3 -c "import sys; sys.path.insert(0,'scripts'); import state_compression as sc; \
    print(sc.quotient_solve(9, refined=True))"

The balanced-greedy falsification and the `n=5` witness construction are in
this note and in `scripts/state_compression.py` (`falsify_coarse_invariant`);
the greedy check is a short inline computation over the same quotient routine.
