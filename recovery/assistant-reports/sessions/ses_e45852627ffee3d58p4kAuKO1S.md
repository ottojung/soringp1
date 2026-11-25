# antonina-IItosMqB3svvqjklkz0nTF-sticky

Session: ses_e45852627ffee3d58p4kAuKO1S
Workspace: /home/lubko/soring-fronts/sorting-increment-spectrum
Created: 1794129975929; updated: 1794130866196

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 412 (msg_1ba8733a9001QEdeX42uxCQMDG)

Posted the finding to Antonina issue #301. No repository or Lean changes; worktree is clean.

## Outcome

No counterexample to

\[
\lfloor \log_2(n+1)\rfloor \le S(n+1)-S(n)\le \lceil \log_2(n+1)\rceil
\]

was found. The upper bound is the standard sound sort-then-insert argument. The lower bound is **proved for all \(n\le 23\)**, and the **first open case is \(n=24\)**.

## Key structural reduction

Let \(C(n)=\lceil\log_2 n!\rceil\), let \(F(n)\) be the Ford–Johnson/merge-insertion comparison count, and let

\[
d(n)=F(n)-S(n)\ge 0
\]

be the Ford–Johnson deficit. The Ford–Johnson increment is

\[
g(m)=F(m)-F(m-1)=\left\lceil \log_2(3m/4)\right\rceil
\in \{\lfloor\log_2 m\rfloor,\lceil\log_2 m\rceil\}.
\]

With \(m=n+1\),

\[
S(m)-S(m-1)=g(m)-\bigl(d(m)-d(m-1)\bigr).
\]

Consequently, if Ford–Johnson is optimal at \(m\), i.e. \(d(m)=0\), then

\[
S(m)-S(m-1)\ge g(m)\ge \lfloor\log_2 m\rfloor,
\]

so the lower bound holds. Therefore **any counterexample must occur where Ford–Johnson is strictly beaten**, at an index \(m=n+1\) with \(S(m)<F(m)\).

## Unconditional range \(n\le 23\)

- For \(m=n+1\le 22\), \(S(m)=F(m)\) follows from the literature, so the lower bound holds for \(n\le 21\).
- \(n=22\): \(S(23)\ge C(23)=75\) and \(S(22)=71\), so the increment is at least \(4=\lfloor\log_2 23\rfloor\).
- \(n=23\): \(S(24)\ge C(24)=80\) and \(S(23)\le F(23)=76\), so the increment is at least \(4=\lfloor\log_2 24\rfloor\).

Thus the front’s recorded \(n\le 21\) extends to all \(n\le 23\), without needing exact \(S(23)\) or \(S(24)\).

## First open case

For \(n=24\), current bounds are \(S(24)\in[80,81]\) and \(S(25)\in[84,86]\). A failure would require \(S(25)-S(24)\le 3\), which is possible only for

\[
(S(24),S(25))=(81,84).
\]

So an 80-comparison sort of 24, or a certified lower bound \(S(25)\ge 85\), would settle \(n=24\) in favour of the law. Similarly the first possible failures at the next indices are \((S(25),S(26))=(86,89)\), \((S(26),S(27))=(91,94)\), and \((S(27),S(28))=(96,99)\), none certified.

## Obstruction to the proposed falsifier

Using only the universal information lower bound cannot refute the claim. For any \(L(n)\le C(n)\) and any valid \(U(n+1)\ge C(n+1)\),

\[
U(n+1)-L(n)\ge C(n+1)-C(n)\ge \lfloor\log_2(n+1)\rfloor.
\]

A genuine refutation needs a certified **excess** at \(n\),

\[
L(n)\ge C(n)+\bigl(C(n+1)-C(n)-\lfloor\log_2(n+1)\rfloor\bigr)+1.
\]

The only available excess certificates are the exact values for \(n=12,\dots,19,22\), each with excess 1, and \(S(28)\ge 99\), also excess 1. At \(n=28\) the needed excess is 2, and the required upper bound \(S(29)\le 102\) is already below \(C(29)=103\). Hence no published pair refutes the law.

## Honest limits

The all-\(n\) statement remains open from \(n=24\) and is entangled with whether Ford–Johnson is optimal below 47. Its first proven strict improvement is at \(m=47\): \(S(47)\le 200<F(47)=201\). That is a ceiling step; it would refute at \(n=46\) only if \(S(47)\le 199\), while the published bound is 200.

Also, the complexity implication that a universal increment law would force every optimal sorter to perform near-information “insertion steps” is not supported: the law is numerical, and the sort-then-insert construction gives soundness of the upper bound, not structural completeness. General-poset results (Kahn–Saks, extension counting) are sound but recover only the information/counting bound on the antichain, not the excess certificates needed for this front.

## Output 503 (msg_1ba884c39001FnCNpeGrTYxnnC)

Recovery inspection complete. I did not repeat the prompt or create any duplicate external effect.

**Verified state**
- Host: `billy-dev`.
- Repository: `/home/lubko/soring-fronts/sorting-increment-spectrum`.
- Git: clean worktree, HEAD still `6a96398`; no commits, files, Lean changes, or other repo side effects from the prior turn.
- Board #301: the finding was posted **exactly once** at `2026-11-08T09:39:13.137Z` under author `SoringP1 frontier: unary-s-increment-floor`. Raw board JSON shows one matching message (not merely a digest deduplication), so no second post is needed.
- Temporary files `/tmp/board_increment_post.txt` and `/tmp/increment_audit.py` exist as local scratch only; they are not repository artifacts.

**No unfinished research work**
The prior turn already completed and reported the mathematical result: no counterexample, lower bound proved for \(n\le 23\), first open case \(n=24\), plus the Ford–Johnson deficit criterion and certificate obstruction.
The requested report was delivered, so I am not rerunning it.

**One record for review**
Durable ledger entry `sorting-increment-spectrum` (front index 354) still shows `status: running`. I deliberately did not edit it, since status reconciliation belongs to the keeper and changing it manually could conflict with its normal recovery logic. The board post itself is durable and confirmed.
