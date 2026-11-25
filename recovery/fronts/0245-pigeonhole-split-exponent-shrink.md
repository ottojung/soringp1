# pigeonhole-split-exponent-shrink

## status

investigated

## origin

executive_commissioned

## agent_id

E4vae8ULxJJWy0kxzOy6wQ-indiana

## exit_state

clearexit

## question

Find a non-enumerative recurrence for the minimax value F(P) exploiting structure (symmetry/decomposition/orbits) giving 2^(O(n log n)) or better uniform time bound avoiding full winning-frontier enumeration.

## basis

Winning-frontier barrier rules out enumerating transcripts/states but doesn't rule out compressed representations.

## falsifier

Show that for hard posets any exact recurrence avoiding transcript enumeration is subject to the same 2^(Omega(n log^2 n)/something) barrier as full enumeration.

## implication

Better time bound is a concrete algorithmic improvement toward understanding exact complexity; relevant to upper bounds.

## finding_unverified

n’t obviously avoid enumerating states. This is a barrier to formula-based compression, not a direct proof that state count is same - but it rules out a large class of “non-enumerative” recurrences.

5) **Certificate soundness vs completeness**  
   - Sound compressed class: can merge only if F identical and move-graph equivalent for all adversarial responses - hard to certify without knowing F. 
   - Complete for all-n: must cover every labelled reachable poset that can arise; hard-poset families will fall outside any efficiently recognizable decomposition class. 
   A method might be sound on structured posets but incomplete as an “all-n non-enumerative recurrence”, or might be complete only by degenerating to enumeration. The falsifier targets exactness + all-n + avoiding transcript enumeration.

### Concrete failed approach / obstruction
Tried to construct orbit+decomposition recurrence: assumes can classify P by (shape_orbit, decomposition_tree) with small class key. Counterexample family: take P to be a “random” labelled poset of “balanced” comparison structure with trivial Aut(P) and no nontrivial series/parallel decomposition; adversary can force a first move into states Q1,Q2 with same property. The equivalence classes F^{-1}(v) for relevant v will contain exponentially many such labelled states with pairwise different move profiles under all label-preserving maps - no nontrivial merges possible by symmetry/decomposition; to determine F(P) you cannot avoid evaluating both branches and you cannot shortcut by a formula. Counting: number of such indecomposable labelled states within depth S(n) is 2^(Ω(n log^2 n)) and they form an “incomparable” family under any efficiently computable compression that preserves exact minimax (otherwise would create a smaller AND-OR instance not equivalent). This matches DFS frontier size up to polynomial factors. Using e(P) directly gives #P-hard per node (worse). So obstruction is: **exact all-n non-enumerative (by symmetry/decomposition/orbits) recurrence is blocked by (a) labelledness + trivial automorphisms forcing class size >=1 per state, (b) indecomposability of hard posets, (c) AND-OR non-distributivity, forcing exploration of a frontier of size exponential in n log^2 n with no known exact compression invariant cheaper than the value itself**. This does not prove a formal lower bound, but is a concrete obstruction to the proposed exponent 2^(O(n log n)).

### Honest limits
- No formal proof of 2^(Ω(n log^2 n)) lower bound for *all* non-enumerative methods; “non-enumerative” is not a formal complexity class. 
- Could exist some other algebraic/compressed representation (not obvious from poset structure) - not ruled out, just not evident and would need to dodge (a)-(c). 
- General poset #P-hardness is suggestive but not directly equivalent to this game complexity. 
- Distinction: barrier to *this* family of methods (symmetry/decomposition/orbits) is strong; barrier to *all* methods weaker. The falsifier as stated is plausible for that family.

### Outcome
No repo/Lean changes. Finding: the front as stated is likely false for hard posets due to labelled states with trivial automorphism groups and indecomposable structure forcing frontier enumeration; exact compression is obstructed by AND-OR non-distributivity and lack of cheap exact invariants (#P-like), giving same exponent class as transcript enumeration. Concrete failed approach = orbit+decomposition recurrence. No proof, only obstruction.

## Other metadata

```json
{
  "finished_at": 1793724173.3495424,
  "started_at": 1793723953.1831005
}
```
