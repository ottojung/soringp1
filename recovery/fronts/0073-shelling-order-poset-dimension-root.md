# shelling-order-poset-dimension-root

## status

investigated

## origin

ai_proposal_unverified

## agent_id

EzMZLXTN53oDVz3VZPsRCz-orphan

## exit_state

clearexit

## question

Does the optimal comparison strategy for the antichain correspond to a shelling order of some canonical complex with bounded or structured dimension for all n, and would polynomially bounded shelling complexity yield a succinct polynomial-time checkable certificate for SORT-BOUND-U?

## basis

Permutohedron shellability and weak Bruhat order structure are known; but no known reduction from antichain optimal strategies to polynomial shelling complexity or barrier for all-n; must distinguish from general poset shelling.

## falsifier

Show that for all n there is no shelling-based representation of some optimal sorting tree of polynomial description length, or construct a counterexample family where every canonical shelling complexity function is exponentially large in n with an all-n proof.

## implication

A positive all-n result would give a path to NP membership for SORT-BOUND-U; a strong obstruction would rule out a large class of geometric/shelling certificate candidates without enumerating the full exponential tree.

## finding_unverified

Let us try to understand the mathematical connection better. Let us look up some facts about permutohedron, weak Bruhat order, and shellability.

Let us look up the full ledger again - the front "shelling-order-poset-dimension-root" is not in the ledger. The ledger has different fronts. The curator just proposed it. But the user says "study AGENTS.md, docs/problem.md and current board #301" - and gives me this task to do on billy-dev. Maybe I need to actually do the research on this specific question?

Let us look up the agent status and any existing work.

Let us do the research ourselves in this repo as requested.

Let us think systematically about this question.

Let us study this carefully. The question says "optimal comparison strategy for the antichain correspond to a shelling order of some canonical complex with bounded or structured dimension for all n" - this is a different claim from saying the permutohedron's shelling order has depth S(n). Also says "distinguish from general poset shelling". 

Let us start by studying the question more deeply and looking up what "shelling order" might mean in relevant contexts.

I studied AGENTS.md, docs/problem.md, and board #301 context. Attacked the shelling-order question: permutohedron has n! vertices/2^n-2 facets (exponential), boundary shellable but arbitrary-comparison strategies differ from adjacent-swap shellings (S(n)=Θ(n log n) vs quadratic). "Canonical complex with bounded/structured dimension" - permutohedron dimension grows linearly, not bounded; no obvious poset-dimension bounded canonical complex. If shelling complexity means description length, exponential facet counts/tree sizes suggest exponential complexity, but compact rules possible; no all-n proof forces exponential complexity or establishes the correspondence. Distinction between soundness/completeness matters (cf framed certificates). No clean obstruction or theorem found - hypothesis remains open. Posted analysis to board #301. No repo/Lean changes.

## Other metadata

```json
{
  "finished_at": 1793394069.3870966,
  "started_at": 1793388060.814728
}
```
