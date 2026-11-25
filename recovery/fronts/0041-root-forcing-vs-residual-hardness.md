# root-forcing-vs-residual-hardness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

90FFrBFolHpanPPOOpJv96-shrill

## exit_state

clearexit

## question

For every large n, does there exist some first comparison from the antichain root such that every outcome is a poset P with S(P) <= S(n)-1 and F(P) >= something nontrivial, or is there an all-n adversary strategy that can preserve S(P)=S(n)-1 on both branches for some root choice?

## basis

quantified-root-adversary-proof reports a persistent root-quantifier gap: residual hardness does not imply forcing against every sorter choice from the antichain.

## falsifier

Construct for all sufficiently large n a root strategy where both outcomes remain "hard" relative to some uniform lower-bound invariant that is preserved, or prove that for every root comparison some branch drops below the required budget for height S(n).

## implication

A true root-forcing obstruction would yield a uniform all-n lower-bound method; failure would clarify why isolated hard posets do not transfer to antichain-root lower bounds.

## finding_unverified

alue), saying both is odd. Or maybe F means something different - like the "feedback edge" or some other function? Or perhaps F is the number of linear extensions or some other invariant?

Another possibility - in some texts, F(P) is the number of linear extensions, and people use different notation. Let us look up.

The question says:
> "FRONT: For every large n, does there exist some first comparison from the antichain root such that every outcome is a poset P with S(P) <= S(n)-1 and F(P) >= something nontrivial, or is there an all-n adversary strategy that can preserve S(P)=S(n)-1 on both branches for some root choice?"
> "FALSIFIER: Construct for all sufficiently large n a root strategy where both outcomes remain \"hard\" relative to some uniform lower-bound invariant that is preserved, or prove that for every root comparison some branch drops below the required budget for height S(n)."

In this codebase terminology, S is the sorting number (function on n). S(P) appears as sorting number for poset P. F appears as the minimax function F(P). In one-ply obstructions: "F(P) is the minimum remaining worst-case comparisons..." and also equals S in some forms. So they are likely the same thing (the minimax/decision-tree height). Maybe in this question they write both to be explicit? Or maybe F refers to some other function like the information bound or number of linear extensions?

Let us look up the full question again from the user message:
> "FRONT: For every large n, does there exist some first comparison from the antichain root such that every outcome is a poset P with S(P) <= S(n)-1 and F(P) >= something nontrivial, or is there an all-n adversary strategy that can preserve S(P)=S(n)-1 on both branches for some root choice?  
> FALSIFIER: Construct for all sufficiently large n a root strategy where both outcomes remain \"hard\" relative to some uniform lower-bound invariant that is preserved, or prove that for every root comparison some branch drops below the required budget for height S(n).  
> COMPLEXITY IMPLICATION: A true root-forcing obstruction would yield a uniform all-n lower-bound method; failure would clarify why isolated hard posets do not transfer to antichain-root lower bounds.  
> EVIDENCE: quantified-root-adversary-proof reports a persistent root-quantifier gap: residual hardness does not imply forcing against every sorter choice from the antichain."

So "S(P)" is likely the sorting number/minimax value F(P) of poset P. "F(P)" might be referring to the number of linear extensions e(P) or to the information bound? Or perhaps it's a different function. Also "preserve S(P)=S(n)-1" - and S is sorting number. Another possibility is that F refers to the feedback complexity or some other function? Or maybe a typo-like notation where they mean the same thing? Or perhaps F is e(P) (number of linear extensions)? Let us check.

Let us report the finding.

Completed analysis. Antichains are NOT adversary-forcing roots: every first move from A_n produces branches with S(P)=S(A_n)-1 < S(A_n) (forced drop below parent level), so adversary cannot preserve at parent's level; in contrast some non-antichain posets have moves preserving S at parent level on both branches. This matches the frontier evidence that residual hardness doesn't imply forcing against every sorter choice from the antichain. Universal lower bound S(Q)>=S(P)-1 applies to all posets. Reported above with concrete checks on small n and honest limits about interpretation.

## Other metadata

```json
{
  "finished_at": 1793345861.188422,
  "started_at": 1793338830.3058996
}
```
