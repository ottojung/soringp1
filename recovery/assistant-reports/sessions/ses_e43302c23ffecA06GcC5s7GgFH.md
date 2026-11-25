# antonina-6gUeMMrUNtwJiDVAQtpfJ8-take

Session: ses_e43302c23ffecA06GcC5s7GgFH
Workspace: /home/lubko/soring-fronts/two-chain-merge-exact-complexity
Created: 1794169099328; updated: 1794170191084

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 714 (msg_1bcdf9f5a0014EwE6lMLZ6fC8F)

## Recovery audit

- No earlier #301 post existed for `two-chain-merge-exact-complexity`; the ledger entry was still `running` with no recorded finding.
- Worktree was clean at `6a96398`; no commits, branches, Lean files, or repository edits were made.
- I created exactly one new external effect: a board #301 comment at `2026-11-08T20:35:27Z`, verified present exactly once.

## Mathematical finding

**The stated #P/PP-hardness falsifier was not reached, but the natural polynomial-time candidate for exact `M(a,b)` is false on literature-certified values.**

The candidate was the extreme-insertion DP

\[
R(0,b)=R(a,0)=0,\qquad
R(a,b)=\min_{1\le x\le b}\max\bigl\{
1+R(a,x-1),\;
1+\lceil\log_2(b-x+1)\rceil+R(a-1,b)
\bigr\}.
\]

It is `O(ab)` and matches exact minimax for all tested pairs with `a+b<=12` except:

\[
R(3,6)=8\quad\text{but}\quad M(3,6)=7,
\]
\[
R(2,8)=7\quad\text{but}\quad M(2,8)=6.
\]

`M(3,6)=7` is independently certified by Hwang’s 1980 primary result `f_3(7)=6`; I also reproduced it by exact closed-state minimax. Therefore no DP that fully resolves one extreme insertion before continuing the lower merge can be exact. At `(3,6)`, after the optimal first comparison `A_3` vs `B_4`, the branch `A_3>B_4` optimally continues with `A_1` vs `B_2`, not by finishing the insertion of `A_3`. Exact `M` requires interleaving the insertion search with the lower merge.

## Exact obstruction to the hardness route

The unary graph

\[
G_M=\{1^a\#1^b\#1^k:M(a,b)\le k\}
\]

is sparse: at input length `N` it has only `O(N^3)` members. Hence:

- if `G_M` were PP-hard under polynomial-time many-one reductions, then `PP ⊆ P/poly`;
- similarly, many-one #P-hardness would put the relevant counting class in `FP/poly`.

So the falsifier’s first horn cannot be proved by a many-one reduction without a major nonuniform collapse. Turing-hardness remains open. This is a barrier to a proof strategy, not a proof that `M` is easy. Binary-encoded `a,b` would be a different question and could plausibly be PSPACE-hard; the front explicitly asks polynomial time in `a+b` (unary).

## Localization

Hwang’s configuration framework has `O((a+b)^{2a})` states, so for every fixed `a`, exact `M(a,n)` is polynomial-time computable in `n`. Together with the certified tape-optimal range `m<=n<=floor(3m/2)+1` (and the `1.52m` extension), the unresolved regime is precisely `a→∞` with `b/a` unbounded.

## Important complexity correction

Polynomial-time `M` would make the split-merge recurrence value `L(n)` polynomial-time computable, but `L(n)>=S(n)` and is strictly above `S(n)` at `n=12`. Conversely, hardness of `M` would not imply hardness of exact `S(n)`; it would isolate a limitation of the independent-completion merge architecture, not a barrier to computing `S`.

**Honest limit:** no all-pairs polynomial algorithm and no hardness theorem were proved. The durable result is the counterexample to the natural `O(ab)` extreme-insertion DP plus the sparsity barrier. No repository or Lean changes were made.

## Output 763 (msg_1bce05f4a001TRW5F3IR6EQdbN)

## Recovery inspection

- **Board effect confirmed:** exactly one #301 post exists for `two-chain-merge-exact-complexity`, at `2026-11-08T20:35:27Z`. I did not post again.
- **Git state:** clean worktree on `billy-dev` at `6a96398`; no commits, branches, Lean, or repository changes.
- **Processes:** no research/merge-probe process is still running.
- **Scratch artifacts:** only `/tmp/opencode` files; not repository effects.
- **Ledger:** still records this front as `running` with no finding and no `finished_at`/`exit_state`. I did not edit it, since that transition is keeper-managed. This is stale operational state, not an incomplete mathematical result.

## Unfinished work

None in the research task. The previous turn already completed the intended deliverable and posted it once.

## Result recap

No #P/PP-hardness reduction was found. The concrete result is a disproof of the natural polynomial extreme-insertion DP:

- `R(3,6)=8` but exact `M(3,6)=7` (certified by Hwang’s `f_3(7)=6` and independently reproduced).
- `R(2,8)=7` but exact `M(2,8)=6`.

The obstruction is that exact `M` interleaves insertion search with the lower merge; it cannot be reduced to resolving one pending extreme at a time.

The stated many-one hardness route is also blocked by sparsity: the unary graph of `M` is sparse, so many-one PP-hardness would imply `PP ⊆ P/poly`. Turing-hardness remains open. No all-pairs polynomial algorithm or hardness theorem was proved. No further external actions were taken.
