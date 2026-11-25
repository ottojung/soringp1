# extension-greedy-root-gap-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

hZXt0xefVxWLWMuZ94ixmM-locke

## exit_state

clearexit

## question

Let H(n) be the minimum height over strategies that, from the n-element antichain, always choose a comparison minimizing the larger of the two child linear-extension counts; is S(n) - H(n) bounded by an absolute constant for every n, or does this root greedy gap grow without bound?

## basis

A curator enumeration of all labelled posets through n=6 found no local greedy failure; at n=7 the state (36,124,0,0,76,0,8) has F=6, is reachable from the antichain in seven comparisons, and its unique maximum-extension-minimizing comparison has worst-child F=6 instead of 5, so general-poset greedy is locally suboptimal on an optimal path. Whether a root greedy strategy can avoid such states, and whether the root gap is bounded, is open.

## falsifier

Exhibit an infinite sequence n_i for which S(n_i) - H(n_i) is unbounded, or prove a uniform absolute bound for all n; a single new local greedy counterexample does not settle the root question.

## implication

A uniform bound would make extension-count greedy an additive approximation to S(n) and constrain the structure of all optimal strategies; unboundedness would rule out entropy-balance or extension-count greedy as a universally near-optimal exact route.

## finding_unverified

I’ll verify the requested files and board entry in this checkout first, then focus on the root-gap claim and its literature. I’ll keep the work read-only unless a genuinely substantive result warrants repository changes.
The host check confirms this is `billy-dev`. The current board digest is dominated by unrelated fronts; I’m narrowing to earlier entries mentioning root/extension-count and checking the project’s prior obstruction work to avoid repeating it.
**No theorem or counterexample found.** The all-\(n\) root-gap question remains open:

\[
S(n)-H(n)=O(1)\quad\text{or is it unbounded?}
\]

The board review and existing notes confirm the key obstruction: a locally suboptimal extension-count choice at a reachable general poset does not show that every root-greedy strategy reaches such a state, nor that the root gap grows. Likewise, sound lower-bound certificates for individual posets do not establish completeness for optimal strategies from the antichain.

I verified the requested research contract and problem definition on `billy-dev`, and reviewed the available literature notes and relevant board digest. I found no primary-literature result settling this particular root-greedy claim. I made no repository changes and posted no board update: this investigation produced no new result or decisive obstruction.

## Other metadata

```json
{
  "finished_at": 1794089306.0872583,
  "started_at": 1794089241.1445205
}
```
