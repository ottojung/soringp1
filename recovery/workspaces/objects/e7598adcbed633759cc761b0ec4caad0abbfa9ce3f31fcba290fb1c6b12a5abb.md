# The n=12 obstruction and finite/structural invariants beyond `log2 e(P)`

**Status (2026-11-05).** Research note answering the falsifiable question:
can the `n = 12` obstruction `C(12) = ⌈log₂ 12!⌉ = 29`, `S(12) = 30` be
explained by a *generalizable finite/structural invariant* — sound for all
relevant `n` (or an infinite family) — that predicts/explains the `+1` gap
beyond `log₂ e(P)`; or is there a precise no-go showing that known candidate
invariant families cannot generalize from `n = 12`?

**Conclusion (B, precise no-go for stated classes; no known generalizing
invariant).** No known finite/structural invariant stronger than the
information bound `L0(P)=⌈log₂ e(P)⌉` is demonstrated to predict or explain
the root obstruction `S(12)=F(antichain₁₂) > 29`. Several natural candidate
families are ruled out as explanations of that gap: scalar functions of
`e(P)` (and equivalent efficiency/slack forms) cannot determine poset
sortability, monotone-in-`e` and symmetry invariants are false, the
Wells/Peczarski/Stober–Weiß efficiency pruning is equivalent to node-level
leaf counting (not a stronger invariant), forced-prefix/split-ratio signatures
occur at tight values, and compositional merge-factor bounds do not strengthen
`L0` on the antichain root. Sound strengthening families exist (the one-ply
adversarial bound `L1`, and more generally finite-depth lookahead) but none is
verified to give `L1(antichain₁₂) ≥ 30`, and fixed finite lookahead is not
known to capture the deep strategic obstruction certified only by exhaustive
search. The `n=12` gap therefore remains a global/strategic obstruction with
no compact, checkable invariant certificate in the literature or in this
repository.

Every claim is labelled `[definition]`, `[literature]`, `[deduction]`,
`[experiment]` (project evidence, cited to internal notes/scripts), or
`[conjecture]`. This note makes no complexity-class claim and no Lean claim.

## 0. Model and the `n=12` fact

`[definition]` `F(P)` is the minimum worst-case number of adaptive pairwise
comparisons needed to identify the unknown linear extension of a finite poset
`P` (algorithm knows `P`, adversary chooses the extension). `S(n) =
F(antichain_n)`. `e(P)` is the number of linear extensions. The information
(leaf-counting) bound is `L0(P)=⌈log₂ e(P)⌉ ≤ F(P)`. `C(n)=L0(antichain_n)=
⌈log₂ n!⌉`. (Model: `docs/problem.md`; `SoringP1/Model.lean`;
`SoringP1/Minimax.lean`.)

`[literature]` Wells proved `S(12) > C(12)=29`, hence `S(12)=30` since
Ford–Johnson sorts 12 in 30 comparisons (Wells, IFIP Congress 1965/1966;
*Elements of Combinatorial Computing*, Pergamon 1971; reported by Peczarski
2012 and Stober–Weiß 2023). Stober–Weiß give a modern bidirectional exhaustive
search: for `n=12`, `E_tot=12!/2²⁹≈0.8922`, `sortable = no` at budget 29,
6190 posets stored, 152 ms total; Wells' one-sided forward exploration already
empties a level (Stober–Weiß, ALENEX 2023, DOI 10.1137/1.9781611977561.ch17,
Table 2 and text; preprint arXiv:2206.05597v2). Exact values are known for all
`n ≤ 22` and the last settled were `S(16)=46, S(17)=50, S(18)=54`
(Stober–Weiß 2023).

`[literature]` The gap is not unique to 12: `S(22)=71 > C(22)=70` (OEIS
A036604/A003070; also tabulated in project note
`docs/research-n12-nontightness.md`).

## 1. What would count as an explanation

A *generalizable finite/structural invariant* explaining the `+1` gap beyond
`log₂ e(P)` should, at minimum, be:

