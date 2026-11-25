# antonina-fmlURtnixzDYUXthMPR1iZ-outright

Session: ses_e4515e305ffetiZ0zOusb6x4gs
Workspace: /home/lubko/soring-fronts/fixed-arity-merge-architecture-threshold
Created: 1794137267506; updated: 1794141385350

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 315 (msg_1bb2835160011lBVrkoZoiw0tj)

## Recovery audit

- Host is `billy-dev`; worktree stayed clean throughout, no commits, no Lean/repository edits.
- No prior #301 post existed for `fixed-arity-merge-architecture-threshold`; the interrupted turn left no external effect.
- Posted exactly one new board #301 comment under `SoringP1 frontier: fixed-arity-merge-architecture-threshold`; digest confirms one matching message.
- The durable ledger still says `running`; I did not hand-edit it, since that belongs to the keeper.

## Mathematical finding

**1. The front is literally degenerate.**  
If `k=1` is allowed, `k*(n)=1` for every `n`, because one block followed by an empty merge is just optimal sorting. If the intended nontrivial range is `k>=2`, then `k=n` always attains by taking all singletons. Thus the quoted “bounded infinitely often vs tends to infinity” question only makes sense after explicitly excluding `k=1`.

I proved a small universal bound in that nontrivial setting:

> **Theorem.** For every `n>=2`, `k*(n) <= n-1`.

*Proof sketch:* take an optimal sorting tree and its root comparison `{a,b}`. Use the `(n-1)`-block architecture consisting of the block `{a,b}` and `n-2` singleton blocks. Sorting the pair costs one comparison; the optimal merge of that 2-chain with the singletons is exactly the optimal continuation after the root comparison, of height at most `S(n)-1`. Hence this architecture has height at most `S(n)`, and at least `S(n)` because it sorts.

**2. The cited split-merge gaps do not apply to this front.**  
The board’s `split-merge-asymptotic-gap` numbers use the *recursive* recurrence

\[
R(n)=\min_{a+b=n}\bigl(R(a)+R(b)+M(a,b)\bigr),
\]

where each block is rebuilt by the same split-merge architecture. This front requires each block to be sorted **optimally**, so its binary value is

\[
B_2(n)=\min_{a+b=n}\bigl(S(a)+S(b)+M(a,b)\bigr).
\]

These are different. In fact,

\[
B_2(12)=S(11)+M(1,11)=26+4=30=S(12),
\]
\[
B_2(13)=S(12)+M(1,12)=30+4=34=S(13).
\]

So in the nontrivial range `k>=2`, `k*(12)=k*(13)=2`. The same one-element split attains at `n=6,7,8,11,14,15,16,22`. Therefore the board’s certified `R(n)-S(n)` gaps at `12,13` and the `569` at `10922` do **not** extend the binary barrier to this one-level architecture.

**3. New exact small values.**  
Using exact minimax over interleaving sets (independent of the repo scripts):

- `k*(2)=k*(3)=k*(4)=2`;
- `k*(5)=3` via blocks `(1,2,2)`;
- `k*(6)=k*(7)=k*(8)=2` via `(1,n-1)`;
- `k*(9)=4` via `(1,1,2,5)`: block cost `0+0+1+7=8`, and `M(5,2,1,1)=11`, total `19=S(9)`;
- `B_2(9)=B_3(9)=20`, so `k*(9)=4`;
- `k*(10)>=5`: `B_2(10)=B_3(10)=23>S(10)=22`; for `k=4`, all partitions except `(1,2,2,5)` have information lower bound `>=23`, and for `(1,2,2,5)` an exhaustive depth-`13` tree search proves `M(5,2,2,1)>=14`, so every 4-block value is `>=23`.

This is strongly nonmonotone: `2` at `n=8`, `4` at `n=9`, `2` at `n=11`. Finite values give no reliable trend.

## Exact obstruction and honest limits

- The positive horn at `K=2` is exactly the open **two-phase exactness** question: `B_2(n)=S(n)` whenever `S(n)=S(n-1)+ceil(log2 n)`. This holds at the known hits `2,3,4,6,7,8,11,...,16,22` but is open infinitely often.
- The negative horn `k*(n) >= c n/log n` cannot follow from current information/merge technology. For fixed `k`, the block-plus-merge information lower bound is only `C(n)+O(k)`, while `S(n) <= FJ(n)=C(n)+0.1137n+O(log n)` and Sergeev gives excess `o(n)`. Proving all fixed-`K` architectures fail for all large `n` needs new lower bounds on `S` or genuinely stronger multiway merge gaps.
- Multiway merge-number lower bounds are **sound** bounds on one stage; they are not completeness/attainment certificates for the antichain root. The recursive `R` gaps are likewise sound only for the recursive architecture class.
- I did not prove either horn. The `n=10`, `k=5` case is not fully settled (the `(2,2,2,2,2)` merge at information bound `17` was left undecided). No repository or Lean changes were justified.

## Output 339 (msg_1bb28cfbc001eM9eg4YM7wkirc)

Recovery inspection complete. No external action was repeated.

**Verified state**
- Host: `billy-dev`.
- Repository: `/home/lubko/soring-fronts/fixed-arity-merge-architecture-threshold`.
- Git: clean worktree, `HEAD = 6a96398`; no commits, Lean changes, or repository edits.
- Board #301: exactly **one** matching comment exists, at `2026-11-08T12:35:29.350Z`, author `SoringP1 frontier: fixed-arity-merge-architecture-threshold`. The digest reports one unique match, so it is not a truncated duplicate.
- Scratch files are confined to `/tmp/opencode/fixedarity/`.
- Durable ledger entry `fixed-arity-merge-architecture-threshold` still shows `status: "running"`. That is keeper bookkeeping; I did not edit it.

**Unfinished work**
None required. The prior turn already completed the investigation and posted its finding: the literal `k*` is degenerate, the cited recursive split-merge gaps do not transfer to the one-level optimal-block architecture, `k*(n) <= n-1` was proved, and exact small values `k*(5)=3`, `k*(6..8)=2`, `k*(9)=4`, `k*(10)>=5` were established. Both all-`n` horns remain open.

The only explicitly unresolved side calculation is the non-decisive `n=10`, `k=5` merge case; leaving it undecided does not affect the reported mathematical conclusion. No further board post, commit, or repository change is warranted.
