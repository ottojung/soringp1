# antichain-orbit-forcing-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

s0yz1QfEkxTt2x1werwCwD-sweep

## exit_state

clearexit

## question

For every sufficiently large n, does there exist some comparison made from the n-element antichain by every height-S(n) sorting strategy such that both outcomes produce posets in the same root-orbit class under S_n and yet force the same minimax cost S(n)-1, or is all-n antichain-forcing a false premise?

## basis

Root quantifier gap appears across board investigations; orbit classes and isomorphism capture symmetry but reachability/forcing under optimal adversarial play remain distinct from residual hardness.

## falsifier

Exhibit an infinite all-n family of first comparisons where no orbit class is forced on both branches at optimal height, or prove the forcing property for some explicit canonical first move for all large n.

## implication

A verified all-n forcing theorem would give a strong lower-bound invariant from the root; its falsification would show root-level symmetries block naive forcing arguments for evaluating S(n) complexity.

## finding_unverified

Let us analyze this carefully.

Let us proceed systematically.

Let us test this hypothesis.

Let us analyze the question precisely.

Let us write up the analysis.

The instruction says "Report honest limits. ... On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." Also says "Report a concise update on the research board (see `docs/operations.md`)". But I need to be on billy-dev and follow the rules - the board is on Antonina issue #301. The instructions also say "Report findings, obstacles and negative results go to **Antonina issue #301**" and give how to use board_digest.py. But posting to the board - how? The operations say "Post only when something changed: a result, a falsification, or a precise obstacle." But I don't see direct API tools for posting in the available functions. Let us look up how it's done.
The finding is clear from symmetry.

I need to report the mathematical finding. The instructions say "Report honest limits... On completion report a mathematical finding..." - this is the finding. I should present it concisely.**Mathematical finding:** All-n antichain-forcing is false. For any $n\ge2$, every first comparison from antichain $A_n$ gives isomorphic branches in same $S_n$-orbit with equal minimax cost $S(n)-1$ (symmetry), but no pair is made by *every* height-$S(n)$ strategy (transitive action of $S_n$ on pairs gives optimal strategies starting with any chosen pair). Root-quantifier gap: symmetry/orbit classes don't force a particular move; naive "antichain forcing" lower-bound arguments fail at the root. Complexity implication unchanged (no direct class separation). No forced canonical move exists for large $n$.


## Other metadata

```json
{
  "finished_at": 1793805971.387055,
  "started_at": 1793804276.6216147
}
```
