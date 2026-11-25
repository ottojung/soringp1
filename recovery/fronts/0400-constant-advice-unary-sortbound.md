# constant-advice-unary-sortbound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

fovbbVZwiNT72HzvUsbS79-frowned

## exit_state

clearexit

## question

Is SORT-BOUND-U = {1^n#1^k : S(n) <= k} decidable in polynomial time with O(1) advice per input length, or does every such decider require omega(1) advice infinitely often, making the known P/log cutoff t_L optimal?

## basis

docs/research-encoding-consequences.md Theorem 3.7 proves P/log via t_L = max{n : n+S(n) <= L}; the ledger records no constant-advice result or lower bound for this cutoff.

## falsifier

Construct an explicit P/O(1) machine deciding every instance, or prove an omega(1) advice lower bound for the cutoff sequence t_L on an infinite set of input lengths.

## implication

P/O(1) membership would strengthen the proven P/log bound for unary SORT-BOUND-U; an omega(1) lower bound would show the monotone cutoff is a genuine advice resource that no uniform rule compresses.

## finding_unverified

hed, not written out in full. The corresponding \(G(n)=a_n-n\) is monotone with \(G(n)=\Theta(n\log n)\).

Consequence: no proof of \(U\in P/O(1)\) can rely only on the monotone threshold representation, the known \(P/log\) cutoff, or the growth class of \(t_L\); it must use arithmetic information specific to \(S\).

## Failed approaches / honest limits

- No explicit \(P/O(1)\) machine was found.
- No \(\omega(1)\) lower bound was found; by the obstruction above, it would prove \(P\ne PSPACE\).
- The tempting consequence \(U\in P/O(1)\Rightarrow S\in FP/log\) is vacuous: every polynomial-growth unary function is in \(FP/log\), since the advice can be \(S(n)\) itself in \(O(\log n)\) bits.
- \(t_L\) is not eventually periodic (that would make \(S\) eventually linear, contradicting \(S(n)=\Theta(n\log n)\)), but \(P/O(1)\) is far larger than eventually periodic, so this does not settle the front.
- General-poset hardness and certificate soundness do not transfer to this advice question.

## Status

The front is open, with a sharp asymmetry: the lower-bound horn is blocked by a \(P\ne PSPACE\)-level implication, while the upper-bound horn is a genuine nonuniform compression question with no known construction or lower bound. This is an exact obstruction, not a proof of either horn.
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

## Other metadata

```json
{
  "finished_at": 1794175840.3412256,
  "started_at": 1794175270.4996798
}
```
