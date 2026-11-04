# Increment/zone gating for information-bound tightness (front: information-tightness-infrequently)

Question (front): does there exist an infinite sequence `n_i → ∞` with
`S(n_i) = ⌈log₂ n_i!⌉`, or is equality achieved only finitely often?

This note applies the **exp/increment machinery of the excess** to the real
sorting number, in contrast to the equal-purpose construction of
`docs/research-encoding-consequences.md` Theorem 6.6 (which uses the same
arithmetic indicator only for an artificial function `G`). Prior fronts on
the same question (`info-bound-tightness-infinite`, `inf-eq-info-bound-alln`,
`equality-set-infinite-alln`, `fredman-additive-exact-regime`; frontier
ledger, all `clearexit`, all open) catalogued the literature and small-n
behavior but none established the move-gating theorems below.

Status labels follow AGENTS.md. All computations cited are exact-integer
where noted (factorial `bit_length` for `⌈log₂ n!⌉`, exact fractional
comparisons), scripts in `/tmp/opencode/tight/` session log; margins exceed
`10⁻⁶` in every float bound used.

## 0. Definitions

- `C(n) = ⌈log₂ n!⌉` (information bound; kernel-checked as the lower bound).
- Excess `g(n) = S(n) − C(n) ≥ 0`.
- Increment `d(n) = S(n) − S(n−1)`.
- C-increment `Δ(n) = C(n) − C(n−1) = ⌈log₂ n!⌉ − ⌈log₂ (n−1)!⌉`.
- Window value `M(n) = ⌈log₂ n⌉`.
- **Zone** of step `m` (m ≥ 4): **cheap** if `Δ(m) = M(m) − 1`,
  **expensive** if `Δ(m) = M(m)`.
- **Beat** at `n`: `d(n) < M(n)` (the optimal increment strictly beats the
  sort-(n−1)-then-binary-insert two-phase increment).

Verified exact data for `n ≤ 22` (sources: Peczarski 2012 `S(n)` for
`n ≤ 16`; Stober–Weiß ALENEX 2023 for `16–18`; `S(19)−S(22)` per Knuth
errata/OEIS A036604, cross-read with `docs/research-n12-nontightness.md`):

| n | S | C | g | d | Δ | zone | beat |
|---|---|---|---|---|---|---|---|
| 12 | 30 | 29 | 1 | 4 | 3 | cheap | no |
| 17–19 | 50/54/58 | 49/53/57 | 1 | 4 | 4 | cheap | yes |
| 20 | 62 | 62 | 0 | 4 | 5 | expensive | yes |
| 21 | 66 | 66 | 0 | 4 | 4 | cheap | yes |
| 22 | 71 | 70 | 1 | 5 | 4 | cheap | no |

Full table in the session log; all rows re-derived here from exact
integer factorials. Equality holds exactly for `n ∈ {0..11, 20, 21}`;
`g = 1` at `12–19` and `22`; `g(23)` unknown (`S(23)` open).

## 1. Zone lemma (arithmetic, proved, exactly verified to n = 4000)

**Lemma Z.** For `m ≥ 4`:

```
Δ(m) = M(m) − 1  ⟺  m is not a power of two  and  {log₂ (m−1)!} + {log₂ m} < 1,
Δ(m) = M(m)      otherwise (in particular at every power of two).
```

*Proof.* Write `a = log₂ (m−1)!`, `b = log₂ m`, fracs `α ∈ (0,1)`, `β ∈ (0,1)`
(nonzero for `m ≥ 4` because `(m−1)!` has an odd factor ≥ 3, so `a` is never
an integer, and `b` is not an integer off powers of two). Then
`⌈a+b⌉ = ⌈a⌉ + ⌈b⌉ − ⌊α+β⌋`, since `α+β ≠ 1` can only fail when
`(m−1)!·m = m!` is a power of two, i.e. `m ≤ 2`. `[deduction]`

The two exceptions are `m ∈ {2,3}` (`2! = 2` is a power of two). Zones have
empirical densities ≈ 0.522 (cheap) / 0.478 (expensive) for `m ≤ 2·10⁵`
[float census; powers of two counted expensive].

## 2. Move decomposition (model, proved)

**Lemma I (two-phase).** `d(n) ≤ M(n)` for all `n ≥ 2`: sort `n−1` keys
optimally, then locate the last key among `n` slots by binary search in
`⌈log₂ n⌉` comparisons. `[deduction]` (standard; sibling of the
kernel-checked `S_le_tight`.)

**Theorem R1 (move identity and rise gate).** For every `n ≥ 2` the excess
moves by `g(n) − g(n−1) = d(n) − Δ(n)`; hence

