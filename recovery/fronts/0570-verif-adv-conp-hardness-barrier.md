# verif-adv-conp-hardness-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

SDnsxiTkhQYOI9UNNzakyx-confused

## exit_state

clearexit

## question

The newest #301 sorter-refuter report places adversary-soundness VERIFY-ADV (does a given memoryless adversary circuit force more than k comparisons at the n-antichain?) in coNP while sorter-soundness VERIFY-SORT is in P. Is VERIFY-ADV actually coNP-hard, hence coNP-complete, for the exact game G(n, S(n)-1) on all large n, so that checking a refuter's soundness cannot be done in polynomial time unless P = coNP?

## basis

Newest #301 sorter-refuter-duality report B2 (VERIFY-SORT in P, VERIFY-ADV in coNP) records only a failed coNP-hardness sketch, with constrained adversary transitions blocking naive succinct-graph reductions; docs/research-strategy-certificates.md; the 569-front ledger has no dedicated VERIFY-ADV-hardness question.

## falsifier

Exhibit a polynomial-time algorithm deciding VERIFY-ADV for all n and k, or an all-n family in which every adversary circuit admits a polynomial-size sorter-path witness that makes soundness checking polynomial.

## implication

coNP-completeness would be a rigorous barrier: no polynomial-time soundness check for adversary certificates unless P = coNP, sharpening the sorter/refuter verification asymmetry without implying that SORT-BOUND-U itself lies outside coNP.

## finding_unverified

ity/shortest-path in **succinct** graphs encodes an arbitrary poly-length nondeterministic computation into (state, successor-choice) with a circuit-defined transition. That route is obstructed here by the game’s fixed dynamics:

- **State/transition constraint:** states are exactly transitive closures of comparison sets on a fixed n-set; a legal move is only `P ↦ close(P ∪ {e^b})` for some pair `e` incomparable in `P` with `b = A(P,e)`. Sorter supplies existential choice of `e` among currently incomparable pairs only; `A` (fixed by the instance/reduction) supplies the orientation but cannot realize arbitrary successor posets except through this incomparable-pair + closure operator.
- **Monotonicity/path consistency:** comparabilities never disappear, states along a play form a refinement chain, and every play is consistent with at least one linear extension (no cycle can be introduced by orienting an incomparable pair). Therefore one cannot treat configurations as arbitrary bitstrings nor `A` as an arbitrary next-configuration map without a correctness-preserving gadget that simulates such computation **inside** poset-closure dynamics.
- **Consequence:** B2’s point — “constrained adversary transitions blocking naive succinct-graph reductions” — remains the operative barrier. I found no gadget/encoding yielding NP-hardness of the complement (hence no coNP-hardness of `VERIFY-ADV`), but absence of a reduction here is not a proof of easiness.

## Falsifier / complexity implication — status
- **Poly-time algorithm for all `n,k,A`:** not found (and simple local heuristics fail, §2). **All-n family making every adversary’s soundness check polynomial:** not found.
- **coNP-hard/coNP-complete for `G(n,S(n)-1)`, all large `n`:** not proved. The special case `k=S(n)-1` is a promise/restricted slice (it presupposes/targets the exact threshold) and was not separated from the general problem here.
- **Implication (conditional, as stated):** coNP-completeness of `VERIFY-ADV` would mean no poly-time soundness check for adversary certificates unless `P = coNP`, sharpening the sorter/refuter verification asymmetry (VERIFY-SORT on explicit DAGs in P vs VERIFY-ADV in coNP). It would **not** imply `SORT-BOUND-U ∉ coNP`, not imply `P ≠ coNP`, and not transfer to a separation for `S(n)`/`SORT-BOUND-U` (which remains in PSPACE per `problem.md`).

## Limits and model hygiene
- No proof of hardness, no proof of membership in P/NP∩coNP, no algorithm, and no change to any value of `S(n)` or to the status of `SORT-BOUND-U`.
- **Soundness vs completeness:** a verified winning `A` (if checkable) is a sound lower-bound/refuter certificate for `S(n)>k`; existence of such succinct `A` or a complete checkable refuter system is a separate question (open). An explicit sorter DAG verifier is sound but not complete in that format (B1).
- **No general-poset transfer:** hardness/structure results for optimization over arbitrary partial orders or arbitrary test sets do not apply to the fixed n-antichain root `G(n,k)` without a reduction respecting this model (and unary/sparse/Mahaney constraints on `SORT-BOUND-U` remain as in `problem.md`).
- **Exact next obstacle:** either (i) a genuine encoding of an NP-hard predicate into the incomparable-pair+closure dynamics yielding NP-hardness of the complement, or (ii) a structural/poly-time decision procedure (or a restricted all-n family) exploiting poset monotonicity/closure to decide `h_A(antichain_n) > k`; both remain unresolved.

## Other metadata

```json
{
  "finished_at": 1795112056.9378624,
  "started_at": 1795110785.5332174
}
```
