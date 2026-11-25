# antonina-fovbbVZwiNT72HzvUsbS79-frowned

Session: ses_e42d1feb8ffeOY7vt3OidH8vgn
Workspace: /home/lubko/soring-fronts/constant-advice-unary-sortbound
Created: 1794175271460; updated: 1794175809889

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 293 (msg_1bd3515ab001Kt5vbNBEQoPmMJ)

**Board report posted once to Antonina #301** (author `SoringP1 frontier: constant-advice-unary-sortbound`, 2026-11-08T22:08:30Z). Worktree remains clean at `6a96398`; no Lean, docs, tests, commits or PRs were created.

## Mathematical finding

Let

\[
t_L=\max\{n\le L-1:\ n+S(n)\le L-1\},\qquad U=\text{SORT-BOUND-U}.
\]

### 1. Exact advice-slice characterization

For a constant \(c\), a \(P/c\) decider with advice \(b_L\in\{0,1\}^c\) yields, for each advice string \(b\), a polynomial-time function \(g_b(L)\): the largest accepted \(n\) on well-formed length-\(L\) inputs (or \(\bot\) if the slice is not an initial interval). Correctness at \(L\) means \(t_L=g_{b_L}(L)\). Conversely, any finite family of polynomial-time \(g_i\) covering \(t_L\) at every \(L\) gives a \(P/O(1)\) decider. Hence

\[
U\in P/O(1)
\iff
t_L \text{ is covered at every }L\text{ by finitely many poly-time functions.}
\]

This is the standard advice-slice equivalence, and it is the precise form of the front.

### 2. Decisive obstruction to the lower-bound horn

Since \(P\subseteq P/O(1)\), if \(U\notin P/O(1)\), then \(U\notin P\). But \(U\in PSPACE\) is established (Claim A of `docs/research-certificates-barriers.md`). Therefore

\[
U\notin P/O(1)\ \Longrightarrow\ PSPACE\nsubseteq P/O(1)\ \Longrightarrow\ P\ne PSPACE.
\]

So the falsifier’s second arm — an \(\omega(1)\) advice lower bound for \(t_L\) — would resolve a major open separation. It is not a viable unconditional target under the project’s scope, and the front’s stated “complexity implication” substantially understates it. This is a one-way implication; \(P\ne PSPACE\) alone does not identify this particular language as being outside \(P/O(1)\).

### 3. Barrier: cutoff shape and growth alone cannot give \(P/O(1)\)

I also gave a diagonal construction showing there is a monotone \(0/1\)-step cutoff \(t\) with \(t_L=\Theta(L/\log L)\) such that

\[
U_t=\{1^n\#1^k:\ n+k+1=L,\ n\le t_L\}
\]

is in \(P/log\) but not in \(P/O(1)\). The diagonalization core is rigorous: enumerate finite families of poly-time functions, and at stage \(i\) choose \(L_i\) and \(t(L_i)\) to avoid every value in that family at \(L_i\), while extending \(t\) by \(0/1\) increments. The growth-preserving “corridor” interpolation is routine but was only sketched, not written out in full. The corresponding \(G(n)=a_n-n\) is monotone with \(G(n)=\Theta(n\log n)\).

Consequence: no proof of \(U\in P/O(1)\) can rely only on the monotone threshold representation, the known \(P/log\) cutoff, or the growth class of \(t_L\); it must use arithmetic information specific to \(S\).

## Failed approaches / honest limits

- No explicit \(P/O(1)\) machine was found.
- No \(\omega(1)\) lower bound was found; by the obstruction above, it would prove \(P\ne PSPACE\).
- The tempting consequence \(U\in P/O(1)\Rightarrow S\in FP/log\) is vacuous: every polynomial-growth unary function is in \(FP/log\), since the advice can be \(S(n)\) itself in \(O(\log n)\) bits.
- \(t_L\) is not eventually periodic (that would make \(S\) eventually linear, contradicting \(S(n)=\Theta(n\log n)\)), but \(P/O(1)\) is far larger than eventually periodic, so this does not settle the front.
- General-poset hardness and certificate soundness do not transfer to this advice question.

## Status

The front is open, with a sharp asymmetry: the lower-bound horn is blocked by a \(P\ne PSPACE\)-level implication, while the upper-bound horn is a genuine nonuniform compression question with no known construction or lower bound. This is an exact obstruction, not a proof of either horn.

## Output 362 (msg_1bd36243e001425njkT4Tbxrv5)

Inspection complete. **No external action was repeated.**

## Effects actually present

- **Host/worktree:** `billy-dev`, `/home/lubko/soring-fronts/constant-advice-unary-sortbound`.
- **Git:** clean at `6a96398`; no commits, branches, stashes, or file changes from this front.
- **Board #301:** exactly **one** matching post exists —
  `2026-11-08T22:08:30.269Z`, author `SoringP1 frontier: constant-advice-unary-sortbound`.
  A `--contains "constant-advice-unary-sortbound"` digest returns **1 unique match**, so no duplicate was made.
- **Repository:** no Lean, docs, scripts, tests, or note files were created or modified.
- **Temporary artifacts:** only `/tmp/opencode/board_post_constant_advice.md`, `board_post_result.json`, `board_post_err.txt`, and `check_cutoff.py`; none are repository changes.

## Durable record

The front `constant-advice-unary-sortbound` remains in the keeper-owned ledger as:

- `status: running`
- `exit_state: null`
- `finding_unverified: null`

That is the only outstanding bookkeeping item. I did **not** edit the ledger manually, since it is keeper-owned and a concurrent write could corrupt or duplicate state. The keeper should record the completed finding from the board post/agent exit.

## Mathematical status (unchanged, already posted once)

The finding is an exact obstruction, not a proof of either horn:

1. \(U\in P/O(1)\) is equivalent to \(t_L\) being covered at every \(L\) by finitely many polynomial-time functions.
2. If \(U\notin P/O(1)\), then \(U\notin P\); since \(U\in PSPACE\), this implies \(PSPACE\nsubseteq P/O(1)\) and in particular \(P\ne PSPACE\). Thus the requested \(\omega(1)\) advice lower bound is at least as strong as resolving a major open separation.
3. A diagonal construction shows the monotone cutoff shape, the \(P/log\) mechanism, and the growth class \(t_L=\Theta(L/\log L)\) alone do **not** imply \(P/O(1)\); the actual arithmetic of \(S\) is essential.
4. No explicit \(P/O(1)\) machine and no lower bound were found. The front remains open, with the lower horn blocked by the \(P\ne PSPACE\)-level implication.

No unfinished mathematical work remains, and no duplicate board post, commit, or push should be made.
