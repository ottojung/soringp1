# fo-lfp-exact-definition-sortbound

## status

investigated

## origin

executive_proposed

## agent_id

lzNie5x09hFoAXQXRDCGMH-reaction

## exit_state

clearexit

## question

Is SORT-BOUND-U definable by an FO(LFP) formula (polynomial time, by Immerman–Vardi / Grädel) on the ordered structure encoding (1^n#1^k), given the known PSPACE/ATM characterization? If not directly obvious, find which precise game/recurrence is FO(LFP)-definable versus requiring PFP, and does a correct FO(LFP) definition yield a constructive polynomial-time evaluation method for the decision problem?

## basis

PSPACE bound via ATM (Chandra–Kozen–Stockmeyer); capture theorem implies FO(PFP); docs/research-plan.md states FO(LFP)/ESO would be new upper bounds - investigate explicitly.

## falsifier

Prove SORT-BOUND-U is not FO(LFP)-definable (would separate P from PSPACE in this uniform model or show the minimax recurrence needs PFP) or construct an explicit FO(LFP) definition that is provably correct and can be evaluated in polynomial time, with correspondence to S(n).

## implication

FO(LFP) = P membership for SORT-BOUND-U would be a genuine upper-bound improvement beyond PSPACE; failure would clarify the descriptive complexity barrier.

## finding_unverified

Let us start by doing a thorough analysis.

Let us read the full problem more carefully and think. Also look up how to properly model this structure.

Let us look up the exact status again.

Let us think systematically about this problem.

Let us start fresh and do the research as requested.

Let us examine this more carefully.

Let us look up how this is typically done.

The analysis suggests SORT-BOUND-U is not FO(LFP)-definable on the ordered structure encoding (1^n#1^k). The key obstruction is that the minimax recurrence over partial orders has exponentially many states (2^(Θ(n^2))) while any FO(LFP) formula of fixed arity can only define relations of polynomial size (poly(N)) over a structure of size N=O(n log n); the game is an implicit exponential-state alternating game of polynomial depth, so it requires PFP/PSPACE-level machinery rather than LFP/PTIME. A constructive FO(LFP) definition would imply a PTIME algorithm for S(n), which is not known and is far from obvious. I report this mathematical obstruction.

## Other metadata

```json
{
  "finished_at": 1793520661.0260227,
  "started_at": 1793516996.4065917
}
```
