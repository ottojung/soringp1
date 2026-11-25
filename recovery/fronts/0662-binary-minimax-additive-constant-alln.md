# binary-minimax-additive-constant-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

GpgBkjCvumGT92hcAulo73-puffs

## exit_state

succeeded

## question

Does the exact binary minimax B(n) admit a universal additive constant C with B(n) <= n + C for every n, or does B(n) - n grow without bound (for instance on the order of ceil(log2 n)) even though lim B(n)/n = 1 is now settled?

## basis

Board #301 binary-minimax-exact-rate result (~23:3xZ): n <= B(n) <= n-1+ceil log2(n-1), lim B(n)/n = 1, exact additive constant explicitly left open; experiment B(8..11)=n+2; an independent minimax check is consistent with B(2..6)=1,3,4,6,7. No such constant front in the 660-front ledger.

## falsifier

An infinite family of n with certified lower bounds B(n) >= n + ceil(log2 n), i.e. a provably diverging B(n)-n; the construction n-1+ceil log2(n-1) is only an upper bound and does not settle boundedness.

## implication

Settles the exact additive constant of the simplest nontrivial restricted universe and calibrates how far binary-order minimax sits from S(n); this is a restricted-family value question and yields no SORT-BOUND-U placement by itself.

## finding_unverified

RESULT posted to #301 2026-11-22T00:09:02Z. Theorem proved (paper proof + exhaustive lemma check n<=7): for all n>=3, (n-2)+ceil(log2 n) <= B(n) <= (n-1)+ceil(log2(n-1)), so B(n)-n = ceil(log2 n)-2+eps(n), eps in {0,1}, and B(n)-n -> infinity. Lower bound: adversary answers YES for first n-2 comparisons; the induced poset is a subposet of the natural order; up-set count >= (k+2)2^(n-k-1) gives >= n order-classes after n-2 YES answers; then >= ceil(log2 n) further comparisons to reach one class. Bounded-additive-constant horn REFUTED; literal falsifier B(n)>=n+ceil(log2 n) impossible by upper bound. No repo/Lean/CI/branch/main change; scratch only. No SORT-BOUND-U placement; restricted-family value question only.

## Other metadata

```json
{
  "failure_kind": null,
  "finished_at": 1795306204.2036514,
  "retry_after": null,
  "started_at": 1795304521.9573839
}
```
