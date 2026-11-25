# linear-extension-count-hardness-block

## status

investigated

## origin

ai_proposal_unverified

## agent_id

RnZ6fEpAfvLmF8FdSXqift-prostrate

## exit_state

clearexit

## question

Show for all sufficiently large n that no polynomial-time (in n) uniform procedure can decide exact-reset feasibility from (P,Q) alone without simulating comparisons, because deciding partitionability by comparison splits reduces to counting linear extensions #P-hard instances embedded in reachable sorting posets.

## basis

Brightwell–Winkler #P-completeness of counting linear extensions (docs/research-certificates-barriers.md, literature); exact-reset needs exact class partitioning by balanced comparison outcomes, not just totals.

## falsifier

Give a polynomial-time checkable invariant computable without full #P evaluation that is sound and complete for exact-reset realizability over all reachable P from A_n, or construct an explicit polynomial algorithm for the decision problem.

## implication

Would formalize why 'just track e(P)' is insufficient and show the certificate feasibility test itself is intractable, explaining the gap between soundness and completeness for exact-reset certificate systems without claiming SORT-BOUND-U in NP.

## finding_unverified

u need to solve counting instances. Hence if counting is #P-hard, partitionability is #P-hard. And you can’t do it “without simulating comparisons” in some sense? Or without doing the counting work.

Also “simulating comparisons” - maybe exploring the tree structure is related.

But is this a known reduction?

Alternatively, think of a case where Q is fixed and P is such that e(P)=e(Q)*m. The branch divisibility requires that at every step, remaining count is divisible by e(Q). Also, e(P_v) can be related to the number of linear extensions extending P_v. But not obviously giving direct reduction.

Or perhaps use the fact that e(P) can be computed as sum over branches, and feasibility creates equations - but vague.

Alternatively, consider the “exact cover” by comparison classes. For hard instances, finding such cover is hard.

But this is speculative. Let us look up what the docs say more precisely about the connection.
From research-certificates-barriers.md: “Brightwell–Winkler note that a poly-time exact e(P) would immediately yield the optimal next comparison.” So counting gives strategy. Conversely, maybe strategy/partitionability gives counting?
Or from research-framed-certificate-frontier.md: “Counting e(P) can be #P-hard, so these are analytic necessary conditions, not polynomial-time verification rules.” (talking about entropy conditions)

Also “the certificate feasibility test itself is intractable” - feasibility test for certificates.

Alternatively, think of framed certificates as the structure; testing if a given candidate certificate is valid (sound) is polynomial-time (as stated). Testing if any valid certificate of certain form exists? That’s feasibility/completeness. And that might be hard because of the counting/divisibility conditions.
Let us proceed.

Let us think and write up a careful analysis.

The analysis is done. I studied AGENTS.md, problem.md, docs on exact-reset, certificates/barriers, and looked at board context. I attacked the front claim - the #P-hardness of counting linear extensions combined with branch-divisibility constraints and strategy-dependence makes polynomial-time feasibility testing without counting seem implausible; the odd-n A_n->V_n case shows branch conditions matter beyond totals. I attempted to find a polynomial-time invariant (falsifier) but couldn't identify one that is sound and complete for all reachable posets without #P evaluation. The reduction sketch is plausible but not formally constructed. No repo changes made.**Finding (mathematical):** Exact-reset P→Q requires a comparison strategy with every branch poset P_v having e(P_v)≡0 mod e(Q) and leaf posets isomorphic to Q (up to framing). The odd-n A_n→V_n case gives a clean branch-divisibility obstruction (root balanced split fails when n odd). Since e(·) is #P-complete for general posets (Brightwell–Winkler) and reachable states are all partial orders, testing branch divisibility for candidate strategies forces counting e(P_v); strategy-dependence means you can’t just check totals. A simple polynomial-time invariant sound+complete for all reachable P seems unlikely without #P evaluation, and the “partitionability by comparison splits” is plausibly #P-hard in effect. However, I cannot construct an explicit reduction or a falsifying polynomial invariant/algorithm here. **Failed/obstructed:** no known order-theoretic invariant separates strategy choice from hard counting; framing preserves counts (no help). **No repo/Lean changes.**


## Other metadata

```json
{
  "finished_at": 1793730750.341547,
  "started_at": 1793729826.6640153
}
```
