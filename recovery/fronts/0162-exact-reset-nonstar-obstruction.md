# exact-reset-nonstar-obstruction

## status

investigated

## origin

executive_manual

## agent_id

UlxxYfX4cwcjAqRJ8w9OIr-feeble

## exit_state

clearexit

## question

Beyond the odd antichain-star case where e(A_n)/e(V_n)=n is odd (proven impossible), are there other boundary families with integer extension ratios realizable as ratio counts but not as isomorphic-branch comparison resets? Characterize the full obstruction class.

## basis

Exact-reset realizability front proved odd star impossible; need broader characterization.

## falsifier

Find a non-star boundary family with integer ratio >=2 realizable by some comparison module with isomorphic branches, or give a complete arithmetic+graph-theoretic characterization of realizable resets.

## implication

Critical for understanding whether certificate arithmetic is sufficient or branch-isomorphism is a hard constraint.

## finding_unverified

I'll start by reading the board, frontier files, and related docs.
Let us look up the front in the frontier files more, and also look at the actual note again carefully. Also look at research notes for context on how this fits.

Now let us look at the front as stated in the user message again. The user says "FRONT: Beyond the odd antichain-star case where e(A_n)/e(V_n)=n is odd (proven impossible), are there other boundary families with integer extension ratios realizable as ratio counts but not as isomorphic-branch comparison resets? Characterize the full obstruction class. FALSIFIER: Find a non-star boundary family with integer ratio >=2 realizable by some comparison module with isomorphic branches, or give a complete arithmetic+graph-theoretic characterization of realizable resets."

This is the front we need to attack. The task is on billy-dev ONLY, study AGENTS.md, docs/problem.md and current board #301. Study the primary literature, attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it. Distinguish general-poset results and certificate SOUNDNESS from completeness. Do not create Lean or repository changes without a genuinely substantive, independently checkable new theorem or counterexample. Report honest limits.

We need to seriously try to disprove/find counterexample to the falsifier: find non-star boundary family with integer ratio >=2 realizable by some comparison module with isomorphic branches, or give complete characterization.

Also "beyond the odd antichain-star case where e(A_n)/e(V_n)=n is odd (proven impossible), are there other boundary families..." - the note shows only odd n impossible for antichain->star. For even n, ratio integer but is it realizable? Or is there another obstruction?

And we need to look at how exact reset is defined more precisely. Let us look up the full definition again - from the note: "An exact reset stage from F to F' is a comparison tree rooted at F such that every reachable leaf has, after its allowed slot framing, certificate extension set exactly Ext(F'). A frame is a bijective relabelling..." Also says "comparison module with isomorphic branches" in the falsifier - that means the tree must have isomorphic branches under some framing?

Looking up how it's used - also look at git blame/history more, and any other files related to "exact reset" or "branch isomorphism"/"framing". Also search for "isomorphic branches" or "slot framing" patterns.
Let us analyze the exact reset condition carefully.

Let us understand the exact reset model precisely.


## Other metadata

```json
{
  "finished_at": 1793560969.9562328,
  "started_at": 1793559716.9502444
}
```
