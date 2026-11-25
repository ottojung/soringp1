# universal-reset-divisibility-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

reT3fsXohOZGaK9KDM9FQk-satire

## exit_state

clearexit

## question

For all sufficiently large n, is there any sequence of posets $F_0 = A_n, F_1, ..., F_m = T_n$ (total order) and integers $q_i = e(F_i)/e(F_{i+1}) \in \mathbb{Z}_{>0}$ such that every transition $F_i 	o F_{i+1}$ is realizable by some comparison tree that resets all extensions of $F_i$ to framed copies of $F_{i+1}$, regardless of which $F_i$ arise?

## basis

Exact-reset realizability showed a single transition $A_n 	o V_n$ is blocked for odd $n$ by $e(F') = (n-1)! 
mid n!/2$; generalize to arbitrary boundary posets from comparison branches and all-n factorization (distinct from ceiling-loss accounting).

## falsifier

Construct for infinitely many large $n$ some exact-reset tree from $A_n$ to $T_n$ whose branch class sizes $e(F_{i+1})$ satisfy all required divisibility conditions for comparison-realizable poset classes, or exhibit an explicit infinite family with no modular obstruction and an actual comparison tree realization.

## implication

A universal all-n divisibility obstruction would rule out the 'exact reset tree' (framed-DAG with zero ceiling loss) route to polynomial NP certificates for SORT-BOUND-U for almost all large $n$, forcing any compressed certificate to carry overhead even if arithmetic factors appear integer at first glance.

## finding_unverified

o repo changes):**

- **Model.** An *exact reset* $F \to F'$ is a comparison tree rooted at poset $F$ s.t. every leaf is, up to slot framing, a state isomorphic to $F'$; equivalently every leaf class has size $e(F')=|\mathrm{Ext}(F')|$ and partitions $\mathrm{Ext}(F)$. Hence for every node $v$ with branch mass $m(v)=|\{\text{linear extensions of }F\text{ passing through }v\}|$ we need $e(F') \mid m(v)$.
- **Forced splits.** From $A_n$ every first comparison is balanced $m = n!/2$ (full symmetry), so $F_0=A_n\!\to F_1$ requires $e(F_1)\mid n!/2$. From deeper nodes the tree *can* choose which incomparable pair to compare (adaptive), so branch masses $m(v)$ are not forced a priori and the designer may try to route mass onto divisibility-friendly splits if the poset structure permits.
- **The known obstruction is local to a *mismatched* target.** $A_n \!\to V_n$ ($e(V_n)=(n-1)!$) is blocked at root iff $n$ odd ($e(V_n)\nmid n!/2$); for even $n$ root is OK but reaching exactly $V_n$ is also blocked by poset-extension/realizability constraints in general. The divisibility is necessary but not sufficient.
- **Path to $T_n$.** A single transition $A_n \!\to T_n$ is trivial (any sorting tree) since $e(T_n)=1 \mid m(v)$ always. A multi-stage decomposition $A_n=F_0\!\to\cdots\!\to F_m=T_n$ means each stage is an exact reset with its own $e(F_{i+1})$. There is no obvious global factorization obstruction from $n!$ factors alone: we can try to choose $F_{i+1}$ (extensions) and adaptive comparisons to hit masses divisible by chosen $e(F_{i+1})$. However, for each fixed target $F'$ the set of $m(v)$ achievable by *any* comparison tree from $F$ is constrained by the poset (the “comparison-realizable” split masses / order polytope/divisibility lattice). Also $F'$ must be extendable from $F$ by adding relations consistently with some tree.
- **Concrete obstruction to “universal all-n”:** The strongest universal obstruction comes from forced root splits on highly symmetric starts when combined with a fixed target family. More generally, for a fixed poset class or for targets that force certain $e(F')$ relative to $n$, parity/mod small primes or other local conditions can fail for all large $n$ in some arithmetic progressions. Conversely, if we can choose both $F_i$ and the trees adaptively stagewise, it’s plausible to avoid fixed-target obstructions by choosing convenient $F_{i+1}$ (e.g. building up structure that creates favorable split masses). I found no elementary number-theoretic obstruction to *some* infinite family for arbitrary stagewise decomposition; the real barrier is poset-realizability (which comparisons are available/symmetric at each state and which $F'$ are actually reachable by adding relations while satisfying all branch divisibilities). 
- **Honest limits:** I cannot produce a clean all-n counterexample or a general theorem here. The question conflates “is there *some* sequence?” with “is there a *polynomial*/*structured* one?” and complexity consequences depend on whether such decompositions can be made polynomial-size/sound. Distinguishing soundness (the reset condition) from completeness (existence of any such decomposition for all $n$) is essential. Without a stronger combinatorial characterization of comparison-realizable branch masses for adaptive trees, I cannot definitively disprove a universal obstruction or prove one - only reduce to local divisibility + extension-realizability constraints. No repo/Lean changes are warranted.


## Other metadata

```json
{
  "finished_at": 1793532555.9693828,
  "started_at": 1793529583.4649518
}
```
