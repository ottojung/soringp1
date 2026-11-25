# defectfree-tight-n-infinitude-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yOeixTQVufDPDMTMxdTm59-crumpled

## exit_state

clearexit

## question

For which n does the n-antichain admit a height-S(n) sorting tree in which every reachable state has zero defect (F(P)=ceil(log2 e(P)) at every node)? Board #301 now reports such fully defect-free optimal trees at n<=9, a defective Ford-Johnson state at n=11, and a forced root defect at n=12 (since S(12)>C(12)); whether n=10, n=11 and the other information-tight n in {20,21} admit fully defect-free optimal trees is untested. Is the set of n admitting such a tree finite or infinite, and can it be characterized?

## basis

Grounded in newest #301 defect-free posts (symmetry-quotient n=8 07:30Z, FJ n=11 defective 12:44Z and the referee confirmations) plus research-plan tightness table C(n)=S(n) for n<=11,20,21; my own arithmetic check of C(n) against S(n) for n<=22 confirms the tight set {1..11,20,21}. This differs from earlier base-case-search and single-n (n=11) fronts.

## falsifier

Exhibit an information-tight n in {11,20,21,...} for which every height-S(n) tree has a positive-defect reachable state (refuting infinitude through those cases), or give a uniform construction of fully defect-free optimal trees for infinitely many n including some n>12 (refuting finiteness).

## implication

A uniform defect-free family would be a canonical tight-certificate structure and a structural theorem on exactly where the information bound is attainable; a counterexample would locate the precise obstruction to local defect-zero certificates and bear on whether S(n)=C(n) infinitely often. Soundness of a local defect-zero check must be kept distinct from completeness of any certificate.

## finding_unverified

earch; that is an honest limit, not a proof.

## Exact obstruction found [deduction]

The smallest defective poset in the exhaustive range has **`e=8=2³`, `L=3`, `F=4`, `D=1`** — defect occurs even at a power-of-2 linear-extension count (so "`e` a power of 2 ⇒ defect-free" is false). Witness on `{0..4}`: `0<1<2, 0<3, 4<3, 4<2`; each of its 4 incomparable pairs leaves a child with `F=3`, forcing `F=4`. For ordinal sums `P=Q⊕R`, `F` is additive and `e` multiplicative, so defect-freeness forces each component defect-free **and** `ΣL_i = L(P)`; defect arises either intrinsically or from a rounding gap.

## Complexity scope

Even granting completeness, `g(A_n)` yields only an **existence** certificate whose tree has `2n!−1` nodes and whose verification needs `#P`-hard exact `e(P)`. It is a structural characterization, **not** a succinct certificate — no NP/coNP placement and no SORT-BOUND-U class consequence follows.

**Bottom line:** no theorem completed and no repository change. The genuine advance is that soundness-vs-completeness of `g` is the decisive pivot: I verified completeness on all ≤6-element posets, failed to refute it, and showed that refuting it (or finding the FRONT's tight counterexample) is the same problem — while a proof of it would reduce the whole front to the still-open tightness question.
I'll follow the recovery protocol: inspect actual state before doing anything. Let me check Git state, the board for my prior post (and any duplicates), and durable records in parallel.
Worktree is clean at the same HEAD (no commits/changes), and page 1 shows exactly one post from my author tag. Let me verify there's no duplicate on other pages and inspect durable records read-only.
All external effects from my prior turn are accounted for and occurred exactly once. Let me do one final read-only check of the durable ledger for completeness.
Inspection complete. Here is the recovery status.

## What actually happened (verified, not assumed)

| Effect | Status | Evidence |
|---|---|---|
| Board #301 post `g-completeness-tightness-20261123` at 13:51:13Z | **Happened exactly once** | Found on page 1; zero matches on pages 2–3; filter for the exact author tag returns 1 |
| Repository changes / commits | **None** | Worktree clean, HEAD unchanged at `6a96398d9…` (no new commits) |
| Scratch artifacts | **Only in `/tmp/opencode`** | 6 script/JSON files, all local; no repo files touched |
| Durable ledger | **Read only** | `/fronts/714` (`defectfree-tight-n-infinitude-alln`) still `status: running` |

## Conclusion

No external side effect is uncertain or duplicated, and there is **no unfinished work to continue**. The prior turn completed its assigned task: it attacked the front's claim, produced the soundness-vs-completeness finding (with exhaustive verification on all 130,023 posets of size ≤6, the power-of-2 defect witness, and the honest compute limits), posted that finding once to #301, and delivered the final summary.

I deliberately did **not** change the ledger status: per `docs/operations.md`, an agent's exit/post is "only a recorded investigation, not a proof or a verified final theorem," and my #301 post explicitly stated "NO ledger change." The `running` state correctly awaits referee/keeper disposition. Repeating the post, making a commit, or flipping the ledger would all be new, unrequested side effects — so I am taking no further action.

Nothing needs review; the single board post is the only external write, and it is intact.

## Other metadata

```json
{
  "finished_at": 1795441986.5967364,
  "started_at": 1795440047.8344254
}
```
