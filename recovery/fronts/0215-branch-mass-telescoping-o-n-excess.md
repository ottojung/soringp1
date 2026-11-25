# branch-mass-telescoping-o-n-excess

## status

investigated

## origin

ai_proposal_unverified

## agent_id

SXDF9B3meVaGexTVR1mrHY-calling

## exit_state

clearexit

## question

Is there an all-n inequality showing that any comparison tree with height <= log2(n!)+o(n) must incur aggregate forgetting/branch-mass telescoping loss >= Omega(n / f(n)) for some slowly growing f, forcing excess >= Omega(n/polylog n)?

## basis

Exact-reset branch-divisibility obstruction generalizes to non-exact splits; Kraft is necessary but not sufficient and comparison realizability gives stronger mass constraints.

## falsifier

Exhibit for every epsilon>0 a uniform family of comparison trees of height <= log2(n!)+epsilon*n for all large n with uniformly bounded or o(n) telescoped branch-mass loss under some sound framed join model.

## implication

A linear (up to polylog) excess lower bound from realizability of branch masses would constrain how close any exact evaluator can approach the information bound without relying on arbitrary prefix-code arguments.

## finding_unverified

Let us start by reading more about the branch mass/telescoping in context and also look up any existing analysis of this specific claim on board or in codebase.

Let us study the exact-reset obstruction more deeply and the telescoping identity, then think.

**Mathematical finding (disproof of the front claim):**

The inequality is false. The exact-reset branch-divisibility obstruction (*docs/research-exact-reset-realizability.md*) is **critical** to exact partitioning: from antichain to a star (odd n) root split gives n/2 not integer relative to leaf classes of fixed size `(n-1)!`, so no exact reset tree exists. That obstruction **does not generalize to non-exact/forgetful framed joins**.

- **Soundness vs completeness (crucial):** in a framed certificate with forgetting, a node annotation Q is allowed to be larger than the union of needed sets (`e(Q) >= m_b`) so we pay forgetting loss `λ_b = log2(e(Q)/m_b) >= 0` (*docs/research-framed-certificate-frontier.md* §4). The divisibility/partitioning constraint that killed exact resets disappears because we need not partition into classes of fixed exact sizes.
- **Known counterexample family:** I. Sergeev (*On the asymptotic complexity of sorting*, ECCC TR20-096, 2020) gives `S(n)=log₂(n!)+O(n/(log n)^(1/5))`. Thus for every ε>0 there is a uniform family of comparison trees with height `≤ log₂(n!)+εn` for all large n and **excess `o(n)`**.
- **Telescoped loss:** under the framed/certificate model, excess `E[D]-log₂(n!) = E[∑ (1-H + λ_b)]` (§4). For a tree (or tree-like representation) `λ_b=0` and loss is just split-entropy imbalance `∑(1-H)`. For compressed DAGs `λ_b` is the forgetting term. Sergeev’s near-information-bound construction has `o(n)` total excess, so its aggregate telescoped branch-mass loss is `o(n)` when modeled in a sound framed join model. This directly satisfies the falsifier and contradicts “any comparison tree…” incurring `Ω(n/f(n))` loss forcing `Ω(n/polylog n)` excess.
- **Constraints remain but are not fatal:** Kraft is necessary but not sufficient and comparison realizability is stronger; the exact-reset shows divisibility is real for *exact* transitions. However those stronger constraints do not force linear (up to polylog) aggregate loss — they are satisfiable arbitrarily close to the information bound asymptotically.

**Concrete failed approach / obstruction I tried to find:** I looked for a generalization of the odd-n divisibility to non-exact splits (allowing arbitrary `e(Q)≥m_b`). No such all-n obstruction emerges from the definitions alone; the degrees of freedom (forgetting, choice of Q/frames, tree structure) are enough that Sergeev’s construction is not ruled out. A proof attempt would need to show some other realizability constraint forces `∑(1-H+λ_b)=Ω(n/f(n))` for *all* comparison trees achieving near-information bound — but I see no obvious all-n combinatorial obstruction and the known asymptotic result is the opposite.

**Honest limits:** This is a paper-level disproof by existence of a counterexample family (Sergeev), not a new theorem proved here. I did not create Lean/repo changes. The point is distinguishing exactness (divisibility kills exact resets) from non-exact sound joins (relaxes it) — which matches “distinguish general-poset results and certificate SOUNDNESS from completeness” as requested. No new obstruction found; the front claim is false.

## Other metadata

```json
{
  "finished_at": 1793676270.5590522,
  "started_at": 1793675708.4191494
}
```
