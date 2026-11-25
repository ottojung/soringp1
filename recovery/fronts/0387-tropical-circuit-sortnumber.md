# tropical-circuit-sortnumber

## status

investigated

## origin

ai_proposal_unverified

## agent_id

6i8KtoCkUm8jQIEKUdMJH0-prove

## exit_state

clearexit

## question

Does the exact sorting number S(n) admit a DLOGTIME-uniform tropical (min,max,+) circuit family of polynomial size in the unary input length n, giving a polynomial-time evaluator, or does every such tropical circuit family require super-polynomial size for infinitely many n?

## basis

The minimax recurrence in docs/upper-bound.md is a min/max/+ straight-line program over exponentially many poset states; docs/problem.md equates SORT-BOUND-U with FP; this model is distinct from the already investigated determinant, LP, and Lasserre relaxations.

## falsifier

Exhibit an all-n family of unary inputs on which every tropical circuit computing S(n) has size 2^{Omega(n)}, or construct a polynomial-size uniform tropical circuit and check it against the exact values through n=22.

## implication

A uniform polynomial-size tropical circuit would put S_unary in FP and SORT-BOUND-U in P without exhibiting an explicit optimal sorting tree; a super-polynomial lower bound would rule out the whole min/max/+ compression route while leaving general FP open.

## finding_unverified

exity question about \(S(n)\), not a min/max/+ algebraic lower bound.

## General posets and soundness/completeness

Jukna-style tropical lower bounds apply to **functions of free input weights** (permanent, spanning tree, APSP, etc.), proved for all assignments. Here \(S(n)=F(\text{antichain}_n)\) is a **single evaluation** at fixed constants. A lower bound for the general-poset minimax \(F(P)\) does not transfer to the antichain root.

Similarly, a supplied tropical circuit is a sound, polynomial-time-checkable value certificate. But the existence of a small **uniform** family—the completeness direction—is exactly what is missing. The nonuniform addition chains are not such a certificate.

## Honest limits

- I did not construct a DLOGTIME-uniform polynomial-size tropical circuit.
- I did not prove an unconditional super-polynomial lower bound for DLOGTIME-uniform tropical circuits.
- I did prove that the stated \(2^{\Omega(n)}\) falsifier is impossible under the standard nonuniform model, with an exact \(\Theta(\log n)\) characterization.
- The productive reformulation is either (i) target \(F(P)\) as a function of posets/weights, or (ii) prove a uniformity lower bound for the addition-chain description of \(S(n)\). Neither is the original unary-\(S(n)\) tropical circuit question as posed.

No Lean or repository changes were made.
I’ll re-check the durable state to confirm the earlier post exists exactly once and that no unfinished side effect remains. I will not repost.
Audit complete. No new external action taken, and no duplicate post was made.

## What actually happened

- **Board #301:** exactly one post exists for this front, at `2026-11-08T18:56:26.777Z`, author `SoringP1 frontier: tropical-circuit-sortnumber`. The filter `--contains "nonuniform tropical size"` returns `1 unique match`.
- **Git:** worktree is clean on `billy-dev`; no commits or repository changes were made.
- **Durable ledger:** the `tropical-circuit-sortnumber` entry still shows `status: running`, `finished_at: null`, `finding_unverified: null`.
- **Agent record:** state is still `running` with `error: recovering from unrecognized_backend_failure; ... failed attempts=7`.

So the mathematical work and the single board report are already durable. The remaining `running` state is an administrative/process transition, not an unfinished research effect. Manually editing the ledger or reposting would risk exactly the duplication the recovery notice warns against.

## Research result already recorded

The post reports the substantive finding:

- Under the standard 0/1-constant tropical model, the nonuniform circuit size for \(S(n)\) on \(1^n\) is exactly the addition-chain length \(\ell(S(n))\).
- Since \(S(n)=\Theta(n\log n)\), this is \(\Theta(\log n)\).
- Therefore the falsifier’s claim that “every tropical circuit requires size \(2^{\Omega(n)}\)” is false nonuniformly, with explicit chains through \(n=22\).
- The surviving question is DLOGTIME uniformity: a uniform polynomial-size family would imply \(S_{\text{unary}}\in FP\), but no such family was constructed.
- General-poset tropical lower bounds do not transfer to the single antichain-root evaluation, and circuit soundness does not supply the missing uniform completeness theorem.

No further research or repository action is warranted. If the keeper does not transition the front out of `running` after recovery, that stale state should be reviewed by the operator rather than fixed by reposting the same result.

## Other metadata

```json
{
  "finished_at": 1794164332.1956713,
  "started_at": 1794163549.5716236
}
```
