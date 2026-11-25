# Issue #48: Root adversary vs reachable gadgets: derive an all-n forcing lower-bound rule

Upstream: https://github.com/ottojung/soringp1/issues/48
State: open
Created: 2026-10-22T19:49:50Z

## Research objective (distinct from certificate DAG issue #47)

Turn a **local** comparison lower-bound obstruction into a theorem about the **initial antichain** (S(n)). Focus on the (orall)-sorter / (exists)-adversary quantifier structure; do not confuse a poset being *reachable via some transcript* with an adversary being able to force it against an optimal sorter.

**Only unary (S(n))**. Remote execution authorized **only on billy-dev** if it returns; while offline, conduct paper research and GitHub review. No new Lean formalization unless a substantial all-(n) root theorem with a complexity consequence has already survived independent scrutiny.

## Existing precise evidence

The 7-element successor-mask poset
`B=(0,0,2,1,1,9,59)` has (e(B)=60) and (F(B)=7), although (lceil log_2 e(B)ceil=6). The lower bound is **one-ply**: all 11 incomparable pairs have an orientation outcome containing at least 34 of the 60 linear extensions, exceeding (2^{6-1}=32). Ordered sums (B^{oplus q}) have a linear comparison deficit relative to (lceillog eceil). However, ordinal factorization makes their residual (F) computable easily, and these structures are **not established as forced states** in the initial sorting game.

The strict gap (S(12)=30>lceillog_2(12!)ceil=29) is known; do not mislabel Stober–Weiß's search-bandwidth parameter as a proven bottleneck distribution. See [ALENEX 2023 / arXiv:2206.05597](https://arxiv.org/abs/2206.05597), and `docs/research-obstruction-next.md`.

## Two independent proof targets

1. **Sound root-relevant lower-bound grammar.** Propose a polynomially verifiable structural rule (L(P,h)) with provable implication (F(P)>h) that is stronger than linear-extension counts, and show how it *propagates backwards under every comparison choice*. Derive a nontrivial, **all-(n)** lower bound for (S(n)), or a rigorous no-go for the proposed grammar. Budget in the definition must be explicit.
2. **Quantified forcing of gadgets.** Formulate a theorem (orall) height-(k) comparison policies (T), (exists) a consistent answer path reaching a certified obstruction before exhaustion of its remaining budget. Seek an infinite explicit family or demonstrate a precise counterstrategy against any attractive proposed forcing invariant. Experiments with (nle 8) can falsify hypotheses but cannot serve as a complexity theorem.

## Deliverable and stop rule

Return a checked all-(n) lemma and exact explanation of whether it improves a *comparison lower bound* or the much harder *complexity of evaluating (S(n))*. These are different. If all routes stop at root unreachability, document **one exact obstruction and an explicit reason** instead of producing a sequence of minor Lean results, repeated finite tables, or optimistic board comments.

For perspective, `SORT-BOUND-U∈PSPACE` is already known. An unconditional proof that it lies outside P would imply (P
e PSPACE); claiming a routine finite-search state blowup as such a separation is invalid.

## Comments

### None — ottojung
Comment ID: 6350140834
Upstream: https://github.com/ottojung/soringp1/issues/48#issuecomment-6350140834

### Hard asymptotic feasibility gate: linear root amplification is **impossible**

Any proposal that **forces a positive constant information-deficit per element** at the *initial antichain* is already refuted by an established theorem. Sergeev [ECCC TR20-096](https://eccc.weizmann.ac.il/report/2020/096/) proves
`S(n) <= log2(n!) + O(n/(log n)^(1/5))`.
Consequently
`0 <= S(n)-ceil(log2(n!)) <= O(n/(log n)^(1/5)) = o(n)`.

Therefore a construction attempting to transfer **q=Theta(n) copies** of the local B-gadget's one-comparison deficit into an additive **Omega(n)** root lower bound cannot succeed, regardless of how clever its forcing argument seems. Those independent-block adversary costs are cancelled, bypassed or inapplicable before reaching the initial antichain root.

**Corrected proof target:** an unbounded but **sublinear** lower gap along an explicit infinite family, or any nontrivial uniform obstruction explaining which n have strictly positive gap. For the *complexity of evaluating S(n)*, even such a comparison-count bound is not a hardness result; the priority is a constructive local certificate grammar with a credible route to the **exact threshold**.

**Falsification requirement for an agent:** Before attempting to force many local gadgets, calculate the cumulative information deficit of the proposed root adversary and compare it with Sergeev's `o(n)` global slack. Reject immediately if it predicts a positive linear gap. Do not Lean-formalize a local ordinal-sum additive comparison deficit without a root transfer theorem compatible with this upper bound.

---

