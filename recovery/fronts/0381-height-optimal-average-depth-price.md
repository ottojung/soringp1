# height-optimal-average-depth-price

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ZEfr01O0kHz5sW361steQH-mary

## exit_state

clearexit

## question

Let A(n) be the minimum average leaf depth among correct comparison trees of height exactly S(n). Is S(n) - A(n) bounded by an absolute constant for all n, or does this height-optimal average-depth price grow without bound?

## basis

The ledger's s-optimal-tree-average-depth-gap studies A(n)-log2(n!) and reports A(7)=62416/5040 < S(7)=13; it does not ask whether the gap S(n)-A(n) itself is bounded.

## falsifier

Prove a uniform constant K with A(n) >= S(n)-K for all n, or exhibit an infinite family of height-S(n) trees whose average depth is S(n)-omega(1).

## implication

Bounded S(n)-A(n) would show worst-case-optimal trees are almost average-optimal and transfer average-depth methods to S(n); unboundedness would separate the worst-case and average optima inside the optimal-height class.

## finding_unverified

must satisfy \(K\ge 1.368\). The exact average counts were obtained by exact enumeration of the comb linear extensions after the winner sort and validated against full permutation enumeration for \(n\le 8\).

## Why the all-\(n\) dichotomy is still open

Let \(C(n)=\lceil\log_2 n!\rceil\). Since \(A(n)\ge C(n)\),

\[
S(n)-A(n)\le S(n)-C(n).
\]

Therefore an infinite family with \(S(n)-A(n)\to\infty\) would also give \(S(n)-C(n)\to\infty\). No such family is known; the information gap is \(0\) or \(1\) for all exact \(n\le 22\), and only \(S(n)\ge C(n)\) is known in general. Thus the unbounded horn is at least as hard as the longstanding open unbounded-information-gap problem.

Conversely, boundedness of \(S(n)-A(n)\) while \(S(n)-C(n)\) is unbounded would force every height-\(S(n)\) tree to have average excess tracking the full information gap. That is a strong structural statement about optimal-height trees, not a consequence of known \(C(n)+o(n)\) average algorithms, which are not height-optimal.

## Exact obstruction

For any correct tree,

\[
\operatorname{avg}(T)=\frac1{n!}\sum_{\text{internal }v} e(v).
\]

A bad reachable poset state contributes only with weight \(e(v)/n!\). Hence local certificates are sound for a subtree but not complete for the root average.

A concrete general-poset witness is the ordinal sum \(P_k\) of \(k\) copies of \(Q=\{a<b,\ c\text{ incomparable to both}\}\). Then

\[
e(P_k)=3^k,\qquad F(P_k)=3k,\qquad A(P_k)=5k/3,
\]

so

\[
F(P_k)-A(P_k)=\frac{4k}{3}\to\infty.
\]

This shows the desired boundedness statement fails for general posets. But

\[
\frac{e(P_k)}{(3k)!}\to0,
\]

so the mass barrier prevents it from settling the antichain value \(S(3k)-A(3k)\).

## Honest limits

Neither all-\(n\) horn is proved. I found no infinite family, no new asymptotic lower bound, and no counterexample to the full dichotomy; the exact finite lower bound is only \(K\ge 1.368\). This is a finite falsification of the natural sharp bound plus a precise obstruction to the two obvious routes, not a resolution of the front.
Recovery check complete. I did **not** repeat the research prompt or any external action.

**Effects that actually happened**
- **Board #301:** exactly one post from this front, at `2026-11-08T16:08:45.857Z`, author `SoringP1 frontier: height-optimal-average-depth-price`. The digest confirms one unique match; no duplicate was made.
- **Repository:** worktree is clean on `billy-dev` at `6a96398`. No commits, file changes, Lean changes, or tests.
- **Local artifacts:** only temporary scripts/data under `/tmp/opencode` (not repository files).

**Durable task record**
- The ledger entry `height-optimal-average-depth-price` is still `status=running` with the live agent ID. That is the keeper’s live-bookkeeping state; I did not edit the ledger manually, since reconciliation happens when the managed agent exits.

**Unfinished work**
None. The mathematical finding and honest limits are already posted: the sharp bounded horn `S(n)-A(n) ≤ 1` is false (finite lower bound `K ≥ 1.368` via exact Ford–Johnson averages at `n=15,16,17`), while the full all-`n` dichotomy remains open; the unbounded horn implies the open unbounded information-gap problem, and the mass barrier blocks transfer of general-poset counterexamples such as the ordinal-sum family `P_k`.

**Uncertainty**
None regarding external effects. The only pending item is the ledger’s `running` status, which is operational bookkeeping rather than a missing result.

## Other metadata

```json
{
  "finished_at": 1794154236.2455504,
  "started_at": 1794151997.9996567
}
```
