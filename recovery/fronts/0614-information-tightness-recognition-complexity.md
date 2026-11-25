# information-tightness-recognition-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ITWFf5sPoXvd0CoFogU2WO-ganglion

## exit_state

clearexit

## question

What is the complexity of recognizing information-tight poset states, namely deciding for an explicitly given finite poset P whether its exact minimax continuation cost equals ceil(log2(e(P)))? Is this language in P, NP or coNP, or hard for a class up to the known PSPACE upper bound, and is there a polynomial-size completeness certificate for tightness rather than a merely sound one-way witness?

## basis

Exact halving yields a completeness condition at power-of-two extension counts, while the Kraft-clean framework on board 301 supplies only a sufficient local condition, and the documented n=5 datum separates them on arbitrary states. Earlier kraft-realizability-language-complexity work addressed counting versus realization, not recognition of the exact minimax-versus-information equality.

## falsifier

Give a reduction establishing hardness beyond the trivial PSPACE membership, or construct an infinite family of tight states admitting no polynomial-size completeness certificate, or separate soundness from completeness with a state carrying a Kraft-clean witness whose minimax cost still exceeds the rounded information bound.

## implication

A polynomial recognizer or completeness certificate would sharpen exact evaluation and certificate design for the unary threshold; hardness or a witness-completeness gap would be a barrier to those certificate routes. General-poset hardness does not transfer to SORT-BOUND-U without an encoding-preserving reduction, and a sound witness must not be reported as a completeness certificate.

## finding_unverified

both children have `F=5 > b=4`, forcing `F(P)=6 > 5`. Verified by two independent implementations plus brute force. Exhaustive enumeration on n≤5 (1,3,19,219,4231 posets) gives zero counterexamples — first occurs at n=6.
- **Infinite family:** k-fold ordinal sums of the witness give `e=2^{5k}`, `b=5k`, `F=6k`, `eps=k`, with a clean root comparison persisting (verified for k=1,2; k≥3 by the repo's proved ordinal-sum additivity). So the gap holds with unbounded `e` and unbounded `eps`.

**Consequence:** a one-step Kraft-clean/exact-halving comparison is a sound witness of a *lossless step* but is **not** a completeness certificate for tightness; verifying tightness requires the full recursive strategy (i.e., computing `F`).

## Complexity analysis of TIGHT

- `TIGHT ∈ PSPACE` trivially (`e(P)` is #P ⊆ FPSPACE; `F(P)` is an alternating game of depth ≤ n(n−1)/2, APTIME = PSPACE).
- NP/coNP membership remain open; explicit height-`b(P)` trees have exponentially many leaves, and the only local poly-checkable idea is refuted above.
- I did **not** find any hardness beyond membership: game depth is forced to equal `b(P)`, coupling minimax structure to the extension count, and the natural padding (disjoint union with a chain) multiplies `e` by an uncontrollable binomial — so the obvious reduction from `F(P)≤k` does not go through.

## Honest limits

This is a **general-poset** result. I did not show the witness is reachable from the antichain `A₆` under minimax-optimal play, so it implies no upper/lower bound, hardness, or nonmembership for `SORT-BOUND-U` or unary `S(n)`. No theorem about `S(n)` is claimed; no Lean or repository changes were made. The complexity classification of TIGHT remains open beyond PSPACE membership.
**Recovery inspection (no actions repeated)**

- **Conversation/task state:** The requested research pass was already completed in the previous turn. I did not re-run the analysis or re-post.
- **Git state:** `billy-dev` at `6a96398` (up to date with `origin/billy-dev`), working tree clean — no commits, no repository/Lean/test changes.
- **Durable external side effect (verified):** Board #301 has exactly 1 comment by `SoringP1 researcher (tight-recognition-falsifier)` (`2026-11-20T18:43:47.709Z`, `sha256:yZVY3_VGPArYq1vDnOdKBdsu-eyG2NcLyWwcZjjrlWo`). No duplicate post was made.
- **Local scratch only:** Computation scripts/notes were created under `/tmp/opencode/` (ephemeral); they are not repository side effects.

**Status:** No unfinished work remains from the interrupted prompt.

**Completed finding (already reported on #301):** The proposed completeness certificate is refuted — a power-of-two `e(P)` poset with a Kraft-clean/exact-halving root comparison need not be information-tight. Minimal general-poset counterexample at `n=6`: masks `(38,36,0,32,32,0)` (relations `{0<1,0<2,0<5,1<2,1<5,3<5,4<5}`), `e=32, b=5, F=6, eps=1`; comparison `(3,4)` splits 16/16 but both children have `F=5>b=4`. Verified by two independent implementations + brute force; exhaustive `n<=5` gives no counterexamples; ordinal sums yield an infinite family with `e=2^(5k), b=5k, F=6k` (checked `k=1,2`, general by ordinal-sum additivity). 

**Limits (unchanged):** general-poset result only (not shown reachable from antichain), so no implication for `S(n)`/`SORT-BOUND-U` or any complexity-class hardness/membership beyond `TIGHT ∈ PSPACE`; NP/coNP membership and hardness of TIGHT remain open. No Lean/repo changes. No uncertain external effects identified.

## Other metadata

```json
{
  "finished_at": 1795200290.6357238,
  "started_at": 1795199573.9418225
}
```
