# antonina-cs7U0JSJlfhvRTG3WDUYaF-amendment

Session: ses_dff64271effefr4xuUFaJVpaRg
Workspace: /home/lubko/soring-fronts/framed-certificate-total-forgetting-loss-linear-alln
Created: 1795306543385; updated: 1795306666285

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 208 (msg_2009d87a3001PnraywbYTCB8q4)

## Mathematical finding

**Claim investigated (FRONT).** For every polynomial-size sound framed certificate for `SORT-BOUND-U` at exact budget `k = S(n)`, does the entropy telescoping identity (docs/research-framed-certificate-frontier.md §4) force total *expected* forgetting loss + imbalance `≥ Ω(n)`, or can a construction achieve `o(n)`?

**Verdict: the `Ω(n)` horn is refuted by deduction. The identity actually forces `o(n)` for *every* exact-budget certificate, regardless of size. The construction horn (polynomial-size exact-budget certificate) remains open and is equivalent to `SORT-BOUND-U ∈ NP`.**

### Proof (paper deduction; labels: deduction + literature)

1. **Identity (literature/paper).** For a sound framed certificate with annotation `P`, set `m=e(P)`. For an outcome `b` with `m_b=e(TC(P+outcome_b))`, `q_b=m_b/m`, and at child `Q` the forgetting loss `λ_b=log₂(e(Q)/m_b)≥0`. The binary outcome entropy is `H=-∑ q_b log₂ q_b ≤1`. The auxiliary walk samples each outgoing arc with probability `q_b` (resampling compatible orders after forgetful joins). For path length `D≤k`,
   ```
   E[∑_queries (1-H+λ_b)] = E[D] - log₂(n!).
   ```
   Both `(1-H)` and `λ_b` are nonnegative, so the LHS is nonnegative; hence `E[D] ≥ log₂(n!)`.

2. **Exact budget.** The certificate is at budget `k=S(n)`, and every root-to-terminal path has at most `S(n)` comparisons, so pointwise `D ≤ S(n)`. Thus `E[D] ≤ S(n)`.

3. **Combine.** Total expected forgetting loss + imbalance
   ```
   E[D]-log₂(n!) ≤ S(n)-log₂(n!).
   ```

4. **Sergeev upper bound (literature; ECCC TR20-096 Thm 3).** `S(n) = log₂(n!) + O(n/(log n)^{1/5})`. Hence
   ```
   0 ≤ S(n)-log₂(n!) ≤ O(n/(log n)^{1/5}) = o(n).
   ```
   (Lower bound 0 is the information bound `⌈log₂ n!⌉ ≤ S(n)`.)

5. **Conclusion.** By squeeze, for any sound framed certificate at exact budget `S(n)` — of any size —
   ```
   0 ≤ E[D]-log₂(n!) ≤ o(n).
   ```
   So total expected forgetting loss + imbalance is `o(n)`, not `Ω(n)`. The `Ω(n)` barrier horn is impossible.

### What this does and does not settle

- **Disproved:** "entropy telescoping forces `Ω(n)` total loss for exact-budget polynomial-size framed certificates." The identity + Sergeev force the opposite. Linear information loss cannot occur at exact budget; the only way to get `Ω(n)` loss is to use a certificate whose height exceeds `S(n)` by `Ω(n)` (e.g. merge sort, Ford–Johnson), which is not an exact-budget certificate.
- **Still open (construction horn):** existence of a *polynomial-size* sound framed certificate at height `S(n)`. The identity is an analytic necessary condition, not a verifier and not a construction. Known polynomial-size framed certificates (merge sort `O(n²)` nodes, rank-envelope insertion `O(n²)` nodes, Ford–Johnson) have height `S(n)+Ω(n)` for large `n` (merge sort surplus `(log₂ e-1)n+O(log n)≈0.44n`; Ford–Johnson surplus `Θ(n)` with slope ~0.06–0.11, while `S(n)` surplus is `o(n)`), so none is exact-budget. Sergeev's `o(n)`-surplus group insertion is not known to be framable with polynomial-size states. This is precisely the `SORT-BOUND-U ∈ NP` question; no P-vs-NP consequence follows.
- **Not a hardness result:** a lower bound in this pinned system would not prove `SORT-BOUND-U ∉ NP`, since NP certificates need not be framed sorters. Parberry's coNP-completeness for arbitrary fixed networks does not transfer to one near-optimal adaptive sorter per `n`.

### Distinctions honored

- **General-poset vs root.** The state-count/poset facts (A001035 labelled posets, Kleitman–Rothschild `2^{Θ(n²)}`) are not used; the deduction uses only `S(n)`'s own asymptotic via Sergeev. No general-poset hardness is asserted for `S(n)`.
- **Soundness vs completeness.** Soundness of the framed grammar is unchanged (checker `scripts/check_framed_strategy.py`). The identity is a *necessary analytic condition* on sound certificates; it neither constructs one nor decides completeness. Counting `e(P)` is #P-hard (Brightwell–Winkler), so the identity is not a polynomial-time verification rule.
- **Encoding.** Unary `N=n+k+1=Θ(n log n)` on informative `k`; `poly(n)=poly(N)`. The `o(n)` bound is in numeric `n`, which is `o(N)`? Actually `n = Θ(N/log N)`, so `o(n)` is also `o(N)`; either way sublinear in input length. The conclusion holds.

### Limits / honest caveats

- The upper bound is asymptotic (`O(n/(log n)^{1/5})`); no explicit constant or finite computable bound is supplied (Sergeev's big-O alone). Extracting an effective bound from the group-insertion proof is a separate task.
- The bound is on *expected* total under the auxiliary resampling walk, not on worst-case per path, and not on the true execution distribution of a uniform random permutation.
- The construction horn is untouched; I did not produce a polynomial-size exact-budget certificate (none is known; this is the open NP question).
- No repository, Lean, test, or board changes made; worktree clean at `6a96398`. The deduction is a short corollary of two already-recorded facts (identity + Sergeev), so it does not meet the publication gate for a new theorem file; it is reported as a refutation of the `Ω(n)` horn.
