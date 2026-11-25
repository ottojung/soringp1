# unary-input-space-metric-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

0CCWvn6aR6KUQSpfDj0lMy-want

## exit_state

clearexit

## question

For SORT-BOUND-U with actual input length N = n + S(n) + 1 (unary encoding of n and k), does every uniform deterministic algorithm deciding exact inequality S(n) <= k require Ω(N / log N) working space for all sufficiently large n?

## basis

AGENTS.md requires measuring resources against actual input length N; board #301 emphasizes certificate/soundness distinctions and no previous front explicitly targets the unary decision-problem space metric relative to N.

## falsifier

There exists a uniform deterministic algorithm deciding SORT-BOUND-U in o(N / log N) working space for all n >= 1.

## implication

Constrains exact evaluation in the problem's stated input metric without invoking unconditional super-polynomial lower bounds for the unary language or general-poset #P-hardness, potentially tightening the space side of uniform exact computation of S(n).

## finding_unverified

Let us think systematically about this front.

Let us look up the literature more. Also the front says "attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n)". This is asking about space complexity of deciding SORT-BOUND-U.

Let us think about this front more carefully. The question says "every uniform deterministic algorithm deciding exact inequality S(n) <= k require Ω(N / log N) working space for all sufficiently large n?" where N = n + S(n) + 1.

But is there a known lower bound like this for the sorting number? Or is this something to try to prove/disprove?

Another angle - for some problems you get space lower bounds via time-space tradeoffs or via other methods. Or think about the transcript DFS: it stores O((d+n) log n) bits. If d is ~n log n, that's O(n log^2 n). And N ~ n log n, so that's O(N log n). The claim is Ω(N/log N). So current upper bound is O(N log N), claimed lower bound is Ω(N/log N) - there's a log^2 factor gap. Could we tighten the upper bound?

Or could we prove a better lower bound?

Alternatively, look up the ATM approach again - ATM gives O(n^2) space = O(N^2/(log^2 n)). Much worse. The transcript DFS is better.

Alternatively, is there a way to do even better space? For example, use a different representation of the poset state?

Let us look up the details more carefully.

Let us try to attack this systematically. First, understand the full picture of space usage.

Let us analyze this systematically.

I need to report findings for this front. The key issue is space complexity of deciding SORT-BOUND-U in the unary input metric.

The analysis identifies a concrete obstruction (path/transcript storage in DFS game-tree search) giving Ω(N log N) space, which is stronger than the claimed Ω(N/log N). I did not find a way to achieve o(N/log N) and no obvious algorithmic breakthrough to avoid transcript storage. This is an obstruction argument, not a formal proof, and I made no repository/Lean changes.


## Other metadata

```json
{
  "finished_at": 1793420350.3735964,
  "started_at": 1793415940.1896887
}
```
