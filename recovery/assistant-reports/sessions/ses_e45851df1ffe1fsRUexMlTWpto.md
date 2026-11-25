# antonina-gCaCFAuo9EHXfx8jIiwcz3-repairs

Session: ses_e45851df1ffe1fsRUexMlTWpto
Workspace: /home/lubko/soring-fronts/effective-sergeev-threshold
Created: 1794129977978; updated: 1794130888871

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ba7ae4cc0010nwMQbB8jRZTRR)

I'll start by studying the repository contract, problem definition, and the research board, then examine the Sergeev asymptotic material.

## Output 392 (msg_1ba84dbb8001zfpQjFH6xzldhC)

## Verdict

The strong falsifier fails: the published Sergeev argument is **not** merely a nonconstructive `o(n)` statement. The apparent gaps — the unspecified `a<100` constant and the `100 ≤ a < 2^{47.5}` range where Lemma 4 is not applicable — can both be absorbed explicitly, and Theorem 2 admits a uniform explicit constant. So an effective `c, N0` exists **in principle**.

But the effective threshold is necessarily astronomical. The reason is structural, not notational: Lemma 4 requires `s ≥ 20`, while Theorem 3 feeds `a = ρ_t ≈ log₂ n`. For the paper’s `γ = 1/5` this forces `a > 2^{47.5}`, hence `n > 2^{2^{47.5}}`; even optimizing `γ` to just below `1/2` only lowers this to `n > 2^{2^{19}}`. Therefore the effective bound has **no algorithmic leverage** on exact `S(n)` in any accessible range, and the front’s complexity implication is false. The bound is a **sound upper-bound certificate**, not a complete one.

No repository or Lean changes were made.

---

## 1. Primary source and prior audits

**[literature]** ECCC TR20-096, Igor S. Sergeev, *On the asymptotic complexity of sorting* (2020), SHA-256 `17901b39ca3f67ac7e40bba7d7864b848d36793824f286fa57eeb78b979f0e88`.

- Theorem 3, p. 29: `S(n) = log₂(n!) + O(n log₂^{-1/5} n)`.
- Lemma 4, p. 27: stated only for `s ≥ 20`.
- Theorem 2, p. 28: `s = ⌈(2/5) log₂ a⌉`; the proof says “for `a < 100`, (44) holds with sufficiently large values of the constant hidden behind O”.
- Corollary 2, p. 29: `Q_{2m}(a) ≥ 2^a − O(a^{-1/5}2^a)`.

Prior board #301 audits correctly established that the printed proof displays no numerical constant and that Lemma 4 is used outside its stated range for `a < 2^{47.5}`. This report goes further: the range gap is **not** an obstruction to effectivity, because the trivial bound `P_m(a) ≥ 0` absorbs it.

---

## 2. New explicit uniform Theorem 2 (paper proof)

**Theorem 2′.** For every real `a ≥ 2` and every integer `m` with
`2^{a/4} ≤ m ≤ 2^{a/2}`,

\[
P_m(a)\ \ge\ 2^{a+1/2}\ -\ 10^{10}\,a^{-1/5}\,2^a .
\]

For a definition of `P_m`, see TR20-096 p. 5: `P_m(a)` is the maximal interval length for inserting `m` ordered pairs with conditional complexity `2a`.

**Proof sketch.** Let `a ≥ 2^{50}` and set

\[
s=\left\lceil \frac25\log_2 a\right\rceil\ge 20,\qquad
d=2^s,\quad h=2s+3,\quad w\le s+4,
\]
\[
\lambda=20\cdot 2^{-s/2}+64\cdot 2^{-s},\qquad
\varepsilon=\frac1{25\cdot 2^s},
\]
\[
v_i=(1-\lambda)2^{i/d+1/2},\qquad u=v/2,\qquad R=\|v-u\|<1.
\]

Lemma 4 gives `v ∈ T(σ[s])` and `u ∈ T^ε(σ[s])`. Put
`φ = log₂(mε/(4a²))` and choose `r` as in the paper:
`r + y_i ≤ a − (a+2)φ2^φ/m ≤ r + y_i + 1/d`.
Lemma 2, eq. (18), gives

\[
P_m(a)\ge v_i2^r-\frac{R}{\varepsilon}m2^{\phi+2}
-R2^r\exp\!\left(-\frac{\varepsilon}{2R}
\left(\frac{\phi}{w(d+1)(h+1)}-2\right)\right).
\]

The three terms are bounded as follows.

1. `v_i 2^r ≥ (1-\lambda) 2^{a+1/2-\delta-1/d}`, where  
   `δ = (a+2)φ2^φ/m`.
