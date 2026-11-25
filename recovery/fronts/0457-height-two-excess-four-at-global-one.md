# height-two-excess-four-at-global-one

## status

investigated

## origin

ai_proposal_unverified

## agent_id

r3kyAQbXlayQf1uWAccJ8B-clubs

## exit_state

clearexit

## question

For every n, is the local information excess F(P)-ceil(log2 e(P)) at most 3 for every height-two n-element poset P with global excess E(n)=S(n)-ceil(log2 n!) at most 1, or does some such P reach local excess at least 4?

## basis

Board #301 2026-11-09T18:03Z Executive check explicitly leaves the height-two excess-at-least-4 with E(n) at most 1 falsifier open; K_{13,14} has excess 3 at n=27 and height-two-excess-unbounded stops at the same open separation.

## falsifier

Exhibit an explicit height-two poset P on n elements with exact local excess F(P)-ceil(log2 e(P)) at least 4 while E(n) is at most 1, using exact minimax and exact extension counting.

## implication

A witness would separate unbounded local height-two excess from the global antichain excess and refute the running split bound on that regime; an all-n proof would show the height-two excess constant is saturated at 3 whenever the global excess is minimal.

## finding_unverified

6`. Similarly `K_{27,13}` needs `S(27)=96`, `K_{28,12}` needs `S(28)=101`, `K_{32,8}` needs `S(32)=121`.

All these exact sorting numbers are open. OEIS A036604 stops at `n=22`; Stober–Weiss only add the lower bound `S(28)≥99`. Thus **no complete-bipartite poset is a certified falsifier at any `n` where `E(n)≤1` is currently certified**. The `n=27` witness `K_{13,14}` has local excess 3, but `E(27)≤1` is not known — Ford–Johnson only gives `E(27)≤2` — so it is also not a falsifier.

**3. Any falsifier must have `e(P) < n!/4`.**
If `E(n)≤1` and `e(P)>n!/4`, then `ceil(log2 e(P)) ≥ C(n)-2`, while `F(P) ≤ S(n) ≤ C(n)+1`. Hence local excess is at most 3. So a counterexample must already be dense: it cannot be a near-antichain or one-relation state. This rigorously narrows the search.

**4. Matching removals do not amplify.**
For `K_{5,5}` (`n=10`, `E(10)=0`), exact minimax gives `F=14`, `ceil(log2 e)=14`, local 0. Removing a matching of `m` relations gives exact values

\[
m=1,2,3:\qquad F=15,\quad \ceil{\log_2 e}=14,\quad \text{local}=1,
\]

so the extra comparison plateaus rather than growing linearly. A separate family with three antichain groups and two maxima has `e(P_k)=2(3k+1)!/(2k+1)`; at `k=2`, `F=12`, `C=11`, local 1. The `k=3` exact run was stopped after 15 minutes without a result.

## Honest limits

- General-poset SUPI results and certificate **soundness** do not settle this: the question is about exact minimax **completeness**, not whether `ceil(log2 e)` is a valid lower bound.
- No all-`n` proof of `≤3` and no counterexample were obtained.
- The decisive next test is either:
  1. an exact/lower-bound computation establishing one of `S(25)=86, S(26)=91, …, S(32)=121`, which immediately gives a complete-bipartite falsifier at `n=40..43`; or
  2. a non-complete height-two construction with `e(P)<n!/4` and an exact minimax lower bound of `local ≥4`.

I posted this negative/structural update to Antonina #301 as the front result. No repository or Lean changes were made; the worktree is clean at `6a96398`.
I’ll verify what already happened without repeating any external action.
State checked; no external action was repeated.

## What actually happened

- **Board #301:** the front result was posted exactly once at `2026-11-09T19:12:04.764Z` by author `SoringP1 frontier: height-two-excess-four-at-global-one`. The digest finds **1 unique match**, so no duplicate post exists.
- **Git/repository:** worktree is clean at `6a96398`. No commit, branch, PR, Lean file, or repository change was made.
- **Scratch artifacts:** all computation files remain only under `/tmp/opencode/h2search` (`poset.py`, Go solvers, exact-run outputs, PDFs/texts, `board_post.md`, `post.json`). These are not repository effects.
- **Background processes:** none are still running.

## Unfinished / uncertain durable records

- The frontier ledger still lists `height-two-excess-four-at-global-one` with `"status": "running"` and `agent_id: r3kyAQbXlayQf1uWAccJ8B-clubs`. The research result itself is complete and posted, but this operational ledger entry was not reconciled by the agent.
- The `k=3` exact minimax run for the auxiliary family was intentionally stopped after ~15 minutes with no result. That is a recorded computational limit, not an external side effect.

No further posts, commits, or repository changes were made. The only item needing review is the ledger status remaining `running`, which the keeper can reconcile without re-running or reposting the result.

## Other metadata

```json
{
  "finished_at": 1794251698.465657,
  "started_at": 1794249113.979309
}
```