- **Sound as a lower bound or obstruction:** from the invariant's value/shape
  on `P` or on the `S(n)` family one can deduce `F(P) ≥ L0(P)+1` (or the
  corresponding root gap) by a finite, checkable argument, not by rerunning the
  full minimax search.
- **Stronger than `L0` where the gap occurs:** it must distinguish the
  obstructed case from cases where `L0` is tight.
- **Generalizable:** it applies to all relevant `n` or to an infinite family by
  a uniform rule, not as an ad hoc `n=12` certificate.

This excludes the full game value `F` itself (it is the target, not an
explanatory invariant) and excludes the exhaustive Wells/Stober–Weiß search as
stated (it certifies `S(12)>29` but is not a compact invariant; its bottleneck
posets are not published as a short structural object, `[deduction]` from
Stober–Weiß's account as analyzed in `docs/research-n12-nontightness.md` §4).

## 2. Candidate families

### 2.1 Leaf counting and equivalent efficiency pruning

`[definition]` Node-level leaf condition: a state reached after `c`
comparisons in a height-`h` tree must satisfy `e(P) ≤ 2^(h-c)`, equivalently
efficiency `E(P)=n!/(2^c e(P)) ≥ E_tot=n!/2^h`.

`[deduction]` The Wells/Peczarski/Stober–Weiß "efficiency" pruning is
definitionally equivalent to this node-level information bound, hence not a new
lower-bound invariant (Observation 2.2 in the efficiency form; argued in
`docs/research-n12-nontightness.md` §4, citing Peczarski 2012 and
Stober–Weiß 2023). It is useful search bookkeeping and cannot explain a gap
beyond `L0`.

### 2.2 Scalar invariants depending only on `e(P)` (including slack)

Candidates: slack ratio `2^{C(n)}/n!`, monotone functions of `e(P)`,
efficiency `E(P)`, or any invariant determined by `e(P)` alone.

`[experiment]`/`[deduction]` (project, `docs/research-n12-nontightness.md`):
- **H1 (slack ratio)** falsified: `n=5` has less slack than `n=12` yet is
  tight; `n=20` tight, `n=22` not, with no predictive threshold.
- **H2 (monotonicity in `e`)** falsified at `n=6`: 9960 labelled-poset pairs
  with `e(P1)<e(P2)` but `m(P1)>m(P2)`; smallest witness `e=13,m=5` vs
  `e=14,m=4`. Peczarski gives the same phenomenon at `n=13` (`P16`, `e=113400`
  sortable in 17, vs `Q'16`, `e=109350` not sortable in 17) `[literature,
  Peczarski 2012 §4]`.
- **Stronger same-`e` obstruction** `[experiment]`: at `n=5`, posets with the
  same `e=8` have `m=3` and `m=4`. Hanamura–Iwata (2011) show `e=7` posets are
  sortable in `⌈log₂7⌉=3`, so the local `e=8` failure is the first such
  boundary `[literature]`.

**No-go (scalar/`e`-only).** No invariant that is a function only of `e(P)`
(or of any quantity determined by `e(P)`: global slack, node efficiency at
fixed depth relative to `e`, etc.) can determine `F(P)` or explain the `n=12`
root gap, because `F` is not a function of `e` and not monotone in `e`. This is
a project deduction from the literature/experiment above, not a claim about the
full Wells search internals.

### 2.3 Forced-prefix / split-fraction signatures

`[deduction]`/`[experiment]` (H4, `docs/research-n12-nontightness.md`): at
budget 29, `n=12` forces early balanced splits (e.g. the depth-1 chain-free
2/3 split and later min–max cross-chain 5/6 are inadmissible by the node-level
bound), while equal-role chain comparisons may remain admissible. The same
*forced second-comparison* phenomenon occurs at tight `n=5,10`. Therefore a
forced-prefix signature is real but not a sound predictor of the global gap.

### 2.4 Symmetry

`[experiment]` (H6): locally loose posets with `|Aut|>1` exist at `n=6` (4680
among loose posets with `e ≤ 64`); symmetry is neither necessary nor
sufficient. Peczarski's remark that `P16` is sortable "because of its symmetry"
is an observation about that case, not a general invariant `[literature]`.

### 2.5 Compositional merge-factor / ordinal-sum bounds

`[deduction]`/`[experiment]` (`docs/research-structural-lower-bounds.md`): for
`P = ⊕_i P_i`, `F(P)=Σ F(P_i) ≥ Σ ⌈log₂ e(P_i)⌉ + Σ δ_i` with certified merge
gaps `δ_i` on merge factors. This is sound and strictly stronger than `L0` on
some non-root posets (smallest merge witness `Merge(2,4)`, `n=6`;
rounding-only witness at `n=7`).

**No-go for the root `n=12` obstruction.** The antichain `antichain_n` is a
single incomparability component with no certified merge-factor gap
(`δ=0` for that non-merge block in the stated rule), so Theorem B gives only
`≥ ⌈log₂ e(antichain_n)⌉ = C(n)`. It cannot explain `S(12)>29`.

### 2.6 One-ply and finite-depth adversarial information bounds

`[definition]`/`[deduction]` (`docs/research-one-ply-obstruction.md`): the
one-ply bound
`L1(P)=0` if total, else `1 + min_{(i,j)} max(L0(P+i<j), L0(P+j<i))`
satisfies `L0(P) ≤ L1(P) ≤ F(P)`. It is a sound, generalizable structural
strengthening of `L0` and has strict witnesses at every size `n ≥ 5` (the
`e=8` witness `W`, extended by ordinal sums). A safe budgeted-pruning
corollary strengthens `e(P)>2^d`.

**Status on `n=12`.** `L1` is *not demonstrated* to explain the antichain gap:
`docs/research-one-ply-obstruction.md` explicitly does not prove `S(12)=30` or
compute `L1(antichain₁₂)`. Computing `L1(antichain₁₂)` requires, for candidate
first comparisons, the partition sizes / `L0` of children of the 12-key
antichain — far beyond the note's small checks. Thus `L1` is a generalizable
*sound family member* but not a verified explanation of this obstruction.

**No-go (known/verified finite-depth local explanation).** No fixed finite
lookahead bound `Lk` (with `L0` leaves, `L0 ≤ ⋯ ≤ Lk ≤ F`) is verified to give
`Lk(antichain₁₂) ≥ 30`. Moreover, the Wells/Stober–Weiß certification of
`S(12)>29` is strategic/global: the one-sided exploration reaches deep levels
before emptying (Wells reported `S_24` empty for `n=12`, per Peczarski 2012 as
extracted in the project note; the full modern search stores thousands of
posets) `[literature]`. A fixed small `k` independent of the obstruction depth
has no known argument capturing that global routing, while `k` large enough to
coincide with `F` is the exhaustive minimax value, not a compact invariant.
`[conjecture, scoped]`: fixed-depth local `Lk` families are unlikely to yield a
compact explanation of the `n=12` root gap, but this is not a theorem here
(absence of a verified proof/certificate, not impossibility).

### 2.7 Human-readable / compact certificate

`[literature]`/`[deduction]` No short closed-form invariant or compact
checkable certificate for `S(12)>29` is known; Wells' and later proofs are
exhaustive poset searches (`docs/research-n12-nontightness.md` §§4,8,10;
Stober–Weiß 2023). A compact certificate would itself be the requested
invariant; none is available.

## 3. Precise no-go summary

For the stated candidate classes, the following are established by the cited
sources and project deductions/experiments:

1. **`e`-scalar class** (`I(P)=g(e(P))`, including slack/efficiency-as-scalar-of-
   `e`): cannot determine `F(P)` or predict the gap (same `e`, different `m`;
   non-monotone in `e`) — *ruled out* as an explanation `[literature,
   Peczarski; Hanamura–Iwata]` + `[experiment]`.
2. **Efficiency-pruning class (Wells/Peczarski/Stober–Weiß heuristic form):**
   equivalent to node-level `L0` — *not stronger than* `L0` `[deduction]`.
3. **Forced-prefix/split-fraction class:** occurs at tight `n` values — *not a
   sound global predictor* `[experiment]`.
4. **Symmetry class (`|Aut(P)|`):** neither necessary nor sufficient —
   *ruled out* `[experiment]`.
5. **Compositional merge/ordinal-sum class (Theorem B as stated):** gives no
   strengthening on `antichain_n` — *cannot explain the root `n=12` gap*
   `[deduction]`.
6. **One-ply `L1` / finite-depth `Lk`:** sound and generalizable, but *no
   verified instance explains* `S(12)>29`; fixed small `k` has no known
   compact argument for the deep strategic obstruction — *unverified / not known
   to generalize to this root gap* `[deduction]` + `[literature context]`.

## 4. Assessment

The `n=12` obstruction is real (`[literature]`, Wells; Stober–Weiß), global and
strategic: local/node-level information conditions and all examined scalar or
purely local structural surrogates fail to explain it, while the only known
certifications are exhaustive searches. Generalizable sound bounds stronger
than `L0` exist (`L1`, `Lk`, compositional bounds on factorizable posets), but
they either do not apply to the antichain root or are not verified/compact
enough to explain `S(12)>29`. Therefore the requested object — a generalizable
finite/structural invariant that *predicts/explains* the `n=12` `+1` gap beyond
`log₂ e(P)` — is **not known**. A precise no-go holds for the stated scalar,
efficiency-as-invariant, forced-prefix-predictor, symmetry, and root-applicable
compositional classes above; the finite-depth lookahead family remains sound but
unresolved as an explanation of this specific obstruction.

## 5. What would change the conclusion

- A proof or verified computation that `Lk(antichain₁₂) ≥ 30` for some stated
  finite `k` (or a stronger sound invariant), with a complexity/cost analysis
  honest about `#P`/enumeration costs, would supply a generalizable sound bound;
  it would count as an explanation only if accompanied by a compact structural
  reason, not merely an expensive computation.
- A compact, independently checkable certificate extracted from (or replacing)
  the Wells/Stober–Weiß search.
- A new invariant that is non-scalar and strategic (trackable over the whole
  decision tree) yet checkable in substantially less than exhaustive minimax
  time, proved sound on an infinite family containing `n=12`.

## 6. Sources

Primary / external:
1. M. Wells, *Applications of a language for computing in combinatorics*,
   Information Processing 65 (Proc. IFIP Congress 1965), 497–498, 1966.
2. M. Wells, *Elements of Combinatorial Computing*, Pergamon, Oxford, 1971.
3. L. R. Ford Jr., S. M. Johnson, *A Tournament Problem*, Amer. Math. Monthly
   66 (1959), 387–389.
4. M. Peczarski, *Towards optimal sorting of 16 elements*, Acta Univ.
   Sapientiae Informatica 4(2) (2012), 215–224.
5. F. Stober, A. Weiss, *Lower Bounds for Sorting 16, 17, and 18 Elements*,
   ALENEX 2023, 201–213, DOI 10.1137/1.9781611977561.ch17; arXiv:2206.05597v2.
6. N. Hanamura, S. Iwata, *Posets with seven linear extensions sortable by three
   comparisons*, Inform. Process. Lett. 111(8) (2011), 365–369,
   doi:10.1016/j.ipl.2011.01.004.
7. OEIS A036604, A003070 (index values only; not primary proofs).

Project sources (internal evidence used above):
8. `docs/problem.md`, `docs/research-plan.md`, `docs/literature.md`.
9. `docs/research-n12-nontightness.md` (scalar/monotonicity/symmetry/prefix
   experiments and deductions; Peczarski `P16/Q'16` discussion).
10. `docs/research-structural-lower-bounds.md` (merge-factor/compositional
    bound; `Merge(2,4)` witness; root non-applicability).
11. `docs/research-one-ply-obstruction.md` and
    `scripts/one_ply_obstruction.py` (sound `L1`, `L0 ≤ L1 ≤ F`, strict witness
    family; no `n=12` antichain computation).

Programmatic checks referenced by project notes: `python3 scripts/evaluate.py`,
`python3 scripts/nontightness_experiments.py`, `python3
scripts/structural_lower_bounds.py`, `python3 scripts/one_ply_obstruction.py`.
