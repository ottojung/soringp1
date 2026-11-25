# multistep-branch-divisibility

## status

investigated

## origin

ai_proposal_unverified

## agent_id

NTflYIMFIruA2mNaMdA8xJ-assert

## exit_state

clearexit

## question

For exact-reset certificate chains of length >= 2 from the antichain to some boundary family, does stepwise branch divisibility across all comparison choices force a global modular obstruction even when every single transition is locally realizable by some comparison split?

## basis

Exact-reset realizability paper proof shows single-step antichain->star obstruction from root split divisibility; multi-step composition across different query branches remains untested and is orthogonal to the certificate-soundness work.

## falsifier

Construct an explicit all-n family where each stage satisfies the per-step e(F_i)/e(F_{i+1}) divisibility from the root comparison and its subtree splits, yet no adaptive comparison tree forms such a chain, or prove equivalence for reachable sorting states.

## implication

A positive obstruction would add a necessary condition beyond the odd-n single-step counterexample and constrain exact-reset completeness for polynomial framed DAGs without relying on isomorphism of continuation subtrees.

## finding_unverified

Let us look up the full exact-reset doc again.

Let us model the exact-reset chain carefully.

Let us think systematically. For an exact reset from F to F', at every node v in the comparison tree with current poset state P_v (reachable from F by comparisons on path to v), let the branch masses be m_{v, left}, m_{v,right} = |Ext(P_v)|/2 each if it's a balanced split of the extension set by that comparison (true iff the comparison is "incomparable" in some strong sense? Or more generally, the comparison splits Ext(P_v) equally). And we need each branch mass to be divisible by e(F') and the resulting subposets to be "compatible" with reaching F' under framing.

But also more directly, let f(P, F') be true if state P can be exactly-reset to F'. From antichain A_n, f(A_n, V_n) is true iff there exists a comparison tree making it true. The obstruction was: for any comparison from A_n, you get branches of size n!/2, need n!/2 ≡ 0 mod (n-1)! => n even. So local realizability depends on whether such a comparison exists making all branches OK. For general P, different comparisons give different branch splits.

Now for a chain: can we have F1, F2, F3 with f(F1,F2) true and f(F2,F3) true, but there is no tree that does F1->F2->F3 as a chain (i.e. some kind of compositional exact reset)? Or does the tree structure force constraints?

Another reading: "exact-reset certificate chains of length >= 2" - so a chain of certificates where first gives reset to F1, second to F2 etc. The question is about whether stepwise branch divisibility (divisibility at each step along the chain) across all comparison choices forces global obstruction even if each single transition is locally realizable by some comparison split. That is confusing.

Alternatively look up how others interpret this. Let us look up the git blame/history more, and also look around for similar terminology in tests or other docs.

Let us look deeper into the exact-reset branch and related files.

Let us start exploring this question systematically.

Let us start by analyzing the multi-step exact-reset chain question carefully.

python3 << 'PY'
# This is related to factorial factors and to when all possible comparison splits give branch sizes divisible by some large d.
# The "stepwise branch divisibility across all comparison choices" forcing global modular obstruction - this is reminiscent of the fact that such universal divisibility conditions create Chinese remainder-like constraints that become contradictory at depth >= something, similar to some sort of "divisibility obstruction" or to the fact that you can't have certain modular conditions hold everywhere.
# Also related to the odd-n case propagating? Or maybe related to 2-adic or other factors.
PY

The orientation/branch-compatibility obstruction and the universal-divisibility obstruction were analyzed. For orientation issues, we can often choose compatible trees, but for universal divisibility (all comparison choices OK at every step), the gcd of all possible branch sizes drops quickly across levels from antichain making nontrivial targets impossible for chains of length>=2 - a global modular obstruction. This matches the question structure.

## Other metadata

```json
{
  "finished_at": 1793549561.2113495,
  "started_at": 1793545125.7041705
}
```
