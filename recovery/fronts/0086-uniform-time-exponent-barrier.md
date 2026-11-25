# uniform-time-exponent-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QAiWKHR31fSgSAtWKjpDao-imperial

## exit_state

clearexit

## question

Is there an all-n lower bound showing that every uniform deterministic algorithm computing S(n) (or deciding SORT-BOUND-U) must run in time at least 2^(Omega(n log n)) on unary inputs, or can the budgeted DFS exponent be reduced below n log^2 n uniformly?

## basis

budgeted DFS gives 2^(O(n log^2 n)); problem states faster exact evaluators in scope; no all-n uniform time exponent barrier found in reviewed investigations.

## falsifier

Give a uniform algorithm achieving time 2^(O(n log n / log log n)) for all large n with proof, or prove that the poset state graph of the minimax recurrence requires time 2^(Omega(n log n)) to evaluate by any uniform method that accesses states by standard representations.

## implication

A tight uniform time lower bound would clarify the position of S(n)-evaluation relative to PSPACE and rule out near-linear-exponent improvements; a better algorithm would improve the known uniform upper bound.

## finding_unverified

t mean simpler cuts fail. The $n=12$ gap ($S(12)> \lceil\log_2 12!\rceil$) is exactly where information pruning fails.
- **Complexity constraints.** Unary is sparse (Mahaney blocks many-one NP-hardness unless P=NP) and in PSPACE; circuit lower bounds don’t apply. Showing a uniform super-polynomial lower bound for unary would imply $P\neq PSPACE$ (a major separation) with no known technique. The “standard representations” (poset/transcript states accessed directly) don’t obviously create a known information-theoretic time lower bound beyond the game-tree size.

**Attempted falsifiers / obstacles:**
1. **Try to beat exponent by selection:** selective minimax (e.g. good move ordering, alpha-beta, proof-number search) is not excluded by the winning frontier. However, the frontier shows there are exponentially many “winning” states at the same level - adversarial choice can force exploring many branches; without a better global strategy it’s unclear how to guarantee < $n\log^2 n$. Also branch-and-bound needs strong admissible heuristics; the only strong general lower bounds on $F(P)$ are information-based and the one-ply/structural bounds (which are themselves costly to compute exactly). No concrete uniform algorithm achieving $2^{O(n\log n/\log\log n)}$ is obvious from the codebase.
2. **Try to prove a lower bound:** to get $2^{\Omega(n\log n)}$ for algorithms accessing states by standard representations, you’d need that the minimax DAG has path-count/exploration lower bounds. The winning frontier is a state-count barrier for enumeration but not obviously a time lower bound for a minimax algorithm that can choose moves. Also “standard representations” is vague - you might be able to use different encodings. No standard representation lower bound is present in the reviewed notes.

**Concrete failed approach / exact obstruction:**
- The cleanest obstruction to *beating* by enumeration is the winning frontier ($2^{\Omega(n(\log n)^2)}$ nonisomorphic winning states) - but that’s only for “enumerate all winning states”. Selective search dodges it by construction.
- The cleanest obstruction to *easy* pruning is the $n=12$ information-gap / one-ply obstructions and trivial-automorphism posets ($\Theta(n^2)$ pairs). These hurt constant factors/pruning, not the asymptotic exponent.
- No theorem in the repo rules out $2^{O(n\log n)}$ uniform time; no theorem proves it necessary for “standard representations”. The question remains open. The most honest answer: **no all-n uniform time exponent lower bound below $n\log^2 n$ is known, and the stated barriers don’t forbid reducing the exponent below $n\log^2 n$ via selective search/canonicalization - but no concrete algorithm achieving $2^{O(n\log n/\log\log n)}$ is evident, and achieving below $n\log^2 n$ would require beating both the $\Theta(n^2)$ branching in worst bad cases and the $\Theta(n\log n)$ depth without simply enumerating the large winning frontier.**

**Complexity implication:** tightening to $2^{\Omega(n\log n)}$ would separate $SORT\text{-}BOUND\text{-}U$ from classes below exponential in $n\log n$ in that exponent scale but $SORT\text{-}BOUND\text{-}U$ is already in PSPACE; more directly, it would rule out “near-linear in the information-theoretic exponent” uniform improvements. A better algorithm would improve the known uniform upper bound (and is in scope per problem statement). Neither is established here.

No repository changes made (no substantive new theorem/counterexample found).

## Other metadata

```json
{
  "finished_at": 1793406826.5273244,
  "started_at": 1793402622.8316107
}
```
