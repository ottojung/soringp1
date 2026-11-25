# Information-theoretic excess: is D(n) = S(n) − ⌈log₂ n!⌉ bounded?

**Status:** research note (front `excess-boundedness-alln`). Labels:
`[literature]`, `[deduction]`, `[experiment]`, `[open]`. Not Lean-checked.
**No claim is proved or disproved in either direction**; the deliverable is
an exact reformulation, verified data, and a precise statement of why both
directions are blocked with current methods.

This supersedes the failed ledger attempt of the same front ID (agent
`ZUXz9lJCh2L32e4P7lRTRu-anything`, status *blocked*), which stopped at the
observation that intermediate-poset excess does not automatically transfer
to the antichain root.

## 0. Statement

`[definition]` `D(n) = S(n) − ⌈log₂ n!⌉ ≥ 0`.
Question: is `sup_n D(n) < ∞` (constant excess) or `sup_n D(n) = ∞`?

## 1. Verified data (experiment, scripts/excess_waste_probe.py)

`C(n) = ⌈log₂ n!⌉` computed by exact integer comparison with powers of two;
`S(n)` values and their provenance from the literature (OEIS A036604;
Peczarski 2004/2007; Stober–Weiß, arXiv:2206.05597 / ALENEX 2023, Table 7);
`F(n)` = Ford–Johnson (merge-insertion) count (OEIS A001768,
`F(n) = Σₖ ⌈log₂(3k/4)⌉`), recomputed exactly.

| n | 1..11 | 12–19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|
| D(n) | 0 | 1 | 0 | 0 | 1 | **0 or 1 (open: S(23) ∈ {75, 76}, C(23) = 75)** |

- `[experiment]` `sup_{n ≤ 22} D(n) = 1`; even at `n = 23` whether `D = 0`
  holds is undecided. Every value of `D(n)` ever computed is 0 or 1.
- `[experiment]` `D` is not monotone: it is `= 1` for `12 ≤ n ≤ 19` and
  drops to `0` at `n = 20, 21`, then returns to `1` at `n = 22`. The same
  drop pattern appears in the Ford–Johnson count `F(n) − C(n)`
  (0 at `n = 20, 21`, 1 at `n = 22`), so the drop is intrinsic to the
  integer structure of `log₂ n!` and partition sizes, not an artefact of
  one algorithm.
- `[experiment]` Ford–Johnson excess `F(n) − C(n)`: `≤ 1` for all
  `n ≤ 22`, first 2 at `n = 25`, 3 at `n = 28`, 4 at `n = 48`, …, 10 at
  `n = 103`, 28 at `n = 255`, 40 at `n = 410`; asymptotically
  `Θ(n)` with constant between `log(3e/8) ≈ 0.028` and
  `log(3/(4 ln 2)) ≈ 0.114` depending on `n` (Sergeev TR20-096, §1).
  The best published all-`n` construction leaves a growing gap:
  `D(n) ≤ S(n) − C(n) ≤ O(n/(log n)^{1/5}) = o(n)` **[literature]**.
- `[experiment]` Waste identity verification below is exact to floating
  precision (`|depth − log₂ n! − Σν| < 8·10⁻¹⁶`) for optimal trees
  `n ≤ 5`.

## 2. Waste identity (paper deduction; exact, not heuristic)

Fix a **reduced** correct comparison tree for `n` keys, where every
reached leaf sorts exactly one permutation. For an internal node `v` let
`e(v)` be the number of linear extensions of the poset reachable at `v`,
and for a taken branch `i` let `e(vᵢ)` be the child's extension count.

For any root-to-leaf path `ℓ` with branch extensions `e(vᵢ)`:

    log₂ n! = Σ_{v on ℓ} log₂ ( e(v) / e(vᵢ) )        (telescoping)

because the extension count falls from `n!` to `1` along the path and the
taken branch is exactly compatible with the leaf's permutation. Therefore,
**exactly**,

    depth(ℓ) − log₂ n! = Σ_{v on ℓ} ( 1 − log₂ (e(v)/e(vᵢ)) ) =: Σ_{v on ℓ} ν(vᵢ)

