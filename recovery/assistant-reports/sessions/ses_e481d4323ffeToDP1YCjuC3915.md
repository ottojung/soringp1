# antonina-Q3fjMbn4ZpOrCdH7sneWlV-sour

Session: ses_e481d4323ffeToDP1YCjuC3915
Workspace: /home/lubko/soring-fronts/exec-sergeev-finite-bound-20261107
Created: 1794086452530; updated: 1794086844634

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 56 (msg_1b7e31144001D38x4UEliF12lZ)

**Stopped: the primary source could not be accessed in this environment.** I can’t responsibly derive constants or identify an exact non-effective step without reading the proof.

I read `AGENTS.md`, `docs/research-plan.md`, and `docs/research-sergeev-asymptotic.md`. The research note identifies Theorem 3 on page 29 of Sergeev’s ECCC TR20-096 and records only the asymptotic bound \(S(n)=\log_2(n!)+O(n/(\log n)^{1/5})\); it explicitly cautions that the big-O does not give usable constants.

Access attempts:
- The ECCC report page loaded and confirmed the report title, author, and abstract: https://eccc.weizmann.ac.il/report/2020/096/
- The linked PDF endpoint, https://eccc.weizmann.ac.il/report/2020/096/download, was rejected by the fetch tool as PDF content.
- A direct `curl` download failed with “Connection reset by peer.”
- Web search was cancelled.

No derivation, code, Lean, or repository edits were made. **Evidence is insufficient to conclude that the proof is non-effective**; the requested analysis remains blocked pending access to the PDF or source.

## Output 268 (msg_1b7e82d2d001AZu8re4k0sZg29)

## Continuity / side-effect check

- Worktree `/home/lubko/soring-fronts/exec-sergeev-finite-bound-20261107` is clean; HEAD is detached at `c865b23`. No commits, branches, posts, or file edits from the interrupted turn.
- The previous turn’s only external action was an attempted ECCC download; `curl` failed with “Connection reset by peer,” so no file was written. Nothing needs to be de-duplicated.
- The primary source is in fact available locally, contrary to the previous turn’s “inaccessible” conclusion: `/var/lib/lubko/wd/viche-state/executive/sergeev-eccc-tr20-096.pdf` and `/tmp/opencode/sergeev.pdf`, both SHA-256 `17901b39ca3f67ac7e40bba7d7864b848d36793824f286fa57eeb78b979f0e88`; text extraction at `/tmp/opencode/sergeev.txt`. I resumed from that copy.

## Bottom line

**There is no ineffective step.** The TR20-096 proof is constructive: the strategy, the vectors `v,u`, the parameter values, and Lemma 2’s inequality are all explicit. The paper nevertheless does **not** yield an explicit finite `U(n)` as written, for two separate reasons:

1. **A finite range gap in the written proof.** Lemma 4 is proved only for `s ≥ 20` (p. 27). Theorem 2 sets `s = ⌈(2/5) log₂ a⌉` (p. 28), so `s ≥ 20` only when `a > 2^{47.5} ≈ 1.99·10^{14}`. The range `100 ≤ a < 2^{47.5}` is unsupported. Hence Corollary 2’s statement “for any `a ≥ 2`” is stronger than what the proof gives.
2. **Unextracted constants.** Theorem 2 (eq. (44), p. 28) and Theorem 3 (p. 29) contain unquantified `O` constants. They are recoverable in principle from Lemma 2, but the paper does not recover them, and without them no numerical `B(n)` can be written.

So the exact missing lemma is: **Lemma 4, or an equivalent strategy estimate, for `s = 3,…,19`**. For `s = 3,…,9` the paper’s own parameter formulas are not even admissible (`λ > 1`); for `s = 10,…,19` they are admissible but the crucial `λ ≤ 1/50` condition fails until `s = 20`. This is finite, not ineffective; but it is genuinely absent.

## 1. What is explicit in the proof

All of the following are stated explicitly:

