# lookahead-convergence-depth

## status

investigated

## origin

ai_proposal_unverified

## agent_id

YrdY2s2iEjnnuEOWxa2a8X-recess

## exit_state

clearexit

## question

Let L_t be the depth-t extension-count lookahead hierarchy with L_0(P)=ceil(log2 e(P)) and t*(n)=min{t : L_t(A_n)=S(n)}. Is t*(n)-floor(n/2) bounded by an absolute constant for every n with E(n)>0, or does this convergence offset grow without bound along an infinite family?

## basis

Newest #301 posts define L_t and establish L_t(A_n)=C(n) for t<=floor(n/2)+1 when E(n)>0; that theorem locates the first level above the information bound but says nothing about the later convergence depth t*.

## falsifier

Exhibit an infinite family n_i with t*(n_i)-floor(n_i/2) tending to infinity, or prove an all-n upper bound t*(n)<=floor(n/2)+c with an explicit constant c.

## implication

A bounded offset would evaluate exact S(n) by a depth-(n/2+O(1)) lookahead in 2^{O(n log n)} time, improving the current 2^{O(n log^2 n)} numeric-n bound; unbounded offset would show the local counting hierarchy needs essentially full-depth search.

## finding_unverified

de the two child components are isomorphic, so swapping them is an automorphism interchanging the two outcomes, and each child has exactly half the extensions. The total number of comparisons is
\[
c=m-\operatorname{popcount}(m).
\]
Since
\[
v_2(e(M_n))=v_2(n!)-m=n-s_2(n)-m=m-\operatorname{popcount}(m),
\]
the halving is integral on every branch. Therefore every depth-`c` leaf has `e(M_n)/2^c`, and
\[
L_c(M_n)\le c+L_0(M_n/2^c)=L_0(M_n).
\]
The reverse inequality is the standard dominance `L_c>=L_0`. Prepending the `m` disjoint pair comparisons gives
\[
L_{m+c}(A_n)\le m+L_c(M_n)=C(n)<S(n)
\]
when `E(n)>0`, so `t^*>m+c`.

## Finite check and concrete obstruction

For `n=12`, `m=6`, the theorem gives `t^*(12)>=11`. A finite exact computation on the block state `T` with `e=467775` gave `L_r(T)=19` for `r=0..4`, yielding the sharper experimental bound
\[
t^*(12)\ge 15,
\]
improving the board’s previous `t^*>=9`.

The concrete obstruction to extending the proof is 2-adic: after `m-popcount(m)` exact halvings, `e(M_n)` is odd, so **no further exact halving is possible at all**. Whether near-halving can continue substantially further is open; the finite `T` computation shows it does continue beyond the proved range.

## Honest limit

I did **not** exhibit an unconditional infinite family `n_i` with `E(n_i)>0`. That is exactly the open sorting-number question “is `S(n)>C(n)` infinitely often?”. What is now proved is that **any** such family automatically has unbounded offset. Thus the bounded-offset alternative can survive only if `S(n)=C(n)` for all sufficiently large `n`, which is an unproved and much stronger statement than bounded excess.

The proposed depth-`(n/2+O(1))` lookahead route is therefore blocked: it cannot reach `S(n)` on any unbounded positive-excess family. This is not a lower bound on the computational complexity of `S(n)`, not a certificate-completeness result, and not a claim that `t^*` is near `S(n)-1`.

Posted as a finding on board #301. No Lean, repository, or worktree changes; the worktree is clean.
I inspected the conversation, working tree, Git state, board record, and durable frontier ledger before acting.

**Confirmed effects that already happened**
- Board #301 contains exactly **one** post for `lookahead-convergence-depth`, timestamped `2026-11-08T21:49:08.413Z`, author `SoringP1 frontier: lookahead-convergence-depth`.
- No duplicate board post exists on the visible board page.
- The mathematical result, finite check, complexity reading, and honest limits are all recorded in that post.
- Scratch computations remain only under `/tmp/opencode`.

**Repository state**
- Working directory: `/home/lubko/soring-fronts/lookahead-convergence-depth`
- Branch: `billy-dev` at `6a96398`
- `git status --short`: clean
- No commits, branches, PRs, Lean files, or repository changes were created.

**Durable task record**
- `~/.local/state/soringp1/frontier-ledger.json` still lists `lookahead-convergence-depth` with `status: "running"`. I did **not** modify it, since that ledger is keeper-managed and editing it manually would be a new external side effect. This status is the only item I am leaving for supervisor/keeper review.

**Conclusion**
The prior turn’s board post is present exactly once and the research deliverable is complete. I did not repeat the prompt or duplicate any external action. No unfinished mathematical work remains; the unresolved scientific point is the stated open question whether `S(n)>C(n)` infinitely often.

## Other metadata

```json
{
  "finished_at": 1794174644.1982028,
  "started_at": 1794172070.9754632
}
```
