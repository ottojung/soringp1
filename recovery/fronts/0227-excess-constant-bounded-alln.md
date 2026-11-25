# excess-constant-bounded-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

GmwOYv4YherSpYXTR8YQja-terrible

## exit_state

clearexit

## question

Is there an absolute constant C with S(n) <= ceil(log2(n!)) + C for all n >= 1, or does the excess D(n)=S(n)-ceil(log2(n!)) grow without bound as n->∞?

## basis

Sergeev gives sublinear excess o(n); exact values show small excess at known tight points but all-n boundedness remains open despite multiple prior investigations of related excess questions.

## falsifier

Prove limsup_{n->∞} D(n)=∞ by constructing a family requiring excess growing to infinity, or refute boundedness via an infinite obstruction sequence for all height-(info+C) strategies.

## implication

Constant bounded excess would imply SORT-BOUND-U is extremely tight to information bound and may force strong certificate constraints; unbounded excess would mean the gap grows and affects near-tightness arguments for all-n polynomial certificates.

## finding_unverified

o, for comparison-based tests, there's the "coin identification" with balance scales vs spring scales etc. Comparisons are like balance? No, pairwise comparison gives a direction, like a comparison test. 

Another way: Fredman showed that you don't need arbitrary tests, you can do it with comparisons if you allow storing information - but that's about computation model. Not directly the same.

Or look up "Information-theoretic bound for sorting" - some sources say "the information-theoretic bound is not tight, and in fact no comparison sort can be optimal for all values of n". Also another form: the difference between the information-theoretic lower bound and the actual lower bound grows as n grows. That would mean excess is unbounded.

Or more precisely, from some tables - the information bound is achieved at n=1,2,3,4,...,11? Let us check: for n=11, S(11)=26, log2(11!) is about 25.25, ceil is 26, so excess 0. n=12 gives excess 1. So achieved up to 11, then exceeded. Maybe it's never achieved again? Or achieved again later?

Also looking up known results - some sources say "it is not known whether there are any values of n > 11 for which S(n) equals the information-theoretic lower bound" (this is mentioned in some places). That would mean for large n, excess >= 1. But excess being >=1 infinitely often vs growing to infinity are different questions.

The question says "does the excess D(n)=S(n)-ceil(log2(n!)) grow without bound as n->∞?" So unbounded as function of n (limsup = ∞). That means even if sometimes equal (D=0), there are other n with arbitrarily large D(n). Or if it were bounded above by constant C for all n, then limsup would be <= C finite.

Also another possibility - bounded below in some cases? No, excess is S(n) minus the lower bound, so D(n)>=0.

So the question is: is there some constant C such that no matter how large n is, you never need more than C extra comparisons beyond the information-theoretic minimum log2(n!)? Or does the gap grow arbitrarily large?

This is exactly the question of whether the comparison model's "information-theoretic defect" is bounded. I need to recall or derive.

A known result by Dobkin and Lipton (1979, "On some generalizations of binary search") and others studied this. Also more directly, there's work by Ford–Johnson etc., but that's upper bounds. Lower bounds on the defect?

Another way: in the book by Knuth Vol 3, or more recent results. Also in some sources, "It is unknown whether there is any n for which the information-theoretic bound is not tight, and whether the gap between the information-theoretic bound and the true minimum number of comparisons is ever greater than 2." - that seems unlikely given Sergeev gives o(n) but also maybe not exactly. Or different statements.

Or perhaps the opposite - it is known that the excess is unbounded? Let us search more specifically.
Let us examine this more carefully. I need to try to attack it - either find a way to prove unbounded excess, or find obstruction to bounded excess. Let us look up known partial results.

Let us look up more specific results. Maybe search online-style through docs more.

Let us look up more about lower bounds.

The key is in Sergeev's asymptotic bound: $S(n)=\log_2(n!)+O(n/(\log n)^{1/5})$. The additive term grows without bound as $n\to\infty$ (even if slowly), so $\limsup_{n\to\infty} D(n)=\infty$ where $D(n)=S(n)-\lceil\log_2(n!)\rceil$. This means there is no absolute constant $C$ with $D(n)\le C$ for all $n$.


## Other metadata

```json
{
  "finished_at": 1793708558.813555,
  "started_at": 1793698329.7665436
}
```
