# multi-chain-merge-exact-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

TQRiPLiniuS1NhA8B24H7n-allowed

## exit_state

clearexit

## question

Is the exact minimax merge number for a disjoint union of k at least 3 chains computable in time polynomial in the total number of elements for every tuple of chain lengths?

## basis

Newest two-chain-merge exact results cover only k=2, while the split-merge recurrence and Ford-Johnson group insertion use multi-chain merges.

## falsifier

Give a polynomial-time algorithm with a correctness and cost proof for all chain tuples, or exhibit an infinite family of tuples whose exact multi-chain merge is super-polynomial under a stated model.

## implication

A polynomial multi-chain merge would make the full split-merge architecture's height computable and narrow the exact S(n) search window; hardness would isolate the first merge stage where near-optimal sorting becomes intractable.

## finding_unverified

 value is `info+1`, so neither `M+constant` nor `max(M+3, info)` is complete.

All reported exact values were checked by two independent minimax implementations with different state encodings. These are finite experiments, not a proof of a complexity lower bound.

## Honest limits

- No polynomial algorithm was found.
- No unconditional super-polynomial lower bound was obtained; for variable `k` this would imply a breakthrough on computing `S(n)`.
- No primary source resolving the computational complexity of exact adaptive multi-list merging was found. Parallel multiway-merging literature concerns a different model and was not imported.
- General-poset hardness was not used; it does not transfer to chain unions.
- The decisive next step remains either a genuine joint multiway algorithm with correctness and cost proof, or a hardness family. The `(2,2,2)` example shows any candidate must be truly multiway; the all-ones tuple shows the variable-`k` version cannot be easier than exact `S(n)`.
On **billy-dev**, current working directory unchanged at `/home/lubko/soring-fronts/multi-chain-merge-exact-complexity`, git worktree clean at `6a96398`.

## External actions already performed (verified)
- **One** board post to Antonina issue #301 at `2026-11-09T00:56:48.076Z`, author `SoringP1 frontier: multi-chain-merge-exact-complexity`  
  - Present as a single unique message on page 1; checked page 2 for duplicates (none found).
  - Body is complete, including the all-ones-tuple reduction, the `(2,2,2)` binary-composition counterexample, `(3,6,1)` and `(5,5,1)` singleton-reduction counterexamples, results summary, and honest limits.
- Result file `/tmp/opencode/mcm/post_result.json` is the response from that single comment.

No commits, PRs, file edits in the repository, or other external actions were performed. Worktree clean.

## Durable task records
- Antonina issue #301 remains open as expected for ongoing project tracking.
- The research front in `/home/lubko/.local/state/soringp1/frontier-ledger.json` is still `running` with our agent ID (`TQRiPLiniuS1NhA8B24H7n-allowed`) and no recorded finding yet. That is normal: the keeper marks a front `investigated`/`blocked` from the agent's exit state, not immediately after a board comment, and is not something I should hand-edit.

## Unfinished work
None remaining.

## Other observations (for review, not action)
- Another unrelated process (`fmini` executing in `/tmp` under a different front, PID 21065) is active on billy-dev. I did not start or alter it.
- All new local artifacts—exact chain-merge computations and the board post text—live only under `/tmp/opencode/mcm/`; nothing was written into the repository.

## Summary of the mathematical result already posted
Short version of the completed front:
- **No** polynomial-time exact algorithm found, and no super-polynomial family proven.
- Precise barrier: the all-ones tuple `(1,1,...,1)` reduces exact `S(n)` polynomially to a variable-`k` multi-chain merge.
- Concrete counterexample: `F(2,2,2)=7` while any binary composition of exact two-chain merge numbers costs at least `8`, showing pairwise-merge certificates are sound but not complete.
- Failed reduction: a syntactically augmenting two-chain→three-chain law like `F(a,b,1)=M(a,b)+3` is false; counterexamples at `(3,6,1)` and `(5,5,1)`, where the exact value is `info+1`, not `M(a,b)+constant`.

All finite computations are explicitly labeled as finite exact calculations, not a lower-bound theorem.

## Other metadata

```json
{
  "finished_at": 1794185896.8999836,
  "started_at": 1794183556.2424917
}
```
