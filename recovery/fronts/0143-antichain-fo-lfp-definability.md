# antichain-fo-lfp-definability

## status

investigated

## origin

ai_proposal_unverified

## agent_id

scqNNVw0NGxYwVK1SnZcSt-memorable

## exit_state

clearexit

## question

Is SORT-BOUND-U definable in FO(LFP) on ordered structures representing the comparison game, or does the alternating minimax quantification over all incomparable pairs at each step create a strict alternation obstruction below PSPACE?

## basis

Descriptive complexity: FO(LFP)=P on ordered finite structures; minimax games alternate existential/universal moves but the exact fixed-point complexity of this specific game needs checking against PS PACE bounds.

## falsifier

Construct an explicit FO(LFP) formula capturing the game (or show a polynomial-time evaluation reducing to it) contradicting known alternation bounds, or prove an alternation-depth/complexity obstruction that forces at least FO(PFP).

## implication

FO(LFP) definability would mean SORT-BOUND-U in P (Immerman–Vardi on ordered structures); an obstruction would rule out a direct P membership via descriptive complexity and sharpen the gap to PSPACE.

## finding_unverified

 order it's weaker. But with a built-in linear order on the structure, FO(LFP) gives all of P.

But SORT-BOUND-U is in EXPTIME as per budgeted DFS bound, and in PSPACE as per ATM bound (Claim A). The question says "FO(LFP) definability would mean SORT-BOUND-U in P" - so if we can show it's FO(LFP)-definable (over ordered structures representing the comparison game/input), that would give P membership. Conversely, if there's an obstruction preventing FO(LFP) definability, that rules out P membership via that route - but P membership might still hold by some other means? Or does it mean the descriptive complexity route to P fails?

But also note: the ATM for SORT-BOUND-U runs in polynomial time with polynomial alternations (alternations = k steps, each step is ∃ pair then ∀ answer, so 2k alternations roughly; polynomial in input length since k ≤ N). APTIME = ∪_c ATIME(n^c) = PSPACE. The alternation hierarchy in terms of number of alternations: ATIME(n^c, k(n)) where k(n) is number of alternations - if k(n) is constant, that's PH level; if k(n) is polynomial, you can get PSPACE. But FO(LFP) corresponds to polynomial time with a fixed-point (which corresponds to a certain kind of alternation/induction), while FO(PFP) gives PSPACE.

Also there is a theorem of Stockmeyer etc about alternation hierarchy, and also descriptive complexity characterizations of PH (Stockmeyer) and PSPACE.

So the question is: is the minimax alternation (∃∀ repeated k times) expressible as a single LFP fixed point, or does it create a strict alternation obstruction requiring PFP?

Also look up how the "game" is modeled. In some cases, alternating games of fixed depth are in PH, unbounded in some forms give PSPACE. But here depth is k (part of input) - polynomial in input length. Also the state graph is the poset graph.

But another way: to define "there exists a winning strategy for sorter of depth k", that's like ∃ strategy ∀ adversary moves... but strategies can be large. Or alternatively the direct game tree evaluation with alternation.

But in terms of FO formulas, you can write it as a formula with k alternations of quantifiers if k is fixed. But k is given in the input (part of SORT-BOUND-U = {1^n # 1^k : ...}) - it's part of the input. So the formula would need to be able to handle different k? Or is it a uniform formula?

Also FO(LFP) formulas are finite formulas (uniform). They can define languages over all finite structures of the appropriate signature. So for input 1^n # 1^k (unary encoding), we have a fixed formula that can say something about any n,k. The fixed point iteration runs some number of times polynomial in the size of the structure.
Let us start by exploring the full picture of the question - this is asking about FO(LFP) vs FO(PFP) for SORT-BOUND-U.

Let us think about this specific game.

Let us study more carefully and try to construct the argument.

This is a structural/descriptive-complexity analysis. The obstruction is: polynomial alternation depth (∃pair ∀answer)^k over an exponentially large implicit poset arena cannot be collapsed into a monotone FO(LFP) on polynomial ordered structures (QBF-like), while ATM alternation gives APTIME=PSPACE. So direct P membership via LFP is obstructed; likely needs FO(PFP)/PSPACE. I could not construct an explicit LFP formula in-session; the winning frontier (2^(Ω(n log^2 n)) states) and arena-size issues support the obstruction. Formal proof would need precise structure modeling. No repo changes made.

## Other metadata

```json
{
  "finished_at": 1793537365.4726648,
  "started_at": 1793534207.7053273
}
```
