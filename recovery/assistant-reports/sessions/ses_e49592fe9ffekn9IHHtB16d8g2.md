# antonina-CXuzFvys6BkalgtCNrlE0x-advisable

Session: ses_e49592fe9ffekn9IHHtB16d8g2
Workspace: /home/lubko/soring-fronts/exec-optimal-merge-tree-gap-20261107
Created: 1794065748055; updated: 1794069805000

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b6a6d65f001Bo1g9V7eKQNHJp)

I’ll treat this as a paper-level research task: first inspect the project’s stated merge-cost obstruction and literature references, then check the source claims and see whether the architecture-cost equality and all‑n dichotomy can actually be proved. I won’t add files or broaden beyond the fixed recursive architecture.

## Output 37 (msg_1b6a6f9fa001dUzK4uLMQMv9Yh)

## Finding: the sum formula is not established

For a fixed tree \(T\), let \(a_v,b_v\) be the numbers of leaves below the two children of internal node \(v\). Then

\[
A_T=\sum_v M(a_v,b_v)
\]

is a valid **upper bound** on the worst-case cost: use an optimal merge procedure at each node, and every execution performs at most \(M(a_v,b_v)\) comparisons there.

The matching lower bound needs care. A merge procedure’s worst case is a particular interleaving of particular identities in its two input runs. To add the local worst cases, one must show that a single permutation of all leaves can realize a worst case at every node, while also inducing the child orders required by those worst cases. The local worst-case interleavings need not be compatible under recursion. This is especially important for identity-dependent merge procedures. The fact that every local merge has worst-case cost \(M(a_v,b_v)\) does **not** by itself prove that the costs add on one global input.

So the requested exact architecture-cost identity is unresolved by the cited local merge results. A minimal safe correction is:

\[
\operatorname{cost}(T,\text{chosen procedures})\le A_T,
\qquad
\text{and hence}\qquad
\min_T A_T
\text{ is an achievable architecture upper bound.}
\]

To call it the *optimal* architecture cost, a separate compatibility theorem is needed—or the architecture must be restricted to a class of merge procedures for which simultaneous realization can be proved.

## All-\(n\) dichotomy: precise obstacle

The source audit in `docs/research-obstruction-next.md` supports the following facts:

- **[Literature]** \(M(m,m)=2m-1\), and tape merge is optimal in specified similar-size ranges.
- **[Literature]** Hwang–Lin give better bounds for unbalanced merges; in particular \(M(1,n)=\lceil\log_2(n+1)\rceil\). Thus \(M(a,b)\) cannot be replaced everywhere by \(a+b-1\).
- **[Deduction]** The balanced two-chain example has a growing *local* information gap. That fact does not yield a linear gap for \(\min_T A_T-\lceil\log_2(n!)\rceil\): a tree may use highly unbalanced merges, where the balanced formula gives no bound.

I do not have a rigorous all-\(n\) lower bound of \(\Omega(n)\) for this sum, or a valid explicit tree family with \(o(n)\) surplus. The key missing ingredient is an all-size estimate for \(M(a,b)\), strong enough to control its sum over every full binary tree, together with a compatible-realization argument if the sum is to represent actual architecture cost exactly. The cited special cases do not supply that estimate. Small-instance computations would not resolve this gap.

Accordingly, the justified outcome is **inconclusive**, not either side of the dichotomy. An \(\Omega(n)\) theorem for the architecture would rule it out as an exact route for sufficiently large \(n\); an \(o(n)\) construction would only meet Sergeev’s asymptotic ceiling, not prove exact \(S(n)\). Neither conclusion follows from the local merge facts audited here. This scope concerns only fixed independent-completion/merge trees, not algorithms that interleave comparisons across unfinished subproblems.

No files were changed.

## Output 141 (msg_1b6a979bc001jsj1QfjVtQjnx1)

The workspace is clean, and no post or commit from this investigation exists; the only board entry is the launch notice. So there is no completed external effect to preserve. I’m continuing the mathematical work only.

## Output 805 (msg_1b6e3d169001EXvQ0RU8Gqgmcu)

No commit, file edit, or board comment from this investigation exists: the worktree is clean and #301 contains only the launch notice. I’ll record the new mathematical correction once, without duplicating anything.

## Output 852 (msg_1b6e43aca001KB3MEqVd63ZQB8)

## Recovery audit

No prior effect from this investigation existed. The worktree was clean at `c865b23`, there was no commit or file edit, and #301 contained only the launch notice. I posted one new, non-duplicate summary comment to #301 under `CXuzFvys6BkalgtCNrlE0x-advisable`; the worktree remains clean. No Lean or code changes.

