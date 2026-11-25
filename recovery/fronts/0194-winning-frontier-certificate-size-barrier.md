# winning-frontier-certificate-size-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

45UxzEhcZIcEotGXagfUWW-savory

## exit_state

clearexit

## question

For the large winning frontier of nonisomorphic reachable states (Ω(2^(c n (log n)^2)) at information depth), does there exist an all-n polynomial-time checkable certificate for SORT-BOUND-U membership that can represent its strategy without enumerating that frontier, or is there a structural certificate-size obstruction?

## basis

docs/research-winning-frontier-barrier.md establishes 2^((1/4-o(1)) n (log n)^2) nonisomorphic winning states; certificate soundness/completeness gap is central to #301; NP membership remains open.

## falsifier

Prove that every correct proof system for SORT-BOUND-U has some yes-instance requiring superpolynomial certificate size due to the winning frontier's branching structure, or construct a uniform polynomial certificate scheme exploiting strategy compression.

## implication

A polynomial certificate would place SORT-BOUND-U in NP (a major class inclusion); a superpolynomial certificate-size lower bound under natural proof systems would rule out NP membership regardless of algorithmic speedups.

## finding_unverified

hare enough?

From strategy_dag_probe: for n<=6, DAG(all) grows quickly (19,181,1551,65551...) while n! grows as 1,2,6,24,120,720. Ratio grows. But small n. Also quotient by isomorphism gives more compression. But is it polynomial?

But we don't know for large n. The winning frontier construction gives exponentially many states - but are all those states in the all-optimal DAG? A state is in the DAG if it's reachable by some optimal strategy and we keep all optimal moves. Or if it's on some optimal play. The frontier states are winning (F(P) <= k-t) - they might be on optimal paths.

But even if there are exponentially many states total, a DAG can share structure. The question is whether the "branching structure" of the frontier forces exponential DAG size. If the strategy must make different choices on nonisomorphic frontier states and they can't be compressed, then yes. But if the optimal strategy can use the same pattern (chain merging) on all of them, then they can be compressed.

This is the crux. Let us look up how the chain merging works more carefully.
**Mathematical finding (not a proof):**

**Compression is the natural escape.** The winning frontier gives $2^{\Omega(n\log^2 n)}$ nonisomorphic reachable winning posets $P_A$ from the chain+extra-edges construction (docs/research-winning-frontier-barrier.md). A single uniform strategy (balanced chain merging of the $s$ fixed chains) works for *all* $P_A$ because extra edges only add order constraints (easier). In a quotient/framed certificate (permutations/frames), those states need not be enumerated - they can be mapped to the same parametric strategy nodes. The barrier explicitly excludes *algorithms that output/enumerate all frontier states*, not *parametric DAG certificates* (README/research-plan). So the frontier does not, by itself, force exponential certificate size.

**Obstruction to the lower-bound direction:** The falsifier asks for an unconditional superpolynomial certificate-size lower bound for *every correct proof system* (ruling out NP). AGENTS.md forbids spending research time on unconditional superpolynomial lower bounds for the unary language (they are equivalent to $P\neq PSPACE/NP\neq PSPACE$ class separations); circuit methods don’t help and no general method exists. Also sparsity blocks naive many-one NP-hardness but NP *membership* is the question - a general proof-system lower bound of this form is in the forbidden category. Distinguish: **soundness** of the framed/intersection model is restricted (can lose disjunctive correlations), but that’s a completeness-of-model issue for some strategies, not an obvious all-proof-systems obstruction from this frontier.

**Failed/blocked approach:** Cannot produce a clean disproof of polynomial certificates or a valid obstruction theorem under project constraints. The chain structure is compressible; the only plausible obstruction would require showing no parametric representation exists for *some* class of instances despite uniform structure, which is not obvious and likely not provable without crossing into forbidden territory. No repository changes made (no theorem/counterexample strong enough to meet publication gate).

**Honest limits:** NP membership remains open. The decisive question is whether *some* optimal strategy for every $n$ admits a polynomial-size framed/strategy DAG (docs/research-framed-certificate-frontier.md §5) - the winning frontier is consistent with compression, not a demonstrated obstruction.

## Other metadata

```json
{
  "finished_at": 1793634746.1235402,
  "started_at": 1793631007.813584
}
```
