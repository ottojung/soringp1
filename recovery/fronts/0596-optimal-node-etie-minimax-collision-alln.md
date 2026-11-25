# optimal-node-etie-minimax-collision-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

OOvVbqh1SNEVEm79YMTG0Z-formally

## exit_state

clearexit

## question

Can every n be sorted by a height-S(n) optimal decision tree in which no comparison at any reachable state splits that state into two children of equal linear-extension count but unequal true minimax value?

## basis

A new from-scratch search at n=6 found a greedy-reachable state (e=28) where comparing keys 1 and 3 yields extension-tied children (e=14 each) with minimax values 5 and 4, and that comparison is minimax-optimal at the parent; no all-n forced structure is known.

## falsifier

Prove that for infinitely many n every height-S(n) sorting tree must use a comparison whose two children are extension-tied yet have different minimax values, or isolate an unavoidable such node on all optimal strategies.

## implication

A positive answer sharply restricts the structure of optimal trees and permits pruning of exhaustive exact evaluators; a negative answer shows harmful extension-ties are unavoidable and must be handled by any exact algorithm.

## finding_unverified

RM**; 8 other optimal comparisons are non-harmful.
- `up=[118,52,32,80,0,0,16]`, e=28, F=6: (4,5) e=(14,14), F=(5,4), val=6 **OPT HARM**; 5 others non-harmful.
- `up=[2,0,27,3,0,83,0]`, e=56, F=7: (0,6) e=(28,28), F=(6,5), val=7 **OPT HARM**; 8 others non-harmful.
- `up=[62,0,50,2,32,0,10]`, e=28, F=6: (1,5) e=(14,14), F=(5,4), val=6 **OPT HARM**; 5 others non-harmful.
- `up=[28,93,16,0,0,72,8]`, e=28, F=6: (3,4) e=(14,14), F=(5,4), val=6 **OPT HARM**; 5 others non-harmful.

In every inspected n=7 counterexample state, **not all optimal comparisons are harmful** (each has multiple non-harmful optimal alternatives), so the state is avoidable within an optimal strategy at that node. **No forced-harm state (all optimal comparisons harmful) was found.** Because the broad forced-harm search was interrupted (incomplete), this is **not** evidence that none exists at n=7 or all n.

### 3. Failed approach (disproved strengthening)
**“Theorem A” (stronger avoidance):** every poset has an optimal comparison whose two children have equal minimax value F(c0)=F(c1). **False** already at small n by exhaustive check: failures among states with F>0 are 6/13 at n=3, 72/195 at n=4, 1320/4111 at n=5, 28800/129303 at n=6. Therefore equal-F optimal splitting is not a general structural property (and is unnecessary for the front); only non-harmful-among-optimal matters.

## Exact obstruction / honest limits (open status of the front)
- **Positive horn (all-n): OPEN.** It would follow from a local/strategy lemma: every poset reachable on some height-S(n) strategy has ≥1 optimal comparison that is not a harmful e-tie (in particular, no forced-harm state is unavoidable on all optimal strategies). This is proved here for n≤6 but refuted in its “every optimal comparison is safe” strong form at n=7; the weaker “some optimal comparison is safe at every encountered state” remains unproved and unrefuted in general.
- **Negative horn / falsifier: OPEN.** A valid falsification would require, for infinitely many n, a state unavoidable on **every** height-S(n) tree such that all its optimal comparisons are harmful e-ties (a forced-harm obstruction), or an equivalent global argument. I did not find such a state; the n=7 search was incomplete after interruption.
- **Why this is hard:** at n=7 harmful optimal ties first appear, showing the phenomenon is real at optimal nodes (unlike n=6 evidence suggested), but optimal decision trees retain choice; certifying “unavoidable on all optimal strategies” is a global property of the minimax game (all optimal policies) and was not resolved here.
- **Complexity implication (status):** neither the pruning restriction (positive) nor the forced-handling necessity (negative) is established all-n. No claim about S(n) values, SORT-BOUND-U membership/separation, NP/coNP certificates, or EXPTIME/PSPACE improvements follows from these finite computations; this is structural evidence/obstruction only.
- **Scope caveat:** results are for the exact comparison-tree minimax model on labeled inputs/poset states (as in the problem); exhaustive results are n≤6, n=7 is sampled/partial — not a proof for all n. Primary literature on exact S(n) (Peczarski 2012; Stober–Weiß 2023; Wells/Knuth/OEIS context per `docs/literature.md`) was consulted for framing; no contradiction with known exact values found (S(6)=10, S(7)=13 consistent). No external side effects were duplicated; interrupted forced-harm search remains for review if a fuller n=7 pass is desired.

## Other metadata

```json
{
  "finished_at": 1795157141.4834654,
  "started_at": 1795155375.137446
}
```