| object | value | location |
|---|---|---|
| `s` | integer; Lemma 4 requires `s ≥ 20` | p. 27 |
| `d` | `2s` | p. 27 |
| `µ` | `30·2^{-s}` | p. 25, eq. (40) |
| `λ` | `20·2^{-s/2} + 64·2^{-s}` | p. 25 |
| `δ` | `2^{-s}` | p. 25 |
| `ε` | `1/(25·2^s)` | p. 27 |
| `b = |I₀|/|I₁|` | `(2√2+1)/4 ≈ 0.9571` | p. 18 |
| `γ` | `1/5` | p. 28 |
| `φ` | `log₂(mε/(4a²))` | p. 28 |
| `n₀` | `n/log n` | p. 29 |
| group size | `m ≈ √n/log n` | p. 29 |
| `L_t` | `2(n₀+tm) − m` | p. 29 |
| `ρ_t` | `log₂ L_t + O(log^{-1/5} n)` | p. 29 |

Lemma 2 (p. 10, eq. (18)) is a fully explicit inequality once `v`, `u`, `ε`, `R=||v−u||`, `w`, `h`, `d` are fixed:

```text
P_m(r+y_i + (r+2)φ2^φ/m)
  ≥ v_i 2^r − (R/ε) m 2^{φ+2}
      − R 2^r exp(−(ε/(2R))(φ/(w(d+1)(h+1)) − 2)).
```

For `σ[s]`, `v_i = (1−λ)2^{y_i+1/2}` and `u = v/2`, so `R` is also explicit in `s`. The proof of Lemma 4 (pp. 27–28) even lists the numerical reserves:

```text
(41′) gap ≥ 1/(2^4·2^s)   > ε,
(42′) gap ≥ 1/(6·2^{s/2}) > ε,
(43′) gap ≥ ε = 1/(25·2^s).
```

Thus, modulo algebra, everything above `s ≥ 20` is effective.

## 2. The exact range gap

Lemma 4 is stated only for `s ≥ 20`. The binding constraint is `λ ≤ 1/50`, used to secure (35) on p. 23. Numerically:

```text
s = 19:  λ = 0.0277434… > 1/50 = 0.02
s = 20:  λ = 0.0195923… < 1/50 = 0.02
```

The sufficient inequality (38) on p. 24 is actually satisfied at `s = 19` too with the paper’s `µ`, but (35) fails because `|J₁|/|J₂ˢ| > 2/(1−λ)` is not certified. At `s = 20` it holds only narrowly:

```text
s = 20:  lower bound 2.04481…  vs  required 2.03997…
```

For `s = 3,…,9` the formulas give `λ = 15.07, 9.0, 5.54, 3.5, 2.27, 1.5, 1.009`, all `> 1`, so the construction is not admissible. For `s = 10,…,19`, `λ > 1/50`, so (35) is not established.

Now set `s = ⌈2γ log₂ a⌉ = ⌈(2/5) log₂ a⌉` as in Theorem 2. Then

```text
s ≥ 20  ⇔  (2/5) log₂ a > 19  ⇔  a > 2^{47.5} ≈ 1.9903·10^{14}.
```

At the paper’s own starting point `a = 100`, `s = ⌈(2/5)·6.6439⌉ = 3`, so Lemma 4 is applied far outside its hypothesis. The gap persists through `s = 19`; `s = 20` begins at `a ≈ 1.99·10^{14}`.

The paper says on p. 28: “For `a < 100`, the inequality (44) holds with sufficiently large values of the constant hidden behind the symbol `O`.” That clause is harmless and can be made explicit: since `P_m(a) ≥ 0`, choosing a constant `C ≥ √2·100^{1/5} ≈ 3.55` makes the right-hand side of (44) non-positive for every `a < 100`. So the `a < 100` clause is not the obstruction. The obstruction is the unproved interval

```text
100 ≤ a < 2^{47.5}.
```

Corollary 2 (p. 28) inherits this gap: its proof is “Theorem 2 plus (6)”, but Theorem 2 is only established for `a > 2^{47.5}` (and `a < 100`). The statement “for any `a ≥ 2`” is therefore not justified by the written proof. There is also a factor-of-two bookkeeping mismatch: Corollary 2 bounds `Q_{2m}(a)`, while Theorem 3 invokes `Q_m(ρ_t)` for groups of size `m` (p. 29). This is harmless asymptotically but must be fixed for any explicit constant.

## 3. Why Theorem 3 does not give a finite `U(n)` as stated

Theorem 3 (pp. 29–30) applies Corollary 2 with `a = ρ_t ≈ log₂ n`. Therefore its displayed proof is valid only when `ρ_t > 2^{47.5}`, i.e.

```text
log₂ n ≳ 2^{47.5}   ⇒   n ≳ 2^{2^{47.5}} ≈ 10^{5.99·10^{13}}.
```

