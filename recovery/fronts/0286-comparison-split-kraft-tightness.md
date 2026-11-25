# comparison-split-kraft-tightness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

T8Q1K7z6sQbxS7MqSSeKla-mounted

## exit_state

clearexit

## question

For the all-n family of comparison-split trees induced by optimal play, is the Kraft sum inequality S = sum 2^{-depth(leaf)} <= 1 always realizable with equality for some infinite subfamily while being strictly subunit on others, and does any infinite family force S <= 1 - c/n^p for fixed c>0,p>=0 preventing a known info-tight construction?

## basis

Kraft inequality is necessary for prefix codes/decision trees; comparison tests have extra structure beyond arbitrary tests; prior fronts tested Kraft obstructions but none gave a tight all-n slack characterization tied to S(n).

## falsifier

Construct an explicit infinite all-n poset family reachable at root with Kraft slack bounded below by Omega(1/poly(n)) for every comparison-split realization, or show Kraft equality is achievable for all sufficiently large n by a uniform construction.

## implication

A uniform all-n Kraft-slack lower bound would rule out any strategy achieving the full information-theoretic height C(n)=ceil(log2 n!) asymptotically via simple splits, independent of the winning frontier enumeration barrier.

## finding_unverified

zing worst-case height) would never do this. Pruning such branches yields nodes with a single child, breaking fullness and giving $\sum 2^{-d(\ell)} < 1$. In the standard minimax (sorter/adversary) game for $S(n)$, optimal sorter strategies do not produce useless comparisons, so the induced trees are full binary with $\sum 2^{-d(\ell)}=1$ for all $n$. The adversary cannot force the sorter to create Kraft slack by useless comparisons; doing so hurts the sorter. Thus Kraft equality is *universal* for optimal-play trees, not "realizable with equality for some infinite subfamily while strictly subunit on others".

**3) The real obstruction is split-realizability, not Kraft capacity.**
The constraint is: from state $P$ with $e(P)$ linear extensions, comparing incomparable $u,v$ gives a partition $(e(P+uv), e(P+vu))$ with sum $e(P)$ where both are extension counts of posets obtained by adding that relation. These are not arbitrary splits — they come from the permutohedron/order constraints. 
- **Divisibility/modular obstructions exist.** The exact-reset case (antichain → star, odd $n$) shows branch masses from the root comparison are not compatible with required leaf class sizes even though totals match (this is stronger than Kraft/counting alone). This is about *realizability of specific partitions*, not about $\sum 2^{-d(\ell)} < 1$.
- **Asymptotically no known Kraft-slack barrier.** Kahn–Saks guarantees balanced comparisons exist in some sense; Sergeev achieves $S(n)=\log_2(n!)+o(n)=C(n)+o(n)$, approaching the information bound asymptotically. No infinite all-$n$ family is known to force $S \le 1 - c/n^p$ preventing asymptotic approach to $C(n)$.

**4) Distinction from general posets.**
Results about arbitrary partial orders do not transfer automatically to the antichain family/root of sorting. The branch-divisibility obstruction is real for exact resets, but it blocks *exact* transitions to specific posets, not the existence of some comparison tree achieving height near $C(n)$ for sorting all permutations.

### Assessment of the proposed falsifier
The falsifier asks to "construct an explicit infinite all-$n$ poset family reachable at root with Kraft slack bounded below by $\Omega(1/poly(n))$ for every comparison-split realization, or show Kraft equality is achievable for all sufficiently large $n$ by a uniform construction." 
- **For proper (optimal-play) trees:** Kraft equality is necessary by tree structure, so you cannot have $\Omega(1/poly(n))$ slack below 1 from Kraft; the first branch is impossible for non-wasteful trees. 
- **For wasteful trees:** slack is easy to create but irrelevant to optimal play/minimizing height. 
- **The comparison constraint gives a different kind of obstruction** (partition realizability/divisibility) which is not captured by the scalar Kraft sum $S=\sum 2^{-d(\ell)}$. 

**Conclusion:** The Kraft-sum formulation as stated does not correctly identify the obstruction for comparison-split trees induced by optimal play. The productive direction is split-realizability (e.g. divisibility/modular constraints on $(e(P+uv),e(P+vu))$) rather than the prefix-code Kraft inequality. No obvious infinite all-$n$ Kraft-slack obstruction emerges; any attempt would need to first distinguish "full binary / no useless comparisons" (Kraft equality automatic) from "wasteful" trees (irrelevant to $S(n)$ optimization). This is a structural point: Kraft capacity is not the bottleneck; comparison-split *geometry/realizability* is.

## Other metadata

```json
{
  "finished_at": 1793803869.233485,
  "started_at": 1793801912.7502823
}
```
