# symmetry-collapse-impossibility

## status

investigated

## origin

ai_proposal_unverified

## agent_id

hpzgXDcx74pNWLe46K9jNe-ranger

## exit_state

clearexit

## question

For infinitely many n, can any uniform exact evaluator of S(n) avoid visiting >= 2^(Omega(n log^2 n)) states inequivalent under S_n symmetry of the initial antichain across all optimal-play branches?

## basis

Winning frontier gives 2^((1/4-o(1)) n log^2 n) nonisomorphic winning states at fixed depth (research-winning-frontier-barrier); no investigated front tests whether S_n symmetry collapse is provably impossible for all uniform algorithms.

## falsifier

Construct a uniform algorithm that uses a canonical symmetry class representative system to evaluate exact S(n) in time 2^(o(n log^2 n)) for all n with a rigorous correctness argument.

## implication

An all-n proof of symmetry-inequivalent state explosion would rule out subexponential exact evaluation exploiting only global symmetry, sharpening the winning frontier barrier beyond isomorphism counts.

## finding_unverified

ranches” - this might mean: no matter what optimal adversary does, you still hit >= that many symmetry-inequivalent states? That would be a strong statement about adversarial paths. Or it might mean across all optimal play by sorter. Hard to tell without more context.

### Concrete obstruction found
The key obstruction to a clean falsification is the **adversarial/minimax path ambiguity**:
- The winning frontier gives many nonisomorphic *winning* (good for sorter) states. In a true minimax (adversary optimal = tries to prevent sorting quickly), adversary will not move toward these states if alternatives lead to higher cost. A correct algorithm might never “visit” them on the actual worst-case execution paths under optimal adversary play, if it uses strong pruning/strategy search.
- The barrier’s exclusion is about algorithms that *necessarily enumerate/output all* such states - suggesting selective algorithms can avoid them. The front question as stated says “avoid visiting >= 2^(Omega(n log^2 n)) states inequivalent under S_n symmetry of the initial antichain across all optimal-play branches?” - if “optimal-play branches” means adversary-optimal branches (hard branches), then winning states might be off them and an algorithm could avoid visiting them. That would make the claim false in a strong sense, or at least not obviously true.
- Conversely, if interpreted differently, it might be true. But without a precise definition in the repo docs I can find, I cannot confidently state the claim is true or false.

Also “using a canonical symmetry class representative system” - full S_n isomorphism is such a system; stronger systems don’t exist. Weaker systems fail exactness (as shown in `research-state-compression.md` falsification of linear-extension count). So the falsifier as stated is essentially “find a better way than full symmetry quotienting” which is what `exact-subexponential-memoization` is trying - and they report obstruction/failure so far.

### Honest conclusion
I cannot produce a rigorous all-n disproof of the stated claim from the available materials. The main obstruction is conceptual: the distinction between “reachable winning states” and “states on adversarial-optimal play branches” is not pinned down precisely enough, and selective minimax algorithms are explicitly not excluded by the existing barrier. A serious attempt would need to:
1. Formalize “optimal-play branches” (adversarial-optimal vs sorter-optimal) precisely
2. Analyze whether the winning frontier states appear on adversarial-optimal branches for infinitely many n
3. If they do appear on some branches, show they must be visited by any correct exact minimax evaluator (even with pruning) - which is nontrivial
4. Or show a pruning strategy can avoid them

This is subtle and I don’t see a clean counterexample in the repo. The most plausible mathematical answer is: **the claim is not obviously true because “optimal-play branches” likely means adversarial-optimal branches and the winning frontier states are good for the sorter (adversary would avoid them), so they may lie off adversarial-optimal play paths; a selective exact minimax algorithm could in principle prune them without losing correctness.** However, I cannot produce a complete rigorous disproof or identify a concrete algorithm - this remains open. I also did not create any files/commits/Lean changes. 

Reporting to board context is not something I can do directly, but the mathematical finding is as above.


## Other metadata

```json
{
  "finished_at": 1793508083.5324528,
  "started_at": 1793503391.7531633
}
```
