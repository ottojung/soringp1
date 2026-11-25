# delta-n-uniform-computability

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QobyXd45piDuBpqHhoyHQn-worrying

## exit_state

clearexit

## question

Is the information-excess function delta(n)=S(n)-⌈log2(n!)⌉ uniformly computable in time polynomial in the binary length of n, given only the known asymptotics S(n)=log2(n!)+o(n) from Sergeev?

## basis

Sergeev gives o(n) slack but no uniform algorithm for delta(n); S(n) complexity is the open target in problem.md and AGENTS.md.

## falsifier

Prove that computing delta(n) for all n is at least as hard as computing S(n) under a uniform encoding-preserving reduction, or exhibit a polynomial-time algorithm for delta(n) from n alone without computing S(n) exactly.

## implication

A polynomial-time uniform algorithm for delta(n) would yield a new route to approximating or characterizing S(n); hardness would show the slack itself is nontrivial to determine.

## finding_unverified

ut computing S. But the OR means if we can prove first part, we "disprove" in the sense of satisfying falsifier? Wait look up the exact instruction again.

> "FRONT: Is the information-excess function delta(n)=S(n)-⌈log2(n!)⌉ uniformly computable in time polynomial in the binary length of n, given only the known asymptotics S(n)=log2(n!)+o(n) from Sergeev?  
> FALSIFIER: Prove that computing delta(n) for all n is at least as hard as computing S(n) under a uniform encoding-preserving reduction, or exhibit a polynomial-time algorithm for delta(n) from n alone without computing S(n) exactly.  
> COMPLEXITY IMPLICATION: A polynomial-time uniform algorithm for delta(n) would yield a new route to approximating or characterizing S(n); hardness would show the slack itself is nontrivial to determine."

The task says "attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it." So the front is a claim? "Is the information-excess function delta(n)... uniformly computable..." - posed as a question but framed as front; maybe the implicit claim is "yes" or the question is to be answered. The falsifier gives conditions - if we can do either thing, that falsifies/disproves something? Or satisfies the falsifier condition.

We need to "attack a precise all-n falsifiable mathematical claim... and try seriously to DISPROVE it". So find which claim is being made and disprove it. The front states the question as if claiming computability? Or maybe the claim is that delta is poly-time computable given only asymptotics. The falsifier says "prove computing delta is >= hard as S OR exhibit poly-time algorithm for delta without computing S" - these are the two ways to resolve; doing the first disproves the possibility of the second? Or both are possible routes.

But the instruction says "try seriously to DISPROVE it" - so disprove the front claim. The front asks if delta is uniformly computable in poly-time in binary length given only asymptotics. So the claim is effectively "yes, delta is poly-time computable given only those asymptotics". Disprove it.

How? Show that you cannot compute delta without computing S (equivalence) so it's as hard as S; also asymptotics don't give algorithm. That would disprove computability from asymptotics alone. That matches falsifier first option - prove delta >=_P S. That disproves the claim that delta is easier/computable via asymptotics alone.

Also need to be precise: "given only the known asymptotics S(n)=log2(n!)+o(n) from Sergeev" - the asymptotic is a theorem about growth; you can't extract exact integer values from asymptotic notation alone. So computability is impossible from asymptotics alone. That’s a clear disproof.Let us write the mathematical analysis.

**Mathematical finding (disproof):** delta(n)=S(n)-⌈log2(n!)⌉ ≡_P S(n) in the binary input model. L(n)=⌈log2(n!)⌉ ∈ FP_m, so S <=_P delta (add L) and delta <=_P S (subtract L). Computing exact delta yields exact S and vice versa. Sergeev’s S(n)=log2(n!)+o(n) is an asymptotic growth bound, not an algorithm or a finite exact characterization — it underdetermines exact delta and gives no shortcut independent of S. The front claim (“poly-time computable given only those asymptotics”) is false; slack is nontrivial because determining it is complexity-equivalent to determining S(n). (Distinguish function computation from certificate soundness/completeness; poset hardness doesn’t transfer without reduction.)


## Other metadata

```json
{
  "finished_at": 1793636551.9092739,
  "started_at": 1793635987.8581252
}
```
