# antonina-qCsdMQjp8ppNSqVGVKYunX-lied

Session: ses_e03a06fa9ffeV91xOp5QSWR9HE
Workspace: /home/lubko/soring-fronts/rank-envelope-grammar-soundness-alln
Created: 1795235483804; updated: 1795235697334

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 297 (msg_1fc623d1c001nVZyOVKjS29w83)

**Finding (label: paper proof sketch + conjecture, not a kernel-checked theorem):**  
The rank-envelope insertion construction can be completed as a sound polynomial-size framed DAG for the **standard Ford–Johnson bound**, whose total comparison surplus over \(\log_2(n!)\) is **linear** (\(\Theta(n)\)), but the same weak-window construction does **not** by itself justify the **\(o(n)\)** surplus of Sergeev’s group insertion. The obstruction is the coupling between pending keys in Sergeev’s containers.

## Claim tested

> There is an all-\(n\) polynomial-size sound framed comparison DAG of height  
> \(\log_2(n!)+o(n)\) obtained by completing rank-envelope insertion, including recursive winner frames and the odd unpaired element.

## What does work: linear surplus

For Ford–Johnson, a pending loser \(b_i\) is anchored by its paired winner \(a_i\): \(b_i<a_i\), and after \(t\) other insertions the paired winner has rank at most \(i+t\). The weak invariant

\[
\operatorname{current}[\ell_j] < x_j < \operatorname{current}[u_j+t]
\]

is sound, and inserting \(x_j\) costs at most

\[
\lceil \log_2(u_j-\ell_j+t)\rceil \le \lceil \log_2(i+t)\rceil
\]

comparisons. The leaves of each insertion search tree can be joined because every other pending loser still satisfies the relaxed window. Recursive winner frames can carry associated loser slots, and the odd unpaired element takes a full-range insertion. This gives an \(O(n^2)\)-node framed DAG at height

\[
F_{\mathrm{FJ}}(n)=\sum_{j=1}^n \lceil \log_2(3j/4)\rceil,
\]

which is \(\log_2(n!)+\Theta(n)\). Thus the rank-envelope construction verifies a **stage with linear surplus**, not \(o(n)\).

## Why the \(o(n)\) case is blocked by joins

Sergeev’s \(O(n/(\log n)^{1/5})\) surplus comes from **group insertion into coupled interval containers**, not from independent single-key insertion. In that construction, pending elements are grouped, and the endpoint of one pending key’s effective interval depends on how many (and which) elements from its container have already been extracted/inserted. The simple rank-envelope weak window treats each pending key independently and only shifts endpoints by a global count \(t\). That bound is sound but too coarse: preserving the sublinear budget requires tracking the coupled container state.

A sound join at a group-insertion stage must therefore distinguish container histories. If one forgets those histories to keep the state count polynomial, the weak windows loosen and the insertion cost reverts to the Ford–Johnson \(\Theta(n)\) surplus. If one keeps them tight, the number of join-incompatible framed states grows with the number of independent container configurations, which is superpolynomial in the natural group/container parameters. Hence the \(o(n)\) completion is not supported by the rank-envelope weak-window construction; the join constraints are the obstruction.

## Honest limits

- This is a **structural obstruction for the specific rank-envelope weak-window construction**, not a proved lower bound against every possible polynomial framed DAG at height \(\log_2(n!)+o(n)\).
- It does not contradict the existence of some other succinct certificate route; it isolates why the natural insertion-stage join does not carry Sergeev’s sublinear surplus.
- No Lean, test, or repository changes were made; the worktree remains clean. The next decisive check would be an explicit framed-DAG encoding of one Sergeev group-insertion stage, counting join-incompatible framed states as a function of the container parameters.

## Output 318 (msg_1fc62c624001bMr8x8RuJEmeNW)

Inspected: worktree is clean; no commits, files, or repository changes were made. No board post or other external action was performed in the prior turn. The durable ledger still shows `rank-envelope-grammar-soundness-alln` as `running`, which should be left for the keeper/execution layer to reconcile; I did not modify it.

Unfinished external action: none identified. The research finding was already produced and reported in the conversation: rank-envelope insertion supports a sound polynomial framed DAG with **linear** surplus (Ford–Johnson), but the weak-window construction does not establish Sergeev’s \(o(n)\) surplus; coupled containers force either looser windows or join-incompatible (superpolynomial) framed states. No further action is needed from this turn.
