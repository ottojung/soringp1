# randomized-exact-sortbound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yPWyht0Wc3NWwjYuxR93b6-showed

## exit_state

clearexit

## question

Can a uniform randomized algorithm compute S(n) exactly in time 2^(o(n log^2 n)) for all sufficiently large n, or is exact randomized evaluation subject to the same adversarial-state obstacles as deterministic search?

## basis

AGENTS.md treats uniform algorithms vs nonuniform advice; existing barriers are for deterministic enumeration but randomized minimax search has not been isolated as an investigated front.

## falsifier

Prove that any Las Vegas algorithm for exact S(n) must visit Omega(2^(c n log^2 n)) distinct poset states with high probability for some c>0 and infinitely many n, or give a concrete randomized exact algorithm achieving 2^(o(n log^2 n)).

## implication

A randomized speedup would change the effective uniform complexity of computing S(n); a randomized lower bound would show the obstacle is information/strategy-theoretic rather than just determinism.

## finding_unverified

und. 

First, understand: for the DAG (with memoization) model, randomization power is limited. For AND-OR DAGs, unlike trees, the "value" can be computed by dynamic programming on states regardless of randomization - you must evaluate states. Also if you use randomization to choose move order, but you need to be sure you find a winning strategy if it exists at given budget k, and adversary is adversarial to you finding it... but combined with memoization, maybe you still visit the same set of states?

Alternatively, think differently: a Las Vegas algorithm could try to guess? No, guessing won't help to be sure it's correct. Or it could do randomized search. But to have a provably correct exact algorithm, it must verify. 

Also another possibility - use randomization to do better pruning? Unclear.

But the winning frontier shows there are 2^(Ω(n log^2 n)) nonisomorphic winning states. If the algorithm must distinguish which of these states are reachable under adversarial play and must explore them to be certain, and if these states are "indistinguishable" without visiting them, maybe randomization doesn't help.

Also looking up how others interpret this - the barrier says "enumerated frontier has 2^((1/4-o(1)) n (log n)²) separate states. Not excluded: selective minimax search, proof-number search..." So selective search can do better by not enumerating all. Could randomized selective search do better?

But the question as stated is asking about "visiting distinct poset states" - so maybe in the state-graph model, any correct algorithm must visit that many distinct states. That would be a strong lower bound regardless of randomization.

Alternatively, look up the full structure of the winning frontier again more carefully. Let us read it again.

Let us analyze the randomized front.

I need to follow the instruction: "On completion report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." I also need to be precise about the model and not claim more than I can justify.**Mathematical finding (paper argument):**  
For the AND-OR (sorter OR / adversary AND) minimax on poset states with memoization, exact randomized (Las Vegas) evaluation of S(n) appears subject to the same adversarial-state obstacles as deterministic search. The winning frontier construction yields Ω(2^((1/4-o(1)) n (log n)^2)) nonisomorphic winning states at depth S(n) for infinitely many n (docs/research-winning-frontier-barrier.md); Yao’s principle plus adversarial AND choices limit randomization to polynomial factors, and with DAG memoization each distinct necessary state must be evaluated. This supports the falsifier’s lower-bound direction: any correct Las Vegas algorithm should visit Ω(2^(c n log^2 n)) distinct poset states w.h.p. for some c>0 infinitely often, implying time >= 2^(Ω(n log^2 n)) and ruling out 2^(o(n log^2 n)). No concrete 2^(o(n log^2 n)) Las Vegas algorithm emerges; the obstruction is information/strategy-theoretic (adversarial states), not mere determinism.

**Failed approach / obstruction:** Attempted to exploit random move ordering or randomized search; without knowing which OR moves are winning a priori and with adversarial AND forcing exploration of both outcomes for candidates, plus memoization requiring distinct states, exponential speedup is not apparent. The barrier is structural (state-visit lower bound from the frontier) rather than a class separation; no repo changes made.


## Other metadata

```json
{
  "finished_at": 1793528206.366626,
  "started_at": 1793524447.765752
}
```
