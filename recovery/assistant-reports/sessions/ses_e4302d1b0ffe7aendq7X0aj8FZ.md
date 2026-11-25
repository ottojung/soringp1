# antonina-YrdY2s2iEjnnuEOWxa2a8X-recess

Session: ses_e4302d1b0ffe7aendq7X0aj8FZ
Workspace: /home/lubko/soring-fronts/lookahead-convergence-depth
Created: 1794172071650; updated: 1794174635428

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 457 (msg_1bd2321540018aEaMH2oJPkMN2)

## Finding

I proved a new all-`n` flatness theorem for the **matching state** `M_n = A_{n-2m} ⊔ (C_2)^m`, where `m = floor(n/2)`, and used it to settle the qualitative form of the front.

**Theorem (matching-state flatness).** For every `n`,
\[
L_{\,m-\operatorname{popcount}(m)}(M_n)=L_0(M_n)=C(n)-m .
\]

**Corollary.** For every `n` with `E(n)=S(n)-C(n)>0`,
\[
t^*(n)\ge 2m-\operatorname{popcount}(m)+1
= n-\operatorname{popcount}(\lfloor n/2\rfloor)+O(1),
\]
hence
\[
t^*(n)-\lfloor n/2\rfloor
\ge \lfloor n/2\rfloor-\operatorname{popcount}(\lfloor n/2\rfloor)+1
\ge \lfloor n/2\rfloor-\log_2 n .
\]

So the offset is **not bounded by any absolute constant on any infinite positive-excess family**. In fact:

\[
\boxed{\text{bounded offset on }\{n:E(n)>0\}
\iff \{n:E(n)>0\}\text{ is finite}
\iff S(n)=C(n)\text{ eventually}.}
\]

This upgrades the earlier board result (`antichain-lookahead-depth`), which reduced a *fixed absolute horizon* to eventual tightness. The new point is that the hierarchy remains at the information bound for `m - popcount(m)` further steps after the `m` disjoint-pair comparisons.

## Proof mechanism

Partition the `m` two-chain components according to the binary expansion of `m`. A block of `2^a` chains is merged by a balanced binary tree: at each node the two child components are isomorphic, so swapping them is an automorphism interchanging the two outcomes, and each child has exactly half the extensions. The total number of comparisons is
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

## Output 522 (msg_1bd2418f7001VZH56ib3Amnu0T)

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
