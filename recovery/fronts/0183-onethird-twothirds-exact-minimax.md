# onethird-twothirds-exact-minimax

## status

investigated

## origin

ai_proposal_unverified

## agent_id

VX6eq9rexNat4UrOfOM4vy-terminate

## exit_state

clearexit

## question

For all sufficiently large n, does the 1/3-2/3 conjecture (balanced comparison existence under uniform linear-extension distribution) hold for every poset P reachable from an n-antichain in some optimal (height S(n)) minimax strategy, and if not, does its failure create an all-n exponential blowup in the number of states that are simultaneously 'admissible' and 'hard' under any correct exact comparison strategy?

## basis

Kahn–Saks 3/11-8/11 theorem and open 1/3-2/3 conjecture; minimax recurrence F(P)=1+min_{incomparable pairs} max{F(P∪{x<y}^+),F(P∪{y<x}^+)} with P antichain root; winning-frontier enumeration shows large state counts but does not force unbalanced splits; distinguish constant-factor approximation from exact minimax state branching.

## falsifier

Construct an infinite family of n-antichains for which every S(n)-optimal strategy produces at some reachable level only posets with NO comparison giving outcomes in (1/3,2/3) of linear extensions (all splits <1/3 or >2/3), and show this forces superpolynomially many minimax states to remain unresolved below the information-theoretic window for all large n.

## implication

A universal 'balanced split' property for all optimal-play reachable states would justify pruning heuristics used in exact S(n) search; its failure as a structural invariant would imply that balanced-split heuristics cannot be correctness-preserving in the worst case for exact minimax computation and would constrain the feasibility of subexponential exact evaluators.

## finding_unverified

 is asking about whether the 1/3-2/3 conjecture (balanced split property) holds for posets reachable on some optimal minimax strategy for sorting, and if not, whether failure creates exponential blowup.

Let us start by analyzing this question carefully.

Let us study the question carefully. We need to try to DISPROVE the claim that 1/3-2/3 holds for all posets reachable in some optimal (height S(n)) minimax strategy from n-antichain. Or alternatively, show the failure creates exponential blowup.

Let us understand this well. The 1/3-2/3 conjecture says every finite poset (not total) has some incomparable pair with linear extension split probability in (1/3, 2/3) under uniform distribution. This is open in general. Kahn-Saks gave 3/11-8/11.

The question is: restrict to posets *reachable from n-antichain in some optimal (height S(n)) minimax strategy*. Is 1/3-2/3 true there? And if false (there are posets on optimal paths with NO balanced comparison in 1/3-2/3 range, only lopsided splits), does that create exponential blowup in "admissible and hard" states?

Also "admissible" in terms of information-theoretic bound - satisfying e(P) <= 2^(remaining budget). "Hard" - meaning they need many more comparisons (large F(P))?

And the falsifier says: construct infinite family where EVERY S(n)-optimal strategy produces at some reachable level only posets with NO comparison in (1/3,2/3), and show this forces superpolynomially many minimax states to remain unresolved below the information-theoretic window.

So the goal is to try to DISPROVE either part - maybe find such a family? Or show it's impossible? The instruction says "study AGENTS.md, docs/problem.md and current board #301. Study the primary literature, attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it."

We need to attack the claim in the FRONT section. The FRONT asks: "does the 1/3-2/3 conjecture (...) hold for every poset P reachable from an n-antichain in some optimal (height S(n)) minimax strategy..." - so the claim/hypothesis being tested is that it DOES hold (or alternatively the full combined claim). Or we need to be precise about what to falsify.

Looking at the full instruction again: "attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it. Distinguish general-poset results and certificate SOUNDNESS from completeness..." The FRONT gives the question; FALSIFIER gives a construction to try. So probably the claim to attack/falsify is something like "the 1/3-2/3 property holds for all posets on optimal minimax paths for sorting" or that this property is necessary for good pruning - and the falsifier tries to show the opposite creates exponential blowup issues.

We need to give an honest mathematical finding/report.

Let us look up the C2 experiment results more closely.

Let us look up more details about the structure of states in sorting.

Let us write up our findings.

The report has been written to REPORT_301.md in the repo. The key findings: for n=3,5,6 every optimal minimax strategy is forced to boundary splits (exactly 1/3,2/3) with no interior balanced comparison under the open-interval reading of the falsifier; for n=4 there is an optimal strategy avoiding this. This matches the falsifier pattern at some n but is not universal, boundary semantics matter relative to the standard conjecture, and no exponential blowup was demonstrated.

## Other metadata

```json
{
  "finished_at": 1793609808.641831,
  "started_at": 1793603983.3105435
}
```
