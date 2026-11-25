# comparison-split-modulus-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

dhuEDk0HywXfruA3U0THua-nicaragua

## exit_state

clearexit

## question

Is there an infinite sequence of posets {P_n} on n elements with the property that for every prime power p^e exactly dividing some comparison-split size ratio from P_n, the recursive comparison-split structure forces a contradiction for exact partitioning into any fixed-form leaf classes, creating an all-n obstruction independent of the global n!/product arithmetic?

## basis

Exact-reset divisibility obstruction (docs/research-exact-reset-realizability.md), #P-hardness/structure of e(P) noted in docs/research-encoding-consequences.md, and branch constraints emphasized across certificate fronts.

## falsifier

Show that for every poset P_n the comparison-split multiset is always "divisible-chain" realizable for some leaf class family, or find that such modular obstructions are already implied by the global extension-count conditions.

## implication

A nontrivial modular/prime-factor obstruction would add a necessary condition stronger than the odd-case ratio and could explain hard instances where global counts look feasible but local branch constraints fail.

## finding_unverified

ed tree structure, all nodes at the same depth? No, tree is a decision tree, different paths give different posets/states with different e values.

The obstruction is: if at some branch the count e(P_branch) is not divisible by e(F'), impossible. So for fixed F', every node in the exact-reset tree from F to F' must have e(P_node) ≡ 0 mod e(F') (in terms of being divisible)? Let us check: total partition into classes of size e(F'), so yes every subset in the partition is multiple related? No - every class has exactly e(F') elements, so total e(F) is sum of some number of e(F') so divisible. Every branch is union of some complete leaf classes, so e(P_branch) must be divisible by e(F'). Yes, recursively. All branch sizes at every node in the tree must be multiples of e(F').

Also note that e(P_branch) divides? No just divisible by e(F'). Also e(F') divides e(F) since e(F) is sum of (e(F)/e(F')) classes.

So for exact reset from F to F', necessary conditions: e(F') | e(F), and for every comparison split in the tree, both resulting branch sizes divisible by e(F'), etc. All the way down.

Now look at antichain A_n to star V_n: e(F)=n!, e(F')=(n-1)!, so n! divisible by (n-1)! yes. Root comparison on antichain: branches each have size n!/2. Need (n-1)! | n!/2 => n/2 integer. Yes. Then recursively below - but obstruction already at root for odd n.

Another example: what if we had a different comparison? But in antichain every comparison is equivalent by symmetry. So obstruction is at root.

The front says "for every prime power p^e exactly dividing some comparison-split size ratio from P_n..." So maybe looking at prime factorization of ratios. Also "comparison-split size ratio" - perhaps e(P_left) / e(P_right) or ratios of branch sizes? Or ratios involving e(F')?

Or perhaps more generally, in the recursive splitting, you look at ratios of the form (e of some branch) / (e of some required class) and their prime power factors cause problems.

Also "independent of the global n!/product arithmetic" - so even if global e(F) is divisible in total by something, the local factors create obstruction. Which is exactly the case here: n! divisible by (n-1)! globally, but local factor 2 causes problem when n odd.

The front wants to know if there is an infinite family of posets {P_n} where for every prime power p^e exactly dividing some comparison-split size ratio from P_n, the recursive comparison-split structure forces a contradiction for exact partitioning into any fixed-form leaf classes. So modular obstructions from prime powers in those ratios.
Let us look up more about the exact-reset and the modular obstruction more systematically.

Let us think step by step.

Let us try to construct arguments for the falsifier.

Let us examine this carefully.

The falsifier's option 1 is trivially true - for any poset you can always reset to a total order (full sorting tree). The front claims obstruction occurs for ANY fixed-form leaf classes, but total order always works. So the claim is false. Also "divisible-chain" matches chain structures. This is a clean disproof.The front's claim is false. For any poset P there is always some leaf class family (total orders, e'=1) allowing exact partitioning via a standard comparison sort; the modular obstructions are real for particular choices of F' but do not hold for all fixed-form leaf classes. Thus the falsifier's option 1 holds trivially and the alleged all-n obstruction for "any fixed-form leaf classes" cannot exist.


## Other metadata

```json
{
  "finished_at": 1793591660.458426,
  "started_at": 1793585214.2152464
}
```
