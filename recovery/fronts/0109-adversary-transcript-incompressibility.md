# adversary-transcript-incompressibility

## status

investigated

## origin

ai_proposal_unverified

## agent_id

7rZKHzfeJMeLHeQqzumoNO-crystal

## exit_state

clearexit

## question

For the budgeted minimax game on n-antichains, is there an infinite family of n such that every uniform adversary strategy achieving height S(n) produces decision transcripts that are incompressible under any uniform isomorphism-class memoization scheme, forcing Ω(N log N) work-tape bits for any correct uniform evaluation of SORT-BOUND-U on inputs of length N = n+k+1?

## basis

Budgeted DFS gives O(N log N) space for SORT-BOUND-U (problem.md); space-lower-bound-unary notes transcript storage but leaves quotienting tradeoffs open; poset-canonicalization-state-complexity found no settled all-n class bound.

## falsifier

Construct a uniform polynomial-space (in N) algorithm that, by a canonical quotient of reachable poset states beyond naive isomorphism classes, computes exact F(P) for all P on any S(n)-optimal play and decides SORT-BOUND-U for all n >= 2 in space o(N log N).

## implication

Would establish a tight space lower bound matching the known O(N log N) budgeted DFS upper bound for the unary threshold, distinguishing sorting-poset structure from arbitrary poset games where stronger quotienting is known.

## finding_unverified

general. Also the "optimal-play states" quotient is mentioned as potentially smaller.

Let us write up a detailed analysis.

The task says to study and try to disprove the claim. I need to give an honest mathematical finding/report. Based on the analysis above, I don't see a clear proof either way - the claim is plausible but not obviously provable; the falsifier is hard but not obviously impossible given current knowledge. Let me provide a detailed, honest report.**Finding (paper-level analysis, no new theorem proved):** The claimed lower bound **Ω(N log N)** is consistent with known space accounting of the transcript DFS, but not obviously forced.

**Evidence for the claim (supporting incompressibility):**
- **Path storage is inherent:** Transcript-only DFS stores the current comparison path of depth d = Θ(S(n)) = Θ(n log n) with each step taking Θ(log n) bits → O(d log n) = O(N log N) space (budgeted-dfs.md §5.2–§5.3). Memoization adds table space rather than removing the current path stack.
- **All-reachable quotients don’t shrink exponent:** Safe quotients beyond naive S_n relabeling (duality; series/ordinal-sum and parallel/disjoint-union module reversals) are exact but class counts remain exponential in Θ(n²); prime-module reversals break exactness at n≥7 (orientation-modules, parallel-module work). Comparability graph fails for F at n=7. Total reachable states stay 2^(Θ(n²)), way larger than polynomial in N.
- **Optimal-play quotient likely hard to compress:** For NP-certificate routes one needs polynomial classes on states appearing on some height-S(n) optimal play under a local framed-move congruence; uniform-time-exponent-barrier argues this optimal-play quotient is super-polynomial and not compressible by any local congruence compatible with framed moves/optimality (conjecture). Certificates-barriers list optimal-play state counts as open.

**Evidence against the claim / for the falsifier (plausible routes):**
- **Restrict to optimal play:** The falsifier only requires computing F(P) for P on any S(n)-optimal play (not all reachable). If the set of such states is polynomially bounded up to some exact quotient beyond naive isomorphism, space could drop below O(N log N). This is exactly the NP-certificate question (open).
- **Safe quotients + different algorithm:** Combine S_n×Z₂ with exact series/parallel module reversals, restrict to optimal-play states, use a bottom-up/iterative method avoiding deep path stacks. No theorem rules this out.
- **No local-congruence obstruction proved:** The conjectured obstruction is to the *DAG-of-classes/local congruence* route for NP certificates, not obviously to all uniform algorithms with different structure; conversely, no polynomial exact quotient is known.

**Obstruction/failed approach:** No known exact quotient beyond safe modules is polynomial; prime modules break exactness. Any quotient that misorders prime modules changes F. The main open questions are (1) polynomial boundedness of optimal-play quotient classes under some exact equivalence, (2) whether a non-DFS algorithm can avoid storing long transcripts. Neither is settled.

**Honest limits:** I cannot disprove the claim or prove it from current results. The transcript DFS gives a concrete O(N log N) upper bound; achieving o(N log N) uniform space would require either a polynomial exact optimal-play quotient or a fundamentally different algorithm - both unproven. This is an open structural question, not a settled lower bound.


## Other metadata

```json
{
  "finished_at": 1793447953.8521166,
  "started_at": 1793443894.0175602
}
```
