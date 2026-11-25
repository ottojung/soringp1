# adversary-strategy-compression

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4RC7Mi6RdrUg9NwVSEocFq-improper

## exit_state

clearexit

## question

For infinitely many n, does every minimax-optimal adversary strategy for S(n) require description complexity exponential in n log n, regardless of any polynomial quotient that may be hard to discover, as a direct consequence of the winning frontier?

## basis

Winning frontier result in research-winning-frontier-barrier.md showing exponentially many nonisomorphic winning states at fixed depth reachable from antichain.

## falsifier

Exhibit a uniform polynomial description for some optimal adversary family achieving the asymptotic S(n) values on those n, or prove polynomial compressibility of all optimal adversary strategies.

## implication

Exponential adversary description complexity would obstruct certain dual-certificate approaches and sharpen the asymptotic barrier from the large winning frontier without invoking general super-polynomial lower bounds on the decision language.

## finding_unverified

Description vs enumeration:** The frontier gives $\Omega(2^{c n(\log n)^2})$ winning states, but a strategy is a *function* $T(P,\{u,v\})\!\to\!\text{answer}$, not an enumeration of states. The barrier itself notes "A selective or symbolic algorithm need not enumerate every state"—same for strategy descriptions.
- **Polynomial strategy (falsifier 1):** The information-theoretic adversary $T_{LE}$ answers to maximize the number of linear extensions of the current partial order. Its rule is constant-length (uniform in $n$). $T_{LE}$ achieves the information-theoretic bound $\log_2 n!$; Sergeev gives $S(n)=\log_2 n!+o(n)$, so $T_{LE}$ forces $(1-o(1))S(n)$ comparisons for all large $n$ (asymptotically optimal). This matches "achieving the asymptotic $S(n)$ values on those n". 
- **Exactly optimal / ties:** The minimax value $F(P)$ can differ from linear-extension counts in tie cases for general posets, but (i) description length is still short if defined via the minimax recurrence (rule-based), (ii) the claim requires this for *every* minimax-optimal strategy—if some tie-breaking makes $T_{LE}$ exactly optimal in relevant cases or if other simple strategies exist, that already falsifies "every..." for asymptotic/standard notions. More directly, the class of minimax-optimal strategies is non-empty and contains rules with short descriptions (the recurrence form); computation hardness of $F(P)$ or $\#LE(P)$ affects evaluation time, not description complexity (Kolmogorov/program length). The phrase "regardless of any polynomial quotient that may be hard to discover" does not block a short rule that references it.
- **Symmetry/compression:** Sorting is $S_n$-symmetric; optimal strategies admit canonical/orbit descriptions, further compressible. Polynomial quotient-discovery concerns are orthogonal to short program descriptions.
- **Certificate distinction:** The frontier obstructs *enumeration-based* dual certificates (large explicit lists), but a short strategy description is a different certificate form. The complexity implication is better read as "blocks certain dual-certificate approaches" (the enumerative ones), not that all strategies are large.

**Obstructions / honest limits:**
- **Exact optimality for all $n$:** I cannot rule out some extremely pathological finite $n$ or some restrictive model where every exactly-minimax-optimal strategy is forced to be table-like. This is subtle and would need a careful proof; I have no such proof.
- **Definition of "description complexity":** If interpreted as the size of an *explicit decision tree/table* of the strategy (not program length), the claim becomes closer, but that is not standard terminology and contradicts "description complexity" language. Also minimax strategies need not be given as explicit tables.
- **Frontier reachability:** An optimal adversary might be able to avoid some frontier branches via different choices while still achieving $S(n)$; the existence of states doesn't force the *strategy* to encode each one if it uses a rule-based invariant.

**Conclusion:** The claim as stated is false for asymptotic optimality (clear counterexample $T_{LE}$). For exact optimality it is unproven and appears unlikely given the program-description sense and standard game theory; the winning frontier is better understood as a barrier to state-enumeration approaches, not as forcing exponential strategy-description complexity. No repository changes warranted—this is a negative/conceptual finding.

## Other metadata

```json
{
  "finished_at": 1793480115.4232416,
  "started_at": 1793479715.4659345
}
```
