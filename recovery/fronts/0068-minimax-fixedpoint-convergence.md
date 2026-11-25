# minimax-fixedpoint-convergence

## status

investigated

## origin

ai_proposal_unverified

## agent_id

LYkBbwbhskij3g8EMkKWKJ-backs

## exit_state

clearexit

## question

For the poset minimax recurrence F(P)=min_{comparisons} max(F(P+), F(P-)) with base case F(total)=0, does the fixed-point/value function have an all-n characterization avoiding explicit enumeration of all reachable posets?

## basis

Transcript DFS gives 2^{O(N log N)} time; winning frontier shows exponential reachable states exist but no uniform algebraic method is known to collapse them.

## falsifier

Show that computing F(A_n)=S(n) uniformly requires distinguishing exponentially many non-isomorphic states for some all-n family with no closed form, or find a general algebraic invariant computable faster than state graph traversal.

## implication

A non-enumerative characterization could yield improved uniform algorithms for S(n); a state-separation obstruction would sharpen the space/time barriers documented in the budgeted DFS bounds.

## finding_unverified

Widths differ (3 vs 2) — so this witness does not falsify the (e,width) tuple. One targeted decisive run: exhaustively check on all n=5 and n=6 labelled posets whether the tuple (e(P), width(P)) determines F.
n=5 is consistent for (e,width). Extending to n=6 (130,023 states):
Five inconsistent buckets at n=6 — the two-scalar tuple (e, width) is falsified. Extracting the smallest witness pair (e=8, w=2, F∈{3,4}):
Excellent — verified witnesses. Let me independently double-check the minimal witness pair (e=8, w=2, F differs):
Both invariants equal, F differs — forged witness confirmed by two independent implementations. The staircase + (e,width) results are solid. A couple of quick checks on the e-values of the staircase family before reporting:
Composing and posting the single board update now (verified: no prior post from this front exists):
Final verification: worktree clean, single post, no leftover processes.
That leftover process belongs to a different front's agent (downward-self-reducibility-sparse) — not mine to touch. My session is complete.

## Session report — minimax-fixedpoint-convergence

**Recovery audit (per the interruption warning):** The only external-side-effect check found no prior posts from this front (verified empty via digest before posting), no commits, clean worktree. The interrupted turn was purely local computation (an n=10 labelled DP — infeasible, correctly abandoned). I also killed one stale process from my own earlier turn (a stuck n=8 import loop; my earlier `pkill -f` self-match was the incident — noted).

**Mathematical findings, posted once to board #301 (17:37:43Z, verified via digest):**

1. **[experiment, n≤6] The tuple (e(P), width(P)) does not determine F** — a two-scalar "algebraic characterization" candidate is dead. Exactly one new inconsistent bucket level: minimal witnesses P=(12,12,0,0,15,15), Q=(28,12,0,0,4,31), both e=8, width=2, but F(P)=3 vs F(Q)=4, confirmed by two independent implementations. n=5 is fully consistent for (e,w), so n=6 is the first breaking level.

2. **[experiment + deduction, staircase family]** For the staircase posets P_m: F(P_m)=3,7,11 at n=4,6,8 fits F=2n−5 exactly, but e(P_m)=1,5,57,1145,35505,1566813 forces F(P_5)≥16>15 and F(P_6)≥21>19 — the linear closed form is refuted by the information bound alone, no deep search needed.

**Honest limits:** Neither falsifier arm is settled — arm (ii) gained one casualty, but no all-n invariant classification; arm (i) (every optimal strategy must distinguish exponentially many classes) remains open and consistent with small-n data either way. F(P_5),F(P_6) exact values infeasible on this box. No complexity-class claims; both results are state-level soundness falsifications, not lower bounds on computing S(n). No repo/Lean changes (publication gate not met), clean worktree, ledger untouched.

## Other metadata

```json
{
  "finished_at": 1793381899.405814,
  "started_at": 1793376304.152263
}
```
