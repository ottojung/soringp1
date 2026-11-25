# surplus-parameter-kernel

## status

investigated

## origin

ai_proposal_unverified

## agent_id

CgP2BIjuQaFCwXBT72lVme-tension

## exit_state

clearexit

## question

For fixed d >= 0, let L_d = {1^n : S(n) <= log2(n!) + d}. Does L_d lie in P (or have a uniform f(d)-poly(n) algorithm) for each fixed d, exploiting the o(n) surplus structure from Sergeev's asymptotics, or is some infinite family in union_d L_d hard for fixed-parameter algorithms?

## basis

Sergeev gives S(n)-log2(n!) = o(n); Stober–Weiß found exact values with small surplus; surplus-parameter-sorted-bound front investigated representation but not parameterized complexity classification.

## falsifier

Give a fixed-parameter tractable algorithm for deciding S(n)-log2(n!) <= d over all n,d, or show that L_d is NP-complete (or hard for some fixed-parameter class) for some fixed d >= 1 via a parameterized reduction.

## implication

FPT in the surplus parameter would yield a practical exact method near the information bound and suggest structure; hardness would show the surplus gap itself contains complexity even if growing sublinearly.

## finding_unverified

\infty$ as $n\to\infty$? That would mean for every fixed $d$, only finitely many $n$ satisfy $S(n) \le \log_2(n!) + d$, so $L_d$ finite => in P trivially. That can't be the point of the question.

Or if we don't take ceil in that form, or if the comparison is different? Let us look up the exact question again carefully.
> "FRONT: For fixed d >= 0, let L_d = {1^n : S(n) <= log2(n!) + d}. Does L_d lie in P (or have a uniform f(d)-poly(n) algorithm) for each fixed d, exploiting the o(n) surplus structure from Sergeev's asymptotics, or is some infinite family in union_d L_d hard for fixed-parameter algorithms?"
> "FALSIFIER: Give a fixed-parameter tractable algorithm for deciding S(n)-log2(n!) <= d over all n,d, or show that L_d is NP-complete (or hard for some fixed-parameter class) for some fixed d >= 1 via a parameterized reduction."

Also note in AGENTS.md they say "SORT-BOUND-U ∈ PSPACE is proved here" - so the threshold language in unary is in PSPACE. Also "showing SORT-BOUND-U ∉ NP would prove NP ≠ PSPACE". And "SORT-BOUND-U is sparse: many-one NP-hardness would imply P = NP". 

But if $L_d$ were infinite for fixed $d$ and NP-complete in some parameterized sense, that would be very interesting. Is it possible that $S(n)$ equals $\lceil \log_2(n!) \rceil + O(1)$ infinitely often or always? Unclear. But the local gap $m(P)-\lceil \log_2 e(P)\rceil$ is unbounded (merge family gives it growing as $O(\log n)$). The global gap $S(n)-\lceil \log_2 n! \rceil$ - is it bounded?

Also some sources say the information-theoretic bound is not asymptotically tight. Sergeev gives better upper bound but excess is still $o(n)$; is it known to be unbounded? That seems likely if the best algorithms still have growing excess. But I need to be precise.
Let us start by reading more carefully about the problem and constraints, then form a precise analysis.

Let us start by exploring the literature and existing results more deeply on this specific question.

Let us understand the full picture of this specific research question.

Let us start by exploring this more deeply.

I need to report a mathematical finding, concrete failed approach or exact obstruction as requested. Let us also check board #301 again quickly and then provide the answer.

**Obstruction (parameterized surplus above information bound):** For L_d = {1^n : S(n) ≤ C(n)+d}, C(n)=⌈log₂ n!⌉, two routes fail. (1) *Trivial finiteness*: if d_n = S(n)-C(n)=o(n) grows unbounded (local merge gaps/log n and Sergeev asymptotics), each fixed L_d finite in P; the uniform parameterized problem (n,d)→d_n≤d is the relevant question. (2) *Naive DP by (poset,state)+remaining surplus* is false because `d+F(P)` does not characterize viable root histories (root-prefix reachability shows additive parameterization fails; sibling dependencies matter). (3) *Enumeration barrier*: the winning frontier extends to k=S(n)+o(n) giving 2^(Ω(n log² n)) information-admissible winning states (not ruled out for selective search, but blocks full enumeration). No known polynomial kernel/FPT decomposition; reduction to NP-hard problems blocked by comparison-model restriction and unary sparsity. No proof of FPT membership or hardness obtained. Conclusion: non-decomposability + exponential frontier are serious obstacles to f(d)-poly(n) algorithms; selective methods not excluded by current barriers. **No repository changes made** (no new Lean/tests/notes) as no independently checkable substantive theorem/counterexample established.


## Other metadata

```json
{
  "finished_at": 1793542923.1842964,
  "started_at": 1793535955.3729432
}
```