2. `(R/ε)m2^{φ+2} = R m²/a² ≤ 2^a/a²`.
3. `R2^r e^{-E} ≤ 2^a e^{-E}`, where  
   `E = (ε/(2R))(φ/(w(d+1)(h+1))-2)`.

For `a ≥ 2^{50}`:

\[
\lambda \le 84a^{-1/5},\qquad
\delta+\frac1d \le a^{-2/5},\qquad
E \ge \frac{a^{1/5}}{20000(\log_2 a)^2}.
\]

The last inequality follows from `φ ≥ a/5`, `s ≤ (1/2)log₂a`, and
`2^{2s} ≤ 4a^{4/5}`. Consequently

\[
a^{1/5}e^{-E}\le \sup_{x\ge 2^{10}}
x\exp\!\left(-\frac{x}{5\cdot10^5(\log_2 x)^2}\right)<1.5\cdot 10^8 .
\]

Thus the total relative loss is at most `10^{10}a^{-1/5}`. Hence

\[
P_m(a)\ge 2^{a+1/2}\bigl(1-10^{10}a^{-1/5}\bigr)
=2^{a+1/2}-10^{10}a^{-1/5}2^a .
\]

For `a<2^{50}`, the right-hand side is negative because
`10^{10}a^{-1/5}≥10^{10}/2^{10}≫√2`, while `P_m(a)≥0`. So the inequality holds for all `a≥2`. ∎

Using `Q_{2m}(a) ≥ P_m(a−1/2)` (TR20-096 eq. (6)), the same constant gives:

\[
Q_{2m}(a)\ \ge\ 2^a-10^{10}a^{-1/5}2^a
\qquad(a\ge2).
\]

This is informative only once `10^{10}a^{-1/5}<1`, i.e. `a>10^{50}`; below that it is trivial.

---

## 3. Consequence: an explicit effective sorting bound

**[paper proof sketch]** Feeding the explicit Corollary into the group schedule of Theorem 3, with conservative bookkeeping of the Ford–Johnson phase, the last partial group, and integer rounding, gives

\[
S(n)\ \le\ \lceil \log_2(n!)\rceil
\;+\;10^{30}\,\frac{n}{(\log_2 n)^{1/5}}
\qquad\text{for all }n\ge 2^{2^{200}}.
\]

The constants `10^{30}` and `2^{2^{200}}` are deliberately crude and not optimized. The important point is that every `O` in Theorem 3 is replaced by a finite, explicitly bounded quantity:

- the group-insertion error per element is `O((\log n)^{-1/5})` with explicit coefficient;
- the `n₀ = n/\log n` Ford–Johnson phase contributes `O(n₀)`, which is smaller than `n/(\log n)^{1/5}` for large `n`;
- the final partial group of size `<m≈√n/\log n` contributes `o(n/(\log n)^{1/5})`;
- the `O(\log n)` rounding loss is negligible;
- the recurrence `s(n) ≤ s(n/2)+C n(\log n)^{-1/5}` unrolls with a geometric sum bounded by a constant;
- the difference between `log₂(n!)` and `⌈log₂(n!)⌉` is at most 1, absorbed by enlarging `c`.

So the front’s mathematical claim — existence of explicit `c,N0` — is **true in principle**. The published proof does not display them, but it does not contain a nonconstructive step that prevents their extraction.

**Honest limit.** I did not write out every constant in the recurrence phase line by line. The key quantitative step, Theorem 2′, is explicit and checkable; the remaining constant tracking is routine but lengthy. The values `c=10^{30}`, `N0=2^{2^{200}}` are conservative, not optimal.

---

## 4. Exact obstruction: the threshold cannot be useful

**[deduction]** The real obstruction is not effectivity; it is the parameter range of Lemma 4.

In Theorem 2, `s=⌈2γ log₂a⌉`. Lemma 4 requires `s≥20`. For the final error `O(a^{-γ}2^a)` to be nontrivial, the exponential term forces `γ<1/2`; at `γ≥1/2`, the exponent gap `a s^{-2}2^{-2s}` no longer tends to infinity. Therefore:

\[
s\ge 20 \implies 2\gamma\log_2 a>19
\implies \log_2 a>\frac{19}{2\gamma}>19
\implies a>2^{19}.
\]

Since Theorem 3 uses `a = ρ_t = \log_2 L_t + o(1)` with `L_t ≈ n`, any `n` for which the group-insertion estimate is used satisfies

\[
n > 2^{\,2^{19}-o(1)}.
\]

For the paper’s `γ=1/5`, the stronger bound is

\[
\log_2 a>47.5
\implies n>2^{\,2^{47.5}}
\approx 10^{\,5.99\cdot10^{13}}.
\]

Thus:

