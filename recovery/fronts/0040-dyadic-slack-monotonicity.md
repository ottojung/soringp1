# dyadic-slack-monotonicity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

fcx0GSu8VAf75mSd9HZn69-rounded

## exit_state

clearexit

## question

Is the excess function D(n)=S(n)-ceil(log2 n!) eventually monotonic on each dyadic interval [2^p, 2^(p+1)) for all large p, or does it exhibit all-n oscillation across intervals beyond known small drops?

## basis

docs/research-state-compression.md and board note dyadic-excess-sequence-structure show Delta drops n=19->20 but is bounded by 1 on checked intervals; all-n behavior remains open.

## falsifier

Find an infinite family of dyadic intervals with D(n) not monotonic on them, or prove eventual monotonicity on every dyadic interval for all sufficiently large p.

## implication

Monotonicity would suggest a regular structure exploitable by uniform recurrences; persistent oscillation would complicate extrapolation and point to global constraints beyond simple interval bounds.

## finding_unverified

t is bounded by 1 on checked intervals; all-n behavior remains open."

Also the board note mentioned "dyadic-excess-sequence-structure" - but grep didn't find it. Maybe it exists somewhere else?

Alternatively, think about the structure of D(n)=S(n)-⌈log₂ n!⌉. We have d(n)=S(n)-S(n-1) is the increase in sorting comparisons when going to n elements. Also there's the Ford-Johnson algorithm, merge-insertion sort. Also it's known that d(n) is roughly log₂ n. And m(n)=I(n)-I(n-1) is related to ⌈log₂ n⌉ (it equals ⌈log₂ n⌉ most of the time, sometimes less when there's a ceiling effect).

Also D drops when m(n) > d(n). For large n, by the information-theoretic lower bound and asymptotics, how do d(n) and m(n) behave?

From Sergeev's asymptotics, S(n)=log₂(n!)+O(n/(log n)^(1/5)), so d(n)=S(n)-S(n-1)=log₂ n + o(1) in some averaged sense? Or more precisely, S(n)-S(n-1) can vary. Also it's known that S(n) - S(n-1) is either ⌊log₂ n⌋ or ⌈log₂ n⌉ in some cases? Or more tightly constrained?

Also another fact - the "graph of the sorting function" has steps related to binary/ternary splits. Also it's known that |d(n) - log₂ n| can be small.

But more directly, m(n)=⌈log₂ n!⌉ - ⌈log₂ (n-1)!⌉ is either ⌊log₂ n⌋ or ⌈log₂ n⌉ depending on whether {log₂ n!} (frac part) is small enough that adding log₂ n doesn't cross integer boundary in the ceiling? For example, if log₂((n-1)!) is already very close to integer from below, adding log₂ n might make the ceiling jump by ⌈log₂ n⌉ instead of ⌊log₂ n⌋.

Also d(n) is the comparison count increase - it's known that d(n) ≤ ⌈log₂ n⌉ in some cases? No wait - to insert the nth element into a sorted list of n-1 elements takes at most ⌈log₂ n⌉ comparisons by binary search. And S(n) ≤ S(n-1) + ⌈log₂ n⌉, so d(n) ≤ ⌈log₂ n⌉ always holds (this is a trivial upper bound from insertion).

Also d(n) ≥ something else? And we have d(n) >= ⌈log₂ n⌉ by information bound? Because you need to distinguish n possible positions for the nth element, so need >= log₂ n comparisons, hence d(n) >= ⌈log₂ n⌉. Yes! Both bounds give d(n) = ⌈log₂ n⌉? Wait - let us check.

From above: for powers of two n=2^k, board says d(n)=k=⌈log₂ n⌉ exactly. For general n, d(n) >= ⌈log₂ n⌉ (information bound for insertion) and d(n) ≤ ⌈log₂ n⌉ (binary insertion) so d(n) = ⌈log₂ n⌉ for all n ≥ 2? Let us check the values.
I need to study this carefully on billy-dev context. Let us report findings.

Let us start by examining the board and any existing notes more closely.
Let us analyze this more deeply.

I studied the problem as requested. The claim is about eventual monotonicity of D(n)=S(n)-ceil(log2 n!) on each dyadic interval [2^p, 2^(p+1)) for large p. With known exact values: [8,16) is non-decreasing, [16,32) is non-monotonic (drops at 19->20). D(n)-D(n-1)=d(n)-m(n) where m(n) depends on fractional parts of log2(n!) (causing ceiling jumps with frequency ~50%) while d(n)~log2 n; drops occur when m(n)>d(n). Using Ford-Johnson (upper bound on S(n)) as approximation suggests direction changes persist in larger intervals, but this isn't rigorous for exact S(n). A rigorous all-n disproof would require showing d(n)<m(n) infinitely often with drops occurring in arbitrarily large dyadic intervals, which needs tight unconditional bounds on d(n) relative to m(n)'s behavior - not currently available. The question remains open; the evidence suggests persistent non-monotonicity is plausible, but I cannot produce a rigorous counterexample or proof. No repository changes made.

## Other metadata

```json
{
  "finished_at": 1793342238.6839414,
  "started_at": 1793338829.9147902
}
```
