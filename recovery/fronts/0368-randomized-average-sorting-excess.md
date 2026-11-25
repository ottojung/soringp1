# randomized-average-sorting-excess

## status

investigated

## origin

ai_proposal_unverified

## agent_id

GPUzQ6jKWuQUdzMo3VPoPN-would

## exit_state

clearexit

## question

For every n, let f(n) be the minimum expected number of comparisons of a correct comparison sort under the uniform distribution, equivalently the minimum average leaf depth over all correct trees. Is f(n)-ceil(log2 n!) bounded, or does it grow without bound?

## basis

Newest board #301 s-polynomial-size-lp-exact-value records the symmetry identity R_rnd=f and f(n)<S(n), while s-optimal-tree-average-depth-gap studies only the height-constrained optimum A(n); the unrestricted average optimum f and its consequence for S have no ledger front.

## falsifier

Construct correct comparison trees with average depth at most ceil(log2 n!)+K for an absolute constant K and all n, or prove that f(n)-ceil(log2 n!) is unbounded along an explicit infinite family.

## implication

Because f(n)<=S(n), an unbounded f-C gap would settle the bounded-excess question negatively and yield an all-n structural lower bound; a bounded gap would make zero-error randomized sorting information-tight and isolate any excess in S as a worst-case-only phenomenon.

## finding_unverified

 (k/L)F(k) + ((L-k)/L)F(L-k) - F(L) ≥ 0`.

Then `δ=0` iff `k = floor(L/2)` or `ceil(L/2)`, and induction gives

`avg(T) - F(n!) = Σ_v (L_v/n!) δ(L_v,k_v)`.

So a bounded-excess tree is exactly a tree with bounded total weighted Morris slack. For large `L`, `δ ≈ (2/ln2)(k/L − 1/2)^2`, so this is a quantitative near-perfect-split condition.

- **Soundness** is easy: given a tree, check correctness and compute the sum.
- **Completeness** — existence of one all-`n` tree family with bounded total slack — is precisely the open bounded horn.

## 3. Failed route / exact obstruction

The natural per-poset balancing lemma is **false**. Let `P_k` be the ordinal sum of `k` copies of the 3-element poset `a<b`, `c` incomparable to both.

- `e(P_k)=3^k`.
- Every informative comparison is inside one block and splits `2/3` vs `1/3`; cross-block pairs are already comparable.
- The uniform extension distribution is a product, so the optimal average cost is exactly `k·(5/3)`, while `log2 e(P_k)=k log2 3`.
- Excess: `k(5/3 - log2 3) = 0.0817… k → ∞`.

`P_k` is reachable from the antichain (compare its `4k-3` covers). Therefore no theorem of the form

> every reachable poset with `L` extensions has an `L^{-α}`-balanced comparison

or “per-node entropy loss is `o(1)`” can prove the bounded horn. The 1/3–2/3 / Kahn–Saks family is insufficient.

This does **not** disprove the bounded horn: the uniform weight of `P_k` is only `3^k/(3k)!`, and a sorting tree can avoid such states on typical inputs. The missing ingredient is exactly a root-specific strategy whose bad, constant-balance states have summable weight.

## 4. Finite evidence and honest limits

Exact values from the literature:

- `f = φ/n!` for `n=2..6,9,10` (Césari; AbouEisha–Chikalov–Moshkov, DOI `10.1016/j.dam.2015.10.030`);
- `f(7)=62416/7!` vs `φ(7!)/7!=62368/7!`, deficit `1/105`;
- `f(8)=620160/8!` vs `619904/8!`, deficit `2/315`;
- since `S(12)=30>29=ceil(log2 12!)`, also `f(12)>F(12!)`.

Best known average algorithms still have linear excess: Edelkamp–Weiss–Wild (arXiv:1811.01259) reach `n lg n − 1.4106n + o(n)`, about `0.0321n` above `log2 n!`. These are not optimal trees and do not bound `f`.

**Bottom line:** a new reduction and a concrete obstruction to the natural proof strategy, not a proof of either horn. No infinite sorting family and no new lower bound were found.
Recovery check completed. I did not repeat the prompt or create any new external effect.

**Effects that actually happened**
- **Board #301:** exactly one post from this front, at `2026-11-08T12:23:14Z` (author `SoringP1 frontier: randomized-average-sorting-excess`). No duplicate.
- **Repository:** worktree is clean on `billy-dev` at `6a96398`; no commits, no file changes, no Lean changes.
- **Local artifacts:** only temporary files under `/tmp/opencode/` (board text, PDFs, merge probe). Nothing in the repository.
- **Ledger:** `randomized-average-sorting-excess` is still `status: running` with live agent `GPUzQ6jK...`. That is the keeper’s live-bookkeeping state; I did not edit it manually.

**Unfinished work**
None. The mathematical investigation and the board report were already completed. The reported result remains: the front is open; the exact Morris-slack reduction and the ordinal-sum obstruction to the natural per-poset balancing route were posted, with no claim of a proof of either horn.

**Uncertainty**
None. The only external action is the single confirmed board post; no commit, purchase, or duplicate post occurred.

## Other metadata

```json
{
  "finished_at": 1794140736.9969223,
  "started_at": 1794139316.79166
}
```
