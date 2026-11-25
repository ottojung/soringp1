# antonina-YoGaLd4kz9IPR4l44M1wEh-boat

Session: ses_e45391042ffex8X0cfpht47Ovw
Workspace: /home/lubko/soring-fronts/s-optimal-tree-average-depth-gap
Created: 1794134962152; updated: 1794136050168

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 598 (msg_1bad651370016B61CWn5AuHxQh)

## Mathematical finding

I attacked the natural all-`n` route to the O(1) horn:

> **Claim.** `A(n) = L(n)` for all `n`, where `L(n)=(q+1)n!-2^q`, `q=ceil(log2 n!)`, is the exact bounded-height coding/Kraft optimum.

This claim is **false**, first at `n=7`.

- **Independent exact computation:** a DP over transitively closed posets, memoizing  
  `F(P,r)=e(P)+min_q(F(P+q,r-1)+F(P+not q,r-1))`,  
  reproduces the posted `n<=6` values and gives
  `A(7) = 62416/5040`, at height `r=13=S(7)`.
- This matches Kollár’s published minimum `f(7)=62416/7!`.
- But `L(7)=62368/5040`. The deficit is
  `48/5040 = 1/105 ≈ 0.0095238`.
- For `n=8`, AbouEisha–Chikalov–Moshkov (*Discrete Appl. Math.*, DOI `10.1016/j.dam.2015.10.030`) prove
  `A(8)=f(8)=620160/8!`, while `L(8)=619904/8!`; deficit `256/40320=2/315≈0.0063492`.
  They also prove every minimum-average tree for `n=8` has minimum depth.
- For `n∈{1,...,6,9,10}`, `A(n)=L(n)` from the coding bound being attained.

So the observed gap stays small:
`A(n)-log2(n!) <= 0.0861` for all `n<=10` (the universal coding maximum), but **coding equality genuinely fails at `n=7` and `n=8`**.

## Exact obstruction / failed approach

Pure Kraft/bounded-height coding cannot prove the O(1) horn. The smallest local realizability obstruction is the `n=5` poset

`succ=(26,0,10,0,8)`, `e=8`, `m=4`,

which has **no comparison splitting `4/4`**; the best split is `3/5`, with entropy loss `0.045566`. Such nodes are invisible to leaf counting and already force the `n=7` deficit.

## Structural reduction

Let `f(n)` be the unconstrained minimum average depth over all correct sorting trees. Then

- `A(n) >= f(n)`;
- `A(n)=f(n)` exactly when a minimum-average tree is also minimum-depth, i.e. Knuth’s simultaneous-optimum problem. This is known for `n<=10`, open in general.

Consequences:

- The **O(1) horn** implies `f(n)=log2(n!)+O(1)`, stronger than the current `o(n)` constructions and Taranovsky’s conjectured `Θ(log n)` optimum. It also follows immediately from the unproved all-`n` bound `S(n)=log2(n!)+O(1)`.
- The **unbounded horn** implies `S(n)-log2(n!)→∞`, since `A(n)<=S(n)`. A lower bound on `f(n)-log2(n!)` would suffice, but is not necessary; a height-constrained argument could in principle work even if `f` is `log2(n!)+O(1)`.

## Honest limits

I did **not** prove either horn. I found no infinite family or new asymptotic lower bound. The finite evidence remains consistent with O(1), but the decisive unbounded alternative would be a sorting-number breakthrough, and the O(1) side is at least as strong as a major open average-sorting/simultaneous-optimum bound.

No repository or Lean changes were made; the worktree is clean. I posted the finding to board #301, including a correction clarifying that `A(n)>=f(n)` means an unbounded `A` implies unbounded **`S` excess**, not necessarily unbounded `f` excess.

## Output 681 (msg_1bad76f8800119vaWZULaLbtaq)

Inspected the existing conversation, worktree, Git state, board #301, and the durable frontier ledger. No duplicate action was taken.

**Effects that actually happened**
- Git worktree is clean on `billy-dev`; no commits, repo changes, or Lean changes.
- The only working files are temporary: `/tmp/opencode/a7.go`, `board_post.txt`, `board_correction.txt`.
- Board #301 contains exactly **two** matching comments from this front:
  1. the finding at `2026-11-08T11:05:42Z`;
  2. the correction at `2026-11-08T11:06:04Z`.
  No duplicate posts were made.
- The ledger entry for `s-optimal-tree-average-depth-gap` still has `status: "running"` with the live agent ID. That is expected while this session is alive; the keeper transitions it after exit. I did not edit the ledger manually.

**Unfinished work**
None. The mathematical result, correction, and honest-limits report are already recorded. The correction remains necessary and is present: `A(n) >= f(n)`, so an unbounded `A` implies unbounded worst-case `S` excess but not necessarily unbounded unconstrained average `f` excess.

**Uncertainty**
No external effect is ambiguous. The only pending state is the ledger's `running` status, which is a live-agent bookkeeping state rather than a missing result.
