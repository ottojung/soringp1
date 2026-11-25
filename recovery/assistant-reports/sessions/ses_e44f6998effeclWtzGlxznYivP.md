# antonina-GPUzQ6jKWuQUdzMo3VPoPN-would

Session: ses_e44f6998effeclWtzGlxznYivP
Workspace: /home/lubko/soring-fronts/randomized-average-sorting-excess
Created: 1794139318106; updated: 1794140708821

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 820 (msg_1bb1d1490001zQmGzoac58lMKQ)

## Result

**The front is not settled: neither the bounded nor the unbounded horn is proved.** I found a precise reduction, a literature correction, and a rigorous counterexample to the natural proof route — but **not** an infinite `n`-family for `f(n)` and not a proof of boundedness.

Posted once to board #301 at `2026-11-08T12:23:14Z`. Worktree remains clean; no commits, Lean, or repository changes.

## 1. Exact reduction

Let

- `φ(L) = (q+1)L - 2^q`, `q = ceil(log2 L)`,
- `F(L) = φ(L)/L = log2 L + ρ(L)`, with `0 ≤ ρ(L) ≤ 0.0861`.

Morris, *Some Theorems on Sorting*, SIAM J. Appl. Math. 17 (1969) 1–6, DOI `10.1137/0117001`, proves via an insertion recursion that any correct comparison tree for a subproblem with `L` surviving permutations has average remaining depth at least `F(L)`. Hence

`f(n) ≥ F(n!)` and `S(n) ≥ ceil(log2 n!)`.

Since `F(n!) - ceil(log2 n!) ∈ [-1,0]`, the front is exactly:

> Is `f(n) - F(n!)` bounded?

**Literature correction:** Kislitsyn’s 1963 “sharpening” is not a stronger general lower bound. The 1966 survey (DOI `10.1007/BF01071410`, §6) says it estimates the average cost of Steinhaus insertion, with constants `0.0533…` and `0.0610…`.

## 2. Local-slack identity

For a full correct tree `T`, node `v`, let `L_v` be the number of permutations reaching `v`, and `k_v, L_v-k_v` the child counts. Define

`δ(L,k) = 1 + (k/L)F(k) + ((L-k)/L)F(L-k) - F(L) ≥ 0`.

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

## Output 866 (msg_1bb1e7dcf001cmQKPYTY676gdJ)

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