## 1. The architecture cost is exactly \(A_T\)

For a fixed full binary tree \(T\) with singleton leaves and an **arbitrary deterministic merge procedure** at each internal node, the optimal architecture cost is exactly

\[
A_T=\sum_{v} M(a_v,b_v).
\]

This corrects the previous turn’s caveat that the sum was only an upper bound.

**Proof (minimax induction).** For a subtree \(v\), let \(F(v)\) be the worst-case total number of comparisons performed at nodes inside \(v\). For an internal node with children \(L,R\) of sizes \(a,b\), choose orders attaining \(F(L)\) and \(F(R)\). These fix the two child sorted orders. For that fixed pair of sorted runs, the merge procedure at \(v\) still faces all \(\binom{a+b}{a}\) possible interleavings, so some interleaving makes it use at least \(M(a,b)\) comparisons. That interleaving combines with the child orders into one global total order. Hence

\[
F(v)\ge M(a,b)+F(L)+F(R),
\]

and induction gives \(F(\text{root})\ge \sum_v M(a_v,b_v)\). The reverse inequality holds by choosing optimal merge procedures, whose local cost is at most \(M(a_v,b_v)\) on every execution. Therefore equality.

Identity-dependent procedures do not break this: their local worst case may depend on the child orders, but for every fixed child order the merge adversary still has an interleaving requiring at least \(M(a,b)\). Recursively chosen child orders are handled by the induction—no single “compatible global permutation” needs to be guessed in advance.

## 2. Exact reduction of the dichotomy

At node \(v\),

\[
M(a_v,b_v)\ge \log_2\binom{a_v+b_v}{a_v},
\]

and the product of all node binomial coefficients telescopes to \(n!\). Therefore

\[
A_T-\log_2(n!)
=
\sum_v \left(M(a_v,b_v)-\log_2\binom{a_v+b_v}{a_v}\right).
\]

Thus

\[
A(n)-\lceil\log_2(n!)\rceil
=
\min_T \sum_v \delta(a_v,b_v)
\;+\;O(1),
\]

where

\[
\delta(a,b)=M(a,b)-\log_2\binom{a+b}{a}\ge 0.
\]

So the all-\(n\) question is precisely whether **every full binary tree must have linear total local merge slack**.

## 3. What the sources do and do not give

- \(M(a,b)\ge \log_2\binom{a+b}{a}\) is the information bound.
- \(M(1,b)=\lceil\log_2(b+1)\rceil\) (Hwang–Lin 1972).
- \(M(a,b)=a+b-1\) in the Stockmeyer–Yao/Murphy–Paull/Christen range, extended to \(n\le 1.52a\) by Li–Sun–Zhang 2016; in particular \(M(m,m)=2m-1\).
- Hwang–Lin also give
  \[
  M(a,b)\le I(a,b)+\min(a,b).
  \]
  Summed over a tree this is at least \(n-1\), so it does not decide the dichotomy.

The missing ingredient is an all-\(n\) lower bound on \(\delta(a,b)\) outside the exact ranges, or an explicit tree family with \(\sum_v\delta(a_v,b_v)=o(n)\). A comb using only \(a=1\) nodes has \(\delta=0\) locally, but the accumulated ceiling loss \(\lceil\log C\rceil-\log C\) along the comb is linear (about \(0.44n\)). The true optimum must trade off this ceiling loss against the exact merge slack \(\delta\); no audited source controls that trade-off for all trees.

**Diagnostic only** (not an all-\(n\) proof): exact minimax values for \(a,b\le 13\) plus tree DP give

\[
A(2),\dots,A(13)
=1,3,5,8,11,14,17,21,24,28,32,36,
\]

with gaps over \(\lceil\log_2 n!\rceil\) equal to \(0,0,0,0,1,1,1,1,2,2,2,3,3\). This is consistent with a linear or sublinear gap but does not establish either.

## 4. Consequence

An \(\Omega(n)\) theorem for \(\sum_v\delta(a_v,b_v)\) would rule out this entire fixed independent-completion/optimal-merge architecture for all sufficiently large \(n\). An explicit \(o(n)\) construction would only match Sergeev’s asymptotic ceiling and would **not** prove exact \(S(n)\). The precise open obstacle is the all-\(n\) behaviour of the local merge slack \(\delta(a,b)\), not the architecture decomposition itself.

## Output 879 (msg_1b6e4a7e6001fa0k5TGcuJF4pL)

Recovery check complete. The prior turn’s effects are confirmed: exactly one comment was posted to Antonina #301, and no commit or repository edit was made. The worktree remains clean at `c865b23`. Nothing remains to continue, and I did not repeat the post.
