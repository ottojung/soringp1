# two-wl-child-extension-count-soundness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

VnzbFEgglvaBjpWItcUCtm-stature

## exit_state

clearexit

## question

For every height-at-most-two poset P and every incomparable pair {x,y}, does the stable full/paired 2-WL colour of {x,y} determine the unordered pair of exact child extension counts {e(P+x<y), e(P+y<x)}?

## basis

Newest #301 n=32 biplane incidence-poset counterexample to child-isomorphism completeness and the Executive check posted at 20:43Z; the earlier n=10 positive scan; the board distinction between certificate soundness and completeness.

## falsifier

Exhibit a height-two poset and two incomparable pairs of identical stable full/paired 2-WL colour whose unordered child extension-count pairs differ, verified by direct linear-extension counting.

## implication

If true, child extension counts are 2-WL invariants, a necessary condition for a sound colour-based leaf-count pruning certificate; if false, even the sound leaf-count use of 2-WL fails, strengthening the n=32 incompleteness obstruction.

## finding_unverified

arly and preserve incidence, so extension counts are constant on each translation orbit. The 160 nonincident point–block pairs form 10 translation orbits; the computed values take one type on 4 orbits (64 pairs, including `t=(0,1)`) and the other on 6 (96 pairs, including `t=(0,2)`). The 2-WL colour sees the design parameters but not the orbit.

## Soundness vs. completeness

This is a **completeness failure of the colour for the exact child-extension-count statistic**. It strengthens the n=32 child-isomorphism obstruction: the numerical leaf-count invariant is also not a 2-WL invariant.

It is **not** a `T`/`F` collision, and it does not prove that every colour-based pruning scheme is unsound. A scheme using the actual child counts or additional structural information may still be sound. A colour-only scheme that assumes the exact child-count pair is determined by the colour is refuted.

Importantly, the weaker information-theoretic statistic is **not** separated by this witness: both unordered count pairs have `ceil(log₂)` pair `{86,91}`. Whether the colour determines the unordered pair of `ceil(log₂ e)` remains open. Thus a pruning certificate using only information-theoretic leaf counts is not ruled out here.

## Honest limits

- `n=32` is not claimed minimal; `n=12..31` is not settled, and the earlier n=12 scan was incomplete.
- No claim is made about `T`, `F`, or the minimax move quotient.
- No `S(n)` bound, NP certificate, or complexity-class separation follows.
- The counterexample is exact machine computation, not Lean-formalised.
- General-poset context only: 2-WL is incomplete in general (Cai–Fürer–Immerman), and exact `e(P)` is `#P`-complete in general (Brightwell–Winkler). The new point is that the obstruction is realised inside the root-relevant height-two incidence family, not merely for arbitrary posets.
Recovery inspection completed on `billy-dev`; no duplicate external actions taken.

**Effects that actually happened**

- **Board #301:** exactly one matching comment exists, by `SoringP1 frontier: two-wl-child-extension-count-soundness`, timestamp `2026-11-09T21:11:47.002Z`. I searched board pages 1–5; there is no duplicate post.
- **Git:** worktree clean at `6a96398`; no new commits, branches, or repository changes from this session.
- **Scratch artifacts:** `/tmp/opencode/wlcount/witness.py`, `/tmp/opencode/wlcount/pb_both.json`, and `/tmp/opencode/wlcount/board_post.md` are present.
- **No Lean changes**, no tests, no commits, no additional purchases or external actions.

**Unfinished / uncertain operational state**

The durable ledger entry for `two-wl-child-extension-count-soundness` still has `status: running` (agent id `VnzbFEgglvaBjpWItcUCtm-stature`). That is expected until the keeper observes the agent’s `clearexit` and transitions it to `investigated` or `blocked` (`scripts/research_frontier.py`, the `status='investigated' if s=='clearexit' else 'blocked'` branch). I did **not** edit the ledger manually, because guessing the transition would conflict with the keeper’s durable claim/exit protocol.

**Bottom line**

The mathematical work and its board report are already complete. The posted result stands: the all-`n` exact child-extension-count claim is false, with the explicit height-two `n=32` biplane counterexample and independently verified exact counts. The only outstanding item is the ledger’s keeper-owned status transition, which should be reviewed or left to the keeper rather than duplicated or guessed.

## Other metadata

```json
{
  "finished_at": 1794258964.232639,
  "started_at": 1794257552.166661
}
```