Below that threshold, the theorem’s proof has no applicable group-insertion estimate. The recurrence

```text
s(n) = S(n) − log₂(n!) ≤ s(n/2) + C n log₂(n)^{-1/5}
```

is then iterated to give `s(n) = O(n log^{-1/5} n)`, but the constant `C` and the threshold are never specified. A standard iteration gives, conditionally, `s(n) ≤ K n log₂(n)^{-1/5}` for suitable explicit `K` once `C` is known and `n` is above a threshold; the boundary term can be absorbed into `K n log^{-1/5} n` for larger `n`. Thus the *shape* of a finite bound is clear:

```text
B(n) = FJ(n)                                        for n < N₀,
B(n) = log₂(n!) + K n (log₂ n)^{-1/5}               for n ≥ N₀,
```

with `N₀ ≈ 2^{2^{47.5}}` if one refuses to repair Lemma 4 below `s = 20`. But `K` and `N₀` are not supplied by the paper. This is an omission of constants, not a non-effective existence argument.

## 4. Consistency with known `S(n)` and Ford–Johnson

The Ford–Johnson count is

```text
FJ(n) = Σ_{k=1}^{n} ⌈log₂(3k/4)⌉
```

(equivalently the paper’s formula on p. 4). It gives:

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FJ(n)=S(n) | 0 | 1 | 3 | 5 | 7 | 10 | 13 | 16 | 19 | 22 | 26 | 30 |

| n | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|
| FJ(n)=S(n) | 34 | 38 | 42 | 46 | 50 | 54 | 58 | 62 | 66 | 71 |

These match the literature values (`S(13)=34`, `S(16)=46`, `S(17)=50`, `S(18)=54`, `S(19)=58`, `S(20)=62`, `S(21)=66`, `S(22)=71`). At `n=12`, `⌈log₂ 12!⌉ = 29` but `S(12)=30`; at `n=22`, `⌈log₂ 22!⌉ = 70` but `S(22)=71`.

Since the group-insertion route only begins at `n ≈ 10^{5.99·10^{13}}`, it says nothing numerically about any `n ≤ 22`, and cannot improve the finite window relevant to `SORT-BOUND-U` (`n ≤ 22` exact, `n = 23` open). Any extracted explicit `B(n)` must dominate the table above, which is automatic here because the threshold is astronomical.

## 5. Sorting comparisons versus evaluation cost

Everything above bounds the **number of comparisons made by one sorting algorithm**. It does not bound the cost of **computing `S(n)`**, deciding `SORT-BOUND-U`, or evaluating `S_unary`. A finite `U(n)` would only:

- certify `S(n) ≤ k` for every `k ≥ U(n)`;
- restrict an exact search to `k ∈ [⌈log₂ n!⌉, U(n)]`;
- combine with a matching lower bound to certify optimality.

It gives neither an algorithm nor a time bound for exact evaluation, and the group-insertion algorithm’s own comparison count is not the cost of computing `S(n)`. In particular, the paper’s `O(n log^{-1/5} n)` is not an “evaluation cost” statement.

## 6. What would finish the extraction

A rigorous explicit all-`n` bound could be assembled from the paper by doing the following finite work:

1. **Repair or bypass the range gap.** Either prove Lemma 4 (or a variant) for `s = 3,…,19`, or accept the threshold `a > 2^{47.5}` and cover smaller `n` by Ford–Johnson.
2. **Extract the constants.** From Lemma 2 and Lemma 4, bound the `O(2^{-s/2})`, `O(2^a/a²)`, and exponential terms uniformly for all `s ≥ 20`, obtaining a numerical `C₂` in
   ```text
   Q_{2m}(a) ≥ 2^a − C₂ a^{-1/5}2^a.
   ```
3. **Fix the rounding and factor-of-two issues:** integrality of `n₀`, `m`, group sizes, and `Q_m` versus `Q_{2m}`.
4. **Choose explicit thresholds** `N₀, N₁` and iterate the recurrence with an explicit `K`.
5. **Verify against** `FJ(n) = S(n)` for `n ≤ 22`; no numerical contradiction is possible, only consistency.

Without steps 1–4, the paper as stated proves only the asymptotic theorem `S(n) = log₂(n!) + O(n log^{-1/5} n)`. It does **not** contain a finite `U(n)`, and the missing quantity is a finite set of constants plus the finite-`s` Lemma 4 range, not an ineffective existence principle.
