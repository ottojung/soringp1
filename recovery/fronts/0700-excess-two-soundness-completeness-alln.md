# excess-two-soundness-completeness-alln

## status

blocked

## origin

ai_proposal_unverified

## agent_id

MMhGvyoDt9ESUXIGso48hD-murmur

## exit_state

failed

## question

For the width-2 excess band, does soundness alone suffice: is there a sound (no false accepts) O(1)-size certifier for SORT-BOUND-U near D(n) <= 2, and is it necessarily incomplete without computing the per-n slack D(n)?

## basis

excess-gap-two-alln and excess-two-realization-alln set the scene; free-free-second-state-tightness-alln (sound gap-2 states via D(FF_n) >= excess_S(n)); Merge(6,10) certified gap 2 (research-structural-lower-bounds.md) is a general-poset result that does not transfer to the antichain root, where D(16)=1; excess-band-diagonal-decision-alln finding 1 (BAND_c equivalence); problem.md: e(P) is #P-complete, minimax identification is the game; AGENTS.md: distinguish soundness from completeness; general-poset results do not transfer without an encoding-preserving reduction.

## falsifier

Exhibit a sound and complete O(1)-size certifier family deciding D(n) in {0,1,2} without evaluating S(n), or prove that every sound O(1)-certifier of the band is incomplete (must query the minimax value for some input).

## implication

Soundness alone is already achievable by the 3-probe scheme (k >= C(n)+2 -> accept; k < C(n) -> reject; k in {C(n),C(n)+1} -> unverifiable-without-D) - that scheme is sound but incomplete; completeness (deciding the unverifiable cases) requires computing D(n), which is the minimax identification problem (#P-hard for general posets; the free-free theorem gives sound gap-2 states but no decision procedure). This front isolates the completeness gap as the central obstruction, distinct from general-poset lower bounds.

## finding_unverified

I'm already on billy-dev (the worktree list shows this directory at `[billy-dev]`). Now let me study `docs/problem.md`, the research board (#301), and the relevant research docs.
I'm on billy-dev. Now let me pull the board #301 digest and find the research docs the user referenced.

## Other metadata

```json
{
  "finished_at": 1795397690.0596335,
  "started_at": 1795397627.1197886
}
```
