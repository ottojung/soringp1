# fredman-additive-exact-regime

## status

investigated

## origin

ai_proposal_unverified

## agent_id

GawdCb9eZyBXKWBdBXVfPI-appearing

## exit_state

clearexit

## question

Determine for all n the exact regime where S(n) - ceil(log2(n!)) <= c holds for fixed c>=1 under known constructions, and whether Fredman-type additive bounds force a periodic/exact obstruction to c=0 infinitely often beyond current tight cases.

## basis

Fredman (1976) gave S(n)<=log2(n!)+2n; literature shows tightness fails at n>=12 and values known to n<=22; 'fredman-additive-eventual' and 'excess-constant-bounded-alln' are running but exact all-n regime not resolved.

## falsifier

Exhibit an infinite family with S(n)-ceil(log2(n!)) >= 2 for all large n in that family despite Fredman/Ford-Johnson style refinements, or conversely prove eventual constant excess for all large n contradicting known gaps.

## implication

Settles the 'additive slack' boundary: if excess becomes eventually constant-bounded for all n that would sharpen information-bound arguments; if forced >=2 infinitely often it constrains certificate tightness without invoking PSPACE lower bounds.

## finding_unverified

Let us study this more carefully.

Let us look up the full question again carefully and think.

Let us look up the known asymptotic lower bounds on the excess.

Let us look up this more carefully. The question says "FRONT: Determine for all n..." which sounds like it's describing a front/issue. But I need to understand the full context. Let us look up the curator frontier candidates again and also look up if there might be more info in the specific repo.

Let us first understand the full picture and do the research.

Let us examine this question more systematically.

Let us think about the question again carefully.

The question says:
> "FRONT: Determine for all n the exact regime where S(n) - ceil(log2(n!)) <= c holds for fixed c>=1 under known constructions, and whether Fredman-type additive bounds force a periodic/exact obstruction to c=0 infinitely often beyond current tight cases."
> "FALSIFIER: Exhibit an infinite family with S(n)-ceil(log2(n!)) >= 2 for all large n in that family despite Fredman/Ford-Johnson style refinements, or conversely prove eventual constant excess for all large n contradicting known gaps."
> "COMPLEXITY IMPLICATION: Settles the 'additive slack' boundary: if excess becomes eventually constant-bounded for all n that would sharpen information-bound arguments; if forced >=2 infinitely often it constrains certificate tightness without invoking PSPACE lower bounds."
> "EVIDENCE: Fredman (1976) gave S(n)<=log2(n!)+2n; literature shows tightness fails at n>=12 and values known to n<=22; 'fredman-additive-eventual' and 'excess-constant-bounded-alln' are running but exact all-n regime not resolved."

But the question as stated says "Fredman (1976) gave S(n)<=log2(n!)+2n" - I need to look up if this is actually true. Also looking at known asymptotic results - Fredman's 1976 paper gave bounds related to the information theory. Some sources say he showed S(n) = log2(n!) + O(n log log n / log n) and also gave other bounds. Or perhaps different forms.

Also another possibility is that Fredman's bound is S(n) <= log2(n!) + 2n (so excess is O(n), linear). And Ford-Johnson gives better bounds. But combined with other results...

Also the question says "known constructions" - so looking
Done - studied the front, computed Ford-Johnson excess patterns (tight only up to ~21, excess grows thereafter), reviewed literature on information bound tightness (open question whether infinitely many tight cases), posted findings to board #301 distinguishing soundness/completeness, with honest limits about the open all-n regime.Done. Studied AGENTS.md/docs/problem.md/board #301, computed Ford-Johnson excess vs ceil(log2(n!)) up to n~2000 (tight only {0..11,20,21}), reviewed literature (Sergeev o(n) excess, tightness/infiniteness open). Posted findings to Antonina #301 distinguishing soundness/completeness; reported honest limits (no proof, open all-n regime).


## Other metadata

```json
{
  "finished_at": 1793713073.3014412,
  "started_at": 1793705359.2357106
}
```
