# subexp-budgeted-dfs-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

rn9vMHXEOXHfx0ka6voq2N-diverse

## exit_state

clearexit

## question

For the unary threshold language SORT-BOUND-U with input length N = n+k+1, is there any all-n uniform deterministic algorithm deciding exact S(n) <= k in time 2^(o(N log N)), or does the structure of budget-reachable poset states force a time lower bound of 2^(Omega(N log N))?

## basis

AGENTS.md states faster or more space-efficient exact evaluation is a realistic frontier; research-budgeted-dfs.md derives 2^(O(N log(N+2))) and asks whether the exponent can be reduced; the winning frontier shows large incompressible state families relevant to budgeted search.

## falsifier

Produce an explicit uniform algorithm achieving time 2^(o(N log N)) for all sufficiently large N with a rigorous correctness argument, or prove that the family of budget-reachable (P,d) states has size 2^(Omega(N log N)) and no correct exact evaluator can avoid visiting a constant fraction of them.

## implication

A verified subexponential-in-N log N algorithm would strictly improve the known uniform upper bound for exact evaluation of S(n); a general barrier theorem would rule out that entire class of approaches and clarify the tight exponent.

## finding_unverified

m achieving this for all large $N$ is present in the repo. Known improvements (transcript vs matrix representation) affect space/polynomial factors, not the $N\log N$ exponent in the time bound. Decomposition/symmetry give exactness but no documented state-count reduction. Algebraic/parametric recurrences are *not excluded* by current barriers, so the door is not closed in principle — but I found no rigorous construction or reduction that actually beats the DFS exponent. **Attempt to produce one: inconclusive / no concrete algorithm.**

2. **Lower bound / “must visit” a constant fraction:** The frontier rules out *methods that necessarily enumerate all* reachable winning states/transcripts (would need $\ge 2^{\Omega(N\log N)}$ states). However the docs explicitly list methods *not excluded*: selective minimax search, proof-number search, stronger state compression/canonicalization, parametric DAG sorting certificates, algebraic recurrences, or any method that evaluates $S(n)$ without listing the full frontier. The root antichain may be losing at budget $k$ in that regime too (frontier is reachable but root need not be inside it as a “must visit” set for all correct evaluators). Automorphism-orbit pruning fails on families with trivial orbits but that only kills *that* heuristic, not all methods. Also “no correct exact evaluator can avoid visiting a constant fraction of them” is stronger than current evidence supports — it would rule out selective methods which are explicitly *not* ruled out. I found no paper argument giving this universal “must visit” property for all correct exact evaluators; the barrier is a strong *enumeration* obstruction, not a general decision-tree lower bound over all algorithms.

**Distinctions (important):**
- This is about *uniform exact evaluation of $S(n)$* (the function/value) for the *antichain root family*, not hardness of arbitrary posets `GEN-SORT` in general — transfer requires a reduction (`docs/problem.md`, `docs/research-hardness-boundaries.md`). 
- Certificate *soundness* vs *completeness*: a polynomial verifier for some strategy DAG is different from showing every optimal strategy has polynomial size (completeness) — the frontier/barrier doesn’t directly settle NP-membership; sparsity gives Mahaney constraints but no membership proof.
- The exponent is in terms of input length $N=n+k+1$ for the unary threshold (and $k$ can be $\Theta(n\log n)$ near optimum). The $2^{\Omega(N\log N)}$ state count matches $N\log N \sim n(\log n)^2$ in that regime.

**Conclusion:** The decisive obstruction is real for *exhaustive/enumerative* approaches, but **not a general lower bound** ruling out all correct exact evaluators. No $2^{o(N\log N)}$ uniform algorithm is known. The question remains open; the tight exponent is not established. Any claim of a general “must visit” lower bound would need to bridge the gap between “large frontier exists” and “every correct algorithm must hit a constant fraction of it” (accounting for selectivity, canonical forms, algebraic methods). I found no such bridge in the reviewed literature/notes.

**Failed approaches noted:** trying to rely on isomorphism/orbit pruning alone (fails on trivial-orbit families), memoizing all reachable states (state graph still huge, and DFS bound already accounts for tree visits; distinct-state count large), and naively transferring arbitrary-poset hardness (no reduction). No repository/Lean changes made; no board post attempted from this environment.

## Other metadata

```json
{
  "finished_at": 1793589304.178853,
  "started_at": 1793587971.851775
}
```
