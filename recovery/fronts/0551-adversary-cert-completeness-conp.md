# adversary-cert-completeness-conp

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Q9o7KX9Wzt4tHu8VVAoaZe-kidney

## exit_state

clearexit

## question

For the minimax sorting game G(n,k) (sorter picks an incomparable pair, adversary answers), define c_adv(n) as the minimum Boolean-circuit size of a memoryless adversary strategy that forces at least S(n) comparisons against every height-(S(n)-1) sorter from the n-antichain. Is c_adv(n) bounded by one fixed polynomial in n for all n, and is the strategy's winning property checkable in time polynomial in n?

## basis

Determinacy of the finite game G(n,k); research-certificates-barriers.md section 1 lower-bound-certificate question; framed-DAG and FO(TC) work proves sorter-side soundness only, never completeness; Mahaney and Berman-Hartmanis sparsity barriers on the tally language.

## falsifier

Exhibit an infinite family of n for which every winning adversary strategy needs superpolynomial circuit size, or prove that no polynomially checkable, complete adversary certificate class can exist for the S(n)>k side.

## implication

A poly-size, poly-verifiable complete adversary certificate would put SORT-BOUND-U in coNP and, with the sorter-side certificates, in NP intersect coNP; a superpolynomial lower bound would be a barrier to any coNP-style certificate route below PSPACE.

## finding_unverified

maining budget), a sufficient statistic. Memoryless strategies are WLOG (reachability games have positional winning strategies), so by determinacy a winning adversary at `k=S(n)−1` always exists and `c_adv(n)` is finite for every n. Confirmed computationally for n=2…6.
- **F2 — the verification gap (central point).** `"A is not winning"` is in NP via the ≤ n(n−1)/2‑pair sorter path, so `VERIFY-ADV ∈ coNP` (unary). Hence a poly‑size circuit is *not* a poly‑verifiable certificate; checking "A wins" is exactly the coNP predicate. This is the soundness/completeness distinction: passing = sound; completeness needs a verifier for a coNP predicate. A trivial memoryless adversary is beaten in ≤ n comparisons (explicit tiny witness).
- **F3 — advice/circularity theorem.** A winning A plus a poly verifier lets binary search recover `S(n)` (largest k with "A wins" = S(n)−1; verified for n=2…6). Such a certificate already carries the full evaluator value — producing it requires solving the game it certifies.
- **F4 — falsifier barrier.** The global falsifier ("no poly‑checkable complete adversary certificate ⇒ SORT‑BOUND‑U ∉ coNP") would imply `PSPACE ≠ coNP` since `SORT-BOUND-U ∈ PSPACE` — an open separation. The narrow form needs a VERIFY‑ADV hardness / circuit lower bound, also open.
- **F5 — the FRONT's implication is correct but narrow:** it needs both hypotheses; it yields only coNP on the adversary side (framed‑DAG/FO(TC) gives sorter‑side soundness only), and it is unary‑specific (binary k makes the witness exponential).

## Honest limits / failed disproof attempts

I could **not** disprove C_adv. Counting gives no circuit‑lower bound on `c_adv` (it is a minimum over a huge strategy space); a reduction from S‑hardness fails because `S ∈ FP` is open and `S ∈ FP/poly` is already true for a tally language; a coNP‑hardness reduction for VERIFY‑ADV is only sketched and blocked by the constrained poset‑transition structure; the information adversary is sound for the log bound but fails exactly where S(n) exceeds it (first at n=12). General‑poset/arbitrary‑test hardness (Hyafil–Rivest, Laber–Nogueira, Parberry) and Mahaney's sparsity barrier supply no falsifier.

**Bottom line:** a precise obstruction and a rigorous reclassification of the certificate route — not a theorem completion. The decisive open subproblem is the complexity of `VERIFY-ADV` (is it coNP‑hard?) and, independently, whether `c_adv` is polynomially bounded.
**Recovery inspection (no actions repeated):**

- **Git/worktree:** `billy-dev` at `6a96398`, clean (`git status --porcelain` empty), no new commits.
- **Scratch artifacts present:** `/tmp/opencode/adv_cert_probe.py`, `/tmp/opencode/report.md`, `/tmp/opencode/post_result.json` (result file confirms posted author/body).
- **Board side effect confirmed:** `board_digest.py --contains "adversary-coNP-cert-front" --page 1` shows the report was posted to #301 at `2026-11-19T09:54:37.068Z` by author `SoringP1 front: adversary-coNP-cert-front`.

**Conclusion:** the previous turn completed all intended work, including the external post. There is no unfinished work and no uncertain effect requiring review, so I did not repost, commit, or modify anything. The finding remains as reported: a precise verification/circularity obstruction (VERIFY-ADV ∈ coNP, advice recovery of `S(n)` via binary search) and failed disproof attempts, but **no proof or disproof** of the `c_adv(n)`/poly-verifiable-complete adversary-certificate claim for all `n`.

## Other metadata

```json
{
  "finished_at": 1795082145.4803104,
  "started_at": 1795081685.3307128
}
```
