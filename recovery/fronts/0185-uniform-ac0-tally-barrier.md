# uniform-ac0-tally-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

u3WCUqEJQ0sWMGtZBX7ABw-murat

## exit_state

clearexit

## question

Is SORT-BOUND-U in DLOGTIME-uniform AC^0, or does the all-n nonperiodic growth of S(n) force every DLOGTIME-uniform constant-depth circuit family for its unary threshold to have super-polynomial size given the cutoff t_L depends on inverting S(n)?

## basis

AGENTS notes tally language is in nonuniform AC^0 (depth-two) via advice t_L; uniform classes differ sharply and DLOGTIME-uniformity requires the family to be constructible from input length without arbitrary nonuniform advice.

## falsifier

Construct a DLOGTIME-uniform AC^0 circuit family deciding SORT-BOUND-U for all lengths, or prove that DLOGTIME-uniformity plus constant depth plus polynomial size is incompatible with exactly representing the nondecreasing threshold t_L(n)=max{n : n+S(n)<=L-1} across all large L.

## implication

Separating nonuniform AC^0 (established) from uniform AC^0 would place SORT-BOUND-U below P but above the weakest uniform constant-depth classes, clarifying how advice/computability of the threshold interacts with exact evaluation of S(n).

## finding_unverified

Let us look up the current frontier and board issue.

**FINDING (deduction):** SORT-BOUND-U ∉ DLOGTIME-uniform AC^0.

**Attack/result:** Try to falsify “in DLOGTIME-uniform AC^0” by analyzing uniformity. DLOGTIME-uniform AC^0 ⇔ threshold predicate P(n,k)= (S(n)≤k) decidable in DLOGTIME. DLOGTIME = random-access deterministic TM, time O(log t) on input of length t; with t = O(log max(n,k)) for binary encodings this means only O(log log max(n,k)) adaptive bit queries. 
- **Information/queries:** S(n) is strictly increasing and S(n) ≥ log2(n!) = Ω(n log n), so S(n) determines n and has Ω(n log n) bits of information; deciding P requires either computing S(n) from n or comparing to k. Neither is possible from o(log max(n,k)) queries (pigeonhole: interval of k values larger than 2^(query budget) contains both sides of a threshold at fixed n; adaptive queries don’t help). 
- **Nonuniform vs uniform:** The known depth-2 nonuniform AC^0 uses advice per length L to hardcode which (n,k) valid (table of size O(L^2)). Uniformity cannot construct that table without deciding P in DLOGTIME – impossible. 
- **Distinctions:** Obstruction is query/information complexity of the *threshold/comparison* (and function inversion), not periodicity of S(n) per se (nonperiodic growth consistent but not necessary). This is different from general-poset results (no valid reduction to arbitrary posets here) and not about certificate *soundness/completeness* (obstruction is uniform constructibility). 

**Honest limits:** This is an information-theoretic/query-complexity obstruction for DLOGTIME, not a full Håstad switching-lemma size lower bound for some other model; I did not construct circuits, just showed equivalence+impossibility. I did not find a DLOGTIME-uniform AC^0 family (and see obstruction). The complexity implication holds if nonuniform AC^0 separation stands: uniform AC^0 strictly weaker in this sense than nonuniform advice-based AC^0. No repo/Lean changes proposed.


## Other metadata

```json
{
  "finished_at": 1793612594.867401,
  "started_at": 1793612096.8876975
}
```
