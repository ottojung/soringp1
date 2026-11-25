# branching-program-width-sorting

## status

investigated

## origin

ai_proposal_unverified

## agent_id

X7d9Lz4BngoXMTYpO9oIEW-happy

## exit_state

clearexit

## question

Is SORT-BOUND-U decidable by uniform width-k branching programs of polynomial size for fixed k (bounded-width BP), or does every bounded-width BP deciding it require super-polynomial size for all fixed k and all sufficiently large n?

## basis

Barrington's theorem links bounded-width BP to NC^1 in power but model constraints differ; ordered/uniform BPs are investigated in some fronts but a clean all-n bounded-width separation for the sorting-threshold remains open.

## falsifier

Construct a fixed-width uniform BP family of polynomial size deciding SORT-BOUND-U for all n, or prove an all-n super-polynomial lower bound for all fixed widths using the comparison-game structure without circuit lower bounds forbidden for P/poly.

## implication

A bounded-width BP lower bound would place SORT-BOUND-U outside the union of fixed-width branching program classes under uniformity, distinguishing it from many regular/NC^1-like structured functions despite unary encoding.

## finding_unverified

Let us start by reading more about the game structure and the PSPACE proof again.

Let us look up the full instruction again carefully:
> "- A uniform super-polynomial lower bound would need a method that does not exist for any natural problem in PSPACE." (from problem.md:102)
> "- circuit lower-bound methods cannot help. Do not spend research time on unconditional super-polynomial lower bounds for the unary language." (from AGENTS.md)

But NC^1 is a class of functions computable by poly-size circuits of logarithmic depth (or equivalently bounded-width BPs). A lower bound against NC^1 means showing the function is not in NC^1 - which is a kind of lower bound (separation). Is this considered "super-polynomial lower bound" in the sense the AGENTS warns against? Or is the warning specifically about trying to get lower bounds against P/poly or against polynomial time in general? Because showing something is not in NC^1 is not the same as showing it's not in P.

But this is important to get right. Let us look up more context from the repo. Also look up how others have interpreted - maybe look up board or other fronts? For example, there might be fronts about NC^1? Let us search.
Let us start investigating this front.

Let us start by exploring this systematically.

Let us analyze this.

I'll start by investigating the bounded-width BP question for SORT-BOUND-U.

Let us prepare a report on this research question.

I studied the repo materials and attacked the bounded-width BP question for SORT-BOUND-U. The strongest plausible obstruction is the comparison-game depth: for informative instances k=Θ(S(n))=Θ(n log n), N=n+k+1 gives game depth k=Θ(N) while NC^1 (ALOGTIME) allows only O(log N) time steps - an inherent depth/time obstruction if no shortcut exists. This uses the comparison-game structure without invoking forbidden P/poly circuit lower bounds. Construction seems implausible. The depth argument is not a categorical proof (a surprising non-game-simulating algorithm can't be ruled out), but it's concrete. Distinguished general-poset results/certificates from the BP algorithm question. No repository changes made.

## Other metadata

```json
{
  "finished_at": 1793795365.3836498,
  "started_at": 1793789894.4068925
}
```
