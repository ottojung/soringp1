# antonina-4JWEeDe1U0iopQQ0Hg6AeM-numerous

Session: ses_e3d691b8bffe8cKAdXXQoMSrKJ
Workspace: /home/lubko/soring-fronts/prime-height-three-excess-one
Created: 1794266031432; updated: 1794271600155

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 482 (msg_1c2ea3906001hgHZYsw2bQxsjY)

I'm resuming after the interruption. State assessment: no post to board #301 exists for this front (`--contains "prime-height-three-excess-one"` returned 0 matches), the worktree is clean at `6a96398`, and all scratch work is in `/tmp/opencode/primeh3`. One background probe (`canQ 3 12 33`) is still running but is **not needed** for the main result — the counterexample is already established by monotonicity alone. Let me do one consolidated, independent re-verification of the falsifier before reporting.

## Output 494 (msg_1c2ea92e20013ljxMVlgQnnxOX)

The assertion itself was misindexed (`range(b,n)` isn't the B block); the check intent is: no relations out of `x`, none within B. Fixing the check:

## Output 521 (msg_1c2eab474001B7Nqtub4k0ZJ8z)

`minimax` takes the succ tuple directly, not extension lists. Simplifying the sanity check:

## Output 541 (msg_1c2eadc560015kFf7iLou5eh3J)

All checks pass — the counterexample is complete and unconditional. Now let me check the posting procedure and confirm nothing for this front is already on the board:

## Output 556 (msg_1c2eaf4c8001EtPiHvBGi8vri1)

No post for this front exists yet. Let me find the posting mechanism:

## Output 581 (msg_1c2eb0e53001EhDQsZY0sDVTxQ)

The counterexample is verified. Posting the falsification to board #301 (JSON output redirected to a file per ops doc):

## Output 592 (msg_1c2eba6a0001bLHev46hJF1aWu)

The JSON output looks like it echoed the issue description; let me verify the comment was actually appended:

## Output 603 (msg_1c2ebb241001BQTg16uBPE7Zck)

The post went through (the JSON includes the full issue; my comment is in `messages`). Confirming via the digest:

## Output 623 (msg_1c2ebcca60019PHa262rXOgGQe)

Done. Final report:

## Result: the front's conjecture is FALSE

**Falsifier (all criteria met):** a poset `Q` on **n = 19**, height exactly 3, prime with respect to *both* decompositions (comparability graph connected ⇒ not a disjoint union; incomparability graph connected ⇒ not an ordinal sum), with information excess ≥ 2:

- **Construction:** layers A = {a₀,a₁,a₂}, B = {b₀,…,b₁₄}, x; relations: all A < B except (a₀,b₀); all A < x; all B < x except (b₁,x).
- **Exact count** (bitmask DP, re-derived twice): `e(Q) = 1374·13! = 8,555,926,579,200`, so `ceil(log₂ e) = 43`.
- **Lower bound** (paper-level, no computation needed): adding back the two deleted relations gives exactly the ordinal sum `A₃ (+) A₁₅ (+) 1`, so `F(K) = S(3)+S(15)+S(1) = 3+42+0 = 45`. Since `Q ⊆ K`, monotonicity gives `F(Q) ≥ 45` — monotonicity was additionally verified exhaustively for all one-relation augmentations with n ≤ 5.
- **Excess ≥ 45 − 43 = 2**, unconditionally (exact F not needed).

**Bonus:** the same one-relation-deletion mechanism already breaks excess ≤ 1 at **height 2**: `P = A₃ (+) A₁₄` minus cross relation (a₀,b₀), n = 17, prime, `e = 86·13!`, `ceil(log₂ e) = 39`, and an explicit strategy pins `F(P) = 41` exactly, so **excess = 2**.

**Moral:** the S-value overshoot `d(a,b) = S(a)+S(b) − ceil(log₂ a!b!)` of the underlying two-antichain product survives as excess of the prime poset, because deleting one cross relation barely changes `e` (~factor 1/ab) while dropping F by at most 1. Small-n enumeration (n ≤ 7) couldn't see this; first counterexamples at n = 17 (height 2) and n = 19 (height 3).

**Delivered:** one board post to #301 (00:46Z, confirmed present exactly once — no duplication from the interrupted turn). No commits, no repo/Lean changes, worktree clean at `6a96398`. The leftover background probe (`canQ 3 12 33`) was killed by the interruption and is not needed for the result.
