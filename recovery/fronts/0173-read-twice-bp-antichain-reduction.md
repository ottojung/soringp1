# read-twice-bp-antichain-reduction

## status

blocked

## origin

ai_proposal_unverified

## agent_id

sGQhNTNeM6SIwA1gsP5deI-enable

## exit_state

failed

## question

Is there an encoding-preserving reduction from unary SORT-BOUND-U to the satisfiability/acceptance of some read-twice branching program family induced strictly by the antichain-root comparison game (not arbitrary partial orders), and if so does that force exponential read-twice BP size for all large n at exact thresholds?

## basis

Board #301 + model fidelity (distinguish general-poset hardness from antichain root) + prior read-once BP investigations; focus on transfer conditions not just model definitions.

## falsifier

Show the antichain comparison constraints make read-twice BP representations polynomial-size for all n via a structure-preserving construction, or prove no reduction preserving root-adversary alternation exists while general-poset results do not transfer.

## implication

A root-preserving reduction would connect exact unary sorting complexity to BP lower bounds without crossing into unconditional P!=PSPACE; distinguishing from read-once (already investigated) tests a strictly stronger but still structured model.

## finding_unverified

g program, is there some input it accepts? That is NP-complete in general for unrestricted BPs? Or for certain forms. Also for read-restricted BPs there are results.

Also let us look up how others interpret this. Another possibility is that you can encode SORT-BOUND-U as: is there a read-twice BP (representing a strategy) that accepts/wins for all inputs? That is, is there a BP of small size implementing a correct sorting strategy of depth k? That would relate to BP size lower bounds for sorting functions.

Also let us think about known results on BP complexity of sorting. It is known that any branching program (oblivious or not) that sorts $n$ elements must have size at least $\Omega(n \log^2 n / \log \log n)$ or similar bounds in some models? Or more directly, for the "sorting network" vs "branching program" distinction - branching programs can do better by being adaptive. But there are still lower bounds.

Also a result by Borodin et al. and others. Or more directly, the fact that sorting requires large branching programs. Also there’s a concept of "Yao’s minimax principle" and connections.

Alternatively, another angle: the comparison model decision tree is a special case of branching program (where nodes test comparisons). The size can be different if you allow sharing. But in standard comparison trees you don't share subtrees in the same way? Or you can have DAGs. Also "branching program" is often used to mean a DAG of nodes with tests.

Alternatively, in some texts, a "branching program" is a directed acyclic graph where each non-sink node is labeled by a variable and has two outgoing edges labeled 0,1, sinks labeled 0 or 1 - this is similar to decision diagrams. For read-once, each variable appears once on any path.

But for comparison-based sorting, the "variables" could be thought as the $\binom{n}{2}$ possible comparisons? But with consistency constraints. Or alternatively, the input is a permutation and comparisons give the order.

Alternatively, another common model: the "input" is given as $n$ values $x_1,\ldots,x_n$ and you can do comparisons $x_i < x_j$ (queries). This is similar to the "decision tree" model. A branching program in this setting might be called a "comparison branching program" or just generalize decision trees to DAGs.

Also "read-twice" would mean that in some sense you read/query the same comparison twice? That seems odd for a strategy. Or perhaps read each input element twice? Unclear. Or maybe in the "graph" model where you have variables for pairwise order relations?

Alternatively, let us look up the exact terminology as might be used in this community. Also the fo-tc-strategy note says "A branching program that reads comparison outcomes (or the input order)" - so it reads comparison outcomes (the results of comparisons). The input order is the hidden permutation; comparison outcomes are the results. "Read-twice" would mean the BP reads the outcome of the same comparison query twice? That would be wasteful and not natural for a strategy. That doesn't fit. Or perhaps reads each element of the input twice?

Alternatively, another interpretation: "read-twice branching program" in the sense of the "2-read" model where you can read each input bit twice total. And "satisfiability/acceptance" - is there an input (assignment to comparison outcomes consistent with some total order) such that the BP accepts? That doesn't directly give SORT-BOUND-U.
Let us start by doing a thorough analysis of this question.


## Other metadata

```json
{
  "finished_at": 1793582896.2247925,
  "started_at": 1793577098.5918064
}
```
