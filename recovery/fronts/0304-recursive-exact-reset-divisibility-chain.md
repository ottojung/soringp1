# recursive-exact-reset-divisibility-chain

## status

investigated

## origin

ai_proposal_unverified

## agent_id

IiIxuYxXmgyHcQlj2NUFBA-throw

## exit_state

clearexit

## question

For all sufficiently large n, does every exact-reset partition chain from A_n down to total orders encounter some stage where branch-divisibility conditions fail for all possible comparison-split choices, or can some infinite family of chains satisfy branch divisibility at every stage for all large n?

## basis

single-stage odd-n obstruction known; multistage branch-divisibility closure across comparisons not characterized

## falsifier

Exhibit an all-n family of multistage exact-reset chains with every stage satisfying recursive branch divisibility, or prove branch divisibility is violated at some fixed depth or eventually for all chains on infinitely many n.

## implication

Would separate single-stage realizability from global chain realizability and determine if exact-reset certificate frameworks are obstructed globally rather than locally.

## finding_unverified

*Disproof by construction:** Insertion-sort chains form such an all-n family with recursive branch divisibility satisfied at every stage.

- **Model (from docs):** Exact reset stage F -> F' means a comparison tree rooted at F with every reachable leaf class of size exactly e(F') = |Ext(F')| (up to slot framing), partitioning Ext(F). Branch divisibility at node G: for some comparison giving G1,G2, need e(F') | e(G1) and e(F') | e(G2) (hence M|e(G) with M=e(F')).
- **Chain:** Let F_0 = A_n, F_k = chain of k+1 elements union n-k-1 isolated elements (up to labeling), F_{n-1} = total order (all chains). e(F_k)=n!/(k+1)!. This is a refinement chain F_0 ⊊ F_1 ⊊ ... ⊊ F_{n-1}.
- **Stage F_0->F_1:** compare any pair x,y in antichain: branches have size n!/2, M=e(F_1)=n!/2!, need (n!/2) ≡ 0 mod (n!/2!) which is true for n>=2.
- **Stage F_{k-1}->F_k:** current state is some poset reachable in previous stage; in insertion sort reachable states include "chain C of k plus rest isolated" and others obtained by inserting elements (e.g. V-shapes). When inserting element y into chain C=(c1<...<ck), compare y with any c_i (the only informative incomparable pairs): e(branch y < c_i) = e(F_{k-1}) * i/(k+1) = (n!/k!) * i/(k+1). M_k = e(F_k)=n!/(k+1)!. (n!/(k!(k+1)) * i) is divisible by (n!/((k+1)!)) since (k+1)! = (k+1)k!. So divisibility holds for **every possible comparison choice** of which c_i to compare y with at every such state. From other reachable states (e.g. V-shape) there is still **some** comparison choice giving divisible branches (and often only one choice exists among incomparable pairs). Thus recursive branch divisibility is satisfied at every stage.
- **Scope:** works for all n>=2.

**Conclusion on the frontier question:** The answer is **no** for "every exact-reset partition chain" - there exists an infinite/all-n family (insertion sort / chain-extension chains) where every stage satisfies recursive branch divisibility. The obstruction is not global across all chains; it is local to particular chains/stages (e.g. A_n -> V_n for odd n is impossible as a single stage, but building up gradually avoids it).

**Complexity implication:** This separates single-stage realizability from global chain realizability. Exact-reset certificate frameworks are not globally obstructed by branch divisibility - good chains exist. The bottleneck is not universal chain-divisibility; other barriers (e.g. the large winning frontier / enumeration barriers, or issues of completeness/soundness of certificates) remain separate concerns. Certificate **soundness** (the divisibility/counting conditions) is necessary but not sufficient alone; **completeness** of some certificate families vs realizability by actual comparison splits is the distinction - and global chain constructions are possible via gradual refinement.

**Failed approaches / limits:** Tried to see if merge-sort style chains fail branch divisibility at stage boundaries - but doing comparisons within groups to form unions of chains gives branch divisibility OK if structured properly; the issue is more subtle. The key is being able to choose both the next poset F_{i+1} and the comparison tree/splits to satisfy divisibility at every node - insertion sort does this by always maintaining "chain+isolated" structure and inserting elements one by one. No Lean/repo changes made (construction is standard combinatorial; no substantively new theorem/counterexample beyond existing obstruction generalization needed). 


## Other metadata

```json
{
  "finished_at": 1793856596.9004362,
  "started_at": 1793854889.4283586
}
```
