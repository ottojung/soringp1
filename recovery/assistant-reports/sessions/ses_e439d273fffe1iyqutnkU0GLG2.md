# antonina-NwjXHXubqZVGOADmdcp5ta-gone

Session: ses_e439d273fffe1iyqutnkU0GLG2
Workspace: /home/lubko/soring-fronts/gpc-height-two-residual-15-18
Created: 1794161957174; updated: 1794166503202

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1bc62dacd001VDMS6Zvoyb1hrq)

I'll start by reading the repo contract and research plan, then inspect the existing GPC tools.

## Output 183 (msg_1bc65207b001AAubZJ7W87uGwN)

I have the full board post. Let me set up my own scratch and build exact tools, starting with independent arithmetic verification and small-case structure.

## Output 276 (msg_1bc6c7e47001vY2uAC6yUgfF4j)

Now let me explore the structure of the height-two case: how `e` grows as cross edges are removed, and how the proof bound `m <= S(a)+S(b)+r` interacts.

## Output 330 (msg_1bc70992d001ClLD2aX0rvQsdf)

The arithmetic checks out, with slightly wider residual splits than the post listed. Now the key structural question: what balance constant is known for height-two posets? Let me check the primary literature.

## Output 388 (msg_1bc7257d1001oMOrYxyjMhHJNa)

Now I'll test a refined merge bound: after sorting the two parts, the residual interleaving count may be small even when many edges are missing. This could rule out the dangerous `m` values without full minimax.

## Output 470 (msg_1bc784104001otvRbnK4ouKf3z)

The width-two GPC bound looks promising. Let me test the key inequality `N_max <= 2ab * e/(a!b!)` that would make the finite window rigorous.

## Output 514 (msg_1bc7a15fd001DYcH8DxV9EV33I)

This gives a rigorous finite-certificate route: for each nondecreasing release vector, the minimal realizing graph has a nested (chain-graph) form, so its `e` is a lower bound for any graph with that release pattern. I'll implement that certificate exactly.

## Output 659 (msg_1bc7ed28b0015PpcOIH2YNktIJ)

The n=15 certificate closes with zero unresolved release patterns. Let me run the n=16 splits.

## Output 703 (msg_1bc7f5d89001AKN6rPsABAgpSi)

The certificate closes n=15 and n=16. Let me run the remaining ordered splits for n=17 and n=18, including the reversed orientations.

## Output 726 (msg_1bc809e91001YAc5qa66klrr4D)

All ordered splits close with zero unresolved. Before trusting this, I need to verify the key rearrangement lemma (sorted releases maximize interleavings) and audit the certificate against brute force on small cases.

## Output 792 (msg_1bc85ed42001MdRQA7PKqNNN1C)

The audit exposed exactly one edge case: the antichain (all-zero release vector), where `m = S(n)` exceeds the non-antichain cap. I'll special-case it and rerun.

## Output 855 (msg_1bc897fd0001pTrzs5O2Wi61oR)

The C certificate closes every residual split. Now let me reproduce it independently in Python (different `e` implementation) for n=15 and n=16, and audit the `m` bound against exact minimax on small cases.

## Output 916 (msg_1bc9ac653001EwsdETNUQsRwbb)

The finite residual is closed. Now let me rigorously extend the `n>=25` arithmetic tail with a finite log check plus an explicit asymptotic argument.

## Output 943 (msg_1bc9d22b4001d1XcvjJunchBlG)

The proof chain is now complete. Let me add summary statistics to the certificate (tightest margin, max residual count) and record the final numbers for the report.

## Output 993 (msg_1bca031aa0014yiY5EidEvJSnB)

The mathematics is closed. Let me now verify the board-posting interface and prepare the report.

## Output 1020 (msg_1bca0b1fc0016F988J5vqV83w5)

Let me consolidate the exact outputs and confirm the worktree is clean before posting.

## Output 1053 (msg_1bca19dbf001iU01f69RaXBOph)

Let me run one final exhaustive sanity check of the theorem on all height-two posets up to 6 elements, then post.

## Output 1082 (msg_1bca6edcc001E8owpti4FM4lnh)

The report is ready. I'll post it to Antonina issue 301.

## Output 1111 (msg_1bca731d7001zVoe320Qdp2PAL)

Posted to Antonina issue #301 at `2026-11-08T19:33:43Z` as **SoringP1 frontier: gpc-height-two-residual**. Worktree remains clean at `f89f6d0`.

## Result: proof, not a counterexample

**Claim.** Every finite height-two poset satisfies

\[
e(P)\ge F_{m(P)+2}.
\]

