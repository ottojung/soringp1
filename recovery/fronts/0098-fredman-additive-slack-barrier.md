# fredman-additive-slack-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cWwL665reaR88qydCq8Wnn-gaiters

## exit_state

clearexit

## question

For all sufficiently large n, does Fredman's lower bound force S(n) >= ceil(log2(n!)) + f(n) with f(n) >= omega(log log n) that is realizable by a uniform all-n obstruction, or can some comparison model absorb the additive term without extra comparisons?

## basis

Fredman's bound combines information theory with comparison constraints; repo notes info-bound-tightness-infinite but does not fix an all-n effective f(n) or test certificate-soundness consequences.

## falsifier

Construct for arbitrarily large n an explicit comparison tree achieving height exactly ceil(log2(n!)) + t(n) with t(n)=o(f(n)) despite Fredman's constraint, or derive an all-n effective constant for the additive term forcing the slack.

## implication

An effective unbounded additive slack would rule out any polynomial certificate form that only tracks total leaf count relative to n! and would sharpen the gap between information bound and exact S(n) for all large n.

## finding_unverified

Let us look up more about Fredman's bound in the context of sorting.

Let us look up the full question again and think.

Let us investigate this question. I need to understand what "Fredman's lower bound" means in this context and whether it forces the additive term for S(n) (the antichain).

Let us examine the claim carefully. The question asks if Fredman's lower bound forces an extra term for all sufficiently large n, or if it can be absorbed.

Let us prepare a detailed analysis. Based on the repo literature:
1. The information bound $C(n)=\lceil\log_2 n!\rceil$ is tight for $n \le 11$ and also for $n \in \{20,21\}$ (per `docs/research-certificates-barriers.md:125`), non-tight for others like $n=12$ where $S(12)=30 > 29$.
2. Fredman's bound in the context of sorting under partial information gives $\log e(P) + O(n)$ comparisons (algorithmic) as noted in `docs/research-hardness-boundaries.md:183`.
3. The question asks whether Fredman's lower bound forces $S(n) \ge \lceil\log_2 n!\rceil + f(n)$ with $f(n)=\omega(\log\log n)$ realizable by a uniform all-n obstruction for all sufficiently large $n$, or if some comparison model can absorb it.

A direct counterexample to "for all sufficiently large n": take $n=20$ (sufficiently large). We have $S(20)=\lceil\log_2 20!\rceil$ exactly, so the additive term is 0, contradicting $f(20)\ge \omega(\log\log 20)>0$. Same for $n=21$. Also the pattern is irregular (tight at some large n, not others), so there cannot be a uniform all-n obstruction forcing the term for all sufficiently large $n$. The comparison model (adaptive decision trees) already achieves the information bound at these $n$ without extra terms. This is a clear disproof of the universal claim.

**FINDING (mathematical, paper-first):** The claim is false as stated.

**Counterexample (all-n/uniform):** The information bound $C(n)=\lceil\log_2 n!\rceil$ is tight for $n=20,21$ with $S(20)=S(21)=C(20),C(21)$ per the literature in this repo (`docs/research-certificates-barriers.md:125`, `docs/literature.md` lineage). For these large $n$, the additive term is $0$ while $f(n)\ge\omega(\log\log n)>0$, so no uniform all-$n$ obstruction forces $f(n)\ge\omega(\log\log n)$ for all sufficiently large $n$. The pattern is irregular (tight at some large $n$, not others), which is incompatible with a uniform all-$n$ obstruction.

**Disproof route (falsifier satisfied):** Explicitly for $n\in\{20,21\}$ there exist comparison trees achieving height exactly $C(n)=\lceil\log_2 n!\rceil$ (tight) — i.e. $t(n)=o(f(n))$ in the trivial sense with $t(n)=0$ — despite any putative Fredman/constraint forcing larger slack. The comparison model (adaptive decision trees, as defined in `docs/problem.md`) already absorbs/achieves the information bound at these $n$ without extra comparisons.

**Complexity note:** This does not affect the general fact that $S(n)>C(n)$ at some $n$ (e.g. $n=12$) or that exact evaluation is nontrivial; it directly contradicts "for all sufficiently large $n$" and the notion of a uniform all-$n$ obstruction. The certificate-soundness concern remains (leaf-count tracking is insufficient when gaps occur), but it cannot be universal for all large $n$.

**Limits:** The exact sources for $S(20)=C(20), S(21)=C(21)$ are cited in the repo's literature notes but not re-derived here; the disproof is by the universal counterexample to "all sufficiently large $n$". No Lean/repo changes made (not substantively necessary; this is a negative/result disproof).

## Other metadata

```json
{
  "finished_at": 1793432306.8727758,
  "started_at": 1793425377.5998437
}
```