with the per-branch *inefficiency* `ν(branch) = 1 − log₂(e(v)/e(branch))`
(free to be negative: an unbalanced branch such as `8 → 1` gains
`3 > 1` bits, so `ν = −2`). Define

    W*(n) = min over reduced correct trees of  max over leaves ℓ of
            Σ_{v on ℓ} ( 1 − log₂ (e(v)/e(vᵢ)) ).

Since depth is an integer and every leaf's depth `≥ log₂ n!` summands is
`≤` its depth-bits, this yields the **exact identity**

**Theorem 2.1 (deduction).** `S(n) = ⌈log₂ n! + W*(n)⌉`, and
`D(n) = ⌈log₂ n! + W*(n)⌉ − ⌈log₂ n!⌉`. In particular:

1. `D(n) ≤ C` for all `n` (the bounded-excess side) **iff** for every `n`
   there is a correct tree in which **every** path accrues ≤ `C + 1`
   total waste (with `ν` signed); a single adversarially path-visible
   per-comparison residue ε > 0 held on Θ(n) comparisons per path makes
   every such tree have waste Ω(n) along the adversary's chosen path.
2. `W*` satisfies the minimax recursion on posets
   `W(P) = min_{x<y} max_{branch} [ 1 − log₂(e(P)/e(branch)) + W(branch) ]`
   with `W(total order) = 0` and `W*(n) = W(antichain_n)`, so bounding
   excess is exactly a **uniform O(1) bound on a continuous potential**,
   stronger and more structured than the scalar `e(P)`.
   `[experiment]` `W` is *not* a function of `e(P)` alone: for `n = 5`
   there are two posets with `e(P) = 8` whose minimax heights differ by
   exactly 1; likewise `e = 15` at `n = 6`. (Consistent with the
   earlier falsification of five scalar invariants,
   `research-n12-nontightness.md`.)
3. `D(n) = 0` forces waste ≤ `slack(n) = ⌈log₂ n!⌉ − log₂ n! = 1 − frac(log₂ n!) ∈ (0,1)` on
   **every** path. For `n = 12`, `slack(12) ≈ 0.1681`:
   the non-tightness at `n = 12` says precisely that no tree has every
   path uniformly within 0.168 bits of perfect split information. For
   `n = 22`, `slack(22) ≈ 0.0164`, an even sharper obstruction.
   `[experiment]` verified:
   maximized waste of optimal `n ≤ 5` trees is `0`, `0`, `0.415`, `0.415`,
   `0.093`; the recurrence reproduces `S(n)` and `D(n) = 0` exactly.

## 3. Why both directions are blocked today (barrier status)

**Bounded side (`sup D ≤ C`) needs a construction, and none exists.**
Every published sorting scheme is an insertion/merge scheme whose
per-insertion waste is bounded below by a positive amount on a positive
fraction of inputs: binary insertion over `log₂ n!` gives excess
`B(n) − log₂ n! = Σ (⌈log₂ k⌉ − log₂ k)` with per-element average
≈ 0.5 → excess `Θ(n) ≈ 0.5·n − circ(n)` (Knuth's `B(n)`; ratio to `n`
measured `0.30…0.52` for `n = 10…10⁴`) `[experiment]`;
Ford–Johnson's constant is in `[0.028, 0.114]` `[literature]`; Sergeev's
group insertion gains only `o(1)` bits per element, still with
`Σ_k`-loss divergent — no published scheme has summable per-element
loss, which is exactly what a constant `C` would require by Theorem 2.1.
No analytic route to `S(n) ≤ ⌈log₂ n!⌉ + O(1)` is known for any `n ≥ 23`
even sporadically: even `D(23) = 0 vs 1` is unsettled **[literature]**.

**Unbounded side (`D(n) → ∞`) needs the first analytic lower bound above
the information bound.** Every single known fact `D(n) ≥ 1` results from
exhaustive search over poset states (Wells 1965 for `n = 12`; Kasai et al.
1994 for `n = 13`; Cheng–Yamamoto–Akiyama / Peczarski 2004 for
`n = 14, 15`; Peczarski 2007 for `n = 22`; Stober–Weiß 2023 for
`n = 16, 17, 18`; the republished values of `S(19) = 58` trace to the
Cheng–Liu–Wang–Liu result cited as [1] in the Stober–Weiß table). No
published argument gives
`S(n) > ⌈log₂ n!⌉` analytically for any `n ≥ 12`, and none gives
`D(n) ≥ 2` for *any* `n` — the smallest unknown cell is `D(23)`.
Moreover any adversary-potential argument must survive the non-monotone
drops at `n = 20, 21` (both `D` and `F − C` return to 0 there), so a
monotone drift argument such as "residue classes accumulate" cannot be
uniform in the naive form.

