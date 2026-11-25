# fo-lfp-descriptive-complexity

## status

investigated

## origin

executive_manual

## agent_id

kTDICDBxLXEHorRMC1WRd6-artistic

## exit_state

clearexit

## question

Can SORT-BOUND-U be defined by a fixed-point logic formula (FO(LFP) or FO(PFP)) on ordered structures that is faithful to the unary encoding and yields a tight complexity correspondence? Does such a definition imply membership in P or only in PSPACE?

## basis

research-plan.md lists descriptive complexity as open: FO(PFP) definition separate from FO(LFP)/ESO (NP) definitions.

## falsifier

Show that no FO(LFP) (or FO(PFP)) definition of the exact S(n)-threshold is faithful under the required encoding, or prove the correspondence fails.

## implication

An FO(LFP) characterization would give an alternative route to complexity class membership (P) and clarify the descriptive complexity of the sorting number.

## finding_unverified

for ordered structures ESO gives NP. For P, Immerman–Vardi says FO(LFP) captures P on ordered structures of *arbitrary* finite size. The input is encoded as an ordered structure - the domain elements are used to represent positions in the input. So for an input of length N, you have a domain of N elements (or you can add order). So the domain size equals the input length. That means if you need to simulate a PSPACE computation on input of length N, the TM uses polynomial space in N - but the *domain* of the structure you're working on is just N elements. That can't be - unless you use tuples. Yes! Because you can form k-tuples from N elements, giving N^k tuples. Relations can be over tuples, so you get higher arity relations over N elements giving the effect of a larger domain. That’s how it works - the domain size is the input length N, but you have relations of arbitrary arity so you can simulate structures of larger "virtual" size.
Let us think more carefully about this specific question. The user says "On billy-dev ONLY..." and gives specific instructions. I need to follow them exactly as written.

Let us look up the exact question again more carefully. The user says:
> "FRONT: Can SORT-BOUND-U be defined by a fixed-point logic formula (FO(LFP) or FO(PFP)) on ordered structures that is faithful to the unary encoding and yields a tight complexity correspondence? Does such a definition imply membership in P or only in PSPACE?"
> "FALSIFIER: Show that no FO(LFP) (or FO(PFP)) definition of the exact S(n)-threshold is faithful under the required encoding, or prove the correspondence fails."

Also says "Distinguish general-poset results and certificate SOUNDNESS from completeness."

A plausible answer is that the tight correspondence fails because of the tension between soundness and completeness when modeling the poset game faithfully on the unary encoding. Or another angle - to be faithful to the exact minimax over all posets (the combinatorial object S(n)), the fixed-point would need to reason about exponentially many poset states, but the ordered structure from unary encoding has size N = n+k+1 and the fixed-point relations can only have polynomially many tuples total; you cannot represent all poset states faithfully, leading to either incompleteness (missing some winning strategies) or unsoundness. The ATM avoids this by alternation without requiring to list all poset states simultaneously in that form. This breaks faithfulness. Also distinguishes from general poset results - for arbitrary posets the state space is even worse. This would mean no such faithful definition exists with tight correspondence.

The strongest clean obstruction is the soundness/completeness/faithfulness tension between the exact poset-minimax (with exponential state space, needing memoization over all reachable posets) and fixed-point logic over domain size N with polynomial tuple relations. While PFP is the natural class correspondence for PSPACE membership, a definition faithful to the exact minimax on the unary encoding is not obviously tight; in particular, any attempt to be faithful to all poset states risks breaking tight complexity correspondence or completeness. FO(LFP) would imply P but faces even steeper obstacles to faithful exact minimax capture. This is an obstruction argument, not a formal disproof - concrete formalization would need to make the representation bound precise. No repository changes suggested without a substantive checkable result.

## Other metadata

```json
{
  "finished_at": 1793338309.9303951,
  "started_at": 1793334138.9299428
}
```
