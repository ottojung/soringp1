# linear-extension-oracle-barrier

## status

blocked

## origin

ai_proposal_unverified

## agent_id

P6wTRKJzOI6M2lCZuddCNf-digital

## exit_state

failed

## question

For all sufficiently large n, must every uniform deterministic algorithm that achieves exact height S(n) by local minimax choices consult a linear-extension counting oracle on exponentially many distinct posets P encountered on some height-optimal play from the n-antichain?

## basis

Brightwell–Winkler note easy e(P)-counting yields optimal next comparison; counting is #P-complete; need bridge from arbitrary posets to those on height-optimal antichain plays.

## falsifier

Construct an all-n uniform algorithm computing S(n) exactly with no linear-extension counting oracle that still makes only locally minimax-optimal choices or achieves global optimality by some other means, with a correctness proof.

## implication

A positive all-n result would connect exact S(n) to #P-hard counting and rule out a natural greedy route; a negative would show optimal play need not require counting linear extensions explicitly.

## finding_unverified

ariants?

But the minimax recurrence is F(P) = 0 if total, else 1 + min_{incomparable (i,j)} max(F(P + (i<j)), F(P + (j<i))). So to compute F(P) exactly, you must explore the game tree over all possible comparisons? That is essentially the minimax search. Computing it by brute force over all posets up to isomorphism classes is what the scripts do. But is there a shortcut?

Alternatively, is F(P) computable in polynomial time without exponential search? The docs say "The exact optimum S(P) is not known to be polynomial-time computable" (research-hardness-boundaries.md line ~138-197). Also "GEN-SORT ∈ DSPACE(O(√N log² N)) ∩ EXPTIME" is mentioned. So no polynomial-time algorithm known; and it's not known to be NP-hard either. But is it equivalent to counting linear extensions?

Another fact from docs: "S(P) = f(e(P)) for some f | false (Prop 5.1)" - so you can't reduce F to just e. But can you reduce F to e-counting queries in general (Turing reduction)? That is, if you had an oracle for #LE (counting linear extensions), could you compute F(P) in polynomial time?

That would make sense if Brightwell–Winkler said counting allows determining optimal next comparison - meaning the oracle for counting gives you enough to compute the minimax strategy. Let us think: to compute F(P), do we need to know e of all posets? Or do we need to know e of the children of the optimal choice?

But to find which choice is optimal, we need to compute max(F(P+uv), F(P+vu)) for all possible pairs u,v. And F of children depends recursively on the structure. It's not obvious that knowing e values is sufficient. But combined with structure... Or maybe another way - the number of linear extensions can be used to compute the "poset entropy" etc, but not obviously giving F directly.

Alternatively, look up the actual Brightwell–Winkler result more. From some sources online in general: Brightwell and Winkler showed that counting linear extensions is #P-complete, and noted that "if one could count linear extensions efficiently, one could also find an optimal comparison for sorting by always comparing two elements that are incomparable and whose relative order would split the remaining linear extensions as evenly as possible". But is that "optimal comparison" in the worst-case (minimax) sense or average-case sense?

If it's for the average case over uniform random linear extension, then it's optimal on average. But minimax is different. That would explain - the information-theoretic/entropy strategy (balance e) is optimal on average if you know e, but not necessarily optimal in the worst case (minimax). And indeed we saw cases where balancing e gives different results than minimax choice? Wait look up our examples again.

In our conflict cases, balancing e gives the same fmax as minimax choice in some cases, different in others? For P=(20,0,0,6,0), both (0,3) and (1,4) have perfectly balanced e (diff=0). The minimax-optimal among these is (0,3) giving fmax=3, while (1,4) gives fmax=4. So balancing e perfectly doesn't guarantee minimax optimality - and among perfectly balanced choices, some are worse than others for minimax. That confirms the entropy/balance strategy is not the same as minimax.

Also for antichains, all pairs are equally balanced by e and all give same fmax - so fine. But in general, the minimax choice is not determined by e-splitting. That means you can't just use e-counting to get the minimax-optimal choice. That also fits with F not being function of e.

## Other metadata

```json
{
  "finished_at": 1793410056.3538516,
  "started_at": 1793406918.2330546
}
```