## 4. Falsifier (restated, sharper than the front question)

Because of Theorem 2.1 the two falsifiers become concrete:

1. **Bounded side.** Exhibit, for all `n ≥ n₀`, a construction (uniform,
   projection to a real sorting procedure permitted — group insertion or
   otherwise) whose tree satisfies max-leaf waste ≤ `C`. Equivalent
   concrete requirement by Theorem 2.1: each element of the construction
   contributes a per-insertion waste schedule whose total sum is O(1),
   in particular per-element loss must tend to 0 *summably*
   (`Σ εₖ < ∞`). No such schedule exists in the published variants of
   binary insertion, merge-insertion, or Sergeev group insertion.
2. **Unbounded side.** Give an analytic (non-enumerative) invariant `W'`
   with `W' ≥ W` pointwise on reachable posets from the antichain under
   optimal play and `⌈log₂ n! + W'(antichain)⌉ → ∞ − ⌈log₂ n!⌉ → ∞`,
   for infinitely many `n`; or at minimum prove `D(23) = 1` (i.e.
   `S(23) = 76`) — a finite exhaustive question (Stober–Weiß estimate it
   as feasible) which would push the known-excess record from
   `sup = 1` to a second confirmed `D ≥ 1` at `n = 23` and arbitrate
   whether the `n = 20, 21` dip is a one-off or a family. It is not
   known whether any `n` has `D(n) ≥ 2`.

## 5. What this changes vs the prior ledger entry

The failed attempt observed only that local excess on intermediate posets
need not transfer to roots. The additions here are:

- the exact waste identity and the reformulation of excess-boundedness as
  a uniform O(1) bound on the minimax potential `W*` (Theorem 2.1);
- the verified data table of `D(n)` (n ≤ 22) and the record observation
  that *every* computed value is 0 or 1 with the non-monotone dip at
  20, 21 (also mirrored by `F − C`);
- the slack sharpening: `D(22) ≥ 1` is a strictly stronger per-path
  regularity statement than `D(12) ≥ 1` (0.016 vs 0.168 bits), so
  the exhaustive searches certify *tightening* constraints as `n`
grows along power-of-2 alignment, not just isolated gaps;
- a precise statement that the construction-side and lower-bound-side
  each require a specific missing tool (summable loss schedule; first
  analytic info-bound-refuting lower bound), and that `D(23)` is the
  immediate decisive cell.

## 6. Sources

- Igor S. Sergeev, *On the asymptotic complexity of sorting*, ECCC
  TR20-096 (2020), Theorem 3 and §1 (Ford–Johnson constants):
  <https://eccc.weizmann.ac.il/report/2020/096/download>
- F. Stober, A. Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements*,
  ALENEX 2023 / arXiv:2206.05597, Table 7 (`C(n), F(n), S(n)` for
  `n ≤ 22`, plus S(23) window and S(28) ≥ 99).
- M. Peczarski, *New results in minimum-comparison sorting*, Algorithmica
  40 (2004) 133–145; *The Ford–Johnson algorithm still unbeaten for less
  than 47 elements*, IPL 101 (2007) 126–128 (`S(22) = 71`,
  `S(23) ∈ {75, 76}` window).
- OEIS A036604 (sorting numbers), A001768 (merge-insertion counts).
- D. E. Knuth, TAOCP Vol. 3, §5.3.1 (merge insertion; binary insertion
  formula `B(n)`).

## 7. Status

`[open]` both directions. Nothing here is a proof of boundedness,
unboundedness, or impossibility; the theorem is an exact identity and
all numeric claims are `[experiment]` or `[literature]`. The
`n = 23` computation (`S(23) = 75 or 76`) is the next concrete step that
would discriminate; no SoringP1 Lean change follows from this note.
