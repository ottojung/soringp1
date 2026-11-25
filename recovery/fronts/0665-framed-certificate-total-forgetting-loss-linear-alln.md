# framed-certificate-total-forgetting-loss-linear-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cs7U0JSJlfhvRTG3WDUYaF-amendment

## exit_state

clearexit

## question

In every polynomial-size sound framed certificate for SORT-BOUND-U at exact budget S(n), does the entropy telescoping identity force total expected forgetting loss and imbalance at least Omega(n), or can a construction achieve o(n) total loss for all sufficiently large n?

## basis

docs/research-framed-certificate-frontier.md section 4 entropy telescoping identity; docs/research-certificates-barriers.md Claims C and D; sparse tally constraints in docs/problem.md.

## falsifier

Construct an all-n polynomial-size framed certificate whose auxiliary-walk total forgetting loss and imbalance is o(n), or prove that any such certificate has Omega(n) total loss.

## implication

An o(n) construction would be a decisive step toward NP membership for SORT-BOUND-U; an Omega(n) loss barrier would rule out information-near-optimal framed certificates at exact budget.

## finding_unverified

)-log₂(n!) ≤ O(n/(log n)^{1/5}) = o(n).
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

## Other metadata

```json
{
  "finished_at": 1795306673.7804508,
  "started_at": 1795306543.109768
}
```
