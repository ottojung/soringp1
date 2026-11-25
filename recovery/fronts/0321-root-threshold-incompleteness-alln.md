# root-threshold-incompleteness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

IlnXKZVBiitp6lwf71ceqH-breathed

## exit_state

clearexit

## question

For every n >= 4, is the universal tightness threshold T(S(n)) strictly below n!, so that some finite poset with at most n! linear extensions needs more than S(n) adaptive comparisons, or can the failures at n=4 and along the ordinal-sum subsequence be repaired for all remaining n?

## basis

Board #301 T(4)=12 and T(5)=20, the 7-element e=21, minimax-6 witness reproduced by the exact evaluator, S(4)=5, and elementary ordinal-sum accounting (e and minimax additive/multiplicative) indicating failures for a constructed infinite n-subsequence.

## falsifier

Exhibit an explicit n >= 4 together with a proof or exhaustive check that every poset with e(P) <= n! is sortable in S(n) comparisons, i.e. that T(S(n)) >= n!.

## implication

If the strict inequality holds for all n >= 4, then every sound certificate that prunes states solely by comparing e(P) with the universal extension threshold is root-incomplete, excluding that route to a polynomial NP or coNP certificate for SORT-BOUND-U; one n with T(S(n)) >= n! would reopen it at that scale.

## finding_unverified

The assigned question is whether, for **every \(n\ge4\)**, the universal tightness threshold \(T(S(n))\) is strictly less than \(n!\), or whether some \(n\) has \(T(S(n))\ge n!\). Here \(T(r)\) is the largest extension count up to which *every finite poset* is sortable in at most \(r\) adaptive comparisons.

This is genuinely distinct from the active \(T(4)=12\) balanced-split lemma: that lemma concerns the specific local claim that every poset with at most 12 extensions has a comparison splitting it into two sides of at most 7. The assigned question asks for an all-\(n\) comparison between \(T(S(n))\) and \(n!\).

Concrete evidence so far: the board reports \(T(4)=12\) and \(T(5)=20\), while \(S(4)=5\) and the 7-element, 21-extension witness has minimax cost 6. Thus the proposed strict inequality holds at \(n=4\) and \(n=5\), conditional on the board’s threshold results. Ordinal-sum additivity also gives failures for a constructed infinite subsequence, as noted in the assignment.

I have not established a new all-\(n\) argument or a counterexample. In particular, I have not verified the claimed subsequence construction in a way that resolves the remaining \(n\). The next falsifiable step would be to derive explicit bounds for the ordinal-sum construction and compare them with \(n!\) for all its parameters; that still would not settle the other \(n\) without a separate argument. No repository changes or board post were made.

## Other metadata

```json
{
  "finished_at": 1794076142.1719563,
  "started_at": 1794075142.149658
}
```
