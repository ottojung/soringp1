# forgetful-join-exponential-classes

## status

investigated

## origin

ai_proposal_unverified

## agent_id

2eUhpP0ctmNAB2SxlGf6qa-amuse

## exit_state

clearexit

## question

For forgetful framed DAG certificates of exact S(n), does there exist an all-n family of root-reachable poset histories whose pairwise joins produce Omega(2^(c n)) distinct feasible order classes at fixed depth?

## basis

Board notes forgetful > exact-reset and join is intersection; exact-reset blocked by divisibility; completeness for forgetful remains open despite prior NP-certificate fronts.

## falsifier

Prove a polynomial bound on the number of meet-classes under forgetful joins for all root-reachable states from optimal strategies, or construct such a family with exponential class growth forcing superpolynomial DAG size.

## implication

A verified exponential class growth would imply no polynomial-size forgetful framed DAG completes to all optimal strategies, separating soundness from completeness without requiring a general NP separation theorem.

## finding_unverified

 this question systematically.

Let us understand the forgetful join model better by tracing the checker logic.

Let us read the full instruction again:
> "On billy-dev ONLY, study AGENTS.md, docs/problem.md and current board #301. Study the primary literature, attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it. Distinguish general-poset results and certificate SOUNDNESS from completeness. Do not create Lean or repository changes without a genuinely substantive, independently checkable new theorem or counterexample. Report honest limits. 
> FRONT: For forgetful framed DAG certificates of exact S(n), does there exist an all-n family of root-reachable poset histories whose pairwise joins produce Omega(2^(c n)) distinct feasible order classes at fixed depth?  
> FALSIFIER: Prove a polynomial bound on the number of meet-classes under forgetful joins for all root-reachable states from optimal strategies, or construct such a family with exponential class growth forcing superpolynomial DAG size.  
> COMPLEXITY IMPLICATION: A verified exponential class growth would imply no polynomial-size forgetful framed DAG completes to all optimal strategies, separating soundness from completeness without requiring a general NP separation theorem.  
> EVIDENCE: Board notes forgetful > exact-reset and join is intersection; exact-reset blocked by divisibility; completeness for forgetful remains open despite prior NP-certificate fronts.  
> If resuming after an infrastructure failure, inspect earlier work and avoid repeating side effects or claims.   
> On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof."

So the "FRONT" is a question - we need to attack it and try to DISPROVE it. Disproving means showing the answer is no / giving evidence against its existence. The falsifier gives two ways to resolve it - one is proving polynomial bound (which would DISPROVE the existence of exponential family). The other is constructing such family (which would PROVE the front true). So we need to try seriously to DISPROVE the front - i.e. try to prove a polynomial bound on meet-classes under forgetful joins for all root-reachable states from optimal strategies.

Let us think systematically.

Let us look up the full context more and understand the question better.

Let us look up the task again carefully and understand what I'm being asked to do.

Let us think: in a forgetful framed DAG (as per the checker), when multiple paths lead to the same node, we take intersection of guaranteed relations from all incoming paths - this is a "join"/meet operation. The state is characterized by the intersection poset. The question is whether there exists an all-n family of root-reachable poset histories whose pairwise joins produce Omega(2^(c n)) distinct feasible order classes at fixed depth. If true, this would mean you need exponentially many different nodes/classes to represent them - forcing superpolynomial DAG size. That would imply no polynomial-size forgetful framed DAG completes to all optimal strategies. The falsifier says "Prove a polynomial bound on the number of meet-classes..." - proving polynomial bound would DISPROVE the front (show it's NOT the case that there exist such families forcing exponential size). So trying to DISPROVE means trying to prove polynomial bound.

Let us start by exploring this systematically.


## Other metadata

```json
{
  "finished_at": 1793329427.6810904,
  "started_at": 1793325394.318544
}
```
