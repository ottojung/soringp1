# antonina-Ny6SNaEG3TyPOEOfbrDan9-loosely

Session: ses_e455e5e01ffehpaDvS6yacG7a5
Workspace: /home/lubko/soring-fronts/bidirectional-backward-frontier-exponent
Created: 1794132517649; updated: 1794133239875

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 257 (msg_1baac4d6a001fM29Qtji54Ini7)

On `billy-dev` only. I studied `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, the relevant research notes, Stober–Weiss arXiv:2206.05597v2, and board #301. I posted the finding there. The worktree is clean: no Lean, repo, or note changes.

## Verdict on the front

The proposed dichotomy is false. For the natural complete pruning used by Stober–Weiss:

- the **unpruned backward ball** `B_k = {P : F(P) ≤ k}` genuinely has `2^{Ω(n²)}` nonisomorphic posets;
- the **reachability/Hasse-pruned frontier** `W_k = {P : H(P)+F(P) ≤ k}` has size `2^{Θ(n log² n)}` at budget `k = C(n) = ceil(log₂ n!)`, not `2^{O(n log n)}` and not `2^{Ω(n²)}`.

Here `H(P)` is the number of cover relations. The key is the board-verified all-`n` reachability lemma: the minimum number of comparisons needed to reach `P` from the antichain is exactly `H(P)`. Therefore the posets occurring on **some** root-winning play at budget `k` are exactly `W_k`. [deduction + board-verified lemma]

## A. The full backward ball is `2^{Ω(n²)}` [paper proof]

For `n = 6m`, let

\[
P = A_m \oplus A_m \oplus A_m \oplus A_m \oplus A_m \oplus Q,
\]

the ordinal sum of five `m`-element antichains and an arbitrary poset `Q` on `m` elements. Ordinal-sum additivity gives

\[
F(P)=5S(m)+F(Q)\le 6S(m)\le 6m\lceil\log_2 m\rceil
\le n\log_2 n-1.585n .
\]

Using `n! ≥ (n/e)^n`,

\[
C(n)=\lceil\log_2 n!\rceil \ge n\log_2 n-1.4427n .
\]

Hence `F(P) < C(n)` for all sufficiently large `m`. The map `Q ↦ P` is injective on isomorphism classes: `Q` is exactly the set of elements having at least `5m` elements below them. Therefore

\[
|B_k| \ge A000112(m)=2^{(1/4-o(1))m^2}
=2^{(1/144-o(1))n^2}=2^{\Omega(n^2)}
\]

for every `k ≥ C(n)`, including `k = S(n)`.

But `H(P) ≥ 4m^2 = n^2/9 > C(n)`, so none of these posets is reachable within budget `C(n)`. This is the concrete failed approach: **ordinal-sum counting gives a huge full backward ball, but the Hasse/reachability pruning removes all of it.** General-poset backward counts do not transfer to the bidirectional frontier.

## B. The pruned frontier is at most `2^{O(n log² n)}` for all `n` [paper proof]

A poset is determined by its transitive-reduction edge set, which has exactly `H(P)` edges. Thus the number of labelled posets with `H(P) ≤ k` is at most

\[
\sum_{h=0}^{k}\binom{n(n-1)}{h}\le 2^{O(k\log n)}.
\]

Since `W_k ⊆ {P : H(P) ≤ k}` and `k = C(n) = O(n log n)` (or `k=S(n)=O(n log n)`),

\[
|W_k| \le 2^{O(n\log^2 n)}.
\]

This holds uniformly for every `n`, with no advice. Stober–Weiss's Hasse-edge optimization (`§4.1`, `§5.5`) keeps a state at level `c` only when `H(P)≤c` and `F(P)≤C-c`, so their complete non-efficiency-pruned backward table is a subset of `W_C`.

## C. Matching lower bound `2^{Ω(n log² n)}` [existing literature + deduction]

The existing winning-frontier construction in `docs/research-winning-frontier-barrier.md` gives, for infinitely many `n=s²` and `k=C(n)`, at least

\[
2^{(1/4-o(1))\,n(\log n)^2}
\]

pairwise nonisomorphic posets `P` reachable at depth `t` with `F(P) ≤ k-t`.

In that construction every installed edge increases the level by exactly one, so no installed edge is transitively implied, and every installed edge is a cover. Hence `H(P)=t`. Therefore `H(P)+F(P) ≤ k`, so the same family lies in `W_k`. Consequently

\[
|W_k| = 2^{\Theta(n\log^2 n)}
\]

at the information budget. This refutes the `2^{O(n log n)}` alternative for the complete pruned frontier, and the earlier full-ball construction does not rescue the `2^{Ω(n²)}` alternative because those states have `H = Ω(n²)`.

## D. Soundness versus completeness, and the honest limit

Stober–Weiss's additional efficiency filter is **sound but incomplete**. At level `c` it keeps `E(P)=n!/(2^c e(P)) ≤ E_thr < 2E_tot`, which is, up to a factor of two, information tightness `F(P)=ceil(log₂ e(P))`. The winning-frontier family used for the lower bound certifies only `e(P) ≤ 2^{F(P)}`, not the reverse factor `e(P) > 2^{F(P)-1}`. So it does **not** give a `2^{Ω(n log² n)}` lower bound for the efficiency-band table.

Thus the precise open gap is:

- upper bound `2^{O(n log² n)}` applies to the efficiency-pruned table;
- whether the efficiency-band frontier is actually `2^{O(n log n)}` is not settled here;
- the complete reachability/Hasse-pruned frontier is `2^{Θ(n log² n)}`.

Finally, even a complete pruned frontier of size `2^{Θ(n log² n)}` gives no uniform `2^{O(n log n)}` algorithm. Enumerating it cannot beat the existing `2^{O(n log² n)}` budgeted DFS. A sub-`n log² n` **selective** evaluator remains open. Soundness of absence-based advice (Stober–Weiss Lemma 4.2) is not completeness of the table.
