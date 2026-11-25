# antonina-r3kyAQbXlayQf1uWAccJ8B-clubs

Session: ses_e3e6b3a8cffeRzC5H17GRoEn1K
Workspace: /home/lubko/soring-fronts/height-two-excess-four-at-global-one
Created: 1794249115100; updated: 1794251658858

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1c194c89e001tLZ2Bc0cdMtTHF)

I'll start by studying the repository, the contract, problem statement, and current board state.

## Output 1001 (msg_1c1b9adea001L8ohF6J6t6gkHU)

## Outcome

I attacked the front’s precise all-`n` claim:

> If `E(n)=S(n)-ceil(log2 n!) ≤ 1`, then every height-two `n`-element poset `P` satisfies  
> `F(P)-ceil(log2 e(P)) ≤ 3`;  
> equivalently, no such `P` reaches local excess `≥ 4`.

I did **not** find a counterexample and did **not** prove the `≤3` bound. The result is a precise obstruction plus new certified finite territory, not a resolution.

## Mathematical findings

**1. Four new certified sizes: `n = 40,41,42,43`.**
Ford–Johnson merge-insertion (OEIS A001768) gives an explicit upper bound `S(n) ≤ FJ(n)`. At these sizes

| `n` | `ceil(log2 n!)` | `FJ(n)` | `E(n)` |
|---:|---:|---:|---:|
| 40 | 160 | 161 | `≤1` |
| 41 | 165 | 166 | `≤1` |
| 42 | 170 | 171 | `≤1` |
| 43 | 176 | 177 | `≤1` |

So these are legitimate new tests of the front, beyond the exact values through `n=22`.

**2. Complete-bipartite route is exactly one open sorting number away.**
For `K_{a,b}=A_a(+)A_b`,

\[
e(K_{a,b})=a!b!,\qquad F(K_{a,b})=S(a)+S(b),
\]

hence

\[
F-\lceil\log_2 e\rceil = E(a)+E(b)+\delta,\qquad \delta\in\{0,1\}.
\]

Using exact `S(k)` for `k≤22` and the Ford–Johnson upper bound for larger `k`, the largest possible complete-bipartite local excess at `n=40..43` is exactly **4**, never more. It reaches 4 only if a Ford–Johnson upper bound is tight. The smallest such certificate would be

\[
K_{25,15}\ (n=40):\quad C=124,\quad F\le S(25)+S(15)\le 86+42=128,
\]

so `local = 4` **iff** `S(25)=86`. Similarly `K_{27,13}` needs `S(27)=96`, `K_{28,12}` needs `S(28)=101`, `K_{32,8}` needs `S(32)=121`.

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

## Output 1055 (msg_1c1bb3fba001JxSHGP1B9L9bLR)

I’ll verify what already happened without repeating any external action.

## Output 1088 (msg_1c1bb774100195rfA5JE5FihEK)

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
