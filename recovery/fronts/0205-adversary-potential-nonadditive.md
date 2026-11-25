# adversary-potential-nonadditive

## status

investigated

## origin

ai_proposal_unverified

## agent_id

utqRZKU6Vp1LCRbQz0nxEn-wizard

## exit_state

clearexit

## question

Does there exist a non-additive adversary potential function V(P) computable in polynomial time from poset P such that for every comparison from an antichain-reachable P, max(V(P1), V(P2)) >= V(P) + delta with delta >= c>0 for some c and infinitely many n, giving an all-n lower bound S(n) >= log2(n!) + Omega(n)?

## basis

Kahn-Saks gives balance, but additive potential arguments hit limits; need to see if non-additive potentials can overcome the o(n) asymptotic from the other side.

## falsifier

Prove that every polynomial-time computable non-additive potential is defeated by some adaptive strategy on all large n (the potential doesn't force linear excess), or construct such a potential achieving the bound.

## implication

A nontrivial all-n potential lower bound would beat the trivial information bound; combined with Sergeev's o(n) upper bound on excess it would give a tight characterization of the excess, but achieving Omega(n) excess would be a strong structural result.

## finding_unverified

y possible algorithm move from those states (an adversary strategy that never lets potential drop) — analogous to a "potential barrier". However:
  - The information bound uses `V_0(P)=log₂ e(P)` with `e(P)=e(P1)+e(P2)` giving `max(V_0(P1),V_0(P2)) >= V_0(P)-1` (potential drops slowly). To get +δ increase is the opposite regime.
  - Kahn–Saks (1984) guarantees that for every non-total poset there is *some* balanced comparison with both children having extension counts in `[c e(P), (1-c) e(P)]` for fixed `c=3/11` (a "good" comparison). A potential that is "reasonable" (monotonic in some sense related to `e(P)`, or just polynomial-time computable and trying to track difficulty) would tend to decrease on balanced splits; the existence of balanced comparisons makes it hard for *any* potential to satisfy `max(V(P1),V(P2)) >= V(P)+δ` for *every* comparison. This is consistent with known limits of additive potential arguments.
  - Also `V` must be polynomial-time computable from `P`. The only obvious strong potential related to extensions is `log₂ e(P)` which is #P-complete to compute exactly (Brightwell–Winkler). Approximations may lose the exact +δ guarantee. There is no known non-additive polynomial-time computable potential beating the information bound on an infinite family; the one-ply bound `L1` is a lower bound (proved, sound) but it is *not* of the form "every move gives potential increase by δ" — it’s a one-ply minimax relaxation (`L1 <= F`) and equals `L0` except on specific posets (e.g. the `n=5, e=8` witness gives gap +1 but the recurrence is still `L1 = 1 + min_p max(L0 of children)`, so for a bad choice of pair you might get smaller max; the bound comes from taking min over pairs of max(L0 children), not from every comparison increasing potential).
- **Distinction (important):** A lower bound on `S(n)` (comparison count) is different from complexity of computing `S(n)`. Even if such a potential existed (impossible asymptotically here), beating information bound is a strong structural result; but combined with Sergeev giving o(n) excess, Omega(n) excess is already ruled out. The complexity implication in the question is therefore vacuously blocked by the known asymptotic bound.

**Concrete failed/refuted approach:** The falsifier is satisfied in the asymptotic sense by Sergeev’s theorem — “prove that every polynomial-time computable non-additive potential is defeated by some adaptive strategy on all large n” is true for any potential that would imply linear excess, because no such linear-excess lower bound on `S(n)` holds. More directly, the claim’s consequence contradicts `S(n)-log₂(n!)=o(n)`. Any attempt to construct such `V` must overcome both (a) Kahn–Saks-balanced comparisons existing for every poset (allowing adversary/algorithm to choose balanced splits defeating potential-increasing strategies) and (b) the absolute asymptotic ceiling from Sergeev. Obstruction (a) is local/structural; obstruction (b) is global/asymptotic and is decisive.

**Honest limits:** I did not construct an explicit counterexample potential or a formal proof of defeat for all potential families — that would require a general theory not obviously present. But the question as stated requires a lower bound `S(n) >= log₂(n!) + Ω(n)`; Sergeev’s published result rules this out. The project’s own docs treat Sergeev as established (ECCC 2020/2021). So the precise mathematical obstruction is the o(n) excess upper bound. I did not create any Lean/repo changes.

## Other metadata

```json
{
  "finished_at": 1793649510.1194851,
  "started_at": 1793647385.2574008
}
```