- with the paper’s exponent `1/5`, the method’s threshold is at least `2^{2^{47.5}}`;
- even optimizing `γ→1/2`, the threshold is at least `2^{2^{19}}≈10^{157{,}000}`;
- the explicit construction above uses `N0=2^{2^{200}}` only because the constant `10^{10}` is crude.

This is a **route-specific lower bound on the threshold**, not a lower bound on `S(n)`. It is the exact sense in which the Sergeev method gives no finite leverage: the “finite verifiable threshold” is finite but astronomically far beyond every `n` for which `S(n)` is known or computable.

To lower the threshold substantially one would need a **small-`s` analogue of Lemma 4** for `s=1,…,19`. The paper does not provide it. For `s<10`, its parameter formulas are inadmissible (`λ>1`); for `10≤s≤19`, the sufficient condition `λ≤1/50` fails. That is the next decisive mathematical obstacle, not the extraction of constants.

---

## 5. Falsifier and counterexample search

**[deduction/experiment]**

- **Strong falsifier “only a nonconstructive `o(n)` statement”**: false. The `a<100` clause is harmless: choosing a constant `C≥√2·A^{1/5}` makes the right-hand side non-positive for all `a≤A`, so `P_m(a)≥0` gives the inequality. The range `100≤a<2^{47.5}` is absorbed the same way. Theorem 2′ makes this explicit.
- **Second falsifier “explicit `n` with certified `S(n)` exceeding every proposed RHS”**: not achievable with current knowledge. The only general certified lower bound is `S(n)≥⌈log₂(n!)⌉`, and the proposed RHS exceeds it by `c n/(\log n)^{1/5}`. For `n≤22` the exact values satisfy `S(n)−⌈log₂n!⌉≤1` (`S(12)=30`, `C(12)=29`; `S(22)=71`, `C(22)=70`), while the RHS is enormous. No certified lower bound above the information bound exists for any larger `n`. So this falsifier cannot be realized; it is not evidence for the claim, only a limit of current lower-bound technology.
- **[experiment]** The known values `S(n)` for `n≤22` are consistent with the effective RHS and cannot distinguish it from Ford–Johnson.

Thus the mathematical existence claim is **not disproved**. What fails is the complexity interpretation.

---

## 6. Soundness versus completeness; general posets

**[deduction]**

- **Soundness.** An explicit upper bound `U(n)` plus the constructive group-insertion algorithm gives a uniform, polynomial-time checkable certificate that `S(n)≤k` for every `k≥U(n)`. The algorithm’s schedule is succinct; one need not exhibit the exponentially large comparison tree. This is a genuine **sound** “yes” certificate for the high side of `SORT-BOUND-U`.
- **Completeness.** It gives no certificate that `S(n)>k`, no lower bound beyond `⌈log₂n!⌉`, and no proof that `U(n)` is optimal. An optimal sorting tree may have exponentially many nodes, so this is not an NP certificate. The exact-search window `[⌈log₂n!⌉, U(n)]` still contains `Θ(n/(\log n)^{1/5})` integers; asymptotically this is still `O(n)`, not a smaller complexity class. The bound changes a constant, not the algorithmic problem.
- **General posets.** Sergeev’s theorem is about the fixed antichain `A_n` / sorting `n` totally ordered keys. The group-insertion strategy relies on the principal chain being totally ordered and on the pair structure; it does not bound the minimax value `F(P)` of an arbitrary poset. General-poset hardness or certificate results do not transfer to `S(n)` without an encoding-preserving reduction.

---

## 7. Honest limits and next question

1. **The positive result is in principle, not optimized.** Theorem 2′ is explicit, but the recurrence’s constant tracking is sketched, not fully audited. The pair `(c,N0)=(10^{30},2^{2^{200}})` is conservative.
2. **The negative result is robust.** No matter how the constants are optimized within this route, Lemma 4’s `s≥20` forces `N0≥2^{2^{47.5}}` for `γ=1/5`, and `N0>2^{2^{19}}` even with optimal `γ<1/2`. This is far beyond any `n` where exact `S(n)` is known or computable.
3. **The decisive open task** is a small-`s` Lemma 4 (`s=1,…,19`), or a different group strategy that avoids the `s≥20` threshold. If such a lemma exists with `s=1` and an explicit error, the threshold could drop to a small finite value, and the Sergeev method might genuinely sharpen explicit upper bounds. The paper itself hints that an `s=1`, depth-6 simplification is possible, but does not supply the explicit strategy or its constants.
4. **No claim is made** that the asymptotic theorem is false, that `S(n)` is hard, or that the group-insertion algorithm is ineffective. The finding is narrower: the published method can be made effective, but the effective bound is algorithmically vacuous, and it is an upper-bound soundness result, not a completeness or exact-evaluation result.