Status: **paper proof conditional on two inputs plus an exact finite certificate**:

- Peczarski, *Order* 23 (2006): GPC for width-two posets (peer-reviewed).
- Gupta, arXiv:2607.23926v2, Theorem 5: GPC for all non-chain posets through 14 elements (preprint).
- Exact integer certificate for n = 15..18, independently reproduced.

It proves only the height-two Fibonacci inequality, **not** GPC for height two, and changes no complexity-class statement about `SORT-BOUND-U`.

## Structural argument

For height-two \(P\) with parts \(a=|L|,\ b=|U|\):

1. \(e(P)\ge a!b!\).
2. Non-antichain lemma: \(m(P)\le S(n)-1\) (proved by skipping a known comparison in an optimal antichain strategy).
3. New release-vector bound: for an order \(\pi\) of \(L\), let \(r(u)\) be the last neighbour position of \(u\in U\). Interleavings are nondecreasing sequences \(x_j\ge r(\sigma_j)\); sorting thresholds maximizes the count.
4. Let \(r^*\) be the sorted release vector of a maximizing pair. Then \(e(P)\ge e_{\min}(r^*)\), where \(e_{\min}\) is the chain-graph poset with edges \(l_i<u_j\iff i\le r^*_j\).
5. Sort \(L\) and \(U\). The residual \(Q\) has width ≤2, so Peczarski's width-two GPC gives
   \[
   m(Q)\le M(N_{\max}),\qquad M(N)=\max\{t:F_{t+2}\le N\}.
   \]
   Hence \(m(P)\le S(a)+S(b)+M(N_{\max})\), capped by \(S(n)-1\).
6. The certificate enumerates every nondecreasing \(r\in[0,a]^b\) and verifies \(e_{\min}(r)\ge F_{U(r)+2}\).

## Exact certificate

- 210,782 release vectors enumerated; **166,920 checked; 43,862 skipped by \(U<m_{\min}\); 0 unresolved.**
- Tightest case: \(n=15\), split \(7+8\), \(r=(1,3,4,4,5,6,6,7)\), \(N=392\), \(U=41\):
  \[
  e_{\min}=583{,}351{,}632 > F_{43}=433{,}494{,}437
  \]
  a margin of \(1.3457\).
- n=18, split \(9+9\): 48,620 vectors, 39,177 checked, min margin 2.909.

The residual split set is slightly larger than the brief listed: n=15 also has \(6+9\); n=16 has \(6+10,7+9,8+8\); all reverses are covered.

## Remaining n

- \(n\le 14\): Gupta census + Peczarski Proposition 2.
- \(n=19..24\): exact arithmetic with \(m\le S(n)-1\); all excluded.
- \(n\ge 25\): exact check \(25..60\), high-precision log check \(25..5999\), and a rigorous analytic bound for \(n\ge 6000\) using \(S(k)\le k\log_2 k+1\), \(F_{U+2}\le\varphi^{U+1}\), and \(a\log a+b\log b\ge n\log(n/2)\).

## Limitations

- Conditional on the Gupta preprint and Peczarski width-two theorem; the certificate is exact but computer-assisted, not kernel-checked.
- The task brief’s phrase “posets with few cross relations” had the density direction reversed: near-minimum \(e\) is the nearly complete bipartite regime. The release-vector certificate avoids enumerating that huge space.
- Scripts and audit logs are under `/tmp/opencode/gpc-residual` (`certify.c`, `certify_py.py`, `tail_check.py`, `arith.py`, audits). No repo or Lean files were changed.

## Output 1175 (msg_1bca8202c001kd6ZPDqQmhgjZR)

Inspected state; **no repeated external action taken**.

## Effects that actually happened

- **Board post:** Antonina #301 contains **exactly one** comment from `SoringP1 frontier: gpc-height-two-residual`, created `2026-11-08T19:33:43.818Z`, 5,383 chars. It contains the finalized report (corrected `m_min` sentence and the `166,920 checked / 0 unresolved` totals). No duplicate exists on page 1.
- **Durable record:** `/tmp/opencode/gpc-residual/post_result.json` holds the API response.
- **Git:** worktree clean at `f89f6d0`; no commits or repository changes were made by this work.
- **Scratch artifacts:** certificate, independent Python recheck, arithmetic/tail scripts, and audit logs remain under `/tmp/opencode/gpc-residual`.

## Unfinished work

None from the original task. The reduction, conditional structural proof, exact n=15..18 certificate, independent verification, n≥19 arithmetic tail, and board report were all completed before the interruption. The only external side effect was the single board post, now confirmed present once.

No commits, purchases, or additional posts were made this turn. No uncertain effects remain.
