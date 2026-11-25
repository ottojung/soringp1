# adversarial-entropy-rate-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

q4n0j1l9M0svZBiZabb3y2-mode

## exit_state

clearexit

## question

Let H_b be the Shannon entropy of the adversary's outcome distribution at comparison nodes b on some strategy for A_n (uniform random linear extension / adversarial worst case for information). Is there an all-n constant ε>0 with E[∑ H_b / D] <= 1-ε over optimal-height strategies of any all-n family (adversarial entropy rate bounded below 1), or can some all-n strategy family keep adversarial entropy rate approaching 1 on all paths while achieving height S(n)?

## basis

Kahn-Saks/Kahn-Kim give balanced comparisons but translating to 'adversarial entropy rate' for exact S(n) all-n families is not settled; distinguish general-poset entropy from the fixed permutation-family constraints.

## falsifier

Give an all-n family of adaptive strategies with worst-case height S(n) such that for every ε>0 and all sufficiently large n, E[∑ H_b / D] >= 1-ε on the induced adversarial distribution, with a rigorous argument distinguishing this from the trivial 1-bit upper bound.

## implication

If adversarial entropy rate is universally bounded below 1 for height-optimal/all-n complete strategies, this constrains any information-theoretic NP-certificate model; if rate can approach 1, it weakens entropy-based ceiling arguments and points to other obstructions.

## finding_unverified

Let us start by reading the relevant docs in detail.

Let us look up more details about entropy in the docs.

**Finding (mathematical):** Disprove the “bounded below 1” (gap ε>0, rate ≤ 1−ε) claim for exact optimal-height strategies on the permutation family. Since $S(n)=(1+o(1))\log_2(n!)$ (Fredman/Ford–Johnson/Kahn–Saks improvements), for any strategy $T_n$ with $D(T_n)=S(n)$ and $H_i=h(p_i)\le 1$ we have $R(T_n,n)=\mathbb{E}_\pi[\sum H_i/D]\ge \log_2(n!)/S(n)\to 1$. The trivial upper bound is 1, so adversarial entropy rate approaches 1 for all all-n families of exact height-optimal strategies.

**Distinction:** This is a property of the fixed permutation (sorting) family, not general posets — Kahn–Saks gives balanced comparisons in general, but general-poset information bounds need not be asymptotically tight; here tightness of the information bound forces the rate to 1. This is about the accounting (total information budget), not that every comparison is “forced balanced” by adversary — it’s the converse effect of height-optimality.

**Complexity/certificate note:** This weakens entropy-based ceiling arguments for information-theoretic NP-certificate models (no universal constant deficit), so obstructions would need to come from other sources (state/completeness/soundness of candidate certificates). Certificate *soundness* vs *completeness* remain separate questions.

**Limits/failed routes:** The argument is asymptotic (ratio → 1), not giving an exact ε>0 for finite n or ruling out other obstructions; it doesn’t construct a short certificate or prove NP membership. I did not create repo/Lean changes (no substantive new theorem/counterexample beyond this standard asymptotic identification). No board post made here (environment not on billy-dev per instructions).

## Other metadata

```json
{
  "finished_at": 1793367590.1382475,
  "started_at": 1793367316.0853682
}
```
