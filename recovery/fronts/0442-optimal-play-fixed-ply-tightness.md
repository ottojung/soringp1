# optimal-play-fixed-ply-tightness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ZItctC9i92gwLNLhgNHYbx-release

## exit_state

clearexit

## question

For every fixed t, is the depth-t extension-count lookahead L_t(P) within an absolute constant of F(P) for every poset P reachable on a height-S(n) optimal play from the n-antichain, for all n?

## basis

Board #301 one-ply L1 theorem and root-only lookahead fronts; docs/research-one-ply-obstruction.md; exact scratch checks of W and ordinal-sum W^(+)k blocks with e=8^k, F=4k and ceil(log2 e)=3k.

## falsifier

Exhibit an explicit n, a state P on a height-S(n) play, and a fixed t with F(P)-L_t(P) at least 2, or prove a uniform all-t bound for that reachable family.

## implication

A fixed-ply local bound within O(1) would yield a stronger sound pruning invariant for exact unary S(n); failure would rule out every bounded-ply local information certificate along optimal play.

## finding_unverified

t for infinitely many `n`.

So a reachable counterexample with `F-L_t >= 2` would itself prove the global sorting lower bound

\[
S(n)\ge \lceil\log_2 n!\rceil+2,
\]

which is a new lower bound beyond the information bound, not a finite local computation.

### The `W^(+)k` evidence does not transfer [deduction]

For the known witness `W` and its ordinal sums:

\[
e(W^{(+)k})=8^k,\quad F(W^{(+)k})=4k,\quad L_0=3k,\quad L_1=3k+1,
\]

so the general-poset gap is `F-L1 = k-1`, unbounded. But if `W^(+)k` occurred in a height-`S(5k)` tree, the theorem above would force

\[
G(5k)\ge k-1.
\]

Exact values give `G(10)=0`, `G(15)=1`, `G(20)=0`, so `W^(+)k` is impossible on optimal plays for `k=2,3,4`. The Ford–Johnson bound `S(5k) <= sum ceil(log2(3i/4))` gives `G(5k)<k-1` exactly for `3<=k<=2000`; the standard asymptotic indicates the same for all larger `k` (I did not turn that asymptotic step into a fully formal all-`n` lemma, but the finite range already excludes every constructible case).

Thus the `W^(+)k` family is a genuine **general-poset non-completeness** result, not a reachable falsifier. This is the distinction between soundness and completeness: `L_t <= F` holds for all posets, but completeness on the reachable family is equivalent to the global bounded-gap problem for `S(n)`.

### Honest limits [open]

- I found **no explicit reachable falsifier** with `F-L_t >= 2`.
- Whether `G(n)` is bounded is open. Exact values through `n=22` all have `G(n) in {0,1}`; the literature bound `S(28)>=99` gives only `G(28)>=1`.
- I do not claim `G(n)` is unbounded, and I do not claim any new exact value of `S(n)`.
- No Lean files, repository changes, commits, or PRs were created. Scratch work is under `/tmp/opencode/fixedply`.

I posted the concise version as a comment on Antonina board #301.
Recovery audit complete — I did **not** repeat the prompt or create any new external effect.

## Effects verified as already completed

- **Board #301:** exactly **one** matching post exists from the previous turn:
  - author: `SoringP1 frontier`
  - timestamp: `2026-11-09T14:48:06.659Z`
  - digest match count: **1**
  - no duplicate posted.
- **Repository:** worktree clean on `billy-dev` at `6a96398`; no commits, edits, Lean files, tests, or PRs.
- **Scratch only:** `/tmp/opencode/fixedply/{check.py,board.md,post.json}`, outside the repository.
- **Durable ledger:** `optimal-play-fixed-ply-tightness` still has `status: running`, `exit_state: null`, `finding_unverified: null`. That is keeper-managed state; I did not edit it manually.

## Unfinished work

None. The previous turn had already completed the investigation and posted the result.

## Mathematical status (unchanged)

The recorded finding stands:

- For every state `P` at depth `d` in any height-`S(n)` tree from the antichain,  
  `F(P) - L_t(P) <= F(P) - L_1(P) <= S(n) - ceil(log2 n!) = G(n)`.
- Hence the fixed-ply reachable-family question is equivalent to the global bounded-information-gap question: `sup_n G(n) < infinity`.
- The `W^(+)k` ordinal-sum blocks have unbounded general-poset `L1` gap `k-1`, but if they appeared on a height-`S(5k)` play they would force `G(5k) >= k-1`; known exact values rule this out for `k=2,3,4`, and the Ford–Johnson check rules it out numerically for the tested larger range.
- No explicit reachable falsifier was found. Whether `G(n)` is bounded remains open.
- No Lean or repository changes were made.

No further action taken to avoid duplicating the existing board post.

## Other metadata

```json
{
  "finished_at": 1794235849.9550395,
  "started_at": 1794235134.3047373
}
```
