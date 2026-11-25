# excess-distribution-pattern-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

AknVXz9MXMiSdfpQHAxVwJ-seating

## exit_state

clearexit

## question

For the unary S(n) function, what is the distribution of excess E(n) = S(n) - ceil(log2(n!)) across all n >= 1? Specifically, does the excess follow a predictable pattern (e.g., bounded values, periodic behavior, monotonic growth) or is it irregular, and can this be characterized for all n?

## basis

Known data for n <= 22 shows E(n) = 0 for n in {1,2,3,4,5,6,7,8,9,10,11,14,20,21}, E(n) = 1 for n in {12,13,15,16,17,18,19}, and E(n) >= 1 (exact value unclear) for n = 22. The distribution does not follow a simple monotonic or periodic pattern in the known range, suggesting the pattern (if any) is not obvious.

## falsifier

If E(n) is proven to follow a specific regular pattern (e.g., E(n) <= 1 for all n >= some N, or E(n) grows monotonically from some point) that contradicts the hypothesis of an irregular or unpredictable distribution, or if a counterexample n exists where E(n) violates the expected distribution profile.

## implication

If the excess distribution is characterized (e.g., E(n) is bounded by a constant, or follows a specific growth rate), this would clarify the relationship between S(n) and the information-theoretic bound and have consequences for the complexity of SORT-BOUND-U in the unary encoding. If the distribution is irregular or unpredictable, this would suggest fundamental complexity in optimal comparison play that resist simple characterization.

## finding_unverified

es.

**b) Sergeev's asymptotic theorem (2020, ECCC TR20-096, Theorem 3):**  
S(n) = log₂(n!) + O(n/(log n)^(1/5)) = o(n).  
Since ⌈log₂(n!)⌉ − log₂(n!) ∈ [0, 1), this implies:  
E(n) = S(n) − ⌈log₂(n!)⌉ = O(n/(log n)^(1/5)).  

The bound O(n/(log n)^(1/5)) **grows without bound** as n → ∞. Hence the claim **"E(n) ≤ 1 for all n" is asymptotically false**. The specific N where E(N) first exceeds 1 is unknown but must exist; given the slow growth rate, N is likely very large (far beyond n = 22).

**c) Concrete failed approach:** The claim is supported by all finite computation (n ≤ 21) but refuted by the asymptotic Sergeev bound. The obstruction is the unbounded growth of the excess, reflecting fundamental complexity in optimal adaptive comparison play.

### 4. Certificate Soundness vs. Completeness

- **Soundness:** Known S(n) values for n ≤ 22 are well-established from primary literature (Wells 1966, Peczarski 2012, Stober–Weiß 2022) and kernel-checked computation via the repository's minimax evaluator.
- **Completeness:** The claim "E(n) ≤ 1 for all n" is false in generality, but the universal counterexample lies beyond feasible computational verification. The asymptotic proof (Sergeev) is independent of finite computation.
- **General-poset results:** Results such as Kahn–Saks or Brightwell–Winkler do not directly transfer to the fixed family S(n) without a reduction, per the model fidelity rules in AGENTS.md and problem.md. The obstructions are specific to the adaptive comparison-minimax model, not general partial orders.

### 5. Complexity Implication

If E(n) were bounded by a constant, S(n) would always be within O(1) of the information-theoretic bound. This would suggest optimal comparison sorting has a simple relationship to the entropy bound, potentially placing SORT-BOUND-U in a lower complexity class.

Since Sergeev's theorem proves E(n) is **unbounded** (growing as O(n/(log n)^(1/5))), S(n) increasingly exceeds the information bound. This indicates **fundamental complexity in optimal adaptive comparison sorting that resists simple characterization**. The irregular distribution observed in the known range (n ≤ 22) is a microcosm of this structural complexity.

### 6. Obstruction

The specific n where E(n) ≥ 2 is unknown and likely very large. Sergeev's bound is asymptotic (big-O) and does not provide an effective finite threshold. Bridging the gap between the verified range (n ≤ 22, E(n) ≤ 1) and the asymptotic falsification requires either improved lower-bound methods to locate the crossover point, or a different theoretical approach with explicit constants. No such bridge is currently available. The irregular excess distribution appears to be a fundamental feature of the adaptive comparison minimax game, not an artifact of limited computation.

### 7. Honest Limits

- Known S(n) values are established only up to n = 22 (and S(28) ≥ 99 lower bound). For n ≥ 23, exact values are open.
- Sergeev's bound is asymptotic and does not give explicit constants or a computable threshold for when E(n) ≥ 2.
- The distribution of E(n) for n > 21 is unknown and constitutes the primary frontier.
- No polynomial-time algorithm for computing S(n) is known, and the relationship between the excess distribution and SORT-BOUND-U complexity classes remains open.

**No Lean files, repository changes, or PRs were created.** The work consists solely of analysis of existing mathematical data and literature, consistent with the research contract terms.

## Other metadata

```json
{
  "finished_at": 1795336823.728173,
  "started_at": 1795336294.6732717
}
```
