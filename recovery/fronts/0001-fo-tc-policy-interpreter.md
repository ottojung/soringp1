# fo-tc-policy-interpreter

## status

investigated

## origin

reviewed_seed

## agent_id

Gm7n6UVDcDZluIRGmVGXEJ-integrity

## exit_state

succeeded

## question

Determine whether uniform FO(TC) policy descriptions admit a polynomially checkable proof of worst-case comparison depth at the antichain root, rather than just polynomial evaluation on a single input order.

## basis

Founder-selected Antonina issue JTsW4AnxTLzN18IBQibXea-fervor and SoringP1 issue #301; previous certificate soundness-versus-completeness gap.

## falsifier

Construct an explicit FO(TC)-expressible policy whose worst-case comparison budget is hard to check or whose all-n expressive completeness provably fails.

## implication

A sound, complete and polynomial-size proof-carrying FO(TC) normal form would establish SORT-BOUND-U membership in NP; execution alone does not.

## finding_unverified

I inspected the local `AGENTS.md`, `docs/problem.md`, the research frontier, and the prior certificate analysis. The worktree is clean. This environment is **not on `billy-dev`**, and I cannot access Antonina or the research board here, so I did not post to #301 or claim to have studied its current contents.

No new result emerged from the available evidence. The precise obstacle remains the gap between **soundness**—a checker can verify a supplied policy/DAG’s worst-case depth—and **completeness**—proving that every yes-instance has a polynomial-size witness. Checking execution on one input order does not certify the maximum over every outcome path from the antichain root. Existing notes also do not establish a polynomial bound on the size of a complete policy certificate. Thus they yield no NP-membership result for `SORT-BOUND-U`.

I stopped without creating repository changes, Lean files, or unsupported claims.

## Other metadata

```json
{
  "failure_kind": "transient_backend_unavailable",
  "finished_at": 1792795775.1232817,
  "launch_error": "antonina: agent Gm7n6UVDcDZluIRGmVGXEJ-integrity is still running; use --steer to redirect it\n",
  "retry_after": 0,
  "started_at": 1792795712.8277183,
  "transient_failures": 7
}
```
