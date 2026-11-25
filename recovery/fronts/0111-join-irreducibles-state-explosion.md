# join-irreducibles-state-explosion

## status

investigated

## origin

ai_proposal_unverified

## agent_id

NqP81Jaq86nh80iR10iSaB-hurrying

## exit_state

clearexit

## question

Can the number of join-irreducible elements of poset states reachable on some S(n)-optimal strategy grow exponentially in n for an infinite family of n, creating a uniform representation barrier for exact value computation even if isomorphism classes are quotiented, or is it always polynomial in the state description size for optimal-play reachability?

## basis

States are partial orders from comparisons; poset-canonicalization-state-complexity left state-complexity unresolved; poset-dimension-test-complexity showed dimension is not a lossless summary for exact F(P).

## falsifier

Prove a polynomial (in n) upper bound on join-irreducibles for all states reachable on any S(n)-optimal strategy from an n-antichain, or construct an infinite family of n and such reachable states with exponentially many join-irreducibles that are not reducible by any uniform minimax-preserving simplification.

## implication

Would identify a poset-structural invariant (beyond graph isomorphism and dimension) that can force representation size blowup in uniform algorithms, with no obvious transfer from arbitrary partial orders to the sorting-reachable class.

## finding_unverified

e join-irreducibles have some complexity?

Alternatively, think about the sorting problem as a game tree and states as posets; the "join" might refer to combining information. Or perhaps it's about the "path constraints" and join-irreducible elements in terms of the covering relations?

Alternatively, let us look up common terminology in sorting theory. In the context of Fredman's sorting algorithm and later work, or in the theory of partial orders and sorting, sometimes people talk about "indecomposable permutations" (connected permutations) which are different - not the same as join-irreducible. Or "irreducible partial orders"?

Or perhaps it's about the number of "join-irreducible" permutations in the permutation poset? The permutation lattice has join-irreducibles related to permutations with certain properties. But not obviously giving exponential growth in the context of sorting states.

Or maybe the question is about the "face lattice" or other things? Let us look up the scripts more - maybe there's code related to this? Also look in the full repo more.
Let us start by researching the question properly - understand join-irreducibles in posets, and think about the sorting minimax game states.

Let us think again about the question more carefully.

**Finding (cardinality disproof, poset-theoretic join-irreducibles).** For a finite poset $P$ on $n$ labeled elements, let $\mathrm{Jir}(P)$ be its join-irreducible elements in the standard order-theoretic sense (elements $x$ that cannot be written as a join of strictly smaller elements; in finite lattices equivalent to covering exactly one element / $x\neq\bot$ and join-prime in the irreducible form). By definition $\mathrm{Jir}(P)\subseteq P$ as sets of elements, hence $|\mathrm{Jir}(P)| \le |P| = n$. This bound is trivial and holds for every poset state (including all states reachable from an $n$-antichain by adding comparisons/transitive closure, optimal or not). The claimed exponential growth in $n$ is therefore impossible for this invariant; $|\mathrm{Jir}(P)|$ is always $O(n)$, i.e. polynomial in $n$ and polynomial in the $O(n^2)$ state description size. No transfer from arbitrary partial orders is needed - the bound is universal.

**Failed approaches / obstructions.** (1) Interpreting "join-irreducible elements" as join-irreducible elements of some larger lattice gave different counts but didn't obviously yield exponential counts in states reachable on $S(n)$-optimal strategies; the per-state cardinality argument above is the cleanest match to the falsifier's "polynomial upper bound on join-irreducibles for all states". (2) The winning frontier gives exponentially many *states* (nonisomorphic posets), but that’s a different object from "number of join-irreducible elements *of* poset states" under the element-count interpretation. (3) Distinction: certificate *soundness* vs *completeness* is orthogonal here - this is a state-description invariant, not a certificate size question per se.

**Limits / honest note.** The terminology is slightly ambiguous in general, but under the standard poset-theoretic reading the answer is a trivial cardinality disproof. If the question meant something else (e.g. join-irreducibles of the order-ideal lattice counted differently, or total across exponentially many states), the falsifier's per-state language points back to the element count; either way the exponential-per-state claim fails by the same kind of counting. No Lean/repo changes warranted.


## Other metadata

```json
{
  "finished_at": 1793448662.5209987,
  "started_at": 1793443894.7381973
}
```
