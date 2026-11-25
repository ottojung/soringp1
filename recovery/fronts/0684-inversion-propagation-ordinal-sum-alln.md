# inversion-propagation-ordinal-sum-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

URCz2bmlU2wD33MRXnQkfC-exalted

## exit_state

clearexit

## question

If some finite poset P with m(P)>=2 is all-inverted (every minimax-optimal comparison sends strictly fewer linear extensions to its minimax-harder child), does taking ordinal sums P, P(+)P, P(+)P(+)P, ... force all-inverted posets at every larger minimax depth, or can all-inversion be an isolated, non-propagating phenomenon confined to finitely many depths?

## basis

Board #301 05:30Z reports a paper proof that tight states are inversion-free and exhaustively verifies Claim C through n=9, leaving the all-n case open. The core-threshold note proves ordinal sums make m additive and e multiplicative, and the ledger's minimal-first-violation-lift front concerns depth-balance violation, not extension inversion.

## falsifier

Exhibit an all-inverted poset P whose ordinal-sum power P^{(+t)} fails to be all-inverted for some t>=2, or prove that the set of minimax depths m admitting an all-inverted poset is finite.

## implication

If all-inversion propagates under ordinal sums, a single finite counterexample refutes the all-n extension-monotone claim for infinitely many n and rules out extension-order-guided evaluators outright; isolation would confine the counterexample search to a finite depth range.

## finding_unverified

ng` with no finding; the board had **no** post for this front (`--contains "propagation"` / `"minimax depths"` = 0; the only "inverted" hit is the sibling front's 05:30Z post). Nothing was duplicated. I posted **exactly one** #301 comment (05:54:45Z, confirmed by digest).

## Mathematical finding

I proved the front's main question outright: **all-inversion propagates under ordinal sums, and is fully characterized by them.**

Setup (definitions from board #301 05:30Z): for a finite poset, an optimal comparison has hard child $H$ with $m(H)=m-1$ and easy child $E$ with $m(E)\le m-2$; a *sibling extension inversion* is $m(H)>m(E)$ but $e(H)<e(E)$. Poset $P$ is **all-inverted** iff $m(P)\ge 2$ and *every* optimal comparison is an inversion (equivalently, Claim C fails at $P$).

**Theorem (paper proof).** Let $C=A\oplus B$. Then:
1. The optimal comparisons of $C$ are exactly the optimal comparisons *inside* $A$ or *inside* $B$; a cross-block comparison is order-determined ($A$-elements $< B$-elements) and never optimal.
2. For any within-block optimal comparison, the hard/easy designation and the inversion status are **identical** in the block and in $C$: appending a block $Q$ multiplies both children's extension counts by $e(Q)$ and adds $m(Q)$ to both minimax values, so $e(H\oplus Q)<e(E\oplus Q)\iff e(H)<e(E)$, and likewise for $m$.

Hence **$A\oplus B$ is all-inverted $\iff$ $m(A\oplus B)\ge 2$ and every block with $m\ge 1$ is all-inverted** ($m=0$ total-order blocks are free; an $m=1$ block forces a tie and kills all-inversion). In particular, if $P$ is all-inverted with $m_0\ge2$, then $P^{(+t)}$ is all-inverted with $m=t\,m_0$, $e=e(P)^t$ for **all** $t\ge1$.

Basis: $e$ multiplicative and $m$ additive under ordinal sum are already proved in `docs/research-series-decomposition.md` §2 (additivity = Jain–Klauck–Sántha deterministic direct-sum, IPL 2010); steps 1–2 are definitional. I independently verified the whole statement from first principles in scratch (2,600 block pairs, $n\le4$: 0 failures; 0 all-inverted posets at $n\le4$).

## Falsifier / complexity implication

- The **isolation horn is impossible conditional on existence**: one all-inverted $P$ yields all-inverted posets at depths $m_0,2m_0,3m_0,\dots$, so that depth set is infinite. My serious attempt to exhibit a falsifying $P\oplus P$ failed precisely because propagation is provably true.
- The other horn ("prove the set of depths finite") is **exactly Claim C** — no all-inverted finite poset exists — which is the still-open `optimal-move-extension-monotonicity-alln` front. So this front yields **no new theorem** about $S(n)$ or `SORT-BOUND-U`; it collapses into that open claim. It is a sound general-poset structural result, not a certificate or complexity theorem.

## Honest limits

- **Conditional.** No all-inverted poset is known (none up to $n=9$ on the board; scratch confirms none $\le4$), so propagation has no known instance. I did not refute Claim C.
- No larger witness search was attempted (the earlier $n\le14$ chain-merge search was killed by the backend failure; exhaustive $n\ge10$ is infeasible).
- Even a positive Claim C gives only a monotone-optimal strategy *normal form*, not a polynomial certificate/evaluator: $e(P)$ is #P-complete and finding the minimax-harder child requires solving minimax. No PSPACE improvement, no NP/coNP placement, no new $S(n)$ value.

No repository, Lean, or ledger changes were made; the single board post is my only external write.

## Other metadata

```json
{
  "finished_at": 1795326916.4661937,
  "started_at": 1795326095.4994562
}
```