```
g(n) − g(n−1) ≤ 1,
and equality (+1) requires cheap(n) with d(n) = M(n).
```

In particular **the excess can rise only at cheap fractional zones**.

**Theorem R2 (drop gate).** If `g(n) < g(n−1)` then
`d(n) ≤ M(n) − 1`, i.e. step `n` is a beat. *Proof:* `d − Δ < 0 ≤ M − Δ
requires Δ(n) = M(n)` and `d < Δ ≤ M(n)`. `[deduction]`

**Theorem R3 (power-of-two rigidity).** `g(2^k) ≤ g(2^k − 1)` for all
`k ≥ 1`: at `m = 2^k`, `Δ(m) = k = M(m)` and `d(m) ≤ M(m)` force a
non-positive move. `[deduction]` Consistent: `g(8)=g(7)=0`, `g(16)=g(15)=1`
(descent verified numerically `n ≤ 22`: every known ±1 move occurs exactly
in the gated zone with the gated increment type).

## 3. Consequence ONE: E is eventually all-or-nothing when beats stop

Let `E = {n : g(n) = 0}` (the tight set; the front's object). Theorems R1/R2
give immediately:

**Rigidity corollary.** If `d(n) = M(n)` for all `n ≥ N` (no beats ever
again), then `E ∩ [N, ∞)` is either empty or all of `[N, ∞)`. *Proof:* moves
`g(n) − g(n−1) ∈ {0, +1}` with `+1` only at cheap zones; `g` is
nondecreasing from `N` on, so once positive it never returns to 0.
`[deduction]`

So the front's finiteness question **reduces to the asymptotics of beats**:

- **E infinite** requires either one final infinite tight run
  (`g ≡ 0` eventually), or infinitely many steps that are simultaneously a
  **beat** and an **expensive-zone** step (c.str. Theorem R2).
- Conversely no known obstacle prevents that; beats are empirically
  frequent (8 of 21 known steps `n ≤ 22`), and cheap/expensive zones both
  have density ≈ ½, so the coincidence class is not arithmetically thin.
  Under independence heuristics `E` is expected infinite; this is evidence,
  not a result.

## 4. Conjecture W (one-bit increment window) and its exact bookkeeping

**Conjecture W.** For every `n ≥ 2`: `d(n) ∈ {M(n) − 1, M(n)}`
(equivalently `d(n) ≥ ⌈log₂ n⌉ − 1`). Verified for **all 21 known increments
`n ≤ 22`** (equality `d = M − 1` exactly at `n ∈ {5, 9, 10, 17, 18, 19, 20,
21}`, i.e. every beat is a one-bit beat). No primary source found for the
all-n statement in the surveyed literature (Ford–Johnson analyses, Knuth
5.3.1, Fredman 1976, Sergeev TR20-096, Stober–Weiß supply upper bounds and
asymptotics, not this inequality). Falsifier: exhibit any `n` with
`S(n) ≤ S(n−1) + ⌈log₂ n⌉ − 2`.

**Theorem B (exact beat accounting, conditional on W; exactly verified on
all known data `n ≤ 22`).** Under Conjecture W, for every `N ≥ 2`:

```
# beats in [2..N]  =  τ(N) :=  Σ_{m=2}^{N} ⌈log₂ m⌉ − S(N).
```

*Proof.* `d(m) = M(m) − beat(m)` elementwise; telescoping `Σ d(m) = S(N)`
and comparing with `Σ⌈log₂ m⌉` gives the identity. Equivalently
`τ(N) = Σ(⌈log₂ m⌉ − log₂ m) − g(N) − (C(N) − log₂ N!)`, with
`0 < C(N) − log₂ N! < 1`. `[deduction under W; verified exactly]`

This makes the ledger's aggregate quantity `τ(n) = Σ_{j≤n} ⌈log₂ j⌉ − S(n)`
(previously used only as an Ω(n) counting gadget in
`research-time-exponent.md` / Theorem 6.6) an **exact beat census**: the
front's question becomes, under W,

> **E infinite ⟺ `# beats(≤n) = ⌊Σ_{m≤n} (⌈log₂ m⌉ − log₂ m)⌋` for
> infinitely many n** (the beat count hugging the Σw staircase),

because `g(n) = Σw(≤n) − τ(n) − res(n)` with `res ∈ (0,1)` forces
`g(n) = 0 ⟺ τ(n) = ⌊Σw(≤n)⌋`. Every quantity except `S` (hence except
`τ`) is pure arithmetic, computable to any precision.

## 5. Sharp prediction at the next open value n = 23

Zone(23) is expensive (exact: `Δ(23) = 5 = M(23) = 5`, from
`C(23) = 75`, `C(22) = 70`), so Theorem R2 permits a drop there, and:

```
g(23) = 1 + d(23) − 5 ∈ {0, 1}     under Conjecture W (d(23) ∈ {4,5}),
S(23) = 75  ⟺  d(23) = 4  ⟺  beat at 23,
S(23) = 76  ⟺  d(23) = 5.
```

The beat census is consistent with both branches (predicted `#beats ≤ 23`
is 9 iff `g(23) = 0`, 8 iff `g(23) = 1`). So the first open tightness
instance is exactly a first-beat question at `n = 23` — same shape as the
resolved `d(2^k) = k` situation at powers of two, but on the expensive
side. No computation in this repository settles `d(23)`; exhaustive search
at `n = 23` is beyond current technique (Stober–Weiß scale per value).

## 6. Reading of the evidence (honest status)

- **No all-n result either way on the front's question.** What is new and
  proved: the zone characterization (Lemma Z), the rise gate (R1), the
  drop⇒beat gate (R2), the power-of-two no-rise theorem (R3), and the
  eventual all-or-nothing rigidity (Corollary in §3).
- What is new and conditional: Theorem B (exact beat census) under W, plus
  the E-staircase reformulation, plus the `n = 23` branch structure.
- Negative outcome preserved: the "eventually no beats" hypothesis — which
  would settle the front by the rigidity corollary plus the known `g(22)=1`
  — is not supported by any known construction (Ford–Johnson-type
  increments historically beat two-phase at `n = 5, 9, 10, 17–21`; Sergeev
  gives only `o(n)` aggregate excess, which permits but does not force
  beat extinction).

## 7. Next best untried attacks (precise)

1. **Prove Conjecture W** (`d(n) ≥ ⌈log₂ n⌉ − 1`). Paper argument outline
   not previously attempted in the ledger: fix the distinguished key
   among any pairwise-comparison transcript; non-distinguished-key
   comparison outcomes depend only on the other keys' order σ, so
   distinguishing the `n` slots of the distinguished key needs a
   slot-separating comparison structure; the classical "−1" saving comes
   from the two extreme slots sharing one comparison which also resolves
   an adjacent pair of σ. Formalizing this yields W; it would turn all of
   §4 unconditional and give `g` moves exactly `{−1, 0, +1}`.
2. **Fractional-part analysis of `{log₂ n!}`.** The expensive-entry
   windows are `{n : {log₂ (n−1)!} + {log₂ n} > 1} ∪ {2^k}`; equidistribution
   (or any density statement) of `{log₂ n!}` mod 1 is a standalone
   arithmetic subquestion, apparently unpublished. Any effective density
   bounds, combined with W and beat-extinction results, bound how often
   tightness can be *entered*.
3. **Beat persistence via constructions.** Exhibit an all-n family where
   `d(n) = ⌈log₂ n⌉ − 1` for infinitely many n with the expensive zone —
   e.g. checking whether Ford–Johnson/merge-insertion increments match
   `M − 1` precisely on Sergeev's group boundaries. A constructive infinite
   beat∧expensive family plus a forcing argument up the tree would build
   an infinite-tightness candidate construction (the front's positive arm).
4. **Beat extinction via lower bounds.** Prove `d(n) = ⌈log₂ n⌉` for all
   sufficiently large `n` — by the rigidity corollary this would collapse
   the front to a dichotomy decidable by `g`'s behavior up to the plateau;
   no known technique supports it (Wells/12–19 gaps punched through dyadic
   blocks), listed for completeness as the extinction arm.

## Sources

- Peczarski, *Towards optimal sorting of 16 elements*, Acta Univ. Sapientiae
  Inform. 4(2) (2012) 215–224 (exact values, `S(15)`, S(22) per errata chain).
- Stober–Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements*, ALENEX
  2023, SIAM, pp. 201–213 (exact `S(16)–S(18)`; efficiency-pruning method).
- Knuth, TAOCP Vol. 3, §5.3.1; *Selected Papers on the Analysis of
  Algorithms* errata, p. 500 (`n ≤ 22` exact, `n = 23` open).
- OEIS A036604 (sorting-number sequence, cross-check of the value table).
- Fredman 1976 (IPL 6, doi:10.1016/0020-0190(76)90095-8) and Sergeev,
  ECCC TR20-096 (excess asymptotics; used only as context, no additive
  constants extracted).
- Repository: `docs/research-n12-nontightness.md` (tightness table n ≤ 22),
  `docs/research-encoding-consequences.md` Thm 6.6 (the same Δ-window and
  `Σ⌈log₂ j⌉` telescoping, for an artificial `G`), frontier ledger fronts
  `info-bound-tightness-infinite`, `inf-eq-info-bound-alln`,
  `equality-set-infinite-alln` (status: investigated/open, no gating
  theorems previously recorded).
