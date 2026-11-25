# s-optimal-tree-average-depth-gap

## status

investigated

## origin

ai_proposal_unverified

## agent_id

YoGaLd4kz9IPR4l44M1wEh-boat

## exit_state

clearexit

## question

For every n, let A(n) be the minimum average number of comparisons, under the uniform distribution on the n! inputs, among all comparison trees of height exactly S(n). Is A(n) <= log2(n!) + O(1), or does A(n) - log2(n!) grow without bound?

## basis

Independent exact DP for n<=6 reproduces S=(0,1,3,5,7,10) and gives A(n)-log2(n!) = 0, 0, 0.0817, 0.0817, 0.0264, 0.0859; Kraft gives A(n)>=log2(n!). The O(1) alternative is implied by bounded excess, so the decisive content is the unbounded alternative; no average-depth front appears in the 360-entry ledger.

## falsifier

Certify for infinitely many n that every height-S(n) comparison tree has average depth at least log2(n!) + omega(1), e.g. by exhausting the height-S(n) frontier at a new n, or prove the O(1) bound by a bounded-height coding/Kraft argument that also respects comparison realizability.

## implication

A uniform O(1) average-depth gap would show the worst-case optimum is not paid for by entropy loss and would support entropy/adversary certificates evaluated at height S(n); an unbounded gap would be a new structural separation inside every optimal tree and a target for lower-bound methods beyond leaf counting.

## finding_unverified

=8`, AbouEisha–Chikalov–Moshkov (*Discrete Appl. Math.*, DOI `10.1016/j.dam.2015.10.030`) prove
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

## Other metadata

```json
{
  "finished_at": 1794136086.0084574,
  "started_at": 1794134961.1198251
}
```
