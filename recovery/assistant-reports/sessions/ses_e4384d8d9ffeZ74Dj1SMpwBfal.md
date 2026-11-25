# antonina-6i8KtoCkUm8jQIEKUdMJH0-prove

Session: ses_e4384d8d9ffeZ74Dj1SMpwBfal
Workspace: /home/lubko/soring-fronts/tropical-circuit-sortnumber
Created: 1794163550116; updated: 1794164322403

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 27 (msg_1bc7b45fb001gfv9aVyNi75MPZ)

I'll start by inspecting the repository state, docs, and any durable records of prior work before doing anything external.

## Output 148 (msg_1bc7ed6760018eNPAfMHWuvaLK)

No prior tropical post or repository work exists; the front is only `running`. I'll now do the mathematical analysis and check the primary literature on tropical/min-max-plus circuits.

## Output 314 (msg_1bc83e484001jTu86a2rVrcaZY)

The mathematical picture is now clear. Let me record the result in a temp file and post it once to board #301, after confirming no duplicate exists.

## Output 356 (msg_1bc852cc3001MbySNnGapyuzLE)

## Prior-side-effect audit

I inspected the worktree, Git state, the frontier ledger, the Antonina agent record, and board #301 before acting.

- The tropical front was `running` under this agent, but its log contained no earlier mathematical work and no earlier board post.
- `board_digest --contains "tropical"` and `--contains "addition chain"` returned no matches. There was no duplicate to avoid.
- The worktree was clean before and after; I made no repository or Lean changes.
- I posted exactly one update to #301 at `2026-11-08T18:56:26Z`, author `SoringP1 frontier: tropical-circuit-sortnumber`.

## Mathematical finding

Under the standard tropical circuit model (Jukna, *Lower Bounds for Tropical Circuits and Dynamic Programs*, ToC **57** (2015), §5: fanin-2 `min`/`max`/`+` gates, constants 0 and 1), the stated super-polynomial lower-bound branch is **false nonuniformly**.

Let \(\ell(m)\) be the addition-chain length of \(m\), i.e. the minimum number of `+` gates needed to produce \(m\) from 1. For the unary input \(1^n\), every input variable has value 1, so a tropical circuit evaluates to a constant expression. Then:

\[
\text{minimum tropical circuit size for }S(n)\text{ on }1^n=\ell(S(n)).
\]

Why: `min`/`max` only select an already-produced value and never create a new magnitude; only `+` creates new values. An addition chain is exactly the `+`-only special case.

Since \(S(n)=\Theta(n\log n)\),

\[
\lceil \log_2 S(n)\rceil
\le \ell(S(n))
\le \log_2 S(n)+\operatorname{popcount}(S(n))-1
\le 2\log_2 S(n),
\]

so

\[
\ell(S(n))=\Theta(\log n).
\]

Therefore **for every \(n\) there is a tropical circuit of size \(O(\log n)\)**. No \(2^{\Omega(n)}\) lower bound for unrestricted tropical circuits can hold. If arbitrary integer constants are allowed as gates, the size is 1; the standard 0/1-constant model is what makes the question non-vacuous.

## Verification through \(n=22\)

Using the exact values \(S(0),\dots,S(22)\) from OEIS A036604 and iterative-deepening search for minimal addition chains, I obtained

\[
\ell(S(n))_{n=0}^{22}
=0,0,0,2,3,4,4,5,4,6,6,6,6,6,7,7,7,7,7,8,8,7,9.
\]

The maximum is 9, at \(S(22)=71\), with the explicit chain

\[
1,2,4,8,16,32,64,68,70,71.
\]

Thus the falsifier's “every tropical circuit has size \(2^{\Omega(n)}\)” branch fails on an explicit all-\(n\) family of tiny circuits.

## The precise obstruction

The only non-trivial version of the front is the **DLOGTIME-uniform** one.

- A DLOGTIME-uniform polynomial-size family would indeed put \(S_{\text{unary}}\in FP\), by evaluating the circuit.
- The nonuniform \(\Theta(\log n)\) circuits give **no algorithm**, because constructing the chain requires knowing \(S(n)\).
- A uniform \(O(\log n)\)-size family would amount to a DLOGTIME-computable addition chain for \(S(n)\). The minimax recurrence supplies no such chain.
- The exponentially large minimax straight-line program is **not** a lower bound: it is one particular expression, and as a constant expression it collapses to \(\ell(S(n))\) gates.

So the front's dichotomy is not a genuine tropical-circuit dichotomy: one side is false nonuniformly, and the other side is a uniformity/description-complexity question about \(S(n)\), not a min/max/+ algebraic lower bound.

## General posets and soundness/completeness

Jukna-style tropical lower bounds apply to **functions of free input weights** (permanent, spanning tree, APSP, etc.), proved for all assignments. Here \(S(n)=F(\text{antichain}_n)\) is a **single evaluation** at fixed constants. A lower bound for the general-poset minimax \(F(P)\) does not transfer to the antichain root.

Similarly, a supplied tropical circuit is a sound, polynomial-time-checkable value certificate. But the existence of a small **uniform** family—the completeness direction—is exactly what is missing. The nonuniform addition chains are not such a certificate.

## Honest limits

- I did not construct a DLOGTIME-uniform polynomial-size tropical circuit.
- I did not prove an unconditional super-polynomial lower bound for DLOGTIME-uniform tropical circuits.
- I did prove that the stated \(2^{\Omega(n)}\) falsifier is impossible under the standard nonuniform model, with an exact \(\Theta(\log n)\) characterization.
- The productive reformulation is either (i) target \(F(P)\) as a function of posets/weights, or (ii) prove a uniformity lower bound for the addition-chain description of \(S(n)\). Neither is the original unary-\(S(n)\) tropical circuit question as posed.

No Lean or repository changes were made.

## Output 389 (msg_1bc869406001fJnCoYERleWOGQ)

I’ll re-check the durable state to confirm the earlier post exists exactly once and that no unfinished side effect remains. I will not repost.

## Output 408 (msg_1bc86b7a2001ttmVm16Zo0OGAu)

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
