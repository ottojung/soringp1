# reachable-profile-depth-growth-certificate-barrier-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

MdwjgGZ16kDbrxwxmkAbXL-laminated

## exit_state

clearexit

## question

For antichain-reachable height-S(n) optimal-play states, let t(n) be the least profile depth at which the extension-count invariant M_t determines the exact minimax cost F on all such states of size at most n. Does t(n) stay bounded by a constant for all n, or must it grow without bound, and if it grows does that exclude every fixed-depth local-invariant certificate for SORT-BOUND-U?

## basis

From-scratch recomputation reproduces the seed pair e=32, F=5/6, equal M1 but unequal M2, and ordinal-square M1/F-gap preservation; board #301 reports zero (e,M1,M2) conflicts over all 16999 iso-classes at n=8, while counting e is #P-hard, so completeness alone yields no algorithm.

## falsifier

Exhibit a constant C with M_C determining F on every antichain-reachable optimal state at every n (bounded case), or exhibit arbitrarily large n with two such states sharing M_C but differing in F (unbounded case, refuting any fixed-depth certificate family).

## implication

A bounded t(n) keeps fixed-depth local invariants alive as a route to NP/coNP membership for SORT-BOUND-U; unbounded t(n) is a barrier excluding that whole certificate family and separates structural invariant-completeness from polynomial-time checkability.

## finding_unverified

 it appears on the board and that my worktree is still clean.
Done. Here is the honest outcome.

## What I did

Worked only on `billy-dev`, clean worktree throughout (`git status` empty, HEAD `6a96398`), no Lean/test/CI/ledger/repo changes. One board post to #301. All code is scratch under `/tmp/opencode/rpdg_task`.

I attacked the front's all‑n claim in **both** directions: bounded `t(n)` (some constant C with M_C determining F on antichain‑reachable optimal states) versus unbounded `t(n)` (arbitrarily large n with equal‑M_C, different‑F optimal states).

## Mathematical finding [experiment], restricted class

I built a from‑scratch engine (own closure, downset‑DP extension count, child enumeration, memoised minimax F) and reproduced the seed pair exactly: e=32, equal M1, F(P)=5 / F(Q)=6, M2 unequal.

Full **forward** enumeration of every F‑tight reachable optimal state from A_n gives counts 3, 19, 181, 2251, 73051, 3,031,407 for n=2…7. In that class:

- **e alone does not determine F** (8 equal‑e groups with F‑gaps at n=6; 18 at n=7).
- **M1 determines F with zero collisions** at n=6 and n=7 (M2, a refinement, also does). Since M1 recovers e and the sibling pairing, this was checked within equal‑e groups.

So the bounded reading `t=1` survives the strongest feasible test; the unbounded‑barrier reading is **not** established. Directly, neither seed state is a member of the 3,031,407 reachable optimal states at n=7, so the general‑poset M1‑cospectral unbounded F‑gap family (this seed and its ordinal squares) does **not** transfer to the front's class. [deduction]

## Concrete failed approaches and exact obstructions

1. The tempting counting prune "an F‑tight child at depth d has e ≥ n!/2^d" is **false**: when both outcomes are tight the adversary can steer to the smaller‑e child. It discarded 34,260 genuine n=6 states, so counting cannot exclude general‑poset gaps on optimal states.
2. M1's determination of F is **not** the one‑ply bound L1 (which is M1‑computable): L1 < F on 2,280 reachable optimal states at n=6. It uses the full sibling‑pair multiset, not a simple potential.
3. My first reverse‑reachability parent generator (cover removal only) was **incomplete** — brute force shows a reachable F=1 state has parents with F ∈ {2,3,4,5}, not just cover‑removal F=2 — so I **withdrew** any claim about the prior n=8 (e,M1) witnesses' optimal‑play status. Forward n=8 enumeration is infeasible (A001035(8)=431,723,379 labelled posets).

## Soundness vs completeness vs checkability [deduction]

- **Soundness** (M1 recovers sibling pairs; F determined given child F‑values) was never in doubt and is unchanged.
- **Completeness** (t=1 on optimal states through n=7) is a structural observation on a restricted class, not an all‑n theorem.
- **Checkability**: e and M1 are #P‑hard, so even a proved bounded t gives only necessary conditions — not polynomial‑time checkability, hence not NP/coNP membership. Conversely, unbounded t would exclude only the fixed‑depth M_t‑invariant family, not every certificate. The front's two‑sided complexity implication is unsubstantiated in both directions.

## Honest limits

The all‑n question remains **open**: no proof of bounded t(n), no counterexample to it; n ≥ 8 untested (my witness sub‑claim was withdrawn). This is a general‑poset/restricted‑class result only — no S(n) value, no bound, no class placement. S(n) and SORT‑BOUND‑U remain open. I did not confuse a passing computation or a posted result with a proof.

## Other metadata

```json
{
  "finished_at": 1795477652.5125241,
  "started_at": 1795475588.8171606
}
```
