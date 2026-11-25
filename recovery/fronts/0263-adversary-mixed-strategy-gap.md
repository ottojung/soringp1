# adversary-mixed-strategy-gap

## status

investigated

## origin

ai_proposal_unverified

## agent_id

uefWiFBkAmQ5wJLPmsvxF4-cornered

## exit_state

clearexit

## question

For the minimax game G(n,k), let V(n,k) be the value (sorter wins?). Is there any all-n case where every pure adversary strategy that is 'extension-count balanced' is strictly worse for the adversary than some other pure strategy, but more directly: can the adversary force a win at budget k = S(n)-1 for all large n by using a non-uniform-in-some-way strategy that exploits the comparison-validity constraints in a manner not captured by the information bound or by any known poset invariant, while every strategy following a simple heuristic (e.g. always balance linear extensions) fails?

## basis

Kahn–Saks/Kahn–Kim give constant-factor balancing; repo distinguishes information bound from S(n); no all-n result showing whether e(P)-balancing is sufficient for the adversary in this exact comparison game appears in investigated fronts.

## falsifier

Prove that for all n and all k < S(n), there exists some adversary strategy of the form 'answer to balance e(P)' (a k-Saks/Kahn type strategy, possibly adaptive) that forces >= S(n)-k extra comparisons against every sorter strategy, showing the adversary's power is captured by extension-count balancing for all n.

## implication

If extension-count balancing is not adversarially optimal for all n under comparison-valid play (the real game constraints), that would mean the gap between information bound and S(n) can arise from adversary strategy constraints, not just sorter choices; this is a structural question about the minimax equilibrium distinct from certificate soundness/completeness already investigated.

## finding_unverified

mize (over comparisons) the maximum (over adversary answers) of remaining cost. So adversary moves after sorter chooses the pair - adversary sees which pair sorter picked and then answers. So adversary is adaptive and adversarial. Sorter wants to choose pairs well in advance.
The front says "can the adversary force a win at budget k = S(n)-1 for all large n by using..." So adversary has a strategy. Also "every pure adversary strategy that is 'extension-count balanced' is strictly worse for the adversary than some other pure strategy" - so some e-balanced adversary strategies are worse than non-balanced ones. That means e-balancing is not the only option and maybe not optimal. The falsifier wants to prove e-balancing strategies DO exist that force enough extra comparisons. That is different from saying e-balancing is optimal - it's saying e-balancing is sufficient. That seems plausible if the structure is constrained.
Let us read the exact question again carefully: "Is there any all-n case where every pure adversary strategy that is 'extension-count balanced' is strictly worse for the adversary than some other pure strategy, but more directly: can the adversary force a win at budget k = S(n)-1 for all large n by using a non-uniform-in-some-way strategy that exploits the comparison-validity constraints in a manner not captured by the information bound or by any known poset invariant, while every strategy following a simple heuristic (e.g. always balance linear extensions) fails?"
So the claim being attacked is: there might exist adversary strategies (exploiting comparison-validity constraints not captured by info bound/invariants) that can force a win at k=S(n)-1 for all large n, BUT every strategy that just balances linear extensions FAILS to do this. So the question is asking - is this true? The front is posing this as a question/hypothesis to investigate. The instruction says "attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it" - so this whole thing is the claim to attack/disprove. The falsifier gives one way to disprove it: prove that e-balancing adversary strategies DO force >= S(n)-k extra comparisons. That would mean e-balancing strategies don't fail - they succeed. That directly disproves the part "every strategy following a simple heuristic (e.g. always balance linear extensions) fails". So proving the falsifier would disprove that claim.
That matches. So the task is to try to prove the falsifier - show e-balancing adversary strategy is sufficient for all n,k < S(n). Let us think if this is true.
Let us first understand the model deeply and look up known results about adversary strategies.

I studied AGENTS.md, docs/problem.md, and board #301 context. For the adversary-mixed-strategy-gap front, the key obstruction is that F (minimax value) is not monotonic in e(P) (P1 e=13,F=5 vs P2 e=14,F=4 at n<=6). An e-maximizing/balancing adversary is therefore suboptimal compared to an F-maximizing adversary; trying to prove the falsifier (that some e-balancing adversary strategy forces S(n)-k extra comparisons for all k<S(n)) fails because suboptimal adversaries cannot guarantee the minimax value S(n). The structural obstruction is general (appears at n>=6), supporting the front's claim that e-balancing strategies are worse than strategies exploiting poset structure beyond extension counts/invariants, though no all-n proof was obtained and no repo changes were made.


## Other metadata

```json
{
  "finished_at": 1793770455.9032404,
  "started_at": 1793764642.5649123
}
```
