# prime-height-three-excess-one

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4JWEeDe1U0iopQQ0Hg6AeM-numerous

## exit_state

clearexit

## question

For every finite poset P of height at most three that is neither an ordinal sum nor a disjoint union of two nonempty posets, is the information excess F(P)-ceil(log2 e(P)) at most 1?

## basis

Board #301 2026-11-09T21:57Z height-three-excess-root-equivalence and the 22:00Z Executive check: series additivity and parallel binomial entropy force any separation to come from a prime height-three poset; exhaustive labelled checks through n=7 found excess at most 1, attained only at height two.

## falsifier

Exhibit an ordinal-sum- and disjoint-union-indecomposable height-three poset with exact information excess at least 2, with independently computed exact minimax height and exact linear-extension count.

## implication

A proof would confine any height-three excess above the antichain value E(n) to the already-studied series and parallel compositions; a counterexample would be a prime local amplifier not reducible to E(n) by the verified composition lemmas.

## finding_unverified

The assertion itself was misindexed (`range(b,n)` isn't the B block); the check intent is: no relations out of `x`, none within B. Fixing the check:
`minimax` takes the succ tuple directly, not extension lists. Simplifying the sanity check:
All checks pass — the counterexample is complete and unconditional. Now let me check the posting procedure and confirm nothing for this front is already on the board:
No post for this front exists yet. Let me find the posting mechanism:
The counterexample is verified. Posting the falsification to board #301 (JSON output redirected to a file per ops doc):
The JSON output looks like it echoed the issue description; let me verify the comment was actually appended:
The post went through (the JSON includes the full issue; my comment is in `messages`). Confirming via the digest:
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

## Other metadata

```json
{
  "finished_at": 1794271625.6805708,
  "started_at": 1794266029.948583
}
```
