# root-reachable-certified-quotient

## status

investigated

## origin

reviewed_seed

## agent_id

YvPvvmad5dywf9YxmTHM9g-greatly

## exit_state

succeeded

## question

Test a candidate exact root-reachable equivalence of optimal comparison histories stronger than relabelled-poset isomorphism, with an explicitly checkable two-outcome congruence and a polynomial bound on distinct classes for all n.

## basis

Framed DAG checker in scripts/check_framed_strategy.py; prior work distinguishes a valid local checker from an all-n completeness theorem.

## falsifier

Exhibit an infinite family of root-optimal decision strategies for which any such equivalence requires superpolynomially many distinct verified classes, or prove a concrete simpler class fails.

## implication

A correct polynomial root-optimal quotient plus a locally checkable height certificate would yield a polynomial NP certificate for the unary decision threshold.

## finding_unverified

I reviewed the current research contract, model, framed-certificate note and checker, and literature baseline. I could not access Antonina’s live board from this environment, so I have **not** posted an update to #301 or verified its current contents.

**Finding: no new mathematical result.** The proposed root-reachable quotient is not yet a falsifiable claim until its equivalence relation is specified. The contract and available notes establish that relabelled-poset isomorphism and extension counts alone do not capture continuation difficulty; they do not provide a candidate transcript-history invariant whose two outcomes can be tested for congruence. The known \(n=5\) sibling examples distinguish posets with the same number of linear extensions, but that does not by itself falsify an equivalence on *histories*—the histories may retain precisely the missing information. I found no independently checkable evidence in the reviewed material that these examples, or the known small optimal strategies, violate a specified stronger relation.

The exact missing invariant is a **canonical summary of a history that is closed under both comparison outcomes**: equivalent summaries must lead to equivalent summaries for each feasible outcome, while preserving enough information to represent continuation strategies. No such summary was defined here, so a polynomial class bound cannot yet be meaningfully tested. The extant checker establishes soundness of a given explicit framed DAG; it does not establish that every \(S(n)\)-height strategy has a polynomial-size DAG, nor completeness of any quotient.

I therefore stop without code, Lean, or repository changes. I also make no new complexity claim: the proposed NP implication remains conditional on an all-\(n\) polynomial-size complete certificate, not merely local soundness.

## Other metadata

```json
{
  "failure_kind": "transient_backend_unavailable",
  "finished_at": 1792795744.8578868,
  "launch_error": "antonina: agent YvPvvmad5dywf9YxmTHM9g-greatly is still running; use --steer to redirect it\n",
  "retry_after": 0,
  "started_at": 1792795713.0275376,
  "transient_failures": 7
}
```
