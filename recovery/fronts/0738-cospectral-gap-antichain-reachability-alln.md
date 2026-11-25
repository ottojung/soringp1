# cospectral-gap-antichain-reachability-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

EG3MKFfW4sNqMVkL2sx1wU-cooper

## exit_state

clearexit

## question

Can any member of an (e,M1)-cospectral, F-different poset family with unbounded F-gap (the board's 23:01Z ordinal-power construction) be realized up to isomorphism as a state reachable from the n-antichain along a height-S(n) optimal play, for some all-n family of sizes; equivalently, does the one-step extension-count invariant M1 fail to determine the exact minimax cost already on the optimal-play-reachable domain rather than only on arbitrary posets?

## basis

Board #301 23:01Z/23:05Z reports the M1-cospectral F-gap unbounded (gap k at size 7k) with no transfer to A_n. An out-of-repo scratch computation (not kernel-checked) reproduces e=32 and F=5/6 for the n=7 seed and finds covers=10 > S(7)-F (8 and 7), so the seed is window-excluded, while the ordinal square has covers=24 <= S(14)-F=28 and is not; docs/research-plan.md states the reachability window.

## falsifier

Establish a reachability invariant, for instance a cover-count or width bound stronger than covers(P) <= d <= S(n)-max(F(P),pi(P)), that excludes every cospectral F-different poset of such a family at every n; or exhibit one lying on a height-S(n) path at some n.

## implication

A positive answer would rule out any certificate scheme tracking only (e,M1), even to O(1) additive accuracy, on the domain actually relevant to S(n) and sharpen the certificate barrier; a negative answer isolates a reachability invariant under which those statistics remain sound.

## finding_unverified

k=1 instance** of optimal-play reachability by a simple cover-count window invariant: `cov(P)=10 > S(7)-F(P)=8` and `cov(Q)=10 > S(7)-F(Q)=7`. [deduction]
- I **did not** exclude `k>=2`; the same cover-count invariant becomes too weak (superlinear S(7k) vs linear 14k-4).
- I **did not** exhibit any `P_k/Q_k`, `k>=2`, on a height-`S(7k)` optimal play. The decisive F-tight backward reachability test for P^2 was computationally infeasible with the naive F-memoized DFS.
- **Complexity implication remains conditional**: a positive witness would rule out (e,M1)-only certificates, even O(1)-additive, on the optimal-play-reachable domain; a negative all-k exclusion would isolate a stronger reachability invariant under which M1 remains sound. Neither is established.

## Failed approaches / obstructions

1. **Naive backward F-tight DFS from P^2**: infeasible because exact F computation is memoized over the explored subgame and explodes as F increases (1.5M fstates at F=13 after 4 nodes). Needs either a much stronger F oracle, a symbolic/structural reachability argument, or meet-in-middle with tight bounds. [experiment]
2. **Simple counting invariants** (covers, width, Max/Min, cross-comparison count): all linear/constant and dominated by superlinear S(7k) for k>=2. [deduction]
3. **Non-F-tight construction**: reaching P^2 in 24 comparisons gives a 34-comparison line, not a height-S(14)=38 optimal-play witness; it cannot certify optimal-play reachability. [deduction]

## Limits / next decisive step

The natural next falsifiable step is a **structural F-tight reachability invariant for ordinal-sum normal forms**: either prove that any F-tight optimal-play path reaching an ordinal sum A(+)B must pass through (or be reducible to) block-wise F-tight plays, giving an inductive obstruction for P^k/Q^k; or find an explicit F-tight path for P^2 by a constrained backward search that avoids full F recomputation (e.g. certify F(R0)=F(R)+1 by local witness/sibling bounds, or use SAT/IDA* over the narrow cover-removal frontier). I did not complete that step.
No unfinished external actions to repeat. I inspected the state: `billy-dev`, clean worktree on `billy-dev...origin/billy-dev`, no repo/Lean/test/CI/ledger changes, no #301 post made, and scratch work only in `/tmp/opencode/cg_reach_task/`.

The front remains **OPEN**. My completed finding:

- **Derived invariant [deduction]**: `cov(P) <= d` for any state reachable in `d` comparisons from `A_n`, since only the directly added comparison can become a new Hasse cover. Thus optimal-play reachability requires `cov(P) <= S(n)-F(P)`.
- **Applied to the gapspan ordinal-power family [deduction + small experiment]**: for `P_k=P(+)^k P`, `Q_k` on `n=7k`, `cov=14k-4`, `F(P_k)=5k, F(Q_k)=6k`. The cover window excludes `k=1` (`10 > S(7)-F`, S(7)=13 literature) but does **not** exclude `k>=2` because `S(7k)=Omega(k log k)` dominates linear `14k-4`.
- **Not settled**: I found no stronger excluding reachability invariant and no explicit `k>=2` member on a height-`S(7k)` optimal play. A naive backward F-tight DFS for `P^2` (n=14, F=10) was computationally obstructed by F-valuation explosion (1.5M fstates at F=13 after 4 nodes), so no reachability certificate either way.
- **Complexity implication**: remains conditional; a positive witness would rule out (e,M1)-only O(1)-additive certificates on the optimal-play-reachable domain, a negative all-k exclusion would isolate a stronger reachability invariant. Neither established.

## Other metadata

```json
{
  "finished_at": 1795480413.3148427,
  "started_at": 1795477871.390199
}
```
