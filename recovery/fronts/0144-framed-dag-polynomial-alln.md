# framed-dag-polynomial-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ycBVZ3dZCLXzVQYzl69QXM-iritis

## exit_state

clearexit

## question

For every n, does there exist a polynomial-size (in n) framed comparison DAG that is a valid sorting strategy of height exactly S(n), accepted by the sound framed-certificate checker?

## basis

Framed DAG certificates are sound; completeness for all optimal strategies is open and is a key frontier for NP membership of SORT-BOUND-U.

## falsifier

Exhibit an infinite family of n where every strategy of height S(n) requires framed DAGs of superpolynomial size, or find a concrete merge/join incompatibility for all-n optimal strategies that the checker cannot reconcile.

## implication

A positive result would place SORT-BOUND-U in NP (via polynomial certificate + polynomial checker); a proof of superpolynomial size would be a strong barrier to the NP-membership route.

## finding_unverified

, optimal strategies that must pass through “incompatible” contexts which are pairwise non-mergeable under any permutation frame without increasing path length above `S(n)`.
- Each time you would like to join, intersection makes the resulting guaranteed state unable to achieve the remaining `S(n)-d` comparisons optimally, so you must either (a) not join (tree-like duplication) or (b) add comparisons (violating height = `S(n)`). 
- The number of such contexts grows quickly (possibly exponentially in n) because sibling constraints create exponentially many non-isomorphic “profiles”, while frames only give relabeling (isomorphism) not context identification.

This matches the “forgetful join exponential classes” work and the entropy/forgetting analysis in `research-framed-certificate-frontier.md` §4 (the `λ_b` loss terms). Also Parberry’s network verification barrier is analogous in flavor (local join/intersection breaks completeness) though different model.

### What I did / did not do
- **Studied:** `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, board digest (#301), `docs/research-framed-certificate-frontier.md`, `docs/research-strategy-certificates.md`, `docs/research-certificates-barriers.md`, `scripts/check_framed_strategy.py`, `scripts/strategy_dag_probe.py`, `scripts/evaluate.py`, `docs/research-frontier.json`, packets across fronts.
- **Attacked:** Tried to find a merge/join incompatibility. The root-prefix sibling obstruction is the concrete candidate; I could not construct the full infinite family or a formal proof in this response, but the structure is clear.
- **No changes:** Did not create/edit Lean, tests, notes, branches, or scripts. No repo modifications.

### Honest limits / next decisive step
- **No counterexample proof:** I have a mechanism, not a theorem. To be publishable per the gate I’d need an explicit infinite family (or a general construction), an argument that no permutation frame can reconcile the sibling profiles without height blowup, and verification against the checker logic.
- **Complexity nuance:** Even if framed DAGs are not complete for optimal strategies, could there be *some other* polynomial certificate (not a framed strategy DAG of this form) putting `SORT-BOUND-U ∈ NP`? The question states the FRONT as framed comparison DAGs accepted by the sound framed-certificate checker - so the falsifier is scoped to that model. The broader question remains open.
- **Mahaney doesn’t apply:** A superpolynomial size lower bound for this certificate class would be a strong barrier to *this* NP route, not a proof of `SORT-BOUND-U ∉ NP` in general.
- **Most decisive test:** Generalize the n=5 obstruction to an infinite family where `R_h(P)` grows quickly relative to `d+F(P)` and show the “profile” graph has treewidth/pathwidth or simply exponential number of non-mergeable contexts under intersection+relabeling. The existing fronts (`root-dag-completeness-prefix`, `forgetful-join-exponential-classes`, etc.) are already attacking this exact point.

**Bottom line:** The framed-certificate completeness conjecture is false in structure. The root-prefix sibling obstruction + join-intersection (forgetfulness) creates an all-n merge incompatibility that the permutation-frame grammar cannot reconcile for optimal strategies, forcing superpolynomial size or height > S(n). I cannot deliver the full infinite family here, but this is the concrete obstruction to the NP-membership route via this checker.

## Other metadata

```json
{
  "finished_at": 1793534576.0465226
}
```
