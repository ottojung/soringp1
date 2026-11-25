# local-slack-value-hunting-alln

## status

blocked

## origin

executive_initiated

## agent_id

FCGZaFc0Mgfl7mMoPC9Hmg-sailor

## exit_state

failed

## question

Extend the positive-slack hunt to n = 7: exhibit a poset P reachable on an optimal play from the n-antichain with slack s = m(P) - ceil(log2 e(P)) >= 2, i.e. stronger than the documented n=12 case (S(12)=30, C(12)=29, slack 1); or prove that every reachable optimal-strategy poset has slack <= 1. Keep experiments consistent with the budgeted minimax solver already in the repo.

## basis

docs/research-obstruction-next.md section 6 (the n=12 gap is the first global gap; max slack 1 at n <= 6); research-n12-nontightness.md; the local gap bound via balanced merge M(m,m)=2m-1 (finite computations, labeled posets, exhaustiveness claims).

## falsifier

Exhibit a poset P with slack >= 2 (reachable on an optimal antichain play), or prove that every poset on any n has slack <= 1 (the n=12 example being the extremal one).

## implication

A slack-2 poset reachable on an optimal antichain play would be the first example of a gap larger than the documented n=12 one; a non-existence proof generalizes the n=12 obstruction to a structural statement about the antichain play.

## finding_unverified

I'll start by studying the environment: confirm I'm on billy-dev, read the contract documents, the board, and the research obstruction docs.
I'm on the correct host path. Let me verify the host name, pull the board digest, and look at the experiment tooling.
I'm on `billy-dev`. I have the board digest (recent activity is on other fronts). Now let me study the contract, the budgeted minimax solver, the literature values, and the board-posting tooling.
I now have the model, the solver, and the literature values. Let me check how to post to board #301, find any locally extracted primary-source PDFs, and confirm the worktree state.
The board is read via `antonina board show --id 301`. Let me check the CLI for the posting command and look for the locally extracted primary-source texts.
No PDFs in the repo; the obstruction note says texts were extracted locally — I'll pull the key primary sources with web search later. First, let me verify the repo is clean (it is: no `git status` output), and write the experiment script. I'll structure it as phases so I can run the n=7 forward-set scan first and see its size before committing to the minimax scan.
The `sizes7` run gave no output — let me check why (maybe an error), and run the evaluate checks individually.

## Other metadata

```json
{
  "finished_at": 1795311271.1245356,
  "retry_after": 0,
  "started_at": 1795309985.825402
}
```
